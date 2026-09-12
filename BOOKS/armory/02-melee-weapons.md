# Chapter Two — Melee Weapons

**Status: RESUBMITTED.** `PT-1747`'s Vibrosword die change applied throughout,
including `Baragwin Assault Blade`, confirmed as `g1_w_vbroswrd01` and fully
recomputed rather than patched. Split from a combined "Melee / Ranged / Lightsabers"
chapter per MAIN's ruling — three chapters, not one, matching `EQUIPMENT-01`'s own
section breaks and this book's identity as a browsable reference rather than a
cover-to-cover read.

Wield classes and how criticals resolve are taught in Chapter One and not restated
here — every weapon below belongs to one of that chapter's six classes.

---

## The base weapons

| Weapon | Damage | Type | Threat | Balanced | Attacks |
|---|---|---|---|---|---|
| **Stun Baton** | **1** | bludgeoning | 20 / ×2 | — | 1 |
| **Short Sword** | **1d6** | piercing | 20 / ×2 | **yes** | 1 |
| **Quarterstaff** | **1d6** | bludgeoning | 20 / ×2 | **yes** | **2** |
| **Gaffi Stick** | **1d8** | piercing | 20 / ×2 | **yes** | **2** |
| **Vibroblade** | **1d10** | piercing | **19–20 / ×2** | **yes** | 1 |
| **Wookiee Warblade** | **1d10** | slashing | 20 / ×2 | **yes** | **2** |
| **Long Sword** | **1d12** | slashing | 20 / ×2 | no | 1 |
| **Gamorrean Battleaxe** | **1d12** | slashing | 20 / ×2 | — | 1 |
| **Vibrosword** | **1d12** | slashing | **19–20 / ×2** | no | 1 |
| **Double-Bladed Sword** | **2d6** | slashing | 20 / ×2 | **yes** | **2** |
| **Vibro Double-Blade** | **2d8** | slashing | 20 / ×2 | **yes** | **2** |

The Attacks column confirms the double-blade ruling — Quarterstaff, Gaffi Stick,
Wookiee Warblade, and both double-bladed types are all marked 2, and every one of them
is also *Balanced*, matching the reduced two-weapon penalty Chapter One's wield classes
already carry for that flag.

And the trade is visible in the threat range: a Vibrosword threatens on 19–20; a
Double-Bladed Sword of identical damage threatens only on 20 — more attacks, less
precise. Balanced weapons take the reduced penalty (rather than the full one) when used
off-hand, per the Player's Handbook's action economy rules.

*(`EQUIPMENT-01 §2`)*

## The progression

Three points on the curve, all Vibroswords, to see how far upgrades move the number.

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibrosword** *(120 credits)* | **1d12** | 19–20 | — |
| **The One's Vibrosword** *(mid)* | **1d12 +5** | 19–20 | **+5** |
| **Bacca's Ceremonial Blade** *(2,480)* | **1d12 +4**, +4 energy, **+2d6 vs droid** | 19–20 | **+4** |
| **Baragwin Assault Blade** *(9,000)* | **1d12 + 2d6 energy + 2d6 sonic** | **17–20** | **+5** |

And the best double weapon:

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibro Double-Blade** *(180)* | **2d8** | 20 | — |
| **Yusanis' Brand** *(8,000)* | **2d8 +2**, +3 fire, **+6–9 ion vs droid** | **19–20** | **+3**, on-hit stun |

Base to best is roughly 6.5 average damage to 20.5, plus an attack bonus of +5 and a
threat range doubled from 10% to 20% — a factor of three on damage across a campaign.

*(`EQUIPMENT-01 §3`, base figure updated for `PT-1747`'s Vibrosword die change (2d6 →
1d12, average 7 → 6.5). The vs-droid bonus is now confirmed rather than assumed:
`data/2da/k1/racialtypes.2da` row 5 is `Droid`, resolving what `ITEMS-01` had flagged as
an unmapped subtype.)*

**The endpoint is now 20.5, recomputed from the real properties rather than adjusted
from the old figure.** `Baragwin Assault Blade` is confirmed as `g1_w_vbroswrd01` — its
Name field turned out to be a string-table reference (`strref 48160`) rather than inline
text, which is why extraction never found a name to grab there in the first place.
Resolved against `dialog.tlk`: *"Baragwin Assault Blade,"* exactly, with a matching
description — a miniaturized vibrosword fitted with discharge capacitors. Both `ITEMS-01`
and `EQUIPMENT-01`'s own citation of it are fixed at the source. **Its base die is
`1d12` too** — the same Vibrosword-family item every other weapon on this page sits on,
missed in the first sweep only because the corrupted row couldn't be found by name.

Recomputing from the confirmed properties (`1d12` base + `2d6` energy + `1d6` sonic
twice) gives **20.5**, not the "24" this chapter carried before — a real correction, not
a small adjustment for the die alone. The original figure never quite reconciled with
the visible properties even before today (they summed to 21 under the old `2d6` base,
not 24), so this isn't purely PT-1747's effect; it's the first time this line has been
checked against the item's actual properties rather than restated from a secondary
source. One reassurance: 20.5 against the base's 6.5 is a ratio of ×3.15 — closer to the
"factor of three" this sentence already claims than either previous figure was.

**⚠ One thing this table doesn't show.** `Bacca's Ceremonial Blade` isn't one item in
`ITEMS-01` — it's four resrefs. The row priced at 2,480 credits is the one shown above.
The other three (cost 0) swap in an `AttackBonus`, `Keen`, and a Use-Limitation gated on
owning `Critical Strike` or `Flurry`, with only the damage die differing between them.
Reads like a unique weapon whose active stat block changes with the wielder's own feat
choices — an unusual mechanic, not an extraction error, and one this chapter isn't the
right place to fully unpack. Worth a look when the Upgrades chapter gets drafted.

---

## Open items, carried from review

Same lightsaber and ranged-damage flags as Chapter One — unaffected by this chapter,
noted for continuity. Bacca's Ceremonial Blade's feat-conditional variants, noted above,
carried forward to the Upgrades chapter as before.

**Closed:** `Baragwin Assault Blade`'s identity, base die, and the chapter's "base to
best" endpoint are all resolved and fixed at the source (`ITEMS-01` and `EQUIPMENT-01`
both corrected). Nothing outstanding from this thread.
