# Armory — Editorial Notes

**⚠ NOT PART OF THE BOOK. Internal record, for MAIN, Coder and the owner.**

**This file exists because of `PT-1844`**, and mirrors `BOOKS/timeline/EDITORIAL-NOTES.md`.
The chapters used to carry their findings in an *"Open items, carried from review"* section
citing internal documents and ruling numbers a reader cannot look up. **Those sections are
moved here as each chapter is passed — preserved, not deleted.**

---

# Chapter One — Weapon Damage and the Defence Formula

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN**, checked against `EQUIPMENT-01` and
`ACTION-ECONOMY-01` directly. **Sources it stood on:** `EQUIPMENT-01 §1` (melee damage),
`EQUIPMENT-01` with `PT-340` (ranged adds Dexterity), `PT-1` (the provisional lightsaber
line), `PT-341` (the Massive Criticals cap), `PT-339`.

**`ATTACKS-01`'s ranged-damage line is stale against `EQUIPMENT-01`'s own `PT-340`
amendment** — reported at `TO-MAIN-30-AUTHOR.md`, not fixed here. This chapter draws its
ranged-damage value from `EQUIPMENT-01` directly, which already has it right.

**The lightsaber-damage-ability line is provisional in its own source (`PT-1`).** Carried
through as a flag rather than smoothed into a stated fact.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 8 internal citations**, including the whole *Source* column of the damage
table.

**⚠ The damage table's source column could not be handled by the approved rule alone**, and
this is the first Armory exception worth recording. **The rule is "attribute to the game's
own data rather than the internal ruling" — but the four rows are not the same kind of
claim:**

- **Melee one- and two-handed** are straightforward extracted values.
- **Ranged adding Dexterity** is a d20 convention rather than something the games state.
- **The lightsaber line is explicitly provisional** — a reading of an ambiguous source.
- **The Massive Criticals cap is a deliberate departure** from the games, which leave it
  uncapped.

**Blanket-attributing all four to "the game's own data" would have been false for three of
them.** So the column was dropped and **provenance is now stated in prose exactly where it
differs from the games** — which is the `⚠ AUTHORED` discipline the Armory already uses,
turned reader-facing.

**The lightsaber warning is stated more strongly than before, not less.** It now says
plainly that this is **this game's reading of an ambiguous source**, that the source calls
lightsabers *"not melee weapons"* about upgrades and criticals rather than damage, and that
**being wrong is worth roughly ±3 damage on every hit a Jedi lands.**

**The Massive Criticals cap now says outright that it is a departure** — *"one of the few
places where this book knowingly differs from its source rather than reporting it"* — which
the old text conveyed only through a ruling number.

**⚠ And a self-caught over-removal.** My first pass at the armour restrictions dropped the
names **`Soresu`** and **`Well Guarded`**, treating them as internal jargon. **They are not
— they are a lightsaber form and a class feature, both real in-game things a reader can look
up in the Player's Handbook.** The audio rendition of this chapter still named them, which
is how the loss was spotted. **Restored, and the passage is now stronger than either
version:** the restriction decides what kind of defence a character can build.

**✔ The audio rendition needed no pass.** `01-weapon-damage-and-defence-formula-audio.md`
was written as continuous prose for a text-to-speech reader and **carries zero internal
citations already** — checked, not assumed. It remains substantively consistent with the
revised chapter.

**⚠ Deliberately NOT loosened.** Every value survives: the three damage formulas, the six
wield classes and their pairing rules, threat ranges and multipliers, the `2d6` cap, the
sum-of-9 armour rule with both organic exceptions, the uncapped-robe rule and the Jedi
Defence-12 example, and both droid plating tables with K2's uncapped sentinel.

---

# Chapter Two — Melee Weapons

*`PT-1844` pass. This chapter had no "Open items" section of the usual shape; what it
carried instead was a work-tracking section on an incomplete sweep, reproduced here.*

**Chapter status: DRAFT, full-catalogue standard applied.** Eleven families, 62 entries.
**Scope rule:** `PT-342`'s K1-overrides-on-shared-items applied where a genuine difference
appears.

## ⚠ Four weapons still carrying the pre-`PT-1747` Vibrosword die

`PT-1747` moved Vibrosword from `2d6` to `1d12`. The sweep covered the nine
`vbroswrd`-stemmed resrefs. **Four more melee weapons still read `2d6, 19–20 ×2` — the
exact pre-ruling Vibrosword signature — and none of them carry that stem, which is why a
stem-matched sweep would pass over them:**

| Weapon | Resref | Confidence |
|---|---|---|
| **Vibrosword** (K2's own) | `w_melee_06` | **Certain** — same weapon, same name, same 120-credit price as K1's |
| **Echani Vibrosword** | `w_melee_21` | **Certain** — names the family |
| **Sith Tremor Sword** (K2's) | `w_melee_22` | **Certain** — direct counterpart of K1's `g_w_vbroswrd03` |
| **GenoHaradan Poison Blade** | `geno_blade` | **⚠ Suspected only** — die and threat match exactly, but the name doesn't say Vibrosword and `BaseItem` could not be read from this copy |

**⚠ UPDATE — three of these four are now fixed at source.** `w_melee_06`, `w_melee_21` and
`w_melee_22` all read `1d12` in the live `ITEMS-01`. **`GenoHaradan Poison Blade` was not
changed and still reads `2d6`** — so either it genuinely isn't a Vibrosword-family weapon,
or it is a fifth miss. **Settling it needs a `BaseItem` read rather than a die-signature
match.**

**Two resref-versus-base-type disagreements worth noting for whoever runs that check:**
`Raito's Gaderffii` sits at `g_w_qtrstaff03` while carrying the Gaffi Stick's `1d8` die,
and `Baragwin Assault Blade` sits at `g1_w_vbroswrd01` with a `g1_` prefix no other weapon
in the family uses. **Resref stem is not a reliable proxy for base weapon type in either
direction** — the same lesson the `Energy Baton` resolution taught from the opposite side.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 5 internal citations**, and one whole section.

**⚠ The proper-noun check was run deliberately this time, and it changed the outcome.**
Following the `Soresu` lesson from Chapter One, every code-formatted term was checked
rather than pattern-matched. **The resrefs stayed** — all 92 of them. **They are the games'
own item identifiers, not internal project references, and a reader can look them up in the
game files.** Stripping them would have destroyed the catalogue's usefulness.

**The Vibrosword sweep section moved here in full.** It was work-tracking — a ruling
number, a sweep's coverage, confidence ratings and what has since been fixed at source.
**None of it is reader content.**

**⚠ But it left a real residue, and that stayed in the chapter.** The `GenoHaradan Poison
Blade`'s die is genuinely unsettled, and a reader using that weapon needs to know. **The
note is now self-contained rather than pointing at a section that no longer exists:** it
reads `2d6` where its family reads `1d12`, it may belong to a different family than its
damage suggests, **and a Gamemaster is told to treat `1d12` as the working value with `2d6`
as a defensible reading.** That is more useful than the cross-reference was.

**⚠ And a dangling reference caught mid-pass.** Removing the sweep section orphaned the
GenoHaradan entry's *"see the note at the top of this chapter"* — **the same failure mode
caught in the Timeline's Chapter Three.** Found by re-reading the entry after the removal
rather than by trusting the edit.

**The tail section became a caution on item codes**, which is the reader-facing half of the
resref finding: **the code is the games' own identifier and is not a reliable guide to what
kind of weapon something is. Read the family heading, not the code.**

**⚠ Deliberately NOT loosened.** All 11 families, all 62 entries, every die, threat range,
price and property line survives. **The K1-over-K2 rule is stated in reader terms rather
than by ruling number, and the one place a genuine divergence is called out — the Sith
Tremor Sword's sonic value — still names both figures.**
