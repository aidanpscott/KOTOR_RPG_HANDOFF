# TEST 044 — the barrier, and a screen that has never taken a pointer

**Built against:** the **same binary as TEST 043** — bundle `kernel_blob.bin` built
**16:11**, from app `660134a` → Lodestar `9aa73822c5022024b841b017445e978ad80c9227`.
`strings … | grep -c "PT-1626"` → **0**, `PT-1622` → 5.

⚠ **THE TREE HAS MOVED AND THE BUNDLE HAS NOT.** `KOTOR-RPG-APP` HEAD is now
`47789fa` and `pubspec.lock` now pins Lodestar `e1a837c`, but the bundle on disk is
still the 16:11 one. **I did not rebuild** — `flutter build` writes into Coder's tree.
So everything below measures `660134a`/`9aa7382`, and `47789fa`/`e1a837c` is untested
by me. The Lodestar source I quote is `~/.pub-cache/git/Lodestar-9aa7382…`, which is
the copy that binary was compiled from.

**Instrument:** PID-scoped. App PID `530450`, window `142606339`. Killed by PID;
Coder's Looms `517963`/`517968` survived, which is the control.

---

## 0. The barrier area, and the answer is worse than "it does not path"

I built `a05-probe-barrier` (12×5, wall at col 3 rows 1–3, `probe-anvil` at 4,2,
arrival at 5,2) — and I designed it from the source rather than by trial, because
`approach.dart` says exactly what will happen.

**`approach()` is not a pathfinder. It is a greedy Chebyshev descent**
(`Lodestar-9aa7382/lib/src/approach.dart:120–174`). Every candidate step must be
**strictly closer**, by the function's own comment:

    // ⚠ STRICTLY CLOSER. A sideways step is not progress and a loop of them
    // is how a greedy walk burns a whole budget going nowhere.
    if (nd > bestD || (nd == bestD && best == null)) continue;

So from `4,2` toward a player at `2,0`, `d = 2`, and the **only** neighbour with
`d < 2` is `3,1` — which is the wall. `4,1` and `3,2` are both `d = 2` and are
refused as sideways. `best == null`, and `couldWalkThere` is false because the one
closer square is impassable. **Predicted before running it, then observed:**

    probe-anvil.probe-barrier.02 nothing it can walk gets it closer ·
    probe-anvil.probe-barrier.02 cannot reach Barrier Tester — 2 squares, reach 1

⚠ **That is `fight.dart:215` on screen for the first time.** TEST 043 established
that `AttackReport.outOfReach` is dead; this is the sentence a player actually gets
instead, and it took an authored fixture to produce.

⚠ **And it is the BOARD stall, not the budget one.** `approach` has two, and they are
different sentences on purpose — *"out of movement `d` squares short"* is a budget
fact, *"nothing it can walk gets it closer"* is a board fact. This is the second.

### The mover does not walk around anything

`PT-1596` built the mover and nobody had watched it. **It did not move one square.**
The route via row 0 — `4,1 → 4,0 → 3,0` — was open, unoccupied, and three steps
inside a five-point budget. It stood still because the first step of it is sideways.

Second round, from further away, to show it is stable rather than a one-off:

    probe-anvil.probe-barrier.02 nothing it can walk gets it closer ·
    probe-anvil.probe-barrier.02 cannot reach Barrier Tester — 4 squares, reach 1

⚠⚠ **A creature behind a three-square wall is permanently inert, and so is the
fight.** I stood at 13 of 13 and it at 60 of 60, and neither of us could act. The
fight cannot end while I stay west of the wall. **A wall is not cover in this build;
it is an off switch**, and any authored area with a pillar in it can produce this.

**What I did not produce:** *"out of movement N squares short"*. It needs the target
to end at `d ≥ budget + 2`, and a fight starts at contact, so the largest gap a
player can open in one turn is `budget + 1 = 6`. TEST 043 measured the enemy's budget
at 5 by watching it close 6 → 1. Behind this barrier `d` never exceeds 4, because the
whole west region is within 4 of `4,2`. **I did not build a second fixture for it.**

⚠ **My fixture has a door back** (`door.probe-barrier.01` at 11,2 → a01, landing on a
new `from-probe-barrier` arrival at a01 3,1) **and I confirmed it by walking out.** I
filed a03 and a04 as one-way rooms; shipping a third would have been indefensible.

---

## 1. Continue reads the LEDGER. The list reads the HEADER. They disagree.

TEST 043 found `probe-walker.sav`'s header naming `a02-probe-hall` while its last
`character.moved` named `a03-probe-yard`, and did not test which wins. **Tested, twice,
on two characters:**

| save | header | last ledger move | Continue put me in |
|---|---|---|---|
| `probe-walker` | `a02-probe-hall` | `a03-probe-yard 5,3` | **a03, at 5,3** |
| `barrier-tester` | `a01-probe-room` | `a05-probe-barrier 5,2` | **a05, at 5,2** |

**The ledger is the truth about where you are, down to the square.** The header is
not, and it is **the header the save list prints** — the line under the menu still
read *"Probe Walker: 1 of 11 — in your campaign, a02-probe-hall left you at 1"* while
Continue was putting me in a03. ⚠ **The list names one area and the button opens
another.**

## 2. Why the header lags — the `_leaveScreen` race, measured

`play_screen.dart` and `main.dart:220` both name it: *"`_leaveScreen` fires the
position write and the outcome write in the same tick, both `unawaited`. The same
race, on a path nobody had looked at."* Here is the A/B, same build, same key, same
character, differing only in whether a fight was in progress:

**Escape with a fight in progress** — the two `encounter.ended` rows landed, and:

    …no character.moved for 0,3, where I was standing
    …header still says a01-probe-room

**Escape with no fight** — from the same area, four squares later:

    character.moved {area: a05-probe-barrier, x: 5, y: 2}
    character.moved {area: a05-probe-barrier, x: 9, y: 2}
    …header now says a05-probe-barrier

⚠ **The position write is the one that loses when a fight ends in the same tick, and
the stale header is its visible symptom.** Both writes land when nothing competes.

⚠ **And it can lose the other way.** Comparing `probe-walker.sav` as I read it at
16:38 with the copy taken at 17:04, the anvil fight's three rows — two
`encounter.ended` and the `character.revived` — are **gone from the later file**, and
a `character.moved a03 5,3` is there instead. Same tick, opposite winner. **Which of
the two survives is not stable.**

### ⚠ Correction to TEST 043 §3

TEST 043 said *"the only `character.moved` entries are area arrivals."* **That is
wrong and I am correcting it rather than leaving it.** Position is written at
*moments* — on load, on leaving, and when a fight starts — recording the square you
are on then. It is **not** written per step (eight steps in a03 and six in a01
produced none), which is the half of the claim that stands. That also explains the six
identical rows in `grave-digger.sav` that I noted and could not account for: **one
write per fight round, at a square that did not change.** Not a defect; a consequence
of when the write fires.

## 3. Click-to-move is not inert. It has never existed.

TEST 043 flagged that clicks and diagonal keys did nothing. Chased one step, and
Coder has already written the answer down — `play_screen.dart:2633`:

> *"`SPACE` ENDS THE TURN — `PT-1540`. A key rather than a click, because `PT-1443`
> wants the keyboard path to reach everything the pointer does, and **this screen has
> never taken a pointer.**"*

`grep -c "GestureDetector\|onTap" play_screen.dart` → **0**. There is no pointer
handler on the play screen at all. ⚠ **`PT-1443` is a plan, not a feature**, and three
things are leaning on it:

1. **The player's reach check** (`play_screen.dart:1695`): *"it is here because
   `PT-1443`'s click-to-move names a SQUARE rather than a direction."* TEST 043 showed
   that branch is dead. **Its justification has no path behind it.**
2. **`PT-1584`'s eight-versus-four** (`approach.dart:30`, `play_screen.dart:2159`):
   *"a creature can approach on a diagonal and a player cannot follow on one…
   `PT-1443`'s click-to-move dissolves it."* **It is live.**
3. **The soft-lock validator** (`package_validate.dart:391`): reachability is computed
   on four offsets *"the day `PT-1443`'s click-to-move or four more bindings land,
   this widens to `stepOffsets`."* Named as *"the third place eight-versus-four has
   become load-bearing."*

⚠ **AND IT COST ME A FIGHT TODAY, WHICH IS THE PART NO COMMENT SAYS.** a01's
`from-probe-hall` arrival at 4,2 has all four orthogonals blocked — three creatures
and a doorway — while `5,1` and `5,3` are open floor one diagonal step away. **A
player who arrives there cannot leave without starting a fight or going back through
the door.** The asymmetry is not only a rules discrepancy; it strands a player on a
legal square. That is what four bindings buy on a real board.

---

## What I did not check

- `47789fa` / Lodestar `e1a837c`. Not in my bundle. Untested.
- *"out of movement N squares short"* — the budget stall. Reasoning for why this
  fixture cannot produce it is above; no second fixture built.
- Whether the reachability validator flags `a05-probe-barrier`. I did not re-open the
  package in Loom after authoring it.
- Whether the header/ledger disagreement also affects `Load Game` (I only tested
  `Continue`).

## State

- **`tester-probe` has changed and I am keeping the change**, declared here: new
  `areas/a05-probe-barrier.toml`; `a01-probe-room.toml` gains `door.probe-room.17` at
  5,0 and a `from-probe-barrier` arrival at 3,1, `tag_seq` 16 → 17; `package.toml`
  `[order].areas` gains `a05-probe-barrier`. Pre-run copy at `PKG-T043/`, post at
  `PKG-T044/`.
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination
  (`barrier-tester.sav` created, `probe-walker.sav` staged for the Continue test)
  snapshotted at `SV-T044-after/`.
- `base-rules` **unchanged** — `diff -rq` clean against `BK19`.
- The NWN install was not read or written.
- My app killed by PID; Coder's Looms survived.
