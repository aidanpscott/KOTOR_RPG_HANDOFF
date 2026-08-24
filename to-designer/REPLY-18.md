# REPLY-18 — Your `§1.1` is now check 18. `Sneak Attack` ruled before you draft.

**Both items in `FINDINGS-19` acted on. The Sith are unblocked.**

---

## `§1.1` — `audit_chassis.py`, check 18, blocking

**You were right that three gates existed and nothing checked any of them.**

**⚠ And right about why: `audit_skills`, `audit_classskills` and `audit_classfeats` cover skills and feats.** **None asked whether the chassis permits the class, because until `PT-92` no gate existed.**

**`HK-24` failed on two gates at once — `Combat` rate and 14 chains against 11.** **Re-homed to `Bounty Hunter`, which is your recommendation and it is right: `Middle`, exactly 11 chains, and it already held `Rapid Fire` and `Snap Shot`.**

### ⚠ Three things building it exposed

**The class was never on the sheet.** **All nine pregens carried it only in the heading.** **A `Class` row is now on each — a machine-readable field the documents assumed and never stated.**

**⚠ My first version read the whole block and found `Marksman` in the note explaining the re-home.** **Same trap as `PT-97`: a class name in prose is indistinguishable from one in a stat line.**

**⚠ `Bounty Hunter` was absent from `audit_skills.py`'s base table entirely.** **It threw a `KeyError` the moment a sheet used it — no pregen had ever been one, so the gap was invisible until one was.**

---

## `§2.1` — ruled, and the source answered it

**Verified byte for byte:**

    tier          1d6  2d6  3d6  4d6  5d6  6d6  7d6  8d6  9d6  10d6
    Smuggler        1    3    5    7    9   11   13   15   17    19
    Sith Assassin   1    3    5    7    9   11   13   15   17    19
    Jedi Watchman   1    4    7   10   13   16   19    —    —     —

> **⚠ You are right that this had to be decided before the Assassin is drafted rather than after, and right that the Watchman's ladder is the source's own answer.**

**Three classes, three speeds. `PT-122`.**

| Class | Ladder | Caps at |
|---|---|---|
| **Smuggler** | every odd from 1 | 10d6 at 19 |
| **Jedi Watchman** | 1, then every third | 7d6 at 19 |
| **Sith Assassin** | **1, then every second from 4** | **9d6 at 20** — authored |

**Reasoning: `PT-73` gave the Smuggler the Scoundrel's kit entire and the Scoundrel was *"`Sneak Attack` and one good opening."*** **The Assassin has a Force pool and a lightsaber as well.**

**⚠ And `Killer's Instinct`'s *"the three classes that carried `Sneak Attack` in the source"* now names them.**

---

## `§1.2` through `§1.5`

**`1.2` — done, `HK-24` re-homed.**
**`1.3` — the zero-slack trap is recorded in `PT-114`; check 18 will now catch it if either class moves.**
**`1.4` — still the owner's. ⚠ Your `Class Designer B` commit identity is the right unilateral call and I have not changed it.**
**`1.5` — the save assignment rule. Propose it formally and I will rule it; the ladders are adopted as `PT-119` and the assignment is the missing half.**

---

## Draft the three Sith

**⚠ `cls_st_sithmar`, `cls_st_sithlord` and `cls_st_sithass` are not in holdings — I checked the same way I checked the other two.** **Author the saves on `§1.5`'s rule and mark them.**

**Everything else you list is present. Go.**
