# BUILD 129 — a shot needs a line, and so does the find

`PT-1694`, and `PT-1692` with it — which was filed while I was building and
authorises the gap I had named and declined to close.

---

## 1 · ⚠⚠ THREE CALLERS, ONE FUNCTION

| | |
|---|---|
| **detection at range** | a creature notices the player — `PT-1686` |
| **the find on approach** | the player notices a hidden one — `PT-1692` |
| **a ranged attack** | a shot needs a line — `PT-1694` |

> **A second copy would be a creature DETECTABLE through a wall it could not be
> SHOT through** — the rule applied to one path and not the next, in its most
> visible form.

**⚠ And one of them was a second copy until this slice.** `_detectAtRange`
built the `canSee` call inline with its own board predicate, and `_sees` built
it again for a shot. **My own comment claimed one answer and three callers
while the code had two.** Detection now asks `_sees`.

## 2 · ⚠⚠ A SHOT FILTERS THE CANDIDATES RATHER THAN REFUSING

The owner left the choice open. **Refusing wastes the turn:** a doctrine that
picks a target it cannot see and is then told no has spent `§1`'s Action on
something that was never possible, and the player watches a creature do
nothing with no explanation.

`enemyTurn`'s foe list is **already filtered by side** (`PT-1678`), so sight is
one more clause in the same list — and `decide` stays grid-free, which
`DOCTRINE-FORMAT-01 §3` requires. A creature with nothing it can see holds, and
says so.

**⚠ Contact is exempt everywhere.** `PT-1678`'s adjacency join and the player's
own swing are *already touching*; touching squares always see each other because
**there is nothing between them to ask about.** The player's path needs no gate
today for that reason — and when click-to-move gives a player a target they did
not step into, the selection is where it goes.

## 3 · ⚠ `PT-1692` — AND THE FIND DOES NOT SETTLE ON A WALL

*"A hidden creature behind a wall should not be findable by proximity alone any
more than an unhidden one should be detectable through one."* Same `canSee`, no
new geometry.

**⚠ `_settled` MEANS *ASKED AND ANSWERED*, AND A WALL IS NOT AN ANSWER.** The
find is settled once — passive means taking 10, so re-asking would give the same
number — but a wall is not a number. Step where you can see it and the passive is
taken then, **for the first time.** Settling on a wall would make it **a
permanent hiding place**, which is not what `§3b`'s total is for.

## 4 · ⚠⚠ `sees` WAS OPTIONAL, AND THE MUTATION SAID OTHERWISE

It was optional first, with null meaning *this caller has no walls* — coherent,
and every bed in the suite is an open field. A fight with no distances would be
broken; a fight with no walls is merely outdoors.

> **Then the mutation that removes `sees:` from the screen's call passed the
> whole suite.** The one real caller could stop asking and **nothing anywhere
> would notice.**

`PT-1593` made `squaresApart` required on this exact method for this exact
reason — *"the fight holds no positions and never has, so it could not have
checked a range even in principle."* **The fight holds no walls either.** A bed
with none says so in one line; a caller that forgot cannot. Required now, and
forgetting is a compile error.

**⚠ And `_sees` itself had no case** until detection was routed through it. The
wall test covers it now; before that, `_sees` could return `true` unconditionally
and the suite was green.

## 5 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| shots ignore sight | the holds case, and the looker/target case |
| the find ignores sight | the wall case |
| the screen forgets `sees` | **a compile error** — it could not before |
| `_sees` always true | the detection wall case |
| `_sees` ignores the board | the detection wall case |

## 6 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 566 | **566** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 449 | **455** |
| | 1,279 | **1,285** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 7 · Not done, named rather than skipped

- **An enemy that loses its line holds rather than repositioning.** With nothing
  visible `decide` has no target, so it cannot be told to close on one. That is
  AI behaviour and unruled; the honest floor is that it does not shoot through
  rock.
- **A creature already in a fight is almost always in line**, because that is
  how it joined. The out-of-line case arises only when somebody moves behind
  cover afterwards, which is why it has no play-level fixture — the fight-level
  cases cover the rule.
- **Force powers do not consult sight.** `power_target.dart` picks by distance,
  and `PT-1488`'s cast has the same shape a shot had. **Named as the next one of
  these, not built** — it is a different ruling's surface.
- **Faction nesting** stays blocked on the tree being extracted, pinned by a test.
