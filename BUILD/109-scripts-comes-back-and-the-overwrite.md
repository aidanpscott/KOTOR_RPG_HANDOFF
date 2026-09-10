# BUILD 109 — `scripts` comes back, and the crossing was overwritten

Loom `908a412` · app `4b66395`. Loom 239 · app 374 · Lodestar 463 · Lens 7 —
**1,083 green.** Screenshot: `BUILD/screens/109-loom-three-roots.png`.

---

# ⚠⚠ `PT-1626` — `downed` WAS WRITTEN AND THEN OVERWRITTEN

`Tester` narrowed it as far as testing from outside can go: *"`r.ledgerKinds`
does not contain `downed` for that blow."* **It does.**

    the engine       applyDamage at exactly 0 → [character.downed]
    the fight        Fight.enemyTurn carries it — probed on that exact blow
    the screen       _persistCrossing calls _persist with it
    the filter       campaignKinds holds it, and Tester proved that too

**The loss is one layer further down, in `main._append`.** A save is rewritten
WHOLE: it reads the log, builds `[...log, ...events]`, **awaits a disk write,
and only then sets the log.**

    _persistCrossing  →  log + [downed]        starts the write
    _endFight         →  log + [ended, …]      reads the SAME log

**Last writer wins, and `downed` is not in it.** A fight-ending blow fires
exactly those two, in one tick.

> **⚠⚠ AND `dialogue.choice-made` SURVIVED FOR THE REASON IT LOOKED LIKE A
> COUNTER-EXAMPLE: nothing else appends in that tick.** `Tester`'s
> discriminating experiment was right about the filter and right about the
> ordering, and could not see past the seam **because both appends succeeded.**

## ⚠⚠ AND TWO WIDER FIXES BROKE TRAVEL BEFORE THE RIGHT ONE

**1 · A serialising queue.** Every append chained onto the last. `whole_loop_test`
stopped travelling — `_enter`'s `await` then waits on a future created in
another async zone, and under `flutter_test`'s fake-async it never resumes.
**Every append still completed**, which is the shape of a zone-crossing stall
rather than a deadlock.

**2 · Extending `main._log` before its own `await`.** Removes the window
entirely and is the shape I would defend on paper. **It breaks travel too, and I
have not explained why** — bisected to that single assignment, with the rest of
the body unchanged.

> **A half-understood change to the save path is not one to ship**, so neither
> did. The race is real, proven in a unit test that models both shapes, and
> **still there for any other pair of appends.**

## What shipped instead: one append, not a lock

`_persistCrossing` buffers when the fight is over, and `_endFight` and
`_leaveScreen` carry the events out **with** the outcome. **The fight-ending
tick makes ONE call, so there is nothing to race with**, and `PT-1421`'s order
is kept — the blow that put you down, then the outcome that stood you up.

## ⚠ AND THE CROSSING WRITER IS NARROWED TO THE KINDS THAT HAD NO WRITER

`no_revive_after_death_test` went red the moment it landed: **one death recorded
twice**, because `_writeOutcome` already writes `died` and `revived`.
`PT-1421` is *one crossing, one event*, and two writers for one kind is the same
defect pointing the other way.

**⚠ AND `_writeOutcome`'s SITE IS STILL WRONG FOR `died` AND STILL NOT MINE TO
MOVE.** Its own comment admits it writes **one per FIGHT** — which is why
`PT-1618` moved `downed` — **but the outcome site also covers a death by
BLEED-OUT at round end, which no strike produces and which `Fight.advance`
currently drops.** Moving `died` without that is trading a duplicate for a loss.

## ⚠ AND `Tester`'s STRUCTURAL BOUND IS NOW A CASE

`pools.dart` makes an enemy `current > 0 ? standing : dead` and never `down`, so
**the player's swing can never produce a `downed` at all.** The enemy hitting the
player at exactly zero is the whole population, and both halves are asserted.

---

# ⚠⚠ `PT-1629` — `scripts` RETURNS, AND MY REASON READ AN ABSENCE AS PERMANENT

I wrote *"there is no script concept, so the row was a heading over a thing that
cannot exist."* **`PT-1341` had already ruled scripts a tab inside Loom with an
LSP outside** — planned, not impossible — and Aurora's three roots are areas,
conversations and scripts.

> **A root RESERVED is a different thing from a root INVENTED.**

    ▸ areas
    ▸ conversations
    ▸ scripts
        not built yet — PT-1341 gives them a tab inside Loom with an LSP
        outside it, so this is a root held open rather than a kind that is
        missing

**⚠ It says what it is rather than sitting empty** — `PT-1500` exactly: a row
that cannot list SAYS SO, and does not say there are none. **And it does not
reopen `PT-1609`:** blueprints stay in the palette, and a script is neither a
blueprint nor a placement — the same reason a conversation keeps its own root.

**⚠ AND IT IS THE THIRD CHANCE AT THE GUARD SPLIT THAT BIT ME TWICE ON SCREEN,
AND IT TAKES NO CALLBACK AT ALL.** There is nothing to guard and nothing to
forget: the row has no verb, because there is nothing yet to do to it.

---

# ⚠ AND `PT-1628` IS ACCEPTED WITH NOTHING TO DO

The slot stands and stays empty. `PT-1366`'s drawn set at that standard is what
changes it.

---

# STILL OPEN

**The `_append` race, for every pair that is not a fight-ending blow** — real,
reproduced, and unfixed because both general remedies break travel · `died`'s
writer is still at the outcome and bleed-out deaths are dropped by
`Fight.advance` · `character.downed`'s `campaign` lifetime · the drawn icon set ·
`§5` has no second interaction the product can reach · the two deferrals in
`STATE.md`.
