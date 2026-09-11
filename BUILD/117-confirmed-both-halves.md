# BUILD 117 — confirmed, both halves, and the save thread closes

`PT-1661`'s pass, run on both guards. `PT-1605` confirmed and it needed a fix
first.

---

## 1 · ⚠⚠ `PT-1605` WAS BROKEN BY MY OWN GATE, AND I FOUND IT BEFORE CONFIRMING

`PT-1658`'s gate was `landing != null`. **On a load `landing` IS null**, so the
case `PT-1605` exists for — the saved square is no longer standable and `_enter`
puts the character somewhere else — **wrote nothing, and the log went on
claiming the wall.**

The rule has three answers, not two:

    a crossing              landing != null      → write
    the log said elsewhere  a fallback moved us  → write
    the log said here       an ordinary resume   → nothing

⚠ **AND A SAVE THAT RECORDS NO POSITION IS THE THIRD, NOT THE SECOND.**
`_firstStandable` derives the same square from the same area every time, so
writing it records **a derivation, not a fact anybody established** — and that
is fifteen of the twenty saves on the shelf. That is why the answer is not
simply *"write when the position differs"*.

**So `Tester 052`'s measurement and my fix did NOT agree, and the fix was
wrong.** It has its own case now.

## 2 · ⚠⚠ THE CONFIRMATION PASS — FOUR RUNS, AND EACH GUARD BITES ALONE

| | `whole_loop_test` |
|---|---|
| **A** both guards present | **4 passed** |
| **B** `PT-1658`'s structural gate removed | **FAILS** — *"a save with no recorded position was rewritten just by being opened"* |
| **C** `PT-1657`'s value comparison removed | **FAILS twice** — *"Continue rewrote the save it was only reading"* and *"an ordinary resume rewrote the save it was only reading"* |
| **D** restored | **4 passed** |

⚠⚠ **AND B IS WHY THE FIRST VERSION OF THIS PASS WAS NOT ENOUGH.** My first
fallback case asserted *an ordinary resume does not write* using a save that
**records a position** — and with `PT-1658`'s gate removed it still passed,
because `PT-1657`'s comparison covered it. **A case that cannot fail on the
ruling it is named after is the same defect one ruling up.** The third case —
a log with no `moved` at all — is the one that only `PT-1658` can answer.

## 3 · ⚠⚠ THE SWEEP: IS ANY OTHER TEST THE SAME SHAPE

**Twenty-six files assert an absence.** Rather than read them, I measured the
specific hazard: instrument `combatantsIn`, run the at-risk files, and list any
that START an entry and never FINISH one.

    a_wiped_save_opens_the_panel   start=1  done=0   ⚠ ENTRY NEVER COMPLETED
    position_survives              start=6  done=6   ok
    no_revive_after_death          start=1  done=1   ok
    a_conversation_is_recorded     start=1  done=1   ok
    free_interaction               start=3  done=3   ok
    unlisted_area                  start=3  done=3   ok
    entry_stop                     start=0  done=0   ok
    wound_survives                 start=3  done=3   ok

**One more found**, and it is `BUILD 112`'s `PT-1642` file.

⚠ **AND ITS CONCLUSIONS STILL STAND, WHICH I CHECKED RATHER THAN ASSUMED.**
Inverting `partyIsWiped` in `main._open` makes **both** its cases fail — so it
discriminates on exactly what it claims. `_where` is decided before anything
enters, so the hung entry is downstream of the assertion. **It is the same
hazard, named, and it is not a false pass.**

### So the full tally across three slices

| | |
|---|---|
| `a_read_does_not_reorder_the_shelf` | **vacuous — deleted**, `BUILD 116` |
| `whole_loop_test`'s first `PT-1654` guard | **vacuous — replaced** by `session_log_test`, `BUILD 115` |
| `a_wiped_save_opens_the_panel` | **hung entry, sound conclusions** — verified by inversion |
| the other seven audited | entries complete |

⚠ **THE ROOT IS STILL UNDIAGNOSED**: `combatantsIn` → `openCharacter` never
returns in some widget harnesses and returns fine in others, on the same
package. **It is what made two of my tests worthless and nothing detects it.**
In `STATE.md`, unclaimed.

## 4 · Closed

`PT-1632`, `PT-1654`, `PT-1657`, `PT-1658`, `PT-1661`, and `PT-1605`'s
re-confirmation. **Nothing further is owed on the save thread.**

---

## Tests

`Lodestar` 490 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` 398 — **1,139, green.**
Pins 4/4. Gate: 2 advisory warnings.
