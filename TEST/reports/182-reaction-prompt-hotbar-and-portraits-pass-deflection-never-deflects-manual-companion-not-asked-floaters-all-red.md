# TEST 182: the reaction prompt (PT-2749 step 3), its rulings, and step 4

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-182/` (MAIN_WORK `2aea6299`), one prefix per item. The step-by-step log is `TEST/reports/182-running-log.md`.

## Build

App `7a863fc`, git archive to `~/kotor-tester/builds/test182`. Lodestar `5c676c45e857af5661301e4feeeffb140f8a6c76` = lock = compiled. Lens `5fe60a9c2be41852fd8818c1ca579a2077808d79` = lock = compiled. Loom has no entry in the lock. Shelf `1e3ffb4` (= origin), check_shelf clean (118 blueprints). `tool/env.sh` sourced. The build went through the lock (2446 s, nearly all of it waiting on Coder's `flutter test -j 1`), and `pubspec.lock` was unchanged. The fixture `dart run`s also went through the lock. The bundle was launched outside it.

Fresh fixtures: `rx-182`, `kind-182`, `defl-182` (Jedi 12 knowing Deflection and Redirection), `defl-only-182` (Jedi 6, Deflection only), plus chargen characters. New local bed `tester-kinds` (one mine per damage kind, one per condition). `tester-pass` gained a stun mine.

## Summary: eight pass, three partial, one fail, one not observed

| # | Check | Result |
|---|---|---|
| 1 | OA prompt under Ask | **PASS**: the game stops before the enemy moves. Centred K2 box: "Opportunity attack / Sentry Droid leaves your reach / one reaction · 1 left / 80% (needs 5+)", Yes / No. Enter and Y swing; Escape and N don't; Space does nothing |
| 2 | Always / Never | **PASS**: Always swings with no box; Never shows no box and makes no swing |
| 3 | Force Deflection | **PARTIAL**: defaults are right (Deflection Always, Redirection Ask). The Ask box reads "Force Deflection / Sith Trooper fires at you / 6 Force points · 37 left · spent only if the shot would hit". Yes, No and Never are wired as described, and misses spend nothing. **But no shot was ever deflected**: under Always and Ask-then-Yes the round 4 hit spent 6 Force *and* landed for 10. Also, a Jedi who knows Redirection is governed only by the Redirection row: "Deflection: Always" does nothing for them |
| 4 | Empty pool / two at once / target gone | **PARTIAL**: empty pool, no box: PASS. Two triggers at once and target-gone were not reached (needs three party members in reach at once) |
| 5 | Stunned | **NOT REACHED**: I got the player stunned with the reaction unspent, but no enemy left my reach while I was stunned. No box appeared in those rounds |
| 6 | Companions | **FAIL**: Kael under MANUAL, beside the droid that then chased me out of his reach: not asked and no swing. The droid's opportunity attack on me was the only reaction logged. The AI case was not run |
| 7 | Same dice | **PASS**: the Always run and the Ask-then-Yes run give identical logs, line for line |
| 8 | Options > Gameplay | **PASS**: K2-look page with Always / Ask / Never per reaction. Default restores Deflection to Always and the others to Ask. Settings survive a load and an app restart |
| 9 | Hotbar | **PASS**: names as ordered (Dash, Disengage, Hide, Scan, Treat, Repair, Aim, Stand up, Rest, One hour / Eight hours of meditation, End Turn; Items: Gear, Throw a grenade), each with its key. Hover box is small and above the button, with the line, the red refusal and the cost footer. Refused presses say why and spend nothing. Hidden in a conversation and at a terminal. One row at 1280x720. **Note**: resizing a running window down to 1280x720 doesn't relayout; a fresh 1280x720 window is fine |
| 10 | Sidebar | **PASS**: "move N of S" (and "move 10 of 5" after Dash); one pip per reaction, dark when spent |
| 11 | Portraits | **PARTIAL**: the red fill rises, the white chunk shows about 0.8 s, enemy wounds float nothing, and the seven icon conditions show K2 icons while the others show by name, all naming themselves on hover. **FAIL**: every damage kind's floater is the same red (#b02c0b): fire, cold, electrical, sonic, energy, light_side, dark_side, universal |
| 12 | Walking | **PASS** for sliding square by square, for the player and enemies. **L approach not observed**: the only approach in my bed was a straight run |
| 13 | Regression | **PASS**: walk up, none; step away, one; the log column; " · Flanking +2"; Continue after F4 + kill; four-way movement; one quick save |

## Findings, most important first

1. **Force Deflection never deflects** (`defl-only-182`, deterministic fight against the Sith Trooper): rounds 1–3 miss and nothing is spent. In round 4 the shot hits, Force goes 37 → 31 (max 36), and the damage lands. Same under Always and under Ask with Yes. No "Deflected" line and no deflect roll appears anywhere (`i03d`, `i03f`). If the deflect roll lost, the log should say so. If it should have won, this is a defect.
2. **A Redirection-knower ignores the Deflection row.** `_deflectFor` / `_deflectionReady` (play_screen.dart ~4867, ~9645) pick Redirection whenever it's known, so only the Redirection row decides. With the defaults, such a Jedi is asked about Redirection and never auto-deflects. With Redirection Never they don't deflect at all, though Deflection reads Always (`i03a`–`i03c`).
3. **A MANUAL companion is not asked** when an enemy leaves its reach (`i06`).
4. **Floaters are one colour for every damage kind** from a hazard (`i11d`). I couldn't produce typed weapon damage, so whether weapons colour correctly is untested.
5. **A live resize doesn't relayout** (`i09h`); the hotbar check passed on a window created at 1280x720.
6. Small: Aim's refusal in a fight reads "you can see — walk into what you mean to hit", not an Action-spent line. The OA box is drawn over the log column. "move 10 of 5" after Dash. The status line still uses the old long roll form.

## How it was run

- OA cases: one pre-fight quick save in `tester-pass` and a scripted replay (`run/rxrun.sh`) with the same inputs every time, so each setting met the same dice.
- Deflection: the same fight from one quick save per setting. Never was finally set through settings.json with the app stopped, because Gameplay clicks were taken by an open box.
- Floaters: a 10 fps recording measured the colour per mine.

Skills: `verification-before-completion`. Kept small per the simplicity rule.

## Addendum (same build, run after filing)

The open cases, closed on 7a863fc (screenshots MAIN_WORK `10f4dc29`):

- **Item 5, stunned: PASS.** Stunned beside two droids with my reaction unspent, a droid left my reach: under Ask no box and no swing; under Always (identical replay) no swing and an identical log (`i05a`, `i05b`).
- **Item 6, AI companion: PASS** for that half. AUTO Kael, with a droid leaving his reach: "Opportunity attack: Kael attacks Sentry Droid : *hit* : (10 + 2 = 12)", no box, and the turn ran on by itself (`i06c`). The MANUAL half stays a FAIL.
- **Item 12, L approach: PASS.** A droid two columns right and four rows down slid up 3 squares, then left 1, with no diagonal step (15 fps tracking, `i12b`).
- Still not reached: item 4's two-at-once and target-gone cases, which need a MANUAL companion to be asked.

## Correction (Tester, 2026-10-15, after reading CODER's TEST 182 fix entry)

- **Finding 1, "Force Deflection never deflects", was overstated.** Every one of my deflection runs replayed the same quick save, so the deterministic dice gave the same round-4 shot each time. That is one deflection roll seen several times, not a pattern. CODER measured 611 rolls in real play: 24.4% deflected against 26.3% predicted. My result is one failed roll, and 4c01d57 printed no roll, so it couldn't be told apart from a defect. ed8fc9d now logs each roll (42417).
- **Finding 3, "a MANUAL companion is not asked", is unconfirmed.** Kael's pool is one reaction per encounter, and I did not check his sidebar pip before the chase, so it may already have been spent. CODER could not reproduce it on the same bed. TEST 183 should check his pip first.
- Finding 2 (a Redirection-knower is governed by the Redirection row) is CODER's design, now stated on both Gameplay rows; it is flagged for a ruling.
