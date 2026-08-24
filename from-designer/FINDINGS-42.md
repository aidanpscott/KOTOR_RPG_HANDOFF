# FINDINGS-42 — the five missing chain counts, and the crit column checked

**Nothing was waiting, so I took the two items in my own lane that nothing blocks.**

---

# 1 — The five ported prestige classes now have chain counts

**`FINDINGS-39 §3` flagged them as the only classes in the roster with a rate and no chain count. `PT-159` makes the number matter for any character holding two classes, so they can no longer be left blank.**

| Class | Rate | `T` | **N** | Caps | The class's own case |
|---|---|---|---|---|---|
| **Jedi Watchman** | Middle | 31 | **12** | **9** | Continues the Sentinel at 13 and narrows by one. Same capstones, one fewer tree — a Sentinel who went undercover keeps the depth and loses the breadth |
| **Sith Marauder** | Middle | 31 | **11** | **10** | **The floor.** Both its chains — `Ignore Pain` and `Increase Combat Damage` — are flat and passive, so it needs no trees of its own and should finish the ones it takes |
| **Jedi Master** | Specialist | 22 | **11** | **5** | Two trees narrower than the `Sage` at 13, one capstone deeper. The Master still holds a blade; the Sage is knowledge |
| **Sith Lord** | Specialist | 22 | **11** | **5** | The Jedi Master's mirror, and the same reasoning |
| **Tech Specialist** | Specialist | 22 | **8** | **7** | **The floor, and it is the only thing the class has — §1.1** |

**All five checked: inside their band, nothing stranded.**

## 1.1 ⚠ The Tech Specialist at 8 is a deliberate use of the one axis it has

**`FINDINGS-26 §3.6` established the problem: `tec_granted` in `feat.2da` is five proficiencies and nothing else, and it is the only class in either game with no granted class feature.** **`REPLY-09` declined to cut it and no chain has been authored since.**

> **At `N` = 8 it reaches **seven capstones** — the most of any `Specialist` in the game, and more than the `Smuggler`, `Machinist`, `Consular`, `Sage` or `Sorcerer`.**

**⚠ That is not a fix and I am not presenting it as one.** **It is a way for the class to be *something* without inventing a chain the source never gave it: no tricks, and the most finished attack trees on its side of the roster.**

**And it fits what the class already is** — a completion prestige class, `CLASS-ROSTER-01 §6`, whose skills are whichever of `Engineer` and `Machinist` you are missing. **Completing things is its whole shape.**

## 1.2 ⚠ And it sharpens the Marauder/Battlemaster pair

    Sith Marauder      11 chains   10 capstones    deep
    Sith Battlemaster  18          11              wide

**`FINDINGS-34` moved the Battlemaster to `Combat` because at `Middle`/16 the two were identical on six axes. They now differ on seven, and the chain counts are the clearest of them: the Marauder finishes almost everything it opens; the Battlemaster opens nearly twice as much.**

---

# 2 — `critthreat` and `crithitmult`, checked as flagged

**`FINDINGS-41 §3` flagged the column as in holdings and unexamined, with three class features resting on it.**

## 2.1 ✓ `ATTACKS-01 §12.1`'s worked examples are correct

**Derived, `k1_baseitems.2da`. `critthreat` is a *width* — how many numbers threaten — not a range.**

    Vibrosword                 2   -> 19–20   ✓ ATTACKS-01 says 19–20
    Double-Bladed Lightsaber   1   -> 20 only ✓ ATTACKS-01 says 20 only
    Lightsaber                 2   -> 19–20
    Blaster Rifle              2   -> 19–20   ✓ matches PREGENS-01's Vess
    Blaster Pistol             1   -> 20 only

**Both examples in `§12.1` hold against source. Nothing to correct.**

## 2.2 ⚠ `crithitmult` is 2 on every single weapon in the file

**Every row. Swords, lightsabers, pistols, rifles, staffs, repeating blasters — all `2`.**

> **⚠ The critical multiplier carries no information and cannot distinguish a weapon, in exactly the way `PT-72` found of base attack bonus.**

**Which is not a defect — `ATTACKS-01 §12.1` already treats it as a constant and gives `Power Attack` the only way to change it.** **But it means weapon choice is expressed on two axes, damage dice and threat width, and a third that looks like an axis is flat.**

**⚠ Worth stating where `PT-72` is stated, so nobody builds a weapon distinction on it.**

## 2.3 ⚠ And it found a defect in my own Commando

**`FINDINGS-29 §4.3`, `Master Chosen Weapon`:** *"your threat range with that family widens by one."*

**`§12.1` expresses threat as a multiplier of the printed width — `×2`, `×3`, `×4`. *Widens by one* is not in that language and the two readings disagree:**

    a pistol, width 1     +1 number -> 19–20     ×2 -> 19–20      same
    a vibrosword, width 2 +1 number -> 18–20     ×2 -> 17–20      ⚠ different

**Same family as the `Master Spotter` ambiguity in `FINDINGS-40 §3` — a clause that was unambiguous while the system it referenced did not exist.**

**Recommend `+1 number`.** **The Precision chains already own `×2 / ×3 / ×4`, and a class feature that multiplies on top of a chain that multiplies is the compounding `ATTACKS-01 §2.3` was written to stop:** *"Each chain was priced as though its capstone discount were the reward for eight levels. Nothing priced the sum."*

---

# 3 — What this leaves

**⚠ Every class with a rate now has a chain count. Thirty-five of thirty-eight.**

**The three without are `Officer`, `Scoundrel` and `Vanguard`, and none is drafted.**

    Officer     no premise. Its space is occupied three times by things that are not classes
    Scoundrel   second-last by owner order; ruled the Sneak Attack specialist
    Vanguard    last by owner order; no purpose exists anywhere in docs/

---

# The question

> **⚠ `§2.3` — `+1 number` or `×2` on the Commando's capstone? They differ on every weapon with a printed width above 1.**

**The five chain counts need confirming but nothing waits on them.**
