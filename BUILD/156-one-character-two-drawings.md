# BUILD 156 — one character, two drawings, and they agree now

---

## 1 · ⚠⚠ `PT-1137` — A TOKEN IS THE SIDEBAR'S PORTRAIT

> *"Each occupied tile shows the same portrait already designed for the
> sidebar — **party or enemy, whichever applies** — rather than a plain marker,
> **so a token on the board and its entry in the sidebar are visibly the same
> character rather than two disconnected representations.**"*

**⚠ AND THE TOKEN ALREADY KNEW.** `board.dart`'s own comment said *"`PT-1137`
makes a token the sidebar portrait, and there is no portrait art, so this is a
disc and a letter"* — correct when written, and **incomplete once the sidebar
existed**: the portrait is still a placeholder circle, but it is an *edged*
circle, and the board drew every creature with the same edge.

    before   friend ●  foe ●        one edge, two creatures
    after    friend ●  foe ●        the sidebar's own colours, and a ring

There is still **no portrait art** — `UI-ASSETS-01 §2` records it as *"currently:
a filled circle"* and the sidebar draws exactly that. **So this is that same
circle**, which is why the two agree now and will still agree the day the art
lands.

**⚠ THE DECORATIVE RING CARRIES NOTHING**, which is the ruling's own
requirement: *"purely a framing device… rather than carrying state on its own."*
It is its own colour, because the edge says party-or-enemy and the emphasis says
selected — **a ring borrowing either would be a third thing quietly reporting
one of them**, and a case holds the three apart.

## 2 · ⚠⚠ TOLD, NOT READ OFF THE PLACEMENT — AND IT IS NOT STYLE HERE

`Lens` takes `hostile` as a set of tags, beside `concealed` and `movedTo`. The
usual argument is `PT-1551`'s — *"the renderer is TOLD, not ASKED"* — but this
one has a sharper reason of its own:

> **Whose side somebody is on is not a fact about the placement any more.**
> `PT-1745` lets a conversation recruit, so the file says who they **started**
> as and the log says who they **are**. A renderer that consulted
> `PlacedThing.role` would draw a recruited companion **red until the area was
> reloaded**.

`shouldRepaint` compares the set for the same reason revealing and moving
already do — **this file has been caught by that exact shape twice.**

## 3 · ⚠⚠ AND MY FIRST ASSERTION WAS WRONG IN AN INSTRUCTIVE WAY

I claimed the board's hostile set and the sidebar's enemies were **equal**. It
failed with a trooper on the board and not in the sidebar — **and both were
right.**

    the board     draws every enemy standing in the room, because they are
                  visibly there
    the sidebar   `PT-1124` — "enemies are not shown at all until they're
                  actually fighting you specifically"

So equality was never the claim. What matters is **containment and
disjointness**: the board may know about more, and it may **never** call a
friend an enemy. Both are asserted now, and the second is the one that would
catch a real defect.

> The two drawings share one source — `isParty` over `_here` — because two
> lists that can disagree eventually do (`PT-1468`), and the whole point of
> this ruling is that these two agree about one creature.

---

## What ran

    Lodestar   682 tests   exit 0
    Lens        13 tests   exit 0   (+3)
    Loom       263 tests   exit 0
    app        560 tests   exit 0   (+1)
    flutter build linux     built

Mutation-checked: telling the board nothing kills the agreement case; Lens's
own cases rasterise the token and compare the pixels rather than counting draw
calls.

## Heads

    Lodestar        f1c2cc0   (unchanged)
    Lens            e79bc06
    Loom            c14d92a
    KOTOR-RPG-APP   44e0e78
    MAIN_WORK       b5dbaf1   (unchanged)

⚠ `Lens` moved for the first time in a long while, so `Loom` and the app both
took the new pin.
