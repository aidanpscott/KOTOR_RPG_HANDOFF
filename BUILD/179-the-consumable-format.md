# BUILD 179 — the consumable format, and a number I got wrong by fifteen times

> ⚠ **FILED AS 177 AND RENUMBERED.** `177` and `178` were already spent — the
> effect model and the save channel — and **neither wrote a note file**, they
> were reported through `STATE.md`. So `ls BUILD/` stops at `176` and is not
> the register; the register is `STATE.md`'s history. Left visible because the
> next person to number a note will make the same check.

---

## 1 · ⚠⚠ THE CORRECTION FIRST

I reported the consumable format as blocking **"the 625 modelled effects"**, in
the proposal and again in the last two closing blocks. **It blocks 42.**

`item_effects.json` carries an answer to this and I never asked it. Every
effect has a `spends` field, written by the extractor itself:

    spends = none    583 effects    ⚠ worn. A belt that gives +2 Constitution.
    spends = gear     42 effects       a thing you use up.

**583 of the 625 are passive properties of equipment somebody is WEARING.** A
consumable base type does nothing for them. They are blocked on a different
thing, which `§4` below names and does not solve.

⚠ **This is `a check shaped by its examples` in the reporting rather than in a
script.** The blocker was found while building the Gear verb, so it got
described in Gear's vocabulary, and the 625 was the biggest number in reach.
Nothing measured it. **A scope figure fifteen times too large is an argument
for spending fifteen times too much on it** — and this one had been in front of
you twice.

The direction you ruled — *both a new consumable base type AND a way to reuse
the already-modelled resref-keyed effects* — **is unaffected.** Only the size
of the prize is.

---

## 2 · ⚠⚠ WHAT THE 42 ACTUALLY ARE — four kinds, not forty-two

Grouped by the shape of what they do, which is the only grouping the schema
cares about:

| Items | Does | Today's category | What it is |
|---|---|---|---|
| **15** | `absorb` | `shield` · `forearm` · `named` | an energy shield, a pool of damage soaked |
| **16** | `damage_over_time` · `condition` | `trap-kit` · `ammunition` · `grenade` | a harmful thing thrown or placed, with a save |
| **6** | `ability` | `adrenal` | +4 or +6 to one ability, 20 rounds |
| **5** | `heal` | `medical` | the medpac ladder |

**Four.** `EQUIPMENT-01` answered exactly this question for weapons — 1,425
items over 25 base types — and `SCOPE-ITEMS-01` states the principle outright:

> *"A ladder is one decision. `w_brifle_01` through `_30` are the same weapon
> at thirty quality steps, and what needs deciding is the CURVE, not thirty
> entries."*

**The medpac ladder is that sentence in miniature** — 10, 20, 30 vitality, with
the skill term multiplied ×1, ×2, ×3. One curve.

### ⚠ And two of the four are not Gear at all

**The 16 thrown-or-placed ones are aimed at somebody.** A Poison Grenade with
*"Save: DC25, 5 rounds"* is an attack, not a thing you use on yourself, and
`§5.2` already assigns the placed half elsewhere: **Demolitions — mines — one
per placement; the skill governs grade and radius.** Ten of the sixteen are
`trap-kit`.

**The 15 shields are worn AND spent.** `§3`'s Gear is *"using a consumable **or
activating a worn device**"*, so the ruling already has a word for them — but
they need the worn path in `§4` as well as the gear one, because the pool has
to sit on the wearer.

> **⚠ So the clean, fully-ruled case is 11 items: 6 adrenals and 5 medpacs.**
> That is what Gear can actually pay for today, and I would rather say so than
> let the 42 stand as a second inflated number four notes from now.

---

## 3 · ⚠⚠ THE SCHEMA

### 3a · The precedent, which already exists

`equipment.toml` is not a weapon table wearing a general name. Its 38 rows sit
in **five sections**, and they do not share a field set:

    14  Ranged                damage, threat, range, attacks
    11  Melee - base weapons  damage, threat, attacks, balanced
     6  Wield classes         wield_class, weapons, may_be_paired
     4  Lightsabers           damage, threat
     3  Droid plating         ⚠ defence, max_dex — and NO damage, NO threat

**`Droid plating` is the whole argument.** A section of base types carrying
defence values and no dice is already in the table, already loaded, already
resolved by `base`. **A `Consumables` section is not a new kind of thing in
this file; it is the fifth precedent for a sixth section.**

### 3b · The proposal

> **`equipment.toml` gains a `Consumables` section carrying four base types:**
> **`medpac`, `adrenal`, `shield-generator`, `charge`.**
>
> **Each row carries the effect as VALUES, in `item_effects.json`'s own
> vocabulary** — `does`, `base`, `rounds`, `terms`, `save`, `pool`, `kinds` —
> **rather than as the prose `items.toml` carries today.**
>
> **An item blueprint names one, exactly as `PT-1452` already requires**, and
> gains nothing new:
>
>     [item]
>     name = "Advanced Medpac"
>     base = "medpac-advanced"

**⚠ Nothing about `PT-1452`'s one form changes.** *"`[equipment]` names a PATH
to an item blueprint. Always. An item blueprint names a BASE TYPE from the
rules, and the base type carries the dice."* A consumable's effect **is** its
dice. It belongs in the same place for the same reason, and the reason is the
one `AuthoredItem` already gives: *an item that restated them could disagree
with it.*

### 3c · The resref half, and why it needs no new field

**The join already exists in the shipped data and I had not noticed.**
`items.toml` carries `resref` and `id` on all 1,424 rows, **and they are the
same string on all 1,424** — the id IS the resref. `item_effects.json` is keyed
on it, and **all 367 of its rows resolve** against `items.toml`. So:

    items.toml          id = "g_i_medeqpmnt01"   resref = "g_i_medeqpmnt01"
    item_effects.json   id = "g_i_medeqpmnt01"   -> {does: heal, base: 10, ...}

**What is missing is not a link. It is a consumer.** Nothing reads
`item_effects.json` into the shelf, because until the effect model there was
nothing to read it into.

> **⚠ SO THE RESREF STAYS INSIDE THE RULES AND NEVER REACHES A PACKAGE.** The
> base-type row is built FROM the resref-keyed effect by the shelf build; the
> blueprint names the base type. A package that had to write
> `g_i_medeqpmnt01` would be naming KOTOR's file layout in our content, which
> is the thing `PACKAGE-NAMING-01` exists to prevent.

### 3d · ⚠ THE ONE QUESTION I CANNOT ANSWER FROM THE DOCUMENTS — yours

**Is a ladder one base type or several?**

    A   three base types        medpac · medpac-advanced · medpac-life-support
        Each row carries its own base and multiplier. `PT-1452` holds
        unchanged — the base type carries the dice, full stop. Four kinds
        becomes about nine rows.

    B   one base type, graded   base = "medpac", grade = 2 on the item
        One row per KIND, and the item names a step on the curve. Matches
        SCOPE-ITEMS-01's "the curve, not thirty entries" more literally.
        ⚠ But it puts a NUMBER on the item blueprint, and `AuthoredItem`'s
        own note is that an item carrying dice can disagree with its base
        type. A grade is a small number, and that is how it would start.

**I recommend A**, for the reason `item_open` already gives in its own
comments, and because three rows is not a ladder of thirty. **B is the right
answer the first time a consumable ships with twelve steps**, and nothing here
does.

---

## 4 · ⚠⚠ THE GAP THIS DOES NOT CLOSE, NAMED RATHER THAN LEFT AS A SURPRISE

**583 effects are worn, and no format carries them.** An implant that gives +3
Constitution, a robe with an energy resistance, 54 lightsaber crystals.

`AuthoredItem` has three fields — `name`, `base`, `description` — and no way to
say *this specific belt gives +2*. `EQUIPMENT-01`'s base types carry a weapon's
dice, which is correct, **and 325 items differ from each other precisely in the
property the base type does not carry.**

⚠ **This is not a consumable question and I am not proposing a schema for it in
the same breath.** It is the larger of the two by fifteen times, it is what
`ITEMS-01..09`'s *"tier, cost, properties"* column has always been about, and
it deserves its own look rather than being annexed to this one. **Flagging it
so the 42 is not mistaken for the whole of the item-effect problem the way the
625 was mistaken for the consumable one.**

---

## 5 · ⚠⚠ TREAT'S HEALING SCALE — and it is the same object, not a separate one

I owed you this as a second proposal. **Reading `§5.3` directly, it is not
separate:**

> **Medicine** — **one medpac**, more vitality restored. The roll answers *how
> much did that heal*, which matters mid-fight where counting supplies does
> not.

**Treat SPENDS A MEDPAC.** So Treat cannot be scaled before the consumable
exists, and the healing scale is a field on the `medpac` base type rather than
a constant in the play screen. That is why the verb ships today saying *"how
much it heals is not ruled yet"* — it is not waiting on a number, it is
waiting on the thing the number lives on.

### What the source actually says

The shelf carries KOTOR's own formula as prose on all three grades:

    Medpac              heal 10 + WIS modifier + (1 x Treat Injury)
    Advanced Medpac     heal 20 + WIS modifier + (2 x Treat Injury)
    Life Support Pack   heal 30 + WIS modifier + (3 x Treat Injury)

**The extractor already modelled it as values** — `base`, and `terms` of
`wis_modifier ×1` and `treat_injury ×n`. It is sitting in
`item_effects.json` unread.

### ⚠ Two things stop it being lifted straight in

1. **`Treat Injury` is not ours.** `SKILLS-01` refuses the mapping outright,
   and this one I read in the document rather than off a code comment —
   *"⚠ `Treat Injury` is not `Medicine` and `Knowledge` is not `Science`; they
   are different skills that happen to overlap"* — and `§6` puts
   **Medicine** under Effect. So the skill term is Medicine's rank; the shape
   is KOTOR's, the skill is ours. `_resolvePick` already rolls exactly that.
2. **KOTOR's formula has no die in it.** It is flat. `§5.3` says *"the roll
   answers how much did that heal"*, and `PT-1326` requires the derivation be
   shown. **A flat formula and a roll that answers the question are two
   different rules**, and I am not going to pick between them quietly.

### The proposal

> **heal = the medpac's `base` + the Medicine check's own total.**
>
>     Medpac (base 10), Medicine 4, rolls 13   ->   10 + 17 = 27 restored
>     "treat Mate — d20 13 + Medicine 4 = 17 · medpac 10 · 27 restored"

**Why this shape and not another:** it keeps `§5.3`'s sentence literally true
(the roll answers how much), it keeps the grade meaningful (the ladder is the
`base`), it keeps `PT-1326`'s derivation on screen, and **the skill enters once
rather than twice** — KOTOR multiplies the skill by grade AND adds WIS, which
on our smaller numbers would make a Life Support Pack in trained hands heal
more than most creatures have.

⚠ **The `×2`/`×3` multipliers are the part I am deliberately dropping**, and I
want that visible rather than buried: KOTOR's skill ranks run far higher than
ours, so a multiplier that reads as flavour there is a different curve here.
**If you want the grade to multiply the skill rather than add a base, say so —
it is the same field, read differently.**

---

---

## 6 · ⚠ ON THE CITATIONS IN THIS NOTE

You raised this last round and it applies here more than usual, so: **the
quotes from `SKILL-RESOLUTION-01 §5.2`, `§5.3`, `SKILLS-01`, `SCOPE-ITEMS-01`
and `PACKAGE-FORMAT-01`'s `PT-1452` ruling were read in those documents
today.** The `PT-1326` and `PT-1452` numbers attached to `item_open` and
`AuthoredItem` behaviour are **quoted off those files' own comments** — the
weaker kind. Every count in this note is measured, and the commands are
`item_effects.json`'s `spends` field and `items.toml`'s `category`, so none of
it rests on a citation being right.

---

## Tests

App **621** green (`+1`: the vitality band and the sidebar now agree mid-fight,
`f279d23`). Nothing in this note is built.

## Still open

- ⚠ **This note is a proposal and nothing in it is a ruling.** Four base
  types, `A` over `B` for ladders, and the heal shape in `§5` all need your
  word.
- **The 583 worn effects** — `§4`. Larger than this one and unproposed.
- **The 16 thrown-or-placed items** — Demolitions' half is `§5.2`'s mines and
  is not Gear.
- **Treat ships saying *"how much it heals is not ruled yet"*** until `§5`
  lands.
