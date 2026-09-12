# Chapter Seven — Droid Equipment

**Status: APPROVED.** Split out from a combined outline row that bundled
droid equipment with worn gear, usable items, and quest/miscellaneous items — five
`ITEMS` files that aren't one coherent category the way Armour's six sub-categories
were. Proposed as four chapters instead of one; see the note at the end.

`ITEMS-04`, another primary-source catalogue on the same footing as `ITEMS-02` and
`ITEMS-03` — no cross-check against a more-primary source needed here, unlike
Chapters Two through Four.

---

## The eight categories

135 items, three appearing in both games.

| Category | Count | What it is |
|---|---|---|
| **Device** | 29 | Charge-limited combat items — stun, slow, flame, poison, ion effects, each consumed on use |
| **Interface** | 15 | Skill bonuses for computer-terminal interaction |
| **Named** | 10 | Unique droid-specific items, the equivalent of the unique weapons named throughout this book |
| **Plating** | 25 | Droid armour — the item-level equivalent of Chapter One's droid-plating formula |
| **Sensor** | 12 | Detection bonuses, including against Stealth |
| **Shield** | 13 | Timed energy absorption — a duration and a damage cap, not a passive bonus |
| **Spike-mount** | 7 | Computer and security bypass modules — see below |
| **Tool** | 18 | Combat-utility bonuses (the sample entry adds an attack bonus alongside a skill bonus) |

**Every device-category item, and most plating, carries a `Use Limitation Feat (Droid
Upgrade N)` property — the "bay gate" `FEATS-LIBRARY-01` already names as the
deliberate exception to how a feat normally reaches a character.** A droid doesn't
learn these the way an organic character learns a feat; the gate is the item
requirement itself, not a separate feat purchase.

## Representative entries — devices

| Name | Cost | Effect |
|---|---|---|
| **Droid Neural Pacifier** | 100 | Stun, DC 15 to negate, one charge |
| **Droid Repulsor** | 200 | Slow, DC 15 to negate |
| **Droid Flame Thrower** | 300 | 30 heat damage plus Horror, DC 15 for half |
| **Droid Neural Scrambler** | 500 | Same stun as the Pacifier, DC 20 instead of 15 — the same effect gated behind a harder save at a higher price |
| **Droid Ion Striker** | 850 | 20 ion damage, no save mentioned |

## Representative entries — plating

| Name | Cost | Grants |
|---|---|---|
| Droid Impact Armor Mark I | 80 | No armour property yet — Mark I is a "dust cover," in its own flavour text |
| Droid Modular Plating Mark I | 130 | Same tier, different tradeoff — discretion over defence, per its own text |
| Droid Impact Armor Mark II | 400 | `Armor 1` |
| **Droid Desh Plating** | 770 | `Ability (Dexterity) 1` and a `DecreaseAC` penalty of −3 — the same real-penalty-against-a-base-value pattern Chapter Five resolved for organic armour, not re-derived here |
| Droid Impact Armor Mark III | 1,250 | `Armor 3` |

---

## A scoping proposal, not yet decided

**The outline currently bundles `ITEMS-04` through `08` — droid equipment, worn gear,
usable items, and quest/miscellaneous items — into one chapter.** Having looked at all
five, they aren't one category the way Armour's sub-categories were:

- **Droid equipment** (this chapter) — its own coherent, thematically distinct set.
- **Worn gear** (`ITEMS-05`, 241 items — belts, forearms, gauntlets, implants, masks) —
  the single largest catalogue after weapons, and mechanically its own thing: passive
  body-slot gear, not weapons or armour.
- **Usable items** (`ITEMS-06`, 58 — adrenals, medical, trap kits) — active consumables,
  a different kind of object entirely from anything worn or equipped.
- **Quest and miscellaneous items** (`ITEMS-07` + `ITEMS-08`, roughly 60 combined) —
  both small enough to share one chapter, and both are genuinely miscellaneous rather
  than a coherent category in their own right.

**Proposing four chapters rather than one**, same reasoning as the Melee/Ranged/
Lightsabers split — different mechanical shapes, and a single chapter covering all
five `ITEMS` files' combined ~500 items would strain this book's own browsable-
reference identity. Not drafting the other three until this is confirmed.

---

## Open items, carried from review

Same lightsaber-damage flag, unaffected. The four-way split proposal above was
approved and the other three chapters are drafted.

**The `spike-mount` corrupted-Name row is resolved.** It is `Advanced Droid Interface`
(`g1_i_drdcomspk01`, Tier 3, 9,000 credits), gated behind `Droid Upgrade 3` and granting
skill 7 in Awareness, Computer Use, Demolitions and Security — *"a self-contained
artificial intelligence system... to provide them with additional resources useful in
the bypassing of computer and conventional"* security. The four skill bonuses, which had
also been showing as unmapped subtypes, resolve cleanly and match the item's own flavour
text. Third instance of that corruption pattern, and the third to resolve the same
way — by reading the raw file rather than the markdown copy.
