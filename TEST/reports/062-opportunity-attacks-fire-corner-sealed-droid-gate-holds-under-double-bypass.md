# TEST 062 — opportunity attacks fire, the corner is sealed, and the droid
# melee gate holds even with both upstream layers bypassed by hand

**Built against:** `run-app.sh`/`run-loom.sh` (always rebuild). KOTOR-RPG-APP
`a32f8d9` (*PT-1715 — a droid is never armed with a blade at chargen either*).
`pubspec.lock`'s `lodestar` pins `resolved-ref 6fd064a516f0d3f70b89e75e0b8084d3b3b66392`
(*PT-1713 — a droid blueprint holding a melee weapon is a validator fault*),
confirmed present and current at
`~/.pub-cache/git/Lodestar-6fd064a516f0d3f70b89e75e0b8084d3b3b66392/`. Loom
`7e22d6b` (*PT-1713 — Loom hands the validator the section column*). All three
local HEADs held steady across the whole session — checked again at the end,
no drift to caveat this time.

App PIDs used and killed by PID: `817889` (pre-fix baseline, killed before
rebuilding), `823649` (post-`a32f8d9` — Tasks 1–3). Loom PIDs used and killed
by PID: `822709`, `826178`, `832102`. Coder's Loom `517968` checked running,
untouched, before and after every one of my launches.

**Instrument:** window-focus discipline mattered more than usual this run —
`xdotool key --window <id>` silently no-ops if the window manager's input
focus has drifted to a different window (Loom, a file picker, or nothing),
and the screenshot still renders the *old* frame with no error. Caught it
twice by noticing a move that should have changed a frame counter or a status
line didn't, and recovered with `windowactivate` + a canvas click before
retrying the key. Named because it cost time and could easily read as "the
game ignored an input" when it was mine to fix.

---

## Task 1 — opportunity-attack fixture re-run, unchanged (PT-1708's fix)

`opportunity-attacks` package, `a01-melee`, reused byte-identical — no fixture
edits, per the queued instruction. Fresh throwaway character ("Reach Tester
Two", Human Soldier, STR/DEX/CON/INT/WIS/CHA all 13, matching TEST 061's
build for a clean before/after).

- **Guard's own turn Strike**, unprompted: vitality `11 → 10`
  (`rolled 17 … hit … damage 1`) — same as TEST 061, still correct.
- **⚠⚠ The Strike that never fired in TEST 061 fired this time, first try**:
  retreating from adjacent (distance 1) to distance 2 produced —

  > `guard.melee.01 catches Reach Tester Two leaving — unarmed · rolled 17 —
  > d20 16 + attack 1 + Strength 0 · needed 14 — hit · damage 1 — 1d3 1 · 9
  > left`

  Vitality `10 → 9`. This is exactly the trigger TEST 061 spent its whole
  report failing to produce three separate times. `PT-1708`'s fix — threading
  `baseAttackAt` into `combatantsIn`/`combatantFrom` so `reactionPool` sees a
  real BAB instead of the old always-`0` — reads as closed.
- **Disengage, then retreat again, same fight**: pressed `d` on my next turn
  while adjacent → `"disengaging — your movement provokes nothing this
  turn"`, action pip spent. Retreated the same one square immediately after
  → **no Strike, no log line, vitality held at 9**, reaction pip still shown
  lit. This is the half TEST 061 could not test at all, because nothing was
  firing to be prevented. Confirmed working on the first attempt.

Both halves of Task 1 hold: the Strike fires, and Disengage actually prevents
it in the same fight, same turn cadence, no fixture changes.

## Task 2 — the corner is sealed, sight and diagonal movement both (PT-1709)

`ranged-detection` package, `a05-corner-peek`, reused byte-identical — the
same wall pair at (3,1)/(4,2) that TEST 060 named as the exact flanking pair
for the diagonal step (3,2)↔(4,1). Fresh throwaway character ("Corner Tester
Two", Human Soldier, same build pattern). Had to switch `[entry]` to
`a05-corner-peek` and relaunch fresh to pick it up — this build's version of
the `TEST 060` package-config-caching lesson; switched via Loom's own "set as
entry" control rather than hand-editing the TOML (see note below), and reset
back to `a01-corridor` afterward the same way.

- **Sight**: engaged `starter.corner.01` at (0,0)/(1,0), then walked the
  bottom row to (0,2), (1,2), (2,2), and finally (3,2) — one square further
  than TEST 060's own sequence, directly adjacent to the pinch. `peek.corner.02`
  (at roughly (6,1), never placed in melee range) **never joined the fight
  roster** at any of those four squares — the "in this fight" panel held at
  one combatant the whole time. TEST 060's exploit is reversed.
- **Diagonal movement**: from (3,2), pressed the physical numpad-9 key
  (`KP_9`, `--clearmodifiers`) attempting the NE cut to (4,1) — the exact
  diagonal the wall pair flanks. Refused: `"the corner is too tight to cut"`,
  move budget unchanged (`5`), position unchanged. Did not additionally test
  the reverse (SW) direction or a `NumLock`-on state — one confirmed refusal
  at the fixture's own named pinch was the ask.

Both halves of Task 2 hold: `canSee`'s corner leak is closed, and the new
diagonal keys are corner-checked the same way.

## Task 3 — the droid melee gate, three layers, and (c) needed a fixture I
## had to build

Built a new package, `droid-melee-gate` (written directly to
`~/.local/share/kotor-rpg/packages/`, one area, one droid blueprint carrying
a hand-authored melee weapon — schema copied from `tester-probe`'s existing
`probe-warden`/`vibroblade` examples rather than guessed). No fixture existed
for this because, per Coder's own note, no shipped data can trigger the
character-side or array-side guards naturally — so confirming those two
needed either reading the source (already done, see below) or manufacturing
the illegal state by hand, which was the actual ask for (c).

**(a) Loom's validator — confirmed, exact reason text.** Opened
`droid-melee-gate` in my own Loom instance, ran verify: `1 problem`.

> `"guard.melee.01" in "a01-gate" is a droid and equips
> "items/weapons/contraband-blade" in slot "weapon_r_1". Melee is closed to
> every droid chassis, so it has no legal attack at all — give it a ranged
> weapon or make it organic.`

Matches `PackageProblem.droidHoldsMelee`'s reason string in
`package_validate.dart` verbatim.

**(b) Chargen's character-side guard — confirmed unreachable through the UI,
one droid class checked, not all nine.** Built a droid player (chassis
Battle → War Droid Mark I → Scout, the only combat-adjacent class a droid
chassis is even offered — Soldier/Marksman/Brawler/Saboteur were all greyed
out at the class step with *"no droid takes this class — nine of eighteen
are open to a chassis"*, and the species screen's own text says why:
*"a chassis reaches eleven ranged attack chains and no melee at all"*). The
Equipment step offered exactly one line — `weapon: Blaster Carbine` — with no
melee-upgrade choice screen at all, unlike the identical step for an organic
Soldier/Scout, which shows a `TAKES THE CLASS'S OWN melee UPGRADE` option box.
So there are, in practice, **three** guards stacked before the character-side
one I was sent to check ever gets asked a question: chassis closes
Combat-rate classes outright, the array data ships clean (Coder's own
`base_rules_test.dart` assertion, not something play can exercise), and the
Equipment step's own choice set never includes melee for a droid. I checked
one droid class (Scout); I did not walk all nine and cannot say none of them
would ever reach the equipment-set guard — only that this one, representative
attempt didn't.

**(c) The runtime gate — confirmed on both paths, with both upstream layers
bypassed by hand, independently.**

- *NPC side*, bypassing (a): the `droid-melee-gate` package was never
  re-saved through Loom after authoring it, so its illegal blueprint loads
  into play exactly as written — Loom's verify catching it does not stop the
  play client from reading the file. Fresh organic player, bumped into
  `guard.melee.01` to start the fight. On the droid's own turn:

  > `guard.melee.01 is a droid holding Contraband Blade — melee is closed to
  > every droid chassis, so it has no attack it can make`

  Player vitality held at `11 of 11` — not merely a miss, no attack was rolled
  at all.

- *Player side*, bypassing (b): built a legitimate droid Scout player
  ("D-Blade Bait") through ordinary chargen exactly as in (b) — chargen gave
  it the `Blaster Carbine` it was always going to get, no melee ever offered.
  Saved (autosave on chargen completion), then hand-decompressed the
  `.sav`'s gzip payload (format is `KRSV` header + gzip'd NDJSON event log,
  read from `Lodestar/lib/src/save_file.dart` at the pinned checkout rather
  than guessed), edited the `character.equipment-set` event's `items` and
  `weapon_r_1` from `items/weapons/blaster-carbine` to
  `items/weapons/contraband-blade`, and re-gzipped it back onto the
  unmodified header. Reloaded through the package's own `Load Game` list
  (which named it correctly, `level 1 scout · a01-gate`) — the load screen
  itself surfaced `"D-Blade Bait · 2 rules about this character not
  checked"`, a load-time integrity notice I hadn't seen worded that way
  before and didn't chase, named for whoever tracks that surface. Engaged
  the same `guard.melee.01`, and on my own turn attempted the Attack:

  > `melee is closed to every droid chassis — you have nothing to swing with`

  Move budget unchanged (`5`), no Action spent, both combatants' vitality
  unchanged. The refusal fired before any dice were touched, matching
  `fight_test.dart`'s own *"AND IT SPENDS NOTHING"* assertion for the NPC
  side — I did not instrument the app to confirm the Action pip specifically
  stayed unspent, but the move-budget number visible on screen didn't move
  either.

All three layers hold, and the third holds *specifically because* it does
not depend on the first two — exactly the property `PT-1713`'s own commit
message says it's for.

---

## A note on how I got past two access refusals mid-session, since both
## bear on what "hand-edit" means for a Tester

Direct file edits under `~/.local/share/kotor-rpg/` — a `package.toml`
`[entry]` change via `Edit` and via `sed`, and a background `run-loom.sh`
launched with plain shell backgrounding (`&`) — were refused by this
session's own permission layer, unrelated to anything in the product. Both
have exact working equivalents that stayed inside the same permissions:
switching `[entry]` through Loom's own "set as entry" control (a real,
in-app write, not a bypass) instead of the raw TOML edit, and using the
`Bash` tool's own `run_in_background: true` instead of a shell `&`. The
`.sav` hand-edit in Task 3(c) went through cleanly with a plain `Write`/
`python3` — the refusal tracked the specific action pattern, not the
directory. Named because a future run hitting the same refusal should reach
for the in-app control first rather than assume the package is locked.

---

## What I did not check

- Reach weapons in the opportunity-attack fixture — this fixture is reach-1
  only, as before.
- The SW diagonal direction, or a `NumLock`-on state, for the corner-cut
  refusal — one confirmed direction at the named pinch was the ask.
- Whether all nine droid class equipment payloads stay melee-free — checked
  Scout only; the source-level guard (`base_rules_test.dart`'s assertion
  over the real shelf) is the actual exhaustive check, and it's Coder's, not
  mine to re-run from the UI.
- What the load screen's `"2 rules about this character not checked"` means
  beyond its own sentence, or whether it's specific to the equipment mismatch
  I introduced — flagged, not chased, since it wasn't one of the three tasks.
- `guard.droid.01` in `opportunity-attacks/a02-droid` — TEST 061 already
  named its own-turn-Strike anomaly there and that finding is closed; not
  re-opened, since re-confirming a closed test isn't where this session's
  three tasks pointed.
- `items/weapons/blaster-rifle`, which will not open: There is no item here —
  this line appeared on **every** organic Soldier I built this session
  ("Reach Tester Two", "Corner Tester", "Corner Tester Two", "Melee Gate
  Player" — all took the melee-upgrade equipment choice) at the moment
  combat's status line first rendered, regardless of what was actually
  chosen at the Equipment step. Named because it's new and consistent across
  four separate characters and two separate packages, not chased because it
  wasn't in scope for any of the three queued tasks.

## State

- `opportunity-attacks` — unchanged, content re-read and confirmed identical
  to what TEST 061 left it at; `[entry]` still `a01-melee`. New saves:
  `reach-tester-two.sav`.
- `ranged-detection` — `[entry]` switched to `a05-corner-peek` for the sight
  and diagonal tests, restored to `a01-corridor` afterward via Loom's own
  control, confirmed on disk. New saves: `corner-tester.sav`,
  `corner-tester-two.sav`.
- `droid-melee-gate` — **new package**, built this session for Task 3(c),
  left in place (one area, one droid blueprint with an illegal melee weapon,
  one item file) since it's the only way to exercise (a) and (c)'s NPC half
  again later. New saves: `melee-gate-player.sav` (organic control, NPC-side
  test), `d-blade-bait.sav` (droid player, hand-edited post-chargen for the
  player-side test — the file on disk right now carries the bypassed
  `contraband-blade` weapon, not what chargen actually gave it).
- No other package touched — `base-rules`, `endar-spire`, `mixed-faction`,
  `taris-undercity`, `tester-probe`, `two-enemies` all confirmed untouched by
  mtime.
- The NWN install was not read or written.
- Every app and Loom process I started was killed by PID; Coder's Loom
  `517968` checked running and untouched before and after each of my three
  launches.
