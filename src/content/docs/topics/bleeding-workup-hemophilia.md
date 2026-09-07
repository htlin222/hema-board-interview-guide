---
title: 出血檢查與 Hemophilia
sidebar:
  order: 12
---

跟 IDA 並列最高頻的門診/benign 主題，常出到「一路問到底」的完整題組。這裡有三層框架，疊起來用就能推導出幾乎所有出血案例的答題順序。

## 🧭 框架一：先分「哪一層 hemostasis 出問題」——比抽血更早的第一步

**這是考官最想聽到的起手式，很多人直接跳去背 PT/aPTT 鑑別清單反而漏了這一步**。看到出血案例，第一個問題永遠是問病史裡的出血型態，而不是先看檢驗報告：

- **黏膜/皮膚出血、發生得快、傷口表淺就流不停**（瘀點、鼻血、牙齦出血、月經過多）→ 提示 **primary hemostasis** 問題（platelet 數量/功能、vWD）。
- **深層組織/關節出血、延遲發生**（受傷後幾小時才腫起來、hemarthrosis）→ 提示 **secondary hemostasis** 問題（凝血因子缺乏）。

這個分流決定你接下來要往 platelet/vWF 方向查，還是往 PT/aPTT/factor 方向查——**先講出這一句分流邏輯，再進入檢驗數字**，是這題的答題骨架。

## 🧭 框架二：PT/aPTT 異常不用背鑑別清單，用 pathway 圖推

PT 和 aPTT 各自測的是哪些因子，其實是可以現場畫出來推的，不用死記鑑別診斷清單：

- **PT** 測 extrinsic pathway（factor VII）+ common pathway（X、V、II、fibrinogen）。
- **aPTT** 測 intrinsic pathway（XII、XI、IX、VIII）+ common pathway（X、V、II、fibrinogen）。

於是：

- **只有 aPTT 延長** → 問題只在 intrinsic pathway 獨有的因子（VIII、IX、XI、XII）或 lupus anticoagulant，common pathway 沒事所以 PT 正常。
- **只有 PT 延長** → 問題在 extrinsic pathway 獨有的 factor VII（半衰期最短，早期肝病/vit K 缺乏最早反映在這裡）。
- **PT/aPTT 都延長** → 問題落在兩條路徑共用的 common pathway（II、V、X、fibrinogen），或是多重因子同時缺乏（DIC、嚴重肝病、warfarin/vit K 缺乏、大量輸液稀釋）。

**這張圖背後最重要的例外**：isolated aPTT prolongation 的鑑別診斷裡包含 lupus anticoagulant／APS，但 **APS 臨床上最常見的表現是血栓，不是出血**——考官很愛在這裡反問，答的時候要主動點出這個矛盾。

## 🧭 框架三：mixing study 的判讀邏輯——「量不夠」還是「有東西在擋」

Mixing study 在問一件事：把病人血漿跟正常血漿 1:1 混合，異常會不會被「稀釋掉」。

- **會恢復正常（correctable）** → 代表病人只是**缺量**，混進去的正常血漿把缺的因子補足了 → 指向 quantitative 因子缺乏。
- **不會恢復（not correctable）** → 代表有東西在**主動抑制**，正常血漿混進去也一樣被抑制掉 → 指向 inhibitor。

判讀時要注意兩個技術細節：

1. **要同時測 0 小時（立即）和 2 小時（培養後）**，因為有些 inhibitor 是 **time/temperature-dependent**（如 acquired hemophilia 的 anti-FVIII 抗體），立即測可能看起來是 correctable，培養 2 小時後才會現形變成 not correctable；lupus anticoagulant 通常是立即作用型，0 小時就看得出來。
2. **要跑一組正常血漿的 control** 一起培養對照——如果 control 組自己也 prolong，代表是檢體處理不當或 factor degradation 造成的技術性問題，不是真的有 inhibitor，不能誤判。

## 套用到實際問法

1. **Isolated aPTT prolongation 的鑑別診斷？**
   - 套框架二：intrinsic pathway 因子缺乏（VIII/hemophilia A、IX/hemophilia B、XI、XII）、acquired inhibitor（acquired hemophilia，多為 anti-FVIII）、lupus anticoagulant/APS（**但臨床主要表現是血栓不是出血**）、vWD（因 vWF 攜帶保護 FVIII，可間接使 aPTT 延長）。

2. **Combined PT/aPTT prolongation 的鑑別診斷？**
   - 套框架二：common pathway 因子缺乏（II、V、X）、多重因子缺乏（DIC、嚴重肝病合成不足、vit K 缺乏/warfarin）、大量輸液稀釋性凝血病變。

3. **異常延長，下一步要做什麼？**
   - **Mixing study**（框架三）。

4. **Mixing study 怎麼做、怎麼判讀？**
   - 套框架三：0 小時 + 2 小時培養都要測，同時跑 control；correctable=量的問題（因子缺乏），not correctable=有 inhibitor；先確認 control 沒有一起 prolong 才能排除技術性問題；有 inhibitor pattern 時再鑑別 lupus anticoagulant（不影響特定因子活性）vs. specific factor inhibitor（acquired hemophilia）。

5. **確診因子缺乏後，還要驗哪些？**
   - Factor VIII、IX、XI 活性為主；**factor XII 缺乏臨床上通常不會出血**，一般不急著驗。
   - 疑似 vWD 者加驗 vWF antigen、activity（ristocetin cofactor）。

6. **Hemophilia 的嚴重度分級與對應 factor level？**
   - Severe：factor level <1%（<0.01 IU/mL），易自發性出血（關節、肌肉）。
   - Moderate：1–5%，中度創傷後出血。
   - Mild：5–40%，通常需較大創傷或手術才出血，可能成年才被診斷。

7. **Hemophilia 最常見的臨床表現？**
   - Hemarthrosis（關節內出血，尤其膝、肘、踝）最典型——回扣框架一：這是「深層、延遲」型出血，本來就該從 secondary hemostasis 方向去想，這裡是驗證。反覆發作會導致 hemophilic arthropathy。

8. **何時要開始 prophylaxis？目標 factor level？**
   - 建議在**第一次關節出血後、或幼年期**即開始 primary prophylaxis，預防反覆關節出血導致慢性關節病變。
   - 目標 trough level 通常維持在 **>1%**（依現行國際指引可能更高，如 >3–5%，需視最新建議與藥物半衰期/劑型調整）。

9. **有 inhibitor 的病人出血時怎麼處理（bypassing agent）？何時考慮？**
   - 當病人產生 anti-FVIII/FIX 抗體，一般因子補充無效，改用 bypassing agent：**FEIBA**（activated prothrombin complex concentrate）或 **recombinant activated factor VII（rFVIIa, NovoSeven）**。
   - 長期可考慮 immune tolerance induction（ITI）或新型非因子藥物（如 emicizumab）。

10. **Acquired hemophilia 怎麼跟 lupus coagulopathy 鑑別？需要哪些檢查？怎麼治療？**
    - 鑑別：套框架三——acquired hemophilia 是 specific factor inhibitor（通常 anti-FVIII），mixing study 呈 time-dependent inhibitor pattern 且**特定因子活性明顯下降**；lupus anticoagulant 通常不會顯著降低單一因子活性、且臨床上較少真的出血（甚至偏向血栓風險，呼應框架二的例外提醒）。
    - 確診：Bethesda assay 測 inhibitor titer。
    - 治療：出血急性期用 bypassing agent；根除 inhibitor 用 **steroid**（單獨或合併）、**cyclophosphamide**、或 rituximab；文獻上合併治療（steroid + cyclophosphamide）緩解率可能較單用 steroid 高，但需權衡感染等副作用風險。

## 容易被電的點

- 沒有先講出血型態分流（框架一）就直接跳進 PT/aPTT 數字，考官會覺得你只是背檢驗流程而不理解邏輯。
- Mixing study 只看單一時間點、忘記對照 control 組。
- 把 combined 與 isolated PT/aPTT prolongation 的鑑別診斷清單搞混——用框架二的 pathway 圖現場推，比背清單穩。
- 只回答「因子缺乏」就停住，沒有主動往下講治療與監測。
