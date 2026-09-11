# BUILD 134 — the keyboard finally has eight

`PT-1707`, closing `PT-1638`. Four keys, and three of the four decisions in it
were not the keys.

---

## 1 · ⚠⚠ IT IS A STRANDING BUG, NOT A CONVENIENCE

> *"An arrival with all four orthogonals blocked and two diagonals open floor.
> **A player who arrives there cannot leave without starting a fight.**"*

**The rule was always eight-way.** `PT-1588` — *"diagonal costs 1 square,
diagonally touching is adjacent"* — and `stepOffsets` has declared the eight
beside `orthogonalStepOffsets`' four since it was written, *"so that the
difference is a fact in the code rather than a discrepancy between files."*

**⚠ A creature could approach on a diagonal and a player could not follow** —
the rule applied to one path and not the next, on the two paths that face each
other across a board. Each offset is read out of `stepOffsets` rather than
retyped, so the keys cannot drift from the list the walk uses.

## 2 · ⚠⚠ BY THE **PHYSICAL** KEY, AND THAT IS NOT A DETAIL

**NumLock decides what a numpad key reports.** With it off, the key under the
player's finger sends `Home`, `Page Up`, `End` and `Page Down` — not
`numpad7/9/1/3`.

> **A logical binding works only for players who happen to have NumLock on**,
> and this is a fix for somebody who is stuck in a room.

**⚠ AND THE PHYSICAL KEY IS THE PRECISE ANSWER RATHER THAN THE BROAD ONE.**
Also binding logical `Home` and `End` would capture the *separate* Home and End
keys elsewhere on the keyboard, which the ruling did not name.

**⚠⚠ AND I NEARLY SHIPPED WITHOUT THE TEST THAT PROVES IT.** Every other case in
the file sends the physical and logical keys *agreeing*, so **a logical binding
passes all of them.** The NumLock-off case — physical `numpad7`, logical `Home`
— is the only one that separates the two, and it is the one a real player meets.

## 3 · ⚠ THE HINT GOES ON THE REFUSAL, AND THAT WAS MEASURED

`PT-1478` is the precedent and it cost a slice: `play/` had zero mentions of
`power` and *"`Tester` tried nine keys before settling it in code."* **A binding
nothing on screen mentions is one only somebody who reads the source can use.**

So I put it on the permanent hint line, and **it broke seventeen tests.** The
line is at its width at 1280: one more clause wraps it to a second line and
**overflows the column by nine pixels.** `PT-1447` already said this screen has
no spare vertical, and I had to measure it to believe it.

**⚠ AND THE REFUSAL IS THE BETTER PLACE ANYWAY.** It arrives at the moment the
player is stuck and is silent every other time — *"the wall blocks the way —
numpad 7 9 1 3 go diagonally"*, and only when every orthogonal is shut.

> **⚠⚠ AND SILENT AGAIN WHEN NO DIAGONAL IS OPEN EITHER.** A sealed square has
> the orthogonals shut too, so a check that stopped there would name four keys
> that **do nothing**. `PT-1613` makes that a legal thing for an author to
> build: *"a creature nobody can reach is a locked room, not a defect."* **A
> refusal that suggests a key which cannot help is worse than one that says only
> what it knows.**

## 4 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the diagonals are not bound at all | 3 |
| numpad `1` and `3` transposed | 1 — the four-corner case, and only it |
| bound by the LOGICAL key | 1 — the NumLock-off case, and only it |
| the diagonal bypasses `_step` | 3 |
| the hint never fires | 1 |
| the hint fires on every wall | 1 |
| `_boxedIn` ignores whether a diagonal is open | 1 — the sealed square |

**⚠ A transposed pair reads correctly and moves a player the wrong way**, which
is why one key passing is not four keys working.

### ⚠ And the bed was wrong twice before the code was

**The box was not a box.** `[[arrivals]]` did nothing and the player started at
`(0,0)`, so four arrows *"refused"* by being off the board. `PlayScreen` takes
`startAt` and the bed says so now.

**And re-pumping `PlayScreen` is not a fresh screen.** Flutter reuses the
`State` of a widget of the same type at the same position, so the four-corner
case kept the player where the previous corner left them — `initState` never ran
and `startAt` was never read. A `Key` per mount. **This looked exactly like a
binding defect for one run.**

## 5 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 602 | **602** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 474 | **480** |
| | 1,340 | **1,346** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 6 · ⚠ Not done, named

- **`PT-1443`'s click-to-move still stands**, and the ruling says so: this is
  *"not a substitute"*. Three things still lean on it — the player's reach
  check, `PT-1584`'s eight-versus-four, and the soft-lock validator's
  four-offset reachability. **The second of those is closed now**; the other two
  are not.
- **An out-of-bounds step still says nothing.** `_step` returns early on a
  square off the board with no sentence, so pressing into the edge of a room is
  silent where a wall speaks. That is `PT-1610`'s shape — *an early return that
  hid something* — and it is one line, but it changes what every edge press
  prints and belongs in its own slice rather than smuggled into this one.
- **`PT-1640` and `PT-1653` stay named, not built**, per the owner.

---

# BUILD 134b — `PT-1708` and `PT-1709`, and the diagonals rebuilt on corrected geometry

## 7 · ⚠⚠ `PT-1708` — THE REACTION POOL WAS ZERO FOR EVERY PLACED CREATURE

`Tester` traced every external input and everything readable from outside said
`§10` should fire. **The reason it did not was not readable from outside**, and
its own report named the boundary correctly rather than crossing it.

I instrumented the clauses and ran them against `Tester`'s own
`ranged-detection` fixture:

    was=1  now=2  reach=1  sees=true  pool=0

**Every clause correct but the pool.**

> `combatantFrom` declares `int baseAttackBonus = 0` and builds
> `reactionPool(dexModifier, baseAttackBonus)` from it. **Its one caller never
> passed it.** A `DEX 10` guard has no Dexterity band, so its entire pool came
> from a ladder nothing supplied — `§10` fired, saw `reactionsLeft == 0`, and
> returned silently.

**⚠⚠ THIS IS `PT-1675`'s DEFECT ONE PARAMETER OVER, AND I REMOVED ITS TWIN
WHILE LEAVING IT SITTING BESIDE IT.** `BUILD 132` called `highestReactionTier`
*"declared, defaulted to zero, passed as a literal zero by its one caller, and
gating every reaction in the product"* — **and said nothing about the other
argument to the same call.**

### ⚠ And my bed hid it, for a reason worth keeping

The sentry had `dex = 14`, *"so the pool is not zero"* — **a Dexterity band
gives a pool without the ladder being supplied at all.** The acceptance passed
against a creature that could not exist in `Tester`'s fixture. It is a `DEX 10`
soldier now, and the seam is asserted directly beside it: a placed creature's
`reactionsLeft` must be non-zero when its class has a ladder and its Dexterity
has no band. **The mutation that restores the defect now fails both.**

### ⚠ The droid half — `Tester`'s question answered, not built

*"Whether melee-closed-to-droids is scoped to opportunity attacks only or is a
wider unenforced rule elsewhere."*

**It is wider, and three documents say so:**

| | |
|---|---|
| `ACTION-ECONOMY-01 §4` | *"An opportunity attack is one `Strike`. `Strike` is melee. **Melee is closed to every droid chassis.**"* |
| `CLASS-ATTACKS-01` | Battle · Assassin · Astromech · Remote — **RANGED ONLY**; *"`Power Attack` and `Strike` are melee and closed to it"* |
| `SPECIES-CHAPTER-v2` | Fixed Armature — *"a chassis reaches eleven ranged attack chains and **no melee at all**"* |

So `Tester`'s observation that *"the droid's own ordinary Strike also fires"* is
a **real unenforced rule**, and the opportunity-attack clause is one instance of
it rather than the rule itself.

**⚠ NOT BUILT, AND DELIBERATELY.** Enforcing it disarms every droid holding a
melee weapon — they would hold every turn — so the right shape is a **validator
fault at authoring time** (a droid blueprint with a melee weapon is
unplayable by the rules) plus the runtime gate, not a silent hold in play. That
is a design decision about Loom's `verify` and the package validators, and it is
the owner's.

## 8 · ⚠⚠ `PT-1709` — A DIAGONAL MAY NOT CUT A CORNER

**`canSee`'s own comment defended the leak**, and I wrote it:

> *"Two walls meeting at a diagonal do not seal the diagonal, which is what a
> player looking at the board expects of a gap they can see through."*

`PT-1703` found it and `TEST 060` proved it exploitable. It is **a hole in every
wall that turns a corner**, which is not what a player expects of one.

`diagonalIsOpen` is **one function with three callers** — sight, `approach`, and
the player's step. *Two separate rules that could drift apart again* is how this
corpus got a creature detectable through a wall it could not be shot through.

**⚠ It asks the TERRAIN, not passability.** Callers answer `passable` false for
an occupied square, and **a creature at a corner is not a wall** — two creatures
standing diagonally would otherwise wall each other in, which no rule says. So
`approach` takes `blocksCorner` separately, defaulting to `passable` so a bed
with no walls is unchanged.

### ⚠⚠ It narrows two things, and both are said out loud

**Contact is no longer exempt everywhere.** `PLAY-STATE-01` says touching
squares always see each other *"because there is nothing between them to ask
about"* — **and when both flanks are wall, there is.** Orthogonal contact is
untouched, and both halves have their own case.

**And `PT-1707`'s keys cannot rescue a player boxed by four WALLS.** Both flanks
of every diagonal are those same walls, so no diagonal is legal. **That board is
a sealed room**, which `PT-1613` says an author may build. The case `PT-1638`
actually found still works, and its own sentence is why: *"cannot leave
**without starting a fight**"* — a square held by a creature is **open
terrain**, so the corner beside it is not sealed. My original box walled all
four orthogonals and **was not `PT-1638`'s board at all**; rebuilt with a guard
holding one of them.

**⚠ The stranding hint asks the same question the keys ask**, so a refusal
cannot name a key that would do nothing.

## 9 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the base attack bonus is not passed through the seam | the seam case **and** the acceptance |
| the corner rule never applies | 3 |
| the corner needs BOTH flanks open | 4 |
| the player's step stops corner-checking | 1 |
| the hint ignores whether a diagonal is legal | 1 |

### ⚠⚠ AND ONE GUARD COULD NOT FAIL, WHICH IS ALSO A FINDING

`diagonalIsOpen`'s `if (dx == 0 || dy == 0) return true;` — deleting it broke
nothing, **and it cannot**: with `dy == 0` the two terms are the destination and
**the square being stepped from**, which every caller has already established is
open. It stays as the rule's SCOPE and **says in its own comment that it is not
a gate**, because `PT-1661` makes an untestable guard a defect and this one is
untestable by arithmetic rather than by oversight.

## 10 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 602 | **607** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 480 | **482** |
| | 1,346 | **1,353** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.
