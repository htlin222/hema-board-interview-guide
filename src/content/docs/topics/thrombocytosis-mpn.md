---
title: Thrombocytosis 與 MPN
sidebar:
  order: 14
---

門診題常見切入點，考的是「reactive 還是 clonal」的完整鑑別思路，以及 MPN 相關基因檢測的熟悉度。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 推理架構：thrombocytosis 三層過濾

1. **先排除 reactive（次發性）**：IDA、感染、發炎、post-splenectomy、malignancy paraneoplastic 這些常見誘因，臨床上 reactive 遠比 clonal 常見，順序上一定先排這個。
2. **確定是 clonal 之後，用 WBC differential 的「形態」分 CML 還是其他 MPN**：不用等基因報告，抹片形態就能先分方向——
   - **CML**：differential 會看到 basophilia、left shift、**各個成熟階段的顆粒球同時存在**（myeloblast 到 segmented neutrophil 一路都有），這是 CML 最具特徵性的抹片印象。
   - **ET / 其他 MPN**：differential 大致正常，主要異常集中在血小板數量本身，沒有 CML 那種「全階段顆粒球同時出現」的左移圖像。
3. **驅動基因檢測，用同一個機轉去理解三個基因**：JAK2、CALR、MPL 這三個基因的共同終點都是讓 **JAK-STAT 訊息傳遞路徑持續活化**，即使沒有 TPO 刺激骨髓也一直產血小板，但三者作用的位置不同——**MPL** 突變直接發生在 thrombopoietin receptor 本身，造成不需要配體就能活化受體；**CALR** 突變蛋白會結合並活化 MPL receptor，作用在受體這一層；**JAK2** 突變則是在受體下游、細胞內的酪胺酸激酶持續活化。理解「三個基因是用不同方式讓同一條路徑活化」之後，「為什麼驗這三個基因」「為什麼結果都指向同一個表現」就不用個別死記，是同一套邏輯的三個入口。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18"/><path d="M9 3v18"/><rect x="3" y="3" width="18" height="18" rx="2"/></svg> 速記表

**三層過濾的完整走法（對應開頭推理架構與 Q1、Q2）**

| 層次 | 要查什麼 | 看到什麼 | 判讀／下一步 |
| --- | --- | --- | --- |
| 第一層：排 reactive | 病史與誘因：IDA、感染、發炎、post-splenectomy、malignancy paraneoplastic | 找得到誘因 | reactive thrombocytosis；矯正 IDA 後追蹤 platelet 是否隨之下降 |
| 第一層：排 reactive | 同上 | 找不到誘因 | 才往 clonal 走；一開口就驗基因＝順序錯誤 |
| 第二層：抹片形態 | 周邊血液抹片 WBC differential | basophilia＋left shift＋myeloblast 到 segmented 各成熟階段顆粒球同時出現 | CML；此圖像特異度高，不用等基因報告 |
| 第二層：抹片形態 | 同上 | differential 大致正常，異常只集中在血小板數量本身 | ET／其他 MPN → 進第三層 |
| 第三層：驅動基因 | JAK2、CALR、MPL 三個一起驗 | 任一陽性 | 共同終點都是 JAK-STAT 路徑持續活化，無 TPO 刺激也一直產血小板 |
| 第三層：驅動基因 | 同上 | 三個都驗不到（triple-negative，約一成） | 基因陰性不能單獨用來排除 ET |

**JAK2／CALR／MPL 三個入口一次記（對應 Q3、Q4、Q5）**

| 基因 | ET 中比例 | 作用位置 | 臨床意義 |
| --- | --- | --- | --- |
| JAK2 | 最高，約 60–66% | 受體下游、細胞內酪胺酸激酶持續活化 | 血栓風險最高，10 年累積約 14.5% |
| CALR | 次之，約 19–27% | 突變蛋白結合並活化 MPL receptor，作用在受體這一層 | 血栓風險較低，10 年累積約 5% |
| MPL | 最少，約 3–4% | thrombopoietin receptor 本身，不需配體就能活化 | 與另兩者同屬一條路徑的不同變異位點 |
| Triple-negative | 約一成 | 三個基因都驗不到 | 不能因基因陰性就排除 ET |

**ET 風險分層的三個面向（對應 Q5）**

| 分層因子 | 內容 | 為什麼一定要講 |
| --- | --- | --- |
| 年齡 | 傳統分層因子 | 少講會被視為沒照 guideline 架構走一輪 |
| 血栓病史 | 過去有無血栓事件，傳統分層因子 | 同上 |
| 基因型 | JAK2 突變血栓風險約為 CALR 兩倍；JAK2 病人血小板數往往還更低卻風險更高，機轉可能與嗜中性球／血小板活化程度較高有關 | 這是獨立於年齡與病史的第三個因子，只答前兩項等於沒把基因檢測串到治療決策 |
| 三者合起來 | 依風險等級決定是否啟動 cytoreductive therapy | 分層講完才能合理銜接到治療決策 |

## 套用到實際問法

**Q1：起手式——門診病人發現 thrombocytosis，第一步怎麼查？**

**最佳答法**：先講「排除 reactive」這個第一動作，再順勢接著講第二步「靠 differential 形態學分方向」，把三層過濾架構的頭兩層一次講完，不要被問一句才答一句。**依照**「thrombocytosis 三層過濾」的架構，reactive 遠比 clonal 常見，所以起手式一定要先把常見誘因（IDA、感染、發炎、post-splenectomy、paraneoplastic）排除掉，再往 clonal 方向走。**因為**這題考的其實是「起手式」本身，考官要看的是你會不會一開口就跳去驗 JAK2、CALR、MPL——那樣代表思路順序錯誤；能主動接著講出「排除 reactive 之後才用抹片形態學分 CML 或 ET，不用等基因報告」，才顯示你對整個過濾架構有整體掌握，而不是只回答眼前這一步就停住。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「reactive 遠比 clonal 常見，起手式是先排除 reactive，不是急著驗 JAK2、CALR、MPL。」

</div>

擬答：
- **第一步：先問診、查病史，排除 reactive（次發性）thrombocytosis**
  - Reactive thrombocytosis 在臨床上遠比 clonal 常見，所以一定要先排除這個方向，不能一開始就往 MPN 想。
  - 常見誘因包括缺鐵性貧血（IDA）、感染、發炎反應、post-splenectomy 狀態，以及惡性腫瘤引起的 paraneoplastic thrombocytosis。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 陷阱：如果一開口就說要驗 JAK2、CALR、MPL，跳過排除 reactive 這一步，會顯得思路順序錯誤、跳太快。
- **第二步：排除 reactive 之後，才往 clonal 方向查，鑑別是 CML 還是 ET／其他 MPN**
  - 這一步先靠周邊血液抹片的 WBC differential 形態學來分方向，不用等基因報告出來才判斷。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「排除 reactive 之後，抹片上要看什麼線索來分 CML 還是 ET？」→ 看 basophilia、left shift、有沒有各成熟階段顆粒球同時出現這個 CML 特徵性圖像（見 Q2）。
- 「如果誘因是 IDA，怎麼確認 thrombocytosis 只是 reactive、不是合併 clonal？」→ 矯正 IDA 之後追蹤 platelet count 是否隨之下降；可連結〈缺鐵性貧血〉篇對 IDA 的 approach 邏輯。

</div>

**Q2：CML 與 ET 的 hemogram（differential）差異是什麼？**

**最佳答法**：先講「要找什麼」（basophilia、left shift、各成熟階段顆粒球同時出現這個 CML 特徵性圖像），再用「沒有這個現象」反推 ET/其他 MPN，用一個高特異度特徵做二分，而不是把兩種疾病的抹片描述分別背出來。**依照**「三層過濾」架構中「先靠形態學分方向、基因報告晚一步」的邏輯，把 CML 的抹片印象當成唯一的判斷錨點來組織答案最有效率。**因為**考官問的是鑑別診斷的思考效率——先講出 CML 那個獨有的「全階段顆粒球同時存在」左移圖像，再用「沒有這個現象」推論 ET，就展現出你懂得用單一高鑑別度特徵做分流，而不是把兩種疾病的描述各自死記、答起來零散又慢，也漏掉兩者之間真正的鑑別關鍵。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「先找 CML 那個『各成熟階段顆粒球同時出現』的左移圖像，看不到就直接往 ET／其他 MPN 想。」

</div>

擬答：
- **第一步：看 differential 有沒有 basophilia 跟左移（left shift）**
  - CML 的抹片會看到 basophilia、left shift，而且從 myeloblast 到 segmented neutrophil，各個成熟階段的顆粒球會同時出現在抹片上，這是 CML 最具特徵性的抹片印象。
- **第二步：如果 differential 大致正常，異常只集中在血小板數量本身**
  - 這種圖像比較符合 ET 或其他 MPN，因為它們沒有 CML 那種「各成熟階段顆粒球同時出現」的左移現象。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「抹片形態學看起來像 ET，接下來要驗哪些基因來確診？」→ JAK2、CALR、MPL 三個驅動基因（見 Q3）。
- 「為什麼可以先靠抹片形態學分方向、不用等基因報告？」→ 因為 CML「各成熟階段顆粒球同時出現」的左移圖像是高特異度特徵，抹片就能先分流，這正是三層過濾架構第二層的邏輯。

</div>

**Q3：疑似 ET 要驗哪些驅動基因？**

**最佳答法**：先講出三個基因的名稱與共同機轉（都落在 TPO receptor 訊息傳遞路徑下游），再主動補上三者的大致比例分布，不要等考官追問才擠牙膏。**依照**「用同一套機轉理解三個基因」的推理架構，JAK2、CALR、MPL 本來就是同一條路徑的三個入口，講機轉時三個名字自然會一起帶出來，不需要分開記。**因為**考官常用這題測試準備的周全度——只答得出 JAK2 屬於及格線，主動講出 CALR、MPL 以及「JAK2 最高、CALR 次之、MPL 最少」的比例分布，才顯示你不是只記得最常見的那一個基因，而是把整套基因檢測連同其背後的盛行率都摸過一輪，這正是這題拉開分數的地方。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「JAK2、CALR、MPL 一次驗齊，因為它們是同一條 TPO 訊息傳遞路徑的三個不同入口，不是三種獨立疾病。」

</div>

擬答：
- **第一步：疑似 ET 時要驗三個驅動基因——JAK2、CALR、MPL**
  - 這三個基因的共同點是都落在 thrombopoietin（TPO）receptor 訊息傳遞路徑的下游，突變後會讓這條路徑持續活化，即使沒有 TPO 刺激，骨髓也會持續製造血小板。
- **第二步：要主動講出各基因在 ET 病人中的大致比例分布**
  - JAK2 突變比例最高，約六成（60-66%）；其次是 CALR，約兩成（19-27%）；MPL 最少，約 3-4%；剩下約一成是三個基因都驗不到的 triple-negative。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 陷阱：只答得出「要驗 JAK2」，講不出 CALR、MPL 以及三者的大致比例分布，會被認為準備不夠周全——這題常被考官拿來評估準備得夠不夠細。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「這三個基因的機轉分別作用在受體路徑的哪個位置？」→ MPL 突變在受體本身、CALR 突變在受體外部活化、JAK2 突變在受體下游酪胺酸激酶（見 Q4）。
- 「如果三個基因都驗不到（triple-negative），代表什麼？」→ 約一成 ET 病人屬於這種情況，基因陰性不能單獨用來排除 ET 診斷。

</div>

**Q4：這些驅動基因的機轉是什麼？**

**最佳答法**：先講出三者共同的下游機轉這個大方向就夠，不必鑽進分子生物學細節，接著主動把「同一套邏輯的三個入口」這句收斂的話講出來作結。**依照**「用同一個機轉理解三個基因」的推理架構，JAK2、CALR、MPL 的機轉本質上是同一件事——讓 TPO receptor 訊息傳遞路徑持續活化，講到這個層次就已經足夠。**因為**考官要驗的是你有沒有把三個基因串成一套邏輯來理解，而不是逐一背誦各自的分子機轉細節；能主動說出「三個基因是同一條路徑的不同進入點」，才代表你是真的理解機轉而非死記基因清單，卡在 TPO pathway 這一層是可接受的深度，硬要往下鑽細節反而偏離這題真正想考的重點。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「JAK2、CALR、MPL 機轉都一樣——讓 TPO receptor 路徑持續活化，差別只在作用位置：受體上、受體外、受體下游。」

</div>

擬答：
- **第一步：講出三個基因的共同機轉——都造成 TPO pathway 持續活化**
  - JAK2、CALR、MPL 三個基因都位在 thrombopoietin receptor 訊息傳遞路徑的下游，突變的共同結果是讓這條路徑持續活化，講出這個大方向即可。
  - 細節考官通常會自己補充教學，不需要主動鑽到分子生物學層次的細節。
- **第二步：把三個基因串成同一套邏輯，不要個別死記**
  - 理解「都是同一條 TPO pathway 的不同進入點」之後，「為什麼要驗這三個基因」跟「為什麼結果都指向同一個表現」就是同一套邏輯的延伸，不需要分開硬背。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 陷阱：機轉問到 TPO pathway 就卡住是可以接受的深度，但至少要能講出這句大方向——三個基因是同一條路徑的不同進入點。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「JAK2 突變跟 CALR 突變在臨床上最重要的差別是什麼？」→ 血栓風險不同，JAK2 突變通常比 CALR 高（見 Q5）。
- 「既然三個基因機轉都指向同一條路徑，為什麼還要三個一起驗、不能只驗一個？」→ 因為三者是不同的變異位點，臨床意義（如血栓風險）不同，合計起來才涵蓋大部分 ET 病人（見 Q3 的比例分布）。

</div>

**Q5：ET 的風險分層與治療 approach 怎麼講？**

**最佳答法**：照 guideline 的架構把年齡、血栓病史、基因型三個面向完整講一輪，再對應到治療決策，不要跳著講或只挑一兩個因子回答。**依照**「風險分層決定治療」這種由診斷推向處置的臨床邏輯，三個分層因子要先講完整，才能合理地銜接到是否啟動 cytoreductive therapy 的決策。**因為**這題其實是把前面基因型的知識（JAK2 突變血栓風險高於 CALR 突變）收斂到臨床決策的最後一關，考官要看的是你會不會把基因型當成獨立於年齡、血栓病史之外的第三個分層因子一起納入考慮——只講傳統的年齡與血栓病史兩項，會顯得沒有把前面基因檢測學到的知識串聯到最終的治療決策上。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「血栓風險不是血小板數目說了算，基因型才是關鍵：JAK2 突變的血栓風險比 CALR 高，即使血小板數更低。」

</div>

擬答：
- **第一步：講出風險分層依據的三個面向——年齡、血栓病史、基因型**
  - 年齡跟過去有沒有血栓病史是傳統的分層因子。
  - 基因型也要納入考慮：JAK2 突變的血栓風險通常高於 CALR 突變，約為兩倍（研究顯示 10 年累積血栓發生率 JAK2 組約 14.5% vs CALR 組約 5%），且血栓風險不是單純由血小板數量決定——JAK2 突變病人的血小板數目往往還比 CALR 突變病人低，血栓風險卻更高，機轉可能跟嗜中性球/血小板活化程度較高有關。
- **第二步：依風險等級決定是否需要 cytoreductive therapy**
  - 建議直接照 guideline 的風險分層架構完整講一輪，把年齡、血栓病史、基因型三個面向都講到，再對應到是否啟動 cytoreductive therapy 的治療決策，而不是跳著講。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「為什麼 JAK2 突變病人血小板數目較低、血栓風險卻更高？」→ 血栓風險不是單純由血小板數量決定，機轉可能跟嗜中性球／血小板活化程度較高有關。
- 「一個年輕、無血栓病史、CALR 突變的病人，風險分層會怎麼歸類？」→ 傳統因子與基因型都偏向低風險，對應到「依風險等級決定是否需要 cytoreductive therapy」這一步，傾向不需要立即啟動治療。

</div>

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9.003a1 1 0 0 1 1.517-.859l4.997 2.997a1 1 0 0 1 0 1.718l-4.997 2.997A1 1 0 0 1 9 14.996z"/><circle cx="12" cy="12" r="10"/></svg> 相關 YouTube 影片

- **[Thrombocytosis: Hemostasis – Lesson 9](https://www.youtube.com/watch?v=bRY4qQYiEIk)** — Strong Medicine · 10:44
  - **對應「三層過濾」第一層**：reactive vs clonal 怎麼分、為什麼順序不能顛倒，跟本頁起手式的邏輯完全一致。
- **[Myeloproliferative Neoplasms (MPNs) – CML, PV, ET, PMF](https://www.youtube.com/watch?v=6GlEZgHZFEo)** — Medicosis Perfectionalis · 9:00
  - **對應第二層的 CML vs ET 定位**：把四個 MPN 放在同一張圖上比較，比單獨記 ET 一種疾病更容易分辨彼此。
- **[Essential Thrombocytosis (ET)](https://www.youtube.com/watch?v=g14v3jx5sCI)** — Medicosis Perfectionalis · 7:58
  - **對應第 3–5 題**：ET 的驅動基因與風險分層概念，看完再回來記 JAK2／CALR／MPL 的比例分布。
- **[Thrombocytosis (Primary and Secondary) – Why Is My Platelet Count High?](https://www.youtube.com/watch?v=2fVptmlkhJs)** — Medicosis Perfectionalis · 13:58
  - **對應「三層過濾」第一層**：primary（clonal）vs secondary（reactive）怎麼分，跟本頁起手式的分流完全同一套，可以當作這頁框架的影音版。
- **[Chronic Myeloid Leukemia (CML) – Philadelphia Chromosome](https://www.youtube.com/watch?v=aZz5idSKuEE)** — Medicosis Perfectionalis · 17:59
  - **對應第二層的 CML vs ET**：BCR-ABL1 怎麼造成那個「各成熟階段顆粒球同時出現」的抹片圖像，理解機轉之後形態學判讀就不是死記。
- **[Hematological Malignancies – Part 1b: Myeloproliferative Neoplasms](https://www.youtube.com/watch?v=eBy5NBf6SF4)** — AMBOSS · 7:19
  - **對應第二層的 clonal 分支**：把 CML／PV／ET／PMF 放在同一張分類圖上，先看清楚彼此的位置，再回頭記各自的驅動基因。
- **[Hematological Malignancies – Part 2B: Myeloproliferative Neoplasms](https://www.youtube.com/watch?v=bcC_LHzcY7g)** — AMBOSS · 4:54
  - **四分半的快速複習版**：適合考前一天把 MPN 這一格的分類重新掃一遍。

## 容易被電的點

- 只答得出「要驗 JAK2」，講不出 CALR、MPL 以及它們的大致比例分布，會顯得準備不夠周全。
- 機轉問到 TPO pathway 就卡住——這是可以接受的深度，考官通常不會逼到分子生物學細節，但至少要知道這個大方向（三個基因都是同一條路徑的不同進入點）。
