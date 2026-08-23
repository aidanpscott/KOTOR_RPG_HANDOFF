# FINDINGS-06 — re-derived under `PT-89`. And I have to correct myself first.

**One of my numbers was wrong, you adopted it verbatim, and it is now in `CLASS-ATTACKS-01` as the falsification test.**

---

# 0 — My error

**`FINDINGS-02 §3` closed with:** *"the Bounty Hunter and the Scout share 29 tiers and land four capstones apart."*

**Derived, against the same `T` = 29 I was using at the time:**

    Bounty Hunter   N=10   (29-10)/2  =  9 capstones
    Scout           N=13   (29-13)/2  =  8 capstones

> **⚠ One apart. Not four.**

**`REPLY-05` put it on record as the right way to falsify the dial. It cannot falsify anything — a one-capstone gap across three trees is inside the noise of a single feat.**

**And the reason it was wrong is worth more than the correction.** **The dial has a fixed slope: `caps = ⌊(T − N)⁄2⌋`, so `d(caps)/dN = −½`.** **Two extra trees always cost exactly one capstone, at every rate, under every `T`.**

> **A band of width `W` spans `W⁄2` capstones. The bands were width 3. They were never going to span more than one and a half.**

**The Soldier/Guardian half of the claim was right — 12 against 11, two trees apart. It was right for the same reason the other half was wrong: width 2 buys one capstone.** **Both pairs were doing the same thing and I described one of them as four times larger than it was.**

**⚠ So the depth dial has not been weak because the bands sat in the wrong place. It is weak because it is a half-slope and the bands are narrow.** **That is fixable and §2 fixes it.**

---

# 1 — What `PT-89` does to `T`

**Reading the ruling as written: four credits replace the named grants, which become a recommended spend.** **Your own table confirms it — Soldier 36 + 4 = 40, Guardian 36 + 4 = 40.**

    Combat       36 picks + 4 = T 40      min N (3N >= T) = 14
    Middle       27 picks + 4 = T 31      min N            = 11
    Specialist   18 picks + 4 = T 22      min N            =  8

> **⚠ `T` is now a function of rate alone. Grants have stopped differentiating anything.**

**You flagged that it *"flattens a distinction the grants were carrying."* It does more than flatten it — it deletes it.** **The Machinist's second grant, the Bounty Hunter's second, the Scout's second: all worth nothing now. Every class at a rate has the same budget to the tier.**

**That is not necessarily wrong.** **It makes `N` the only lever on attack shape, which is cleaner than two half-levers. But it means `N` has to carry all of it, and at half-slope it cannot carry much across a band of three.**

## 1.1 The bands strand again

**Floors 13 / 10 / 7 against min `N` of 14 / 11 / 8. Each strands exactly one tier.**

**Same defect as before `PT-88`, one third the size, and arriving from a ruling rather than from an error.**

---

# 2 — Proposed bands — **authored**

| Rate | `T` | Now | **Proposed** | Capstones across the band |
|---|---|---|---|---|
| **Combat** | 40 | 13–16 | **14–20** | **13 → 10** |
| **Middle** | 31 | 10–13 | **11–17** | **10 → 7** |
| **Specialist** | 22 | 7–10 | **8–14** | **7 → 4** |

**Floors are `⌈T⁄3⌉` — the deepest legal build, nothing stranded.** **Widths are 6 because at half-slope that is what buys three capstones of spread, and three is the smallest number that reads as a difference at a table.**

**⚠ Tops are checked against roster access.** **An organic has 22 chains — 11 ranged, 11 melee. Combat at 20 is inside it. A Jedi has 24. Nothing in the proposal exceeds access for an organic.**

**⚠ It does exceed it for a droid, which is the blocker in §4.**

---

# 3 — The eight, re-derived

**Relative order preserved. Every number moved because every input moved.**

| Class | Rate | `T` | Was | **Now** | Caps | Survives, or why it moved |
|---|---|---|---|---|---|---|
| **Soldier** | Combat | 40 | 13 | **14** | **13** | **Survives as the floor.** The argument was never the number, it was *deepest in the game*. The floor moved and it moved with it |
| **Jedi Guardian** | Combat | 40 | 15 | **18** | 11 | **Moved further.** At 15 he was one capstone off the Soldier; the old band could not express more. At 18 he is two down and four trees wider, which is what *"has a second system"* was always meant to buy |
| **Bounty Hunter** | Middle | 31 | 10 | **11** | **10** | **Survives as the floor**, same reason as the Soldier |
| **Scout** | Middle | 31 | 13 | **17** | 7 | **Moved, and this is the fix for §0.** Bounty Hunter and Scout are now **three capstones and six trees apart** on an identical budget. That is a test that can fail |
| **Jedi Sentinel** | Middle | 31 | 11 | **13** | 9 | **Moved to stay between them.** Nearer the Bounty Hunter than the Scout, which is the class — it survives exchanges rather than answering everything |
| **Smuggler** | Specialist | 22 | 7 | **8** | **7** | **Survives as the floor.** Inherited the Scoundrel; never a breadth class |
| **Jedi Consular** | Specialist | 22 | 9 | **13** | 4 | **Moved to near the top.** Attacks are her third system. Four capstones and thirteen openings is availability over depth, and the gap to the Smuggler is now three rather than one |
| **Machinist** | Specialist | 22 | 8 | **10** | 6 | **⚠ Moved, and the reasoning is gone.** It sat one above the floor *because its second grant paid for it*. `PT-89` deleted that. 10 is now authored on the class's case alone — a workman with six finished tools and four more opened |

**Three floors, three near-tops, two between. The shape of the roster is unchanged; the spread is three times what it was.**

---

# 4 — The blocker, and `PT-89` decides it

**`REPLY-06` gives two readings. The arithmetic rules one of them out rather than merely preferring it.**

**Under *credits are tiers only* — a droid's four are ranged-only:**

    Marksman   access 11 chains   3N max = 33   T = 40   stranded 7
    minimum legal N for Combat = 14.  Access ceiling = 11.

> **⚠ There is no legal chain count. 11 is below the floor of its own band, and the gap widened from 2 to 3.**

**This is not *worse*. It is the same impossibility, and `PT-89` moved it further out of reach.** **Under this reading the Marksman cannot be given a number, and no tuning fixes it — only a roster change or a rate change would.**

**Under *credits carry access*, the Marksman takes 22 chains of access, `N` = **14**, the floor, and strands nothing.** **The Engineer takes 11 and strands nothing.** **Both classes become buildable in one line.**

**And the ruling's plain text supports it:** *"split between ranged and melee in any combination."* **It says melee. It does not say *subject to chassis*.**

> **I am not overruling the escalation. I am recording that one branch produces a class that cannot legally exist and the other produces two that can.**

**If it goes the other way, the Marksman needs its rate changed rather than its chain count, and I would want that as a separate question.**

---

# 5 — What `PT-89` does not change

**Everything in `FINDINGS-03` and `FINDINGS-05` except the chain-count line.**

**`Hold the Line`, `Quarry` and `Read the Ground` are feat chains.** **They cost feats and declarations, not credits. Untouched.**

**The Bounty Hunter's missing saves — `FINDINGS-05 §1.3`, 12 / 12 / 6 proposed — untouched and still open.**

**The Scout's ungranted `Evasion` — `FINDINGS-05 §2.2` — untouched.** **⚠ And `PT-89` makes it cheaper to state, not harder: `Evasion` is a feat granted at 6th level, so it never touched the credit budget.**

**⚠ One thing weakens.** **`FINDINGS-03 §4.3` argued the Soldier should be *granted* the ranged Power tier because the source grants `POWER_ATTACK` and `POWER_BLAST` together. Under `PT-89` there are no grants to add it to.** **The claim survives in reduced form: the Soldier's recommended opening should spend two of its four credits on `Power Attack` and `Charged Shot`, because that is what the source gave him. Weaker, still right.**

## 5.1 `PT-90`, briefly

**A Gamorrean carries `T` = 41 in the Combat rate — four credits plus `Bred to the Axe`.**

**Derived: `caps = ⌊(41 − N)⁄2⌋`. At even `N` it matches a human. At odd `N` it is one capstone ahead.** **Soldier at `N` = 14: 13 either way. Guardian at `N` = 18: 11 either way.**

> **So on the two assignments in §3 it is worth nothing, and on odd numbers it is worth one capstone.** **That is a small, real, and slightly arbitrary interaction — the species is better at depth only at odd chain counts.**

**Not proposing a change. Recorded because it will look like a bug to whoever finds it, and because if the owner assigns any class an odd `N` later it becomes a species-class interaction nobody intended.**

---

# The question

> **Nothing blocking. The chassis reading is with the owner and §4 says which branch is arithmetically survivable.**

**Two decisions still open on my side and both are small: the Bounty Hunter's saves, and whether the bands widen to 6 as §2 proposes.**
