# TEST 180 running log (draft, text only)

Started 2026-10-14. Tester, Xvfb :2, own data dir (~/.local/share/tester-data), no K2, no BG3.

## Build
- App 617578e (git archive to ~/kotor-tester/builds/test180, on disk). Built through tool/one_at_a_time.sh: 11 s, no wait. pubspec.lock unchanged.
- Lodestar d8390023997fdb17e4e897bafe70f14254f494fd = lock = compiled. Lens fe10327793b1a28882b088d2fbf8148e83ead926 = lock = compiled. Loom: no entry in the app's lock.
- Shelf 1e3ffb4 (data dir, = origin HEAD). check_shelf: see below.
- tool/env.sh sourced. Bundle launched with plain & outside the lock (run/launch.sh).
- Read first: Coder's TEST 179 fix entry (PLAYTEST-RULINGS-01.md, MAIN_WORK 5c443b57). Coder flags as open: mine damage writes no vitality event (reload restores health); outside a fight there is no path line, so "Walks onto a mine" shows only in a fight.

## Items
- check_shelf: 31 rules files, 118 standard blueprints, identical.
- Local beds (my data dir only, not on Shelf): tester-mines (copy of Locked and Trapped + guard droid at (3,0) by the mines + a hidden crate at (5,4)); tester-lshape (start (0,2), droid (1,2) to bump, droid (5,0) offset, Kael henchman at (9,4)); tester-nine (nine sentry droids); tester-rough from TEST 179.
- Authored saves (one locked dart run, specs in notes/fixtures/specs180/): flank-ninety (tester-rough), lsh-ninety (tester-lshape), nine-ninety (tester-nine): Soldier 3, CON 30, Short Sword C1 + Blaster Rifle C2, 3 medpacs; boot-ninety (Store Bed, Soldier 3, Heavy Leather Armour worn, 5000 credits).

### Items 1, 2, 10 (tester-rough, Flank Ninety + Kael manual, two sentry droids)
- 1: from (6,2) at turn start, hover rough (5,1): "2 squares (3 movement) · 2 left" + "Provokes an attack from Sentry Droid" (i01-rough-label-and-legend.png). Plain (4,4): "4 squares · 1 left" (i01-plain-4-squares.png). PASS.
- 2: the legend follows the hover: "5 → 2" on the rough path, "5 → 1" on the 4-square path. After a click it reads plain "4 move" (i02-legend-after-click-and-L.png). At a turn start on (8,1), with no rough neighbour, plain "5 move" (i02-legend-turn-start-no-rough.png). BUT at a turn start next to rough ground ((5,2) and (6,2), with rough (5,1)/(6,1) above), with the pointer far off the board (1850,1000), it reads "5 → 3 move" (i02-legend-pointer-off-next-to-rough.png). Coder's entry says that is PT-1519's next-step-onto-rough preview, by design. Against the order's wording ("pointer off the board, no stale preview") it is not stale but it is a preview with no pointer: MAIN to rule. PASS for click and turn change; pointer-off shows the PT-1519 preview.
- 10 flanking:
  - Straight (me (6,3), Kael (4,3), droid (5,3)): hover "90% (needs 3+) / +3 attack · +2 Strength · +2 Flanking, against Defence 10" (i10a); my line "... + Strength 2 + Flanking 2 · needed 10 — hit" (i10b); Kael's line "Kael: unarmed · ... + Strength 1 + Flanking 2 · needed 10 — hit" (i10c). PASS. Wording: the reasons say "+2 Flanking", the lines "Flanking 2" (order said "Flanking +2").
  - Diagonal (Kael (6,3), me (8,1), droid (7,2)): Kael's line "+ Flanking 2" (i10e). PASS.
  - L (me (8,2), Kael (6,3), droid (7,2)): my line has no flanking term (i10f). PASS.
  - Ranged (Blaster Rifle from (6,3), opposite Kael): no flanking term (i10d). PASS.
  - Downed ally: not reached yet. Enemy pair flanking me: not yet.
- Findings so far:
  - The combat log panel sits on top of the board's right columns (x 1227+): it hides a droid standing at (7,2) (i14-your-turn-banner-log-hides-droid.png), most of the path to (8,4) and (8,1), and it covers the hit-chance tooltip (i13-log-covers-tooltip.png). Clicks still reach the square under it.
  - Status line after a kill ends with a raw event tag: "... · 0 left · a shot uses Dexterity, not Strength · character.died" (i10d).
- 14 (seen so far): hover banner "Sentry Droid · Level 1" with a vitality bar and "24 of 24"; red dashed melee-reach ring 3x3 including diagonals (i10a). The strip: portraits/initials in initiative order, the actor raised, hourglasses on those who have acted (i14-strip-start.png); a dead droid leaves the strip (i14-strip-dead-removed.png). "Your Turn" big centre text appears with the last enemy action banner "Sentry Droid: unarmed on Flank Ninety" still visible (i14-your-turn...).
- 13 (seen so far): the log groups by "Round N", each action line with its roll line beneath; it keeps every line (rounds 1-4 scroll).

### Items 3-6 (tester-mines: fresh chargen Mine Eighty, Mine Two, Mine Three)
- 3a: a click at (560,600), just left of the grid, does nothing (i03a). PASS.
- 3d: outside a fight, click (3,3) from (1,1): arrived at (3,3), 11 of 11, both noticed mine squares unsprung (went round) (i03b). PASS.
- 3b: in a fight (guard droid bumped at (3,0)), hover (1,2) and (1,1) from (3,1): the route goes down column 3, along row 4, up column 0 round the mines (red past movement) (i03c). PASS.
- 3c: hover the mine square (2,2): "2 squares · 3 left / Walks onto a mine / Provokes an attack from Probe Droid" (i03d). PASS.
- 4: walked onto the mine in a fight: "goes off — d20 20 = 20 vs 15 · 3 damage · 8 of 11 · 2 more rounds"; centre line "Mine Two: 8 of 11", party bar 8 of 11 (i04a). Quick save + load mid-fight: 8 of 11, "the fight resumes — round 1, Mine Two's turn" (i04b). Outside a fight (Mine Three): "goes off — d20 7 = 7 vs 15 · 6 damage · 5 of 11"; centre and bar 5 of 11 (i04c); F4, Load: 5 of 11; app RESTARTED, Continue: 5 of 11 (i04d). PASS (better than Coder expected: the reload keeps the health). Note: after the reload the line reads "you notice Mine — 15 against 12" for a mine already sprung (not drawn).
- 5: "the Damaged Power Panel is in the way", "the Footlocker is in the way", "the Security Console is in the way" (i05a, i05b); routes go round them (i03c). A found hidden crate (no stealth) blocks: "the Shipping Crate is in the way" (i05a). An UNFOUND hidden crate (stealth 60, fresh character, no "you notice" line) does not block: I stood on its square (i05c). PASS. FINDING: the unfound hidden crate is still DRAWN ("C" at (5,4)) from the moment the area loads, for every fresh character. Lens's skip list for concealed things is built from creatures only (play_screen.dart ~line 764 walks _here). My bed's crate is the only hidden placeable anywhere (no shipped package has one).
- 6: panel header "POWER COUPLING FAULT — OUTPUT 0%" -> after the repair "POWER COUPLING ONLINE — OUTPUT 100%" (i06a). PASS. Once online the panel lists no reply at all, so its dimmed line no longer appears; the console's dimmed lines fit in full: "— you have 1 spike", "— you have 0 spikes" (i06b). PASS.
