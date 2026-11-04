# TEST 227: the P O P O alternation, the double-blade's four swings, Rapid Pair, the unarmed rules text

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-227/` (MAIN_WORK `4b89dc3a`).

## The order file did not reach me

`MAIN-TO-TESTER-TEST-227.txt` is not on this machine; I searched the disk and the repos. I had only MAIN's one-line summary, so the build and the steps below are inferred. If the order held any other step or a different hash, it was not run.

- **Hash**: the newest app main, `f7b8478`, which carries `tool/author_tester_test227_saves.dart` and `test/the_test227_beds_test.dart`. **Shelf**: origin/main `8d24198`, whose two commits since `194cc43` carry the unarmed rows.
- **Steps**: the bed script's header and `PT-2752` in the ledger.

## Build

- **App**: main `f7b8478`, a worktree beside my clone. `gate.py --at f7b8478`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at f7b8478, 5504 tests, 0 failed"; ARCHIVE last green at f7b8478. Lodestar `4d6c401` = lock; built through the lock; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `8d24198`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test227_saves.dart` (Flurry Pair, Flurry Double, Rapid Pair), pristine copies kept. My own, in tester-attacks: **Lu TwoSeven** (Soldier 7, no attacks held, a level-up to 8 waiting).

## Summary: all pass; one line not reached

| # | Check | Result |
|---|---|---|
| 1 | Flurry Pair (Vibroblade, Vibrosword) | **PASS**. Every tier swings four, main, off, main, off, each with its own weapon's die. Flurry: "Flurry · Vibroblade · … − dual-wield 3 − Flurry 4 · … 2d10 1+9 + Strength 3×2 × 2 critical", "off-hand: Vibrosword · … damage 6 — 1d12 5 + Strength (off hand) 1", "Vibroblade · … miss", "off-hand: Vibrosword · … damage 3 — 1d12 2 + Strength (off hand) 1". Whirlwind and Barrage are the same at "− Whirlwind 2" and "− Barrage 1". The off hand threatens on its own weapon's 19: "off-hand: Vibrosword · … d20 19 … threat not confirmed" |
| 2 | A target falling on a later swing | **PASS**. Weakling, Flurry: "Vibroblade · … d20 4 … miss", then "off-hand: Vibrosword · … d20 11 … hit · damage 11 — 1d12 10 + Strength (off hand) 1 · -8 left · dies", with no third or fourth swing. Combat log: one miss, one hit, "Weakling dies", then Round 6. **Control**: the turn before, the same declaration at the Weakling missed all four, so the four swings are not cut short without a fall |
| 3 | Flurry Double (Vibro Double-Blade) | **PASS**. Every tier swings four, main end, off end, main end, off end, at "− dual-wield 2" (Two-Weapon Fighting on a double-blade, §7.6), each end with the whole Strength 3. Flurry: "… 4d8 1+1+1+5 + Strength 3×2 × 2 critical", "off-hand: … miss", "… 2d8 6+2 + Strength 3", "off-hand: … miss". Whirlwind: "… 2d8 5+1 + Strength 3", "off-hand: … 2d8 4+1 + Strength 3", "… 2d8 8+7 + Strength 3", "off-hand: … 2d8 3+1 + Strength 3". Barrage ends on an off-end critical: "off-hand: … 4d8 8+6+8+2 + Strength 3×2 × 2 critical" |
| 4 | Rapid Pair (two Blaster Pistols) | **PASS**. Rapid Fire is main, off, main, off, at "− dual-wield 3 − Rapid Fire 4 − point blank 4": "Blaster Pistol · … d20 17 … damage 11 — 1d8 8 + Dexterity 3", "off-hand: Blaster Pistol · … d20 20 … threat confirmed … 2d8 1+1 + Dexterity 3×2 × 2 critical", "Blaster Pistol · … d20 9 … miss", "off-hand: Blaster Pistol · … damage 6 — 1d8 3 + Dexterity 3". The off hand keeps the whole Dexterity (§7.2a). **Control**: a plain Shoot is two: main, then "off-hand:" |
| 5 | Unarmed rules text | **PASS**. The level-up Attacks grid, Lu TwoSeven, all nine read in the app. **Body Blow**: "1d6 damage on the first attack that hits this round. Attack −3. Critical multiplier +1 …". **Hammer Blow**: "2d6 … Attack −3. Critical multiplier +1, and knockback 2 squares …". **Haymaker**: "3d6 … Attack −3. Critical multiplier +1, knockback 4 squares …". **Uppercut, Nerve Strike, Blackout**: "Threat span +1", "+2", "+3". **Combination**: "Three strikes unarmed, each +2 attack if the previous hit. Attack −4, Defense −2". **Chain Punch**: "Three strikes … Attack −2, Defense −1". **Rain of Blows**: "Three strikes … Attack −1, Defense −1. If all three hit the target is Slowed …". Text only; none of these was played |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 64 ("reg227"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 102 of 196) |

**Not reached**: the silent flee and breakoff lines. Nothing fled or broke off in these fights, so I saw neither the old raw lines nor their absence. A search of the Combat log text for raw "word:word" keys found none.

My slip, no finding: in the Flurry Pair run, a Left after the Weakling died walked her off her square, and the Brute's opportunity attack followed. It's left out of the results above.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
