# TEST 053 — autosave-on-door-use confirmed, appends cleanly

**Built against:** `run-app.sh` (always rebuilds). Tree/bundle at `843fbb0`
(*PT-1663 — autosave on door use was already true, and silent*), bundle built 07:25.
`strings … | grep -c "PT-1663"` → 1.

**Instrument:** PID-scoped via `run-app.sh`'s `exec` (shell PID `658558` is the app
PID directly). Killed by PID; Coder's Loom `517968` untouched.

**Task:** confirm a door crossing writes "saved" onto the status line,
append-not-assign, and that it doesn't collide with the room-name text already
there.

---

No existing save sat near a walkable door — all five shelf saves are in `tester-probe`'s
one-way rooms (`a03`/`a04`) or format-1 with no recorded area. Built a fresh character
(**Door Tester**, Human Soldier) to reach `a01-probe-room`'s open floor.

Walked one step, read the line at rest:

    a01-probe-room · 1, 0

Stepped once more, onto `door.probe-room.06` at (2,0), crossing to `a03-probe-yard`:

    Probe Yard — arrived at from-probe-room · saved

⚠ **Confirmed both halves of the ask.** The label appears, appended after the existing
room-arrival text with a `·` separator — not replacing it, not overwriting it. Full
native-resolution frame checked for overlap: the line reads cleanly with room to spare
before the right-hand `Door Tester · arrows to move · m map · esc to leave` block;
no clipping, no visual collision with any other element on screen.

**And it isn't only a label** — verified the underlying file: `door-tester.sav`'s
ledger ends `character.moved {area: a03-probe-yard, x:0, y:0}`. The status line's
"saved" claim matches an actual write to disk, not a decorative-only string.

## What I did not check

- A second door crossing in the same session (a03/a04 are one-way, so this fixture
  cannot test a chain of two saves back to back).
- Whether the label behaves the same on a **Continue**-triggered transit as opposed
  to a fresh character's first door.
- Window sizes other than 1280×720.

## State

- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination
  (`door-tester.sav`) snapshotted at `SV-T053-after/`.
- `tester-probe` **unchanged** — `diff -rq` clean against `PKG-T052-after`.
- The NWN install was not read or written.
- Standing by per instruction — not chasing the conversation wizard's Interrupt half.
