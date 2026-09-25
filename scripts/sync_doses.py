#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""把手冊的總表來源注入對應主題頁：

- src/booklet/criteria/<slug>.md → 主題頁「## 診斷標準」段落
- src/booklet/doses/<slug>.md    → 主題頁「## 參考劑量」段落

兩種內容都只維護一份，手冊總表跟主題頁都從這裡來。主題頁裡用成對的 HTML 註解當錨點：

    <!-- criteria:start --> … <!-- criteria:end -->
    <!-- doses:start -->    … <!-- doses:end -->

由本腳本產生，不要手改。沒有錨點時，診斷標準插在參考劑量之前，參考劑量插在
「## 相關 YouTube 影片」之前（那一節前面固定是內容、後面是附錄）。重跑是冪等的。

手冊裡的第一性原理框（<div class="fp">）在網站上改成引用區塊，EPUB 與 Anki 也吃得下。

用法：
    uv run --script scripts/sync_doses.py           # 寫回
    uv run --script scripts/sync_doses.py --check   # 只比對，有差異就 exit 1（給 CI 用）
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOOKLET = ROOT / "src" / "booklet"
TOPICS = ROOT / "src" / "content" / "docs" / "topics"
SITE = "https://htlin222.github.io/hema-board-interview-guide"

FRONT = re.compile(r"^---\s*\n[\s\S]*?\n---\s*\n", re.M)
VIDEO_H2 = re.compile(r"^## (?:<svg[\s\S]*?</svg>\s*)?相關 YouTube 影片", re.M)
FP_DIV = re.compile(r'<div class="fp">([\s\S]*?)</div>')

# (資料夾, 錨點名, 段落標題, 段落開頭說明)。順序＝在主題頁裡的先後。
KINDS = [
    (
        "criteria",
        "criteria",
        "診斷標準",
        "診斷標準每一組先講第一性原理（這套標準為什麼長這樣），再列切點；"
        "WHO 2022 與 ICC 2022 有差異時並列。與 "
        f"[A4 手冊]({SITE}/booklet/) 的診斷標準總表同源。",
    ),
    (
        "doses",
        "doses",
        "參考劑量",
        "成人常規參考劑量，用來答「數量級、途徑、頻率、要監測什麼」；"
        "實際處方以仿單、健保規定與最新指引為準，特殊族群另行查核。"
        f"與 [A4 手冊]({SITE}/booklet/) 的劑量總表同源。",
    ),
]


def markers(name: str) -> tuple[str, str]:
    return f"<!-- {name}:start -->", f"<!-- {name}:end -->"


def for_site(body: str) -> str:
    """手冊用的 HTML 框改成網站也好讀的 Markdown 引用區塊。"""

    def repl(m: re.Match[str]) -> str:
        inner = re.sub(r"<b>(.*?)</b>", r"**\1**", m.group(1)).strip()
        return "> " + re.sub(r"\s*\n\s*", " ", inner)

    return FP_DIV.sub(repl, body)


def block(name: str, heading: str, note: str, body: str) -> str:
    start, end = markers(name)
    return f"{start}\n## {heading}\n\n{note}\n\n{for_site(body).strip()}\n{end}\n"


def inject(md: str, name: str, new: str, later: list[str]) -> str:
    """有錨點就換掉；沒有就插在「後面那幾種段落」或影片節之前。"""
    start, end = markers(name)
    if start in md and end in md:
        return re.sub(
            re.escape(start) + r"[\s\S]*?" + re.escape(end) + r"\n?", new, md, count=1
        )
    for other in later:
        pos = md.find(markers(other)[0])
        if pos >= 0:
            return md[:pos] + new + "\n" + md[pos:]
    m = VIDEO_H2.search(md)
    if m:
        return md[: m.start()] + new + "\n" + md[m.start() :]
    return md.rstrip() + "\n\n" + new


def main() -> int:
    check = "--check" in sys.argv
    pending: dict[pathlib.Path, str] = {}
    for idx, (folder, name, heading, note) in enumerate(KINDS):
        later = [k[1] for k in KINDS[idx + 1 :]]
        for f in sorted((BOOKLET / folder).glob("*.md")):
            topic = TOPICS / f.name
            if not topic.exists():
                print(f"跳過 {folder}/{f.name}：沒有對應主題頁", file=sys.stderr)
                continue
            body = FRONT.sub("", f.read_text(encoding="utf-8"), count=1)
            body = re.sub(
                r"^<!--\s*page\s*-->\s*$\n?", "", body, flags=re.M
            )  # 手冊分張標記，網站不需要
            cur = pending.get(topic, topic.read_text(encoding="utf-8"))
            pending[topic] = inject(cur, name, block(name, heading, note, body), later)

    dirty = 0
    for topic, new in sorted(pending.items()):
        if new == topic.read_text(encoding="utf-8"):
            continue
        dirty += 1
        if check:
            print(f"落後：{topic.relative_to(ROOT)}")
        else:
            topic.write_text(new, encoding="utf-8")
            print(f"已更新 {topic.relative_to(ROOT)}")
    if check and dirty:
        print(
            f"\n{dirty} 頁的診斷標準／參考劑量與手冊來源不同步，跑 `npm run sync:doses`",
            file=sys.stderr,
        )
        return 1
    if not dirty:
        print("全部同步")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
