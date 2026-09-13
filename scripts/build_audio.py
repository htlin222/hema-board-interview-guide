#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["edge-tts>=6.1"]
# ///
"""把逐字稿合成成有聲書，一章一個 mp3。

先跑 build_transcript.py 產生 dist-audio/<slug>.jsonl，這裡只負責合成與拼接。

為什麼要分段合成再拼：
  edge-tts 一次請求只能用一個 voice，但內容是中英夾雜的。中文語音唸
  "intrinsic pathway" 會走音，英文語音唸中文更慘，所以照語言切段、各用各的
  聲音，最後用 ffmpeg 接起來。

實測過的重點（scripts/build_transcript.py 有對應的處理）：
  edge-tts 不會自動把大寫縮寫逐字母唸——"CRAB" 和 "crab" 的音訊長度一模一樣
  （都是 0.82 秒），要加空格變成 "C R A B" 才會逐字母（1.49 秒）。

用法：
    uv run --script scripts/build_audio.py              # 全部章節
    uv run --script scripts/build_audio.py itp          # 只做指定章節
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import pathlib
import subprocess
import sys

import edge_tts

ROOT = pathlib.Path(__file__).resolve().parent.parent
AUDIO = ROOT / "dist-audio"
CACHE = AUDIO / ".cache"

VOICES = {"zh": "zh-TW-YunJheNeural", "en": "en-US-AndrewNeural"}
RATE = {"zh": "+8%", "en": "+0%"}  # 中文稍快，跟英文段落的語速比較接近
CONCURRENCY = 6  # 再高會被 Edge 的端點限流


# 快取版本：處理方式改變時要跟著改，否則會沿用舊的（未修剪的）片段
CACHE_VER = "v2-trim"

# 每個 edge-tts 片段前後都帶著靜音，幾千段拼起來會累積成大量空白
# （未修剪前實測：一章 18.7 分鐘裡有 37% 是靜音）。在進快取前就把兩端修掉，
# 讓成品裡的停頓只來自我們自己插入的那幾種長度。
TRIM = (
    "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02:detection=peak,"
    "areverse,"
    "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02:detection=peak,"
    "areverse"
)


def key_of(seg: dict) -> str:
    h = hashlib.sha256(
        f"{CACHE_VER}|{seg['lang']}|{VOICES[seg['lang']]}|{RATE[seg['lang']]}|{seg['text']}".encode()
    ).hexdigest()[:20]
    return h


async def synth_one(seg: dict, sem: asyncio.Semaphore) -> pathlib.Path:
    path = CACHE / f"{key_of(seg)}.mp3"
    if path.exists() and path.stat().st_size > 0:
        return path
    async with sem:
        last = None
        for attempt in range(5):
            try:
                raw = path.with_suffix(".raw.mp3")
                c = edge_tts.Communicate(
                    seg["text"], VOICES[seg["lang"]], rate=RATE[seg["lang"]]
                )
                await c.save(str(raw))
                if raw.stat().st_size > 0:
                    await asyncio.to_thread(
                        subprocess.run,
                        ["ffmpeg", "-y", "-i", str(raw), "-af", TRIM, "-q:a", "5", str(path)],
                        check=True, capture_output=True,
                    )
                    raw.unlink(missing_ok=True)
                    if path.exists() and path.stat().st_size > 0:
                        return path
                last = "檔案為空"
            except Exception as e:  # noqa: BLE001
                last = f"{type(e).__name__}: {e}"
            # 被限流時要退避夠久，否則只是繼續撞牆
            await asyncio.sleep(2 ** attempt + 0.5)
        path.unlink(missing_ok=True)
        raise RuntimeError(f"合成失敗（{last}）：{seg['text'][:40]}")


def silence(ms: int) -> pathlib.Path:
    p = CACHE / f"sil{ms}.mp3"
    if not p.exists():
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
             "-t", f"{ms / 1000}", "-q:a", "9", str(p)],
            check=True, capture_output=True,
        )
    return p


async def build_chapter(slug: str, n: int, total: int) -> None:
    segs = [json.loads(ln) for ln in (AUDIO / f"{slug}.jsonl").read_text().splitlines() if ln]
    sem = asyncio.Semaphore(CONCURRENCY)

    done = 0

    async def run(s: dict) -> pathlib.Path:
        nonlocal done
        p = await synth_one(s, sem)
        done += 1
        if done % 100 == 0:
            print(f"    {done}/{len(segs)}", flush=True)
        return p

    parts = await asyncio.gather(*(run(s) for s in segs))

    lines = []
    for seg, p in zip(segs, parts):
        lines.append(f"file '{p}'")
        if seg.get("pause"):
            lines.append(f"file '{silence(seg['pause'])}'")
    listing = CACHE / f"{slug}.txt"
    listing.write_text("\n".join(lines), encoding="utf-8")

    out = AUDIO / f"{n:02d}-{slug}.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
         "-c:a", "libmp3lame", "-b:a", "64k", "-ar", "24000", "-ac", "1", str(out)],
        check=True, capture_output=True,
    )
    dur = float(
        subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(out)],
            capture_output=True, text=True,
        ).stdout.strip()
    )
    size = out.stat().st_size // 1024
    print(f"[{n}/{total}] {slug:30s} {len(segs):4d} 段  {dur / 60:5.1f} 分  {size:5d} KB")


async def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    files = sorted(AUDIO.glob("*.jsonl"))
    if not files:
        print("找不到逐字稿，先跑 build_transcript.py", file=sys.stderr)
        return 1

    import re

    topics = ROOT / "src" / "content" / "docs" / "topics"

    def sidebar_order(slug: str) -> int:
        m = re.search(r"order:\s*(\d+)", (topics / f"{slug}.md").read_text(encoding="utf-8"))
        return int(m.group(1)) if m else 99

    # 章號要用全站章序算，不能用篩選後的位置——否則單獨重建某一章時，
    # 檔名會變成 01-itp.mp3 而不是它真正的章號。
    all_slugs = sorted((f.stem for f in files), key=sidebar_order)
    numbers = {s: i for i, s in enumerate(all_slugs, 1)}

    only = sys.argv[1:]
    slugs = [s for s in all_slugs if not only or s in only]
    if not slugs:
        print(f"找不到章節：{only}", file=sys.stderr)
        return 1

    for slug in slugs:
        await build_chapter(slug, numbers[slug], len(all_slugs))

    total = sum(
        float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
            capture_output=True, text=True).stdout.strip() or 0)
        for p in AUDIO.glob("*.mp3")
    )
    print(f"\n合計 {total / 60:.0f} 分鐘（{total / 3600:.1f} 小時）→ {AUDIO.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
