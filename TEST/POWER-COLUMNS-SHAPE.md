# The shape for `PT-1489`'s effect columns — what I want to read

**Measured across 104 powers before proposing.** Counts are how many rows
actually need each column, so the authoring cost is visible.

⚠ **Three rules, and they are `PT-1452`'s standard:**

1. **One form per column.** No column ever means two things.
2. **Absence is `null`, and `null` never means a default.** A power with no
   save has `save_type = null`; that is not "Fortitude 0".
3. ⚠ **A row that does not fit says so** — `not_modelled = "…"` — rather than
   being pressed into a column that nearly fits. One power needs this.

---

## The save — **53 rows**

    save_type      fortitude | reflex | will          null = no save
    dc_base        5 | 10 | 15                        null when save_type is
    dc_scale       caster_level | force_levels | defender_level
    dc_abilities   wis+cha | none

⚠ **`dc_scale` is the column that earns its place.** Three real formulas hide
in nineteen phrasings:

    DC 5  + the character's level   the majority
    DC 10 + the attacker's level    the Force Scream chain, ×3
    DC 5  + FORCE levels            Affliction · Contagion · Plague

⚠ **And `defender_level` is a fourth, running the other way.** `Force Immunity`
is `DC 15 + the DEFENDING character's level` and `Force Resistance` is
`DC 10 + the defending character's level` — **the target's level raises the
DC, not the caster's.**

⚠ **`dc_abilities` is `wis+cha` in 49 of 53 and `none` in 4** — and the four
are the two defender-scaled ones plus two that write *"at the same DC"*,
back-referencing a DC stated earlier in their own cell. **I would rather read
`none` than infer it from `dc_scale`.**

⚠ **`Force Resistance` is the row that does not fit.** It is an **opposed
roll** — *"d20 + his or her level versus a DC of 10 + the defending
character's level"* — not a save at all. `save_type = null` plus
`not_modelled = "opposed roll, not a save"`, so it is distinguishable from a
power that simply has no save. **That distinction is the one this project keeps
paying for.**

## The damage — **25 rows**, and ⚠ it cannot be one column

Nine rows share one scaling shape and it has four moving parts:

    1d6 per Force level to 20, then 1d6 per two levels — maximum 25d6
     ─┬─     ─────┬─────    ─┬─        ─┬─                     ─┬─
    die      scale        band       then-per                  cap

    damage_die     "1d6"                     null = no damage
    damage_per     1 | 2                      levels per die below the band
    damage_scale   force_levels | character_levels   ⚠ one row uses character
    damage_to      20                         the band edge; null = no band
    damage_then    2 | 4                      levels per die above it
    damage_max     "25d6"

⚠ **Five columns for one number**, and I would still rather have them than a
string I have to parse. A grammar inferred from nine examples is the
positional-array defect again — **named fields are why `extract_equipment` no
longer slides a Stun Baton's `attacks` into `balanced`'s slot.**

## The rest — cheap

    duration       integer, in rounds        null = instantaneous   67 rows
    condition      stunned | slowed | distracted | paralysed |
                   blinded | immobilised     null = none            11 rows

⚠ **A closed set of six**, counted: stunned ×7, slowed ×4, distracted ×2,
paralysed ×1, blinded ×1, immobilised ×1. If a seventh is needed, it is a new
value rather than free text.

## One row, whole, so there is nothing to guess

```toml
[[powers]]
id            = "force_choke"
save_type     = "fortitude"
dc_base       = 5
dc_scale      = "caster_level"
dc_abilities  = "wis+cha"
damage_die    = "1d6"
damage_per    = 1
damage_scale  = "force_levels"
damage_to     = 20
damage_then   = 2
damage_max    = "25d6"
duration      = 2
condition     = "stunned"
```

## ⚠ And what I do NOT want a column for

**Movement — 3 of 104.** `Force Push`'s *"pushed back 4 metres — 2 squares"* is
nearly unique. A column would be null on 101 rows and a push system would serve
three powers. ⚠ **Leave it in the prose and let the line say so**; when a
fourth power needs it, that is the slice that earns it.

---

# ⚠⚠ AMENDMENT before you author — four things the worked row was missing

You asked, and measuring found four. **A shape corrected after 104 rows is 104
rows**, so all four are here with their counts.

## 1 · `save_effect` — what a SUCCESSFUL save does · **24 of 53**

    save_effect    negates | half            null = the document does not say

⚠ Without it a save is rolled and **nothing knows what passing means.** 17
powers say *negates*, 5 say *half*, 2 say *"results in no effect"* — which is
`negates` in different words, and is why this is a column rather than a
keyword match. The other 29 saves state nothing, and `null` must stay
distinguishable from `negates`.

## 2 · `area_squares` — **19 of 104**, and it changes the TARGET slice

    area_squares   integer radius in SQUARES   null = a single target

⚠ **Nineteen powers do not have "a target".** *"all enemies within a 10-metre
radius"*, *"every creature in the user's line of sight within 10 metres"*,
*"every enemy within a 15-meter radius"*.

⚠ **In squares, because that is the board's unit** — and the document already
converts, twice: *"a 10-metre radius — 5 squares"*, *"14 metres — 7 squares"*.
**Please keep converting; the app cannot use metres and I do not want to divide
by two and call it a rule.**

## 3 · `damage_per_round` — **6 of 104**

    damage_per_round   true                   null = once, on the cast

`Force Choke` and `Force Strangle` deal their damage *"each round, for the
duration"*. Without this, `damage` × `duration` is unresolvable: **the same two
numbers mean one hit or twelve.**

## 4 · ⚠⚠ `affects` — WHO the power is aimed at · **and this one is not a column, it is a gap in my gate**

    affects        enemy | ally | self        null = the document does not say

Six powers **heal**, and ⚠ **three of them heal party members**: *"heals all
party members within 14 metres"*. `Dark Healing` heals **self**. `Death Field`
and `Drain Life` damage an enemy **and** heal the caster.

⚠ **`targets` and `excludes` say what KIND may be affected. Nothing says
whether a power is aimed at a friend or an enemy** — so `PT-1488`'s gate would
let you Force Push an ally and Heal a trooper with equal confidence. **That is
mine to fix and I cannot fix it without this column.**

## The worked row, amended

```toml
[[powers]]
id               = "force_choke"
save_type        = "fortitude"
save_effect      = "negates"
dc_base          = 5
dc_scale         = "caster_level"
dc_abilities     = "wis+cha"
affects          = "enemy"
area_squares     = null          # a single target
damage_die       = "1d6"
damage_per       = 1
damage_scale     = "force_levels"
damage_to        = 20
damage_then      = 2
damage_max       = "25d6"
damage_per_round = true          # ⚠ each round, for the duration
duration         = 2
condition        = "stunned"
```

⚠ **Seventeen columns, and I am not proposing an eighteenth.** Every one is a
fact the document already states in prose; none is a derivation. If a row needs
something none of them holds, `not_modelled` is the honest answer and I would
rather read that than a column bent to fit.

---

# ⚠ Batch one: **22 is enough — plus nine rows, and I measured which**

You asked whether 22 is enough to build against. **Yes**, and here is the check
rather than the opinion. Twelve shapes the columns have to carry, counted in
the 22 and in all 104:

| shape | in the 22 | in all 104 |
|---|---|---|
| save · negates | 4 | 17 |
| save · half | 4 | 17 |
| `dc_base` 5 | 12 | 46 |
| `dc_base` 10 / 15 | 1 | 5 |
| `dc_scale` force levels | 2 | 15 |
| ⚠ `damage_scale` character levels | **0** | 3 |
| `area_squares` | 2 | 25 |
| `damage_per_round` | 1 | 6 |
| ⚠⚠ heals — i.e. `affects` | **0** | 6 |
| `condition` | 5 | 13 |
| damage dice | 6 | 25 |
| no save at all | 9 | 47 |

**Ten of twelve are exercised**, several by a single row — which is enough to
find a shape that does not fit, and that is what a first batch is for.

## ⚠⚠ But the two it misses are not random

**No row in the 22 heals.** So `affects` would read `enemy` on all 22 and
**the column would look unnecessary** — the very column I argued hardest for,
untested by the batch chosen to test the shape. And `damage_scale` would be
`force_levels` on all 22, so a second value would never be written.

⚠ **A shape that survives 22 rows chosen by reachability is not the same as a
shape that survives 22 rows chosen to exercise it.**

## So: **31 rows, and the nine are named**

The 22, plus:

    Heal · Improved Heal · Master Heal      heal ALLIES  → affects = "ally"
    Dark Healing                            heals SELF   → affects = "self"
    Death Field · Drain Life                harm an enemy AND heal the caster
                                            ⚠ the two that may not fit `affects`
                                              at all — say so rather than
                                              choosing one
    the 3 rows scaling on character levels  → damage_scale = "character_levels"

**That is the smallest batch that exercises every column.** Nine extra rows
against a shape you would otherwise correct after 104.

⚠ **And `Death Field` and `Drain Life` are the ones to author first of the
nine.** If `affects` cannot hold *"harms an enemy and heals the caster"*, I
would rather learn it on row 23 than row 104 — and `not_modelled` is a
perfectly good answer there.
