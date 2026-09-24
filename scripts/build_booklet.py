#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.45"]
# ///
"""把 /booklet/ 印成 A4 PDF，並檢查每一張有沒有溢出。

先 `npm run build`，本腳本讀 dist/booklet/index.html。每張 .sheet 是固定 297mm 高、overflow hidden，
所以溢出不會在 PDF 上多出一頁、而是被裁掉——這裡直接量 scrollHeight 與 clientHeight，
超過就列出頁碼與超出的 px，並以非零 exit code 結束，讓 CI 擋下來。

用法：
    npm run build && uv run --script scripts/build_booklet.py
    uv run --script scripts/build_booklet.py --check   # 只檢查不輸出 PDF
"""

from __future__ import annotations

import os
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
# 平行寫稿時可用 BOOKLET_DIST 指到 `astro build --outDir` 的目錄，避免互相覆蓋 dist/
SRC = ROOT / os.environ.get("BOOKLET_DIST", "dist") / "booklet" / "index.html"
OUT_DIR = ROOT / "dist-booklet"
OUT_FILE = OUT_DIR / "hema-board-interview-booklet.pdf"  # ASCII 檔名，GitHub Release 會改掉 CJK

MEASURE = """
() => [...document.querySelectorAll('.sheet')].map(s => {
  // scrollHeight 永遠 ≥ clientHeight，量不出剩餘；所以量 .inner 的自然高度
  const c = s.querySelector('.content');
  const need = c.querySelector('.inner').offsetHeight;
  return {
    page: s.dataset.page,
    id: s.id,
    title: s.querySelector('h1')?.textContent ?? '',
    over: Math.max(0, need - c.clientHeight),
    room: Math.max(0, c.clientHeight - need),
  };
})
"""


def launch(p):
    """優先用本機的 Google Chrome（字型、CJK 都齊），沒有再退回 playwright 自帶的 chromium。"""
    for kw in ({"channel": "chrome"}, {}):
        try:
            return p.chromium.launch(**kw)
        except Exception:  # noqa: BLE001 - 找不到 channel 就換下一個
            continue
    raise SystemExit("找不到可用的 Chromium；先跑 `uv run --with playwright playwright install chromium`")


def main() -> int:
    check_only = "--check" in sys.argv
    if not SRC.exists():
        print(f"找不到 {SRC}；先跑 npm run build（或 npx astro build --outDir <dir> 並設 BOOKLET_DIST）", file=sys.stderr)
        return 2

    with sync_playwright() as p:
        browser = launch(p)
        page = browser.new_page()
        page.emulate_media(media="print")
        page.goto(SRC.as_uri(), wait_until="load")
        page.wait_for_timeout(300)  # 等字型載完再量
        rows = page.evaluate(MEASURE)

        bad = [r for r in rows if r["over"] > 0]
        for r in rows:
            flag = "溢出" if r["over"] > 0 else "ok"
            extra = f"超出 {r['over']}px" if r["over"] > 0 else f"剩 {r['room']}px"
            print(f"[{flag:>2}] p{r['page']:>2} {r['title']}  ({extra})")

        if not check_only:
            OUT_DIR.mkdir(exist_ok=True)
            page.pdf(
                path=str(OUT_FILE),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            print(f"\n→ {OUT_FILE.relative_to(ROOT)}  ({len(rows)} 頁)")
        browser.close()

    if bad:
        print(f"\n{len(bad)} 頁溢出，請刪減：{', '.join('p' + r['page'] for r in bad)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
