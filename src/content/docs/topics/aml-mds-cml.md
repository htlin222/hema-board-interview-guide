---
title: AML / MDS / CML 治療決策
sidebar:
  order: 18
---

這三個診斷考的重點都不是型態學（那是跑台的範圍），而是**診斷後的決策流程**。三者都套 [lymphoma 篇](/hema-board-interview-guide/topics/lymphoma-treatment-lines/) 提過的「先分期/分層、再決定治療強度」骨架，只是分層工具跟後續路徑不同。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 推理架構：急性骨髓疾病的共通決策順序

1. **確認診斷**：臨床表現 → 骨髓檢查 → flow cytometry → cytogenetics／基因突變檢測。
2. **風險分層**：依 favorable／intermediate／high risk 分層——這一步決定接下來要多積極。
3. **依分層決定治療強度**：高風險/年輕體能好 → 傾向 intensive chemotherapy 甚至提早轉向移植；風險較低或體能差 → 傾向 less intensive 或先觀察。

同一套「確認診斷→分層→決定強度」順序也適用 MDS（用 IPSS score 分層），只是 CML 的路徑不同——CML 不是靠分層決定治療強度，而是**幾乎所有病人一律先用 TKI**，分層概念換成監測治療反應的 milestone。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18"/><path d="M9 3v18"/><rect x="3" y="3" width="18" height="18" rx="2"/></svg> 速記表

**三個疾病各自用什麼分層、治療怎麼決定（對應「推理架構」與下面 AML／MDS／CML 三節）**

| 疾病 | 分層／監測工具 | 治療怎麼決定 | 這頁的招牌陷阱 |
| --- | --- | --- | --- |
| AML | 誘導強度看 **fitness**（Ferrara criteria）；移植與否看 **ELN 2022 分層 × MRD × TRM** | 兩個問題分開答：fit 才給 7+3（>75 歲為相對禁忌），但 fit 不等於會獲益（TP53／複雜核型考慮 Ven+HMA）；移植門檻是「不移植復發風險 >35%」 | 把兩個問題混成一句「年輕體能好就打化療、順便早點評估移植」——favorable risk 反而不該在 CR1 移植 |
| MDS | IPSS risk score；加上兩次骨髓報告之間 blast 比例的變化趨勢 | 分層低 → best supportive care 或 clinical trial；分層高 → hypomethylating agent（azacitidine），也可能考慮 allogeneic transplant | 只看第一次骨髓報告的靜態數字，漏掉 blast 上升代表的疾病演進 |
| CML | 不靠分層決定強度，改看 BCR-ABL1 分子反應的 milestone | 幾乎所有病人一律先用 TKI，再依 milestone 有沒有達標調整 | 只說「要定期監測分子反應」，講不出具體切點 |

**AML 兩個決策分開看（對應 AML 段落第一個論點）**

| 問題 | 判準 | 怎麼分 |
| --- | --- | --- |
| 誘導給多強 | **Fitness**，不是年齡 | 不建議 7+3：>75 歲（相對禁忌）、或符合 Ferrara criteria 的 unfit（ECOG PS ≥3、EF ≤50%、DLCO/FEV1 ≤65% 或需氧、需腎替代、Child-Pugh B/C、難治感染、需住院精神疾病） |
| 誘導給多強（進階） | Fitness 過關**不等於**會獲益 | TP53 突變、複雜核型即使 fit，長期預後仍差 → 趨勢改用 venetoclax + HMA 或標靶治療取代 7+3 |
| 緩解後移植？Favorable | CBF、NPM1mut/FLT3-ITD wt、CEBPA bZIP | **不建議 CR1 移植**；首選 3–4 療程高劑量 cytarabine 或 auto-HCT。**但 MRD 持續陽性 → allo-HCT** |
| 緩解後移植？Intermediate | 無共識，個別化 | MRD 陰性 → 化療／auto-HCT 即可；**MRD 陽性 → allo-HCT** |
| 緩解後移植？Adverse | 生物學本身就決定 | **CR1 即移植，不論 MRD**，除非 TRM 過高 |
| 整體門檻與反例 | 復發風險 vs 移植風險對沖 | 不移植復發風險 **>35%** 才考慮 allo-HCT；反過來 **MRD 陰性者可能因 NRM 上升而使移植獲益消失甚至為負**。共病用 HCT-CI 量化 |

**一線 TKI 怎麼依共病選（對應 CML 段落「TKI 治療策略：一線藥物與副作用比較」）**

| 藥物 | 招牌副作用／要監測什麼 | 共病上的取捨 |
| --- | --- | --- |
| 選藥大原則 | 第二代 TKI 通常更快達到更深的分子學反應，但副作用型態不同 | 不是一律優先選二代，要依病人共病權衡 |
| Imatinib | 腸胃道不適、水腫（periorbital／下肢）、肌肉痠痛；長期使用資料最多、耐受性整體不錯 | 有肺部病史而要避開 dasatinib 時的可考慮選項 |
| Dasatinib | 肋膜積水（pleural effusion）；長期使用有肺動脈高壓的顧慮 | 有肺部／心臟病史的病人要謹慎選用 |
| Nilotinib | QT 波間期延長、心血管／動脈阻塞性事件（周邊動脈疾病、心肌梗塞）；用藥前後監測心電圖、血糖、血脂；可能誘發高血糖與胰臟炎；服藥時間需注意進食（影響吸收與 QT 交互作用） | 有心血管病史的病人要避開 |
| Bosutinib | 腹瀉；需留意肝毒性 | — |

**CML 從治療中到停藥的時間軸（對應 CML 段落「milestone 監測時程」與「停藥策略 TFR」）**

| 時間點 | 目標／要做的事 | 沒達標或復發怎麼辦 |
| --- | --- | --- |
| 3 個月 | BCR-ABL1 IS ≤ 10% | 屬 failure／warning：先查服藥順從性、藥物交互作用，再考慮換藥或加驗 BCR-ABL1 kinase domain mutation |
| 6 個月 | BCR-ABL1 IS ≤ 1% | 同上 |
| 12 個月 | 達到 major molecular response（MMR，≤ 0.1%） | 同上 |
| 考慮停藥（TFR）前 | 第一次慢性期（無加速期／芽細胞期病史）、先前治療沒有失敗過、TKI 總時間滿 5 年（用過二代 TKI 可縮短到滿 4 年）、有高品質快速標準化的 qPCR 監測能力，且分子反應達 MR4.5 深度並維持至少 2 年 | 條件不是只看「反應夠深」，任一項不滿足就不啟動停藥 |
| 停藥後 0–6 個月 | 每月監測一次 | 一旦復發要及時重新啟動 TKI |
| 停藥後 6–12 個月 | 每 2 個月監測一次 | 同上 |
| 停藥後 12 個月以後 | 可拉長到每 3 個月一次 | 同上 |

## AML

- **決策點：哪些病人適合 intensive chemotherapy、哪些病人要轉向移植**
  - **最佳答法**：把這題**拆成兩個獨立的問題**分開答，是拉開分數最有效的方式——(1) 誘導治療給多強？看的是 **fitness**；(2) 緩解後要不要移植？看的是**疾病生物學 + MRD**。**依照**「這兩個問題用的判斷變項根本不同」這個事實，混在一起講就會出現「年輕體能好所以打強化療、順便早點評估移植」這種聽起來合理但其實錯誤的答案（favorable risk 反而不該在 CR1 移植）。**因為**考官要看的是你知不知道現代 AML 的決策已經不是「年齡決定強度、風險決定移植」這麼粗，而是 fitness 與生物學各管一段。
  - **第一個問題：誘導治療給多強？——判準是 fitness，不是年齡**
    - 標準 7+3（cytarabine + anthracycline）不建議用於 **>75 歲**（相對禁忌），或符合 **Ferrara criteria** 的 unfit 病人：ECOG PS ≥3、EF ≤50%、DLCO 或 FEV1 ≤65%（或需氧氣）、需腎替代治療、Child-Pugh B/C 肝硬化、難治性感染、需住院的精神疾病等。
    - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 現代的問法已經從「**誰撐得住**強化療」變成「**誰真的能從中獲益**」：即使 fitness 過關，若屬不良風險生物學（**TP53 突變、複雜核型**），誘導緩解率或許還可以，但長期預後仍差，趨勢是改採 **venetoclax + HMA** 或標靶治療取代 7+3。能講出這個轉變，等於告訴考官你讀的是近幾年的東西。
  - **第二個問題：緩解後要不要移植？——ELN 2022 風險分類 × MRD × 移植相關死亡率**
    - 整體門檻：預估**不移植的復發風險 >35%** 時才考慮 allo-HCT，也就是要拿復發風險去對沖移植本身的 TRM。
    - **Favorable risk**（CBF、NPM1 突變／FLT3-ITD 野生型、CEBPA bZIP）：**不建議 CR1 移植**，首選 3–4 療程高劑量 cytarabine 鞏固或 auto-HCT；**但 MRD 持續陽性者仍要轉 allo-HCT**。
    - **Intermediate risk**：沒有共識，要個別化。**MRD 陰性**可留在化療／auto-HCT；**MRD 陽性建議 allo-HCT**。
    - **Adverse risk**：多數建議 **CR1 就移植，不論 MRD**，除非 TRM 風險過高。
    - 支持數據：一項 769 人的研究顯示，依此策略接受移植者三年整體存活明顯較佳（favorable HR 0.38、intermediate HR 0.53、adverse HR 0.51）。
    - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 反過來也要記得：**MRD 陰性的病人不一定該移植**——非復發死亡率（NRM）的增加可能把移植的效益抵消掉甚至變成負的。這是「移植不是越早越好」的具體證據，被追問時講得出來很加分。
    - 其他要一併考慮的：年齡、共病（用 **HCT-CI** 量化）、donor 可及性與配對程度、中心經驗、病人意願。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「這題要拆成兩個問題：誘導強度看 fitness（Ferrara criteria），移植與否看生物學加 MRD——判準不同，不能混在一起講。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「Favorable risk 的病人也要在 CR1 移植嗎？」→ 不用，首選高劑量 cytarabine 鞏固或 auto-HCT；除非 MRD 持續陽性（例如 CBF 融合基因未達 3-log 下降、NPM1 MRD 陽性）才轉 allo-HCT。
- 「一個年輕、體能很好，但帶 TP53 突變的病人，你會直接打 7+3 嗎？」→ 這正是「fit 不等於會獲益」的情境，現代趨勢會考慮 venetoclax + HMA 或標靶治療，而不是硬上 7+3。
- 「什麼時候該轉去評估 allogeneic transplant？」→ 以「不移植的復發風險 >35%」為門檻，整合 ELN 2022 分層與 MRD；可對照 [myeloma 篇](/hema-board-interview-guide/topics/myeloma-and-transplant/) 移植適應症的判斷邏輯（該篇重點是自體、這裡是異體）。

</div>

- **常見追問：「t(9;22) transform 成 AML 常不常見」——容易答反的陷阱題**
  - **最佳答法**：先講「Philadelphia chromosome 最典型對應的疾病是 CML 慢性期」這個定錨點，再回答 transform 成 AML 的相對機率，順序不能顛倒。**依照**「先確認診斷、再談後續」的推理順序，把 t(9;22) 的原始定位講清楚，才有立足點去比較 BCR-ABL1 陽性急性白血病中 ALL 遠比 AML 常見這件事。**因為**這題就是考官刻意設計來測「直覺跟事實是否一致」的陷阱——直覺容易把 Ph 染色體跟 AML 連在一起，但正確答案是 ALL 遠比 AML 常見，能先講對應關係再答機率，才展現出你不是靠直覺答題，而是真的釐清了疾病分類的邏輯。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 直覺容易覺得 t(9;22)／BCR-ABL1 陽性應該常見於 AML，但事實剛好相反：**BCR-ABL1 陽性的急性白血病中，ALL 遠比 AML 常見**。
  - 正確結論：Philadelphia chromosome（t(9;22)／BCR-ABL1）本身最典型對應的疾病其實是 **CML 慢性期**，不是 AML；被問到這題時，要先把這個對應關係講清楚，再回答 transform 成 AML 的相對機率，順序不能顛倒。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「t(9;22) 這題的陷阱是直覺聯想到 AML，但事實是 BCR-ABL1 陽性急性白血病裡 ALL 遠比 AML 常見。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「Ph 陽性 ALL 的治療跟一般 ALL 有什麼不同？」→ 要加上 TKI（如 imatinib／dasatinib）合併化療，可連到 [ALL 篇](/hema-board-interview-guide/topics/all-leukemia/)。
- 「Philadelphia chromosome 最典型對應的 CML 慢性期，跟本篇 CML 段落的 TKI 治療邏輯是同一套嗎？」→ 是，可對照本篇 CML 一線用藥的討論。

</div>

- **急性白血病型態不確定是 AML 還是 ALL 時的基本處理**
  - **最佳答法**：不要在型態學卡住不敢下結論，要主動提出下一步的檢驗行動。**依照**「型態學本身有時無法可靠區分 myeloid 與 lymphoid lineage」這個事實，講出遇到看起來介於兩者之間的抹片時，正確反應是問問病理能不能先幫忙加染 **MPO**，或是口頭直接聯絡 **flow cytometry**，**因為**考官要看的是你在不確定的時候有沒有「知道下一步該做什麼」的臨床反應，而不是要你當場憑肉眼武斷分類——講得出下一步動作，比硬猜一個答案更能拿分。
  - MPO（myeloperoxidase）染色陽性支持 myeloid lineage（傾向 AML）；但型態學跟細胞化學染色都只能做初步判斷。
  - 最終確診 lineage 一定要靠 **flow cytometry** 做 immunophenotyping，不能只靠骨髓抹片型態或單一染色就下結論——這也是跟 [ALL 篇](/hema-board-interview-guide/topics/all-leukemia/) 共通的免疫分型邏輯，AML 跟 ALL 的最終區分本來就不是靠肉眼。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 常見陷阱是覺得答不出來就是知識不足而慌張，其實臨床上遇到不確定的型態，主動聯絡病理或檢驗單位加做染色、加驗 flow，才是正確且專業的處理方式，不是知識不足的表現。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「型態學看不出來 myeloid 還是 lymphoid 時，正確反應不是硬猜，而是主動問病理能不能加染 MPO、口頭聯絡 flow cytometry。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「MPO 染色陰性就能排除 AML 嗎？」→ 不行，MPO 陰性只代表不支持 myeloid lineage，不是排除，最終診斷仍要靠 flow cytometry。
- 「AML 跟 ALL 最終的 lineage 區分邏輯有什麼不同？」→ 兩者最終都是靠 flow immunophenotyping 而非肉眼型態，可對照 [ALL 篇](/hema-board-interview-guide/topics/all-leukemia/) 的免疫分型討論。

</div>

## MDS

- **典型案例呈現方式：兩次骨髓報告的「疾病演進」設計**
  - **最佳答法**：一看到題目給了兩次骨髓報告，就要主動把兩者放在一起比較 blast 比例的變化趨勢，而不是針對第一次報告的靜態數字就下結論結案。**依照**推理架構裡「確認診斷」這一步其實隱含疾病是動態的這個前提，MDS 的判讀不能只看單一時間點的快照，而要看演進趨勢。**因為**考官刻意設計兩次報告就是要測你會不會捕捉到「疾病演進」這個關鍵訊息——只看第一次報告作答的人會漏掉 blast 比例上升代表的疾病惡化，答對這題展現的是你有能力做縱向而非橫斷的臨床判讀。
  - 口試官通常會先給一次貧血合併輕微 dysplasia、blast 比例不高的骨髓報告。
  - 過一段時間，再給第二次追蹤報告，顯示 blast 比例明顯上升。
  - 這個設計的目的是考你會不會注意到**疾病演進**，而不是只看單一時間點的靜態分層；回答時要主動指出「這兩次報告要放在一起看、比較 blast 比例的變化趨勢」，而不是只針對第一次報告的靜態數字就下結論結案。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「看到題目給兩次骨髓報告，這本身就是在暗示我要比較 blast 比例的變化趨勢，不是只評第一次報告。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「如果第二次報告 blast 比例已經超過 20%，代表什麼？」→ 代表疾病演進為 AML，治療邏輯要切換到本篇 AML 段落的分層決策。
- 「兩次報告之間的追蹤間隔要怎麼抓？」→ 依風險分層跟症狀變化調整，本質上仍是「持續評估、依結果調整」的同一套邏輯，跟 CML milestone 監測的精神一致。

</div>

- **要能講出 IPSS risk score 怎麼估、對應的處置方向**
  - **最佳答法**：把分層結果跟處置方向兩件事綁在一起講，不要只背 IPSS 公式的組成分數。**依照**推理架構裡「風險分層決定治療強度」的核心邏輯，回答時要明確講出「低風險對應 best supportive care／clinical trial，高風險對應 hypomethylating agent 等積極治療」這個配對關係。**因為**考官要驗證的是你知不知道分層的目的是什麼，而不是你會不會背評分表——只列出分數計算方式而講不出後續處置，等於只做了一半的答案。
  - 依 IPSS risk score 估出來的風險分層，會對應到不同的處置強度：分層低的傾向 best supportive care 或考慮 clinical trial；分層較高、需要積極介入的則會用到 hypomethylating agent 等治療。
  - 講的時候要把「分層」跟「處置方向」明確配對講出來，不能只背分層公式而講不出後續要怎麼處理。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「IPSS 分數本身不是重點，重點是分數要能對應到具體的處置方向：低風險支持性照顧、高風險積極治療。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「低風險病人什麼情況下會考慮升級成積極治療？」→ 當出現疾病演進（如 blast 比例上升）等惡化徵象時，呼應本篇「兩次骨髓報告」論點裡的動態判讀邏輯。
- 「高風險 MDS 除了 hypomethylating agent，還有什麼選項？」→ 可能考慮 allogeneic transplant，可對照 [myeloma 篇](/hema-board-interview-guide/topics/myeloma-and-transplant/) 的移植決策邏輯。

</div>

- **常見延伸提問：hypomethylating agent（如 azacitidine）為什麼對 MDS 有效**
  - **最佳答法**：先講機轉（DNA methyltransferase 抑制劑→抑制異常甲基化→腫瘤抑制基因重新表現），再連結到臨床證據（三期試驗的 OS 獲益），兩層分開講清楚。**依照**「機轉先於臨床證據」的邏輯順序回答，才能讓口試官看到你理解的是「為什麼有效」，而不是只背「證實有效」的結論。**因為**這類延伸提問是在測基礎藥理機轉的深度——能講出 azacitidine 是讓異常前驅細胞恢復分化、而非單純殺死腫瘤細胞這個細節，才顯示你真的懂機轉，而不是只記得藥名跟適應症。
  - 機轉：azacitidine 是 DNA methyltransferase 抑制劑，會抑制異常的 DNA 甲基化。
  - MDS 的病生理裡，腫瘤抑制基因常因為異常甲基化被沉默（silencing），azacitidine 讓這些基因重新表現、促使異常的骨髓前驅細胞恢復分化，而不是單純殺死腫瘤細胞。
  - 臨床證據：關鍵的三期試驗顯示，azacitidine 在高風險 MDS 病人身上比傳統的 conventional care（含低劑量化療、支持性療法）能延長整體存活期（OS），這是它成為高風險 MDS 標準治療的依據。
  - 也可能被問到特定染色體異常（例如 del(5q)）在本地病人中常不常見，要有心理準備回答盛行率相關的問題。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「azacitidine 有效不是因為殺死腫瘤細胞，而是讓被異常甲基化沉默的腫瘤抑制基因重新表現、促使前驅細胞恢復分化。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「azacitidine 跟傳統化療的作用機轉本質差異在哪？」→ 傳統化療是細胞毒殺，azacitidine 是表觀遺傳調控（抑制 DNA methyltransferase），讓細胞恢復正常分化。
- 「臨床證據上 azacitidine 的 OS 獲益是跟誰比較出來的？」→ 是跟傳統 conventional care（含低劑量化療、支持性療法）比較，這也是它成為高風險 MDS 標準治療的依據。

</div>

## CML

- **TKI 治療策略：一線藥物與副作用比較**
  - **最佳答法**：先講選藥的整體邏輯（第二代 TKI 反應更快更深，但副作用型態不同，臨床上依共病選藥），再逐一講每個藥物的招牌副作用，不要只列藥名清單。**依照**「依病人共病選藥」這個臨床邏輯，把每個藥物的副作用跟對應的禁忌族群（如 dasatinib 對肺病史病人的顧慮、nilotinib 對心血管病史病人的顧慮）連起來講，才是完整的答案。**因為**考官設下的陷阱就是看你答不答得出每個藥物「各自」的副作用——只背得出藥名清單卻講不出 dasatinib 的肋膜積水、nilotinib 的心血管風險，會被認為只是背誦藥名清單，沒有臨床選藥的概念。
  - 一線可選第一代 **imatinib**，或第二代 TKI（**dasatinib**、**nilotinib**、**bosutinib**）——第二代 TKI 通常能更快達到更深的分子學反應，但副作用型態不同，臨床上會依病人共病選藥，不是隨便選一個。
  - **Imatinib**：長期使用資料最多，耐受性整體不錯，常見副作用是腸胃道不適、水腫（periorbital/下肢）、肌肉痠痛。
  - **Dasatinib**：要特別注意**肋膜積水（pleural effusion）**風險，長期使用也有肺動脈高壓的顧慮，有肺部/心臟病史的病人要謹慎選用。
  - **Nilotinib**：要注意 **QT 波間期延長**，以及心血管/動脈阻塞性事件（如周邊動脈疾病、心肌梗塞）風險上升，用藥前後需監測心電圖、血糖、血脂；另外要注意可能誘發高血糖與胰臟炎，服藥時間需避開空腹以外進食（會影響藥物吸收與 QT 交互作用），這也是常被忽略的細節。
  - **Bosutinib**：常見副作用是腹瀉，也需留意肝毒性。
  - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 常見陷阱：只答得出藥名，講不出每個藥物各自要特別留意的副作用（dasatinib 的肋膜積水、nilotinib 的心血管風險），會被認為只是背藥名清單、沒有臨床選藥的概念。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「選 TKI 不是背藥名清單，而是依病人共病選藥：肺病史避開 dasatinib，心血管病史避開 nilotinib。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「病人有肺部病史，選哪個 TKI 比較適合？」→ 避開 dasatinib（肋膜積水／肺動脈高壓風險），可考慮 imatinib，但若有心血管病史則要避開 nilotinib。
- 「二代 TKI 反應更快更深，是不是就該一律優先選二代？」→ 不是，要權衡副作用與共病，這正是「依共病選藥」而非單看反應深度的核心邏輯。

</div>

- **停藥策略：treatment-free remission（TFR）**
  - **最佳答法**：不要只講「深度分子反應維持夠久就能停藥」這一句話，TFR 其實是一整組條件（病程階段、治療反應史、治療時間長度、監測能力）加上停藥後的追蹤計畫，缺一不可。**依照**推理架構裡「持續評估、依結果調整」的邏輯，TFR 不是一次性決定，而是停藥前要通過完整資格檢核、停藥後仍要監測的動態過程。**因為**考官要看的是你知不知道 TFR 是有多重條件、有風險的決策，而不是把停藥講成「反應夠深就停」這麼單一的判斷——只講 MR4.5 跟時間長度，漏掉病程階段跟治療反應史這幾個條件，會顯得對這個決策的完整度理解不足。
  - 條件不是只有「深度分子反應維持夠久」一項，而是要同時滿足：病人處於**第一次慢性期**（沒有加速期或芽細胞期病史）、**先前治療沒有失敗過**、TKI 治療總時間通常需**滿 5 年以上**（若中間有用第二代 TKI，門檻可以縮短到滿 4 年）、並且要有能力做到**高品質、快速、標準化的 qPCR 監測**；在滿足這些前提下，再看分子反應是否達到**深度且持續**（通常是 MR4.5 這個深度）並維持**至少 2 年以上**，才會考慮嘗試停藥。
  - 停藥後的監測要密集：**前 6 個月每月監測一次**，**第 6 到 12 個月每 2 個月監測一次**，之後可以拉長到**每 3 個月一次**，一旦復發要能及時重新啟動 TKI。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「TFR 不是『反應夠深就停藥』這麼簡單，而是病程階段、治療反應史、治療時間長度、監測能力四個條件都要滿足的動態決策。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「停藥後如果分子反應復發，下一步怎麼辦？」→ 要及時重新啟動 TKI，這也是為什麼停藥後前 6 個月要每月監測。
- 「為什麼治療總時間門檻是滿 5 年，用過二代 TKI 可以縮短到滿 4 年？」→ 因為二代 TKI 能更快達到更深的分子學反應，呼應本篇「一線藥物比較」論點裡二代 TKI 反應更快更深的邏輯。

</div>

- **CML 的 milestone 監測時程，用具體切點記，比模糊講「要監測」更有說服力**
  - **最佳答法**：直接講出 3 個月、6 個月、12 個月各自對應的具體切點數字，再補上沒達標時要往回查服藥順從性、藥物交互作用，或考慮換藥／加驗 kinase domain mutation 的處置邏輯，不要只模糊地說「要定期監測分子反應」。**依照**推理架構裡「CML 用監測 milestone 取代風險分層」的邏輯，這一步本質上仍是「持續評估、依結果調整」的同一套骨架，只是評估對象換成分子反應而非細胞遺傳學分層。**因為**具體切點比模糊描述更有說服力，也才能展現你真的知道 failure／warning 的判斷標準是什麼，而不是只知道「有在監測」這個空泛概念。
  - 常見的分子學反應監測時間點與目標（ELN 建議的大致架構）：**3 個月** BCR-ABL1 IS ≤ 10%；**6 個月** ≤ 1%；**12 個月** 達到 major molecular response（MMR，即 ≤ 0.1%）。
  - 沒有在這些時間點達標，稱為治療反應不佳（failure/warning），要考慮是否有服藥順從性問題、藥物交互作用，或需要換藥、加驗 BCR-ABL1 kinase domain mutation。
  - 這一步是 CML 取代「風險分層決定治療強度」的那個位置——CML 幾乎所有病人一律先用 TKI，不靠分層決定要不要治療；本質上仍是框架裡「持續評估、依結果調整」的同一種邏輯，只是評估的對象換成監測分子反應，而不是骨髓型態或細胞遺傳學分層。

<div class="callout callout-keywords">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

「講監測不能只說『要定期追蹤分子反應』，要直接講出 3 個月 ≤10%、6 個月 ≤1%、12 個月達 MMR 這三個切點。」

</div>

<div class="callout callout-followup">
<div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

- 「12 個月沒有達到 MMR，下一步該做什麼？」→ 先查服藥順從性、藥物交互作用，再考慮換藥或加驗 BCR-ABL1 kinase domain mutation。
- 「這套 milestone 監測邏輯跟 AML／MDS 的風險分層在本質上有什麼共通點？」→ 都是本篇推理架構裡「持續評估、依結果調整」的同一套骨架，只是評估對象從骨髓型態／細胞遺傳學換成分子反應。

</div>

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9.003a1 1 0 0 1 1.517-.859l4.997 2.997a1 1 0 0 1 0 1.718l-4.997 2.997A1 1 0 0 1 9 14.996z"/><circle cx="12" cy="12" r="10"/></svg> 相關 YouTube 影片

- **[Acute Myeloid Leukemia (AML) – Auer Rods, Myeloperoxidase Positive](https://www.youtube.com/watch?v=bNlnYvjhxAU)** — Medicosis Perfectionalis · 12:08
  - **對應 AML 段落與 MPO 那一題**：為什麼 MPO 陽性支持 myeloid lineage，看過型態圖之後，「型態不確定就加染 MPO、聯絡 flow」這個處置就變得直覺。
- **[Chronic Myeloid Leukemia (CML) – Pathogenesis, Symptoms and Treatment](https://www.youtube.com/watch?v=RTdHf_V2EGw)** — JJ Medicine · 10:22
  - **對應 CML 段落**：BCR-ABL1 融合基因怎麼形成、TKI 怎麼阻斷它，理解機轉之後 milestone 監測為什麼盯分子反應就講得出理由。
- **[Myelodysplastic Syndrome (MDS) | Clinical Medicine](https://www.youtube.com/watch?v=HjyAGaUN_TY)** — Ninja Nerd · 23:44
  - **對應 MDS 段落**：無效造血、blast 比例、風險分層到 hypomethylating agent 一路講完，補足本頁只點到的 IPSS 與 azacitidine 機轉。
- **[Chronic Myeloid Leukemia (CML) – Philadelphia Chromosome](https://www.youtube.com/watch?v=aZz5idSKuEE)** — Medicosis Perfectionalis · 17:59
  - **對應 CML 段落**：Philadelphia chromosome 怎麼形成 BCR-ABL1、為什麼 TKI 能精準阻斷它，是理解 milestone 監測為什麼盯分子反應的前提。
- **[Blast Crisis in Chronic Myeloid Leukemia (CML)](https://www.youtube.com/watch?v=bo9qRqqSR3c)** — Medicosis Perfectionalis · 5:14
  - **對應「疾病演進」這個共通考點**：CML 慢性期怎麼進展到 blast crisis，跟 MDS 那題「兩次骨髓報告要一起看」是同一種縱向判讀的思路。
- **[Hematological Malignancies – Part 1a: Hematopoiesis, Acute Leukemias](https://www.youtube.com/watch?v=5IIsrHQtesY)** — AMBOSS · 11:48
  - **對應本頁推理架構的第一步（確認診斷）**：從造血分化樹講起，說明急性白血病是卡在哪一階段的分化障礙——理解這點，flow cytometry 為什麼是確診 lineage 的關鍵就不用背。
- **[Acute Promyelocytic Leukemia (APL) Illness Script](https://www.youtube.com/watch?v=VlPH4sLyVIQ)** — The Clinical Problem Solvers · 4:32
  - **illness script 是什麼長相，看這支最快**：CPSolvers 把一個疾病壓縮成「哪種人、怎麼發病、有什麼特徵、怎麼確認」四格。APL 本身也是 AML 裡唯一需要當急症處理的亞型（DIC 風險），值得單獨記住。

## 容易被電的點

- MDS 案例題容易忽略「兩次骨髓報告要一起看」的設計，只看第一次報告就下結論，漏掉疾病演進（blast 比例上升）這個關鍵訊息。
- BCR-ABL1 陽性的急性白血病答成 AML 比 ALL 常見——順序答反了。
- CML／AML 的分子生物學細節被追問到很深時（例如某個基因突變的下游機轉），答不出來很正常，講到自己有把握的深度就好，不用硬掰。
