# BUILD 122 — looting: the token goes, a pile stays, stepping on it takes it

`PT-1525`. The marker question first, because the answer was not the one the
ruling records.

---

## 1 · ⚠⚠ THE MARKER PART HAD STOPPED BEING TRUE — A REGRESSION, NOT NEW WORK

**Asked of the code rather than of the ruling, and it failed.** I killed a
creature on a real board and read what the renderer was told:

    CONCEALED: {}          ← nothing hidden
    AFTER STEP: a01-command-deck · 1, 0   ← the square IS walkable

So half the rule held and half did not. `_stillHere` removes a dead creature
from `_here` at both moments one can die — it is not bumped into, not in the
fight, not in the panel, and its square is vacated. **And its token was still
being painted on the square it died on**, under the player's own marker.

> **`_here` is not what draws.** `Lens` paints `area.contents` — the FILE's
> placements — and skips only what `concealed` names. And `concealed` was built
> **by iterating `_here`**:
>
> ```dart
> Set<String> get _concealed => {
>       for (final p in _here)
>         if (_concealedThing(p.placement)) p.placement.tag,
>     };
> ```
>
> A creature removed from `_here` **can no longer be named there.** The filter
> and the renderer could not both be right, and the one that was wrong was the
> one nobody had asked.

⚠ **The rule was applied to the list that decides who ACTS; the board draws from
the list of what EXISTS.**

### ⚠ And the test could not see it, for the reason that keeps costing us

`nothing_dies_test`'s case *"⚠⚠ AND A DEAD CREATURE LEAVES NOTHING"* builds its
own list, in the test file, from `stateOf` — **`_stillHere`'s predicate,
re-implemented** — and asserts that the dead one is not in it. It proves
`stateOf` answers `dead`. **Nothing had ever asked the board.** Green
throughout.

**A rigorous check aimed at the wrong subject.** The case is kept and now says
what it does not cover and where that is covered instead.

**The fix:** the fallen come from the log, which is the one place that still
knows. `character.died`'s subject is the placement TAG — `combatantFrom` is
given `tag: p.tag` at the seam that builds a combatant — so a death names
**which** trooper died rather than which kind.

## 2 · ⚠⚠ REMAINS ARE A PROJECTION, AND THAT IS FORCED

`PT-1521` ruled a dead creature leaves nothing on three blockers. `PT-1525`
found all three block the **placeable** path and *KOTOR abandoned that path* —
`RancorCorpse` and `KraytCorpse` ship with zero placed instances.

**⚠ One of the three still stands and decides the shape:** `AREA-FORMAT-01 §4`
bars the engine from editing a package. So **nothing is written into
`[[contents]]`**, and a pile exists because the log says a creature died there
and does not say its things have been taken. `PT-1525`'s own line: *"it is
runtime state `PLAY-STATE-01` already projects."*

```
Remains  tag    the PLACEMENT that died — not the blueprint's handle
         where  the area and the square it STOOD on
         holds  item blueprint paths still in it
```

### ⚠ The square is the DEATH's, not the placement's

`ENGINE-SPEC-04 §4` writes no position during a round, so a creature a doctrine
walked died somewhere its file never mentions. `character.died` now carries `x`
and `y`. **A death written before it did falls back to the authored square** —
the best answer available, stated rather than silently exact.

## 3 · ⚠⚠ ONCE LOOTED IT DISAPPEARS — ONE PREDICATE, BOTH RULES

The owner asked me to pick and say why.

| | |
|---|---|
| a creature that carried nothing | **no pile, ever drawn** |
| a pile that has been emptied | **no pile, no longer drawn** |

**An empty pile IS an empty pile**, whichever way it got that way. Drawing one
after looting but not before would be the board contradicting the owner's own
rule, and a marker whose only remaining meaning is *you already looted this* is
a memory aid, not a fixture.

**⚠ And it is the answer that needs no second state anywhere.** *Stays, empty*
requires a stored flag, and a flag would have to persist — which is the thing
`§4` will not let us write into a package and a projection gets for free.

**⚠ THE COST, NAMED:** a square you have looted and a square where nothing died
look the same. That is the whole of what is given up.

## 4 · ⚠ THE VERB WAS ALREADY THERE, AND SO WAS ITS PRICE

A player's only gesture on the board is **step**, and it already means three
things by where you step: into a creature talks or fights, onto a door travels.
**A pile is the fourth.** A pick-up key would be a second affordance on a board
with one.

**⚠⚠ `ACTION-ECONOMY-01 §5` NAMES IT.** Its six free interactions are *draw or
stow · open or close an unlocked door · drop · **pick up** · hand over · speak*.
So the open question *loot mid-fight or only after resolution* **was already
answered by a document**: picking up is a free interaction, and a free
interaction is a thing you do on your turn. Nothing was invented.

> **⚠⚠ AND IT MAKES `§5`'s SECOND SENTENCE REACHABLE FOR THE FIRST TIME.**
> `_interactionToll`'s own comment records that *"no second interaction is
> reachable, and neither sentence below can print"* — speak cannot be taken in
> a fight and a door abandons the fight that holds the counter. **Two piles
> inside one turn's movement is a second interaction that does not end the
> round.** The machinery kept for that day now has a caller.

## 5 · ⚠ WHAT THE LOG RECORDS — ASKED BEFORE ASSUMING A SHAPE

`item.acquired`, one per item, `campaign` lifetime, **declared in
`EVENT-KINDS-01` since the vocabulary was written and emitted by nothing until
now.**

```
subject  the looter
item     an item blueprint PATH — PT-1452 makes [equipment] a path ALWAYS
from     the pile's placement TAG
area     where
```

**⚠⚠ A TRANSFER IS ONE EVENT.** An `item.lost` for the corpse beside it would be
**two writers for one crossing** — `PT-1421`, the defect `PT-1626` paid for. The
acquisition carries `from`; what is left in the pile is **derived**. Store the
choice, derive the consequence.

**⚠ `item.lost` gets no constant and no fold either, deliberately.** Nothing
takes an item away yet, and a fold for a kind nobody writes is exactly
`PT-1523`'s `character.moved` — declared, folded, emitted by nothing, zero
occurrences across seventeen saves, passing both drift checks that existed.
`check_event_producers` was built to see that shape.

**⚠ `PT-1266`, minded: single log, single writer.** `_take` puts the events in
`_log` and hands them **up**; it touches no file. And it goes through
`_persist`, which asks the vocabulary — `_persist`'s own comment says *every
persist site in this app ignored `SAVE-LOAD-01 §4` in favour of hand-picking its
own kinds*, and writing `onAppend` directly here would have been that again in
the slice that quotes it.

## 6 · ⚠ TAKE-ALL, AND THE TWO DECISIONS ARE ONE DECISION

A chooser has to offer *leave this behind*, and then it has to be able to show
you what you left — **which is the empty pile the owner has already ruled out
drawing.** Take-all is the reading that needs no second state. Named as a
choice: the day an inventory has weight or a limit, a chooser is what that
change is for.

**⚠ Re-interacting with looted remains** — the third open question — falls out:
there is nothing to re-interact with, and the square is an ordinary square.

## 7 · What a player sees

    droid.command-deck.50 falls — Vibroblade · rolled 15 … character.died
    a01-command-deck · 1, 0 · took hold-out-blaster
    carrying — hold-out-blaster
    arrows to move · m map · i carrying · esc to leave

**⚠ A LINE, NOT AN INVENTORY SCREEN, AND THAT IS NAMED AS A LIMIT.**
`INVENTORY-01` does not exist: nothing weighs an item, stacks one, equips one
from a pack or sells one. **A screen implies every one of those**, and building
the frame before the rules is how a surface comes to promise what nothing behind
it can do — `PT-1517`'s rule about a pip for a budget nothing spends.

The pile is drawn by `Lens` as **its own kind of object**: a low squat body on
the floor of the cell, in its own colour. A token is a disc with a letter, an
arrival a square with a name, a door a square with a bar — it shares no shape
with any of them, and `UI-STYLE-VALUES-01 §1` gives every accent exactly one
meaning, so borrowing one would have made that token ambiguous.

## 8 · ⚠ Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the fallen are not concealed *(the regression, restored)* | both board cases |
| the board is not told about piles | the pile appears |
| the death records no square | the death's payload |
| stepping on a pile takes nothing | the take, the line, the carry |
| the take is not persisted | it reached the writer |
| `_carried` built AFTER `_stillHere` | **only** the unlooted-reload case |
| `from` carries the blueprint kind, not the tag | both take cases |
| an emptied pile stays *(in Lodestar)* | the empty rule, and the two-pile case |
| a creature with no carry still makes a pile | the no-marker rule |
| Lens draws at every square / draws nothing | the pile's place, the cull |

**⚠⚠ AND TWO OF MY OWN CASES WERE VACUOUS AND WERE REWRITTEN.**

- **Lens's cull test** sampled square `0,0` to ask whether an out-of-bounds pile
  had reached it — **which no pile would have reached in any case.** It passed
  with the bounds check deleted. It now samples the square the pile would land
  on.
- **The app's "reload"** pumped a second `PlayScreen` at the same position, so
  Flutter kept the `State` — and `_log` is `late final … = [...widget.log]`,
  **initialised once.** The reloaded screen went on holding the log of the
  session that had just looted. Caught because a toggle stayed toggled. It now
  carries a `Key`.
- **`_carried` from the filtered list** is caught by exactly one case: the
  **unlooted** reload. The looted one cannot see it, because there the pile is
  meant to be gone either way. That case exists because the mutation did not
  fail without it.

## 9 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 515 | **527** |
| `Loom` | 252 | **252** |
| `Lens` | 7 | **10** |
| `KOTOR-RPG-APP` | 405 | **409** |
| | 1,179 | **1,198** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing and both in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins, all level.
`check_event_producers.py`: *every kind a projection folds, something writes.*

## 10 · Not done, named rather than skipped

- **A creature that WALKS before dying is untested in the app.** `_fellAt`
  prefers `_movedTo`, and producing the case needs a doctrine-driven walk ending
  in a one-blow death. The fold's half is tested in `Lodestar`; the screen's
  half is not.
- **Only `[equipment]` is looted.** A creature has no carried-but-unequipped
  inventory in `AUTHORED-CHARACTER-01`, so a pile holds what the creature wore.
- **Nothing can be equipped from what you carry**, and nothing can drop it.
  `item.lost` waits for its first producer.
- **A pile on a door square loses its sentence.** Stepping there loots and then
  travels, and arrival rewrites the status line. The item is taken and logged;
  only the word is lost.
- **`campaignKinds` defaults to `const {}`** and a caller that omits it writes
  nothing and says nothing. Documented on the field, so it is stated rather than
  silent — but it is still a default that fails quietly.
