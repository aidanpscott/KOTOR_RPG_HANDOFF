# BUILD 132 — something finally spends a reaction

`ACTION-ECONOMY-01 §10`. `BUILD 131` ended with *"§10's opportunity attack has
a pool to draw on now and still no trigger."* This is the trigger.

---

## 1 · ⚠⚠ THE FIRST REACTION SPENT OUTSIDE A CONVERSATION

> *"They exist. They are universal. They draw on the reaction pool.
> **Trigger:** an enemy **leaves your melee reach on foot** while you can see
> them. **Effect:** one `Strike` at no penalty. **No chain applies.**
> **Prevented by:** the **Disengage** action."*

**⚠ *"NO CHAIN APPLIES"* IS WHY THIS ONE COULD BE BUILT AND THE OTHERS CANNOT.**
Parry, Snap Shot and Overwatch are in `ATTACKS-01` and in **no extract**, so
every other reaction waits on content. `§10` waits on nothing — `PT-1675` made
the pool non-empty, and no feat gates it.

Three layers, and the split is `ENGINE-INTERFACE-01 §4`'s:

| | |
|---|---|
| `leavesReach(was, now, reach)` | `Lodestar` — `was <= reach && now > reach` |
| `Fight.opportunityAttacks` | the rule: sides, droid, sight, Disengage, the pool |
| the play screen | the board, as before-and-after callbacks |

### ⚠ At reach is INSIDE it

`was <= reach`, because the square you can be hit from is the square you are
threatened in — the same boundary `strike` refuses past, and what gives `§15.1`'s
reach weapon its entire value. **A mutation to `<` fails one case and only one.**

### ⚠⚠ Closing provokes nothing, and a symmetric test gets it exactly wrong

`§4`: *"Opportunity attacks trigger on an enemy **LEAVING** melee reach. Nothing
triggers on an enemy **CLOSING**. That is deliberate and it is D&D's own line…
melee gets zone control and ranged gets range."*

> **A `was != now` test passes every other case in the group and inverts this
> one.** It is pinned separately for that reason.

### ⚠⚠ The blow lands at the distance it STARTED from

The opposite of `enemyTurn`'s choice, and not an inconsistency. That one measures
where a creature **ended**, because it moved and then swung. This fires *because*
the mover left: **at the ending distance they are out of reach by definition**,
so resolving there makes `strike` refuse every single time — a rule that can
never fire. You hit them as they go.

### ⚠ The clauses are ordered by cost, and that ordering is load-bearing

`spendReaction` is the only clause with a side effect, so every free question is
asked first. **A droid, an ally, or somebody who never left reach must not be
charged a reaction for a swing they were never going to take** — and the mutation
that moves the spend to the top fails four cases.

### ⚠ A watcher holding a gun strikes unarmed

`§10`'s effect is one `Strike`; `§1` makes `Strike` the melee default and a
blaster cannot make one. **`unarmed` is already this file's word for *no melee
weapon in hand***, so it is reused rather than a pistol-whip being invented.

### ⚠⚠ Droids make none — `§4`, and the corpus already found the mirror

> *"An opportunity attack is one `Strike`. `Strike` is melee. Melee is closed to
> every droid chassis… **⚠ Found in play, not in review.** A scenario printed
> five reaction uses across four enemy droids and **not one was spendable under
> any circumstance.**"*

Building `§10` without this clause prints that defect pointing the other way.
`Present.kind` has answered *is this a droid* since `PT-1490` and
`TARGETING-01` reads it; **the droid clause asks the same field rather than
inventing a second notion of a droid.** The player is in the list too, so a
droid **player** is gated and not merely enemies.

### ⚠ Sight's fourth caller, and it is not `_sees`

`§19.5` makes a watcher *unaware* of someone they cannot perceive, and Hidden is
the first way it lists — so this asks `_sees` **plus** *is the mover concealed*.
**Folding concealment into `_sees` itself would make `PT-1686`'s detection
quietly stop finding hidden creatures it is explicitly meant to leave alone.**

## 2 · ⚠⚠ DISENGAGE SHIPS WITH IT, NOT AFTER IT

`§10` names **exactly one** counter and it did not exist. Neither did any other
`§1` Action but Attack.

> **A trigger built without its only preventer is a rule that can only ever be
> suffered.** This corpus names *an exception that outlives its exception*; this
> is its twin — **a rule that arrives without its own.**

`Budgets.disengage()` spends the Action and sets the flag **only if that
succeeded** — set-then-pay is a free Disengage, which is `§10` deleted rather
than countered. It dies at the next `startTurn`, because `§1` says *your*
movement, meaning the turn that bought it. **`d` on the play screen**, beside
`f`/`m`/`i`/`space` — the first Action in the product that is not Attack.

## 3 · ⚠ AND THE REACTION PIP COULD NOT SHOW A SPEND

`budget_strip` drew `left: reactionsLeft, total: reactionsLeft` — **the same
field twice**, so the row was always full and a spent reaction showed as one
fewer star with nothing to compare it against.

**It could not be wrong until now.** Nothing outside a conversation spent a
reaction, and a counter that never moves cannot misreport a move — the same
shape as `PT-1540` finding *a spent pip goes grey* unreachable for the Action.

`Budgets.reactionsMax` is the denominator, re-seeded in `Encounter.begin`
alongside the pool. **Nothing reads it to decide whether a reaction may be
spent** — it is the denominator of a sentence, not a rule. And the pip now
disappears at zero **max** rather than zero **left**: no allowance means no pool
and no slot; an emptied pool **exists** and `PT-1517` wants that drawn grey.

## 4 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| `was <= reach` → `<` | 1 |
| any change of distance provokes | 1 (the closing case) |
| Disengage ignored | 1 |
| Disengage set before it is paid for | 1 |
| Disengage survives the turn boundary | 1 |
| droid clause dropped | 1 |
| sight clause dropped | 1 |
| sides dropped | 1 |
| the reaction is spent first | 4 |
| watchers in reverse order | 1 |
| the blow resolves at the ENDING distance | 1 |
| the step never calls it | the acceptance |
| **the snapshot taken one line too late** | the acceptance |
| the `d` key does nothing | 2 |
| the pip's total goes back to `reactionsLeft` | 2 |
| the pip is guarded by `reactionsLeft` | 1 |

### ⚠⚠ AND ONE OF MY OWN TESTS WAS VACUOUS, WHICH IS THE POINT OF DOING THIS

*"An ally leaving your reach provokes nothing"* passed — **and the mutation that
deletes the side check passed it too.** The trooper had the bed's default pool of
**zero**, so what silenced it was affordability, not sides. Rebuilt with a
control case directly above it — the same geometry, the same pool, the same
sight, **only the side differs** — and the mutation now fails.

## 5 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 579 | **595** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 456 | **473** |
| | 1,299 | **1,332** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 6 · ⚠ Not done, named rather than skipped

- **⚠⚠ THE ENEMY HALF IS BUILT AND CANNOT FIRE ON ANY BOARD THAT EXISTS.**
  `enemyTurn` only ever **closes** — `if (away > want.within)` — and closing on
  your only target never leaves that target's reach. An enemy leaves a reach
  only when moving toward a *different* party member, and **the party is one**.
  The wiring is there so the rule is not remembered onto the second path the day
  a companion exists; it is exercised by nothing but its own construction, and
  that is stated rather than implied. **Worth a `TEST` pass the day companions
  land, not before.**
- **The PATH is not read.** Two endpoints, so a creature that starts outside a
  reach, walks through it and ends outside provokes nothing. The player's step is
  one square, so **for the player the endpoints ARE the path** and it is exact.
- **Forced movement.** `§10` says *on foot*; `§19`'s knockback is unbuilt and
  must not provoke when it lands.
- **The other eleven `§1` Actions.** Dash, Dodge, Aid, Hide, Ready, Scan, Slice,
  Treat, Repair, Improvise and Use the Force-as-Attack are still unbuilt.
  Disengage is here because `§10` required it, not because the menu arrived.
- **Reach weapons.** `§15.2`: *"reach is not a data-layer concept in KOTOR…
  entirely ours to author"*, and nothing authors it — so every threatened area
  is one square. Read through `reachSquares` rather than written as `1`, so the
  day a Force pike exists there is one argument to change.
- **`Ready` is still the ranged answer nobody has used** — `§4`'s own note, six
  scenarios and zero uses, *"a discoverability problem, not a rules gap."*
