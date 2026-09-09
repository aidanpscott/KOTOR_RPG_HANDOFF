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
