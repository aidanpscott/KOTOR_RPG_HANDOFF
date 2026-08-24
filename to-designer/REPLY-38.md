# REPLY-38 — `baseitems.2da` is in holdings. The range work amended, and one verification passed.

**Both games' files are in `data/`. `PT-168`.**

---

## ⚠ `EQUIPMENT-01` was faithful

**`maxattackrange` carries exactly four values across both games — 17, 23, 25, 28 — and K1 and K2 agree on every weapon.** **`PT-163` through `PT-166` were built from eight rows of `EQUIPMENT-01` and the source confirms them.**

---

## Two things the file has that we did not

### The hard ceiling is 50 metres

    maxrange = 50   on every ranged weapon
    maxattackrange  17 / 23 / 25 / 28

**⚠ Two different numbers. A weapon *engages* at 23 and cannot *reach* past 50.**

**This validates the increment reading rather than replacing it.** **50 is about two increments for a pistol** — **our three-increment ceiling is more generous than the source, and the `−2` steps are what pays for it.**

**Snapped to 48 m and stated as the absolute maximum for any ranged attack.**

### ⚠ Grenades have a throw range and we never had one

    maxattackrange 25   on twelve grenades and the rocket

**`ACTION-ECONOMY-01 §53` rules a grenade throw is an Attack rather than Gear, and nothing said how far.**

> **24 metres, and it does not take increments.** **You can throw it that far or you cannot** — an arm behind it rather than a barrel, and the source gives one value instead of a ladder.

**⚠ And this is why `PT-166`'s collapse of 25 into 24 mattered more than it looked.** **25 is the most common `maxattackrange` in the file, thirteen items, and twelve are grenades.** **The Blaster Carbine shares the number by coincidence.**

---

## ⚠ And a verification that passed — against the right game

**I diffed all 24 `EQUIPMENT-01` weapons against both files.**

**Against K2: ten disagreed, every one exactly one die step low.**
**Against K1: every weapon matches exactly.**

**`EQUIPMENT-01 §105` has the choice and the reason on file:** *"K1's numbers make a cleaner system. A vibrosword is 2d6, so a K1 lightsaber sits exactly one die step above it. K2's 2d10 is two steps, which widens the gap between a Jedi and everyone else for no reason our port needs."*

> **⚠ A consistent ten-weapon offset that looks like error and is a decision with its reasoning recorded.**

**Stated in `ACTION-ECONOMY-01` because the next reader with `k2_baseitems.2da` open will find the same ten and reach for a fix.**

**⚠ That is the shape to expect on the 49 Force powers too.** **Some of what looks wrong will be ruled, and `PT-146` says owner-signed changes stay.**

---

## The file has more we have not used

**`weaponsize`, `weaponwield`, `damageflags`, `critthreat`, `crithitmult` — all present, all unexamined.**

**⚠ Worth a pass when you next touch equipment.** **`weaponwield` in particular: it is what decides one-handed against two-handed, and `ATTACKS-05`'s Two-Weapon chains assume a rule nobody has checked against source.**

---

## Then, unchanged

**The Agent rebuild — the only `X`.**
**The eight `P`s.**
**And the 49 Force powers.**
