# A4 手冊（booklet）寫作規範

同一份內容也會建成平板大字版（`/booklet-a5/`，`src/pages/booklet-a5/`、`src/styles/print-a5.css`）：同樣是 A4 橫式，但每頁只放約半張內容、字約 1.5 倍，每章自動分頁，不需要另外寫。只要 A4 版每頁塞得下，大字版一章大約就是兩頁。

`src/booklet/pages/*.md` 每一個檔案 = 一張**橫式** A4（297×210 mm）。由 `src/pages/booklet/index.astro` 依檔名順序渲染成 `/booklet/`，
再由 `scripts/build_booklet.py` 印成 PDF 並檢查每一頁有沒有溢出。

`src/booklet/criteria/*.md` 是**診斷標準的唯一來源**，手冊末尾的「診斷標準總表」由它拼出，主題頁的「診斷標準」段落也由 `scripts/sync_doses.py` 從這裡注入。每份先放一個第一性原理框（這組疾病的診斷必須證明哪幾件事），每條標準都要對應回其中一件；WHO 2022 與 ICC 2022 不同就並列。內容一張放不下時可在中間放 `<!-- page -->`，後半段進「（續）」張（只有 CRITERIA_SHEETS 裡有續張的組別可用，見 `src/lib/booklet-data.ts`）。

`src/booklet/doses/*.md` 是**藥物參考劑量的唯一來源**：手冊末尾的劑量總表由它拼出來，
主題頁的「參考劑量」段落也由 `scripts/sync_doses.py` 從這裡注入（檔名對應 `src/content/docs/topics/<slug>.md`）。

## 每頁的固定結構

```markdown
---
title: IDA（缺鐵性貧血）
kicker: 04 · 貧血
site: iron-deficiency-anemia # 對應主題頁 slug，可省略
---

<div class="fp"><b>第一性原理</b>　一句話，講出這一章所有分岔都從哪個生理事實推出來。</div>

## MECE 分岔

| 層 | 問什麼 | 分支（互斥、窮盡） | 決定了什麼 |
| … |

## 速記表

（一到三張表）

## 破題關鍵句

| 題 | 一開口就講 |

## 容易被電

- 三到五條，一行一條
```

## 版面：橫式、斑馬紋、並排

- 橫式是為了讓表格多放幾欄、一列不折行；表格奇偶列自動不同灰底，方便橫向對齊同一列。
- 高度比直式少三成，所以用寬度換高度：「破題關鍵句」＋「容易被電」兩段自動並排成兩欄。
- 其他短段落要並排時，在該段 `## ` 標題**之前**的段落結尾寫一行 `<!-- pair -->`，這段就會跟下一段並排（見 `src/lib/booklet.ts` 的 `layoutSheet`）。
- 樣式在 `src/styles/print.css`，手冊、每章速查（`/handout/`）與 release 的 PDF 共用這一份，改一處三處一起變。它是全域樣式：內容是 Markdown 轉出後用 set:html 塞進去的，scoped 樣式套不到。
- 每章速查的內容由主題頁自動抽取、長度不固定，所以它不做溢出檢查，而是頁面載入時把內容等比例縮到剛好一張。

## 密度與長度

- 字體 8pt、表格 7.1pt。寫完一定要跑 `npm run build && npm run build:booklet`，溢出的頁會被腳本點名。
- 只用表格與條列，不寫段落。一格最多兩句。
- 擬答、影片、「依照…因為…」的說理不進手冊——那些留在網站。手冊留的是**能自己生出答案的東西**：第一性原理、分岔、切點數字、破題句、陷阱。
- 可以用 `<div class="two">…</div>` 把一段排成兩欄；表格通常不要放進兩欄。

## 第一性原理 + MECE 的意思

- **第一性原理**：不是「口訣」，是一個站得住的生理或邏輯事實（例：人體沒有主動排鐵機制；ITP 沒有任何 checkpoint test）。整章的分岔要能從它推出來。
- **MECE**：每一層分岔的分支要**互斥**（一個病人只會落在一支）且**窮盡**（沒有病人落在分支外）。如果原本的清單不 MECE（例如把「診斷有誤」跟「順從性」平列），就重新切成一個乾淨的二分或三分，再把原本的項目掛到分支底下。
- 每一層只問**一個**問題；問題的答案直接決定下一步要 order 什麼或選哪條治療路徑。

## 劑量檔（`doses/<slug>.md`）

```markdown
| 藥物 | 適應症／情境 | 參考劑量 | 備註（監測、調整） |
```

- 成人劑量、常規給法；特殊族群只寫最常被問的一句。
- 只列主題頁**有提到**的藥；若為了讓一張表可用而補了主題頁沒提的藥，在備註標「補充」。
- 所有數字都是參考值，頁尾統一放免責聲明，表內不重複寫。

## 平行寫稿

幾個人（或幾個 agent）同時寫不同頁時，各自建到不同目錄再量，避免互相覆蓋 `dist/`：

```bash
./node_modules/.bin/astro build --outDir dist-me     # 注意：`npx astro build --outDir` 會被 npm 吃掉參數
BOOKLET_DIST=dist-me uv run --script scripts/build_booklet.py --check
```
