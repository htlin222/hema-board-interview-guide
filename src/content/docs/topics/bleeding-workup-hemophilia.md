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

   擬答：
   - **套框架二：PT 正常代表 common pathway 沒事，問題鎖定在 intrinsic pathway 獨有的因子。**
     - 先想因子缺乏：Factor VIII 缺乏（hemophilia A）、factor IX 缺乏（hemophilia B）、factor XI 缺乏、factor XII 缺乏。
   - **再想 acquired inhibitor：acquired hemophilia，通常是 anti-FVIII 抗體造成的後天抑制物。**
   - **接著一定要提 lupus anticoagulant/APS，這是這題最常被追問的陷阱。**
     - ⚠️ Lupus anticoagulant 在檢驗上會讓 aPTT 延長，但臨床上 APS 最主要的表現是血栓，不是出血，答的時候要主動點出這個矛盾，不要讓考官覺得你以為 lupus anticoagulant 等於出血傾向。
   - **最後別漏掉 vWD：因為 vWF 在血中會攜帶並保護 factor VIII，vWF 缺乏或功能異常時 FVIII 半衰期縮短、活性下降，也可能間接使 aPTT 延長。**

2. **Combined PT/aPTT prolongation 的鑑別診斷？**

   擬答：
   - **套框架二：PT、aPTT 都延長，代表問題落在兩條路徑共用的 common pathway，或是同時有多重因子缺乏。**
     - Common pathway 因子單一缺乏：factor II、factor V、factor X 缺乏。
   - **多重因子同時缺乏的情境要一併列出。**
     - DIC（消耗性凝血病變，同時消耗多種因子與 fibrinogen）。
     - 嚴重肝病，因肝臟合成凝血因子能力下降（factor VII 因半衰期最短通常最早受影響，但嚴重時 common pathway 因子也一起下降）。
     - Vitamin K 缺乏或使用 warfarin，影響 vitamin K 依賴性因子（II、VII、IX、X）的合成。
   - **也要提到大量輸液或大量輸血造成的稀釋性凝血病變**，因為快速大量補液會把體內原有的凝血因子稀釋掉，同樣會表現成 PT、aPTT 都延長。

3. **異常延長，下一步要做什麼？**

   擬答：
   - **PT 或 aPTT 異常延長後，下一步是做 mixing study（對應框架三）**，目的是分辨病人是「因子量不夠」還是「有東西在主動抑制凝血」，這一步決定後續要往因子補充還是往找 inhibitor 的方向走。

4. **Mixing study 怎麼做、怎麼判讀？**

   擬答：
   - **做法：把病人血漿和正常血漿以 1:1 混合，同時測 0 小時（立即）和 2 小時（37°C 培養後）兩個時間點，並且要跑一組正常血漿的 control 一起培養對照。**
     - ⚠️ 一定要同時測 0 小時和 2 小時，因為有些 inhibitor 是 time/temperature-dependent，像 acquired hemophilia 的 anti-FVIII 抗體，立即測可能看起來 correctable，培養 2 小時後才會現形變成 not correctable；lupus anticoagulant 通常是立即作用型，0 小時就看得出來。
     - ⚠️ 一定要跑 control 組：如果 control 組自己也 prolong，代表是檢體處理不當或 factor degradation 造成的技術性問題，不是真的有 inhibitor，不能誤判成陽性。
   - **判讀第一層：correctable 還是 not correctable。**
     - Correctable（混合後恢復正常）代表病人只是缺量，混進去的正常血漿把缺的因子補足了，指向 quantitative 因子缺乏。
     - Not correctable（混合後仍然延長）代表有東西在主動抑制，正常血漿混進去也一樣被抑制掉，指向 inhibitor 存在。
   - **判讀第二層：確認是 inhibitor pattern 之後，再進一步鑑別是哪一種 inhibitor。**
     - Lupus anticoagulant：通常不會顯著降低單一特定因子的活性。
     - Specific factor inhibitor（如 acquired hemophilia 的 anti-FVIII）：會讓對應的特定因子活性明顯下降。

5. **確診因子缺乏後，還要驗哪些？**

   擬答：
   - **針對 hemophilia 相關因子，主要驗 factor VIII、factor IX、factor XI 活性，用來確診並分型。**
     - ⚠️ Factor XII 缺乏雖然會讓 aPTT 延長，但臨床上通常不會造成出血，所以一般不急著驗。
   - **如果臨床上懷疑 vWD，要加驗 vWF antigen 和 vWF activity（ristocetin cofactor assay）**，因為 vWD 的診斷需要同時看 vWF 的量和功能，不能只靠 factor VIII 活性。

6. **Hemophilia 的嚴重度分級與對應 factor level？**

   擬答：
   - **Severe：factor level 小於 1%（小於 0.01 IU/mL）**，容易出現自發性出血，好發於關節與肌肉，不需要明顯外傷就會出血。
   - **Moderate：factor level 介於 1% 到 5%**，通常在中度創傷後才會出血，自發性出血相對少見。
   - **Mild：factor level 介於 5% 到 40%**，通常需要較大創傷或接受手術時才會出血，很多病人甚至到成年後才因為手術或拔牙出血被診斷出來。

7. **Hemophilia 最常見的臨床表現？**

   擬答：
   - **最典型的表現是 hemarthrosis，也就是關節內出血，好發在膝關節、肘關節、踝關節。**
     - 回扣框架一：hemarthrosis 屬於「深層組織、延遲發生」型的出血，本來就該從 secondary hemostasis（凝血因子）的方向去想，這裡剛好是驗證框架一分流邏輯的具體例子。
   - **反覆的關節出血如果沒有妥善控制，會逐漸導致 hemophilic arthropathy**，也就是慢性關節病變、關節破壞與功能喪失，所以早期預防出血非常重要。

8. **何時要開始 prophylaxis？目標 factor level？**

   擬答：
   - **建議在病人第一次關節出血後、或幼年期，就開始 primary prophylaxis**，目的是預防反覆關節出血累積造成的慢性關節病變，而不是等到已經出現關節破壞才開始治療。
   - **目標 trough level 通常維持在大於 1%**，把病人從 severe 的表現型拉到接近 moderate 的出血頻率。
     - 依現行國際指引，實際目標可能設定更高（如大於 3% 到 5%），需要依照最新治療建議、所使用藥物的半衰期與劑型來調整,不是一個固定不變的數字。

9. **有 inhibitor 的病人出血時怎麼處理（bypassing agent）？何時考慮？**

   擬答：
   - **當病人產生 anti-FVIII 或 anti-FIX 抗體時，一般的因子補充治療會失效，因為補進去的因子會被抗體中和掉，這時要改用 bypassing agent 來繞過被抑制的那個因子。**
     - 第一線選擇之一是 **FEIBA**（activated prothrombin complex concentrate）。
     - 另一個選擇是 **recombinant activated factor VII（rFVIIa, NovoSeven）**。
   - **長期治療方面，可以考慮 immune tolerance induction（ITI）來嘗試根除抗體，或使用新型非因子藥物（如 emicizumab）作為長期出血預防的替代方案。**

10. **Acquired hemophilia 怎麼跟 lupus coagulopathy 鑑別？需要哪些檢查？怎麼治療？**

    擬答：
    - **鑑別要套框架三的 mixing study 判讀邏輯。**
      - Acquired hemophilia 是 specific factor inhibitor，通常是 anti-FVIII 抗體，mixing study 會呈現 time-dependent inhibitor pattern（0 小時可能 correctable、2 小時培養後變成 not correctable），而且對應的特定因子活性會明顯下降。
      - Lupus anticoagulant 通常不會顯著降低單一因子的活性，而且臨床上較少真的表現出血，甚至偏向血栓風險，這點呼應框架二提到的例外——考官很愛在這裡反問兩者的差異。
    - **確診要做 Bethesda assay，測出 inhibitor titer 來定量抗體的抑制強度。**
    - **治療分兩個層次。**
      - 出血急性期先用 bypassing agent（FEIBA 或 rFVIIa）控制出血。
      - 根除 inhibitor 則使用 **steroid**（可單獨使用或合併其他藥物）、**cyclophosphamide**、或 **rituximab**。
      - 文獻上合併治療（steroid 加 cyclophosphamide）的緩解率可能比單用 steroid 高，但需要權衡感染等副作用風險，不是一律都要合併使用。

## 容易被電的點

- 沒有先講出血型態分流（框架一）就直接跳進 PT/aPTT 數字，考官會覺得你只是背檢驗流程而不理解邏輯。
- Mixing study 只看單一時間點、忘記對照 control 組。
- 把 combined 與 isolated PT/aPTT prolongation 的鑑別診斷清單搞混——用框架二的 pathway 圖現場推，比背清單穩。
- 只回答「因子缺乏」就停住，沒有主動往下講治療與監測。
