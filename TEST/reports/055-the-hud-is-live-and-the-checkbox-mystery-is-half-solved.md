# TEST 055 — the HUD is live, and the checkbox mystery is confirmed for one tool and not another

**Built against:** `run-app.sh` / `run-loom.sh` (always rebuild). App tree/bundle at
`488b8b0` (*PT-1672 — the roster panel, and PT-1675's silence*), built 09:31. Loom
tree/bundle at `36924f8` (*repin lodestar — PT-1672's roster and PT-1675's withheld
interrupt*), built 09:31.
`strings … | grep -c "PT-1672"` → 10 (app), `"save_on_use"` → 13 (Loom).

**Instrument:** PID-scoped via `run-app.sh`/`run-loom.sh`'s `exec` (shell PID is the
process PID directly). App `690300`, Loom `680572`; killed by PID. Coder's Loom
`517968` untouched throughout.

---

## 1. The roster panel — two confirmed live, two structurally unobservable

Read the panel's source before touching it. `roster_panel.dart`'s player card has a
vitality bar plus, when Force-capable, a **three-segment** Force bar
(`current` / `headroom` / `degraded`, the last in its own colour, `C.forceDegraded`,
never a dimmed fill). Enemy rows use the same vitality shape scaled down, plus a
`hidden` amber label. Both `_vitalityColour` and `_trackColour` give down/dying/dead
their own colours, and the comment names the exact reason: *"Down, dying and dead are
all at or below zero, so the FILL band has width zero for every one of them — the
state colour was unreachable exactly in the three states it exists to distinguish…
the track carries it when there is nothing left to fill."*

### Confirmed — live during a fight, damage moves the bars in real time

Built a Jedi Guardian (`Hud Tester`) to get a Force pool onto the card, then bumped a
real, pre-existing a01 creature (`probe-sentinel.probe-room.08`) into a fight.

    Round 1: Hud Tester 13/13, force 6/6  ·  probe-sentinel.probe-room.08 33/33
    Round 2: Hud Tester 11/13             ·  probe-sentinel.probe-room.08 27/33
    (…several rounds…)
    Round N: Hud Tester 4/13              ·  probe-sentinel.probe-room.08 2/33

**Confirmed both halves.** Both rows were on screen from the first turn (player card
top, enemy row below, "in this fight" header), and every attack's numeric log line
matched the bar's new proportion exactly — the fill widths shrank live, in step with
the combat log, no lag or stale frame observed across five rounds.

### Not observable — and traced to why, rather than left unresolved

⚠⚠ **A hidden combatant's row.** `_rowsFor`'s `hidden: unseen.contains(h)` reads
`_concealed`, which is `{stealth-concealed creatures} ∪ _fallen` — **a dead
combatant is unioned into the same concealment set**, so in principle a dead row
*would* render hidden-marked rather than vanish. But `_roster` itself is
`combatRoster(_log, encounter: _areaId)`, and the panel's own comment says
*"the roster is empty between fights — `combatRoster` closes every membership on
`encounter.ended`."* Every fight this build can construct is strictly 1-vs-1 —
`grep -n "combatants: \["` finds exactly one call site,
`Encounter(combatants: [me, p.combatant])` — so the instant either side reaches 0,
the fight ends and the panel disappears in the same tick.

**Tried to catch the transition anyway rather than assume it.** Captured four frames
in rapid succession (~0.2–0.3s apart) around the sentinel's killing blow — the panel
was already gone in all four. There is no third combatant to test hidden-persistence
against, and no visible window between "alive, roster open" and "dead, roster
closed" in a 1-vs-1 fight.

⚠⚠ **A dead/down/dying row's empty track.** Same limitation, same evidence. I
confirmed the *mechanism* is real by reading `_Bar`'s implementation — a state's
track uses `_vitalityColour(v)` instead of the neutral dim exactly when the fill
width is 0 — but could not observe it live for the same reason: the panel that would
show it closes before or in the same frame as the state change, in every fight this
app can currently construct.

**Both are scoped negatives, not gaps in the search:** the code is correct by
inspection, the fixture that would exercise it (a surviving multi-combatant
encounter) does not exist in this build, and I did not build one because there is no
code path to build one — `Encounter`'s only constructor call takes exactly two
combatants.

### A bonus confirmation, found by accident

Bumping `probe-narrator` (my own `TEST 054` interrupt fixture) this session produced
a new, more explicit line: *"there is an interruption here and you have no reaction
to spend."* `PT-1675` landed between sessions and gives the zero-reaction case an
explicit sentence rather than silent suppression — a direct improvement on the exact
gap `TEST 054` filed.

---

## 2. The `save_on_use` checkbox — confirmed for one tool, and not the whole story

Read `grid_view.dart`'s `_tap` before touching Loom: *"Place beats paint beats
select. Only one is armed at a time, because the palette selection is the mode"* —
`placingWay != null` → `placing != null` → `painting != null` → only then
`onSelect`.

**With nothing armed**, clicking `door.probe-room.05` (my own `save_on_use = true`
door from `TEST 054`) at (5,2) showed the selection bar correctly:

    door.probe-room.05
    doorway → a02-probe-hall · from-probe-room · at 5, 2
    ◉ save on use
    crossing here saves the game and says so — §4b

**With `terrain → floor` armed**, clicking the exact same square: **no selection bar
at all** — the status line read *"edited a01-probe-room"* instead. ⚠⚠ **Confirmed,
and it is the whole explanation for this case.** Terrain painting is the tool
`_tap` intercepts *unconditionally* (`if (widget.painting != null) { onPaint(…);
return; }`, no occupancy check), so an armed paint tool hides the bar on *any*
square, door or not. Disarming and clicking again immediately restored the bar,
`◉ save on use` intact.

⚠ **The write was real and I checked the damage.** Painting "floor" onto a square
whose area declares `default = "floor"` (no explicit tile map) turned out to be a
logical no-op — `diff` against my pre-session copy shows exactly one blank line
removed (Loom's writer normalizing the file on save) and nothing else. The
connection, its `at`, and `save_on_use = true` are all byte-for-byte where I left
them. Confirmed the file still parses.

⚠⚠ **With `doors` armed instead, on the same already-occupied square, the bar
appeared correctly anyway** — `save_on_use` still showing `◉`, no write to the file
(the diff shows only the one line from the terrain test, nothing from this). *So
Coder's hypothesis is confirmed for paint-type tools, and is not, on this evidence,
the complete explanation for every palette tool* — a way-placement tool aimed at a
square that already holds a way appears to fall back to selecting it rather than
attempting a duplicate placement, which is a different code path than the
unconditional paint branch. **Say so plainly where it holds (terrain, and by the
same structure any unconditional paint variety), and name the one case where I
could not reproduce it (an already-placed doorway with the doorway tool itself
armed) rather than rounding both up to "solved."**

---

## What I did not check

- Whether `creatures`/`placeables` (placement-type tools, not paint, not way)
  reproduce the hidden-bar mystery on an occupied square — I tested `terrain` and
  `doors` only, the two the brief named as suspects.
- Whether the mystery reproduces on an **empty** square with `doors` armed — a
  different question (placing a *new* doorway there) from the one asked. I only
  clicked squares that already held content, mirroring the original report.
- Force pool degradation, hidden creatures via the stealth matrix, and every other
  Force-bar behaviour beyond what this brief's four points named — out of scope for
  this run.

## State

- **`tester-probe` gained one cosmetic normalization from Loom's own writer**
  (one blank line removed from `a01-probe-room.toml`, from the terrain-paint
  reproduction above), no other content changed — verified by `tomllib.load`, by
  reading the connection block back whole, and by diff. Kept, since it is
  Loom's own output and the connection it touched is unaffected. Snapshot
  `PKG-T055-after/`.
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination
  (`hud-tester.sav`) at `SV-T055-after/`.
- `endar-spire`, `base-rules`, `taris-undercity`: **untouched** — md5 and mtime
  verified against the `T054` baseline.
- The NWN install was not read or written.
- Both my processes killed by PID; Coder's Loom `517968` survived.
