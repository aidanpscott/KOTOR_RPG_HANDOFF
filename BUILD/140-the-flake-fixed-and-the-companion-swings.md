# BUILD 140 — the flake given a cause, and the companion proved to swing

---

## 1 · ⚠⚠ THE `whole_loop_test` FLAKE — THIRD SIGHTING, AND WHAT ALL THREE SHARE

`sandboxed()` symlinks `packages` at the **real shelf**, and the real shelf is
shared with `Tester`, **who creates and deletes fixture packages while a suite
is running** — it held nine the last time I counted and two of those appeared
during this thread.

This file taps a package **by name** in a **lazy horizontal row**: a tile past
the fold is **not built at all**, so `find.text` returns nothing and its
position depends on how many packages exist *at that instant*. It has failed in
a full run and passed alone three times, **always on the shelf and never on the
code** — confirmed once by stashing, where the clean tree failed harder than
mine.

**⚠ THE FIX IS THE TOOL THAT ALREADY EXISTED.** `copiedShelf(only: […])` —
*"a copy of the real one, not a fixture… `PT-1346` rules the test bed is the
Builder's own output"* — so the bytes are the shipped ones and **nothing can
change under the run.** Two packages, `base-rules` and `endar-spire`, which is
everything this file opens.

**⚠ AND WITH TWO TILES `Endar Spire` IS NEVER PAST THE FOLD**, which removes the
scroll from the equation rather than making the scrolling cleverer. The copy
costs nothing measurable: the file still runs in 28 seconds.

> **⚠⚠ AND I COULD NOT REPRODUCE IT TO CONFIRM THE MECHANISM.** Two full runs
> back to back both passed before the change. **This is the cause the evidence
> fits, not one I watched fail**, and the comment in the file says so — a fix
> for an unreproduced flake is a hypothesis until it survives a few weeks.

## 2 · ⚠⚠ AND THE COMPANION ACTUALLY SWINGS — THE HALF I SHIPPED WITHOUT ASSERTING

`BUILD 139` proved the sides, the roster and the wipe rule. **It did not prove
the companion acts**, and *"fights on your side"* is the claim the whole slice
rests on. Caught it re-reading my own report rather than from a failure.

It does. `enemyTurn` returns null **only** for the `playerTag`, so anybody else
is driven by the doctrine — and the doctrine's `foes` come from `isParty`, so a
companion's targets are **the player's enemies with no word added anywhere.**

The mutation that flips the side filter makes the companion swing **at the
player**, and this is the case that sees it.

## 3 · ⚠ `PREGENS-01`'s DROID DEFENCE — COMPUTED, NOT EDITED

`PT-1446` makes `MAIN_WORK/playtest/` the owner's, and `PREGENS-01` is in it. So
these are the numbers rather than a commit:

| Pregen | Plating | Was | **Now** |
|---|---|---|---|
| **T4-K9** *(line 267)* | Light | `10 + 4 + 2` = **16** | `10 + 3 + 2` = **15** |
| **HK-24** *(line 369)* | Medium | `10 + 6 + 2` = **18** | `10 + 4 + 2` = **16** |

**There is no Heavy-plating pregen**, so `+9` changes nothing here.

**⚠ AND NOTHING ELSE IN THE PROJECT CARRIES THESE NUMBERS.** Censused across the
corpus, the shelf and the app: droid plating is not an item blueprint in any
package, and the app derives Defence from `defenceTerms` and the class ladders.
**Two figures, one file** — plus its mirror at `HANDOFF/docs/PREGENS-01.md`,
which syncs.

The placeholder markers can go with them: lines **275**, **285**, **375**,
**427**, and the open-questions row at **495**.

### ⚠⚠ AND THE REAL LADDER CHANGES WHAT THE GRADES ARE *FOR*

The placeholder's `+4 / +6 / +8` was a smooth ramp where each grade was simply
better. The real `+3 / +4 / +9` is not:

> **Light and Medium are one point apart and both uncapped; Heavy is five
> better and caps Dexterity at `+1`.**

So the choice is **not** a ladder at all — it is *high-Dex droids take Light or
Medium and keep their Dexterity; low-Dex droids take Heavy and trade it away.*
The placeholder made Medium a real step up over Light; the data makes it nearly
a wash. **Worth knowing before anyone balances against the old shape.**

Both droids also get easier to hit, and **closer to each other** — two points
apart becomes one.

## 4 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 625 | **625** |
| `Loom` | 261 | **261** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 503 | **504** |
| | 1,399 | **1,400** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓. **Three consecutive clean full
runs**, which is not proof the flake is gone but is what there is.

## 5 · ⚠ Companions — still not done

- **Nothing recruits.** A companion is placed by an author and is in the party
  from the moment the area opens. `AUTHORED-CHARACTER-01 §5`'s *"the log applies
  to it from the moment it joins"* has no **joining**, and what triggers one is
  a design question rather than a gap I can close.
- **Nothing switches control** — the doctrine drives it, which is what makes the
  slice work at all.
- **It does not travel.** Walk through a door and it stays in the room, because
  `[[contents]]` is an area's and nothing carries a party across one. **This is
  the most defect-shaped of the three** — a party member that does not follow is
  not a party member — but *how* it travels is still a decision.
- **`§10`'s enemy-side trigger is reachable for the first time** and nothing has
  driven it. A `TEST` pass: an enemy walking past a companion to reach you.
