# BUILD 119 — autosave on door use was already true, and silent

`PT-1663`. The question answered first, then the one thing that was missing.

---

## 1 · ⚠⚠ THE ANSWER: A DOOR CROSSING ALREADY PERSISTS TO DISK

> **Owner: before building, answer one question rather than assuming it — does
> a door crossing already persist TO DISK, or only to the in-memory log until a
> leave or quit flushes it?**

**To disk, on the spot.** It has since `PT-1523` gave the arrival its place:
`_enter` calls `_writePosition`, hands the event to `onAppend`, and that runs
`main._append` → `SessionLog` → `SaveStore.write`. **A file write, awaited,
inside the crossing.**

⚠ **MEASURED RATHER THAN READ OFF THE CALL CHAIN.** The existing mid-session
read in `whole_loop_test` sits after a fight AND a travel, so it could not say
which wrote. The samples are now taken **either side of the crossing and
nothing else** — an ordinary step writes nothing, `_writePosition` fires at two
moments only — so any change between them is the arrival and nothing else.

**Checked by removal**: disable the arrival's persist and the case fails with
*"crossing a door wrote nothing to disk"*. ⚠ **And a first attempt at that
check did NOT bite** — removing only the `landing != null` limb left `hadRecord`
covering it, because after the first arrival the log already holds a position.
The crossing is persisted by **either** limb; only removing both stops it.
`PT-1661`, applied to my own check before trusting it.

### So the ruling was already built, except for one half

**`PT-1663` needed no new write and no new detector.** What it needed was the
half that did not exist: **a player has never had any way to know.**

## 2 · ⚠ WHAT COUNTS AS USING A DOOR, AND IT IS ALREADY STRUCTURAL

**A connection crossed, not a doorway stood next to.** The travel fires from
`_step` on `c.x == nx && c.y == ny` — *stepping onto* the connection's square —
and `landing` is non-null only there. **The definition is a fact about the code
path, not a comparison**, so `PT-1580`'s confusion cannot recur here: there is
no approach branch to leak into.

## 3 · The two open questions, ruled

| | |
|---|---|
| **Does a fight suppress it?** | ⚠ **No — keep writing mid-fight.** Measured current behaviour: walking out mid-fight writes the outcome and the arrival together, which is `PT-1448`'s own path. Suppressing it would re-open the hole that ruling closed — *"the outcome of every fight a player WALKED OUT of died with the process."* Unchanged. |
| **Does the player see it?** | ⚠ **A word on the existing status line.** |

## 4 · What was built

    Starboard Hold · north · saved

⚠ **APPENDED, NOT ASSIGNED.** `PT-1464` is the rule and it was learned here:
*"the toll's sentence was set in `_step` and then overwritten by the arrival
line inside the same synchronous call"* — the defect that hid the player's own
attack across four `TEST` reports. This appends exactly as the toll does, so the
room's name and the save land **on one frame**.

⚠ **SAID AFTER THE WRITE, NOT BEFORE IT**, so it reports what happened rather
than what was about to.

⚠ **AND IT IS AS TRANSIENT AS THE ROOM'S NAME.** The next successful step clears
`_said`, which is why `whole_loop_test` cannot assert it — its walker is still
walking when the travel happens. The assertion lives in `play_walk_test`, whose
crossing is controlled and stops on the arrival frame. **Said rather than
worked around.**

### Confirmed by removal, both halves

| | `play_walk_test` |
|---|---|
| indicator removed | **fails** — *"the door wrote the save and said nothing"* |
| assigned instead of appended | **fails** — *"the save and the room are on separate lines, so one will overwrite the other"* |
| restored | passes |

The second case is the one worth having: a version that assigns would pass a
naive *"does it say saved"* check and silently destroy the arrival line.

---

## Tests

`Lodestar` 503 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` — see the push.
Pins 4/4. ⚠ Nothing in the aptitude derivation was touched.
