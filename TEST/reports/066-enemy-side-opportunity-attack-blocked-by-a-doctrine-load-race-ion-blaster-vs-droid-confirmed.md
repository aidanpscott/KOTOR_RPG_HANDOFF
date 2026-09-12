# TEST 066 — the enemy-side §10 opportunity attack couldn't be driven, and why;
# door-crossing-mid-fight and PT-1740's Ion Blaster vs-droid bonus both confirmed

**Built against:** `run-app.sh` (always rebuilds). KOTOR-RPG-APP `d875bfb`
(*PT-1745 — a conversation recruits, and all four effect paths land the same
way*). `pubspec.lock`'s `lodestar` pin: `resolved-ref ea486f79...`, which is
also Lodestar's own current HEAD (`ea486f7`, *item_test — the compound-damage
case asserted the refusal PT-1740 overturns*) — checked directly against
`.dart_tool/package_config.json`'s `rootUri` for the actual compiled
checkout, and all three agree. No Loom involved this session — the one
validator finding below was read from `package_validate.dart`'s source, not
observed live in Loom's UI.

App PID `32202`, killed by PID at the end of the session, confirmed gone.
Coder's Loom (`12445`, wrapper `12443`) checked running, untouched, before
and after.

---

## 1. Primary task — enemy walks past a companion to reach the player, drawing a
## Strike — NOT driven. Two real findings block it, not a fixture problem.

Built `companion-fixture` (mine, from an earlier session) around this exact
scenario: `mate` (companion, `role = "henchman"`) sits between `chaser` (a
second hostile) and the player, so `chaser` closing on the player specifically
has to leave `mate`'s reach on the way. I own this package and iterated on it
in place rather than reverting — same standing practice as reusing
`opportunity-attacks`/`two-enemies` across sessions.

**Finding A — a doctrine attached to the creature the player bumps never
takes effect, because it's loaded without `await` and the fight starts
before the read finishes.**

`play_screen.dart`'s walk-into handler:

```
if (_doctrine == null && target.doctrine != null) _loadDoctrine(target);
...
_fight == null ? _begin(target) : _playerStrikes(target);
```

`_loadDoctrine` is `Future<void>`, does `await f.readAsString()`, and is
fired **without** `await` at the call site. `_begin` runs synchronously
right after, in the same call stack, and constructs `Fight(doctrine:
_doctrine ?? plainAggression, ...)` — `Fight.doctrine` is `final`, set once.
File IO cannot complete before the next synchronous line runs, so `_begin`
always captures `_doctrine == null` and falls back to `plainAggression`,
regardless of what's authored. The later `setState(() => _doctrine = ...)`
updates a state variable nothing reads again.

I confirmed this isn't theoretical: I attached a custom doctrine
(`hunt-player.toml`, `[[prefer]] match = {role = "player"}`) to `chaser`
first, saw plain-aggression behaviour anyway, then re-read `_alsoInContact`/
`_wouldFight`/`_detectAtRange` and found the doctrine is loaded **only** via
this one walk-into call site — a creature that joins by detection (as
`chaser` does here) never has its own doctrine read at all, only whichever
one (if any) got attached to the creature the player actually bumped. I
moved the attachment to `starter` (the one bumped) instead, since `Fight`
holds exactly one `Doctrine` for the whole encounter, applied on every
enemy's turn (`fight.dart`, `decide(doctrine, ...)` in `enemyTurn`) — and
still got plain-aggression results, which is Finding A: the load never
completes before `_begin` reads it, for *any* creature, bumped or not.

**Finding B — even under the working fallback, `AnyEnemy()`'s "first in
initiative order" makes targeting proximity-blind, and in this fixture
initiative consistently favours the companion.**

With `plainAggression` in effect, `foes` for both hostiles is `[mate,
player]` in the fight's fixed initiative order (`mate` rolled 13, the player
9, three separate fresh-chargen attempts in a row — the underlying dice
read as deterministic for this exact build sequence, not re-rolled by
leaving and re-entering the encounter). `AnyEnemy()` takes `pool.first`, so
both `starter` and `chaser` target `mate` every time, never the player — a
companion happening to out-roll the player in initiative is enough to make
the requested direction (enemy leaves the companion's reach *because it's
making for the player specifically*) unreachable by data alone, without a
working per-creature or per-fight doctrine override (blocked by Finding A).

**What I did confirm, as a side effect:** the opportunity-attack mechanism
itself fires correctly for a companion as either party — `starter`
approaching `mate`, drawn away from the player's own reach and then away
from `mate`'s, produced ordinary Strikes each time a mover's start-in/end-out
distance changed, matching `_reachSnapshot`/`_opportunities`'s single
before/after comparison. The literal mover=enemy/watcher=companion/
destination=player permutation specifically is what Findings A and B block.

`companion-fixture`'s doctrine attachment now lives on `starter` (not
`chaser`), with `hunt-player.toml`'s own comment updated to record Finding A
so a future session doesn't re-attach it to the wrong creature expecting a
different result.

## 2. Secondary — companion crosses a door mid-fight — CONFIRMED, quick look

Started a fight (bumped `starter`, `mate` joined), then walked the player to
`a01-corridor`'s door with the fight still live (`starter`/`chaser` both
standing). Crossing produced no `in this fight` panel in `a02-second-room` —
fight abandoned — and `mate` appeared beside the landing point at its
pre-crossing vitality (54 of 60), carried by `_bringTheParty` rather than a
declared placement (the second room's own `[[contents]]` never mentions
`mate`). `starter`/`chaser` did not follow. Reproduced a second time in the
`ion-vs-droid` fixture below (`shooter` crossed `a01-organic`'s door mid-fight
at 27 of 40, landed beside me in `a02-droid`, `organic-target` did not
follow) — same shape, different package, so this isn't an artifact of one
fixture's geometry. Matches exactly what Coder named as correct-but-worth-
knowing per §4.

## 3. New task — PT-1740's Ion Blaster vs-droid conditional damage — CONFIRMED

Built `ion-vs-droid` (new, mine): `shooter` (role=henchman, `[equipment]
weapon_r_1 = "items/weapons/ion-blaster"`, item blueprint `base =
"ion-blaster"`) starts adjacent to the player in `a01-organic`, whose only
hostile is `organic-target` (species=human) — a single-foe fight, so
targeting ambiguity (Findings A/B above) can't interfere. A door carries
`shooter` into `a02-droid`, whose only hostile is `droid-target`
(species=droid), for the other half of the comparison.

**Vs organic**, the clean derivation line, after several rounds:

> `shooter.organic.01: Ion Blaster · rolled 13 — d20 12 + attack 1 +
> Dexterity 4 − point blank 4 · needed 12 · 1 square, increment 8 — hit ·
> damage 3 — 1d4 3 · 0 left`

Base `1d4` only — no `+ NdM vs <kind>` clause at all, matching
`DamageOutcome.line`'s own shape for an empty `bonusFaces`. `organic-target`
died to that hit.

**Vs droid**, after crossing the door:

> `shooter.organic.01: Ion Blaster · rolled 15 — d20 14 + attack 1 +
> Dexterity 4 − point blank 4 · needed 12 · 1 square, increment 8 — hit ·
> damage 6 — 1d4 4 + 1d10 vs droid 2 · -5 left`

The bonus clause fires — `+ 1d10 vs droid 2` — and only against the droid.
Between the two hits, the same weapon, same wielder, same `resolveAttack`
call site, differing only in `targetIs` (read from `p.species == 'droid'`,
`attack.dart:157`): bonus present against `droid-target`, absent against
`organic-target`. This is the direct confirmation of my own `TEST 065`
finding, now built as Coder said it would be.

One authoring mistake of my own, not an engine finding: `a02-droid.toml`'s
first draft put its `[[connections]]` on the same square as its own
`[[arrivals]]` — `PackageProblem.twoWaysOnOneSquare`, read from
`package_validate.dart` after the Library screen flagged `ion-vs-droid` with
"1 problem." Moved the connection off the landing square; not re-verified in
Loom (none run this session) but the rule read directly against the fix
leaves nothing else it could still be.

---

## What I did not check

- Whether `_loadDoctrine`'s missing `await` also affects the
  conversation-triggered fight-start path mentioned in its own comment ("a
  fight can start from a conversation and `_begin` is synchronous") —
  reasoned from the same code, not separately driven through a conversation
  fixture.
- Whether initiative is genuinely seeded deterministically for this build or
  whether three same-shaped chargen sequences just happened to reproduce the
  same rolls by coincidence — treated as load-bearing for Finding B's report
  but not traced into the dice source itself.
- Any doctrine other than `plainAggression`/a `Prefer(role=player)` shape —
  `Nearest`, `Weakest`, and multi-`[[never]]` doctrines untested this
  session.
- `ion-vs-droid`'s critical-hit path (`× multiplier`) against either target
  kind — every hit observed this session was a normal hit, no natural-20
  came up.

## State

- `companion-fixture` — `starter.toml` now carries the `doctrine` attachment
  (moved off `chaser.toml`), `hunt-player.toml`'s comment records Finding A.
  Left as the package's working state, not reverted — mine, iterated in
  place as in prior sessions.
- `ion-vs-droid` — new package, mine, left in place: `a02-droid.toml`'s
  connection/arrival square fixed post-hoc, everything else as first
  authored. Three saves created this session across both packages
  (`dresh-rhen`, `ravik-kesh`, `corrin-solvek`) — ordinary Tester save
  artifacts, not cleaned up.
- No other package touched — confirmed by mtime against a listing taken
  before this session's edits.
- App PID `32202` killed by PID, confirmed gone. Coder's Loom (`12445`/
  `12443`) checked running, untouched, before and after.
