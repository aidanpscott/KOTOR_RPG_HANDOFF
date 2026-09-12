# Chapter Five — Armour

**Status: APPROVED.** The defence formula, the sum-of-nine rule, robes, and
droid plating are all taught in full in Chapter One and not restated here — this
chapter is the item catalogue, the same relationship Chapter Two's melee weapons had
to Chapter One's damage formula.

**⚠ A different kind of source than the last three chapters.** `ITEMS-02` isn't a
secondary-sourced summary table the way `EQUIPMENT-01`'s weapon tables were — it's
already the primary-source catalogue, converted from the actual game files under the
same seven rulings cited throughout this book (`PT-339` dice, `PT-341` Massive
Criticals, `PT-308` tiers, `PT-327` unique, `PT-345` crystals, `PT-349` Upgradeable,
`PT-384` the feat remap). It doesn't need the same cross-check against a more primary
source that caught real errors in Chapters Two through Four — it largely *is* that
source.

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

**One priced pair worth knowing about, because it's an owner ruling rather than an
oversight:** the Dark Padawan Robe was priced down from 900 to 700 credits (`PT-980`)
specifically because it is *mechanically identical* to the standard Jedi Robe — same
`Armor 1`, same Force Point regeneration, same restriction. Same effect, same price,
by ruling.

**`DecreaseAC` is a real penalty against a base value that exists elsewhere, resolved
rather than guessed at.** The property's subtype (2) resolves against
`iprp_acmodtype.2da` to `AC_Armor` specifically — not some narrower vs-melee or
vs-ranged distinction. `Light Combat Suit`'s own `BaseItem` reference points to
`baseitems.2da`'s `Armor_Class_4` row (`baseac` 4, `dexbonus` 5) — an ordinary Light
entry under Chapter One's sum-of-nine rule. So this item's true net protection is **+3
armour**, not the category's usual +4, while keeping the full +5 Dexterity cap:
genuinely below-average gear, not a display quirk or a separate mechanic.

**The same two-step path resolves any other `DecreaseAC`/`IncreaseAC` entry in the
catalogue:** `iprp_acmodtype.2da` for which AC component the property touches, and the
item's own `BaseItem` reference into `baseitems.2da` for the number being modified.

---

## Open items, carried from review

Same lightsaber-damage flag, unaffected by this chapter. `DecreaseAC` closed above —
confirmed, not a real gap. Still worth stating plainly: this chapter samples five of
173 items rather than auditing the full catalogue line by line, the way
the eleven-row weapon tables in Chapters Two through Four could be. A category count
and a representative sample is the right grain for a browsable-reference chapter; a
full 173-item transcription would belong to `ITEMS-02` itself, not to prose built on
top of it.
