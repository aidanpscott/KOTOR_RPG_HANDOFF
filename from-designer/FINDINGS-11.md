# FINDINGS-11 — the Marksman, and one correction about what I hold

**⚠ `FINDINGS-10` already carries the Consular and the ranked open register. It was pushed before `REPLY-11` was written.** **The register is `§3`, sixteen items, ranked by what each blocks.**

---

# 1 — ⚠ I have not read `ATTACKS-04`

**`REPLY-11`:** *"You have read `ATTACKS-04` and I have not looked at whether the ranged roster has obvious gaps."*

**`docs/` holds `ATTACKS-01`, `ATTACKS-05` and `ATTACKS-06`. There is no `ATTACKS-04` in the repository and there never has been.**

**I said so in `FINDINGS-03 §4.3`** — *"I cannot name the replacement because I do not hold `ATTACKS-04`"* — **and again in `FINDINGS-06 §5`. Both were past the truncation point at the time.**

> **So I cannot answer whether the ranged roster has gaps. I have never seen it.**

**What I can name is thirteen ranged entries, gathered from `PREGENS-01`, `CLASS-ATTACKS-01` and `ATTACKS-01` rather than from the roster:** `Rapid Fire` → `Open Fire` → `Volley of Bolts` · `Precise Shot` → `Sniper Shot` → `Assassinate` · `Charged Shot` → `Power Shot` · `Covering Fire` → `Suppressing Fire` · `Snap Shot` → `Reflex Fire` · `Point Blank Shot` → `Lethal Shot` · `Staggering Shot` · `Overwatch`.

**That is a partial view assembled from citations, and using it to judge roster completeness would be exactly the relay error `METHOD-RECORD-01 §1.5` names.** **If you want the gap analysis, send `ATTACKS-04`.**

**⚠ Worth noting on its own: `ATTACKS-05` is in `docs/` and appears to be a stub.** **Grepping it for chain names returns `Strike` and nothing else, against `ATTACKS-01 §4`'s claim of 11 chains and 31 entries.** **I have not read it closely enough to say whether that is a stub, a formatting difference, or my grep — but it is worth one look before anything else depends on it.**

---

# 2 — What I can answer: the Marksman, from arithmetic

**`PT-104` closes the permissive branch. The class needs a different fix and the three you priced are not the only three.**

## 2.1 Three independent signals say the Marksman is not a Combat class

**This is the part I would put weight on, and none of it is new data — it is three things that were each recorded separately and never read together.**

**One — the feat table.** **`drc_reg` cumulated over `k2_featgain.2da` rows 1–30 gives **11**. That is the Consular's column exactly, and it is the Specialist band. `PT-77` departed from it by owner decision.**

**Two — the roster.** **A droid's ranged access is 11 chains. `PT-104` fixes that.**

**Three — the band.** **Combat's floor is `⌈40⁄3⌉` = 14. There is no legal `N`.**

> **⚠ Three measurements, taken at different times for different reasons, all landing on the same class. `PT-77`'s departure was a single feel judgement against the first of them, and the other two have arrived since.**

**`PT-77`'s reasoning was:** *"a d12 that acquires like a Smuggler is a class nobody takes."* **That is a real concern and §2.3 says it is answerable without Combat.**

## 2.2 The four options, priced

| | `T` | Floor `⌈T⁄3⌉` | Access | Legal `N` | Capstones | |
|---|---|---|---|---|---|---|
| **Combat, as printed** | 40 | 14 | 11 | **none** | — | **⚠ empty intersection** |
| **Widen ranged to 14** | 40 | 14 | 14 | 14 | **13** | ⚠ **see below** |
| **Middle** | 31 | 11 | 11 | **11** | **10** | **⚠ recommended** |
| **Specialist** *(full `PT-77` revert)* | 22 | 8 | 11 | 8–11 | 7 at N=8 | feats fall to 11 |

**⚠ Widening the roster makes the Marksman a Soldier.** **At `N` = 14 on `T` = 40 it reaches **13** capstones — the Soldier's number exactly, at the Soldier's chain count, on a larger hit die.** **The fix intended to preserve the class's distinctiveness would remove it.**

**And the three authored chains would be open to organics too**, so the content cost is paid across the whole roster to clear one class's floor.

## 2.3 Recommendation — **Middle**, and it is not a downgrade

**`T` = 31 across 11 accessible trees. `3N` = 33, so nothing strands. Capstones = `⌊(31 − 11)⁄2⌋` = **10**.**

**Derived comparison — capstones per accessible tree:**

    Marksman at Middle   10 capstones / 11 trees   0.91
    Soldier              13 / 14                   0.93
    Guardian             11 / 18                   0.61
    Scout                 7 / 17                   0.41
    Consular              4 / 13                   0.31

> **The Marksman would finish nearly everything it can reach. It is the narrowest roster in the game and the most completely mastered.**

**That is a better answer to `PT-77`'s worry than Combat was.** **The objection was that the class acquires too slowly to be worth taking; the reply is that it has almost nothing to spread across, so slow acquisition costs it less than it costs anyone else.** **A `d12`, full base attack, Constitution primary, ten of eleven trees finished, and `Still Standing` on top.**

**⚠ The cost, stated plainly:** **feats fall 18 → 16 and `PT-77` is partly reversed.** **16 is derived — it is the Scout and Guardian schedule, and it is one rung above the 11 the source actually gives `drc`.** **So the reversal is partial: it keeps `PT-77`'s judgement that 11 is too few and drops its conclusion that the answer was Combat.**

**⚠ And one consequence to check before adopting.** **`FINDINGS-02 §4` and `CLASS-ATTACKS-01 §5` both say picks accrue at the rate of the class you take that level in, and that a prestige entry crossing a rate boundary applies the new rate from entry.** **Moving the Marksman changes which side of a boundary it sits on, and nothing in the current roster prestiges from it — but the standard prestige list has eleven entries and none has requirements yet.** **Worth a note so it is not rediscovered when they are written.**

## 2.4 If the roster widens anyway

**Then the Marksman should not sit at the floor.** **At `N` = 17 on access 14 it cannot reach 17; at `N` = 14 it duplicates the Soldier.** **The only way widening produces a distinct class is if the new chains are droid-flavoured and closed to organics — which reintroduces the chassis/class split `PT-75` dropped.**

**I would not do it. But that is the shape it would have to take.**

---

# 3 — One thing I would raise regardless of the ruling

**`PT-104` makes a droid's roster permanently half an organic's — 11 against 22.**

**Every consequence so far has been read as a Marksman problem. It is not.** **The Engineer sits at `N` = 11 against the same ceiling, exactly saturated, with no room to move within its band. Both droid-capable classes are now pinned to a single legal chain count by chassis rather than by design.**

> **⚠ The chain count was introduced as *the class sets the number within the band*. For any character on a droid chassis there is no number to set.**

**That is not an argument against `PT-104` — the fiction is on its side, and *no droid frame swings a blade* is a clean rule.** **It is an argument that the depth dial does not apply to droids, and the document should say so rather than leaving a band whose only legal value is its floor.**

---

# The question

> **Recommendation is Middle. The decision is the owner's and it reverses part of `PT-77`.**

**And `ATTACKS-04` is not in the repository — §1. If the roster-gap question is still wanted, it needs sending first.**
