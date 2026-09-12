# Chapter Five — Armour

**The defence formula, the sum-of-nine rule, robes and droid plating are all taught in
Chapter One and not restated here.** This chapter is the catalogue — the same relationship
Chapter Two has to Chapter One's damage rules.

**⚠ One difference worth knowing, because it affects how much to trust these numbers.** The
armour figures in this chapter were converted straight from the games' own item files.
**They did not pass through a summary first**, which is where the errors corrected in
Chapters Two, Three and Four came from.

---

## The six categories

173 items in total, nine of them appearing in both games.

| Category | Count | What it is |
|---|---|---|
| **Clothing** | 16 | No armour bonus by default; civilian and party-member wear, some unique (Atton's jacket, Mira's mesh jacket) that quietly matches light-armour protection despite the slot |
| **Disguise** | 2 | Not combat gear at all — grants a `Disguise` property and little else, worn to pass as something you aren't rather than to take a hit |
| **Light** | 37 | The Light armour class from Chapter One's table — armour bonus 4–5, high Dexterity cap |
| **Medium** | 41 | Mid-range of Chapter One's table |
| **Heavy** | 34 | The low-Dexterity-cap end of Chapter One's table |
| **Robes** | 42 | Uncapped Dexterity, per Chapter One's own exception — the largest single category, reflecting how central Force users are to this game's item design |

## Representative entries

| Name | Category | Cost | Note |
|---|---|---|---|
| **Light Combat Suit** | Light | 50 | Cheapest armour in the game |
| **Heavy Combat Suit** | Light | 100 | Same category, better protection, same Dexterity treatment |
| **Padawan Robe** | Robes | 50 | `Armor 1` — the entry-level robe every Jedi pregen starts closest to |
| **Atton's Ribbed Jacket** ⚠ unique | Clothing | 0 (found, not bought) | `Armor 4` — matches Light armour's protection from a Clothing slot |
| **Sith Armor** ⚠ unique | Disguise | 0 (found, not bought) | `Armor 2` plus a disguise property — one of only two items in this category |

**⚠ One price in this chapter is deliberately not the games' own.** The **Dark Padawan
Robe** was priced down from 900 credits to **700**, because it is *mechanically identical*
to the standard Jedi Robe — same `Armor 1`, same Force Point regeneration, same
restriction. **Two items that do exactly the same thing now cost the same.** That is a
change this game made on purpose, not an error in the source.

**⚠ Some armour carries a `DecreaseAC` property, and it means exactly what it says.** It is
a real penalty, not a display quirk.

**Worked example — the `Light Combat Suit`.** Its base row in the games' own armour table
gives armour 4 and a Dexterity cap of +5, an ordinary Light entry under Chapter One's
sum-of-nine rule. Its `DecreaseAC` property then reduces the armour component
specifically — **not some narrower penalty against melee or ranged attacks.**

**So its true protection is `+3` armour, not the `+4` its category suggests**, while
keeping the full `+5` Dexterity cap. **Genuinely below-average gear, cheaply priced to
match.**

**Any other `DecreaseAC` or `IncreaseAC` entry resolves the same way:** find which part of
Defence the property touches, then find the base value it is modifying in the item's own
armour row.

---
