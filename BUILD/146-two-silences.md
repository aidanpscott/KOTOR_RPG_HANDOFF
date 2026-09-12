# BUILD 146 — two silences, and two items that were already built

---

## 0 · ⚠⚠ TWO OF THE THREE THINGS ON MY OWN LIST WERE ALREADY DONE

I read the code before building anything, and it is worth saying plainly that
**my list was stale rather than the product**:

* **`PT-1653`** — Console Home saying nothing about package health — was built
  at **`PT-1648`**, commit `1721be8`, *"package health at the screen where a
  package is chosen"*. Per-tile problem counts, a row-level *"checked, none
  with problems"*, and `package_health_on_console_home_test` includes **the
  exact pair Tester compared** (*"THE PAIR TESTER COMPARED NO LONGER RENDER
  ALIKE"*) and an end-to-end case asserting the tile's count is the one
  `Verify` would give. `PT-1653`'s other half — *"`2 rules unchecked` is not a
  health indicator and looks like one"* — was closed at `PT-1648` too, by
  naming its subject.
* **`PT-1640`'s ability half** — `combatantFrom` reading species for speed and
  not for abilities — was built at **`PT-1636`**, and `main.dart` passes
  `abilityAdjustmentBySpecies` through all three `combatantsIn` call sites.
  **⚠ I checked the one I added myself last slice** (`_sidesChanged`,
  `PT-1745`): it passes all four facts, so a recruited companion is not
  rebuilt at bought scores.

**Nothing was rebuilt.** What was left of `PT-1640` is `§5` below.

## 1 · ⚠⚠ THE BOARD'S EDGE REFUSES OUT LOUD — `PT-1610`'s SHAPE

`_step` had **one silent `return` left**:

    if (nx < 0 || ny < 0 || nx >= a.width || ny >= a.height) return;

Every other refusal in that same function is a sentence. The wall names the
tile. The corner says it is *too tight to cut*. A companion says who they are.
**Walking off the map did nothing at all** — the same keypress, the same kind
of no, and **the only one a player could read as a key that is not bound.**

    the room ends there
    the room ends there — numpad 7 9 1 3 go diagonally

## 2 · ⚠⚠ AND THE HINT BELONGED TO IT ALL ALONG

`_boxedIn`'s own `free()` tests the bounds **before** it tests the tile. So a
player pinned against the map edge has **always** satisfied *"every orthogonal
blocked"* — the condition the wall's refusal uses to decide whether to name the
diagonals. **The edge and the wall were the same situation to the player and
two different answers on screen.**

The test board for it is `PT-1638`'s own, moved to the left wall of the map:

    # . .        (0,0) WALL
    P G .        the player at (0,1), a guard at (1,1)
    # . .        (0,2) WALL

West is off the board, north and south are wall, east is the guard — and
`(1,0)` is still reachable, because that diagonal's flanks are the guard's
square (open **floor**) and a wall. One flank open, so the step is legal. **The
escapable box, at the edge.**

## 3 · ⚠ ONE EXISTING CASE CHANGED ITS EVIDENCE AND NOT ITS CLAIM

*"AND A DIAGONAL INTO A WALL IS REFUSED LIKE ANY OTHER STEP"* proved *the
player is where they were* by reading the position line — **and that line only
shows when nothing else is being said.** It was reading the silence this slice
removed.

It now reads the refusal, then proves the position **by where the next step
lands**: `(1,1)` is one southeast step from `(0,0)` and from nowhere else on
that board. Same claim, evidence that survives the fix.

## 4 · ⚠⚠ `speedNote` HAD THREE HITS AND NONE OF THEM A READ — `PT-1640`

> *"`speedNote` is a second discarded sentence of the same kind as
> `DamageRoll.line`: three hits and none of them a read."*

`combatantFrom` has written it since `PT-1490` — **a species the rules do not
carry, or a blueprint naming none at all** — and nothing in the product ever
showed it. Set in one place, asserted `null` in one test, displayed nowhere.
**A fallback that explains itself to nobody is how `speed: 10` sat hardcoded
through every slice**, which is what the field's own comment says.

The in-area band carries it now. **No `⚠`**, because it is not a fault — the
creature is placed and it fights — and **after** the unresolved row, so that if
the panel must lose something, *a creature that is not on the board outranks one
that is merely slow.*

## 5 · ⚠⚠ AND THE SENTENCE GOT SHORTER BECAUSE I MEASURED THE PANEL FIRST

`PT-1501` was paid for **once already on this exact band**: two long sentences,
one `Text`, `maxLines: 2`, and the second one silently gone while every
`find.textContaining` test passed.

So I measured before keeping, rather than after `Tester` stood on it:

    Tester's own room (4 placements, 2 malformed)         163 chars, fits
      + the speed note at its old length (85)             ⚠ EXCEEDS two lines
      + the speed note at 47                              fits

**The fix is not a trim.** The half both speed sentences shared — *"so the
default is used"* — **moved into the count that leads them**, which is
`PT-1501`'s own rule:

    1 at the default speed — no rule for `snivvian`
    1 at the default speed — no species named

**And the measurement is a case in the suite now**, so the next clause somebody
adds to this band is measured before it is kept rather than after.

---

## What ran

    Lodestar   659 tests   exit 0
    Loom       261 tests   exit 0
    app        530 tests   exit 0   (+5)
    flutter analyze         clean
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings

Mutation-checked: dropping the edge sentence kills two cases; dropping the
band clause kills one.

## Heads

    Lodestar        95bc648   (unchanged)
    Loom            5ed6185   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   081ef6b
    MAIN_WORK       cc780df
