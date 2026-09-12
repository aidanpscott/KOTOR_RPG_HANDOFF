# Chapter Three — Ranged Weapons

**Status: REVISED — drafted against `MAIN_WORK/rules/`, the authoritative sources.**
Wield classes and critical-hit resolution are taught in Chapter One and not restated
here.

**⚠ This chapter's earlier draft was built on a stale copy.** Every correction it
reported has since been absorbed into the live `EQUIPMENT-01`, and the live document
also carries three things that copy never had: `Heavy Blaster`, `Marksman Rifle`, and
`Sniper Rifle`. The table below is the live one.

---

## The base weapons

| Weapon | Damage | Type | Range | Threat |
|---|---|---|---|---|
| **Hold Out Blaster** | **1d4** | energy | 24 m | 19–20 · on-hit stun |
| **Sonic Pistol** | **1d4** | sonic | 16 m | 20 · Dex damage |
| **Disruptor Pistol** | **1d6** | physical | 24 m | **18–20** |
| **Ion Blaster** | **1d6** + 1d10 vs droid | ion | 16 m | 20 · **×3** |
| **Blaster Pistol** | **1d8** | energy | 24 m | 20 |
| **Heavy Blaster** | **1d10** | energy | 24 m | 20 |
| **Disruptor Rifle** | **1d10** | physical | 28 m | **18–20** |
| **Ion Rifle** | **1d10** | ion | 28 m | 20 · **×3** |
| **Sonic Rifle** | **1d10** | sonic | 28 m | 20 · Dex damage |
| **Bowcaster** | **1d10** | energy | 28 m | 19–20 |
| **Marksman Rifle** | **1d10** | energy | **40 m** | 19–20 |
| **Blaster Carbine** | **1d12** | energy | 24 m | 20 · ×2 |
| **Blaster Rifle** | **1d12** | energy | 28 m | 19–20 |
| **Sniper Rifle** | **1d12** | energy | **50 m** | 19–20 |

**All pistols are *Balanced*** — they take the reduced off-hand penalty from Chapter
One's wield classes.

**The name is `Hold Out Blaster`, no hyphen — `PT-1477`.** `STARTING-EQUIPMENT-01`
spells it unhyphenated thirteen times and `ITEMS-01` once; the hyphenated form survived
in one document only. The catalogue sits closest to the source — `g_w_hldoblstr01` is
the game's own resref — so the outlier was the document furthest from where the name
came from.

## The two long rifles — `PT-1783`

**`Marksman Rifle`, 1d10 at 40 metres.** Revised from `1d12`. Blaster Rifle's reach
problem solved the other way round: less damage per shot, considerably more range. It
is not a Blaster Rifle alias — this book already distinguishes four rifles by damage
type, and the Marksman Rifle differs on the columns a marksman actually cares about.

**`Sniper Rifle`, 1d12 at 50 metres.** A separate weapon, not a rename — the longer of
the two by both die and range, and the longest-reaching weapon in the book.

Both are plain. No proficiency gates, no class restrictions, no special ammunition —
the same simple shape `Blaster Rifle` has. What a character does with the extra reach is
the only thing that distinguishes them in play.

### What the perception-extension property actually does — `PT-1782`

Both rifles carry it. It is **passive** (no action to activate, nothing to maintain),
it **matches the weapon's own range** rather than granting some separate fixed bonus,
and it **respects line of sight** — it extends how far you can perceive, not what you
can perceive through.

**The practical consequence is that these rifles' range is real rather than
theoretical.** A weapon that reaches 50 metres is worth nothing if its wielder cannot
detect anything past 30; the shot exists on paper and never on the table. The
perception extension is what closes that gap: a sniper can engage what shorter weapons
cannot reach *because they can see that far in the first place*. Without it, the extra
range would be a number on a sheet that never changed a fight.

## Where the ceiling sits

**A base blaster pistol averages 4.5 damage (`1d8`). A base vibrosword averages 6.5
(`1d12`) and adds Strength.** A Soldier at Strength 16 (+3) swings for 9.5 average with
a weapon costing 120 credits, where a blaster does 4.5 at any Strength.

*This paragraph was held out of the previous draft as stale on two counts. Both are
now fixed at source: the vibrosword figure for `PT-1747`'s die change, and the pistol
figure, which read `3.5` — `1d6`'s average rather than `1d8`'s — and appears to have
gone stale independently, possibly predating `PT-339`. Ranged weapons add Dexterity to
damage under `PT-340`, which the comparison's own framing now accommodates rather than
contradicts.*

**The best pistol in either game** is Cassus Fett's Heavy Pistol — 6–19 damage, +5
attack, 25% chance to stun, on top of rifle-like damage.

---

## ⚠ Sniper Rifle is ruled but not catalogued

**`PT-1783` creates `Sniper Rifle` as a base weapon type, and `EQUIPMENT-01`'s table
carries it. `ITEMS-01` has no row for it** — no resref, no cost, no description. The
only `Sniper Rifle` string in the catalogue is `Sith Sniper Rifle` (`g_w_blstrrfl002`),
a different and pre-existing K1 weapon.

`Marksman Rifle` by contrast does have its row — `a_w_mrksmnrfl01`, authored, Tier 1,
400 credits, with its own description: *"A long barrel, a heavy stock and a scope rail.
It hits softly and it hits from where nobody expected."*

**So the Sniper Rifle currently exists as a ruled type with nothing to buy.** Naming
this rather than inventing around it: a resref and a price are mechanical values and
not mine to assign. The description is mine to write whenever the row is created, and
it should sit in the same register as the Marksman Rifle's — plain, physical, and about
what the weapon does to a fight rather than what it is made of.

---

## Open items, carried from review

The full family-by-family catalogue — 94 pistols and 78 rifles in `ITEMS-01`, organised
Base versus Advanced by tier the way Chapter Two's eleven families are — is the
remaining work on this chapter, and the next increment. The base table, the rulings, and
the two new weapons above are complete and current.

`Hold Out Blaster`'s earlier "could not be confirmed" flag is closed; `PT-1477` explains
both why it existed and why searching for the hyphenated form missed it.
