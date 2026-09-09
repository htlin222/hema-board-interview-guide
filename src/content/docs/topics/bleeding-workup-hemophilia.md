---
title: 出血檢查與 Hemophilia
sidebar:
  order: 12
---

跟 IDA 並列最高頻的門診/benign 主題，常出到「一路問到底」的完整題組。這裡有三層框架，疊起來用就能推導出幾乎所有出血案例的答題順序。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 框架一：先分「哪一層 hemostasis 出問題」——比抽血更早的第一步

**這是考官最想聽到的起手式，很多人直接跳去背 PT/aPTT 鑑別清單反而漏了這一步**。看到出血案例，第一個問題永遠是問病史裡的出血型態，而不是先看檢驗報告：

- **黏膜/皮膚出血、發生得快、傷口表淺就流不停**（瘀點、鼻血、牙齦出血、月經過多）→ 提示 **primary hemostasis** 問題（platelet 數量/功能、vWD）。
- **深層組織/關節出血、延遲發生**（受傷後幾小時才腫起來、hemarthrosis）→ 提示 **secondary hemostasis** 問題（凝血因子缺乏）。

這個分流決定你接下來要往 platelet/vWF 方向查，還是往 PT/aPTT/factor 方向查——**先講出這一句分流邏輯，再進入檢驗數字**，是這題的答題骨架。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 框架二：PT/aPTT 異常不用背鑑別清單，用 pathway 圖推

PT 和 aPTT 各自測的是哪些因子，其實是可以現場畫出來推的，不用死記鑑別診斷清單：

- **PT** 測 extrinsic pathway（factor VII）+ common pathway（X、V、II、fibrinogen）。
- **aPTT** 測 intrinsic pathway（XII、XI、IX、VIII）+ common pathway（X、V、II、fibrinogen）。

於是：

- **只有 aPTT 延長** → 問題只在 intrinsic pathway 獨有的因子（VIII、IX、XI、XII）或 lupus anticoagulant，common pathway 沒事所以 PT 正常。
- **只有 PT 延長** → 問題在 extrinsic pathway 獨有的 factor VII（半衰期最短，早期肝病/vit K 缺乏最早反映在這裡）。
- **PT/aPTT 都延長** → 問題落在兩條路徑共用的 common pathway（II、V、X、fibrinogen），或是多重因子同時缺乏（DIC、嚴重肝病、warfarin/vit K 缺乏、大量輸液稀釋）。

**這張圖背後最重要的例外**：isolated aPTT prolongation 的鑑別診斷裡包含 lupus anticoagulant／APS，但 **APS 臨床上最常見的表現是血栓，不是出血**——考官很愛在這裡反問，答的時候要主動點出這個矛盾。

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/></svg> 框架三：mixing study 的判讀邏輯——「量不夠」還是「有東西在擋」

Mixing study 在問一件事：把病人血漿跟正常血漿 1:1 混合，異常會不會被「稀釋掉」。

- **會恢復正常（correctable）** → 代表病人只是**缺量**，混進去的正常血漿把缺的因子補足了 → 指向 quantitative 因子缺乏。
- **不會恢復（not correctable）** → 代表有東西在**主動抑制**，正常血漿混進去也一樣被抑制掉 → 指向 inhibitor。

判讀時要注意兩個技術細節：

1. **要同時測 0 小時（立即）和 2 小時（培養後）**，因為有些 inhibitor 是 **time/temperature-dependent**（如 acquired hemophilia 的 anti-FVIII 抗體），立即測可能看起來是 correctable，培養 2 小時後才會現形變成 not correctable；lupus anticoagulant 通常是立即作用型，0 小時就看得出來。
2. **要跑一組正常血漿的 control** 一起培養對照——如果 control 組自己也 prolong，代表是檢體處理不當或 factor degradation 造成的技術性問題，不是真的有 inhibitor，不能誤判。

## 套用到實際問法

1. **Isolated aPTT prolongation 的鑑別診斷？**

   **最佳答法**：先用框架二的 pathway 邏輯鎖定「只剩 intrinsic pathway 獨有因子」的範圍,再依序從量的問題（因子缺乏）講到質的問題（inhibitor）,最後主動點出 lupus anticoagulant 和 vWD 這兩個例外。**依照**「先確認是缺量還是有抑制物、才決定後續要驗因子活性還是做 Bethesda assay」的邏輯順序鋪陳,答案才有層次而不是各因子平行羅列。**因為**考官真正要篩的是你敢不敢主動點出 lupus anticoagulant 臨床表現是血栓而非出血這個反直覺陷阱,以及你知不知道 vWD 是透過保護 FVIII 這個間接機制才會拉長 aPTT——這兩點都是常見答法只列因子清單、卻漏講機轉深度的地方。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Isolated aPTT prolongation 的鑑別診斷，重點不是背出四個因子，而是要立刻點名 lupus anticoagulant 這個會延長 aPTT、臨床卻是血栓體質的陷阱。」——一開口就先講出這個反直覺矛盾，才能讓考官相信你懂機轉、不是在背清單。

   </div>

   擬答：
   - **套框架二：PT 正常代表 common pathway 沒事，問題鎖定在 intrinsic pathway 獨有的因子。**
     - 先想因子缺乏：Factor VIII 缺乏（hemophilia A）、factor IX 缺乏（hemophilia B）、factor XI 缺乏、factor XII 缺乏。
   - **再想 acquired inhibitor：acquired hemophilia，通常是 anti-FVIII 抗體造成的後天抑制物。**
   - **接著一定要提 lupus anticoagulant/APS，這是這題最常被追問的陷阱。**
     - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> Lupus anticoagulant 在檢驗上會讓 aPTT 延長，但臨床上 APS 最主要的表現是血栓，不是出血，答的時候要主動點出這個矛盾，不要讓考官覺得你以為 lupus anticoagulant 等於出血傾向。
   - **最後別漏掉 vWD：因為 vWF 在血中會攜帶並保護 factor VIII，vWF 缺乏或功能異常時 FVIII 半衰期縮短、活性下降，也可能間接使 aPTT 延長。**

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「如果懷疑是 inhibitor 而不是單純因子缺乏，下一步要做什麼？」→ 做 mixing study 分辨是量的問題還是抑制物問題（見第 3、4 題）。
   - 「如果 mixing study 顯示 correctable，最後會不會指向 vWD？」→ 見第 11 題，correctable 之後不能停在 FVIII 缺乏，要往回問 vWF 保護不足的問題。

   </div>

2. **Combined PT/aPTT prolongation 的鑑別診斷？**

   **最佳答法**：先點出 common pathway 單一因子缺乏臨床上少見,把重心放在更常見的「多重因子同時缺乏」情境,並依「消耗性（DIC）→合成不良（肝病、vit K/warfarin）→稀釋性（大量輸液）」這個致病機轉的順序講,不要把幾個病因平鋪並列。**依照**「combined PT/aPTT 延長多半代表多重因子一起出問題」這個框架二的推論邏輯來安排講述順序,才能呈現出你是用機轉在分類,不是背清單。**因為**考官要看的是你能不能把 DIC、肝病、vit K 缺乏、稀釋這幾個機轉完全不同卻長得很像的鑑別診斷排出優先順序與致病邏輯上的差異,而不是背出同一串名詞卻講不出彼此的區別。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Combined PT/aPTT prolongation，common pathway 單一因子缺乏臨床上很少見，重點要放在 DIC、肝病、vit K 缺乏、稀釋這幾個機轉造成的多重因子缺乏。」——一開口就把重心從「單一因子」轉到「多重因子的致病機轉」，才是這題真正的鑑別度所在。

   </div>

   擬答：
   - **套框架二：PT、aPTT 都延長，代表問題落在兩條路徑共用的 common pathway，或是同時有多重因子缺乏。**
     - Common pathway 因子單一缺乏：factor II、factor V、factor X 缺乏。
   - **多重因子同時缺乏的情境要一併列出。**
     - DIC（消耗性凝血病變，同時消耗多種因子與 fibrinogen）。
     - 嚴重肝病，因肝臟合成凝血因子能力下降（factor VII 因半衰期最短通常最早受影響，但嚴重時 common pathway 因子也一起下降）。
     - Vitamin K 缺乏或使用 warfarin，影響 vitamin K 依賴性因子（II、VII、IX、X）的合成。
   - **也要提到大量輸液或大量輸血造成的稀釋性凝血病變**，因為快速大量補液會把體內原有的凝血因子稀釋掉，同樣會表現成 PT、aPTT 都延長。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「肝病造成的凝血異常，為什麼常常 PT 比 aPTT 先出現異常？」→ 因為 factor VII 半衰期最短，肝功能下降時最早反映在 PT（見框架二）。
   - 「如果懷疑 DIC，還會合併看到什麼實驗室數值變化？」→ Fibrinogen 同時被消耗下降，是與單純肝病或稀釋性凝血病變區分的線索。

   </div>

3. **異常延長，下一步要做什麼？**

   **最佳答法**：不用糾結是 isolated 還是 combined,直接講出「下一步統一都是 mixing study」,並主動說明這一步要回答的問題是什麼。**依照**「mixing study 分辨的是量不夠還是有東西在抑制」這個框架三的核心邏輯,把它定位成整個 workup 的分岔點——結果會決定要往因子活性檢驗還是 Bethesda assay 走。**因為**這題常被單獨抽出來考,考官要確認你知道 mixing study 在整個流程裡的角色是「承上啟下」,而不是把它跟前面 PT/aPTT 鑑別診斷混在一起講、講不出它為什麼是必經的下一步。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「不管前面是 isolated 還是 combined PT/aPTT prolongation，異常延長之後下一步永遠一樣——做 mixing study，分辨是缺量還是有抑制物。」——這句直接點出 mixing study 是整個 workup 的分岔點，不需要糾結先前的分類。

   </div>

   擬答：
   - **PT 或 aPTT 異常延長後，下一步是做 mixing study（對應框架三）**，目的是分辨病人是「因子量不夠」還是「有東西在主動抑制凝血」，這一步決定後續要往因子補充還是往找 inhibitor 的方向走。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「如果 mixing study 顯示 correctable，接下來要驗哪些項目確診？」→ 見第 5 題，驗對應因子活性（懷疑 vWD 時加驗 vWF antigen/activity）。
   - 「如果 not correctable，怎麼進一步定量抑制物的強度？」→ 見第 10 題的 Bethesda assay。

   </div>

4. **Mixing study 怎麼做、怎麼判讀？**

   **最佳答法**：先把「怎麼做」的兩個技術細節（0 小時與 2 小時都要測、要跑 control 組）講清楚,再進入「怎麼判讀」的兩層邏輯,不要跳過操作細節直接講 correctable/not correctable。**依照**「acquired hemophilia 的 anti-FVIII 抗體是 time/temperature-dependent、而 lupus anticoagulant 是立即作用」這個機轉差異,說明為什麼一定要測兩個時間點,才不會把 0 小時看似 correctable 的 acquired hemophilia 誤判成單純因子缺乏。**因為**這題的鑑別度不在於知不知道 correctable 代表缺量、not correctable 代表 inhibitor（這是基本常識）,而在於知不知道 0 小時/2 小時和 control 組這兩個操作細節如果漏掉,會直接導致誤判——這正是實務上最容易出錯、也最常被拿來考細節的地方。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Mixing study 不能只測一個時間點——一定要同時測 0 小時和 2 小時，因為像 acquired hemophilia 的 anti-FVIII 抗體是 time-dependent，立即測會被誤判成 correctable。」——先講這個操作細節，才能避免漏掉這題最常被拿來考的誤判陷阱。

   </div>

   擬答：
   - **做法：把病人血漿和正常血漿以 1:1 混合，同時測 0 小時（立即）和 2 小時（37°C 培養後）兩個時間點，並且要跑一組正常血漿的 control 一起培養對照。**
     - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 一定要同時測 0 小時和 2 小時，因為有些 inhibitor 是 time/temperature-dependent，像 acquired hemophilia 的 anti-FVIII 抗體，立即測可能看起來 correctable，培養 2 小時後才會現形變成 not correctable；lupus anticoagulant 通常是立即作用型，0 小時就看得出來。
     - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 一定要跑 control 組：如果 control 組自己也 prolong，代表是檢體處理不當或 factor degradation 造成的技術性問題，不是真的有 inhibitor，不能誤判成陽性。
   - **判讀第一層：correctable 還是 not correctable。**
     - Correctable（混合後恢復正常）代表病人只是缺量，混進去的正常血漿把缺的因子補足了，指向 quantitative 因子缺乏。
     - Not correctable（混合後仍然延長）代表有東西在主動抑制，正常血漿混進去也一樣被抑制掉，指向 inhibitor 存在。
   - **判讀第二層：確認是 inhibitor pattern 之後，再進一步鑑別是哪一種 inhibitor。**
     - Lupus anticoagulant：通常不會顯著降低單一特定因子的活性。
     - Specific factor inhibitor（如 acquired hemophilia 的 anti-FVIII）：會讓對應的特定因子活性明顯下降。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「如果 0 小時 correctable、2 小時卻變成 not correctable，最可能是什麼診斷？」→ Acquired hemophilia（見第 10 題）。
   - 「如果 control 組自己也 prolong，代表什麼，會不會誤判成有 inhibitor？」→ 代表檢體處理不當或 factor degradation 造成的技術性問題，不是真的有 inhibitor，不能誤判成陽性。

   </div>

5. **確診因子缺乏後，還要驗哪些？**

   **最佳答法**：先講為什麼優先驗 factor VIII、IX、XI 而不是 factor XII,再主動接上「如果懷疑 vWD 要加驗 vWF antigen/activity」這一段,不要驗完因子就停住。**依照**「factor XII 缺乏雖然會讓 aPTT 延長,但臨床上不會造成出血」這個機轉,說明驗因子的優先順序要跟著臨床出血風險走,而不是跟著哪個因子會讓 aPTT 延長走。**因為**考官要確認你懂得分辨「檢驗異常」跟「臨床有意義」是兩件事,同時要看你會不會主動想到 FVIII 活性下降有可能是 vWD 透過保護機制被間接拖累,所以不能只驗 FVIII 就下結論,得同時看 vWF 的量跟功能才能完整鑑別。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「驗因子的優先順序要跟著臨床出血風險走，不是跟著誰會讓 aPTT 延長走——factor XII 缺乏會延長 aPTT，臨床上卻不太出血，不用急著驗。」——這句直接區分「檢驗異常」跟「臨床有意義」，是這題的鑑別度所在。

   </div>

   擬答：
   - **針對 hemophilia 相關因子，主要驗 factor VIII、factor IX、factor XI 活性，用來確診並分型。**
     - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> Factor XII 缺乏雖然會讓 aPTT 延長，但臨床上通常不會造成出血，所以一般不急著驗。
   - **如果臨床上懷疑 vWD，要加驗 vWF antigen 和 vWF activity（ristocetin cofactor assay）**，因為 vWD 的診斷需要同時看 vWF 的量和功能，不能只靠 factor VIII 活性。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「Factor VIII 活性偏低，怎麼判斷是原發性 hemophilia A 還是繼發於 vWD？」→ 要同時看 vWF antigen/activity，見第 11 題完整推理鏈。
   - 「確診 vWD 之後，還要怎麼分型？」→ 見第 11 題的 type 1/2/3 分型。

   </div>

6. **Hemophilia 的嚴重度分級與對應 factor level？**

   **最佳答法**：講分級時不要只背三個數字區間,要把每一級都掛回「誘發出血所需的創傷門檻」這個臨床意義,並主動強調 mild hemophilia 常常拖到成年才因手術或拔牙被診斷出來這一點。**依照**「factor level 越低、自發性出血的門檻越低」這個劑量效應邏輯,把 severe/moderate/mild 講成一個連續的臨床光譜,而不是三個孤立的數字級距。**因為**考官要看的是你知不知道這個分級系統的臨床意義是什麼、而不是能不能背出 1%、5%、40% 這幾個數字——尤其 mild hemophilia 因為平常不太出血、容易被忽略到成年才確診,這一點正是分級的臨床意義所在,也是常見答法只背數字就漏掉的地方。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Hemophilia 嚴重度分級不是背三個數字區間，而是 factor level 越低、自發性出血門檻越低的連續光譜——mild 甚至常常拖到成年手術或拔牙時才被診斷出來。」——一開口把數字掛回臨床意義，才不會讓答案聽起來像在背表格。

   </div>

   擬答：
   - **Severe：factor level 小於 1%（小於 0.01 IU/mL）**，容易出現自發性出血，好發於關節與肌肉，不需要明顯外傷就會出血。
   - **Moderate：factor level 介於 1% 到 5%**，通常在中度創傷後才會出血，自發性出血相對少見。
   - **Mild：factor level 大於 5%、小於 40%**（注意下界是「大於」5%，不是「5%到」——5% 本身算在 moderate 的上限，兩級不能重疊），通常需要較大創傷或接受手術時才會出血，很多病人甚至到成年後才因為手術或拔牙出血被診斷出來。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「Severe hemophilia 的病人，什麼時候要開始考慮 prophylaxis？」→ 見第 8 題，第一次關節出血後或幼年期就要開始。
   - 「Mild hemophilia 平常較少出血，臨床上最典型的表現是什麼？」→ 仍是 hemarthrosis（見第 7 題），只是 mild 病人常要等到較大創傷或手術才顯現。

   </div>

7. **Hemophilia 最常見的臨床表現？**

   **最佳答法**：先講 hemarthrosis,並主動把它扣回框架一「深層組織、延遲發生」的出血型態分流邏輯,再往下延伸講反覆關節出血造成的 hemophilic arthropathy,不要講完典型表現就停住。**依照**「hemarthrosis 屬於 secondary hemostasis 問題該有的出血型態」這個框架一的判準,把臨床表現跟機轉框架連起來講,而不是把「hemophilia 會關節出血」當成單獨背誦的事實。**因為**考官要看的是你能不能把不同題目之間的框架串起來用、顯示你是理解機轉而非片段記憶,同時要看你會不會主動往後延伸講到慢性關節病變這個長期後果,這才能點出為什麼後面會問到 prophylaxis 的必要性。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Hemophilia 最典型的表現是 hemarthrosis，這正好呼應框架一『深層組織、延遲發生』的 secondary hemostasis 出血型態。」——直接把臨床表現扣回一開始講的分流框架，顯示你是用邏輯串起整篇答案，而不是片段背誦。

   </div>

   擬答：
   - **最典型的表現是 hemarthrosis，也就是關節內出血，好發在膝關節、肘關節、踝關節。**
     - 回扣框架一：hemarthrosis 屬於「深層組織、延遲發生」型的出血，本來就該從 secondary hemostasis（凝血因子）的方向去想，這裡剛好是驗證框架一分流邏輯的具體例子。
   - **反覆的關節出血如果沒有妥善控制，會逐漸導致 hemophilic arthropathy**，也就是慢性關節病變、關節破壞與功能喪失，所以早期預防出血非常重要。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「反覆關節出血如果沒控制，最終會演變成什麼？為什麼要提早介入？」→ Hemophilic arthropathy，這正是第 8 題 prophylaxis 要提早開始的理由。
   - 「同樣是深層、延遲發生的出血，換成術後出血不止，思考邏輯有沒有不一樣？」→ 邏輯相同，都先套框架一判斷是 primary 還是 secondary hemostasis 問題。

   </div>

8. **何時要開始 prophylaxis？目標 factor level？**

   **最佳答法**：先講清楚為什麼要「提早」在第一次關節出血後或幼年期就開始 prophylaxis,再講目標 trough level 這個數字本身是會隨指引與藥物調整的,不要把大於 1% 講成一個死的定值就結束。**依照**「反覆關節出血會累積成不可逆的 hemophilic arthropathy」這個上一題已經建立的機轉,說明 prophylaxis 的邏輯是搶在關節破壞發生之前介入,而不是等到已經有關節病變才治療。**因為**考官要看的是你懂不懂 prophylaxis timing 背後「預防不可逆傷害」這個核心理由、而不只是背出一個時間點;同時主動承認目標數字會依現行指引與藥物半衰期調整,能顯示你不是死背單一數字,而是理解這是一個會隨治療進展變動的臨床判斷。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「Prophylaxis 要在第一次關節出血後、或幼年期就開始，目的是搶在 hemophilic arthropathy 這種不可逆傷害發生之前介入。」——先講「為什麼要提早」這個核心理由，再帶目標數字，考官才會覺得你懂治療邏輯，而不是背 trough level。

   </div>

   擬答：
   - **建議在病人第一次關節出血後、或幼年期，就開始 primary prophylaxis**，目的是預防反覆關節出血累積造成的慢性關節病變，而不是等到已經出現關節破壞才開始治療。
   - **目標 trough level 通常維持在大於 1%**，把病人從 severe 的表現型拉到接近 moderate 的出血頻率。
     - 依現行國際指引，實際目標可能設定更高（如大於 3% 到 5%），需要依照最新治療建議、所使用藥物的半衰期與劑型來調整,不是一個固定不變的數字。

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「如果病人已經產生 inhibitor，prophylaxis 的藥物選擇會不一樣嗎？」→ 見第 9 題，可以考慮 emicizumab 這類非因子藥物作為長期預防。
   - 「目標 trough level 為什麼不是一個固定數字？」→ 依現行指引與所用藥物半衰期、劑型調整，不是死背單一數字。

   </div>

9. **有 inhibitor 的病人出血時怎麼處理（bypassing agent）？何時考慮？**

   **最佳答法**：先講清楚「為什麼一般因子補充會失效」的機轉,再帶出 bypassing agent 是為了繞過這個機轉才存在的解法,最後把急性止血（FEIBA/rFVIIa）跟長期處理（ITI、emicizumab）分成兩個層次講。**依照**「抗體會把補進去的因子中和掉」這個機轉,說明 bypassing agent 的邏輯是繞過被抑制的那個因子、而不是單純加大補充劑量,這樣才能講出為什麼要換一整類藥物而不是提高劑量。**因為**考官要看的是你懂不懂補充治療失效背後的免疫機轉,而不是只背出 FEIBA、rFVIIa 這兩個藥名;同時要看你會不會主動區分「急性出血先止血」跟「長期想辦法根除抗體或繞開它」是兩個不同時間尺度、不同目標的治療決策,而不是把所有藥物混在一起講。

   <div class="callout callout-keywords">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

   「有 inhibitor 的病人，補進去的因子會被抗體中和掉，所以治療邏輯不是加大劑量，而是換成 bypassing agent 繞過那個被抑制的因子。」——先講清楚補充治療為什麼會失效，才有理由帶出 FEIBA、rFVIIa 這些換藥選項。

   </div>

   擬答：
   - **當病人產生 anti-FVIII 或 anti-FIX 抗體時，一般的因子補充治療會失效，因為補進去的因子會被抗體中和掉，這時要改用 bypassing agent 來繞過被抑制的那個因子。**
     - 第一線選擇之一是 **FEIBA**（activated prothrombin complex concentrate）。
     - 另一個選擇是 **recombinant activated factor VII（rFVIIa, NovoSeven）**。
   - **長期治療方面，可以考慮 immune tolerance induction（ITI）來嘗試根除抗體，或使用新型非因子藥物（如 emicizumab）作為長期出血預防的替代方案。**

   <div class="callout callout-followup">
   <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

   - 「長期想根除抗體，除了 ITI，還有什麼選項？」→ 見第 10 題的 steroid、cyclophosphamide、rituximab 等免疫抑制治療。
   - 「這個抑制物到底是不是 anti-FVIII 抗體造成的 acquired hemophilia，要怎麼跟 lupus anticoagulant 鑑別？」→ 見第 10 題，套 mixing study 的 time-dependent pattern，再加上臨床出血傾向相反這兩條證據鏈。

   </div>

10. **Acquired hemophilia 怎麼跟 lupus coagulopathy 鑑別？需要哪些檢查？怎麼治療？**

    **最佳答法**：鑑別診斷這一段要同時調用框架三（mixing study 的 time-dependent inhibitor pattern）和框架二（lupus anticoagulant 傾向血栓而非出血的矛盾）這兩條線索,而不是只套一個框架就作答;確診檢查跟治療則按「定量→急性處理→根除病因」的順序講完整。**依照**「acquired hemophilia 是 time-dependent specific factor inhibitor、lupus anticoagulant 是立即型且不影響單一因子活性」這個 mixing study 判讀邏輯,搭配兩者臨床出血傾向完全相反這個事實,做出雙重佐證的鑑別,而不是只憑其中一個線索下結論。**因為**這題本質上是全篇框架整合的總考點——考官要看你能不能同時想到「檢驗判讀」跟「臨床表現」兩條完全不同的證據鏈同時指向同一個鑑別診斷,而不是死記兩個病名的定義;能答出治療要分「急性止血」跟「根除抗體」兩層,也才顯示你理解 bypassing agent 跟 immunosuppression 是解決不同問題的兩種手段。

    <div class="callout callout-keywords">
    <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

    「Acquired hemophilia 和 lupus anticoagulant 要同時用兩條證據鏈鑑別——mixing study 的 time-dependent pattern，加上兩者臨床出血傾向完全相反這個事實。」——這題是全篇框架整合題，一開口就展現你同時調用檢驗判讀和臨床表現兩條線索，而不是只背兩個病名的定義。

    </div>

    擬答：
    - **鑑別要套框架三的 mixing study 判讀邏輯。**
      - Acquired hemophilia 是 specific factor inhibitor，通常是 anti-FVIII 抗體，mixing study 會呈現 time-dependent inhibitor pattern（0 小時可能 correctable、2 小時培養後變成 not correctable），而且對應的特定因子活性會明顯下降。
      - Lupus anticoagulant 通常不會顯著降低單一因子的活性，而且臨床上較少真的表現出血，甚至偏向血栓風險，這點呼應框架二提到的例外——考官很愛在這裡反問兩者的差異。
    - **確診要做 Bethesda assay，測出 inhibitor titer 來定量抗體的抑制強度。**
    - **治療分兩個層次。**
      - 出血急性期先用 bypassing agent（FEIBA 或 rFVIIa）控制出血。
      - 根除 inhibitor 則使用 **steroid**（可單獨使用或合併其他藥物）、**cyclophosphamide**、或 **rituximab**。
      - 文獻上合併治療（steroid 加 cyclophosphamide）的緩解率可能比單用 steroid 高，但需要權衡感染等副作用風險，不是一律都要合併使用。

    <div class="callout callout-followup">
    <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

    - 「確診之後怎麼定量抑制物的強度？」→ Bethesda assay，測出 inhibitor titer。
    - 「如果換成單純的 lupus anticoagulant／APS 病人，治療方向會完全不同，為什麼？」→ APS 治療重點是抗凝血而非止血，呼應框架二提到的血栓體質矛盾。

    </div>

11. **Isolated aPTT prolongation，mixing study 後恢復正常，這樣的 pattern 要怎麼往下推理，最後會指向什麼診斷？**

    **最佳答法**：不要停在「mixing study correctable，所以是因子缺乏」就結束，要把框架三跟框架二串起來、再往前多推一步。**依照**「mixing study correctable 代表量的問題（框架三），isolated aPTT 又把範圍鎖定在 intrinsic pathway 獨有的因子（框架二）」這個雙框架疊加的邏輯，先推出最可能缺的是 factor VIII，**因為**它是 intrinsic pathway 因子裡最常見、也最容易受間接機轉影響而下降的一個；但真正拉開分數的地方是接下來這一步——講出 FVIII 活性下降不能就地停在「缺 FVIII」，還要主動往回問「是不是 vWF 保護不足才連帶讓 FVIII 下降」，因為 vWF 在血漿中負責攜帶並保護 factor VIII 避免被過早清除，一旦 vWF 量不足或功能異常，FVIII 半衰期就會縮短、活性隨之下降，最後才推到 von Willebrand disease（VWD）這個診斷——這才是把框架二、框架三跟診斷邏輯完整串起來的答法，而不是把 FVIII 缺乏本身當成終點。

    <div class="callout callout-keywords">
    <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5" fill="currentColor"/></svg>破題關鍵句</div>

    「Mixing study correctable 之後不能停在『缺 FVIII』就結束，要往回問一句『是不是 vWF 保護不足才連帶讓 FVIII 下降』，才會推到 von Willebrand disease。」——這句話直接示範把框架二、框架三跟診斷邏輯串起來的完整推理，而不是把 FVIII 缺乏當成終點。

    </div>

    擬答：
    - **第一層：套框架三，correctable 代表量的問題，不是 inhibitor。**
      - Mixing study 混合後恢復正常，代表病人只是缺量，混進去的正常血漿把缺的因子補足了，方向是找因子缺乏，不用往 inhibitor（Bethesda assay）那條路走。
    - **第二層：套框架二，isolated aPTT 把範圍鎖定在 intrinsic pathway 獨有的因子。**
      - PT 正常代表 common pathway 沒事，問題只可能在 factor VIII、IX、XI（factor XII 缺乏臨床上不太出血，優先度較低）。
      - 這幾個因子裡最常見、也最容易被問到「最可能是哪一個」的答案是 **factor VIII**。
    - **第三層：不能停在「FVIII 缺乏」，要主動往回推一步問「為什麼 FVIII 會缺」，指向 von Willebrand disease。**
      - <svg class="icon-inline icon-warning" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg> 常見陷阱是答到「FVIII 缺乏」就停住，忘了 FVIII 在血漿中是靠 vWF 攜帶並保護才不會被過早清除的——vWF 缺乏或功能異常時，FVIII 半衰期縮短、活性繼發性下降，這才是為什麼 isolated aPTT prolongation 最後常常指向 VWD，而不是原發性 hemophilia A。
      - **VWD 是最常見的遺傳性出血疾病**，這是流行病學上的基本事實，答題時可以順帶點出來強化這個診斷的合理性。
      - 確診要靠 **vWF antigen** 和 **vWF activity（ristocetin cofactor assay）**（呼應第 5 題已經提過的檢查），同時看量跟功能才能完整鑑別，不能只看 factor VIII 活性下降就下結論。
      - 分型上大方向分成：**type 1**（量的部分性缺乏，最常見）、**type 2**（功能性異常，又分好幾個次分型）、**type 3**（幾乎完全缺乏，最嚴重、但最少見）。

    <div class="callout callout-followup">
    <div class="callout-title"><svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>追問</div>

    - 「VWD 的三個分型，在 vWF antigen/activity 檢驗上分別是什麼 pattern？」→ Type 1 是量的部分性缺乏、type 2 是功能性異常、type 3 是幾乎完全缺乏（本題已列出分型）。
    - 「如果病人是停經前女性且有月經過多，這個線索怎麼跟框架一對起來？」→ 黏膜/皮膚出血型態提示 primary hemostasis 問題，呼應 VWD 本質上是 primary hemostasis 異常，也可延伸到 [IDA 篇](/hema-board-interview-guide/topics/iron-deficiency-anemia/) 月經量怎麼問的邏輯。

    </div>

## <svg class="icon-inline" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9.003a1 1 0 0 1 1.517-.859l4.997 2.997a1 1 0 0 1 0 1.718l-4.997 2.997A1 1 0 0 1 9 14.996z"/><circle cx="12" cy="12" r="10"/></svg> 相關 YouTube 影片

下列影片都是實際搜尋後、再用 YouTube oEmbed 逐一驗證過確實存在且可播放的（2026-09 檢查），不是憑印象列出的連結；每一支都標明**為什麼選它**、**對應到本頁哪一段**，看之前先知道要帶走什麼。

- **[Hemostasis: Lesson 4 – Tests (INR, PTT, platelets, fibrinogen, D-dimer)](https://www.youtube.com/watch?v=q548IZGbt28)** — Strong Medicine · 25:21
  - **對應框架二的完整版**：PT 與 aPTT 各自測哪些因子、怎麼從 pathway 反推鑑別診斷，本頁那張推理圖的觀念都在這支裡。
- **[How to interpret mixing studies (prolonged PT/PTT)](https://www.youtube.com/watch?v=aVnc2S5K1rE)** — Medmastery · 4:28
  - **對應框架三**：correctable vs not correctable 的判讀邏輯，四分半講完，看完再回來記 0 小時／2 小時／control 這三個技術細節。
- **[Hemophilia & Other Coagulation Deficiencies: Hemostasis – Lesson 11](https://www.youtube.com/watch?v=bG-VNAkbr74)** — Strong Medicine · 13:34
  - **對應第 6–9 題**：嚴重度分級、prophylaxis、inhibitor 與 bypassing agent 的臨床脈絡一次串起來。
- **[Von Willebrand Disease & Qualitative Platelet Disorders: Hemostasis – Lesson 10](https://www.youtube.com/watch?v=fP6Q-iAAzdM)** — Strong Medicine · 14:07
  - **對應第 11 題**：為什麼 vWF 不足會把 FVIII 一起拖下水、進而延長 aPTT，這條間接機轉是該題的核心。

## 容易被電的點

- 沒有先講出血型態分流（框架一）就直接跳進 PT/aPTT 數字，考官會覺得你只是背檢驗流程而不理解邏輯。
- Mixing study 只看單一時間點、忘記對照 control 組。
- 把 combined 與 isolated PT/aPTT prolongation 的鑑別診斷清單搞混——用框架二的 pathway 圖現場推，比背清單穩。
- 只回答「因子缺乏」就停住，沒有主動往下講治療與監測。
