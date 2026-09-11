# BUILD 133 — the backlog I had never read

Eight rulings had been sitting unread on my own list for slices. I read them
before picking work, and three of them were live defects with nothing blocking
the fix.

---

## 1 · ⚠⚠ `PT-1637` — A WALL WAS AN OFF SWITCH

> *"A wall is not cover in this build, it is an OFF SWITCH. A creature behind a
> three-square wall is permanently inert and so is the fight — it stood at 13 of
> 13 and the creature at 60 of 60 and neither could act, and **any authored area
> with a pillar in it can produce this.**"*

`approach` was a **greedy Chebyshev descent**: every step had to be strictly
closer. A creature whose nearer neighbours were all wall had nowhere legal to
go — *"an open three-step route inside a five-point budget, and it did not move
one square, because the first step of it is sideways."*

### ⚠⚠ MY OWN COMMENT ARGUED AGAINST FIXING IT, AND THE ARGUMENT WAS HALF RIGHT

> *"Inventing A\* here would be inventing a rule about what a creature knows
> about a room."*

**Greedy descent is equally an invention** — no more support in the corpus
(there is no pathing rule anywhere in it; I searched) and the additional
property of **looking like a bug**. The choice was never between a rule and no
rule. It was between two inventions, and one of them stops the fight.

### ⚠ So the knowledge is bounded by a number the rules already give

A **uniform-cost search over movement points**, limited to what the creature can
spend this turn: *it routes around what it could walk around now, and sees no
further than its own legs.* `ACTION-ECONOMY-01 §1`'s speed is the horizon, so
**no perception rule is invented.**

**⚠ COSTS RATHER THAN STEPS**, because `PT-1513` doubles difficult ground and a
search on step count routes a creature through the swamp to save a square and
then cannot pay for it. Pinned by a board where the longer way round is the
cheaper one.

**⚠ AND ON OPEN GROUND THE CHEAPEST ROUTE IS THE STRAIGHT LINE**, with the
greedy walk's own tie-breaks kept — so **every board that used to work walks
identically**, which is what the existing bed asserts square by square. The
difference is confined to the ones `PT-1637` filed.

### ⚠⚠ The two stalls are exact now rather than guessed

*Out of movement* is a **budget** fact and *nothing it can walk gets it closer*
is a **board** fact. The only honest way to tell them apart is **whether more
movement would have helped** — a question about squares it cannot afford. So the
search looks a little past the budget to answer it and **walks to none of them.**

> **TWO CHEAPER ANSWERS WERE WRONG AND BOTH LOOKED RIGHT.** *"Any square was
> rejected for cost"* calls a walled-in creature **out of movement**, because a
> bounded search hits its budget edge in every direction including behind
> itself. *"An unaffordable square is CLOSER"* fails the case the whole change
> exists for — **the first step of a way round is not closer.**

Both were written, both passed most of the bed, and both were caught by an
existing case rather than by review.

## 2 · ⚠⚠ `PT-1645` — THE ROW A PLAYER READS BEFORE CHOOSING

Two defects in one line, and the ruling had already settled the first.

### The header named the area the session began in

`PT-1641` located it exactly: `_entry` is assigned **on opening a save, on New
Game, and on Play from the hub — never during play**, and `PlayScreen` travels
without telling `main`. So the header **lagged by however many areas you
walked**.

> `Continue` and `Load` read the LEDGER. The `Load Game` row reads the HEADER.
> **The row said `a05-probe-barrier` and loading it opened `a01-probe-room`.**

It is **the same expression the resume uses** now — position's area, then the
package's entry — rather than a second opinion that can disagree again. The
fallback is not a second source: it fires only when the ledger holds no position
at all, which is exactly when the resume falls back too.

**⚠ Asserted on the header, because the ledger half has been right all along.**
Reverting the one line reproduces `PT-1639`'s sentence exactly: `a01-command-deck`
where the ledger says `a02-starboard-hold`.

### And the detail was clipped at every window size

`PT-1645` found the cause in one word: **the name was `Expanded` and the detail
`Flexible`** — tight against loose — so *"a short name still claims its full
share and the long string is always the one that yields."*

**⚠⚠ AND THE FULL WIDTH WAS ONLY HALF THE FIX, WHICH I FOUND BY MEASURING
RATHER THAN BY REASONING.** With the two halves no longer competing the detail
gets **520 units and wants 648** — the panel is a fixed `200 × scale`, so
*"widening does not help because the panel does not grow"* is true of the row's
own share as well. It takes two lines.

**⚠ What was being lost is the UNIT**, which carries the meaning: `7 ho`,
`19 ho`, and `14` with nothing after it — *"could be minutes, hours or days, in
the field a player uses to answer which one was I just in."*

**⚠ MEASURED, NOT LOOKED AT.** `find.text` matches a widget's DATA and a clipped
`Text` still holds the whole string, so the test lays the same span out at the
width the row actually gave it and asks `didExceedMaxLines`. Both mutations —
back to one line, back to the `Row` — fail it.

## 3 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| back to strictly-closer steps | 4, including `PT-1637`'s own board |
| search on steps, not costs | 1 |
| never look past the budget | 4 |
| the off-axis tie-break dropped | 2 |
| the stall never says *out of movement* | 4 |
| the header goes back to the frozen `_entry` | the loop test, with `PT-1639`'s exact pair |
| the detail back to one line | 1 |
| back to `Row`, `Expanded` / `Flexible` | 1 |

### ⚠⚠ And two of my own tests were wrong before the code was

**The pillar board proved nothing at first.** A wall three deep on a four-row
board still has a strictly-closer route round it — the diagonals make it free —
so the mutation back to greedy **passed my headline test.** Rebuilt on
`PT-1637`'s own board, reconstructed from its sentence: every strictly-nearer
neighbour is wall and the open ones are all sideways. It fails the mutation now,
and there is a second case asserting that **about the board** rather than about
the walk.

**And the detour test asserted its own premise.** I expected the way round a
short wall to be LONGER than the straight line and it is exactly the same
length. **The test was wrong, not the walk.**

### ⚠ A third bed was wrong in the way that costs the most

An awaited `File.writeAsBytes` inside `testWidgets` **never completes** — fake
async does not turn real I/O — so the test **hung instead of failing**, twice,
with no output at all. Written synchronously now, with the reason in the file.

## 4 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 595 | **602** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 473 | **474** |
| | 1,332 | **1,340** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 5 · ⚠ Still unread by nobody, and still open

Reading the eight closed four of my own blind spots and opened three items I am
**not** taking without a ruling or a bigger slice:

- **⚠⚠ `PT-1638` — the diagonal keys do nothing, and it stranded a player.**
  *"An arrival with all four orthogonals blocked and two diagonals open floor. A
  player who arrives there cannot leave without starting a fight."* `approach`
  already declares the eight and the four as **one list and a subset of it**, and
  `PT-1588` rules diagonal adjacency — so the rule is settled and only the
  keyboard is not. **It needs four more keys and a decision about which**, which
  is `PT-1443`'s click-to-move territory.
- **`PT-1640` — species reaches the SPEED and not the ABILITY SCORES, off the
  same blueprint field.** *"A field read for one purpose and dropped for another,
  in one function."* Whether a blueprint's species should carry its ability
  adjustments is a rules question — `AbilityAdjustment` is three of six extracted
  — so it is named rather than guessed.
- **`PT-1653` — a clean package has no way to say it is clean.** *"`Tester Probe`
  at thirteen problems and `Endar Spire` at zero render as identical library
  cards"*, and the first sign of trouble is a warning band inside a room you have
  already entered. That is a design question about Console Home.
- **`PT-1652`** is explicitly *named rather than ruled* and needs nothing from me.
