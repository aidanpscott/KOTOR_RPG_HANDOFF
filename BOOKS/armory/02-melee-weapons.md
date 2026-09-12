# Chapter Two — Melee Weapons

**Status: REVISION IN PROGRESS — format validation, part one of N.** New standing rule
from the owner, retroactive: every item chapter carries the full catalogue, not a
representative sample — organized within each category by Base versus Advanced items,
and by tier. Applies to this chapter and five others (Ranged Weapons, Armour, Droid
Equipment, Worn Gear, Usable Items); Quest and Miscellaneous Items gets it for its
`ITEMS-08` half only, per explicit exception — quest items and datapads stay conceptual
rather than catalogued.

**Scope confirmed before writing at this scale, since guessing wrong here multiplies
across hundreds of entries:**

- **Both games, full combined catalogue, K1 taking precedence where a shared item
  genuinely differs — `PT-342`.** 165 resrefs are shared between K1 and K2 across the
  item corpus; 162 are byte-identical, and the K1-overrides rule exists for the rare
  case a real difference shows up. `PT-342` also names three cases that looked like
  conflicts and weren't: a K2 rename collapsing two K1 items into one, and a displayed
  field masking a `BaseItem` index difference rather than a real divergence. Checking
  before declaring a conflict, not just importing one, applies here the same way.
- **No nameless placeholder rows, and no creature/innate-weapon entries** — NPC preset
  gear (`propvs01` and its siblings) and a beast's natural attacks are engine assets,
  not items a character finds or buys, and get no catalogue entries.

## ⚠ A structural question this surfaced, not yet resolved

**Organizing K1's melee weapons by family is straightforward — every K1 resref groups
cleanly by stem** (`g_w_vbroswrd0N` are all Vibroswords, `g_w_stunbaton0N` are all Stun
Batons, and so on), **matching the eleven base weapon types Chapter One's wield-class
table already established.** K2's items don't carry that grouping — they're numbered
sequentially (`w_melee_01` through `w_melee_30`) with no stem to sort by, so matching
them to a family means checking each one's actual base weapon column against Chapter
One's eleven types.

**Most match cleanly.** A few don't. `Energy Baton` (`w_melee_03`) shows `1d4` damage
plus a secondary `1d3` piercing property; `Exchange Negotiator` (`w_melee_08`) shows
`1d6` plus a secondary `1d6` piercing property. Neither die matches Stun Baton's `1`
flat damage, despite both sharing a stun-on-hit theme with that family in their flavour
text. **This may mean K2 introduces base weapon types beyond the eleven Chapter One
already catalogued** — which would mean Chapter One's own wield-class table needs a
K2-specific addendum, not just this chapter's family groupings. Not resolved here;
flagging before assigning a dozen more ambiguous K2 items to families on a guess.

---

## Vibrosword — the format, validated on one complete family

Chosen because it's the family with the most existing research behind it — Chapter
One's wield-class table, and the Bacca's Ceremonial Blade identity/base-die/upgrade
findings from Chapters Two, Four, and Six. Sending this one family for a format check
before writing the other ten.

### Base

| **Vibrosword** | `g_w_vbroswrd01` · K1 · Tier 1 · 120 credits |
|---|---|
| **Damage** | 2d6, slashing, threat 19–20 ×2 |
| **Properties** | None |
| **Description** | *"Ultrasonic generators power this Echani-developed weapon design. A rare cortosis weave that protects against sparring damage ensures that traditional swordplay will endure in the time of lightsabers."* |

K2 carries the identical item as `w_melee_06`, same cost, same properties, same
description with one word changed (*"A cortosis weave"* rather than *"A rare cortosis
weave"*) — one of `PT-342`'s 162 byte-identical shared resrefs.

### Advanced

| **Krath Dire Sword** | `g_w_vbroswrd02` · K1 · Tier 1 · 250 credits |
|---|---|
| **Damage** | 2d6, slashing, threat 19–20 ×2 |
| **Properties** | Enhancement 1 |
| **Description** | *"This was a weapon of distinction in the time of the Krath. Protected against lightsaber sparring damage, Sith would grant these cortosis-laced blades to only the most loyal underlings."* |

| **Sith Tremor Sword** | `g_w_vbroswrd03` · K1 · Tier 2 · 980 credits |
|---|---|
| **Damage** | 2d6, slashing, threat 19–20 ×2, +2 sonic |
| **Properties** | Damage (Sonic) 2 · Enhancement 2 |
| **Description** | *"Traced to the Bladeborn, a Sith offshoot dedicated to sword mastery, these cortosis-laced weapons were given to 'masterblades' who survived no less than ten lightsaber-wielding warriors in combat."* |

K2's `w_melee_22` carries the same name and description with Sonic damage raised to 3
rather than 2 — a genuine K1/K2 difference on a shared name. `PT-342`'s rule applies:
K1's version (Sonic 2) is what this book uses, though both exist and neither is a
transcription error.

| **Echani Foil** | `g_w_vbroswrd04` · K1 · Tier 2 · 1,750 credits |
|---|---|
| **Damage** | 2d6, slashing, threat 19–20 ×2 |
| **Properties** | Enhancement 3 · Keen |
| **Description** | *"These swords were crafted to honor Raskta Fenni, the best Echani duelist of her time. Many were sold, but imperfections in the difficult lightsaber-deflecting cortosis weave caused few to survive."* |

| **Bacca's Ceremonial Blade** ⚠ unique | `g_w_vbroswrd05` · K1 · Tier 2 · 2,480 credits |
|---|---|
| **Damage** | 2d6, slashing, threat 19–20 ×2, +4 energy, Massive Criticals 2d6 |
| **Properties** | Damage (Energy) 4 · Damage (Racial: Droid) 2d6 · Enhancement 2 (×2) · Massive Criticals 2d6 |
| **Description** | *"The great Bacca was hunting the Shadowlands ages ago when an alien ship crashed through the forest. He saw that first contact as a warning of the destruction outsiders could bring. Made from the debris..."* |

**This is the purchasable form.** Three more resrefs share this name and this weapon's
identity but aren't separately purchasable (cost 0) — `g_w_vbroswrd06/07/08` swap in an
`AttackBonus` and `Keen`, gated behind owning `Critical Strike` or `Flurry`, with only
the damage die differing between the three (1d6, 1d8, 2d6 energy respectively). Resolved
in Chapter Six as a fixed-property pattern, not an upgrade-tree mechanic — the same
shape as `Keen` and `Massive Criticals` baked into a resref rather than installed. Not
re-catalogued as three more separate entries; noted here where the base form lives.

**No K2 equivalent** — `Bacca's Ceremonial Blade` is K1-exclusive.

---

## Open items, carried from review

Same lightsaber-damage flag, unaffected. The K2 base-weapon-type structural question
above is new and blocks assigning the rest of K2's melee catalogue to families with
confidence. Vibrosword is the only complete family in this revision — sending now for
a format check before writing Short Sword, Long Sword, Stun Baton, Quarterstaff, Gaffi
Stick, Vibroblade, Wookiee Warblade, Gamorrean Battleaxe, Double-Bladed Sword, and Vibro
Double-Blade, plus whatever K2-exclusive families the structural question above turns
up.
