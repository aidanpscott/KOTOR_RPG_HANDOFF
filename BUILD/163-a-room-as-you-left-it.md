# BUILD 163 — a room as you left it, and a companion facing into it

---

## 1 · ⚠⚠ `PT-1841` — THE FORGETTING HAD A SENTENCE DEFENDING IT

`_enter` cleared `_movedTo` with this comment:

> *"⚠ AND WHERE ANYTHING WALKED TO IS FORGOTTEN WITH THE ROUND — `§4`. Leaving
> re-reads the file, which is the authoritative position again."*

**The second sentence is still true and the first was the behaviour.** `§4`
writes no position and bars the engine from editing the package, so the FILE is
authoritative about **where an author put somebody**. It says nothing about
where they walked — and treating that silence as an instruction to forget is
what put every creature back on its authored square every time a player stepped
through a door and came back.

**⚠ `PT-1525` HAD ALREADY ANSWERED IT FOR A CORPSE.** Same three blockers, and
that ruling found they *"block the PLACEABLE path"* only: a body needs none of
them because *"it is runtime state `PLAY-STATE-01` already projects."* A
position is the same kind of fact about the same creature. **Nothing is written
into the package here either.**

## 2 · ⚠ WRITTEN ON THE WAY OUT, AND ONLY WHAT MOVED

One `character.moved` per creature whose square differs from its authored one.
A creature standing where the file put it has nothing to record, and a row per
creature per crossing would grow the save every time a player walked through a
door — `PT-1526`'s *"two moments rather than every keypress"*, the same rule the
player's own crossing is already written under.

⚠ The fallen are not written: a dead creature is not on the board, and a
position for one would be a square nothing draws and something might still walk
into.

⚠ The projection lives in `play_state.dart` beside `areasKnown`, because
`handledByPlayState` already declares `character.moved`. A new set would be a
second declaration of one fact.

## 3 · ⚠⚠ AND A LATENT BUG HAD TO BE FIXED FIRST

The crossing's duplicate check was:

    _log.lastWhere((e) => e.kind == CharacterEventKind.moved)

**No subject filter** — exact while the player was the only subject that ever
moved in the log. Writing creature moves would have made an enemy's step the
`last`, missed all three comparisons below it, and **appended every crossing a
second time.**

**Found by asking what else reads this kind before writing it**, rather than by
watching the log grow. Both engine readers (`areasKnown`, `projectPlayState`)
already filter by subject; this one did not.

## 4 · ⚠⚠ WHERE A COMPANION LANDS

`_bringTheParty` took the first passable neighbour in `stepOffsets` order, which
begins **up-left**. An arrival is almost always on a room's edge — `§4·0` puts
one where a door lets you in — so the first passable square was usually **the
corner behind the player**, and a party arrived stacked along the wall it had
just come through.

The measure is the room's own geometry and needs no new field: **how far a
square is from the nearest edge.** The interior-most neighbour wins;
`stepOffsets` order breaks every tie, so `PT-1013` still holds and two
companions land in the same two squares on every load.

**⚠ IT IS A READING, SAID OUT LOUD.** Nothing rules where a follower stands on
arrival — `§3b`'s rings are about **following**, which takes over on the next
step. What is ruled is that it should make sense relative to where you came in,
and *away from the wall you came through* is the only direction the format
actually gives.

**⚠ ONE EXISTING ASSERTION MOVED WITH IT.** `BUILD 141`'s acceptance pinned
`(1,0)` — *"`stepOffsets`' first passable neighbour is up-left"*. It is `(1,1)`
now. **The assertion moved because the behaviour was asked to move**, and the
old square is written into the test so the change is legible rather than
silent.

---

## Tests

    Lodestar   727 pass   (positions_test +6)
    App        583 pass   (companion +2)

Both halves mutation-checked: removing the write fails the memory case alone;
restoring the raw `stepOffsets` order fails the landing case **and** `BUILD
141`'s.

`check_engine_pin` 4 compared, all level.

## Still open

- **`§2`'s character screen** — its entry is the **click**, `PT-1443`'s.
- **`Dash`/Hustle** unbuilt (`h` decided), so *Hidden disables running* has
  nothing to disable.
- **`Scan`, `Slice`, `Treat`, `Repair`** — unblocked by `PT-1843`, unbuilt.
- **The stealth field generator** — the rule is built; no item declares itself
  one.
- ⚠ **A flake, first sighting at `BUILD 162`**: `whole_loop_test` failed once
  inside a full run and passed alone and on re-run.
