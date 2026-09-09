# BUILD 64 — `PT-1488`: choose one, check eligibility

**696 green** — Lodestar 303 · Lens 4 · Loom 120 · app 269.

---

## The target

A cast has one now. **The thing you are fighting** — the same affordance as an
attack, where walking into a creature strikes it. ⚠ No document rules a second
one, and building a target picker to aim at the only thing present would be
building ahead. **Casting outside a fight refuses and spends nothing.**

## The gate — three answers, and it never guesses

| | |
|---|---|
| **permitted** | the `targets` column names the kind |
| **excluded** | ⚠ and the wording says **which half refused** — *"does not affect a droid"* is the prose; *"is aimed at droid, not a sentient"* is the column omitting it. **A list that omits a kind is not the same as prose that excludes it.** |
| **silent** | nothing says — 15 of the 22 powers open at 1st level |

⚠⚠ **An excluded cast spends NOTHING.** A refused cast that still cost you the
pool would read as a tax, which is the worst of both.

---

## ⚠⚠ And a placement has no kind — a finding, not a gap I left

`AUTHORED-CHARACTER-01` gives a character blueprint a name, a class, a level, a
faction, abilities, vitality and protection — **and no species and no
chassis.**

- the Sith Trooper's file names none
- `Loom`'s character writer offers none
- `OpenedCharacter` has no field for one

So `kindOf` returns **null for every creature in the bed**, and the gate says
*"nothing records what this is"* rather than reading absence as consent.
**Inferring `sentient` from the absence of the word `droid` is exactly the
guess this gate exists to prevent.**

⚠ **It explains something else too.** `combatantsIn` takes `speed` as a
hardcoded argument, and `AUTHORED-CHARACTER-01` line 144 says speed lives on
the species because *"the blueprint carrying one would be a second source for a
fact the species already owns"* — **and there is no species to own it.** One
absent field, two symptoms.

**NEED:** a character blueprint cannot say what kind of thing it is. Until it
can, the gate is correct and permanently silent about placements, and
`PT-1486`'s `excludes` has nothing to refuse.

---

## The column shape — `HANDOFF/TEST/POWER-COLUMNS-SHAPE.md`

Measured first, and **the six you named become thirteen honestly**:

- ⚠ `dc_scale` earns its place — three real formulas in nineteen phrasings,
  **plus a fourth running the other way**: `Force Immunity` and `Force
  Resistance` are `DC 15/10 + the DEFENDING character's level`.
- ⚠ `dc_abilities` is `wis+cha` in **49 of 53** and `none` in 4. I would rather
  read `none` than infer it.
- ⚠ **Damage cannot be one column** — nine rows share a two-band shape with
  four moving parts. Five named fields, because a grammar inferred from nine
  examples is the positional-array defect again.
- ⚠ `Force Resistance` gets `not_modelled = "opposed roll, not a save"` rather
  than being pressed into `save_type`. **Absence and error must stay
  distinguishable.**
- ⚠ **No column for movement** — 3 of 104.

## Still open

- ⚠ **A blueprint has no species**, so no placement has a kind.
- The effect columns — yours, and the shape is filed.
- `PT-1484` unblocked; `PT-1485`; 45 annotation cells; conditional damage.
