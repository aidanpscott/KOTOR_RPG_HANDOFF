# TEST 078 — the vitality band now agrees with the sidebar, confirmed
# across three rounds. Click-to-move works for the ruled cases, but it
# charges movement TWICE per square, and a click at an unreachable tile
# walks you out of the room through a door

**Built against:** `run-app.sh` (always rebuilds). App started 20:48:41;
local `KOTOR-RPG-APP` HEAD `f279d23` (20:13:43, *the vitality band shows
the fight's own number during a fight*), which is the tip and contains
both commits under test — `f279d23` itself and `dd53dcf` (*Click-to-move
— PT-1443 becomes a feature*).

**The working tree was not clean**, and it touches the file under test:

```
 M lib/play/attack.dart
 M lib/play/play_screen.dart
 M pubspec.lock
 M test/two_enemies_test.dart
```

That is Coder's in-progress **Treat/medpac** work (`_aMedpac`, `_heal`,
the `treat — no medpac` refusals) — the thing I was told to hold off on.
I grepped the added lines: they touch none of `_walkTo`, `onTapTile` or
the band, so the two features below are the committed ones. I did not
exercise Treat, Repair or Gear, and I left the changes exactly as found.

Engine pin I compiled against: `lodestar`
`c89d55ff869da3f212bdbddef10201bbf749b3b0` (working tree); HEAD's pin is
`724cdbe0a572cf8fc25c176a564fe554d056cf52` — the usual floating `ref:
main` drift. **`approach.dart` is byte-identical between the two**, so
Defect A below is not an artifact of that. `lens`
`e79bc066233fabc7776c8b94737029646d762e6e`. Checkouts present.
`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`.

App PID `50999` killed by PID, confirmed gone.

---

## 1. The vitality band matches the sidebar — CONFIRMED

Driven in `companion-fixture`'s corridor, watching both surfaces in the
same frame across three rounds of a real fight:

| moment | sidebar | band |
|---|---|---|
| right after `hit · damage 2 · 58 left` | Chaser **58 of 60** | `chaser.corridor.03: 58 of 60` |
| a round later | Chaser 58, Mate **59 of 60** | `chaser…: 58 of 60 · mate…: 59 of 60` |
| two rounds later | Chaser **54**, Mate **48 of 60** | `chaser…: 54 of 60 · mate…: 48 of 60` |

The unwounded rows agreed too (`Kaeda Draan: 13 of 13`,
`starter.corridor.01: 16 of 16`). **They never disagreed**, including in
the frame immediately after a blow landed and with two combatants at two
different wounded values — which is the case the old fold got wrong
(everybody at full capacity in the band while the sidebar showed the real
number).

## 2. Click-to-move — the ruled cases all hold

- **It walks you there.** From `(0,0)` clicked `(5,1)`; arrived exactly
  at `5, 1`, and the companion followed.
- **A click on a creature refuses**, with the ruled sentence and nothing
  else: **"walk into them to act — choose an action first to aim at
  somebody"** — no attack, no silent no-op, no movement.
- **You do not walk through an ally.** Bumping her on the keyboard gives
  **"mate.corridor.02 is with you — there is no way past without walking
  round"** and the player stays put; the click router never lands on an
  occupied square.
- **Doors work by click** exactly as by key: clicked the door tile in the
  Second Room and got **"Corridor — arrived at start"**.
- **The keyboard is unchanged.** Arrows still move one square per press,
  and a single step costs exactly **1** movement.

## ⚠ Defect A — a click charges movement twice per square

Measured in one fight, same character, speed 5:

| input | squares moved | movement spent |
|---|---|---|
| one arrow key | 1 | **1** |
| click 2 squares away | 2 | **4** (5 → 1) |
| click 6 squares away | **0** | **5** (5 → 0), *"no move left this turn"* |

So a click costs double, and when the doubled cost exceeds the budget the
player **does not move at all while still losing the whole move**.

**Mechanism**, read in the engine I built against and consistent with both
numbers: `_walkTo` hands `approach()` the live `f.player.budgets`, and
`approach` is a *mover*, not a planner — `approach.dart:325` is
`spent += budgets.move(1, crossing: ground);`. It spends the budget while
producing the route; `_walkTo` then replays that same route through
`_step`, which spends it again. Two squares is 2 + 2 = 4. Six squares
drains all 5 in the planner, leaving nothing for the walk, so the legs are
refused and the player stands still.

**It is invisible outside a fight**, which is why it reads as working:
there `_walkTo` builds a throwaway `Budgets(speed: a.width * a.height)`,
so the double spend comes out of a budget nobody can see and no pips show.

**Practical effect:** at speed 5 a click can carry you at most two
squares, and any click three or more away burns the entire move for little
or nothing. The keyboard is unaffected, so the two movers now disagree
about what a square costs — which is the *"a rule applied to one path and
not the next"* shape the click-to-move commit itself names as the thing it
was avoiding.

## ⚠ Defect B — clicking an unreachable tile walks you out of the room

In `tester-probe`'s **Probe Hall**, row 1 is a solid wall band, so the
floor block at rows 2–3 / cols 0–1 cannot be reached from the arrival at
`(0,0)`.

Clicked `(1,3)` — a floor tile on the far side of that wall. **The player
crossed the door at `(1,0)` and arrived in the Probe Room**, a different
area, which is not the tile that was clicked. **Reproduced twice** from a
standing start at `(0,0)`.

The wall itself was not walked through — the player never ended up behind
it — but the outcome is an area change nobody asked for. `_walkTo` only
prints its refusal (`r.stalled ?? 'there is no way there'`) when
`r.route` is **empty**; here the route came back non-empty with a first
leg onto the door square, and stepping onto a door is a room change. The
keyboard has no equivalent: it refuses in place.

---

## What I did not check

- **Difficult terrain specifically.** Its only visible effect is on the
  move remainder, which exists solely against a combat budget — and
  Defect A makes any click-path cost arithmetic unreliable, so I could not
  get a clean reading. Keyboard behaviour over difficult ground is
  long-standing and not part of this change.
- **Treat, Repair and Gear** — held off as instructed, and they are the
  subject of the uncommitted work sitting in my build.
- Whether **Defect B** also fires for an unreachable destination with no
  door anywhere on the attempted route — every unreachable case I could
  reach in these fixtures had one.

## State

- No fixture edits this session; TEST 077's temporary probe placement
  remains removed.
- Saves created in `companion-fixture` (Kaeda Draan) and the earlier
  `tester-probe` character reused; neither cleaned up.
- App PID `50999` killed by PID, confirmed gone. **Coder's uncommitted
  working-tree changes left exactly as found.**
