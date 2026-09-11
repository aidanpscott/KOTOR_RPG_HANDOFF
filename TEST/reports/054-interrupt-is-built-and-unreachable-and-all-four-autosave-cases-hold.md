# TEST 054 — the interrupt is built and unreachable, and all four autosave cases hold

**Built against:** `run-app.sh` / `run-loom.sh` (always rebuild). Tree/bundle at
`869ae85` (*PT-1666 — the gate is the door's, and an unchecked crossing is held*),
app bundle built 08:11. `strings … | grep -c "PT-1666"` → 10, `"PT-1664"` → 16,
`"PT-1668"` → 0, `"PT-1669"` → 0.

⚠ **`PT-1668`/`PT-1669` are not commit numbers in this tree** — I searched both the
app and Lodestar source and found neither. Reading `PT-1666`'s own code comments, the
four-case reasoning the brief attributes to `PT-1669` is written *inline* inside
`_unsavedCrossing`'s doc comment in `play_screen.dart:460`, and `PT-1668`'s "third
link list, gated" is `PT-1664`'s own `interrupt` field. I am treating both as rulings
folded into the commits I have, not missing code.

**Instrument:** PID-scoped via `run-app.sh`/`run-loom.sh`'s `exec` (shell PID is the
process PID directly). App `670416`, Loom `680572`; killed by PID. Coder's Loom
`517968` untouched throughout.

---

## 1. The interrupt — built correctly, and structurally unreachable for the player

Read the mechanism before touching the app. `dialogue.dart`'s reader:

- An NPC line's `interrupt` list is legal **only** on a line that `then`-continues.
  `interrupt` present without `then` fails with `interruptWithoutContinuation`:
  *"a line that already asks has nothing to interrupt."*
- At runtime (`dialogue_run.dart:631`), `interrupts: reactionsLeft > 0 ? _offers(…) :
  const []` — **the gate is a straight `reactionsLeft` comparison**, and taking one
  (`interrupt(option, …)`) does `reactionsLeft--`.

⚠⚠ **And `reactionsLeft` is always 0 for the player, unconditionally, in this build.**
`play_screen.dart:1769` — the player's `Budgets` construction —
hardcodes `highestReactionTier: 0` as a literal. `round.dart`'s `reactionPool`
computes `min(max(byDex, byBab), highestReactionTier)`, so **whatever the player's
DEX or base attack bonus, the result is `min(anything, 0) = 0`.** This is not a bug I
found; it is named and dated in the app's own comment, `play_screen.dart:1741`:
*"A REACTION POOL OF ZERO, ALWAYS — `PT-1534`… nothing supplies a tier."*

**Built the fixture anyway, to confirm the gate behaves correctly under that
condition rather than assume it.** `probe-narrator` carries a valid interrupt line:

    [[npc]]
    id = "opening"
    say = "The countdown reaches zero, unless something stops it."
    then = ["opening-continues"]
    interrupt = ["cut-in"]

Walked into it. The panel showed **only** `[Continue]` — no interrupt option, no
error, no broken state. Pressed it: *"...and nothing did."* Exactly the behaviour
`reactionsLeft <= 0` predicts.

⚠ **So the confirmable half of the ask is confirmed, and the other half is a scoped
negative I am stating rather than working around**: *"only offers when the player
has a free reaction"* holds — I demonstrated the zero-reaction case correctly
suppresses the offer, on the one case this build can produce. **I could not
demonstrate the has-a-reaction case, or "consumes one when taken," because no
character build, feat, or state in this app can give the player a nonzero
`reactionsLeft` — the input is a compile-time literal.** This is worth a name of its
own if it doesn't have one: the interrupt system is fully built and internally
correct, and currently dead code from the player's side.

### The illegal combination — refused exactly as the reader promises

`probe-illegal` carries the barred shape:

    [[npc]]
    id = "bad-line"
    say = "This line asks you something AND claims an interrupt."
    replies   = ["only-reply"]
    interrupt = ["cut-in-bad"]

Walking into it (⚠ by accident, mid-navigation, after an unrelated fight — see below)
produced:

    this conversation will not load — bad-line — this line carries `interrupt` and
    does not continue. An interrupt is for a line that CONTINUES — PT-1578 gives
    Continue the moment a player has no choice, and that is the moment there is
    something to cut into. A line that already asks has nothing to interrupt.

**Confirmed: rejected outright**, in the same *"this X will not load"* voice the app
already uses for a bad doctrine. I did not need to construct anything exotic — the
reader's own message names the exact rule.

### ⚠ An accidental fight, and I did not chase it further

Both new creatures sit at squares I had confirmed open two sessions ago, but a
navigation miscalculation walked me into `probe-sentinel.probe-room.08` — a *real*,
pre-existing a01 creature — twice, once per test character. Both fights resolved
(the sentinel died both times); the player fell to 4/13 HP once and was never in
real danger, since a disposable test character dying costs nothing here. Flagging
this only because it is why the illegal-conversation refusal above was captured
*after* a combat log rather than cleanly — the content of the refusal is unaffected.

---

## 2. All four PT-1666 cases confirmed, one file-diff at a time

Built the two doors needed: `door.probe-room.05` (a01→a02) now carries
`save_on_use = true` — the **checked** door. `door.probe-room.06` (a01→a03, already
existing, never edited) is the **unchecked** comparison. A third,
`door.probe-room.20` (a01→a11, new, unchecked), lands on an arrival I walled over —
`a11-probe-uncheckedwall`'s `walled-in` at (1,0) — to force `PT-1605`'s fallback
through a door that never opts into autosave.

### Case 1 — checked door: writes, and shows "saved"

    before: event count 22
    crossed door.05 → a02
    status: "Probe Hall — arrived at from-probe-room · saved"
    after:  event count 23, new row {a02-probe-hall, 0, 0}

**Confirmed, both halves.**

### Case 2 — unchecked door: writes nothing

    before: event count 23
    crossed door.06 → a03 (no save_on_use)
    status: "Probe Yard — arrived at from-probe-room"   ← no "· saved"
    after:  event count 23, unchanged

**Confirmed, both halves** — and the reverse of the checked door (a02→a01, a
*different* connection entry, never marked) showed no "saved" either, a free
consistency check.

⚠ Crossing this unchecked door landed me in `a03-probe-yard`, which is a one-way
room by design. That character (`Interrupt Tester`) is now permanently there;
built a fresh character (`Door Case Tester`) for the remaining two cases.

### Case 3 — fallback through an unchecked door: writes anyway

This is the one the brief flagged as worth the most attention, and it took two
tries: my first attempt failed on my own mistake, not the feature — `a11` was
already declared in `package.toml` when I authored it, but the running session
had cached the **package's area list** from before that edit, so the door refused
with *"the manifest does not list 'a11-probe-uncheckedwall'"*. Exited to the
library and reopened the package fresh — the individual **area files** were
already proven to re-read live in TEST 052; the **package-level area roster** is
not, and needs a full re-open to pick up a new area's registration. Worth naming
as its own small fact.

With the fresh registration, standing at (3,0) and stepping once onto the door
tile (4,0) itself — not resuming already on top of it, which the first attempt did
by accident and which just re-fires the neighbouring `door.probe-room.17` instead:

    status: "Probe Unchecked Wall — arrived at walled-in · the arrival 'walled-in'
             is not standable, so you are at 0,0"
    immediately after: event count unchanged (22)     ← no immediate write
    pressed Escape
    after Escape:      event count 22 → 23, new row {a11-probe-uncheckedwall, 0, 0}

⚠⚠ **Confirmed, and the timing is the finding worth keeping precise.** The write is
not immediate at the crossing — consistent with the door being unchecked, so no
autosave fires at that instant — but it is **not lost**: leaving the screen persists
it, exactly as `_unsavedCrossing`'s own doc comment describes: *"crossing an
unchecked door and pressing esc [would otherwise write] NOTHING… `PT-1523`'s second
moment would have been silently repealed by a ruling about doors."* The fallback
earns its event regardless of the door's own opt-in state.

### Case 4 — ordinary Continue resume: writes nothing, either way

    before Continue:                     event count 23 (case 3's write)
    Continue (resumes in a11, at 0,0):   event count 23, unchanged
    Escape immediately, no movement:     event count 23, unchanged

**Confirmed, both halves** — resuming a save writes nothing by itself, and leaving
again without having moved writes nothing either (PT-1658's read-must-not-write
guarantee, holding under PT-1666's changes).

---

## ⚠ PT-1617 — a file changed that is not mine

    endar-spire/areas/a01-command-deck.toml   modified Sep 11 07:55

Reported, not reverted. I did not open `endar-spire` this session. Re-baselined my
md5 comparison file to the new state (`pkgs-baseline-T054.md5`) so the next run
compares against what's actually there.

## What I did not check

- Whether any character build, feat, or future content can ever supply a nonzero
  `highestReactionTier` — the value is a literal at one call site; nothing in the
  current feat/power data reaches it. I traced the code rather than exhaustively
  trying every feat.
- Whether Loom exposes `save_on_use` as an actual checkbox in its door-authoring UI,
  or only as a hand-authorable TOML field — I set it by direct file edit, consistent
  with how every fixture this thread has been built, and did not open Loom's door
  editor to look for the control the brief's word "checkbox" implies.
- Whether the package-arealist re-registration gap above (needing a full re-open
  rather than just re-entering) affects `Load Game` the same way it affects `New
  Game`/`Continue`.

## State

- **`tester-probe` gained two fixture areas' worth of content, kept deliberately.**
  New `dialogue/interrupt-valid.toml`, `dialogue/interrupt-invalid.toml`,
  `blueprints/characters/probe-narrator.toml`, `blueprints/characters/probe-
  illegal.toml`; `a01-probe-room.toml` gains both creatures, `door.probe-room.20`
  (→ a11, unchecked), and `save_on_use = true` on `door.probe-room.05`; new
  `areas/a11-probe-uncheckedwall.toml`; `package.toml` registers `a11`. All files
  parse. Loom's count moved 14 → 17, and all three new faults are `a11`'s own
  deliberate ones (`landingNotStandable`, `connectionUnreachable`,
  `areaHasNoWayOut`) — confirmed by the exact arithmetic and by reading each row.
  Snapshots `PKG-T054-before/`, `PKG-T054-after/`.
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination
  (`interrupt-tester.sav`, `door-case-tester.sav`) at `SV-T054-after/`.
- `base-rules` unchanged. `endar-spire` changed by someone else, reported above,
  re-baselined.
- The NWN install was not read or written.
- Both my processes killed by PID; Coder's Loom untouched.
