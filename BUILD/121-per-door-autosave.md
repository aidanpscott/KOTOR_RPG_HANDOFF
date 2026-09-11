# BUILD 121 — autosave is the door's decision

`PT-1666`, owner ruling revising `PT-1665`. **Autosave no longer fires on every
door crossing.** A connection carries `save_on_use`, unset by default, and only
a checked door writes.

⚠ **The mechanism did not change and was not touched.** The write, the
status-line word and append-not-assign are `PT-1663`'s and `PT-1665`'s. What
moved is **who decides** — the door, not the crossing.

---

## 1 · ⚠⚠ THE SURFACE EXISTS, AND IT HAD NOTHING TO PUT IN THE ROW

The owner asked me to say whether a door authoring surface exists and, if not,
what the smallest version looks like. **It exists.**

`Loom`'s `_SelectionBar` — the placement property sheet built at `PT-1566` —
has shown **doorways** since `PT-1553` put the selection in the shell. Select a
door on the board and it already names the tag, the target and the landing
point. It had **delete** and **clear** and no fields, because until this ruling
a doorway had no authorable property at all.

> **So the nearest surface WAS the right one. What it lacked was a field, not a
> screen.**

The checkbox is a `_Toggle` — the same control `hidden` uses, a word with a
filled or hollow mark rather than a coloured box, because `PT-1517` rules that
**a control whose only signal is colour loses its identity exactly when it
dims.** Under it, one line saying what the state means.

    door.deck.01
    doorway → a02-hold · north          clear   delete

    ◉ save on use
    crossing here saves the game and says so — §4b

## 2 · ⚠⚠ THE DEFECT CLOSING IT EXPOSED — A RULE APPLIED TO ONE PATH

`ContentsWriter.withFieldsSet` — the edit-in-place path — matched
`[[contents]]` only. `withTagRemoved`, **eight lines down, same file, same
argument**, matched **both** `[[contents]]` and `[[connections]]`.

> **A doorway could be DELETED by tag and not EDITED by tag**, and the selection
> bar had been showing doorways for the whole time that was true.

It is fixed by making the header test the same test in both. A tag is unique
across an area — `§2·0f` gives the area **one** counter, so a door and a
creature cannot collide on a number — which is why one lookup serves both.

## 3 · ⚠⚠ THE GATE'S TWO ARMS HAD TO BECOME EXCLUSIVE

`PT-1658`'s gate read:

```dart
if (arrived.isNotEmpty && (landing != null || hadRecord))
```

`hadRecord` is *the log has ever placed this character anywhere*. **On a
crossing it is true for everybody.** Left as an `||`, an unchecked door would
have written through the second arm —

> **the ruling would have shipped inert, and every test of it would still have
> passed**, because the first arm makes the checked case work either way.

The two arms are different questions about different moments. A load asks *did
a fallback move me*; a crossing asks *does this door save*. The structure now
says so:

    a checked door        through.saves        → write, and say so
    an unchecked door     through != null      → nothing
    a fallback on a load  hadRecord            → write        (PT-1605)
    an ordinary resume    the log said here    → nothing      (PT-1658)

## 4 · ⚠⚠ AND `PT-1657`'s SUPPRESSION WAS AIMED AT THE WRONG SUBJECT

**This is the finding of the slice**, and it is this project's most expensive
recurring shape, in the guard written against it.

`_writePosition` refuses to emit a position **the log already records** —
`PT-1657`, and it is right: resuming a save re-recorded a fact the save already
held, so **looking at a save reordered the shelf.**

That check was exactly correct while every position in `_log` had **also
reached disk**. `PT-1658` put the first exception in — a load's arrival, which
came *out of* the save, so nothing was at risk. **`PT-1666` puts in a second
that is nothing like it:** an arrival through an unchecked door is a place the
player genuinely walked to and **the save has never heard of it.**

> Cross an unchecked door, press `esc`. `_leaveScreen` asks `_writePosition`,
> which **asks memory whether disk knows**, and memory says yes. Nothing is
> written. **`PT-1523`'s second moment — *leaving the screen persists where you
> stand* — would have been silently repealed by a ruling about doors.**

The two questions are now asked separately, and neither answers for the other:

    duplicatesLog      → do not add it to `_log` a second time
    _unsavedCrossing   → disk has not got it, so emit it anyway

⚠ **And the flag is not *did the position change*.** A resume that derives a
square nobody established must still write nothing on the way out — `PT-1658`'s
fifteen-of-twenty case. What it marks is **a fact a player made**, held back
only because the door said not to save yet.

## 5 · ⚠ ONE PARAMETER, BECAUSE THE PAIR COULD DISAGREE

`_enter(id, landing:)` became `_enter(id, through:)`, one record of
`(lands, saves)`.

A `String? landing` beside a `bool saves` is **a pair a caller can set
inconsistently** — `saves: true, landing: null` is a door that saves and goes
nowhere, which the type would have permitted and nothing would have caught.
`PT-1560`: *"a signature that lies about the model is a defect waiting for its
second caller."* A crossing is one thing, so it is one value.

## 6 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| reader always `false` | `AND A CHECKED DOOR SAYS SO IN THE FILE` |
| reader always `true` | all three default/`false`/non-boolean cases |
| `withFieldsSet` back to contents-only | `THE IN-PLACE EDITOR REACHES [[connections]]`, and the round trip |
| toggle writes `false` instead of `true` | the round trip, and `UNCHECKING REMOVES THE LINE` |
| gate ignores the door (`PT-1665`'s behaviour) | `AN UNCHECKED DOOR WRITES NOTHING`, and `play_walk` |
| crossing not held (`_unsavedCrossing` never set) | `the arrival was DISCARDED rather than held` |

⚠ **And `loom_can_write_test` fired on its own**, naming
`area_open.dart: save_on_use` **the moment the reader gained the field and
before the toggle existed** — which is the whole errand it was built for.

## 7 · ⚠ THE TEST BED NOW HAS ONE OF EACH

`~/.local/share/kotor-rpg/packages/endar-spire` — the shared bed, **not a repo**
— had two doors and both were silent. `a01`'s forward door now carries
`save_on_use = true`; `a02`'s way back does **not**.

⚠ **Both halves are now walked in one test.** `play_walk_test` crosses forward
and expects `saved`, then crosses back and expects **nothing** — and the second
assertion is the one that can tell a working gate from an ignored one.

`PT-1667` said re-confirming after the checkbox lands *"would need a door with
the box checked, which does not exist yet."* **It exists now, and it is the
Command Deck's aft door.**

## 8 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 511 | **515** |
| `Loom` | 244 | **252** |
| `Lens` | 7 | **7** |
| `KOTOR-RPG-APP` | 404 | **405** |
| | 1,166 | **1,179** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing and both in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins compared, all level.

## 9 · Not done, named rather than skipped

- **No package in the tree ships a checked door except the test bed.** Nothing
  autosaves that did not ask to, which is the ruling; it also means a player
  opening an existing package will see autosave never fire until an author opens
  Loom.
- **The tree row does not show the checkbox state.** A door that saves looks
  like a door that does not until it is selected.
- **`Lens` draws nothing for it.** A save point is invisible on the board,
  which may be right — it is a rules fact, not a picture — and is the owner's.
