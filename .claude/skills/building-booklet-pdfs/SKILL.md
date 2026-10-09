---
name: building-booklet-pdfs
description: Builds, edits, validates and publishes this repo's study booklets — the one-sheet-per-topic landscape A4 booklet and the large-print tablet edition (same content, about two pages per topic, type about 1.5x), both rendered from src/booklet/ to PDFs with a nested bookmark outline and released to booklet-latest. Covers writing pages in the first-principle + MECE format, adding diagnostic criteria and reference doses (synced into the website topic pages), OpenEvidence page-by-page validation with one subagent per page, layout checks, and publishing. Use when the user asks to change, add or verify booklet / 手冊 / A4 / 平板版 / 大字版 / PDF content, diagnostic criteria (診斷標準), doses (劑量), or the release PDFs.
---

# 手冊 PDF：撰寫、驗證、建置、發布

這個 repo 的手冊有兩種版面、**一份內容**。改內容只改 `src/booklet/`，兩版和網站主題頁都會跟著變。

| 產物 | 網址 | 版面 | 檔案 |
| --- | --- | --- | --- |
| A4 手冊 | `/booklet/` | 橫式 A4，**一主題一張**，固定外框、手寫到剛好塞滿 | `hema-board-interview-booklet.pdf` |
| 平板大字版 | `/booklet-a5/`（網址沿用舊名） | 同樣橫式 A4 紙，**每頁約半張內容**、字約 1.5 倍，頁面 JS 自動切頁，一主題約兩頁 | `hema-board-interview-booklet-a5.pdf` |

兩個 PDF 都在 release `booklet-latest`，都有三層書籤（分組 → 章 → h2 小節）。push 到 main 由 `.github/workflows/booklet.yml` 自動重建並覆蓋。

## 檔案地圖

| 要改什麼 | 檔案 |
| --- | --- |
| 正文（每檔一章／一張 A4） | `src/booklet/pages/NN-*.md` — 寫法見 `src/booklet/README.md` |
| 診斷標準（每個主題一份） | `src/booklet/criteria/<topic-slug>.md` |
| 參考劑量（每個主題一份） | `src/booklet/doses/<topic-slug>.md` |
| 總表怎麼分組成一張張 | `src/lib/booklet-data.ts`（`CRITERIA_SHEETS`、`DOSE_SHEETS`） |
| 共用樣式（灰階、斑馬紋、表格） | `src/styles/print.css`；大字版覆寫在 `src/styles/print-a5.css` |
| 大字版切頁邏輯 | `src/pages/booklet-a5/index.astro` 內的 inline script |
| 建置＋檢查＋書籤 | `scripts/build_booklet.py` |
| 把 criteria／doses 注入網站主題頁 | `scripts/sync_doses.py` |

slug＝`src/content/docs/topics/<slug>.md` 的檔名。criteria／doses 的 frontmatter `order` 照抄主題頁的 sidebar order。

## 指令

```bash
npm run build                 # Astro 建站（含 /booklet/ 與 /booklet-a5/）
npm run check:booklet         # 只檢查不出 PDF：A4 每張溢出量＋大字版頁數/截斷/超寬
npm run build:booklet         # 檢查並輸出兩個 PDF（含書籤）到 dist-booklet/
npm run sync:doses            # criteria/ 與 doses/ → 主題頁「診斷標準」「參考劑量」段落
python3 .claude/skills/building-booklet-pdfs/scripts/compact_tables.py <md...>   # 表格改回緊湊格式
```

`check:booklet` 的判讀：A4 每張要 `ok` 且**剩 ≥20px**（CI 用 Noto Sans CJK，字寬跟本機 PingFang 不同，要留餘裕）。大字版要「網頁 N 頁 = PDF N 頁」且沒有錯誤訊息；它會列出不是剛好兩頁、或字級被調小（0.93／0.87）的章。

## 工作流程

### 改既有內容（最常見）

```
- [ ] git pull（可能有別的 session 也在改這個 repo）
- [ ] 改 src/booklet/{pages,criteria,doses}/ 的 md；只改有問題的格子，不重寫整頁
- [ ] compact_tables.py 跑過改動的檔
- [ ] 改了 criteria/ 或 doses/ → npm run sync:doses
- [ ] npm run build && npm run check:booklet，A4 剩 ≥20px、大字版無錯誤
- [ ] git add 只加自己改的路徑（不要 git add -A），commit，push
- [ ] gh run list 等 booklet／Pages／EPUB 三個 workflow 都綠
```

溢出時：刪次要字句，**不刪切點數字**；或把短段落用 `<!-- pair -->` 並排（見 `src/booklet/README.md`）。

### 新增一章

在 `src/booklet/pages/` 新增 `NN-slug.md`（檔名排序＝頁序，可用 `10a-` 插在 10 與 11 之間），結構照 `src/booklet/README.md`：第一性原理框 → MECE 分岔表 → 速記表 → 破題關鍵句 → 容易被電。全書地圖 `01-map.md` 的頁碼範圍要跟著改。

### 新增或修改診斷標準／劑量

1. 寫 `src/booklet/{criteria,doses}/<slug>.md`。診斷標準開頭放一個 `<div class="fp"><b>第一性原理</b>　…</div>`，說明「這組診斷必須證明哪幾件事」，每條標準在最右欄寫「證明哪一件」；WHO 2022 與 ICC 2022 不同就並列兩欄。
2. 一張放不下：中間放一行 `<!-- page -->`，後半段進 `<slug>#2` 續張——但續張要先在 `CRITERIA_SHEETS` 定義（目前 MPN、白血病、Lymphoma、漿細胞有）。
3. `npm run sync:doses` 會把它注入主題頁（第一性原理框在網站上轉成引用區塊，`<!-- page -->` 會被拿掉）。

### 用 OpenEvidence 逐頁驗證（使用者要求「validate」「查證」時）

一頁一個 subagent，平行派出（同時上限 20 個，超過的等有空位再補）。每個 subagent：用 OE 查最容易錯的切點／試驗數字／劑量（最多 4–5 次 `oe_ask`，共用一個瀏覽器分頁），檢查分岔表是否 MECE，只改自己那一頁，建到自己的 `--outDir` 量版面，回報每條修改附 OE 網址。完整任務說明範本與主控收尾步驟見 [references/validation.md](references/validation.md)。

開工前先 `mcp__openevidence__oe_auth_status`；回 relay 錯誤就請使用者打開已登入的 openevidence.com 分頁並 `/mcp` 重連，不要繞過。

## 一定要記得的坑

- **不要用 `npx astro build --outDir X`**：npm 會吃掉參數、照樣寫進 `dist/`。平行建置用 `./node_modules/.bin/astro build --outDir X`，再 `BOOKLET_DIST=X uv run --script scripts/build_booklet.py --check`。
- **字級種類會讓 PDF 暴增**：Chrome 為每一種字級各嵌一份字型。大字版的逐章縮小只准用固定檔位（1／0.93／0.87），也不能用 CSS `zoom`（印出來會變點陣字型）。
- **樣式必須是全域的**：內容是 Markdown 用 `set:html` 塞進頁面，Astro 的 scoped `<style>` 套不到；樣式放在 `src/styles/*.css` 並在頁面 frontmatter import。
- **使用者要「大字」是指實際字級**：大字版不能用真正的 A5 紙（原尺寸或網頁上看字還是小）。它是 A4 紙、A5 版面 × √2。網頁上也要真的分頁，不能是一章一張長卡片。
- **A4、大字版、網站要長得一樣**：任何版面改動同時檢查兩個頁面與 `print.css`。
- **主題頁的站內連結要用完整網址**：EPUB 驗證器（epubcheck）不接受 `/hema-board-interview-guide/...` 這種絕對路徑。
- **主題頁有些內容來自考生實際被問的題目**：查證發現不精確時，保留原題、加上正確的限定，不要直接刪。
- **表格被自動補對齊空白**：寫完跑 `compact_tables.py`；版面量測要在最終格式下做。
- **其他 session 可能同時在這個工作目錄**：`ListAgents` 看同 repo 的 peer；用 SendMessage 協調誰 commit 哪些檔，commit 時用明確路徑。

## 發布確認

```bash
gh release download booklet-latest -p "*.pdf" -D /tmp/bk --clobber
uv run --with pypdf python -c "
from pypdf import PdfReader; import glob
for f in sorted(glob.glob('/tmp/bk/*.pdf')):
    r=PdfReader(f); p=r.pages[0]
    print(f, len(r.pages), 'pages', round(float(p.mediabox.width)/72*25.4), 'x', round(float(p.mediabox.height)/72*25.4), 'mm', len(r.outline), 'top bookmarks')"
```

兩個檔都應是 297 × 210 mm、有 3 個頂層書籤（正文／診斷標準總表／參考劑量總表）。網站有 CDN 快取，驗證線上頁面時在網址加 `?nc=$RANDOM`。
