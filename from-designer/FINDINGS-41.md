# FINDINGS-41 — the Duelist's premise verified against source, and one feat that fails the same test

**`REPLY-38` flagged `weaponwield` as *"a rule nobody has checked against source."* I checked it, because the `Duelist` is built on it.**

---

# 1 — ✓ The Duelist's condition holds

**`FINDINGS-27 §2.1` gave `Single Combat` a wielding condition on owner instruction — *a single one-handed weapon and an empty off hand, two-handers excluded* — and I had no source for what one-handed meant.**

**Derived, `k1_baseitems.2da`:**

    wield 1   Stun Baton
    wield 2   Long Sword · Vibrosword · Short Sword · Vibroblade · Lightsaber ·
              Short Lightsaber · Gammorean Battleaxe
    wield 3   Quarterstaff · Double-Bladed Sword · Vibro Double-Blade ·
              Double-Bladed Lightsaber · Gaffi Stick · Wookiee Warblade
    wield 4   all six pistols
    wield 5   all six rifles
    wield 6   Repeating Blaster · Heavy Repeating Blaster

**`ACTION-ECONOMY-01 §658` already reads it correctly:** *"1, 2 and 4 are one-handed and may be paired. 3, 5 and 6 are two-handed and may not."*

> **✓ So the Duelist may hold a sword, a vibroblade, a lightsaber, a short lightsaber or a pistol — and may not hold a quarterstaff, a double-blade or any rifle.**

**That is what the owner described and the source supports it exactly. Nothing to change.**

**⚠ And it confirms a consequence I asserted without proof.** **`FINDINGS-27 §2.1` said the Duelist gives up the two largest melee damage multipliers. Derived: a double-bladed lightsaber is `wield 3`, so it is barred, and `ACTION-ECONOMY-01 §7.4`'s `1.5×` Strength needs a two-handed weapon, which is also barred.**

---

# 2 — ⚠ `Dueling` fails the test the Duelist passed

**`FEATS-LIBRARY-01`:** *"+1 attack and defence when unarmed or wielding a single blaster pistol, melee weapon, or lightsaber."*

**⚠ *A single melee weapon.* A quarterstaff is a single melee weapon. So is a double-bladed sword and a Wookiee Warblade.**

> **The feat that exists to reward fighting with one weapon currently rewards fighting with a two-handed one.**

**Its own description says why that is wrong** — *"the counterpart to Two-Weapon Fighting… a character focused on one weapon fights more efficiently than one splitting attention"* — **and a double-blade is explicitly two weapons under `ACTION-ECONOMY-01 §464`: *"a double-blade is two weapons, not one large one."***

**⚠ So `Dueling` and `Dual Strike` can both apply to the same double-bladed lightsaber, and one of them is written to exclude the other.**

**Recommend restating it as `weaponwield` 1, 2 or 4, or unarmed** — **the same clause `§658` already uses, so no new rule and no new category.**

## 2.1 ⚠ And it narrows an argument of mine

**`FINDINGS-27 §2.1` argued `Single Combat` and `Dueling` are two separate conditions — *"a condition on your hands, and a condition on the field."***

**If `Dueling` is restated to one-handed-only, the two share their wielding condition and differ only on *exactly one enemy in reach*.** **Still two conditions, but closer than I claimed. Recorded rather than defended.**

---

# 3 — What else in `baseitems.2da` touches classes

**`REPLY-38` says `weaponsize`, `damageflags`, `critthreat` and `crithitmult` are unexamined. Two matter to work already drafted:**

**`critthreat` and `crithitmult`.** **⚠ Three class features widen a threat range — the `Commando`'s capstone, the `Gunslinger`'s tier 3 as originally drafted, and `One Shot` before `FINDINGS-40` removed it.** **`ATTACKS-01 §12.1` defines the multiplier against *a weapon's printed threat range*, and that column is now in holdings and unchecked.**

**`weaponsize`.** **`wield 2` spans sizes 2, 3 and 4 — so a Long Sword and a Short Lightsaber are both one-handed and different sizes.** **⚠ Nothing in the class work uses size, but `ATTACKS-05`'s `Dual Strike` distinguishes *"one-handed: two swings"* from *"two-handed: one swing with damage rolled twice"*, and size may be the axis that was intended rather than wield.**

---

# 4 — Standing, unchanged

**`Officer` is the only draftable class left and has no premise. `Vanguard` likewise, scheduled last. `Beast Master` is blocked on the bestiary. `Scoundrel` is second-last by owner order.**

**⚠ The Agent rebuild is `FINDINGS-39 §1` and the eight `P` names are `FINDINGS-39 §3`, pushed before `REPLY-37`. Fifth request for material already on disk.**

---

# The question

> **⚠ `§2` — restate `Dueling` as `weaponwield` 1, 2 or 4? As written it rewards the two-handed weapon it was created to be the opposite of.**
