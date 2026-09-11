# BUILD 116 — a load must not write, and a test of mine that asserted nothing

`PT-1658` built. **And `BUILD 114`'s guarantee was never actually tested.**

---

## 1 · ⚠⚠ THE CORRECTION I OWE, FIRST

`BUILD 114` closed `PT-1657` with three widget cases in
`a_read_does_not_reorder_the_shelf_test.dart`. They opened a save through `App`
and demanded the file be unchanged. **All three passed because the screen never
finished opening it.**

`_enter` awaits `combatantsIn`, which awaits `openCharacter`, and in that
harness the future never completes — traced step by step:

    ENTER   id=a01-command-deck landing=null
    ENTER-0 about to open a01-command-deck
    ENTER-1 opened a01-command-deck -> OpenedArea
    CI start contents=1
    CI item sith-trooper.command-deck.39 from=characters/sith-trooper
    CI  exists=true
    ⟨openCharacter never returns⟩

So nothing was ever written, and **a case asserting *nothing was written* is
green for the wrong reason.**

⚠ **FOUND BY REMOVING BOTH GUARDS AND RE-RUNNING. All three still passed.** It
is the check this corpus names most often — *a suspiciously clean zero is
usually a dead instrument* — and **I wrote the instrument myself, one slice
after writing the same lesson down about `whole_loop_test`.** Twice in two
slices.

The measurement moved to `whole_loop_test`, which demonstrably reaches the
board: it walks, fights, travels and reloads, and half the file would fail if it
were not entering.

## 2 · ⚠⚠ AND THE DEFECT IS REAL — CONFIRMED IN A LIVE HARNESS

With both guards removed, `whole_loop_test` now fails on the reload:

> **`Continue` rewrote the save it was only reading — that moves `savedAt`,
> reorders the shelf, and grows the log by one duplicate arrival for the life
> of the character.**

With the guards in, it passes. **That is the first non-vacuous measurement of
this defect anywhere in the suite.**

## 3 · ⚠ WHAT ARRIVAL SHOULD DO ON LOAD — AND IT IS STRUCTURAL NOW

> **Owner: it needs to record the game state in memory without necessarily
> writing to disk. Distinguish "the character is now loaded" from "something
> happened worth persisting."**

`_writePosition` still records the square in `_log`, so projections and
`_leaveScreen` see it. **Only the persist is gated**, and the gate is a fact
rather than a comparison:

    a crossing has a landing · a load does not

⚠⚠ **`PT-1657`'s GUARD WAS INCIDENTAL AND I SHOULD HAVE SAID SO.** It suppressed
the write by asking whether the log already recorded this square. Measured on
the real shelf:

    5 saves with a recorded position · 15 without

**For those fifteen there is nothing to compare against**, so the comparison
cannot answer and the write happens. Both guards are now in, and each was
checked against the other:

| guard removed | `whole_loop` (a save WITH a position) |
|---|---|
| both | **fails** |
| structural only | passes — the value comparison covers it |
| value only | passes — the structural gate covers it |

The value comparison covers the five; the structural gate covers the fifteen.

⚠ **`PT-1265` IS THE ROOT.** *The same log yields the same bytes.* **A read that
mutates what it reads breaks that at the root**, and no comparison of values can
be trusted to hold a guarantee that structure can.

⚠ **`PT-1523` IS UNAFFECTED.** Leaving the screen persists where you stand, a
door crossing persists its arrival, and a session that did nothing has nothing
to resume differently.

## 4 · What is left standing

⚠ **The shelf measurement is now a test**, not a memory: if every save comes to
record a position, it fails and says that `PT-1657`'s comparison would have been
sufficient after all — so the claim in §3 cannot quietly go stale.

⚠ **AND `PT-1654`'s FIXTURE IS UNBLOCKED.** `Tester` set it up against a stable
`savedAt` and a stable log across a load; both now hold.

---

## Tests

`Lodestar` 490 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` 396 — **1,137, green.**
⚠ **Two fewer than `BUILD 115`, and that is the point**: three vacuous cases
were deleted and one real one added. Pins 4/4. Gate: 2 advisory warnings.
