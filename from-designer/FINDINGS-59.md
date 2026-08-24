# FINDINGS-59 — ⚠ Audit: `PT-122` contradicts a chain in the same document it was written into

**Owner: *"we did a shit ton of work beforehand… it sounds like one of you was just ignoring all that past work."*** **Audited. `§1` is the finding; `§2` is the method; `§3` is what the method cleared.**

---

# 1 — ⚠ `FEATS-LIBRARY-01` holds two incompatible `Sneak Attack` systems

**Both are in the same file, 568 lines apart, and neither references the other.**

## Line 124 — the chain

    Sneak Attack           Requires Stealth 5.   add 2d6, capped at Stealth ÷ 3
    › Improved             Requires Stealth 10.  +4d6
    ›› Master              Requires Stealth 15.  +6d6, critical multiplier +1

**Three tiers. `ATTACKS-01 §3`: every tier replaces the one below. **Caps at 6d6**, gated on `Stealth` ranks, available to anyone who buys it.**

## Line 692 — `PT-122`'s ladder

    Smuggler        every odd level from 1        10d6 at 19
    Sith Assassin   1, then every second from 5    9d6 at 20
    Jedi Watchman   1, then every third            7d6 at 19

**⚠ A ladder rising with class level, granted to three named classes, capping at 10d6 — and gated on nothing.**

## 1.1 They cannot both be true

    the chain    3 tiers · 6d6 max · bought · gated on Stealth ranks
    the ladder   10 steps · 10d6 max · granted · gated on class

> **⚠ The ladder's floor at level 19 is 10d6. The chain's ceiling at any level is 6d6.** **A Smuggler holds both and the document does not say which.**

**And the interaction with `Killer's Instinct` is priced against the chain, not the ladder:** *"a character with this and `Master Sneak Attack` deals 6d6 + 3d6 — roughly 31 average… lethal to most non-boss targets."*

**⚠ Under the ladder it is `10d6 + 3d6` — **45 average**, against wound points that equal Constitution.** **The line calling 31 *"lethal to most non-boss targets"* was written about the smaller number.**

## 1.2 Whose error

**`PT-122` is a class-workstream ruling. It was written into `FEATS-LIBRARY-01` without reconciling against the chain already at line 124 of that file.**

**⚠ That is my lane and the owner's read is correct.** **The ruling reasons entirely from `k2_featgain.2da` and class identity, and never asks what the corpus already says a `Sneak Attack` is.**

**And I compounded it.** **`FINDINGS-58` set the Scoundrel at **12d6** — above the ladder, twice the chain, and I never opened line 124 either.**

---

# 2 — The audit method, so this is repeatable

**⚠ Checking feature *names* is worthless — every name I authored now appears in the corpus because the main agent adopted it. `Never the Same Twice` is minutes old and already in `FEATS-LIBRARY-01`.**

**What works is checking **the same mechanic for two different numbers**:**

    for each mechanic a class ruling depends on
      grep every figure the corpus states for it
      if the set has more than one value, one of them is ours

**That found `Sneak Attack` in one pass, and it is the check that should have run before `PT-122`.**

---

# 3 — What the audit cleared

**Feat totals — all 35 classes with a rate cross-checked against `FEAT-SCHEDULE-01`. **Zero mismatches**.**

**`crithitmult`** — checked in `FINDINGS-42`, uniform in K1, three K2 exceptions we do not port. **Clean.**

**Band and stranding checks** — all 35 pass, `CLASS-STATE-03`'s generated output.

**⚠ And the ones already caught and fixed rather than missed:** `ATTACKS-06` versus `FORMS-01` on *forms are feats* — `PT-185`. `PT-160` claiming no range rules when `§13` held them — `REPLY-39`. The `Dueling` wield clause — `PT-...`. The `Master Spotter` half-range, which `§13.2` had already answered. **Five contradictions found, four resolved, and this is the fifth.**

---

# 4 — Which model should stand

**⚠ Owner's call, and the two are not equally costly to change.**

**The chain, at 6d6.** **Consistent with every other feat chain in the game, gated on `Stealth`, buyable by anyone.** **⚠ Cost: `PT-122` is void, and with it the three-speed differentiation that keeps Smuggler, Assassin and Watchman distinct. Those three classes then share their defining mechanic identically — which is the exact problem `PT-122` was written to solve.**

**The ladder, at 10d6.** **Keeps three classes distinct.** **⚠ Cost: line 124's chain must be deleted, `Killer's Instinct`'s worked example is wrong by 14 damage, and one feat chain in the game scales with class level while every other is three tiers.**

**⚠ There is a third option and it costs least: **keep both, and make them the same object**.** **The chain's three tiers become the *access*, and a class ladder sets how fast the dice rise within it — so `Master Sneak Attack` is the gate and the class decides whether you reach 6d6 at level 12 or level 24.** **Caps at 6d6 for everyone, three speeds preserved, and `Killer's Instinct`'s worked example stays true.**

---

# The question

> **⚠ Chain at 6d6, ladder at 10d6, or the third option — one chain with class-set speed, capping at 6d6?**

**The `Scoundrel` in `FINDINGS-58` is void either way and I will redraft it once this is settled.**
