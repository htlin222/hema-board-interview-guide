#!/usr/bin/env python3
"""重新驗證站上每一支 YouTube 影片連結是否仍然存在且可嵌入。

做法沿用 curate-course 的原則：**不信任任何上游宣稱**（包含當初策展時
自稱驗證過的紀錄），每次都直接對 YouTube oEmbed API 重打一次。oEmbed 回
200 才算數——「能播」不等於「能嵌入」，而影片被下架、轉私人、地區封鎖時
oEmbed 會直接回 401/403/404。

用法：
    npm run build && python3 scripts/verify-videos.py          # 驗證產物
    python3 scripts/verify-videos.py --source                  # 驗證原始 md
    python3 scripts/verify-videos.py --json                    # 給 agent 讀

離開碼：有任何一支失效就是 1，可以直接放進 CI。
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist" / "topics"
DOCS = ROOT / "src" / "content" / "docs" / "topics"
OEMBED = "https://www.youtube.com/oembed?url={}&format=json"
VIDEO_RE = re.compile(r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})")


def collect(source: bool) -> dict[str, set[str]]:
    """回傳 {video_id: {出現的檔名}}。"""
    if source:
        files = sorted(DOCS.glob("*.md"))
        label = lambda p: p.name  # noqa: E731
    else:
        files = sorted(DIST.glob("*/index.html"))
        label = lambda p: p.parent.name  # noqa: E731

    if not files:
        where = "原始 markdown" if source else "dist/（先跑 npm run build）"
        print(f"找不到任何檔案：{where}", file=sys.stderr)
        sys.exit(2)

    found: dict[str, set[str]] = {}
    for path in files:
        for vid in VIDEO_RE.findall(path.read_text(encoding="utf-8")):
            found.setdefault(vid, set()).add(label(path))
    return found


def check(vid: str) -> tuple[str, bool, str]:
    url = OEMBED.format(urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe=""))
    req = urllib.request.Request(url, headers={"User-Agent": "verify-videos/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
        return vid, True, f"{data.get('title', '?')} :: {data.get('author_name', '?')}"
    except urllib.error.HTTPError as exc:
        return vid, False, f"HTTP {exc.code}（影片可能已下架、轉私人或禁止嵌入）"
    except Exception as exc:  # noqa: BLE001
        return vid, False, f"{type(exc).__name__}: {exc}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", action="store_true", help="驗證原始 markdown 而非 dist 產物")
    ap.add_argument("--json", action="store_true", help="輸出 JSON")
    args = ap.parse_args()

    found = collect(args.source)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, sorted(found)))

    dead = [(v, m) for v, ok, m in results if not ok]

    if args.json:
        print(
            json.dumps(
                {
                    "total": len(results),
                    "ok": len(results) - len(dead),
                    "dead": [
                        {"id": v, "reason": m, "pages": sorted(found[v])} for v, m in dead
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for vid, ok, msg in results:
            mark = "OK  " if ok else "FAIL"
            print(f"{mark} {vid}  {msg}")
        print(f"\n合計 {len(results)} 支，失效 {len(dead)} 支")
        for vid, msg in dead:
            print(f"  ✗ {vid} — {msg}（出現在：{', '.join(sorted(found[vid]))}）")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
