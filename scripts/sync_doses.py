#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""把 src/booklet/doses/<slug>.md 注入對應主題頁的「參考劑量」段落。

劑量只維護一份（doses/），手冊總表跟主題頁都從這裡來。主題頁裡用一對 HTML 註解當錨點：

    <!-- doses:start -->
    ## 參考劑量
    …（由本腳本產生，不要手改）…
    <!-- doses:end -->

沒有錨點的主題頁，段落會插在「## 相關 YouTube 影片」之前（那一節前面固定是內容、後面是附錄）。
重跑是冪等的。

用法：
    uv run --script scripts/sync_doses.py           # 寫回
    uv run --script scripts/sync_doses.py --check   # 只比對，有差異就 exit 1（給 CI 用）
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOSES = ROOT / "src" / "booklet" / "doses"
TOPICS = ROOT / "src" / "content" / "docs" / "topics"

START, END = "<!-- doses:start -->", "<!-- doses:end -->"
FRONT = re.compile(r"^---\s*\n[\s\S]*?\n---\s*\n", re.M)
VIDEO_H2 = re.compile(r"^## (?:<svg[\s\S]*?</svg>\s*)?相關 YouTube 影片", re.M)

NOTE = (
    "成人常規參考劑量，用來答「數量級、途徑、頻率、要監測什麼」；"
    "實際處方以仿單、健保規定與最新指引為準，特殊族群另行查核。"
    "與 [A4 手冊](/hema-board-interview-guide/booklet/) 的劑量總表同源。"
)


def block(body: str) -> str:
    return f"{START}\n## 參考劑量\n\n{NOTE}\n\n{body.strip()}\n{END}\n"


def inject(md: str, body: str) -> str:
    new = block(body)
    if START in md and END in md:
        return re.sub(re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\n?", new, md, count=1)
    m = VIDEO_H2.search(md)
    if m:
        return md[: m.start()] + new + "\n" + md[m.start() :]
    return md.rstrip() + "\n\n" + new


def main() -> int:
    check = "--check" in sys.argv
    dirty = 0
    for f in sorted(DOSES.glob("*.md")):
        topic = TOPICS / f.name
        if not topic.exists():
            print(f"跳過 {f.name}：沒有對應主題頁", file=sys.stderr)
            continue
        body = FRONT.sub("", f.read_text(encoding="utf-8"), count=1)
        old = topic.read_text(encoding="utf-8")
        new = inject(old, body)
        if new != old:
            dirty += 1
            if check:
                print(f"落後：{topic.relative_to(ROOT)}")
            else:
                topic.write_text(new, encoding="utf-8")
                print(f"已更新 {topic.relative_to(ROOT)}")
    if check and dirty:
        print(f"\n{dirty} 頁的參考劑量與 doses/ 不同步，跑 `npm run sync:doses`", file=sys.stderr)
        return 1
    if not dirty:
        print("全部同步")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
