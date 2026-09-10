#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["genanki>=0.13", "markdown-it-py>=3.0"]
# ///
"""把主題頁內容打包成 Anki 牌組（巢狀：主題 :: 卡片類型）。

牌組結構：
    血液科口試 :: <主題> :: 推理架構 / 破題關鍵句 / 擬答 / 追問 / 速記表 / 容易被電的點

抽取邏輯跟站上的 handout 共用同一組錨點：每個問答區塊都被兩個 callout 夾住——
「破題關鍵句」在前、「追問」在後，中間就是擬答。這比去猜各頁不一致的標題寫法可靠
（頁面上至少有五種問答標題格式：`**Q: …**`、`**Q1：…**`、`**N. …**`、
編號清單、粗體論點）。

ID 與 GUID 都由內容雜湊決定，所以重跑產生的檔案可以直接重新匯入而不會變成重複卡。

用法：
    uv run --script scripts/build_anki.py            # → dist-anki/hema-board-interview.apkg
"""

from __future__ import annotations

import hashlib
import html
import pathlib
import re
import sys

import genanki
from markdown_it import MarkdownIt

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPICS = ROOT / "src" / "content" / "docs" / "topics"
OUT_DIR = ROOT / "dist-anki"
OUT_FILE = OUT_DIR / "hema-board-interview.apkg"  # 純 ASCII：GitHub Release 會把 CJK 檔名悄悄改成 default.apkg

ROOT_DECK = "血液科口試"
SITE = "https://htlin222.github.io/hema-board-interview-guide"

md = MarkdownIt("js-default")  # js-default 這個 preset 含表格支援


def stable_id(*parts: str) -> int:
    """由內容決定的 ID，範圍取 Anki 慣用的 1<<30 .. 1<<31。"""
    h = hashlib.sha256("::".join(parts).encode()).hexdigest()
    return (1 << 30) + (int(h[:8], 16) % (1 << 30))


def strip_icons(s: str) -> str:
    return re.sub(r"<svg[\s\S]*?</svg>\s*", "", s)


def dedent(block: str) -> str:
    """把整塊內容左移到最小縮排，否則 markdown 會把它當成程式碼區塊。"""
    lines = [ln for ln in block.split("\n")]
    indents = [len(ln) - len(ln.lstrip()) for ln in lines if ln.strip()]
    n = min(indents) if indents else 0
    return "\n".join(ln[n:] if len(ln) >= n else ln for ln in lines)


def render(block: str) -> str:
    return md.render(dedent(strip_icons(block))).strip()


def plain(block: str) -> str:
    """取純文字。要塞回 HTML 欄位，所以 escape——內容裡有 `<10%`、`>35%` 這類寫法。"""
    txt = re.sub(r"<[^>]+>", "", strip_icons(block))
    return html.escape(re.sub(r"\s+", " ", txt).strip())


CALLOUT_KEY = '<div class="callout callout-keywords">'
CALLOUT_FUP = '<div class="callout callout-followup">'
CALLOUT_END = re.compile(r"\n\s*\n\s*</div>")


def callout_body(text: str, start: int) -> tuple[str, int]:
    """回傳 callout 的內文與其結束位置（start 指向 callout 開頭）。"""
    after_title = text.index("</div>", start) + len("</div>")
    m = CALLOUT_END.search(text, after_title)
    end = m.end() if m else len(text)
    body = text[after_title : m.start()] if m else text[after_title:]
    return body.strip(), end


BOLD_LINE = re.compile(r"^\s*(?:[-*]\s*|\d+\.\s*)?\*\*(.+?)\*\*\s*$", re.M)


def question_before(text: str, pos: int) -> str:
    """往前找最近的一行粗體標題當作題目。"""
    hits = list(BOLD_LINE.finditer(text, 0, pos))
    if not hits:
        return ""
    raw = strip_icons(hits[-1].group(1)).strip()
    return re.sub(r"^(?:Q\d*[:：]|\d+\.)\s*", "", raw).strip()


def sections(text: str) -> list[tuple[str, str]]:
    marks = [(m.group(1), m.start(), m.end()) for m in re.finditer(r"^## (.+)$", text, re.M)]
    out = []
    for i, (title, s, e) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else len(text)
        out.append((strip_icons(title).strip(), text[e:end].strip()))
    return out


CSS = """
.card {
  font-family: -apple-system, "PingFang TC", "Heiti TC", "Noto Sans TC", sans-serif;
  font-size: 17px; line-height: 1.65;
  text-align: left; color: #1f1b2a; background: #fbfafd;
  padding: 4px 2px;
}
.tag { display:inline-block; font-size:12px; letter-spacing:.03em;
  color:#6b3fa0; border:1px solid #d5c8ea; border-radius:3px;
  padding:1px 7px; margin-bottom:10px; }
.q { font-weight: 700; font-size: 18px; }
hr#answer { border: none; border-top: 1px solid #ddd6ea; margin: 14px 0 10px; }
.card ul, .card ol { padding-left: 1.15em; margin: 6px 0; }
.card li { margin: 3px 0; }
.card table { border-collapse: collapse; width: 100%; font-size: 14px; margin: 8px 0; }
.card th, .card td { border: 1px solid #ddd6ea; padding: 4px 7px; vertical-align: top; }
.card th { background: #f1eafb; }
.card td:first-child { font-weight: 600; }
.src { margin-top: 14px; font-size: 12px; color: #7d7590; }
.src a { color: #7d7590; }
.nightMode .card, .card.nightMode { color:#e6e1f0; background:#1b1a21; }
.nightMode th { background:#2b2536; }
.nightMode th, .nightMode td, .nightMode hr#answer { border-color:#403a4d; }
.nightMode .tag { color:#c4a7f0; border-color:#4a4060; }
"""

MODEL = genanki.Model(
    stable_id("model", "v1"),
    "血液科口試（問答）",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Kind"}, {"name": "Source"}],
    templates=[
        {
            "name": "問答",
            "qfmt": '<div class="tag">{{Kind}}</div><div class="q">{{Front}}</div>',
            "afmt": '<div class="tag">{{Kind}}</div><div class="q">{{Front}}</div>'
            '<hr id="answer">{{Back}}<div class="src">{{Source}}</div>',
        }
    ],
    css=CSS,
)


def note(deck_key: str, kind: str, front: str, back: str, url: str, tags: list[str]) -> genanki.Note:
    return genanki.Note(
        model=MODEL,
        fields=[front, back, kind, f'<a href="{url}">{url}</a>'],
        guid=genanki.guid_for(deck_key, kind, front),
        tags=tags,
    )


def build() -> int:
    files = sorted(TOPICS.glob("*.md"))
    if not files:
        print("找不到主題頁", file=sys.stderr)
        return 1

    decks: dict[str, genanki.Deck] = {}

    def deck_for(name: str) -> genanki.Deck:
        if name not in decks:
            decks[name] = genanki.Deck(stable_id("deck", name), name)
        return decks[name]

    deck_for(ROOT_DECK)
    counts: dict[str, int] = {}

    for f in files:
        raw = f.read_text(encoding="utf-8")
        slug = f.stem
        title_m = re.search(r"^title:\s*(.+)$", raw, re.M)
        title = (title_m.group(1).strip() if title_m else slug).strip("'\"")
        url = f"{SITE}/topics/{slug}/"
        base_tags = [f"topic::{slug}"]
        body = raw.split("---", 2)[-1]

        def add(kind: str, front: str, back: str) -> None:
            if not front or not back:
                return
            name = f"{ROOT_DECK}::{title}::{kind}"
            deck_for(name).add_note(
                note(f"{slug}|{kind}", kind, front, back, url, base_tags + [f"kind::{kind}"])
            )
            counts[kind] = counts.get(kind, 0) + 1

        secs = sections(body)

        # 推理架構／框架／核心邏輯：一節一張
        for heading, content in secs:
            if re.search(r"推理架構|框架|核心邏輯", heading):
                add("推理架構", f"{title}：{heading}", render(content))

        # 速記表：一張表一張卡，用表格前的粗體小標當題面
        for heading, content in secs:
            if "速記表" not in heading:
                continue
            chunks = re.split(r"\n(?=\*\*)", content)
            for ch in chunks:
                if "|" not in ch:
                    continue
                m = re.match(r"\*\*(.+?)\*\*", ch.strip())
                if not m:
                    continue
                add("速記表", f"{title}：{strip_icons(m.group(1)).strip()}", render(ch[m.end():]))

        # 容易被電的點：整節一張
        for heading, content in secs:
            if "容易被電" in heading:
                add("容易被電的點", f"{title}：容易被電的點", render(content))

        # 問答區塊：以「破題關鍵句」callout 為錨點，往前找題目、往後找擬答與追問
        pos = 0
        while (i := body.find(CALLOUT_KEY, pos)) != -1:
            opener, key_end = callout_body(body, i)
            question = question_before(body, i)
            j = body.find(CALLOUT_FUP, key_end)
            nxt_key = body.find(CALLOUT_KEY, key_end)
            has_fup = j != -1 and (nxt_key == -1 or j < nxt_key)

            answer_block = body[key_end : (j if has_fup else (nxt_key if nxt_key != -1 else len(body)))]

            if not answer_block.strip():
                # itp.md / aml-mds-cml.md 這類頁面，論點內容在 callout「之前」，
                # 所以往回從題目那一行取到 callout 開頭。
                qm = list(BOLD_LINE.finditer(body, 0, i))
                if qm:
                    answer_block = body[qm[-1].end() : i]

            # 「擬答：」有兩種寫法：獨立標籤行，或是一個 bullet（內容縮排在它底下），整行拿掉。
            answer_block = re.sub(
                r"^[ \t]*(?:[-*][ \t]*)?擬答[:：][ \t]*$\n?", "", answer_block, flags=re.M
            )
            # 擬答會一路吃到下一個 `## ` 標題，砍掉。
            # 注意這裡只能 rstrip：先 lstrip 會把第一行的縮排移掉，
            # 後面幾行的相對縮排就對不上，巢狀清單會被 markdown 當成段落的延續文字。
            answer_block = re.split(r"\n##\s", answer_block)[0].rstrip()

            if question:
                add("破題關鍵句", question, f"<p><b>{plain(opener)}</b></p>")
                if answer_block.strip():
                    add("擬答", question, render(answer_block))

            if has_fup:
                fup, fup_end = callout_body(body, j)
                for line in re.findall(r"^\s*[-*]\s+(.+)$", fup, re.M):
                    q, _, a = line.partition("→")
                    if a:
                        add("追問", f"{title}｜{plain(q).strip('「」 ')}", render(a.strip()))
                pos = fup_end
            else:
                pos = key_end

    OUT_DIR.mkdir(exist_ok=True)
    genanki.Package(list(decks.values())).write_to_file(OUT_FILE)

    total = sum(counts.values())
    print(f"牌組 {len(decks)} 個、卡片 {total} 張 → {OUT_FILE.relative_to(ROOT)}")
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {v:4d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
