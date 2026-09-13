#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""把主題頁轉成「可朗讀的逐字稿」，並輸出語音合成用的分段檔。

一次產生兩個檔案，內容同源，避免逐字稿跟實際合成的語音對不起來：
  dist-audio/<slug>.txt    人看的逐字稿（先審這個）
  dist-audio/<slug>.jsonl  合成用的分段（lang + text + 停頓）

三個必須處理的坑：

1. **中英要不同聲音**：中文語音唸英文醫學名詞會走音，反之亦然。所以逐字稿要
   標好語言邊界，合成時分段用不同 voice。只有「拉丁字母」才觸發切換——數字、
   標點、單位留在中文段，否則「2–4 週」會被切成三段，聲音來回跳。

2. **大寫縮寫要逐字母唸**：aPTT 要唸 A-P-T-T 而不是「阿普特」。規則是含兩個以上
   大寫字母的詞就拆開，但有例外清單（imatinib 這種小寫藥名不動；CRAB、SLiM 這種
   當作單字唸的縮寫也不拆）。

3. **表格沒辦法直接唸**：全站 44 張速記表，逐格唸出來沒有意義。改成把每一列
   組成一句話（「第一欄：欄二標題是…；欄三標題是…」）。

用法：
    uv run --script scripts/build_transcript.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPICS = ROOT / "src" / "content" / "docs" / "topics"
OUT = ROOT / "dist-audio"

# ── 縮寫處理 ─────────────────────────────────────────────────────────────────
# 這些「看起來像縮寫」但要當單字唸，不拆成字母
SAY_AS_WORD = {
    "CRAB", "SLiM", "FEIBA", "MRD", "GELF", "PBAC", "IRIDA", "AQUILA",
    "QuiRedex", "STaMINA", "PERSEUS", "GRIFFIN", "CORAL", "TRANSFORM",
    "BELINDA", "ZUMA", "EMN", "HO", "AML", "ALL", "CML", "MDS", "ITP", "TTP",
    "HUS", "DIC", "PNH", "IDA", "MPN", "ET", "PV", "PMF", "CLL", "DLBCL",
    "MGUS", "MGRS", "APL", "HLH", "AIHA", "TMA", "MAHA", "NTDT", "TRM", "NRM",
    "HCT", "IPSS", "ELN", "TFR", "MMR", "ORR", "PFS", "OS", "CR", "PR", "VGPR",
    "TKI", "HMA", "IMiD", "ASCT", "VTE", "DVT", "PE", "CKD", "IBD", "RA",
    "TRALI", "TACO", "OPSI", "GVHD", "EMA", "PBSCT", "CAR",
}
# 特別讀法：換成更接近口語的說法再交給語音
SPEAK_AS = {
    "aPTT": "a P T T",
    "PT": "P T",
    "MCV": "M C V",
    "MCH": "M C H",
    "RDW": "R D W",
    "TSAT": "T SAT",
    "TIBC": "T I B C",
    "sFLC": "s F L C",
    "HbA2": "H b A two",
    "HbF": "H b F",
    "G6PD": "G six P D",
    "T2*": "T two star",
    "BCR-ABL1": "B C R A B L one",
    "JAK2": "JAK two",
    "CALR": "CALR",
    "MPL": "M P L",
    "TP53": "T P fifty-three",
    "CD55": "C D fifty-five",
    "CD59": "C D fifty-nine",
    "CD5": "C D five",
    "CD23": "C D twenty-three",
    "CD38": "C D thirty-eight",
    "FVIII": "factor eight",
    "FIX": "factor nine",
    "FXI": "factor eleven",
    "FXII": "factor twelve",
    "FII": "factor two",
    "FV": "factor five",
    "FX": "factor ten",
    "VRd": "V R d",
    "Dara-VRd": "Dara V R d",
    "VCd": "V C d",
    "7+3": "seven plus three",
    "MR4.5": "M R four point five",
    "ADAMTS13": "ADAMTS thirteen",
    "vWF": "v W F",
    "vWD": "v W D",
    "MPO": "M P O",
    "IgA": "I g A",
    "IgG": "I g G",
    "IgM": "I g M",
    "IPF": "I P F",
    "TPO": "T P O",
    "EPO": "E P O",
    "DAT": "D A T",
    "PIGA": "P I G A",
    "NRBC": "N R B C",
    "PPI": "P P I",
    "qPCR": "q P C R",
    "CBF": "C B F",
    "IS": "I S",
    "vit K": "vitamin K",
    "vit": "vitamin",
}
# 單位：唸成英文口語，不要讓語音唸出斜線
UNITS = {
    "g/dL": "grams per deciliter",
    "mg/dL": "milligrams per deciliter",
    "ng/mL": "nanograms per milliliter",
    "IU/mL": "international units per milliliter",
    "mL": "milliliters",
    "mm": "millimeters",
}

# 這裡只收「漢字」，不含全形標點。原本把 CJK 標點範圍也算進來，
# 結果「，」「。」被當成可發音的中文字，產生只有一個標點的段落，
# 而 edge-tts 收到純標點會直接回 NoAudioReceived。
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
CJK = HAN  # 語言判斷沿用漢字範圍
LATIN = re.compile(r"[A-Za-z]")
SPEAKABLE = re.compile(r"[A-Za-z0-9\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

# 凝血因子的羅馬數字要唸成數字：factor VII 是「factor seven」，不是「V I I」
ROMAN = {
    "XIII": "thirteen", "XII": "twelve", "XI": "eleven", "VIII": "eight",
    "VII": "seven", "VI": "six", "IX": "nine", "IV": "four",
    "V": "five", "X": "ten", "II": "two", "I": "one",
}

# 符號：語音唸不出來，或會唸成「右箭頭」「degree C」這種雜訊
SYMBOLS = [
    ("⚠️", ""), ("⚠", ""), ("\U0001f9ed", ""),
    ("→", "，"), ("←", "，"), ("↑", "上升"), ("↓", "下降"),
    ("≥", "大於等於 "), ("≤", "小於等於 "),
    ("＞", "大於 "), ("＜", "小於 "),
    ("≈", "約 "), ("±", "加減 "), ("×", " 乘 "),
    ("℃", "°C"),
    ("–", "到"), ("——", "，"), ("—", "，"),
]


def normalize_symbols(text: str) -> str:
    for a, b in SYMBOLS:
        text = text.replace(a, b)
    # 中文語音唸「百分之 N」比唸「N 百分號」自然
    text = re.sub(r"(\d+(?:\.\d+)?)\s*°C", r"攝氏 \1 度", text)
    text = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"百分之 \1", text)
    text = re.sub(r"(?<=[）)\w])\s*\+\s*(?=[A-Za-z（(㐀-鿿])", " 加上 ", text)
    text = re.sub(r"(?<![\d.])1\s*[:：]\s*1(?![\d.])", "一比一", text)
    # 斜線：中文之間唸頓號、英文之間唸 and，否則語音會唸出「斜線」
    text = re.sub(r"(?<=[一-鿿])\s*[／/]\s*(?=[一-鿿])", "、", text)
    text = re.sub(r"(?<=[A-Za-z])\s*[／/]\s*(?=[A-Za-z])", " or ", text)
    # 符號換成中文標點後會留下多餘空白（「延長 ， 問題」），收乾淨
    text = re.sub(r"\s+([，。、；：」）])", r"\1", text)
    text = re.sub(r"([（「])\s+", r"\1", text)
    text = re.sub(r"([，。、；：])\1+", r"\1", text)
    return text


def expand_roman(text: str) -> str:
    """只在 factor／F 前綴或因子清單的語境轉換，避免誤傷正常英文字。"""
    pat = "|".join(ROMAN)
    text = re.sub(
        rf"\b(factor |Factor |F)({pat})\b",
        lambda m: f"factor {ROMAN[m.group(2)]}",
        text,
    )
    # 清單裡的裸寫法，例如「（X、V、II、fibrinogen）」
    text = re.sub(
        rf"(?<=[（(、,\s])({pat})(?=[、,）)\s])",
        lambda m: f"factor {ROMAN[m.group(1)]}",
        text,
    )
    return text


def expand_terms(text: str) -> str:
    """縮寫與單位換成可朗讀的形式。長詞先換，避免 PT 先吃掉 aPTT 的一部分。"""
    text = normalize_symbols(text)
    text = expand_roman(text)
    for k in sorted({**SPEAK_AS, **UNITS}, key=len, reverse=True):
        v = {**SPEAK_AS, **UNITS}[k]
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(k)}(?![A-Za-z0-9])", v, text)

    # 其餘含兩個以上大寫字母的詞，預設逐字母唸
    def spell(m: re.Match[str]) -> str:
        w = m.group(0)
        if w in SAY_AS_WORD or w.lower() == w:
            return w
        if sum(c.isupper() for c in w) >= 2 and len(w) <= 6:
            return " ".join(w)
        return w

    return re.sub(r"(?<![A-Za-z0-9])[A-Za-z][A-Za-z0-9]{1,5}(?![A-Za-z0-9])", spell, text)


def segment(text: str) -> list[dict]:
    """依語言切段。只有拉丁字母觸發英文段；數字與標點跟著相鄰段落走。"""
    runs: list[dict] = []
    for ch in text:
        if CJK.match(ch):
            lang = "zh"
        elif LATIN.match(ch):
            lang = "en"
        else:
            lang = None  # 中性：數字、標點、空白
        if runs and (lang is None or runs[-1]["lang"] == lang):
            runs[-1]["text"] += ch
        elif lang is None:
            runs.append({"lang": "zh", "text": ch})
        else:
            runs.append({"lang": lang, "text": ch})

    out = []
    for r in runs:
        t = r["text"].strip()
        if not t:
            continue
        # 沒有任何可發音字元（只剩標點）的段落一定要併回前一段：
        # edge-tts 收到純標點會回 NoAudioReceived 而不是空音檔。
        speakable = SPEAKABLE.search(t)
        if not speakable:
            if out:
                out[-1]["text"] += t
            continue
        if r["lang"] == "en" and not LATIN.search(t) and out:
            out[-1]["text"] += " " + t
            continue
        out.append({"lang": r["lang"], "text": t})
    return out


# ── markdown → 朗讀文字 ───────────────────────────────────────────────────────
SVG = re.compile(r"<svg[\s\S]*?</svg>\s*")
CALLOUT_OPEN = re.compile(r'<div class="callout callout-(keywords|followup)">')
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def clean(s: str) -> str:
    s = SVG.sub("", s)
    s = LINK.sub(r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"[*`]", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[ \t]+", " ", s).strip()


def table_to_speech(rows: list[list[str]]) -> list[str]:
    """表格轉成句子：每一列一句，用表頭當欄位名。"""
    if len(rows) < 2:
        return []
    head = [clean(c) for c in rows[0]]
    out = []
    for r in rows[2:] if len(rows) > 2 and set("".join(rows[1])) <= set("-| :") else rows[1:]:
        cells = [clean(c) for c in r]
        if not any(cells):
            continue
        first, rest = cells[0], cells[1:]
        # 第一欄要帶上欄名，否則唸出來會變成沒頭沒尾的「正常，…是延長」
        lead = f"{head[0]}：{first}" if head and head[0] else first
        bits = [f"{head[i + 1]}：{c}" for i, c in enumerate(rest) if c and i + 1 < len(head)]
        out.append(f"{lead}。{'；'.join(bits)}。")
    return out


def parse_chapter(md: str) -> list[tuple[str, str]]:
    """回傳 [(朗讀文字, 停頓標記)]，停頓標記用來在合成時插入不同長度的靜音。"""
    lines = md.split("\n")
    out: list[tuple[str, str]] = []
    i = 0
    table: list[list[str]] = []

    def flush_table():
        nonlocal table
        if table:
            for s in table_to_speech(table):
                out.append((s, "short"))
            table = []

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if s.startswith("|"):
            table.append(s.strip("|").split("|"))
            i += 1
            continue
        flush_table()

        if not s:
            i += 1
            continue
        if s.startswith("## "):
            out.append((clean(s[3:]), "section"))
        elif m := CALLOUT_OPEN.match(s):
            label = "破題關鍵句" if m.group(1) == "keywords" else "可能的追問"
            out.append((label, "label"))
        elif s.startswith("</div>") or s.startswith('<div class="callout-title">'):
            pass
        elif re.match(r"^\s*(?:[-*]|\d+\.)\s*擬答[:：]?\s*$", s):
            out.append(("完整擬答", "label"))
        else:
            t = clean(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", ln))
            if t:
                out.append((t, "short"))
        i += 1

    flush_table()
    return out


def build() -> int:
    files = sorted(TOPICS.glob("*.md"))
    chapters = []
    for f in files:
        raw = f.read_text(encoding="utf-8")
        meta, body = raw.split("---", 2)[1], raw.split("---", 2)[2]
        title = re.search(r"^title:\s*(.+)$", meta, re.M).group(1).strip().strip("'\"")
        order = int(m.group(1)) if (m := re.search(r"order:\s*(\d+)", meta)) else 99
        body = re.split(r"\n##\s*相關 YouTube 影片", body)[0]  # 影片段落不朗讀
        chapters.append((order, f.stem, title, body))
    chapters.sort()

    OUT.mkdir(exist_ok=True)
    total_seg = total_char = 0

    for n, (_, slug, title, body) in enumerate(chapters, 1):
        pieces = [(f"第 {n} 章，{title}", "section")] + parse_chapter(body)

        segs: list[dict] = []
        txt_lines: list[str] = []
        for text, kind in pieces:
            spoken = expand_terms(text)
            txt_lines.append(("\n" if kind in ("section", "label") else "") + spoken)
            parts = segment(spoken)
            if parts:
                parts[-1]["pause"] = {"section": 900, "label": 500, "short": 250}[kind]
                segs.extend(parts)

        (OUT / f"{slug}.txt").write_text(
            f"# {title}\n\n" + "\n".join(txt_lines) + "\n", encoding="utf-8"
        )
        (OUT / f"{slug}.jsonl").write_text(
            "\n".join(json.dumps(s, ensure_ascii=False) for s in segs) + "\n", encoding="utf-8"
        )
        chars = sum(len(s["text"]) for s in segs)
        total_seg += len(segs)
        total_char += chars
        en = sum(1 for s in segs if s["lang"] == "en")
        print(f"{n:2d}. {slug:30s} 段 {len(segs):4d}（英 {en:3d}）字 {chars:5d}")

    print(f"\n共 {len(chapters)} 章、{total_seg} 段、{total_char} 字 → {OUT.relative_to(ROOT)}/")
    print("先審 .txt，確認唸法沒問題再跑 build_audio.py")
    return 0


if __name__ == "__main__":
    sys.exit(build())
