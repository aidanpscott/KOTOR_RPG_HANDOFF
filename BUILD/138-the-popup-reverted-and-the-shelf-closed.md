# BUILD 138 — the popup reverted, the field pre-filled, the shelf closed

`PT-1732`, `TEST 064`, and `taris-undercity`.

---

## 1 · ⚠⚠ THE POPUP IS GONE, AND THE REASON IT EXISTED WAS NEVER TRUE

`PT-1719` ruled the pop-up *"matching how KOTOR itself handles naming"*.
`TEST 064` checked retail directly: **it does not.** *"Name is a full-screen
panel, same chrome and modal weight as every other step — NOT a popup, nothing
else visible behind it."*

I built the overlay in `BUILD 137` and `PT-1732` landed after the push. Reverted
to the routed stage it was, from the commit before it, **position unchanged** —
`PT-1728` always kept name where Identity sat, and that half was never in
question.

## 2 · ⚠ AND THE SHAPE THE GAME ACTUALLY HAS

`TEST 064`: *"a single-line field pre-populated with an already-generated random
name, a Random Name button that replaces the whole field on each press
(confirmed twice, two different results)."*

Both built. **The button avoids returning what is already in the field** — one
that can return it reads as a button that did nothing — and the avoid loop is
**bounded rather than a `while (true)`**, because a name the player can overtype
beats a hang.

### ⚠⚠ THE NAMES ARE OURS, AND THE FILE SAYS SO IN ITS FIRST PARAGRAPH

I searched for a source and there is none: **no `names.toml`, no name column in
`species.toml`, and no ruling that names a single player character.** A
generated name needs a source and the project has none.

> So it is a **fixture**, with the standing `unarmed` has in `attack.dart`:
> *"these dice are ours… defined once, here… so that the next person searching
> for invented numbers finds one hit."*

One list, one file, and **the one thing to delete the day a name table is
ruled.**

### ⚠⚠ AND A DROID GETS NO GENERATOR AT ALL

`PT-1720`/`PT-1722`–`PT-1726` rule droid designations **exactly** — a chassis
prefix, a per-model suffix shape, and `DROID-MODELS-01 §0c`'s six-name canon ban
list — and `PT-1727` says none of it is built.

**Handing a droid "Vash Corrin" would be inventing over a rule that already
exists.** The field stays empty, the button is absent, and the screen says which
— *"a droid's designation follows its chassis, and that is not built yet."*

**⚠ `Rundown` CARRIES AN EXPLICIT `isDroid`** rather than testing
`species.startsWith('droid')`, which is **a value used as a key** — the shape
this corpus names, and the wrong way to ask a question a field can answer.

## 3 · ⚠ `taris-undercity` IS CLOSED

`endar-spire`'s eleven weapon blueprints cover all **eighteen** classes' stock
weapons between them. Copied — **verbatim except one line.**

`blaster-rifle`'s description read *"Republic-issue, and standard issue to Sith
boarding parties"*, which is `endar-spire`'s own fiction and not the Undercity's.
**Dropped rather than rewritten**: `description` is optional, absence is honest,
and **writing new flavour in somebody else's package is authoring rather than
repair.**

**⚠ MEASURED AFTER, NOT ASSUMED**: both packages now report **zero**
stock-weapon faults across eighteen classes.

**⚠ AND IT IS NOT IN ANY REPO.** The shelf lives at
`~/.local/share/kotor-rpg/packages`, which `Tester` shares — so this change is
on the machine and in no commit. Named here because that is the only record of
it.

## 4 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the field is not pre-populated | 1 |
| the button may return the same name | 1 |
| `anotherName` stops avoiding the current name | 1 |
| a droid gets the generator and an organic name | 1 |

### ⚠⚠ AND ONE OF THOSE ONLY LANDED AFTER I BUILT A SOURCE TO MAKE IT LAND

The avoid-loop mutation **passed** at first. With 576 combinations a collision
is a 1-in-576 event and a widget test will not reach it on purpose — **a guard
that cannot be made to fire is one `PT-1661` says is not a guard.** A scripted
`Random` that returns the same draw forever makes the collision certain, and the
mutation fails on it now.

## 5 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 619 | **619** |
| `Loom` | 258 | **258** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 493 | **497** |
| | 1,380 | **1,384** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 6 · ⚠ Not done, named

- **Droid designations** — ruled across `PT-1720`/`PT-1722`–`PT-1726`, unblocked
  by `TEST 064`, and not built. The name screen has the seam waiting for it.
- **`§4a`'s upgrade extraction**, parked as ruled.
- **The out-of-bounds silent `_step` return**, `PT-1640`, `PT-1653` — unchanged.

**Next: companions.**
