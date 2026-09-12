# Chapter One — Weapon Damage and the Defence Formula

**Status: APPROVED.** Checked against `EQUIPMENT-01` and `ACTION-ECONOMY-01` by MAIN
directly, confirmed accurate. First chapter committed under the incremental,
one-at-a-time outline process.

---

Attack rolls are taught in full in the Player's Handbook (Attacks, §12.5) — melee and
lightsaber use Strength, ranged uses Dexterity. This chapter doesn't re-teach that roll.
It gives what a weapon's own stat line contributes once that roll is made.

## Damage, by category

| Category | Formula | Source |
|---|---|---|
| Melee, one-handed | weapon dice + Strength | `EQUIPMENT-01 §1` |
| Melee, two-handed | weapon dice + 1.5× Strength | `EQUIPMENT-01 §1` |
| Ranged | weapon dice + Dexterity | `EQUIPMENT-01`, `PT-340` |
| Lightsaber | weapon dice + Strength | `PT-1` — **⚠ provisional** |

**Lightsaber note:** the source calls lightsabers "not melee weapons." Treated as
melee-for-damage as a working assumption, flagged as worth ±3 a hit on every Jedi if
that assumption turns out wrong.

## Wield classes

Every weapon is one of six classes, which sets what may be paired.

| Class | Weapons | Pairs? |
|---|---|---|
| 1 — one-handed light | Stun Baton | yes |
| 2 — one-handed | Long Sword, Vibrosword, Short Sword, Vibroblade, Lightsaber, Short Lightsaber | yes |
| 3 — two-handed staff | Quarterstaff, Gaffi Stick, Wookiee Warblade, Double-Bladed Sword, Vibro Double-Blade, Double-Bladed Lightsaber | no — it *is* the pair |
| 4 — pistol | Blaster, Heavy Blaster, Hold-Out, Ion Blaster, Disruptor Pistol, Sonic Pistol | yes |
| 5 — rifle | Ion Rifle, Bowcaster, Carbine, Disruptor Rifle, Sonic Rifle, Blaster Rifle | no |
| 6 — heavy | Repeating Blaster, Heavy Repeating Blaster | no |

## Critical hits

A weapon's *threat range* (e.g. 19–20) is the roll that scores a critical. Its
*multiplier* (×2, ×3) applies to the dice, not to ability bonuses. Massive Criticals —
bonus damage on top of the multiplier — are capped at `2d6` regardless of the source
game's uncapped value (`PT-341`).

## Defence

> `10 + armour bonus + Dexterity modifier`, and the Dexterity contribution is capped by
> the armour worn.

For organic armour, one rule generates the whole table: **armour bonus + max Dexterity
bonus always sums to 9.**

| Armour class | Bonus | Max Dex | Type |
|---|---|---|---|
| 4 | +4 | +5 | Light (leather) |
| 5 | +5 | +4 | Light (leather) |
| 6 | +6 | +3 | Medium/Heavy |
| 7 | +7 | +2 | Medium/Heavy |
| 8 | +8 | +1 | Medium/Heavy |
| 9 | +9 | +0 | Medium/Heavy |

Two organic exceptions exist, both from the source game: the Armoured Flight Suit
follows the rule (+5/+4); the Zeison Sha does not (+3/+4, summing to 7).

**Robes are the exception that matters.** A robe's Dexterity contribution is *uncapped*.
A Jedi in a Master Robe (+3) at Dexterity 28 (+9) reaches Defence 12 — higher than any
suit of armour produces, at the cost of every point of armour it isn't wearing. This is
why Jedi wear robes.

**Droid plating** is a separate item class and never followed the sum-of-9 rule:

| Plating | K1 | K2 |
|---|---|---|
| Light | +3 / +6 | +3 / uncapped |
| Medium | +4 / +3 | +4 / uncapped |
| Heavy | +9 / +1 | +9 / +1 |

K2's Light and Medium plating use the game's own sentinel for "no cap" rather than a
small positive number — that's why they read as uncapped rather than +6 or +3 in that
column.

**Two restrictions carry over from the source and are not otherwise stated:** armour is
unusable by droids (they wear plating instead) and by Wookiees. And armour blocks Force
powers — already load-bearing elsewhere (the Heavy-Armour/Soresu gate on `Well
Guarded`), confirmed rather than assumed here.

---

## Open items, carried from review

**`ATTACKS-01`'s ranged-damage line is stale against `EQUIPMENT-01`'s own `PT-340`
amendment** — reported at `TO-MAIN-30-AUTHOR.md`, not fixed here. This chapter draws its
ranged-damage value from `EQUIPMENT-01` directly, which already has it right.

**The lightsaber-damage-ability line is provisional in its own source (`PT-1`).** Carried
through as a flag rather than smoothed into a stated fact.
