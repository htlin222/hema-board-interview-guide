---
title: ALL（急性淋巴性白血病）
sidebar:
  order: 19
---

ALL（acute lymphoblastic leukemia）在成人血液科門診相對少見，很多住院醫師的第一線臨床經驗都集中在 AML，但口試考的不是罕見度，而是**基本的診斷流程跟分子分型治療決策**有沒有建立起來。這篇要處理的是 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 沒有涵蓋、但同樣屬於基本題等級的獨立主題：急性白血病診斷不確定型別時怎麼辦、以及 Philadelphia chromosome 陽性 ALL 的治療決策。

<!-- doses:start -->
## 參考劑量

成人常規參考劑量，用來答「數量級、途徑、頻率、要監測什麼」；實際處方以仿單、健保規定與最新指引為準，特殊族群另行查核。與 [A4 手冊](https://htlin222.github.io/hema-board-interview-guide/booklet/) 的劑量總表同源。

| 藥物／Regimen | 情境 | 參考劑量 | 備註（監測、調整） |
| --- | --- | --- | --- |
| Imatinib | Ph+ ALL 加在化療骨幹 | 400–800 mg PO 每日（與化療併用常用 600 mg），持續至移植或維持期 | 誘導期即開始；追 BCR-ABL1 MRD |
| Dasatinib | Ph+ ALL（穿透 CNS 較佳） | 140 mg PO 每日（或 70 mg bid） | 肋膜積水；老年常搭配低強度化療 + steroid |
| Ponatinib | Ph+ ALL 一線（PhALLCON）或 T315I（補充） | 30 mg PO 每日，MRD 陰性後可減至 15 mg | 補充：動脈阻塞、胰臟炎、高血壓 |
| Hyper-CVAD（補充） | 成人 Ph− 或 Ph+ 骨幹 | A 療程：cyclophosphamide 300 mg/m² q12h ×6（d1–3）+ mesna、vincristine 2 mg d4、11、doxorubicin 50 mg/m² d4、dexamethasone 40 mg d1–4、11–14；B 療程：MTX 1 g/m² 24 h + cytarabine 3 g/m² q12h ×4；A/B 交替共 8 療程 | 補充：≥60 歲 cytarabine 減至 1 g/m²；leucovorin 救援；G-CSF |
| CNS 預防（補充） | 所有成人 ALL | IT MTX 12 mg ± cytarabine 70–100 mg ± hydrocortisone，每療程 1–2 次，共 8–16 次 | 補充：Ph+、T-ALL、高 LDH 風險較高 |
| 維持治療 POMP（補充） | 緩解後 2–3 年 | 6-MP 60 mg/m² PO 每日 + MTX 20 mg/m² PO 每週 + vincristine 1.4 mg/m² 每月 + prednisone 5 天每月 | 補充：Ph+ 併 TKI；TPMT／NUDT15 基因型影響 6-MP 劑量（東亞 NUDT15 常見） |
| Blinatumomab | Ph− B-ALL 鞏固（E1910）、MRD 陽性、R/R | R/R：第 1 療程 9 μg/day d1–7 → 28 μg/day d8–28 持續輸注，之後 28 μg/day ×28 天，休 14 天（42 天一療程）；鞏固／MRD+：28 μg/day ×28 天不需 step-up（<45 kg 用 15 μg/m²/day） | CRS、神經毒性；dexamethasone 前置；E1910：MRD 陰性者鞏固加 blinatumomab，OS 改善（HR 0.42） |
| Inotuzumab ozogamicin | R/R CD22+ B-ALL（補充） | 1.8 mg/m²/療程分 0.8（d1）、0.5（d8）、0.5（d15），CR 後 1.5 mg/m² | 補充：VOD/SOS 風險，移植前限 ≤2 療程 |
<!-- doses:end -->

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 推理架構：急性白血病診斷是同一套骨架，分層依據不同

[AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 提過急性骨髓疾病的共通決策順序是「確認診斷 → 風險分層 → 依分層決定治療強度」。ALL 走的是**完全相同的骨架**，差異在後面兩步的分層依據跟治療路徑：

1. **確認診斷**：臨床表現（貧血、血小板低下、感染傾向等骨髓衰竭症狀）→ 骨髓檢查看型態與 blast 比例 → **flow cytometry** 確認 lineage（lymphoid vs. myeloid）→ cytogenetics／分子檢測進一步分型。這一步跟 AML 完全共用同一套流程，型態學上曖昧不清時，flow cytometry 就是拿來拍板 lineage 的工具。
2. **分子分型分層**：AML 用 favorable/intermediate/high risk 的細胞遺傳學分層，ALL 則是先問**Philadelphia chromosome（t(9;22)/BCR-ABL1）陽性與否**——這是成人 ALL 治療分流最關鍵的第一個分岔點，其次才是其他細胞遺傳學與分子標記（如 MLL 重排、hypodiploidy 等）。
3. **依分型決定治療強度與藥物組合**：BCR-ABL1 陽性走「化療 + TKI」的組合路徑；陰性則走純化療為主的多階段療程（induction → consolidation → maintenance）。無論哪一種分型，成人 ALL 一旦達到緩解，都要積極評估**異體移植**的角色，這點跟 AML 裡「年輕、體能好、細胞遺傳學不利 → 提早轉向移植」的邏輯是相通的，只是 ALL 對移植的態度整體更積極。

換句話說，ALL 不是另一套要重新背的骨架，而是同一套「確認診斷→分層→決定強度」邏輯，套用到不同的分層工具（lineage 判定、Philadelphia chromosome 狀態）跟不同的藥物組合（化療±TKI）上。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18"/><path d="M9 3v18"/><rect x="3" y="3" width="18" height="18" rx="2"/></svg> 速記表

**型態不確定是 AML 還是 ALL 時，每個工具各自能回答什麼（對應第 1 題）**

| 工具 | 能回答什麼 | 不能回答什麼／下一步 |
| --- | --- | --- |
| 骨髓抹片型態 | 看 blast 比例與型態，形成初步印象 | 型態學上有時無法可靠區分 myeloid 與 lymphoid，曖昧時不要硬猜 |
| MPO（myeloperoxidase）染色 | 陽性支持 myeloid lineage（傾向 AML）；主動請病理科加做，臨床上常是更快先做的一步 | 陰性只代表不能排除 lymphoid，不等於排除 AML；仍屬初步篩選 |
| Flow cytometry 免疫分型 | 用細胞表面標記（myeloid vs. B／T lymphoid）拍板 lineage，是分辨 AML 與 ALL 最直接且決定性的工具 | 要口頭聯絡實驗室說明是型態不確定的緊急個案、請優先處理，不要被動等報告排隊 |

**Philadelphia chromosome 對應的疾病與相對常見度（對應第 2 題，最容易答反的陷阱）**

| 被問到什麼 | 正確答案 | 一句話理由 |
| --- | --- | --- |
| t(9;22)／BCR-ABL1 最典型對應哪個疾病 | CML 慢性期 | 這是定錨點，不管從 AML 側還是 ALL 側被問，都要先講出來再談機率 |
| BCR-ABL1 陽性的急性白血病裡，AML 還是 ALL 常見 | ALL 遠比 AML 常見 | 跟「Ph 染色體聽起來比較急、應該是 AML」的直覺相反，最常被答反 |
| 為什麼這個標記在 ALL 特別重要 | 成人 ALL 有相當比例是陽性，且直接決定要不要加 TKI | 它是成人 ALL 治療分流的第一個分岔點，重要性甚至高於在 AML 裡 |

**依 BCR-ABL1 狀態決定的治療路徑（對應第 3 題）**

| 分型 | 治療骨幹 | 緩解後 |
| --- | --- | --- |
| BCR-ABL1 陽性 ALL | TKI 為骨幹：ponatinib + 低強度化療（PhALLCON），或 chemo-free TKI + blinatumomab（D-ALBA 的 dasatinib-blina、MDACC 的 ponatinib-blina）；CNS 預防 IT 12–15 次不能省 | 改為 MRD 導向：早期深度分子緩解（IG/TR 或 NGS 陰性）且無高風險特徵者可不移植；MRD 持續陽性、IG/TR MRD+、WBC ≥30–70×10⁹/L、IKZF1-plus 者仍 allo-HCT |
| BCR-ABL1 陰性 B-ALL | Pediatric-inspired（CALGB 10403、GRAALL）或 hyper-CVAD 多階段化療；**MRD 陰性者鞏固期加 blinatumomab ×4（E1910）**；高風險（KMT2A-r、IKZF1del、MRD ≥10⁻⁴）亦加 blina | MRD 導向：MRD 持續陽性、KMT2A-r、hypodiploid／TP53、部分 Ph-like → 移植；MRD 陰性者不移植 |
| ≥60 歲 Ph− | INO 為基礎的減量或無化療方案（INO → blina、INO + dex 誘導、mini-hyper-CVD + INO） | 通常不移植 |
| T-ALL | 骨幹 + PEG-asparaginase，中高風險加 nelarabine（AALL0434） | ETP、MRD 持續陽性 → 移植 |
| 兒童 ALL（拿來對比） | 以化療為主，標準風險亦加 blina（AALL1731） | 移植角色相對保守 |

**成人 ALL 近三年關鍵試驗：口試要講得出「對照組是誰、贏了哪個終點」**

| 情境 | 試驗（年） | 實驗 vs 對照 | 主要終點 | OS | 口試怎麼講 |
| --- | --- | --- | --- | --- | --- |
| Ph− B-ALL、MRD 陰性 | E1910（NEJM 2024；FDA 2024-06 核准鞏固期） | Blinatumomab ×4 + 鞏固化療 vs 鞏固化療，30–70 歲 | 3 年 RFS 80% vs 64%，HR 0.53 | **3 年 OS 85% vs 68%，HR 0.41** | 「MRD 陰性者加 blina 仍有 OS 獲益，是第一個證明免疫治療改善 MRD 陰性病人 OS 的試驗；收的是 MRD 陰性，不是陽性。」 |
| Ph− B-ALL 高風險 | GRAALL-2014／B-QUEST（Blood 2026） | 鞏固／維持加 blina vs 歷史對照 | 5 年 CIR 23% vs 49%；DFS 68% vs 42% | 5 年 OS 79% vs 60% | 「高風險加 blina 後，真正做移植的人沒有額外 DFS 好處。」 |
| Ph+ 新診斷 | PhALLCON（JAMA 2024；FDA 2024-03 加速核准） | Ponatinib 30 mg vs imatinib 600 mg，皆 + 低強度化療 | Cycle 3 末 MRD 陰性 CR **34.4% vs 16.7%** | EFS 未成熟（NR vs 29 個月） | 「第三代 TKI 一線 MRD 陰性 CR 加倍；主要終點不是 OS，不要講成延長存活。」 |
| Ph+ chemo-free | D-ALBA（NEJM 2020；JCO 2024）；MDACC ponatinib-blina（JCO 2024；2025） | 單臂 | D-ALBA 4 年 OS 80.7%、DFS 75.8%，29/63 未化療未移植；pona-blina CMR 83–87%、3 年 OS 88–91%、60 人僅 2 人移植 | — | 「GIMEMA ALL2820 phase 3（pona-blina vs imatinib-化療）2025 年底讀出正向，正式 HR 待刊登；復發以 CNS 為主，IT 不能省。」 |
| Ph+ 要不要 CR1 移植 | Ghobadi（Blood 2022）；GRAAPH-2014（JCO 2024） | CR1 移植 vs 不移植（回溯 n=230）；MRD 分層 | 移植 OS aHR 1.05（復發 aHR 0.32 被 NRM aHR 2.59 抵銷）；IG/TR MRD ≥0.01% 才預測 DFS，BCR::ABL1 定量不預測（43% 多系殘留） | 高風險組移植 HR 0.33 | 「早期 CMR 者可不移植；IG/TR MRD 陽性或 WBC 高的高風險組移植仍有益。」 |
| MRD 陽性 CR | BLAST（Blood 2018；FDA 2018） | Blinatumomab 單臂 | MRD 完全反應 78% | 中位 OS 36.5 個月；反應者 NR vs 14.4 個月 | 「MRD+ 先用 blina 清除，再依風險移植。」 |
| ≥60 歲 Ph− | Alliance A041703（JCO 2025）；GMALL INITIAL-1（JCO 2024） | INO ×2 → blina ×4–5，無化療無維持；INO + dex 誘導 | CR 97%、1 年 EFS 75%；CR 100%、3 年 EFS 55% | 1 年 OS 85%；3 年 OS 73% | 「老年 ALL 的死因是感染與次發骨髓惡性，方向是用抗體取代化療。」 |
| R/R B-ALL | TOWER（NEJM 2017）；INO-VATE（2016）；ZUMA-3（3 年 2025）；FELIX（NEJM 2024；FDA 2024-11） | Blina vs 化療；INO vs 化療；brexu-cel、obe-cel 單臂 | Blina CR 34% vs 16%；INO CR/CRi 73.8% vs 30.9%、橋接移植 39.6% vs 10.5%、VOD 14%；brexu-cel CR/CRi 73%；obe-cel ORR 77%、CR 55%、≥G3 CRS 2.4% | Blina OS 7.7 vs 4.0 個月，HR 0.71；INO OS HR 0.75；brexu-cel mOS 25.6 個月 | 「Blina／INO 達 MRD 陰性後移植仍是標準鞏固；CAR-T 後要不要移植有爭議。」 |
| T-ALL | COG AALL0434（JCO 2020） | ± nelarabine，1–31 歲中高風險 | 5 年 DFS 88.2% vs 82.1%；CNS 復發 1.3% vs 6.9% | — | 「一線 nelarabine 的隨機證據來自兒童／AYA，成人沒有專屬 RCT。」 |

## 套用到實際問法

- **急性白血病型態不確定是 AML 還是 ALL 時，基本處理流程是什麼**
  - **最佳答法**：**依照**推理架構裡「確認診斷」這一步的邏輯，先講型態學不確定時不要憑印象猜測，而是要主動請病理科加做染色跟聯絡 flow cytometry 這兩個具體動作，把「怎麼確認」講清楚，而不是直接跳到治療。**因為**這題考的是基本臨床處置的直覺反應——考官要看你在型態學曖昧不清時，知不知道下一步該找誰、做什麼檢查，而不是要你憑經驗猜這個病人比較像哪一種白血病。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「型態不確定時我不猜，我主動請病理科加做 MPO 染色、同時電話通知 flow cytometry 優先處理。」——一開口就交代「找誰、做什麼」這兩個具體動作，不要停在「型態學不確定」這句描述上。

</div>

  - 擬答：
    - 遇到骨髓抹片型態上無法明確區分 AML 或 ALL 時，第一個動作是主動聯絡病理科，請他們加做細胞化學染色來幫忙區分 lineage。
      - 最常用的是 **MPO（myeloperoxidase）染色**：MPO 陽性支持 myeloid lineage（傾向 AML），陰性則不能排除 lymphoid lineage。
      - 這一步是型態學層次的初步篩選，還不是最終定論，但可以快速縮小方向。
    - 第二個動作是口頭聯絡 flow cytometry 實驗室，說明這是型態學不確定的緊急個案，請他們優先處理免疫分型。
      - Flow cytometry 用細胞表面標記（如 myeloid markers vs. B/T lymphoid markers）來確認 lineage，是目前分辨 AML 與 ALL 最直接且決定性的工具。
      - 主動口頭聯絡而不是被動等報告排隊，代表你理解這個診斷分歧會直接影響後續治療方向的選擇，時間上耽誤不起。
    - 回答時要把「先染色初篩、再靠 flow cytometry 拍板」這個順序講出來，而不是只講「做 flow cytometry 就好」，忽略掉染色這一步在臨床上其實常常是更快先做的動作。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「MPO 陰性能不能因此說這一定是 ALL？」→ 不行，MPO 陰性只代表不能排除 lymphoid lineage，最終仍要以 flow cytometry 的表面標記拍板，可對照 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 裡確認診斷的共通骨架。
- 「Flow cytometry 確診後是 AML，下一步你會做什麼？」→ 進入細胞遺傳學／分子檢測做風險分層，可連結 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 的 favorable/intermediate/high risk 分層邏輯。

</div>

- **t(9;22) transform 的急性白血病，AML 常見還是 ALL 常見**
  - **最佳答法**：**依照**[AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/)裡已經講過的「先定錨 Philadelphia chromosome 最典型對應 CML 慢性期，再回答相對機率」的順序，站在 ALL 這一側回答時，直接講出「BCR-ABL1 陽性的急性白血病中，ALL 遠比 AML 常見」這個結論，並補充這正是這個分子標記在 ALL 治療決策上特別重要的原因。**因為**這題是跟 AML 篇互相呼應的陷阱題，考官很可能在問完 AML 那一側的版本後，反過來從 ALL 這一側再問一次，測你答案會不會前後矛盾。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「BCR-ABL1 陽性的急性白血病裡，ALL 遠比 AML 常見——這跟直覺相反，千萬不要答反。」

</div>

  - 擬答：
    - Philadelphia chromosome（t(9;22)/BCR-ABL1）最典型對應的疾病是 CML 慢性期，這個定錨點不管從哪一側被問都要先講出來。
    - 在急性白血病的範圍裡，BCR-ABL1 陽性遠比較常見於 **ALL**，而不是 AML；成人 ALL 病人中有相當比例會是 Philadelphia chromosome 陽性，這也是為什麼這個分子標記在 ALL 的治療分型裡是第一個要問的問題。
      - 這跟直覺容易把 Ph 染色體聯想到「比較嚴重、比較急」的 AML 剛好相反，回答時要特別小心不要順著直覺答反。
    - 因為 BCR-ABL1 陽性在 ALL 裡的盛行率不低，且直接牽動後續要不要加 TKI 的治療決策，這個分子標記在 ALL 的重要性甚至比在 AML 裡更高。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「Philadelphia chromosome 最典型對應哪一個疾病？」→ 直接定錨在 CML 慢性期，可對照 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 裡對這個染色體異常的原始定義。
- 「確認這個 ALL 是 BCR-ABL1 陽性之後，治療會怎麼改變？」→ 直接銜接下一題（加 TKI，緩解後評估異體移植）。

</div>

- **BCR-ABL1 陽性 ALL 的治療重點是什麼，移植的角色在哪裡**
  - **最佳答法**：**依照**推理架構裡「依分型決定治療強度與藥物組合」的邏輯，先講「BCR-ABL1 陽性就要加 TKI」這個最核心的分流決策，再往下講移植在達到緩解後的角色，兩層分開講、不要混在一起講成一句籠統的「積極治療」。**因為**這題考的是治療原則有沒有內化成邏輯而不是背誦——能講出「陽性就加 TKI」跟「緩解後評估移植」是兩個獨立但連續的決策點，才顯示真的理解成人 ALL 的治療脈絡。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「BCR-ABL1 陽性就加 TKI，緩解後就積極評估異體移植——這是兩個獨立但連續的決策點，不要混成一句『積極治療』。」

</div>

  - 擬答：
    - Philadelphia chromosome（BCR-ABL1）陽性的 ALL，治療上的重點就是以 **TKI** 為骨幹，這是這個分型底下最關鍵的一個決策。現在的一線首選是第三代 **ponatinib**：PhALLCON（JAMA 2024）對 imatinib 600 mg 都加低強度化療，cycle 3 末 MRD 陰性 CR 34.4% vs 16.7%，FDA 2024 年 3 月加速核准；另一條路是 **chemo-free**——TKI 加 blinatumomab（D-ALBA 的 dasatinib-blina 4 年 OS 80.7%，MDACC 的 ponatinib-blina 3 年 OS 約 90%、60 人只有 2 人移植），phase 3 GIMEMA ALL2820 已讀出正向。
      - TKI 針對的是驅動這個白血病的 BCR-ABL1 融合蛋白，加上 TKI 可以提升緩解率與反應深度，這跟 CML 裡 TKI 的角色概念上是相通的，只是在 ALL 是搭配化療一起使用，而不是單獨作為主要治療。
    - 成人 ALL 達到緩解後要評估**異體移植**，但現在是 **MRD 導向**而不是一律移植：Ph+ 早期達深度分子緩解（IG/TR 或 NGS MRD 陰性）且無高風險特徵者，CR1 移植沒有 OS 好處（Ghobadi，230 人回溯：復發減少被 NRM 增加抵銷，aHR 1.05）；IG/TR MRD 陽性或 WBC 高的高風險組移植仍有益（GRAAPH-2014，HR 0.33）。要注意 Ph+ 的 MRD 要看 IG/TR 或 NGS，BCR::ABL1 定量有 43% 是多系殘留、不預測預後。這跟兒童 ALL 以化療為主、移植角色相對保守的態度仍然不同，但差距已縮小。
      - 回答時可以主動點出這個「成人 vs. 兒童 ALL 治療態度不同」的對比，展現你知道年齡層會影響移植角色的權重。
    - 整體邏輯是：先確認診斷跟 lineage、再看 Philadelphia chromosome 狀態決定要不要加 TKI、達到緩解後再評估移植——跟推理架構裡「確認診斷→分層→決定強度」完全對應，只是每一步換成 ALL 專屬的分層工具跟藥物選擇。

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「成人跟兒童 ALL 對移植的態度為什麼不同？」→ 成人 ALL 整體預後相對兒童較差、緩解後復發風險較高，因此傾向積極評估移植；兒童 ALL 以化療為主，移植角色相對保守。
- 「如果這個病人 BCR-ABL1 陰性，治療路徑會有什麼不同？」→ 走以化療為主的多階段療程（induction → consolidation → maintenance），不需常規加 TKI；**MRD 陰性者鞏固期加 blinatumomab ×4**（E1910：3 年 OS 85% vs 68%，HR 0.41，FDA 2024 核准）；緩解後依 MRD 與高風險特徵（KMT2A-r、hypodiploid／TP53、MRD ≥10⁻⁴）決定移植，可對照 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 的 MRD 導向邏輯。
- 「E1910 收的是 MRD 陽性還是陰性的病人？」→ **陰性**（flow <0.01%）；MRD 陽性的證據是 BLAST（單臂，MRD 反應 78%，FDA 2018）。兩者族群、設計、終點都不同，混在一起是最常見的講錯。
- 「六十幾歲的 Ph− ALL 你會怎麼打？」→ 用 inotuzumab 為基礎的減量或無化療方案：A041703（INO ×2 → blina ×4–5，完全無化療，1 年 OS 85%）、INITIAL-1（INO + dex 誘導，3 年 OS 73%）；老年死因是感染與次發骨髓惡性，所以化療越少越好。
- 「復發的 B-ALL 有哪些選項？」→ 依 CD19／CD22 與前線暴露選：blinatumomab（TOWER OS 7.7 vs 4.0 個月，HR 0.71）、inotuzumab（INO-VATE CR/CRi 73.8% vs 30.9%，注意 VOD 14%、移植前限 ≤2 療程）、CD19 CAR-T（brexu-cel ZUMA-3 mOS 25.6 個月；obe-cel FELIX ORR 77%、≥G3 CRS 只有 2.4%，FDA 2024-11）；達 MRD 陰性後移植仍是標準鞏固。

</div>

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9.003a1 1 0 0 1 1.517-.859l4.997 2.997a1 1 0 0 1 0 1.718l-4.997 2.997A1 1 0 0 1 9 14.996z"/><circle cx="12" cy="12" r="10"/></svg> 相關 YouTube 影片

- **[Acute Leukemia – ALL and AML](https://www.youtube.com/watch?v=Uyp6WLVsnys)** — Medicosis Perfectionalis · 13:10
  - **對應第 1 題**：把 ALL 與 AML 放在一起對照，型態、免疫表型、臨床表現的差異一次看清楚，正是「型態不確定時怎麼辦」那題的背景。
- **[Acute Lymphoblastic Leukemia (ALL) – Symptoms, Pathogenesis, Diagnosis](https://www.youtube.com/watch?v=IN2MtisTzC0)** — Medicosis Perfectionalis · 16:04
  - **對應診斷流程**：從臨床表現到骨髓、flow cytometry、細胞遺傳學的完整順序，跟本頁推理架構第一步相同。
- **[Acute Lymphoblastic Leukemia (ALL) – Treatment](https://www.youtube.com/watch?v=SBDZtArHViE)** — Medicosis Perfectionalis · 9:29
  - **對應第 3 題**：ALL 的療程分期（induction／consolidation／maintenance）以及 Ph 陽性要加 TKI 的道理。
- **[Acute Leukemia: Etiology & Subtypes – Pathology](https://www.youtube.com/watch?v=TXP8dwAA3kk)** — Lecturio Medical · 19:30
  - **對應第 1 題的病理背景**：ALL 與 AML 的亞型分類與病理特徵講得比一般教學影片深，看完再回來看「型態不確定怎麼辦」那題會更有把握。

## 容易被電的點

- 把 t(9;22) transform 的常見度答反，講成「AML 比較常見」，忽略了 BCR-ABL1 陽性急性白血病其實是 ALL 遠比 AML 常見這件事——這跟 [AML/MDS/CML 篇](/hema-board-interview-guide/topics/aml-mds-cml/) 裡從 AML 角度問的同一個陷阱是同一題,只是問法反過來。
- 型態學不確定 AML/ALL 時直接跳去講治療，漏掉「先染色、再聯絡 flow cytometry 確認 lineage」這個基本處置流程，讓答案顯得沒有章法。
- 只講得出「BCR-ABL1 陽性要加 TKI」，卻講不出成人 ALL 緩解後移植角色這一段，讓答案停在一半，沒有把治療路徑講完整；或反過來說「Ph+ 一律 CR1 移植」——TKI + blinatumomab 時代已改 MRD 導向。
- 把 E1910 講成「MRD 陽性者加 blina」：E1910 收的是 MRD 陰性者，主要終點是 OS（HR 0.41）；MRD 陽性的證據是 BLAST。
- 把 PhALLCON 講成「ponatinib 延長 OS」：主要終點是 cycle 3 末 MRD 陰性 CR（34.4% vs 16.7%），EFS 尚未成熟，對照組是 imatinib 600 mg。
- 說「免疫治療可以省掉 IT」：blina／INO 對 CNS 穿透差，chemo-free 方案的復發以 CNS 為主，IT 12–15 次不能省。
