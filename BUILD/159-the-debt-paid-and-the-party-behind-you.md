# BUILD 159 — the debt paid, 118 descriptions reunited, and the party behind you

---

## 1 · ⚠⚠ `PT-1832` — THE DEBT IS PAID, AND MY OWN TEST WAS THE FIRST TO KNOW

`EVENT-KINDS-01` now declares `party.waiting` and `party.following` at
`campaign`, beside `party.joined` / `.left`. `BUILD 158` pinned that debt with
a test **written to fail the day it landed**. It did, along with the 51-kind
count beside it. Both were watched failing; the debt test is deleted, exactly
as its own reason line instructed.

**⚠ AND THE DEFERRED ASSERTION IS NOW THE REAL ONE.** `companion_test` reads
`campaignKinds` off the installed shelf **the way `main.dart` does** — not a
set written in the bed, which would prove the bed and not the product — and
asserts the order reaches the persisted stream with its area and square, and
that following clears it there too. An instrument check sits above it: *if the
shelf did not declare the kind, every persistence assertion below would pass
vacuously.*

✓ `Tester` confirmed the same thing independently at `TEST 071`, across a
fully killed-and-relaunched process.

## 2 · ⚠⚠ AND `emitted` WAS SEVEN KINDS SHORT OF WHAT THE APP CONSTRUCTS

Its own comment says *"every kind this build can write."* It listed chargen and
dialogue only. `character.died`, `.moved`, `.revived`, `item.acquired`,
`encounter.began`, `.ended` and `party.joined` **have all been written by the
play screen for slices without appearing in it.**

    CHECK A HAS BEEN MEASURING 17 OF 24

and passed the whole time, because every one of the seven **is** declared — so
the gap cost nothing and proved nothing. Found by scraping `CharacterEvent(`
construction sites and comparing, rather than by adding two names to a list.

The list is `chargenKinds + playKinds + dialogueKinds` now. That also aims the
lifetime rule properly: *"every CHARGEN kind is permanent"* was written as
*everything emitted minus the two dialogue kinds*, which held only while
chargen and dialogue were the only writers.

**⚠ AND CHECK A WAS PROVED AGAINST A REAL FAILURE** — one row deleted from the
installed shelf, and it fired. It had never been seen to fail.

## 3 · ⚠⚠ `PT-1832` — 118 ORPHANED DESCRIPTION ROWS REUNITED

**Matched on the blueprint's own string, not on position** — the ruled method.
Position is what produced the damage, so re-using it would assume the thing
under test. Each row is searched for as a **prefix** of a real `.uti`
description, and **a match that is not unique is not a match.**

**⚠⚠ THREE INDEPENDENT CONFIRMATIONS, NONE OF THEM ASKED FOR.** Nothing told
the matcher where to look:

    118 rows resolve, and ALL 118 belong to items in ITEMS-09
    ITEMS-09's own header says "118 ROWS LIFTED OUT OF plot, device,
      sensor, clothing AND creature"
    ITEMS-09 carried 143 items and ZERO descriptions

`PT-781` moved the item rows and their description rows did not go with them.

**⚠ THE POPULATION WAS 149, NOT 182.** Thirty-three were never orphans: the
source cell on this project's own rows reads `⚠ AUTHORED`, not `AUTHORED`, and
a pattern accepting only a bare word **did not match those item rows at all**
— so their descriptions read as orphaned while sitting correctly under their
own items, 27 in `ITEMS-08` alone. **A check keyed to a SPELLING of its
subject, the fourth sighting in this corpus.**

**⚠ AND NINE MORE ARE THE KNOWN MULTILINE ROWS**, which `extract_items.py`
already documents. Not a defect.

**Left alone and named: 22** rows whose string several blueprints share. What
separates upgrade items with identical prose is the property text KOTOR puts at
the front of the same string, and where even that collides there is no answer
to act on.

Nothing is rewritten, only relocated — byte for byte, so a hand correction
inside one travels with it. The target row is found by its text and the match
is **asserted** unique, because line numbers move as rows are inserted. Then
the 116 moved rows were repaired for truncation too: they were orphans when the
repair last ran, so it had skipped them.

## 4 · ⚠⚠ `PT-1136` — `§3b`, AND THE PARTY WALKS BEHIND YOU

> *"One character is actively controlled at a time… Everyone else auto-follows
> the active character."*

**The mechanism is adopted, not invented.** `TRACE-36` found following in both
games is *"a persistent, native engine action using real pathfinding… never a
simple 'stay within some distance' rule."* So it asks `approach`.

**The formation is a system the source shipped and never switched on** — a
close ring at one tile and a second, farther ring for anyone who does not fit.
Read as **distances asked of `approach`** rather than eight reserved squares,
which is `§3b`'s own qualifier: a follower *"heads toward their formation slot
when there's room to."*

**The one gap the source left is answered.** Both games leave a completely
blocked follower unhandled — *"the developers' own shipped code for that exact
case is empty, with a comment asking themselves what should happen there."*
Ours says so and holds, and because the question is asked again every step it
**resumes the instant a path opens with nothing storing that it was stuck.**

**⚠ THE TWO FEATURES HAD TO MEET.** `PT-1122`'s *wait here* would mean nothing
if `§3b` dragged them along anyway, so a companion with a standing order is not
in the follow order at all.

## 5 · ⚠⚠ `Approached` GAINS `route`, AND THAT IS THE REAL FINDING

The first version gave the search a **one-point budget**, since a follower
moves one square per step of the leader's. But in `approach` **the budget is
also the horizon** — its own words, *"it can see no further than its own
legs"* — so one point cannot find a detour, because `PT-1637`'s finding is that
*"the first step of a detour is not closer."*

    A follower behind a pillar stood still.

**Precisely the greedy-descent defect `PT-1637` was opened to fix,
reintroduced one subsystem over.** Caught by the routes-round-a-wall case. So
the search runs to the whole board and only the **first square of the route**
is taken; `route` is additive and every existing caller is untouched.

**⚠ AND A FRESH `Budgets` IS A TURN THAT IS ALREADY OVER.**
`..moveLeft = horizon` produced a budget that **looked full and searched
nowhere**, reporting *out of movement* with 256 points in hand, because
`approach` reads `turnOver ? 0 : moveLeft`. `startTurn()` is what fills a pool.

**⚠ THE GROUND IS NOT PRICED.** `PT-1513` doubles difficult ground out of the
movement **budget**, and a budget is a turn. Outside a fight **the player pays
nothing for it either** — the step charges inside its `fight != null` guard and
nowhere else — so pricing a follower there would be a rule applied to one path
and not the next.

## 6 · ⚠⚠ AND MY OWN ACCEPTANCE TEST PROVED NOTHING, FOR ONE SLICE

It looked for `Zaalbar` on screen — **which the `PT-1804` sidebar prints
whether or not anybody moved.** Both halves passed on a board that had not been
asked anything. Outside a fight the *only* thing that reports a creature's
square is the refusal you get for walking into them, so that is what both tests
read now.

**A check aimed at the wrong subject, in my own test, one slice after naming
the class.** Worth the line: `PT-1804` made the old observable ambiguous and
nothing said so.

**⚠ AND THE SQUARE IS `approach`'s TIE-BREAK RATHER THAN MINE.** Two squares
were equally close and equally cheap; the search keeps the one **less
off-axis** — *"a creature lines up while it closes rather than drifting off the
row."* I guessed the diagonal and was wrong about my own board. Written into
the test rather than quietly corrected.

---

## Tests

    Lodestar   705 pass   (follow_test +8)
    App        572 pass   (companion +2, emitted_kinds −1: the debt test)

Analyzer clean on both; remaining infos are all pre-existing.
`check_shelf` ✓ 25 identical · `check_extracts` **stale 0** ·
`check_engine_pin` 4 compared, all level · gate **SENDABLE**, same two
pre-existing warnings.

## Still open

- **`§2`'s character screen**, behind `PT-1443`'s first-click question — and
  it is what `Trade / give item` is waiting for.
- **`PT-1108`**, the second combat interaction system.
- **The combat half of party control**, which `§3b` names as separate and
  still open — this slice is the exploration half only.
- **22 ambiguous description rows** and the **15 crystal rows** whose cell
  composes property text with the description.
