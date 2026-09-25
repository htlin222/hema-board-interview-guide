# 血液科口試走向指南

整理歷屆血液專科醫師考試「口試」關卡的考生心得，**去名化後**只保留考試走向本身：主題分布、典型問答流程、答題心法。不含任何真實考官／考生姓名或針對特定個人的評論。

僅供準備血液專科口試參考，非官方資料，實際考試內容以主辦單位公告為準。

網站：<https://htlin222.github.io/hema-board-interview-guide/>

## 內容怎麼組織

12 個主題章，每章的結構固定：

| 段落              | 作用                                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 推理架構          | 可重複套用的邏輯，讓沒背過的案例也能自己推                                                                             |
| 診斷標準          | 各疾病的診斷標準（WHO 2022／ICC 2022 等），先講第一性原理再列切點；與手冊的診斷標準總表同源（`src/booklet/criteria/`） |
| 參考劑量          | 章內提到的藥物的成人常規劑量，與 A4 手冊的劑量總表同源（`src/booklet/doses/`）                                         |
| 破題關鍵句        | 一開口就該講的那一句                                                                                                   |
| 最佳答法          | 用「依照…因為…」講出這樣答的道理                                                                                       |
| 擬答              | 巢狀條列，可直接照著唸                                                                                                 |
| 追問              | 考官接下來最可能問什麼                                                                                                 |
| 速記表            | 考前掃一眼用（全站 43 張）                                                                                             |
| 容易被電的點      | 常見失分處                                                                                                             |
| 相關 YouTube 影片 | 82 支，全部經 oEmbed 驗證存在                                                                                          |

醫學內容經 OpenEvidence 逐項查證，修正過的地方以指引與試驗數據為準。

## 五種產物

| 產物                       | 位置                                                                            | 建置                                                          |
| -------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 網站                       | GitHub Pages                                                                    | `npm run build`                                               |
| 一頁速查（可列印 A4 橫式） | 站內 `/handout/`                                                                | 同上，由主題頁即時抽取；版面與手冊共用 `src/styles/print.css` |
| A4 手冊（27 頁 PDF）       | 站內 `/booklet/`；[release `booklet-latest`](../../releases/tag/booklet-latest) | `npm run build && npm run build:booklet`                      |
| 平板大字版手冊（PDF） | 站內 `/booklet-a5/`；同一個 release                                             | 同上，跟 A4 版一起建置                                        |
| EPUB（Kindle 相容）        | [release `epub-latest`](../../releases/tag/epub-latest)                         | `npm run build:epub`                                          |
| Anki 牌組（巢狀）          | [release `anki-latest`](../../releases/tag/anki-latest)                         | `npm run build:anki`                                          |

EPUB 與 Anki 都由主題頁的 markdown 直接產生，內容一改、workflow 會自動重建並覆蓋 release 資產，不需要人工同步。

A4 手冊是另外手寫的（`src/booklet/pages/`，每檔一張 A4），不是主題頁的列印版：每章重新用「第一性原理 → MECE 分岔 → 速記表 → 破題關鍵句 → 容易被電」壓成一頁，末尾是診斷標準總表與參考劑量總表。診斷標準與劑量分別只維護在 `src/booklet/criteria/`、`src/booklet/doses/`，`npm run sync:doses` 會把兩者注入各主題頁的「診斷標準」「參考劑量」段落，`npm run check:booklet` 會量每一頁有沒有溢出。寫法見 `src/booklet/README.md`。

平板大字版（`/booklet-a5/`，網址沿用舊名）讀同一份 `src/booklet/`，不另外寫內容：紙張同為 A4 橫式，但等於把每張 A4 切一半放大成一整頁，字約為 A4 版 1.5 倍；每章從新的一頁開始、內容自動往下流，一章大約兩頁。某章只多出一小截時，頁面會把那章字級調小一檔收回整數頁。改 A4 手冊的內容，大字版重新建置就同步。

## 本機開發

```bash
npm install
npm run dev
```

需要 [uv](https://docs.astral.sh/uv/) 才能跑 EPUB／Anki／圖檔的建置腳本（腳本用 PEP 723 內嵌相依，不必另外建 venv）。EPUB 另需 `pandoc`。

## 檢查

```bash
npm run verify:videos     # 對每個 YouTube 連結重打 oEmbed，確認沒有失效
epubcheck dist-epub/hema-board-interview.epub
```

影片連結的驗證是對**建置產物**重跑，而不是信任策展時的紀錄——實際抓到過漏驗的項目。

## 部署

Push 到 `main` 會觸發三個 workflow：網站部署到 GitHub Pages、EPUB 與 Anki 牌組重建並更新對應的 release。
