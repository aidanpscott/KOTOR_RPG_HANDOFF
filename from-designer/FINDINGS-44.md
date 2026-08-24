# FINDINGS-44 — `PT-170` kills the Sharpshooter's capstone, and I can measure exactly how much

**`REPLY-39` says map size is a balance lever and that on `SCENARIOS-01`'s corridor *"the increment ladder never fires."*** **It lands on a class I revised two exchanges ago and I have quantified it rather than agreed with it.**

---

# 1 — The arithmetic

**Grid is 2 metres a square — `ACTION-ECONOMY-01 §9`. `SCENARIOS-01`'s corridor is 5 × 12 squares, so **10 × 24 metres**.**

**A rifle's increments under `PT-163` are 28 / 56 / 84, with the wall at 84.**

| The Sharpshooter tier needs | metres | squares |
|---|---|---|
| **`One Shot`**'s range clause to matter — target past one increment | 28 | **14** |
| **`Called Shot`**'s fourth increment, nearest edge | 84 | **42** |
| the same, far edge | 112 | **56** |

> **⚠ The corridor's longest axis is 12 squares. The whole map sits inside one increment, so no range penalty ever applies on it.**

**`One Shot`'s range clause is dead there. `Called Shot` needs a map **four times** the corridor's length before its nearest edge exists.**

## 1.1 What survives, and it is most of the chain

**⚠ Not as bad as it first reads, and worth stating before anyone reworks the class.**

    T1  cannot miss except on a natural 1     works at every range, on every map
    T1  ignores range penalties               ⚠ dead inside one increment
    T2  ignores cover                         works everywhere
    T3  fourth increment                      ⚠ needs ~42 squares of open ground

**Two of the four clauses are map-independent, and they are the two the class is actually played on.** **The `Sharpshooter` is not cut — its capstone is.**

---

# 2 — The fix, and it is inside the class

**A capstone that only fires outdoors is a capstone most campaigns never see.** **`REPLY-39` is right that map size is the lever, but the class should not be waiting on a gamemaster chapter that does not exist yet.**

**Proposed `Called Shot`, revised:**

| Tier | | Effect |
|---|---|---|
| ›› **`Called Shot`** | 8 | **You may take an aimed shot at a fourth increment** — 112 m with a rifle, where no other character may attack at all. **And if you did not move this turn, aiming costs a Bonus action rather than your declaration.** |

**⚠ The second clause is the one that works indoors, and it is the natural shape of the tier:** **a master sniper does not need as long.**

## 2.1 Priced

**It halves the cost of the whole chain — a can't-miss shot every round instead of every other round.**

    Sharpshooter, aiming every round       4.5 damage, guaranteed
    Sharpshooter, aiming every other round 2.25
    Korr, Barrage                          27.3 at roughly 70%

**⚠ Six times behind a Combat class even at double rate, because a rifle is `1d8` and `EQUIPMENT-01 §1` gives ranged attacks no ability modifier to damage.**

**The chain never becomes a damage engine. What doubles is *certainty*, which is what the class sells.**

**And the cost is real: *if you did not move this turn*.** **A Sharpshooter who repositions pays the full declaration, so the tier rewards holding a firing position — which is the class.**

---

# 3 — ⚠ Two things `REPLY-39` corrects that touch my work

**`§13` existed and `PT-160` said no range rules did.** **`FINDINGS-38 §1.1` is where that claim originated — I grepped `ACTION-ECONOMY-01` and `ATTACKS-01` for *maximum range*, *range penalty*, *short range* and *long range*, found nothing, and reported it.**

**⚠ `§13` is titled *Ranged flanking and weapon range* and none of my four search terms appears in its heading.** **The grep was against the wording I expected rather than the wording used.**

> **Same failure as `FINDINGS-11 §1`, where I searched `ATTACKS-05` for backticked chain names and it bolds them.** **Third instance of mine: a clean-looking negative from a search pointed at the wrong pattern.**

**⚠ The countermeasure is not a better search term.** **It is that a negative result about a document should be confirmed by opening the document, and I did not open `ACTION-ECONOMY-01`'s section list before reporting an absence in it.**

**And `Master Spotter` was never ambiguous.** **`FINDINGS-40 §3` asked whether *half maximum range* meant half the increment or half of three. `§13.2` already answers it. That question is withdrawn.**

---

# 4 — What is still mine and unanswered

**Six, none blocking:**

**The Commando's `+1 number` versus `×2`** — `FINDINGS-42 §2.3`.
**`Dueling`'s wield clause** — repriced by `REPLY-39`, so closed.
**`Superior Two-Weapon Fighting`** — restrict to Weaponmaster and Marauder, or extend to the Gunslinger.
**`Repair` on the Jedi Master and Sith Lord.**
**Form grants on prestige entry** — I recommended none.
**The five chain counts in `FINDINGS-42`** — assigned, not confirmed.

**And three classes remain undrafted: `Officer`, `Scoundrel`, `Vanguard`. None has a premise and two are scheduled last by owner order.**

---

# The question

> **⚠ `§2` — does `Called Shot` gain the Bonus-action clause? Without it the Sharpshooter's capstone needs a 42-square map and the largest one in the corpus is 12.**
