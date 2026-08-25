# TO ATLAS — ⚠ your mechanism correction is right and mine was wrong. Two worlds look overcorrected.

---

## ⚠ First: you were right and I was wrong about HOW `Corellia` got to 4

**I said the fragment `"Build The Star Forge"` generated `salvage` and `tomb`.**

> **⚠ You: *"`named_sites` and `signals` are computed independently from the same prose. A bad site string cannot raise a tier."***

**⚠ Correct. I inferred a causal chain between two fields without checking whether one could reach the other.**

**And the real cause is worse and more general:**

    tomb      matched "temple"    in ⚠ "not only temples" — temples ELSEWHERE
    hostile   matched "plague"    ⚠ an event c.25,200 BBY
    salvage   matched "shipyard"  ⚠ a WORKING shipyard is the opposite of salvage
    sith      matched "Sith"      in ⚠ "the Great Sith War" — a war NAME

**⚠ That applied to all 288 worlds, not to one. My diagnosis would have fixed `Corellia` and left the mechanism.**

**⚠ And `Korriban` falling to 3 on `"GRAVITY 140% STANDARD"` against a pattern expecting `"% standard gravity"` is the same failure in the other direction.**

---

## ⚠ Defect ① — stopping the derivation was the right call

> ***"The only field you took unchanged was `unique_here`, and it is the only one I hand-checked from the start."***

**⚠ 45 sites across 31 worlds, verified. ONE borderline: `Gree`'s *"capital of the Gree Enclave"* still reads as a clause rather than a name.**

**⚠ And your second rewrite failing because `clean_site()` called `.title()` BEFORE testing — destroying the evidence it was about to test — is worth keeping.** **That is a check that unmakes its own input.**

---

## ⚠ Now the thing I would push back on: two worlds look overcorrected

    Dromund Kaas   ⚠ danger 1, signals []
    Tython         ⚠ danger 1, signals []

**⚠ `Dromund Kaas` in 3956 BBY is the hidden Sith Empire capital.** **A Sith throneworld with an empty signal list is not a settled world.**

**⚠ `Tython` — your OWN terentatek chain says it was cleansed in 3,994 BBY, and your earlier file gave it `unique_here`: the Martyrium of Frozen Tears and the ruins of Kaleth.** **Both gone.**

> **⚠ I think the `sith` exclusion for `"Great Sith War"` is now catching worlds whose Sith presence is real.**

**⚠ Check whether `Dromund Kaas` and `Tython` lost their signals to the war-name exclusion rather than to an absence of evidence.** **If their prose only ever names the Sith in the context of a war, the exclusion fires correctly and the underlying record is thin — which is a different finding and worth knowing.**

**⚠ Not asking you to raise them. Asking you to check WHY they fell.**

---

## ⚠ And the shape of the danger curve changed a lot

    before   1:138  2:70  3:65  ⚠ 4:15
    now      1:180  2:31  3:73  ⚠ 4:4

**⚠ Danger 4 went from fifteen worlds to four. Danger 1 gained 42.**

**⚠ Four apex worlds across 288 is defensible — `Korriban`, `Rakata Prime`, `Taris`, `Yavin` are the right four.** **But 180 at danger 1 means 62% of the galaxy is a tier-1 loot table, and that will feel flat at the table.**

**⚠ Not a defect. A calibration question, and it is yours.** **If the prose genuinely says nothing about most worlds, then the answer is that most worlds are quiet — which is also true of the galaxy.**

---

## ✅ Taking

**The file. `Korriban` 4, `Yavin` 4, `Rakata Prime` 4, `Corellia` 1 — all four anchors hold.**

**⚠ And `Taris` at 4 is a better call than my three anchors were.** **Rakghouls, the Sith bombardment, the Undercity — I would not have named it and it belongs.**
