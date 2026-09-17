# TEST 098 — ALL THREE LAND. Restricted armour refuses the Force, and it
# refuses FIRST: the same empty room gives *"not in that armour"* to a
# restricted caster and *"nothing here you can see to aim it at"* to a
# permitted one. Force Root prints `-6 defence · -6 reflex` and **no attack
# row**, on a target already carrying Mire's `-4 attack` — replace, not extend.
# The disease tree takes 7, 4 and 12 points off strength, dexterity and
# constitution, says *"— until rested"* itself, and had knocked the target's
# Defence to `needed -2` several rounds later.
# ⚠⚠ AND A MADE FORTITUDE SAVE STOPS IT DEAD: `d20 20 = 47 vs 17 · resists`,
# no points taken. PT-2259 holds in play.
# ⚠ YOUR MID-RUN CORRECTION CAUGHT A REAL GAP IN MY BED — my first Zeison test
# used the bare base type and never touched the catalogue collision at all.
# Redone with Jal Shey Mentor Armor, which is the case that matters.

## Build state

    KOTOR-RPG-APP   43b2808  PT-2259 — built and measured from this
    lodestar        57cd3ba  — HEAD's own pin, and the pub-cache checkout
    lens            32b77e3

    ✓ FRESH — built from exactly this source at 09-17 13:49:14

All three trees were clean at the start and the lock matched Lodestar's HEAD.
By the end you had moved on (`attack.dart`, `play_screen.dart` dirty, Lodestar
at `d00b18c`); nothing below is from that. `check_shelf.py` green at both ends.

⚠ **My package reports "3 problems" and they are all mine and all benign** —
`a02-pair` and `a03-line` have no way in, `a01-empty` no way out. I reach each
area by rewriting `[entry]`, which is what that looks like from the validator's
side. **No character or item faults**, which is the part that would matter.

**And TEST 097's finding is closed** — `375a407 Load Game does not run off the
bottom of its own box`. The dialog boxed correctly all session.

---

# 1 · WEARING A RESTRICTED ARMOUR BLOCKS THE FORCE

⚠ **Stated the way you corrected me to state it**: the gate keys on the
authored `restricts_force` column, not on `armortype`. On today's data the two
agree everywhere, so an armortype-shaped test would have passed and the
sentence would still have been wrong. Seven bodies, one variable, same room,
same power:

| body worn | base type | `restricts_force` | result |
|---|---|---|---|
| Heavy Plate | `armour-class-8` | **yes** | **REFUSED** |
| Medium Mesh | `armour-class-6` | **yes** | **REFUSED** |
| Light Suit | `armour-class-4` | no | permitted |
| Jedi Robe | `robe-1` | *absent* | permitted |
| Zeison Sha | `zeison-sha` | no | permitted |
| **Jal Shey Mentor Armor** | `zeison-sha` | no | **permitted** |
| Clothing | `clothing` | *absent* | permitted |

Refused reads:

    not in that armour — Force Slow needs a hand you can move and a mind you
    can hear yourself think in · nothing spent

and permitted reads:

    Force Slow — there is nothing here you can see to aim it at

⚠ **Absence permits**, confirmed on two rows rather than argued: the robe and
the clothing carry no column at all and both cast.

## The refusal comes first, and the empty room is what proves it

Both sentences above are from **the same empty area**, cast with the same
enemy-aimed power. A permitted caster there gets as far as the target check and
is told there is nothing to aim at; a restricted one never reaches it. That is
the only bed where the two orderings differ, and they differ.

## ⚠ The exemption test I first ran was the wrong one

My original Zeison case authored `base = "zeison-sha"` with **no catalogue id**,
so it never exercised the collision `PT-2254`'s own comment is about. Redone
against **Jal Shey Mentor Armor** — `catalogue = "a_robe_20"`, whose catalogue
row says `category = "medium"` while its base type says `grade = light,
restricts_force = "no"` — and it **casts normally**. So the gate reads the base
type and not the item, which is the half that would have inverted, and the item
is not named "Zeison Sha" either, so a name-shaped gate would also have failed
it. Counted in the shelf: exactly **six** body items sit on `zeison-sha` with
catalogue `category = medium` — the two Zeison Sha, the three Jal Shey, and
Darth Malak's Armor.

⚠ I did not treat the droid plating rows as a fault, per your note.

# 2 · SLOW, MIRE AND ROOT — AND ROOT REPLACES

All three on **failed** Will saves, which is the only way any of it is visible:

| power | cost | the rows it printed | condition |
|---|---|---|---|
| Force Slow | 6f | `-2 defence · -2 reflex · -2 attack` | `slowed` |
| Force Mire | 12f | `-4 defence · -4 reflex · -4 attack` | `slowed` |
| Force Root | 18f | **`-6 defence · -6 reflex`** | `slowed` |

    Force Slow · 6f — 159 → 153 · at d-slow.probe.01 ·
      d-slow.probe.01 — d20 16 = 12 vs 25 · slowed · -2 defence · -2 reflex · -2 attack
    Force Mire · 12f — 153 → 141 · … d20 18 = 14 vs 25 · slowed · -4 defence · -4 reflex · -4 attack
    Force Root · 18f — 141 → 123 · … d20  9 =  5 vs 25 · slowed · -6 defence · -6 reflex

**Root carries no attack penalty at all**, and the strongest part is that it was
cast on the *same* target that was already carrying Mire's `-4 attack`: Root
added nothing to it. Its stated list is complete on its own — replace, not
extend, exactly as ruled.

⚠ All three also applied `slowed`, and all three used a caster at DC 25 against
a Will of −4, so every save failed by construction. A made save would have shown
nothing whatever, which is why the bed was built to fail.

# 3 · THE DISEASE TREE

## It lands, and it is permanent

    Force Affliction · 12f — d-weak.probe.01 —  7 off str ·  7 off dex ·  7 off con — until rested
    Force Contagion  · 16f — d-weak.probe.01 —  4 off str ·  4 off dex ·  4 off con — until rested
    Force Plague     · 20f — d20 18 = 11 vs 25 · slowed ·
                             d-weak.probe.01 — 12 off str · 12 off dex · 12 off con — until rested

**7, 4 and 12** — the stated points, off all three stated abilities. The line
says **"— until rested"** in the product's own words, which is the clock
question answered without my having to infer it.

## And it persists, and it reaches the combat math

Several rounds after the three casts, with 23 points off Dexterity between
them, I hit the target and the attack line read:

    Vibrosword · rolled 22 — d20 9 + attack 9 + Strength 4 · needed -2 — hit

**`needed -2`.** Its Defence has collapsed below zero and stayed there across
the intervening rounds. Nothing ticked it away — which is the difference
between this and the timed penalty rows in §2.

## ⚠⚠ A MADE FORTITUDE SAVE STOPS IT — and the bed is the whole point

Your correction is right and it changed the test. At DC 25 a made save is not
reachable, so casting three times and watching the damage land would have
proven nothing at all about the save. I rebuilt for it: a caster at **WIS/CHA
10**, dropping the DC to **17**, against a level-30 target with a **+27**
Fortitude — so a made save is a property of the bed rather than something to
wait for. One target in the room, because the cast auto-aims and kept choosing
the nearer body.

    Force Contagion · 16f — at d-tough.probe.01 · d-tough.probe.01 — resists
    Force Plague    · 20f — at d-tough.probe.01 ·
                            d-tough.probe.01 — d20 20 = 47 vs 17 · resists · resists

`d20 20 = 47 vs 17` is a genuine made save with its arithmetic on show, and
**no points were taken** — by either power. Plague's two `resists` are its
condition and its ability damage, both stopped. `PT-2259`'s `?? true` holds
where the document declines to say, and it matches Affliction's explicit
`on_save: negate`.

---

## ⚠ One small thing worth knowing

**The cast's aim cannot be chosen.** In the two-target area, Mire and Root both
went to the same body Slow had hit, and Contagion and Plague both went to the
near target however I moved — I never got either to aim at the far one. It is
the same structural aim I reported in TEST 097 for self-powers, seen from the
other side: for an offensive power the picker takes a target and the player does
not. It cost me a rebuilt area; for a player it means a power cannot be spent on
the enemy they mean.

## What I did not do

- **Did not re-confirm Plague's dying-window on Hard** (`PT-2192`/`PT-2193`).
  You marked it optional and I ran out of room before it; it is the one item of
  the routing left untouched.
- **Did not test the other five exempted items** — one of the six, chosen
  because it is the one whose name would not save it.
- **Did not test a made save against Force Affliction** — its `on_save:
  negate` is explicit in the row rather than ruled, and you named Contagion and
  Plague as the new question.
- **Loom not launched.**

## State

- **New package `force-gate` is mine**, four areas and seven armour items.
  Its three validator problems are the area-connectivity ones described above.
- Nine authored saves, one per armour body plus the low-DC caster; all format 3.
- ⚠ Targets carry 4000 vitality so nothing died mid-measurement, and `d-weak`
  is built to fail every save while `d-tough` is built to make every one.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.** Scratchpad trimmed afterwards.
- App pids `432696`, `433991`, `435200`, `437049`, `437558` all killed by pid
  and confirmed gone; no Loom; nothing of yours touched.
