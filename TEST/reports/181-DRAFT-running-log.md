# TEST 181 running log (draft, text only)

Started 2026-10-14. Tester, Xvfb :2, own data dir, no K2, no BG3.
Read first: Coder's TEST 180 entries (PLAYTEST-RULINGS-01.md, MAIN_WORK 0b11d923): AoO gate (ranged holders make none; every enemy step checked), log column, hidden placeables, no tags ("<B> dies"), Continue writes the square on every save, kept targets, legend preview on hover only, mine victim saves as itself (but NOTE: Coder's earlier entry says a companion's Evasion/armour is not read for a mine outside a fight; the 5cde10d entry says it now is).

## Build
- App 5cde10d, git archive to ~/kotor-tester/builds/test181. Built through tool/one_at_a_time.sh: 2298 s (waited behind Coder's flutter test). pubspec.lock unchanged.
- Lodestar 29b139f22e7aeafd52867a1be390bd2bd4558b9c = lock = compiled. Lens fe10327793b1a28882b088d2fbf8148e83ead926 = lock = compiled. Loom: no entry in the lock.
- Shelf 1e3ffb4 (= origin). tool/env.sh sourced. Bundle launched with & outside the lock.
- New local beds: tester-pass (me (5,3) beside droid (5,4); droid (9,0); Kael (6,0)), tester-minek (Kael; mines 6 dmg at (3,2),(3,4), 200 dmg at (6,2),(6,4); DC 15 half), tester-minesolo (lethal mine (3,1)). Authored (one locked dart run, specs notes/fixtures/specs181/): aoo-181, evk-181 (Kael given Evasion via a feat-taken event on his tag), pwr-181 (Jedi Consular 6: force_push, force_stun, fear; 2 frag grenades, 2 medpacs; tester-rough), solo-181.

## Items

### Item 1: opportunity attacks (tester-pass, Aoo One authored; three fights from one pre-fight quick save; each creature has ONE reaction per encounter, so cases were spread across fights)
- Layout: me (5,3) bump droid A (5,4); droid B (9,0); Kael (6,0) MANUAL.
- (b) (5,3)->(6,3), diagonal to A: hover "1 square · 4 left", no provoke line; then (6,3)->(6,4), round A while adjacent: no attack (i01b). PASS.
- (c) (6,4)->(7,4), out of A's reach: hover "1 square · 2 left / Provokes an attack from Sentry Droid"; one attack: "Opportunity attack: Sentry Droid attacks Aoo One : *miss* : (7 + 1 = 8)", status "Sentry Droid catches Aoo One leaving — ..." (i01c). PASS.
- (h) Kael hit droid B (it then kept Kael); I stood at (7,1); Kael walked to (4,0); B chased him along row 0 from (9,0) past me: "Opportunity attack: Aoo One attacks Sentry Droid : *miss* : (3 + 5 = 8)" (i01h). PASS.
- (g) fight 2: move-and-attack from (5,3) onto B at (9,0) (path to (8,1), 5 squares): hover "5 squares · 0 left / Provokes an attack from Sentry Droid" (that's A, which I leave). Log: A's one opportunity attack, then "Aoo One attacks Sentry Droid : *hit* : (13 + 5 = 18)"; nothing from B on the approach (i01g). PASS. Note: the hit-chance tooltip and the enemy's hover banner overlap ("80% (nee..." hidden).
- (d) fight 2 round 2: (8,1) -> (11,1) past B: hover "3 squares · 2 left / Provokes an attack from Sentry Droid"; exactly one: "Opportunity attack: Sentry Droid attacks Aoo One : *miss* : (10 + 1 = 11)" (i01d). PASS. (I started inside B's reach, so the "enter" half is not in this run.)
- (a) fight 3: walk to (8,1) and stop beside B: log shows only A's opportunity attack (from leaving A), none from B (i01a). PASS.
- (e) fight 3 round 2: d ("disengaging — your movement provokes nothing this turn"), (8,1)->(8,3) out of B's reach: hover "2 squares · 3 left", no provoke line; no attack (i01e). PASS (B's reaction was unused; in fight 2 the same B did react in round 2, so it could).
- Seen: droid B ("noticing") took no action in round 1 of any of the three fights, even after Kael/I hit it.

### Item 2: combat log
- 1920x1080 (i02d) and 1280x720 (xdotool windowsize; i02c): the log is its own column right of the board; never over a square. PASS.
- Scroll back: after 13 rounds the top was cut off; wheel up shows "Round 1 ..." again (i02a). PASS.
- Flanking: "Sentry Droid attacks Aoo One : *hit* : (13 + 3 = 16) · Flanking +2" (one line). PASS.
- Kill: log "Sentry Droid dies"; status "... · -3 left · dies"; no dotted event kind seen in any line (i02b). PASS.
- Notes: the enemy action banner can sit over the top of the log column; the dead droid's card reads "struck down 0 of 24" while the bottom line reads "Sentry Droid: -3 of 24".
