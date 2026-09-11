# TEST 056 — the doorway-tool case closes, and it corrects my own TEST 055

**Built against:** `run-loom.sh` (always rebuilds). Loom tree/bundle at `36924f8`
(*repin lodestar — PT-1672's roster and PT-1675's withheld interrupt*), same
binary as TEST 055 — no new commit landed while idle
(`KOTOR-RPG-APP` still at `488b8b0`).

**Instrument:** PID-scoped via `run-loom.sh`'s `exec`. Loom `692327`; killed by PID.
Coder's Loom `517968` untouched.

**Task:** the one open case from TEST 055 — an already-placed doorway with the
doorway tool itself armed, on the same square. Idle-time chase, not urgent.

---

## ⚠⚠ Correction to TEST 055 — I had not actually armed the tool

TEST 055 reported: *"With `doors` armed instead, on the same occupied square, the
bar appeared correctly anyway… no write to the file."* **That reading was wrong,
and the reason is procedural: clicking `doors` in the palette only expands the
category, listing its one variety, `doorway`, underneath. It does not arm anything
by itself.** My TEST 055 click landed on the category header, not the variety, so
`_placingWay` was never set and the tap fell straight through to `onSelect` —
which is exactly why it looked like a normal selection. I was testing "nothing
armed" a second time under a different label.

Read `grid_view.dart`'s `_tap` again with this corrected understanding, and
`area_tab.dart`'s `onPlaceWay: (x, y) => setState(() => _wayAt = Point(x, y))` —
**no occupancy check anywhere in that callback**, and `_wayAt != null` unconditionally
opens `PlaceWayDialog`. So the predicted behaviour, once the tool is *actually*
armed, is a third outcome distinct from both "selects" and "silently does nothing."

## Confirmed empirically, and it matches the source exactly

1. Clicked `doors` (expands the category — confirmed by the `+ doorway` row
   appearing, not yet armed).
2. Clicked `doorway` itself (the text brightens, matching how `floor` brightened
   under `terrain` in TEST 055 — this is the actual arm).
3. Clicked `door.probe-room.05`'s existing square, (5,2) in `a01-probe-room`.

**Result: the `DOORWAY` placement dialog opened** — *"leads to"* with the full area
list, *"landing on / pick an area first"*, `Cancel` / `Place` (disabled until a
target is chosen). **Not a selection. Not silence. A third, distinct behaviour**:
armed-doorway-on-an-occupied-square offers to place a **second** connection on top
of the first, exactly as the unconditional callback predicts.

## Confirmed it does not write until you tell it to

Clicked `Cancel`. Checked immediately:

    status bar: "…tester-probe · 17 problems"   ← unchanged, no "edited a01-probe-room"
    diff -rq PKG-T055-after/tester-probe  vs  current:  clean

**No selection bar appeared after cancelling either** — the click never selected
the existing door at any point in this sequence; it went straight to the dialog.
I did not click `Place`, which would have written a genuine second `[[connections]]`
entry at (5,2) and is not a state worth leaving behind in a shared fixture.

---

## The full picture, now closed

| tool armed | click on an occupied door square |
|---|---|
| nothing | selects it — `save_on_use` checkbox shows and reads correctly (TEST 055) |
| `terrain → floor` (paint) | paints silently — no bar, no dialog, status says "edited" (TEST 055) |
| `doors → doorway` (place-a-way) | **opens the place-doorway dialog** — offers a duplicate, writes only on `Place` (this report) |

Three palette states, three different outcomes, and none of them is "hides the
checkbox and does nothing else" — the closest to that is the paint case, which is
still the correct explanation for the original bug report (an author with a paint
tool left armed from a prior action, clicking around to inspect doors).

## What I did not check

- Whether choosing a target area and pressing `Place` would create the duplicate
  connection cleanly or trip a new Loom validation fault — did not execute it,
  to avoid leaving a two-connections-one-square fixture behind.
- `creatures`/`placeables` armed the same way (variety selected, not just category
  expanded) on an occupied square — still untested, now for a better reason: I know
  what "armed" actually looks like this time and ran out of scope before circling
  back to it.

## State

- **`tester-probe` unchanged** — `diff -rq` clean against `PKG-T055-after`.
- `endar-spire` + `base-rules` unchanged — md5-verified against `T054` baseline.
- The NWN install was not read or written.
- My Loom killed by PID; Coder's Loom `517968` untouched.
- Multi-combatant fights have not shipped — `KOTOR-RPG-APP` HEAD unchanged at
  `488b8b0`. Standing by.
