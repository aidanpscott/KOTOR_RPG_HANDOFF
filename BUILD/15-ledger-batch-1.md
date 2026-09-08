# 15 · Ledger batch 1 — events and replay, in memory

**`KOTOR-RPG-APP` `172963b` · `Lodestar` `e9483fb`.** 172 tests pass, analyze
clean. **Nothing is written to disk.**

---

## ⚠ THE ACCEPTANCE HOLDS — both shapes

A character is built **through the screens**, the log is replayed, and the two
records are compared **field by field** — every key of `asMap`, not a spot
check. Two independent paths to one record; if they were the same path the test
would be a tautology.

| | |
|---|---|
| **organic Jedi** | nine steps, every one completed, then Accept. `identity.name`, `origin`, two powers, and every other field reproduce exactly |
| **droid, Astromech** | six steps. **`origin` is `null`, not `{}`** — *absent, not zeroed*; `gender` null, `powers` empty, `chassis` set and `subrace` null |

The droid case is the one that would have passed by luck: **replay takes no
step order, no shape and no rules.** It is a fold over the log, and everything
it needs is in the events.

---

## ⚠ The re-lock, ruled — and it is my reading

**`character.step-reopened`**, carrying the list of steps it discarded. Replay
clears exactly those slices of the projection. **Nothing leaves the log** —
`CHARACTER-RECORD-01`: *"a correction is a new event, not an edit. Nothing
rewrites history."*

> **⚠ AND THE DISCARD LIST TRAVELS IN THE EVENT** rather than being re-derived
> from the step order at replay time. Replay *could* recompute "everything after
> Origin" — and would then replay an **old** log differently the day the order
> changes. Naming what was discarded, in the event, is the same argument as
> naming a superseding ruling beside a value instead of recomputing it.

**Flagged as mine, not ruled.**

---

## ⚠ The vocabulary does not cover creation

**`EVENT-KINDS-01`'s Character table has exactly one creation kind —
`character.created`** — and `§6` leaves every payload *"deliberately"*
unspecified. `CHARACTER-RECORD-01` asks for *"a species chosen, a point spent,
a feat taken"*, and there are no kinds for those.

`§4` says what to do: *"a package that needs a kind we do not have should say
so; an escape hatch that accepts anything is a vocabulary that has given up."*
**So thirteen kinds are proposed**, in `§2`'s own shape, tenseless, recording
rather than requesting, all `permanent`:

    character.species-set · .model-set · .class-added · .origin-set
    character.gender-set · .backstory-set · .ability-set · .skill-ranked
    character.feat-taken · .power-taken · .grant-resolved
    character.equipment-set · .identity-set     ⚠ and .step-reopened

**A reading, not a ruling.** They live in `Lodestar/lib/src/ledger.dart` and
`EVENT-KINDS-01` does not know about them.

---

## ⚠⚠ Two defects the ledger found on its first run

### The re-open kept the value of the step it re-opened

`_reopen` cleared every step **after** the one re-opened and **kept its own**.
Nothing read that value back, so nothing had ever noticed — **but the record
built from the choice objects still carried the old Origin while replay had
already discarded it, and the two paths disagreed.**

A step that is not complete has no value in the record. It is cleared now.

> **This is what the batch was for.** Four slices of passing tests, a capture
> pass and a design review did not find it; two paths to one record found it in
> one run.

### A 337-pixel overflow no capture could have shown

The hub summary's `_Line` put two unconstrained `Text`s either side of a
`Spacer`. **The first time a *completed* Abilities line — six scores — reached
it, it overflowed by 337px.** No capture had ever completed Abilities. The value
takes what is left and wraps.

---

## The two orphans

| | |
|---|---|
| **`backstory.lifestyle`** | **No event.** `PT-1411` marks it orphaned in the record itself, and `PT-1401` left nobody to choose one. **An event for a choice nobody makes invents a value**, and `§1`'s own principle is *absent, not zeroed* |
| **`identity.story_origin`** | **Written.** `§5` calls it *"proposed here, not ruled"* — but the screen already produces all three of its values, and if the field is later dropped the projection loses a key, which is cheaper than a value nobody can reconstruct |

---

## ⚠ A contradiction inside `CHARACTER-RECORD-01` — reported, not resolved

| Section | Says |
|---|---|
| **`§2`** | *"`abilities` — the **final** scores, not the point-buy spend."* |
| **`§5`** | *"Closed at `PT-1260` … `abilities` holds the **bought** scores; the species modifier is applied on read, per `§3`."* |

**The ledger follows `§5`**, because it is also what `§1`'s own first principle —
*store the choice, derive the consequence* — requires, and `§3` lists ability
adjustments as derived. Both are recorded in the code.

---

## Scope, and what was NOT built

**No file, no header, no compression, no `Continue`, no `Load Game`.**
`SAVE-LOAD-01` is batch 2 and `PT-1265`'s bit-identical guarantee is its
acceptance, not this one. Play still leads nowhere.

**Not built:** validation. `§4` gives thirteen legality rules and replay checks
none of them — *"validate on load"* means validate the projection, and there is
no load yet.

**One thing recorded by name because there was nothing else:** a droid model
has **no `id`**. `DROID-MODELS-01` is keyed by chassis and the extraction
carries no identifier, so `character.model-set` records the model's **name**.
