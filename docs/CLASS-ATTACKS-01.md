# CLASS-ATTACKS-01 — grants and schedules

**The document `ATTACKS-01 §7` and `§11.6` have both been deferring to.**

> **Two separate things.** **What a class is *given*, and how fast it *picks*.** **The first is identity; the second is budget.**

---

## 1. The principle, from the source

**`ATTACKS-01 §7` recorded it and this document acts on it:**

> ***"In KOTOR, class identity came from what you were given.*** **Scouts were granted Rapid Shot and Targeting, Smugglers got Sniper Shot and Sneak Attack, Soldiers got Power Attack.** ***Selectable lists ran 50 to 69 feats for nearly every class and were almost identical."***

**So grants are few and load-bearing. The selectable roster is wide and shared.**

**⚠ This is the third time the project has landed on the same rule.** **`Killer's Instinct` and `Squad Tactics` set the precedent: class identity belongs in grants, not in roster-level locks.**

---

## 2. Rate assignment

**Three rates. `ATTACKS-01 §11.3` defines them; this assigns them.**

| Rate | Classes | Source signal |
|---|---|---|
| **Combat** | **Soldier · Jedi Guardian · Marksman** | **Feats 18–23 at level 30.** **The Soldier's 23 is the ceiling; the Marksman's 18 is the floor** |
| **Middle** | **Bounty Hunter · Scout · Jedi Sentinel · Weaponmaster · Marauder · Watchman · Engineer** | **16 or 15 at level 30. `featgain.2da` treats these as one kind of character** |
| **Specialist** | **Smuggler · Jedi Consular · Machinist · Jedi Master · Sith Lord · Assassin** | **11 or 10 at level 30** |

**Derived from `FEAT-SCHEDULE-01`'s level-30 totals**, because that is the only signal the source gives about how fast a class acquires anything.

### 2.1 Scout and Guardian share a rate — `PT-54.2`

> **K2's feat schedules for Scout, Guardian, Weaponmaster and Marauder are byte-identical, rows 1 through 30.**

**They differ on BAB and hit die, and that is where the Guardian's advantage is paid.** **Charging it a second time through attack picks would double-count.**

### 2.2 Two surprises worth stating

**The Soldier is alone at the top and that is honest.** **23 against 16 is not a rounding difference.** **Combat is a thin tier because the source made it one.**

### 2.2a The Bounty Hunter is Middle, and it is the third class built this way

**Full BAB and d10, `Middle` picks.** **`PT-68`.**

> **It hits as often and as hard as a Soldier, carries a Scout's bag of tricks, and knows twice what a Soldier knows.**

**⚠ The only class in the game with full BAB, d10, and a `Middle` pick rate.**

**⚠ The Marksman is Specialist, not Combat.** **`featgain.2da` gives it 11 at level 30 — the Smuggler's number, not the Soldier's.** **Its d12 and full BAB carry its combat identity instead.** *The name is the source's and it misleads.*

---

## 3. The schedule, extended to thirty

**`ATTACKS-01 §11.3` ran to level 20. `PT-55` set the ceiling at 30.**

| Level | Combat | Middle | Specialist |
|---|---|---|---|
| **1** | **+2** (2) | +1 (1) | +1 (1) |
| **2** | +1 (3) | +1 (2) | **—** (1) |
| **3** | +1 (4) | +1 (3) | +1 (2) |
| **4** | +1 (5) | +1 (4) | **—** (2) |
| **5** | +1 (6) | +1 (5) | +1 (3) |
| **6** | **+2** (8) | +1 (6) | **—** (3) |
| **7** | +1 (9) | **—** (6) | +1 (4) |
| **8** | +1 (10) | +1 (7) | **—** (4) |
| **9** | +1 (11) | +1 (8) | +1 (5) |
| **10** | +1 (12) | +1 (9) | +1 (6) |
| **11** | **+2** (14) | +1 (10) | +1 (7) |
| **12** | +1 (15) | +1 (11) | **—** (7) |
| **13** | +1 (16) | +1 (12) | +1 (8) |
| **14** | +1 (17) | **—** (12) | **—** (8) |
| **15** | +1 (18) | +1 (13) | +1 (9) |
| **16** | **+2** (20) | +1 (14) | **—** (9) |
| **17** | +1 (21) | +1 (15) | +1 (10) |
| **18** | +1 (22) | +1 (16) | **—** (10) |
| **19** | +1 (23) | +1 (17) | +1 (11) |
| **20** | +1 (24) | +1 (18) | +1 (12) |
| **21** | **+2** (26) | **—** (18) | +1 (13) |
| **22** | +1 (27) | +1 (19) | **—** (13) |
| **23** | +1 (28) | +1 (20) | +1 (14) |
| **24** | +1 (29) | +1 (21) | **—** (14) |
| **25** | +1 (30) | +1 (22) | +1 (15) |
| **26** | **+2** (32) | +1 (23) | **—** (15) |
| **27** | +1 (33) | +1 (24) | +1 (16) |
| **28** | +1 (34) | **—** (24) | **—** (16) |
| **29** | +1 (35) | +1 (25) | +1 (17) |
| **30** | +1 (36) | **+2** (27) | +1 (18) |

**All three land on a whole number of trees at both twenty and thirty.**

| | L20 | trees | **L30** | **trees** |
|---|---|---|---|---|
| **Combat** | 24 | 8 | **36** | **12** |
| **Middle** | 18 | 6 | **27** | **9** |
| **Specialist** | 12 | 4 | **18** | **6** |

### 2.3 Chains are a band, not a number

**Owner ruling. The pick totals above buy a *range* of chains, and each class sits somewhere in its band.**

| Rate | `T` | **Chains entered** | Capstones at the floor | at the top |
|---|---|---|---|---|
| **Combat** | **40** | **14–20** | **13** | **10** |
| **Middle** | **31** | **11–17** | **10** | **7** |
| **Specialist** | **22** | **8–14** | **7** | **4** |

**⚠ Raised twice. 11–13 → 13–16 → 14–20. `PT-88`, then `PT-95`.**

**Floors are `⌈T ⁄ 3⌉` — the deepest legal build, nothing stranded. Widths are 6.**

> **⚠ Why 6, and it is the finding that forced the second raise.** **`caps = ⌊(T − N) ⁄ 2⌋`, so the slope is exactly `−½`. Two extra trees always cost one capstone, at every rate, under every `T`.**

**A band of width `W` spans `W ⁄ 2` capstones.** **The width-3 bands could never span more than one and a half, whatever their floor.** **The dial was not mispositioned — it was too narrow to register.**

**Width 6 spans three capstones, which is the smallest spread that reads as a difference at a table.**

**⚠ Tops checked against roster access.** **An organic reaches 22 chains — 11 ranged, 11 melee — and a Jedi 24. Combat's top of 20 fits.**

**⚠ Raised from 11–13 / 8–10 / 5–7 by `PT-88`.** **The old bands stranded picks at every value except the top.**

> **A tree absorbs 1 to 3 tiers. `N` trees absorb between `N` and `3N`. A class spends its whole budget only if `3N ≥ T`, where `T` is picks plus granted tier-1 chains.**

    Combat, T=37:   N=11 -> 4 stranded   N=12 -> 1   N=13 -> 0
    Middle,  T=29:  N=8  -> 5 stranded   N=9  -> 2   N=10 -> 0
    Specialist, 19: N=5  -> 4 stranded   N=6  -> 1   N=7  -> 0

**⚠ A stranded pick is worse than a wasted one.** **Three currencies, no crossover — `ATTACKS-01 §11.1` — so it cannot become a feat or a skill point.** **It is a number on the sheet that buys nothing, and a player who finds it will assume they misread the rules.**

**Chain count is a *depth* dial.** **Capstones reachable = `⌊(T − N) ⁄ 2⌋`** — *each tree costs 1 tier to enter, each capstone 2 more.*

    Combat, T=37:  N=13 -> 12 capstones   N=16 -> 10 capstones

> **Low `N`: few trees, all finished. High `N`: more answers, fewer capstones.** **That is the trade, and it works two above where the band was printed.**

> **⚠ The rate sets the band. The class sets the number within it.**

**Assigned so far:**

| Class | Rate | Chains | Feats@30 | Capstones |
|---|---|---|---|---|
| **Soldier** | Combat | **14** | 23 | 13 |
| **Jedi Guardian** | Combat | **18** | 20 | 11 |
| **Marksman** | Combat | **14 ⚠** | 18 | 13 |
| **Bounty Hunter** | Middle | **11** | 16 | 10 |
| **Scout** | Middle | **17** | 16 | 7 |
| **Jedi Sentinel** | Middle | **13** | 15 | 9 |
| **Engineer** | Middle | **11** | 16 | 10 |
| **Smuggler** | Specialist | **8** | 11 | 7 |
| **Jedi Consular** | Specialist | **13** | 11 | 4 |
| **Machinist** | Specialist | **10** | 11 | 6 |

**⚠ RULED, and it does not resolve. `PT-104`. Owner: droids may not spend attack credits on melee.**

**So a droid Marksman's four credits are ranged-only and its accessible roster stays at 11 chains.**

    credits   T    stranded   legal N in band 14-20
       4      40       7          none
       3      39       6          none
       2      38       5          none
       0      36       3          none

> **⚠ Reducing a droid's credits does not help.** **The gap is band-against-access, not budget.** **Combat's floor is 14 and droid ranged access ceilings at 11 — an empty intersection at every credit count.**

**Three fixes and only two are real:**

**A droid-specific band.** **⚠ Does not work.** `⌈T⁄3⌉` is 12 against an access ceiling of 11 — still empty.

**Drop the Marksman to `Middle`.** **Works: `T` = 31, access 11, `3N` = 33, nothing stranded at N=11.** **⚠ But feats fall from 18 to 16, and it reverses `PT-77`, which moved the class *to* `Combat` by owner ruling.**

**Widen droid ranged access.** **Needs at least 14 accessible chains against the roster's 11 — three more to author.** **⚠ Leaves `PT-77` intact and gives droids something they lack rather than taking something away.**

**⚠ Owner ruling wanted, and it is now a narrower question than before: reverse `PT-77`, or author three ranged chains.**

**⚠ The Marksman's 14 remains unbuildable until then. `PT-99`.**

> **Under *credits carry access* it is legal and strands nothing.** **Under *credits are tiers only* a droid Marksman reaches 11 ranged chains, and the Combat band is 14–20.** **Empty intersection — no legal number exists at that rate.**

**⚠ If the restrictive branch is chosen, 14 is void and the Marksman needs its *rate* revisited rather than its chain count.**

**Recorded because adopting the number in one document while another calls the question open is the divergence pattern this project has named.** **Cheaper to reconcile now than after the prestige classes read from it.**

**⚠ All ten assigned. `PT-95`.** **Three floors — Soldier, Bounty Hunter, Smuggler — three near-tops, and the rest between.**

> **The Bounty Hunter and the Scout share `T` = 31 and land three capstones and six trees apart. That is a test that can fail in play.**

**⚠ An earlier version of this note said four capstones apart. It was one.** **Corrected — the width-3 band could not have produced four.**

**⚠ All three moved when the band was raised — `PT-88`.** **The old values were assigned against 11–13 and two of them stranded picks under 13–16.**

> **⚠ The Guardian's 13 is the one to watch.** **It was the *top* of the old band — the widest Combat build. Under the new band 13 is the *floor* — the deepest.** **The number did not change and its meaning inverted.** **Moved to 15, which is what 13 used to mean.**

**Soldier 13 is deliberate and it is the only class at the floor.** **`§4.4`: he has the fewest skills, no Force, and the worst non-weapon saves in the game. Twelve capstones is the compensation.** **⚠ If the Soldier ever moves to 16, the Guardian drops to 13 and they swap identities — they must not both sit at 13.**

**⚠ `Marksman` sits at the floor of the `Combat` band on both axes and takes the most skill points in the tier.** **A d12 that endures, acquires slowly for its tier, and knows more than the Soldier.**

**A `Middle` class with 8 chains buys deeper into each; one with 10 buys wider.** **Same picks, different shape.**

**⚠ Not assigned yet.** **Each class gets its number as it is designed** — agenda `§1.2`. **Until then, treat the midpoint as the working figure.**

---

**Combat's `+2` lands every fifth level from 1.** **Middle skips every seventh, and takes `+2` at 30 to land whole.** **Specialist runs on odd levels, plus 10, 11, 20 and 30.**

> **⚠ A pick is not a feat.** **`ATTACKS-01 §11.1`: three currencies, three tracks, no crossover.** **An attack pick cannot buy a feat and a feat cannot buy an attack.**

---

## 3a. Four attack credits at 1st level — owner ruling

> **Every class receives four attack credits at 1st level. The player splits them between ranged and melee in any combination.**

**Four ranged, four melee, two and two — any split. `PT-89`.**

### What this replaces

**Named grants per class.** **The previous rule handed each class three or four specific tier-1 chains and gave the player no choice.**

**⚠ The grants in `§4` are not deleted. They become the class's *recommended* opening** — *what a Soldier looks like if you do not want to choose.* **The four credits are what a player who does want to choose spends instead.**

### ⚠ It raises `T` for every class, and by different amounts

    class        picks   old T   new T
    Soldier         36      38      40
    Guardian        36      37      40
    Marksman        36      37      40
    Scout           27      29      31
    Smuggler        18      19      22

**Classes that were granted fewer chains gain more.** **The Guardian and the Smuggler gain three; the Soldier gains two.**

> **⚠ That flattens a distinction the grants were carrying.** **Re-check the chain counts against the new `T` before treating them as settled.**

### ⚠ And it overrides the chassis block, which was not obvious

**`ATTACKS-01` line 124: *"Melee is chassis-blocked; ranged is role-blocked. No droid frame swings a blade."***

**But this rule says *every class* gets four credits split *any* way.** **A droid `Marksman` spending one on melee has entered a melee tree.**

**Two readings, and they cannot both hold:**

**The credits carry access.** **Then the chassis block yields to the class rule, and the `Marksman` and `Engineer` stranding problem is solved** — *a droid with a vibroblade is not absurd, and `PT-75` already said droids and organics draw from one class list.*

**The credits are tiers only, spendable within existing access.** **⚠ Then a droid's four credits are ranged-only, `T` rises to 40 against an access ceiling of 33, and the Marksman strands seven instead of five.** **The ruling makes the blocker worse.**

**⚠ Owner ruling wanted. The first reading resolves an open blocker; the second deepens it.**

---

## 4. Grants

**Two or three per class, at 1st level, costing no pick.** **These are the class.**

| Class | **Recommended opening** — `PT-89` | Why |
|---|---|---|
| **Soldier** | `Power Attack` · `Charged Shot` · `Strike` · `Shoot` | **The source grants `POWER_ATTACK` *and* `POWER_BLAST` at 1st — `feat.2da`, `sol_granted`.** **`POWER_BLAST` is `usetype` 1, ranged active, tiers at 4 and 8 — which is `Charged Shot`'s ladder exactly.** **⚠ Four grants, not three. He is the only class the source gives weight in both hands** |
| **Bounty Hunter** | `Rapid Fire` · `Snap Shot` · `Shoot` | Takes targets alive and moving. Volume and reaction, not weight |
| **Scout** | `Rapid Fire` · `Precise Shot` · `Shoot` | **The source grants Rapid Shot and Targeting.** These are their equivalents |
| **Smuggler** | `Precise Shot` · `Sneak Attack`* · `Shoot` | **The source grants Sniper Shot and Sneak Attack.** *`Sneak Attack` is a feat rider, not an attack — `PT-29` |
| **Scoundrel** *(prestige)* | `Snap Shot` · `Point Blank Shot` · `Shoot` | **⚠ Held.** Close, fast, and gone. **This was the pre-merge Smuggler's row and survived `PT-73` as an orphan** — reassigned to the prestige class rather than deleted, because it is a real identity and the Scoundrel needs one |
| **Machinist** | `Charged Shot` · `Covering Fire` · `Shoot` | Fights by preparation and by denying ground |
| **Jedi Guardian** | `Sarlacc Sweep` · `Strike` · `Shoot` | The blade first. A crowd answer at 1st level |
| **Jedi Sentinel** | `Deflecting Slash` · `Strike` · `Shoot` | Defence that answers back |
| **Jedi Consular** | `Saber Pierce` · `Strike` · `Shoot` | One precise blade, because the Force is the weapon |
| **Marksman** | `Power Attack` · `Strike` · `Shoot` | **⚠ Melee restored.** `PT-75` dropped the droid/organic class split; an organic may take this class and `ATTACKS-05`'s closure is a *chassis* restriction, not a class one |
| **Engineer** | `Covering Fire` · `Shoot` | Support, and the only attack it reliably contributes |

**⚠ `Strike` and `Shoot` are the free baseline** — `ATTACKS-01`. **Listing them is a statement that no class is denied them, not a grant of anything scarce.**

### 4.1 The recommended openings

**⚠ Superseded as *grants* by `§3a`. Retained as what each class looks like if the player does not want to choose.**

### 4.1a A chassis may be closed out of a grant; a class is not

**Every class gets three grants.** **⚠ Was *"both droid classes get two"* — `PT-75` ruled they are not droid classes.** **A chassis may still be closed out of a grant; the class is not.**

> **`Strike` is closed to droids and nothing replaces it.** **`ATTACKS-05` bars melee to every chassis, which `PT-26` extended to opportunity attacks.**

**This is a real deficit and it is the droid upgrade system's job to answer** — `DROID-SKILLS-01 §3`, unbuilt.

---

## 5. Prestige classes

**Grants nothing. Picks continue from the character's rate.**

**⚠ And no entry credit anywhere** — `MULTICLASS-01 §5` removed the system entirely. **The rate a class pays at is the whole mechanism.**

> **`FEAT-SCHEDULE-01` established that prestige feat columns read from *their own* class level.** **Attack picks do not.** **A Guardian who enters Weaponmaster at 15 keeps counting attack picks from character level 15, because both classes are Middle and the rate does not change.**

**⚠ Where entry crosses a rate boundary, the new rate applies from the level of entry and picks already spent are not recalculated.** **A Consular entering Jedi Master stays Specialist and nothing happens. A Smuggler entering Assassin likewise.**

**No prestige entry in the current list crosses a boundary.** **If one ever does, this is the rule.**

---

## 6. What this does not settle

**Which attacks are *restricted* rather than merely ungranted.** **`Killer's Instinct` and `Squad Tactics` are class-locked and nothing defines the mechanism.**

**⚠ The multiclass pick question is closed** — `MULTICLASS-01 §3.1`. **Neither summing nor the higher rate: picks accrue at the rate of the class you take that level in, read at your current character level.**

**The Smuggler's full identity.** **Three grants are not a class.**
