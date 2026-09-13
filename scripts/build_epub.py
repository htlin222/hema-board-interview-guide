#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10.0"]
# ///
"""把主題頁打包成 Kindle 相容的 EPUB。

設計取向：極簡、黑白、巢狀目錄（章 → 節）。

Kindle 的轉檔器會丟掉不少東西，所以這裡刻意不用網站上的那套呈現：
- 行內 SVG 圖示全部移除（Kindle 不保證渲染 SVG，留著只會變成破圖或空白）
- callout 的 <div> 改寫成 blockquote，這是各家閱讀器都穩的結構
- 不用 CSS 變數、flex、grid；只用最基本的邊框與間距

用法：
    uv run --script scripts/build_epub.py
"""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPICS = ROOT / "src" / "content" / "docs" / "topics"
OUT_DIR = ROOT / "dist-epub"
OUT_FILE = OUT_DIR / "hema-board-interview.epub"  # ASCII：GitHub Release 會改掉 CJK 檔名

TITLE = "血液科口試走向指南"
SUBTITLE = "推理架構 × 破題關鍵句 × 擬答 × 追問"
SITE = "https://htlin222.github.io/hema-board-interview-guide"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"

CSS = """
html { font-size: 100%; }
body { margin: 0 0.6em; line-height: 1.6; text-align: justify; }
h1 { font-size: 1.45em; margin: 1.2em 0 0.7em; page-break-before: always; line-height: 1.35; }
h2 { font-size: 1.12em; margin: 1.4em 0 0.5em; border-bottom: 1px solid #999; padding-bottom: 0.15em; }
h3 { font-size: 1em; margin: 1.1em 0 0.4em; }
p { margin: 0.45em 0; }
ul, ol { margin: 0.45em 0; padding-left: 1.3em; }
li { margin: 0.25em 0; }
blockquote {
  margin: 0.7em 0; padding: 0.1em 0 0.1em 0.8em;
  border-left: 3px solid #666; font-style: normal;
}
blockquote p { margin: 0.3em 0; }
.label { font-weight: bold; }
table {
  border-collapse: collapse; width: 100%;
  margin: 0.7em 0; font-size: 0.82em; page-break-inside: avoid;
}
th, td { border: 1px solid #999; padding: 0.3em 0.4em; text-align: left; vertical-align: top; }
th { font-weight: bold; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1.4em 0; }
.frontmatter { text-align: left; }
.frontmatter h1 { page-break-before: avoid; }
"""


def make_cover(path: pathlib.Path) -> None:
    """直式封面（1600×2560，Kindle 建議比例）。標誌沿用站台的血滴＋羅盤。"""
    S = 2
    W, H = 800 * S, 1280 * S
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)

    def droplet(cx, cy, r):
        import math

        m, n = 1.35, 240
        raw = [
            (math.sin(t) * (math.sin(t / 2) ** m), -math.cos(t))
            for t in (2 * math.pi * i / n for i in range(n))
        ]
        hw = max(abs(x) for x, _ in raw)
        yb = next(y for x, y in raw if abs(abs(x) - hw) < 1e-9)
        k = r / hw
        d.polygon([(cx + x * k, cy + (y - yb) * k) for x, y in raw], fill="black")

    def needle(cx, cy, r):
        import math

        q = math.sqrt(0.5)
        tip, waist = r, r * 0.3
        d.polygon(
            [
                (cx + tip * q, cy - tip * q),
                (cx + waist * q, cy + waist * q),
                (cx - tip * q, cy + tip * q),
                (cx - waist * q, cy - waist * q),
            ],
            fill="white",
        )

    mr = 92 * S
    droplet(W // 2, 420 * S, mr)
    needle(W // 2, 420 * S, mr * 0.78)

    def centered(text, y, size):
        f = ImageFont.truetype(FONT, size)
        w = d.textbbox((0, 0), text, font=f)[2]
        d.text(((W - w) / 2, y), text, font=f, fill="black")

    centered(TITLE, 660 * S, 64 * S)
    d.rectangle([W / 2 - 110 * S, 770 * S, W / 2 + 110 * S, 770 * S + 2 * S], fill="black")
    centered(SUBTITLE, 820 * S, 27 * S)
    centered("整理歷屆考生口試心得，去名化後只保留考試走向", 1120 * S, 22 * S)
    centered("htlin222.github.io/hema-board-interview-guide", 1180 * S, 19 * S)

    img.resize((800, 1280), Image.LANCZOS).save(path)


WARN_SVG = re.compile(r'<svg class="icon-inline icon-warning"[\s\S]*?</svg>\s*')
ANY_SVG = re.compile(r"<svg[\s\S]*?</svg>\s*")
CALLOUT = re.compile(
    r'<div class="callout callout-(keywords|followup)">\s*'
    r'<div class="callout-title">[\s\S]*?</div>'
    # 標題與內文之間有沒有空行，各頁寫法不一致（編號清單那兩頁沒有），所以只要求換行
    r"\s*\n\s*"
    r"([\s\S]*?)"
    r"\n\s*</div>"
)


def to_blockquote(m: re.Match[str]) -> str:
    """callout <div> → blockquote。Kindle 對 div+border 支援不一，blockquote 穩。"""
    label = "破題關鍵句" if m.group(1) == "keywords" else "追問"
    body = ANY_SVG.sub("", m.group(2)).strip()
    lines = [f"**{label}**", ""]
    lines += [ln.strip() for ln in body.split("\n")]
    return "\n" + "\n".join(f"> {ln}".rstrip() for ln in lines) + "\n"


SITE_LINK = re.compile(r"\]\(/hema-board-interview-guide/topics/([a-z0-9-]+)/?\)")


def convert(md: str) -> str:
    # 站內跨頁連結 → 書內跳轉（EPUB 裡原本的絕對路徑是壞的參照）
    md = SITE_LINK.sub(r"](#ch-\1)", md)
    md = CALLOUT.sub(to_blockquote, md)
    md = WARN_SVG.sub("**注意**：", md)  # 站上是警示圖示；紙本/電子書用文字標示
    md = ANY_SVG.sub("", md)
    # 影片段落整段拿掉：離線閱讀時一串 YouTube 連結沒有意義
    md = re.split(r"\n##\s*相關 YouTube 影片", md)[0]
    return md.rstrip() + "\n"


def front_matter(raw: str, slug: str) -> tuple[str, int, str, str]:
    fm = raw.split("---", 2)
    meta, body = fm[1], fm[2]
    title = re.search(r"^title:\s*(.+)$", meta, re.M).group(1).strip().strip("'\"")
    order_m = re.search(r"order:\s*(\d+)", meta)
    return title, int(order_m.group(1)) if order_m else 99, body, slug


def build() -> int:
    files = sorted(TOPICS.glob("*.md"))
    chapters = sorted(
        (front_matter(f.read_text(encoding="utf-8"), f.stem) for f in files), key=lambda c: c[1]
    )

    tmp = pathlib.Path(tempfile.mkdtemp())
    cover = tmp / "cover.png"
    make_cover(cover)

    parts = [
        "# 關於這份指南\n",
        "整理歷屆血液專科醫師考試「口試」關卡的考生心得，**去名化後**只保留考試走向本身："
        "主題分布、典型問答流程、答題心法。不含任何真實考官或考生姓名，也沒有針對特定個人的評論。\n",
        "每一章的結構固定：先給一個可以重複套用的**推理架構**，接著是**破題關鍵句**"
        "（一開口就該講的那句）、**擬答**（可以直接照著唸的完整答案）、"
        "**追問**（考官接下來最可能問什麼），最後是**速記表**與**容易被電的點**。\n",
        f"網站版另有影片清單與可列印的一頁速查：<{SITE}>\n",
        "> 僅供準備血液專科口試參考，非官方資料，實際考試內容以主辦單位公告為準。\n",
    ]
    for title, _, body, slug in chapters:
        # 顯式 id：讓跨章連結有穩定的目標（pandoc 自動產生的 id 不好預測）
        parts.append(f"\n# {title} {{#ch-{slug}}}\n")
        parts.append(convert(body))

    md_path = tmp / "book.md"
    md_path.write_text("\n".join(parts), encoding="utf-8")
    css_path = tmp / "epub.css"
    css_path.write_text(CSS, encoding="utf-8")

    OUT_DIR.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = tmp / "meta.yaml"
    meta.write_text(
        f"""---
title: "{TITLE}"
subtitle: "{SUBTITLE}"
creator: htlin222
language: zh-TW
date: "{datetime.now().strftime('%Y-%m-%d')}"
identifier: "{SITE}"
description: "整理歷屆考生口試心得，去名化後的口試主題、推理架構、擬答與準備策略。"
rights: "去名化整理，非官方資料"
---
""",
        encoding="utf-8",
    )

    cmd = [
        "pandoc",
        str(meta),
        str(md_path),
        "-f",
        "markdown+raw_html+pipe_tables",
        "-t",
        "epub3",
        "--toc",
        "--toc-depth=2",       # 章 → 節，兩層巢狀目錄
        "--split-level=1",     # 一章一個檔案，Kindle 翻頁比較順
        f"--css={css_path}",
        f"--epub-cover-image={cover}",
        "--metadata",
        f"dcterms:modified={now}",
        "-o",
        str(OUT_FILE),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        return 1

    size = OUT_FILE.stat().st_size // 1024
    print(f"章節 {len(chapters)} 章 → {OUT_FILE.relative_to(ROOT)}（{size} KB）")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(build())
