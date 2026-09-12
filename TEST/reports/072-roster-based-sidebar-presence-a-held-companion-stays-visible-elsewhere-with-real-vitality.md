# TEST 072 — PT-1833 confirmed live: a companion holding position in a
# different room stays on the sidebar (roster-based membership, not
# room-based) marked "not in this room · holding position," and their
# vitality is the real, wounded number rather than a false full health

**Built against:** `run-app.sh` (always rebuilds). Local `KOTOR-RPG-APP`
HEAD at build time: `295d268` (10:58:01, *PT-1833: the sidebar asked the
room, and membership is the roster's* — this task's own commit, no drift
this session). `pubspec.lock` pins: `lodestar` `ref: main` resolved to
`74bdfd01df670b4a7ebe9e9286f5f041dca524c7`, `lens` `ref: main` resolved
to `e79bc066233fabc7776c8b94737029646d762e6e` — both confirmed present as
actual checkouts at `~/.pub-cache/git/Lodestar-74bdfd0...` and
`~/.pub-cache/git/Lens-e79bc06...`. `check_shelf.py` run at session
start: `✓ 25 rules files, all identical to what the extracts generate`.

App PID `156821` killed by PID, confirmed gone. Coder's Loom (`12445`/
`12443`) checked running, untouched, before and after.

---

## Setup: wounding Mate before leaving her behind

Built "Talia Rhen" (Human Soldier, Merchant) through chargen to `Play` in
`companion-fixture`'s `a01-corridor`. Bumped `starter.corridor.01` to
start a fight and let several rounds pass — Mate took real damage from
`mate.corridor.02`'s attacker, dropping to **46 of 60**. Crossed the door
to `a02-second-room` to end the fight (as established in TEST 069/071,
leaving the area ends an active encounter), picking up two more points of
opportunity-attack damage on the way — Mate settled at **42 of 60**.
Walked back through the door into `a01-corridor`, now in exploration
mode, and confirmed her row still read **42 of 60** before proceeding —
i.e. the wound was already real and persistent going into the actual
test.

## Roster-based presence — CONFIRMED

With Mate still following (not yet holding), clicked **Wait here** on
her row: status line read **"Mate will wait here,"** row updated to
**"Soldier · 1 · holding position," 42 of 60** — the order took effect
without touching her HP. Walked back to the door and crossed into
`a02-second-room`.

**Mate's row did not disappear.** It read:

**`Mate` / `not in this room · holding position` / `42 of 60`**

— present, correctly labelled, no verb buttons at all (`Wait here`,
`Follow / regroup`, `Trade / give item` all absent — matching
`party_sidebar.dart`'s `_verbs` getter, which returns an empty list when
`row.elsewhere` is true, since `§3a`'s catalogue is aimed at what's
actually reachable and Mate isn't in this room to be given any of those
three orders). This is exactly BUILD 158's regression, now fixed: a
companion holding position in the room behind you used to vanish from the
one surface that could ever offer them `Follow / regroup`; now she's
visibly still party, just elsewhere.

## Vitality reflects reality, not full health — CONFIRMED

Mate's off-board row read **42 of 60** — the exact HP she had when
ordered to hold, not `60 of 60`. This matches the commit's own stated
intent (*"a row reading full health for somebody you left bleeding would
be worse than no row"*) and its mechanism: the off-board row is resolved
through `combatantsIn` (the same reader `_bringTheParty` uses) and then
run through `_restore`, rather than being a static/default-health
placeholder.

---

## What I did not check

- Whether walking back into `a01-corridor` and clicking **Follow /
  regroup** correctly re-attaches Mate and clears "not in this room" —
  the task's ask was specifically about the disappearing-row/vitality
  bugs, and this is a straightforward continuation of TEST 071's already-
  confirmed regroup behavior; didn't re-drive it.
- A companion holding position while a *third* room is loaded (neither
  the holding room nor the room she'd be brought into) — only the direct
  two-room case was tested.
- Whether the row's `elsewhere` state is visible/correct while the player
  is mid-fight in a different room's encounter (combat hides all
  party-directed verbs and, per source, is a separate `f.order`-driven
  list — not applicable to this specific check, but not independently
  re-confirmed here).

## State

- `companion-fixture` (mine) — no files added or changed this session;
  confirmed by mtime, same five weapon-item blueprints and `mate.toml` as
  prior sessions.
- One new save created this session ("Talia Rhen"), reached `Play`,
  fought, crossed the door twice, issued one Wait-here order — not
  cleaned up, ordinary Tester artifact.
- App PID `156821` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
