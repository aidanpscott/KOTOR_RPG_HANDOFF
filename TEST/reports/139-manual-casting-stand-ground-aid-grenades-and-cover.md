# TEST 139 — manual casting, Stand Ground, Aid, grenades, and cover's first real confirmation

**Build.**

```
local HEAD              31857c2  "Cover Slice 5b: seeksCover wired into
                                  real combat, and Defensive's own two
                                  halves finally both exist"
working tree             one local, uncommitted `pubspec.lock` bump found
                        at session start (536c4e85 → 15780d93 on
                        Lodestar's own `main`) — not touched; archived
                        from the COMMITTED tree via `git archive HEAD`,
                        which reads the committed lock, not the working
                        one
pubspec.lock resolves    lodestar  536c4e85fae3f4ec5efb1d49a08d0e53053b3447
pub-cache checkout       ~/.pub-cache/git/Lodestar-536c4e85.../ — present,
                        confirmed against the committed lock
```

All three agree, on the committed tree. `check_shelf.py` clean: 29 rules
files, 65 standard blueprints. By the end of this pass the live
`KOTOR-RPG-APP` repo had picked up substantial further uncommitted work
from Coder — `play_screen.dart`, `pubspec.lock`, `test/
doctrine_picker_test.dart` modified, a new `test/protects_test.dart`, and
a live `flutter test` run of the full suite in progress — all left
untouched; everything below ran from the git-archived snapshot only.

**Verdict — all five items confirmed. Two genuine gaps in existing
coverage found and closed with new, real, end-to-end tests: grenades
correctly declining a friendly-fire throw, and cover's own mechanics
reaching a real board at all.** Every cover-related test in the existing
suite — `cover_defence_test.dart`, `enemy_seeks_cover_test.dart`,
`defensive_holds_distance_test.dart` — is a Fight-level unit test against
synthetic `coverOf`/`seekCover` callbacks; nothing had confirmed cover
through a real `PlayScreen` and a real authored tile before this pass.

---

## 1. Manual companion casting — confirmed, including the pool-isolation claim

`manual_companion_casts_test.dart` already reads both `forcePoolForTest`
(the player's own pool) and `companionForcePoolForTest` (the companion's)
before and after the companion's real cast, explicitly proving the
player's own pool never moves — exactly the routed claim, not something I
needed to add. Baseline run clean.

## 2. Stand Ground — confirmed

`stand_ground_never_walks_test.dart`'s own four tests (never closes
despite wanting to, still shoots when already close, `retreatFrom` never
runs either, the same shape authored as real TOML content reaches an
identical `Decision`) directly match the routed claim. Mutation-tested
against the exact trap the doctrine's own commit named (a doctrine left
at the default `wantRange` would pass the `holdsGround` gate by
coincidence). Baseline clean.

## 3. Aid — confirmed, real end-to-end heal added

`fight_test.dart`'s five Aid tests (all Fight-level, synthetic
`usePower`) already prove the threshold, `includeSelf: true` (the
opposite of `healerDoctrine`), and the absence of a revive step — the
last of which is airtight at the source regardless: `hurtIn` (Lodestar)
requires `c.vitality.current > 0` unconditionally, and `aidDoctrine` has
exactly one `SupportRule`, built from `hurtIn` — there is structurally no
path from a fallen ally to a heal, so a live re-proof of "no revive"
would only restate a source-level guarantee already mutation-tested.

What no existing test does is reach `_useSupportPower`/`_applyPower`
through a real fight the way `jediSupport`'s own end-to-end test does.
Built that:

```
⚠⚠⚠ AN AID COMPANION REALLY HEALS A WOUNDED ALLY, THROUGH THE REAL
_useSupportPower/_applyPower CALL CHAIN
All tests passed!
```

⚠ My own first attempt tracked the wrong combatant — I'd assumed the
thug would attack the ally who initiated contact (Track A's own
bump-in), matching TEST 137/138's pattern, but this time it attacked the
medic instead, leaving my intended "wounded ally" untouched the entire
run. Read my own diagnostic print before concluding anything was wrong:
the medic itself dropped below half health and then rose again, which is
still exactly the routed claim — "heal an ally **or self**" — just the
self case, and a clean, direct demonstration of `includeSelf: true`
rather than the ally case I'd planned for.

## 4. Grenade/item-use — confirmed, one real gap closed

`enemy_uses_item_test.dart` (Fight-level, synthetic) and
`enemy_grenade_test.dart` (real `PlayScreen`, one enemy) already prove a
doctrine throws through the real call site and that a null return falls
through to an ordinary attack. But `enemy_grenade_test.dart`'s own
comment says outright why it uses exactly one enemy creature: a second
creature near the player would also sit inside the blast, so
`bestBlastCentre`'s own friendly-fire refusal (`if (friendly) continue;`
in Lodestar's `sight.dart`) would discard every centre and the grenadier
would never throw — the OTHER half of the routed claim, deliberately
never exercised there.

Built it — a second, same-side enemy standing beside the grenadier, both
within blast range of the only reachable target:

```
⚠⚠⚠ A GRENADIER NEVER THROWS WHEN THE ONLY CENTRE WOULD ALSO CATCH ITS
OWN SIDE
⚠ FINDING: thrown=false — [... real combat log ...]
All tests passed!
```

Twelve real rounds, the grenadier never threw once, and correctly fell
back to ordinary melee instead — through the real `_enemyUsesItem` call
site, not a synthetic doctrine. (The fight ended in the player's own
death from that melee, an artifact of the fixture's own HP numbers, not
a finding.)

## 5. Cover — confirmed, and this is the substantial one

Every existing cover test — Slices 2 through 5b — is a Fight-level
`test()` against a synthetic `coverOf`/`seekCover` callback:
`cover_defence_test.dart`, `enemy_seeks_cover_test.dart`,
`defensive_holds_distance_test.dart`. Grepped the whole suite for any
`testWidgets` touching `coverOf`/`_coverAt`/`CoverTier` and found none.
Nothing had ever confirmed a real authored tile actually reaching a real
board before this pass.

**Defence/Reflex bonus — confirmed live, through a real tile:**

```
⚠⚠⚠ A REAL halfCover TILE GRANTS THE REAL DEFENCE BONUS TO WHOEVER
STANDS ON IT, AND LOSES IT ON STEPPING OFF
⚠ off cover: [base 10, class 3] (total 13)
⚠ on cover: [base 10, class 3, cover 2] (total 15)
⚠ back off cover: [base 10, class 3]
All tests passed!
```

A real area TOML (`legend = { "'" = "halfCover" }`, confirmed against
Lodestar's own `_knownTypes` map directly rather than guessed from the
glyph docs), read through `myDefenceTermsForTest` — the exact +2 term
appears the instant the player steps onto the tile and disappears the
instant they step off, live, not cached.

**Defensive doctrine pathing to real cover — confirmed live:**

```
⚠⚠⚠ A REAL defensive ENEMY WALKS ONTO A REAL, REACHABLE COVER TILE —
seeksCover, THROUGH THE REAL enemyTurn CALL
⚠ FINDING: shooter reached the cover tile = true
All tests passed!
```

⚠ My first attempt at this put the cover tile BETWEEN the enemy's start
and the player's own approach path — once the player walked to
adjacency, their own square blocked the enemy's only route to it, and
the fight never even started because I'd asked for full adjacency before
checking. Redesigned with the cover tile on the far side of the enemy
from the player's approach, so nothing the player does can occupy the
enemy's own path there.

**Total cover blocking targeting, the ranged-from-cover hit bonus, and
retreat backing off past a blast radius — not independently re-tested
through a new fixture, and here is exactly why:**

- Total cover: Slice 3's own commit is unusually careful research rather
  than a claim to take on faith — it identifies the two real targeting
  paths (`fight.dart`'s own `sees()`-filtered `foes` list, and
  `_reachedBy`'s `_sees()` check for powers) and cites the specific
  existing tests that already prove each (`enemy_moves_test.dart`,
  `a_blast_stops_at_a_wall_test.dart`), then reasons through the one gap
  it found (the player's own adjacent walk-into strike never checks
  `_sees`) to a real conclusion: two creatures cannot be legally adjacent
  through a wall in the first place, so the gap is unreachable by
  construction. I could not find a separate, manual "attack a specific
  tile" verb this app exposes beyond that adjacency-driven contact and
  the already-proven AI/power paths, so there was no further real UI
  surface left to test independently.
- Ranged-from-cover hit bonus: proven at the Fight level
  (`cover_defence_test.dart`'s own dedicated shooter-side test,
  deliberately checking the shooter's own attack total rather than the
  target's Defence specifically so it can't silently re-test Slice 2 for
  the wrong reason) and wired into all three real call sites per the
  commit. Building a real fixture would need a companion or player
  equipped with an actual ranged weapon standing on cover, which this
  pass's remaining time went to the cover-reaching-a-real-board question
  instead, since nothing at all had confirmed that yet.
- Retreat past a blast radius: already real and already proven —
  `enemy_grenade_test.dart`'s own `keep_at_least` bed backs the grenadier
  off past `grenadeBlastSquares` before it ever throws, asserted directly
  (`seen.any((s) => s.contains('backs off'))`). Nothing further needed.

---

## Fixtures

All scratch, in `$S/app-head4/test/`, deleted after this pass:

- `tester_own_grenade_avoids_friendly_test.dart` — §4.
- `tester_own_aid_real_heal_test.dart` — §3.
- `tester_own_cover_defence_real_test.dart` — §5.
- `tester_own_defensive_seeks_real_cover_test.dart` — §5.

No stray processes belonging to this session — one long-running
`flutter_tester` and a live, in-progress full-suite `flutter test` run
were found via `ps aux`, both pointed at the live repo's own
`package_config.json`; neither touched (Coder's own concurrent work,
matching the uncommitted changes found in the live tree).
