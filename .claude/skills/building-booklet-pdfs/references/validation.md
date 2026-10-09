# OpenEvidence 逐頁驗證：任務說明範本與收尾

## 目錄
- 派工方式
- 任務說明範本（存成 scratchpad 檔，每個 subagent 的 prompt 指向它）
- 每個 subagent 的 prompt
- 主控收尾

## 派工方式

- 一頁一個 `general-purpose` subagent，同一則訊息平行派出；同時上限 20 個，超過的等第一個完成再補。
- 劑量總表一張由數個 `doses/<slug>.md` 組成，派工以「張」為單位，指定它只能改哪幾個檔。
- 用量上限（429 weekly limit）會中斷一批 subagent：重派時在說明裡加「接手說明」，要它先 `git diff -- <檔>` 看半完成的修改，對的保留、錯的改回。
- subagent 若回報檔案被改名或多出新頁，代表有別的 session 在改 repo：`ListAgents` 找同 repo 的 peer，用 SendMessage 協調。

## 任務說明範本

```markdown
# 手冊單頁驗證任務（共用說明）

Repo：<repo 路徑>。手冊在 `src/booklet/pages/NN-*.md`（每檔＝一張橫式 A4），劑量在 `src/booklet/doses/<slug>.md`，
診斷標準在 `src/booklet/criteria/<slug>.md`。寫作規範見 `src/booklet/README.md`，先讀它。完整原文在
`src/content/docs/topics/<site>.md`（頁面 frontmatter 的 `site:`）。

## 你要做的三件事

1. 醫學正確性（用 OpenEvidence 查證）
   - 先 ToolSearch `select:mcp__openevidence__oe_ask`，呼叫時 `wait_for_completion: true`、`timeout_sec: 240`。
   - 挑這頁最容易錯、最常被追問的主張：切點、比例、試驗名稱與結果、劑量、分類定義、指引版本。
     一次打包 3–6 個主張、用英文問、要求逐條回答附依據。最多 4 次 oe_ask；追問用 `original_article_id`。
   - OE 明確反駁 → 改；OE 說有條件或已過時 → 改成現行說法或加限定；OE 沒提到 → 保留，不要憑空改。
2. MECE 檢查
   - 每張分岔表：每層只問一個問題？分支互斥且窮盡？由頁首第一性原理推得出來？
   - 常見毛病：不同層級平列（病名與機轉混在一欄）、同一項出現在兩支、漏一整類、「其他」垃圾桶分支。
     修法是重切成乾淨的二分或三分，再把原項目掛到分支下。
   - 速記表、破題句、容易被電有沒有跟分岔表或其他頁互相矛盾。
3. 修改：只改有問題的地方，不重寫整頁、不改風格、不擴寫。新增的非主題頁內容標「（補充）」。

## 版面驗證（必做）

./node_modules/.bin/astro build --outDir dist-v-<頁碼> 2>&1 | grep -iE " error|Complete"
BOOKLET_DIST=dist-v-<頁碼> uv run --script scripts/build_booklet.py --check 2>&1 | grep -E "p ?<頁碼> "
- 不要用 npx astro（會吃掉 --outDir）。你那頁要 ok 且剩 ≥20px；溢出就刪次要字句，不刪切點數字。
- 做完 `rip dist-v-<頁碼>`（不能用 rm）。表格維持緊湊 `| a | b |`，被補對齊空白就改回。
- 只准改你負責的檔案，不要 commit，不要跑 sync_doses。

## 最後回報（繁體中文，精簡）
- 修改清單：每條一行「原本 → 改成｜依據 https://www.openevidence.com/ask/<article_id>」；MECE 結構修改另列。
- 查證了但沒改的重點主張（一行帶過）。
- 最終剩餘 px。
```

## 每個 subagent 的 prompt

一行指向說明檔，再加這一頁的重點，例如：

> 先讀 <說明檔路徑> 並照做。你負責第 07 頁：`src/booklet/pages/07-ttp-tma-evans.md`。頁碼 07。重點查證：ADAMTS13 切點、PLASMIC 切點、caplacizumab 與 rituximab 在現行指引的地位、TMA family 內部鑑別。

撰寫新的診斷標準時同樣模式，但說明檔改成「產出 criteria/<slug>.md」，並要求每條標準對回第一性原理、WHO 2022／ICC 2022 並列、可用 `<!-- page -->` 續張（限已定義續張的組別）。

## 主控收尾

```
- [ ] 讀每份回報：subagent 指出跨頁不一致（例如劑量表與正文寫法不同、主題頁仍是舊說法）就由主控統一修
- [ ] 清掉殘留的 dist-v-*／dist-c-* 建置目錄
- [ ] compact_tables.py 跑過所有改動的 md
- [ ] npm run sync:doses
- [ ] npm run build && npm run build:booklet，全部 ok
- [ ] 有 peer session 時：把提交版本抽到 `git worktree add --detach <tmp> HEAD`、在裡面 `npm ci` 後建置檢查（不要 symlink node_modules，Astro 會壞）
- [ ] git add 明確路徑 → commit（訊息寫重要修正與依據）→ push → 等 CI 全綠 → 下載 release PDF 確認
```
