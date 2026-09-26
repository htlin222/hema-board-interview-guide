#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.45", "pypdf>=4"]
# ///
"""把 /booklet/ 印成 A4 PDF，並檢查每一張有沒有溢出。

先 `npm run build`，本腳本讀 dist/booklet/index.html。每張 .sheet 是固定 A4 橫式（297×210mm）、overflow hidden，
所以溢出不會在 PDF 上多出一頁、而是被裁掉——這裡直接量 scrollHeight 與 clientHeight，
超過就列出頁碼與超出的 px，並以非零 exit code 結束，讓 CI 擋下來。

同一支腳本也印平板大字版（/booklet-a5/，A4 橫式、每頁約半張內容、字約 1.5 倍）：每章自動分頁，所以不量溢出，改成檢查
網頁頁數＝PDF 頁數、沒有任何一頁內容被截掉、沒有東西超出頁寬。

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
SRC_A5 = SRC.parent.parent / "booklet-a5" / "index.html"
OUT_A5 = OUT_DIR / "hema-board-interview-booklet-a5.pdf"

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
            pdf = page.pdf(
                format="A4",
                landscape=True,
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            OUT_FILE.write_bytes(with_outline(pdf, page.evaluate(A4_OUTLINE)))
            print(f"\n→ {OUT_FILE.relative_to(ROOT)}  ({len(rows)} 頁)")

        a5_problems = check_a5(browser, None if check_only else OUT_A5)
        browser.close()

    if bad:
        print(f"\n{len(bad)} 頁溢出，請刪減：{', '.join('p' + r['page'] for r in bad)}", file=sys.stderr)
        return 1
    if a5_problems:
        return 1
    return 0


# PDF 書籤（巢狀）：第一層分組（正文／診斷標準總表／參考劑量總表）→ 第二層各章 → 第三層章內小節（h2）。
# 每一項記它在第幾頁（0 起算），由頁面 DOM 讀出；Chrome 的 page.pdf 不會自己產生這種分組。
A4_OUTLINE = """
() => [...document.querySelectorAll('.sheet')].map((s, i) => ({
  id: s.id, title: s.querySelector('h1').textContent.trim(), page: i,
  subs: [...s.querySelectorAll('.inner h2')].map(h => [h.textContent.trim(), i]),
}))
"""
A5_OUTLINE = """
() => {
  const out = [];
  [...document.querySelectorAll('#pages .pg')].forEach((p, i) => {
    if (p.dataset.chapter) out.push({ id: p.dataset.id, title: p.dataset.chapter.trim(), page: i, subs: [] });
    p.querySelectorAll('.pg-body h2').forEach(h => out.at(-1).subs.push([h.textContent.trim(), i]));
  });
  return out;
}
"""
GROUPS = [("criteria-", "診斷標準總表"), ("doses-", "參考劑量總表"), ("", "正文")]


def with_outline(pdf: bytes, chapters: list[dict]) -> bytes:
    """在 PDF 加上巢狀書籤，並設定開檔時顯示書籤欄。"""
    import io

    from pypdf import PdfReader, PdfWriter

    writer = PdfWriter(clone_from=PdfReader(io.BytesIO(pdf)))
    group_items: dict[str, object] = {}
    for ch in chapters:
        group = next(name for prefix, name in GROUPS if ch["id"].startswith(prefix))
        if group not in group_items:
            group_items[group] = writer.add_outline_item(group, ch["page"])
        item = writer.add_outline_item(ch["title"], ch["page"], parent=group_items[group])
        for title, page in ch["subs"]:
            writer.add_outline_item(title, page, parent=item)
    writer.page_mode = "/UseOutlines"
    buf = io.BytesIO()
    writer.write(buf)
    return buf.getvalue()


A5_MEASURE = """
() => ({
  wide: [...document.querySelectorAll('#pages table, #pages .fp')]
          .filter(e => e.scrollWidth > e.clientWidth + 1).length,
  cut: [...document.querySelectorAll('#pages .pg-body')]
          .map((b, i) => b.scrollHeight > b.clientHeight + 1 ? i + 1 : 0).filter(Boolean),
  pages: document.querySelectorAll('#pages .pg').length,
  chapters: [...document.querySelectorAll('#pages .pg[data-chapter]')].map((p, i, all) => {
    const idx = [...document.querySelectorAll('#pages .pg')].indexOf(p);
    const next = all[i + 1] ? [...document.querySelectorAll('#pages .pg')].indexOf(all[i + 1]) : document.querySelectorAll('#pages .pg').length;
    return { title: p.dataset.chapter, pages: next - idx, s: p.dataset.s };
  }),
})
"""


def check_a5(browser, out) -> int:
    """印平板大字版並檢查；回傳問題數。沒有 /booklet-a5/ 就跳過。

    頁面自己用 JS 把每章切成一張張 .pg（螢幕上看到的就是印出來的頁），
    所以這裡檢查：網頁頁數＝PDF 頁數、沒有任何一頁的內容被截掉、沒有東西超出頁寬。"""
    if not SRC_A5.exists():
        return 0
    import io

    from pypdf import PdfReader

    page = browser.new_page(viewport={"width": 1300, "height": 900})
    page.goto(SRC_A5.as_uri(), wait_until="load")
    page.wait_for_function("document.body.dataset.paged", timeout=60000)  # 等切頁跑完
    info = page.evaluate(A5_MEASURE)
    pdf = page.pdf(prefer_css_page_size=True, print_background=True)
    outline = page.evaluate(A5_OUTLINE)
    page.close()

    actual = len(PdfReader(io.BytesIO(pdf)).pages)
    print(f"\n平板大字版：{len(info['chapters'])} 章 → {info['pages']} 頁（PDF {actual} 頁）")
    for c in info["chapters"]:
        if c["pages"] != 2 or c["s"] != "1":
            print(f"   {c['title'][:28]:30s} {c['pages']} 頁  字級 {c['s']}")

    problems = 0
    if info["wide"]:
        print(f"平板大字版：{info['wide']} 個表格或框超出頁寬", file=sys.stderr)
        problems += 1
    if info["cut"]:
        print(f"平板大字版：第 {info['cut']} 頁有單一區塊比一頁還高，內容被截掉", file=sys.stderr)
        problems += 1
    if actual != info["pages"]:
        print(f"平板大字版：網頁 {info['pages']} 頁 ≠ PDF {actual} 頁", file=sys.stderr)
        problems += 1
    if out and not problems:
        out.write_bytes(with_outline(pdf, outline))
        print(f"→ {out.relative_to(ROOT)}")
    return problems


if __name__ == "__main__":
    raise SystemExit(main())
