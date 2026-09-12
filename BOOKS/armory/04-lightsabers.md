# Chapter Four — Lightsabers

**Status: DRAFT, for review.** Split from the combined "Melee / Ranged / Lightsabers"
chapter per MAIN's ruling. Wield classes and critical-hit resolution are taught in
Chapter One and not restated here — the Short Lightsaber is class 2, the standard
Lightsaber is also class 2, the Double-Bladed Lightsaber is class 3.

**⚠ This chapter's base table is checked against the raw `.2da` files directly
(`data/k1_baseitems.2da`, `data/k2_baseitems.2da`), not `ITEMS-01`'s markdown copy —
that copy's merged "K2+K1" tag turns out to mask the two games' real, different
values for these three weapons. Detail below.**

---

## The base weapons, by game

| Weapon | K1 | K2 | Threat | Wield | Size |
|---|---|---|---|---|---|
| **Short Lightsaber** | **2d6** | 2d8 | 19–20 / ×2 | 2 — one-handed | Small |
| **Lightsaber** | **2d8** | 2d10 | 19–20 / ×2 | 2 — one-handed | Medium |
| **Double-Bladed Lightsaber** | **2d10** | 2d12 | 20 only / ×2 | 3 — two-handed staff | Large |
| **Training Lightsaber** | **1d8** | — | see below | — | — |

**The Training Lightsaber is a fourth entry, authored rather than extracted** — 150
credits, `a_w_trnsbr01`, and it takes a colour crystal like any other lightsaber
(`PT-1472`), the crystal supplying properties while the base supplies the die. Giving a
padawan's practice weapon a master's dice would have been a ruling in itself, and `1d8`
is that ruling going the other way: a step below the Short Sword's cousin and well
below the real thing. **It is what you learn on.** Two siblings exist — Training Short
Lightsaber at `1d6` and Training Double-Bladed at `1d10`.

**⚠ Two live documents disagree on its threat range, and this chapter does not pick.**
`EQUIPMENT-01` states threat `19–20`. `ITEMS-01` gives `20` — and gives `20` for all
three training sabers, which makes its side internally consistent where `EQUIPMENT-01`
states the figure once in prose. Flagged rather than resolved; the consistency argues
for `20` but that is an argument, not a reading of the source of record.

**Use K1's — our campaign is 3956 BBY and K1 is the era**, same standing choice as every
other weapon in this book.

**⚠ The standard `Lightsaber`'s K1 die is corrected here from `EQUIPMENT-01 §4b`'s
stated `2d10` to the confirmed `2d8`.** Checked directly against `data/k1_baseitems.2da`,
row 8, label `Lightsaber`: `numdice` 2, `dietoroll` 8 — not 10. K2's row 8 in
`k2_baseitems.2da` confirms `2d10`, matching `EQUIPMENT-01`'s stated K2 value exactly —
only the K1 figure was wrong.

**Why this matters beyond one number:** the corrected K1 progression — Short `2d6`,
standard `2d8`, Double-Bladed `2d10` — rises by exactly one die step at each tier. The
stated progression (`2d6`, `2d10`, `2d10`) skips a step between Short and standard, and
then gives the two-handed Double-Bladed saber the *same* die as the one-handed
standard — an odd result for a weapon whose whole tradeoff is meant to be more damage
at the cost of precision. The corrected values resolve that oddity as a side effect of
just being right.

**⚠ A methodological note worth passing on, not specific to lightsabers.** `ITEMS-01`'s
markdown copy tags all three lightsaber resrefs `K2+K1` and shows only K2's numbers
under that combined tag (`2d8`/`2d10`/`2d12` — the Short Lightsaber row I checked in
Chapter One's own research showed this same pattern). **A `K2+K1` tag in that catalogue
does not mean the two games share a value — it can mean the extraction recorded only
one game's number for a resref present in both.** Confirmed for lightsabers by checking
the raw `.2da` directly; not confirmed or ruled out for anything else tagged the same
way. Worth knowing before trusting a `K2+K1` tag at face value elsewhere in the item
catalogue.

*(`EQUIPMENT-01 §4b`, K1 standard-Lightsaber die corrected against `data/k1_baseitems.2da`
directly.)*

## What this chapter is holding back

**`EQUIPMENT-01 §4b`'s rationale for choosing K1's dice over K2's has two parts, and
only one still stands.** *"Our campaign is 3956 BBY and K1 is the era"* — unaffected by
anything, kept above as the chapter's stated reason. The second part — *"a Vibrosword is
2d6, so a K1 lightsaber sits exactly one die step above it"* — is stale on two counts
now: Vibrosword is `1d12` since `PT-1747`, not `2d6`, and even before that change the
comparison was against the *stated* (wrong) standard-Lightsaber die of `2d10`, which
was never one step above `2d6` in the first place — that's two dice steps. Not rewriting
this sentence unilaterally; the era-based reason already carries the choice on its own,
and what (if anything) should replace the Vibrosword comparison is an editorial call,
same shape as Chapter Three's "note the ceiling" paragraph.

**Crystals are `PT-345`'s subsystem — a lightsaber's other properties come from the
crystal fitted to it, not from the weapon itself.** `ITEMS-03` catalogues 104 of them,
from Rubat (+1 damage, +1 attack, 1,000 credits) up through rarer stones with larger,
mixed bonuses. That's Upgrades-chapter scale, same reasoning as Bacca's Ceremonial
Blade's variants and Cassus Fett's Heavy Pistol in the last two chapters — not
catalogued here, only named as the reason this weapon category needs its own chapter
in the first place.

---

## Open items, carried from review

The lightsaber-damage-ability flag from Chapters One through Three — genuinely this
chapter's own subject now, not just carried for continuity. `EQUIPMENT-01 §4b` itself
raises the same caveat independently: *"lightsabers are not melee weapons,"* a
statement the source makes about upgrades and criticals rather than damage, which is
exactly why treating lightsabers as melee-for-damage is a working assumption rather
than a confirmed rule. Two independent paths to the same open question, not two
separate ones.

New this chapter: the K1/K2 rationale paragraph (editorial), and the `K2+K1` tagging
caution above, which isn't this chapter's to resolve but felt worth surfacing where it
was found.
