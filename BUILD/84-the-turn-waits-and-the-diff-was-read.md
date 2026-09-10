# BUILD 84 — the turn waits, verified on the screen; and the diff nobody had read

**864 green** — Lodestar 395 · Lens 7 · Loom 131 · app 331.

Lodestar `61e2849` · Lens `6b55219` · Loom `be9215c` · app `f453601`.

---

## ⚠⚠ 1 · `PT-1540` — VERIFIED ON THE SCREEN, NOT ON THE DIFF

`BUILD 82` built it. **This slice asked the question a player asks**, in a
running fight, on the real bed, with a real character:

> **After I swing, is my action pip grey ON A FRAME, and is my turn still
> mine?**

`turn_waits_test.dart`, five cases, all through `PlayScreen` with the keyboard:

    bright BEFORE            action 1 of 1     ⚠ THE CONTROL
    swing (arrow into it)
    grey AFTER, on a frame   action 0 of 1     ⚠⚠ PT-1537 CLOSED
    the prompt is still up   "space to end your turn"
    move survives            move 10 of 10
    gear survives            gear 1 of 1
    space → new round        action 1 of 1     the enemy answered on YOUR key

⚠ **THE SEMANTICS LABEL IS THE SCREEN, not a back door.** `_Budget` carries
`'action 1 of 1'` on purpose — *"the shape is the identity on screen and the
label is the identity to anything that cannot see one"* — and the pip's colour
is `left == 0` **in the same widget**, so the label and the paint cannot
disagree.

⚠ **THE CONTROL IS THE HALF THAT MATTERS.** Without *bright before*, *grey
after* would pass on a pip that was grey the whole time — **which is exactly
what `PT-1517` was.**

## ⚠⚠ AND `PT-1537` CLOSES, AND IT WAS NEVER A REPORTING FAILURE

`Tester` never saw a bright pip go grey across four reports. **The spent state
existed between two statements and never reached a frame**: the strike spent the
action, ended the turn, ran the enemy's turn and began a new round **inside one
keypress**.

> **A negative that could not be observed is not a negative.**

## ⚠⚠ AND THE SCREEN FOUND SOMETHING THE DIFF WOULD NOT HAVE

**THE GLOW IS UNREACHABLE IN PLAY.**

`anythingLeft` counts `!gearSpent`, and **`spendGear()` HAS NO CALLER IN THE
APP** — grepped both trees: `round.dart` writes `gearSpent` in `startTurn` and
in `spendGear`, `budget_strip.dart` reads it, and **nothing calls it.** The
screen offers no gear verb.

So however much a player spends, `anythingLeft` stays true and the prompt
**never reaches its lit form.** Proved on screen: action spent, all ten points
of movement walked off, and the line still reads `space to end your turn` and
not `⟩ nothing left — space to end your turn`.

⚠ **THE CANCELLABLE HALF WORKS AND IS THE HALF THAT MATTERS** — the prompt is
present from the first frame of the turn and space ends the turn whenever you
like, which is `STUDY 20`'s *"usable EARLY, because ending a turn with movement
in hand is a legitimate choice."* **What is missing is only the glow.**

⚠⚠ **AND THE TEST ASSERTS THE GAP, NOT A FIX.** Excluding gear from
`anythingLeft` would delete a real budget from `§1`; adding a gear verb is a
feature nobody ruled. **Neither is mine to choose. The day either happens the
case fails and says so** — an assertion that a thing is missing is the only kind
that cannot rot into a lie.

## ⚠ 2 · `PT-1534` AND `PT-1517` — BOTH CLOSED, BOTH SAID WITH THE SCREEN

**`PT-1534` — Strength 18 and the line names Dexterity 0.**

A Soldier with `STR 18`, `DEX 10` and a blaster rifle — `Tester`'s own case.
The player's own attack line, read off the screen, contains **`Dexterity 0`**.

> **Omitting a zero term reads as *counted-and-irrelevant*. A bare zero reads as
> *counted-and-nil*. Naming the ability reads as *this is the one that counts,
> and yours is average*.** The 18 is worth nothing to a rifle, and the line now
> says so instead of saying nothing.

**`PT-1517` — the reaction pip is gone, not grey.**

On the first frame of a real fight the strip shows **`move`, `action`, `gear`
and no `reaction`.** The control is in the same assertion: `action 1 of 1` and
`gear 1 of 1` are both found, so **a missing star is an absence and not an empty
screen.**

⚠ **AND THE POOL REALLY IS ZERO, WHICH IS A DIFFERENT FACT AND STILL TRUE.**
`reactionPool` returns `min(allowance, highestReactionTier)` and nothing
supplies a tier, so every player has none. **`reactionPool`'s own doc says zero
is a real answer** — *"a character with neither has no reactions at all."* What
was wrong was **drawing a slot for a pool that does not exist**, and that is
what is fixed.

## ⚠ 3 · THE TWO STALE EXTRACTS — THE DIFF, READ

`BUILD 83` found them and refused to re-stamp. **This is what the diff says.**

Both extracts re-run to a scratch path and compared against what was on disk:

    every value                  BYTE IDENTICAL — seven chassis, three
                                 first-level overrides, every score, every
                                 basis mark, every note
    the recorded digest          moved
    every `source` citation      shifted by EXACTLY +32 lines

⚠⚠ **THIRTY-TWO IS `PT-1489`'s BLOCK.** `## ⚠ THE EFFECT HALF NEEDS AUTHORED
COLUMNS — PT-1489` occupies lines **186–217**, exactly 32 lines, **above
everything either extractor reads.** It is `BUILD 63`'s measurement of the
effect columns — **prose and one summary table neither extract touches.**

> **Nothing an extract READS changed. What changed is where it is.**

⚠⚠ **SO THE STAMP WAS RIGHT NOW AND WOULD HAVE BEEN WRONG A DAY EARLIER.** Ten
`source` citations were pointing **32 lines off**. `PT-1483` and `PT-1474` are
both about a citation being *where it was decided* — **a silently wrong citation
is worse than an amber check.** Re-stamping without reading the diff would have
buried it; re-stamping after reading it **fixed ten of them.**

    check_extracts   current 34 · stale 1     (event_kinds, the deliberate one)

⚠ **AND `base-rules` DID NOT MOVE.** `gen_base_rules.py` re-run against the live
shelf — 22 of 22 kinds written, **directory identical byte for byte.** The
shipped package was never affected, so this was never a play-facing defect.

⚠ **WHAT NOBODY SAID:** the document was edited on **2026-09-09** and the two
extracts were not re-stamped in the same slice. **An extractor's citations are
part of its output**, so a prose insertion above a table is a re-run, not a
no-op. `PT-1410` already rules that *a fingerprint sees a source change and not
a broken read* — **this is the case that ruling describes, and it behaved
exactly as designed.**

## ⚠ ONE HARNESS FINDING, AND IT IS THE FLAKE CLASS AGAIN

Typing `stand aside` into the trooper's conversation **lost its first four
characters**: the box read `d aside` and the screen said *nothing here means
that*. The conversation opens on an async read, and **the settle before it was
long enough on this machine and not a wait.**

> **A settle long enough today is not a wait.** Fifth occurrence, fourth
> costume. Fixed by waiting for `Stand aside.` to be on screen before typing a
> character.
