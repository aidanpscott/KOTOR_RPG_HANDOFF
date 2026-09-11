# BUILD 128 — detection needs a line, not just a distance

`PT-1686`'s gap, the owner's follow-up. Plus two smaller items from the same
list.

---

## 1 · ⚠⚠ THE RIGHT NUMBER AND THE WRONG GEOMETRY

`TileType.blocksSight` has been on the vocabulary since `§2·0a` was written and
was **read by nothing.** `PT-1550`'s own note records the non-use as
deliberate — *"`wall.blocksSight` stays true and stays unread"* — because
`hidden` is an author's flag rather than a perception system.

**`PT-1686` made the absence a defect.** Detection compared a DISTANCE and
nothing else, so **a creature noticed the player through solid rock** at any
range under the radius.

**⚠ The board is the caller's** — `ENGINE-INTERFACE-01 §4` keeps the engine off
a world, so `canSee` takes a predicate exactly as `approach` takes `passable`.
**Off the board is not a wall**: a line that leaves the room is already
impossible, and answering *blocked* there would seal the edges.

**⚠ Contact needs no line.** `PT-1678`'s adjacency join is *already touching*.

## 2 · ⚠⚠ SYMMETRIC BY CONSTRUCTION, AND THAT IS A DECISION

A single Bresenham walk **is not symmetric**: for some diagonal pairs it clears
A→B and blocks B→A.

> **So *can I see you* and *can you see me* get different answers about the same
> wall — and the creature would detect the player from a square the player could
> not be detected from.** One question with two answers, in the worst place for
> it.

A line is clear when **either** traversal is. That also makes a corner
permissive: two walls meeting at a diagonal do not seal it, which is what a
player looking at the board expects of a gap they can see through. **Named as a
choice**; the strict reading would seal it.

**⚠ Swept, not spot-checked.** The symmetry case walks all 625 ordered pairs on
a 5×5 board of scattered walls, because **the asymmetric pairs are exactly the
ones a hand-picked example misses.** A single-direction mutation fails it.

**⚠ The endpoints are never asked about.** A creature standing in a doorway can
see out of it; asking about the origin would blind anything on a blocking square
and asking about the target would make it invisible. Neither is a sight rule —
both are an off-by-one.

## 3 · ⚠⚠ AND DETECTION WAS NOT EVALUATED WHEN A FIGHT BEGINS

Found while looking at the third item. `_detectAtRange` ran when the player
**stepped** and when an enemy **moved** — and a fight starts on a step that
**returns before the step's own call**, because walking into a creature is not
walking onto a square.

> **So a creature standing in range when the fight began was not detected until
> somebody moved afterwards** — and if the player won initiative, that was a
> whole round later.

**⚠ IT SURVIVED BECAUSE `_enemyTurns` DETECTS TOO.** In the bed the droids win
initiative, so the enemy loop ran and detection with it: **the gap was invisible
for exactly the fights the tests could start.**

## 4 · ⚠ `range` COMES OUT FROM BEHIND `hidden` — §3c CORRECTED

`§3c` read *"a `range` follows `stealth`'s rules: hidden only"* and the reader
refused one in plain sight. **That was right for the one reader it had:**
`range` existed for `PT-1573`'s find-on-approach, which only ever asks about a
creature that is hiding.

**`PT-1686` gave it a second reader** — detection, about **unhidden** creatures
— so *hidden only* stopped being a rule and became a limitation.

> **One number, read from whichever side is deciding.** *How far off it can be
> noticed* and *how far off it notices* are the same distance.

**⚠ `stealth` stays hidden-only.** A hiding total on something in plain sight is
two statements that cannot both be true — `PT-1379`.

**⚠ And Loom's control came out with it**, or it would be `PT-1379` inverted:
**the Builder unable to author something the reader now accepts.** The sentence
under the control changes with the placement.

## 5 · ⚠ THE FACTION RE-CHECK — NOTHING TO DO, AND WHY

Asked before building. `_wouldFight` reads `_hostile` **first** and returns true,
so a creature a conversation turned hostile joins whatever its faction says.
**That is `PT-1437` working**: the package said so explicitly, and a faction is
what happens when nothing has.

And it *is* re-evaluated: `_detectAtRange` runs on every move and `_wouldFight`
reads `_hostile` and `_myFaction` live, so a mid-fight defection changes the
answer for anyone not already flagged.

**The one thing not re-checked is a creature already IN the fight** — and
`PT-1687` is explicit that *"the gate is only at the moment of joining by contact
or range."* **Leaving a fight is out of scope by the ruling**, so there is
nothing here to build. What the look did turn up is §3.

## 6 · ⚠⚠ AND I MINTED A RULING NUMBER

I wrote `PT-1691` through the code, the tests and the document. **`PT-1508`:
*ruling numbers are the owner's to assign.***

`audit_rulings.py` blocked the gate with *"CITED BUT NEVER WRITTEN: PT-1691,
cited 2x"*. The slice has no number — it came from a prompt — so it cites
`PT-1686`, whose gap it closes, and says the follow-up was the owner's.

> **A standing constraint that only a check enforces.** The same check I had to
> repair two slices ago for going blind to a dash character.

## 7 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| one direction only *(asymmetric)* | the sweep, and the corner |
| nothing blocks sight | both wall cases |
| the endpoints are asked about | touching squares, and the doorway |
| detection ignores sight | the through-a-wall case |
| the range control back behind `hidden` | the settable case |

**⚠ And one mutation did not apply** — my anchor string was wrong, the assertion
threw, and I pushed before noticing. **Redone against the pushed code**, which
is the only version whose guard matters.

## 8 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 555 | **566** |
| `Loom` | 253 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 447 | **449** |
| | 1,265 | **1,279** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 9 · Not done, named rather than skipped

- **The find-on-approach still sees through walls.** `_lookAround` is
  `PT-1573`'s rule — noticing a HIDDEN creature — and it compares a distance
  with no line. It is the same defect one rule over, **and it is a ruled
  behaviour I did not have a ruling to change.**
- **Nothing else consults sight.** A ranged attack does not; `PT-1543`'s range
  bands are distance alone, so you can still shoot through a wall.
- **Faction nesting** stays blocked on the tree being extracted, pinned by a
  test that says so.
- **A creature that loses sight of the player stays in the fight**, which is
  `STUDY 32`'s deliberate answer — *"do not make visibility the membership
  rule"* — and `PT-1672` keeps its row. Recorded because it is the first thing
  sight makes somebody ask.
