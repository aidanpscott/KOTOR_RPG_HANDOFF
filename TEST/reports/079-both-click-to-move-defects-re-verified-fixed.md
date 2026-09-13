# TEST 079 — both TEST 078 click-to-move defects re-verified and CLOSED:
# the double charge is gone (three controlled measurements at the exact
# keyboard rate), and an unreachable tile now refuses cleanly instead of
# walking you through a door into another room

**Built against:** `run-app.sh` (always rebuilds). App started 21:35:19;
local `KOTOR-RPG-APP` HEAD `6c2a6d6` (21:25:12, *the object-directed
context menu*), which contains the fix under test — `d90a297`
(*click-to-move: the double charge, and the reroute through a door*).

`pubspec.lock` pins: `lodestar`
`c89d55ff869da3f212bdbddef10201bbf749b3b0` — **the same engine build TEST
078 ran against** — and `lens`
`cc0fd1493313e9a529618473d46294f70955b940`; both present as checkouts.
Worth noting because it means the fix is entirely in `play_screen.dart`
and not in the mover: `approach()` still spends the budget it is handed;
the screen simply stopped handing it the live one.

The working tree was **clean** when I checked at session start. By the end
three chargen files (`hub.dart`, `identity_screen.dart`,
`step_strip.dart`) were modified — Coder's in-progress work, untouched by
me, unrelated to either feature here; chargen itself ran normally.

`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`. App PID `66798` killed by PID, confirmed
gone.

**Also in HEAD, and it matters to this test:** `6c2a6d6` puts an
object-directed context menu on the **secondary** gesture and leaves
`onTapTile` walking. Every measurement below is a left click, so the
primary gesture still moves — which this whole run depends on and
therefore demonstrates.

---

## 1 · The double charge — FIXED

Same fixture and the same speed-5 Soldier as TEST 078, all in one fight:

| input | squares | movement spent | landed on the clicked tile? |
|---|---|---|---|
| one arrow key (baseline) | 1 | **1** (5 → 4) | — |
| click | 2 | **2** (4 → 2) | yes, `2, 1` |
| click | 3 | **3** (5 → 2) | yes, `2, 1` |
| click | 5 | **5** (5 → 0) | yes, `7, 1` |

Three controlled clicks, all at **exactly one point per square** — the
keyboard's rate. In TEST 078 the two-square click cost 4.

The other half of that defect is gone too. The case that previously spent
the entire budget and **moved the player nowhere** — a six-square click on
five movement — now walks as far as the budget reaches and stops with
*"no move left this turn"*.

*(On that long click I could not reconcile spend against displacement from
the endpoint alone — it ended three squares from where it started having
spent five, on a board where enemies had moved and a reaction had fired.
I did not chase it, because the three controlled measurements above settle
the rate directly and a route picked around obstacles is not reconstructable
from its last square. Flagging it as unreconciled rather than asserting it
is fine.)*

## 2 · The unreachable-tile reroute — FIXED

Reproduced the exact TEST 078 case: `tester-probe`'s **Probe Hall**,
standing at `(0,0)`, row 1 a solid wall band, clicking `(1,3)` on the far
side of it.

**"nothing it can walk gets it closer"** — the player did not move, did
not cross the door, did not change area. Previously this walked through
the door at `(1,0)` and landed in the Probe Room.

Then every other walled-off tile in that room, one click each:

- `(0,2)`, `(0,3)`, `(1,2)` — floor behind the wall
- `(2,3)` difficult, `(3,3)` hazard, `(3,2)` water

**All seven refuse identically**, with the player still at `(0,0)` in the
Probe Hall at the end of the sequence.

**Control — the refusal is not refusing everything.** In the Probe Room,
clicked `(2,3)`, a reachable floor tile with no door between: walked and
arrived exactly at `2, 3`.

### One thing that looks like the old defect and is not

My first control attempt clicked `(3,0)` in the Probe Hall and **did**
cross the door into the Probe Room. That is correct: the hall's door sits
at `(1,0)`, between `(0,0)` and every other tile in the only walkable row,
so any route rightward steps onto it — and stepping onto a door crosses it
on the keyboard too. The hall is simply a bad room for a reachable-tile
control, which is why the real control above was run in the Probe Room.
Naming it so it is not mistaken for a regression by the next reader.

---

## What I did not check

- **Difficult terrain cost arithmetic**, still. TEST 078 deferred it
  because the double charge made click-path costs unreadable; that is
  fixed now, but the only reachable difficult ground in these fixtures
  (`a03-probe-yard`) is a one-way room, and I judged the remaining
  click-cost question answered by the three clean measurements above.
- **Treat, Repair, Gear** — still held off.
- The **context menu** itself (`6c2a6d6`), which is in my build but was
  not part of this ask. I only exercised the primary gesture.

## State

- No fixture edits this session.
- Saves: the `companion-fixture` character (Isolde Tarn) is new; the
  `tester-probe` character was reused. Neither cleaned up.
- App PID `66798` killed by PID, confirmed gone. Coder's in-progress
  chargen edits left exactly as found.
