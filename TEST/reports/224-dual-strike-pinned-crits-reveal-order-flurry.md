# TEST 224: the Dual Strike chain, the pinned Deathstroke and Power Shot beds, the reveal's order, the Flurry family

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-224/` (MAIN_WORK `e15203b2`).

## Build

- **App**: main `6b3fc20`, a worktree beside my clone. `gate.py --at 6b3fc20`: "SENDABLE"; "FOR TESTER — CORE at 6b3fc20, 5482 tests, 0 failed"; ARCHIVE last green at 6b3fc20. Lodestar `4f97619` = lock = compiled; built through the lock; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `194cc43`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test224_saves.dart` (Dual One, Dual Two, Dual Double, Deathstroke Sixteen, Power Shot Critical), pristine copies kept. Reused pristine Sneak Strike (221 script), Blade Tiers and Gun Tiers (222 script).

## Summary: all pass

| # | Check | Result |
|---|---|---|
| 1 | Dual Strike | **PASS**. Dual One (one Vibroblade): "Dual Strike · Vibroblade · rolled 28 — d20 20 + attack 8 + Strength 3 − Dual Strike 3 · needed 10 — hit · threat confirmed: rolled 21 … · damage 34 — 4d10 1+9+9+7 + Strength 4×2 × 2 critical"; "Double Strike · … − Double Strike 2 … damage 11 — 2d10 5+2 + Strength 4"; "Two-Pronged Attack · … − Two-Pronged Attack 1 … damage 15 — 2d10 5+6 + Strength 4". One swing each; Defense stays "base 10 + Dexterity 2 + class 2 = 14" under all three. Dual Two (two Vibroblades), main then "off-hand:", each "− dual-wield 3 − <tier> N". **Control**: tier 1 main "d20 1 … miss", then off hand "d20 17 … hit · damage 11 — 1d10 10 + Strength (off hand) 1", no threat. Tier 3: main "d20 3 … hit", then off hand "d20 11 … hit · threat confirmed: rolled 21 — d20 14 … · damage 12 — 2d10 5+5 + Strength (off hand) 1×2 × 2 critical": the confirmation is rolled. Dual Double (Vibro Double-Blade): two swings, both "Vibro Double-Blade"; tier 2: first "d20 15 … hit", second "d20 16 … hit · threat confirmed: rolled 18 … 4d8 … + Strength 3×2 × 2 critical"; tiers 1 and 3: second swing a miss after the first. First blow drops the target: Dual Two at the Weakling, "Dual Strike · Vibroblade · … d20 17 … hit · damage 9 — 1d10 6 + Strength 3 · −6 left · dies", no off-hand line |
| 2 | Deathstroke 16 | **PASS**. "Deathstroke · Vibroblade · rolled 27 — d20 16 + attack 8 + Strength 3 · needed 10 — hit · threat confirmed: rolled 15 — d20 4 … · damage 40 — 3d10 2+4+4 + 6d6 … + Strength 4×3 × 3 critical · 360 left · d20 13 + fortitude 2 = 15 vs 21 · stunned" |
| 3 | Power Shot critical | **PASS**. "Power Shot · Blaster Pistol · rolled 24 — d20 20 + attack 8 + Dexterity 3 − Power Shot 3 − point blank 4 … hit · threat confirmed: rolled 22 … · damage 52 — 3d8 7+5+7 + 6d6 6+3+4+6+4+1 + Dexterity 3×3 × 3 critical · 348 left · prone — d20 19 = 19 vs 21 · takes hold" (19 + 24 + 9 = 52) |
| 4 | Reveal in the Combat log | **PASS**. Sneak Strike, the opener: "Sneak Strike is hidden. / A fight begins. / Round 1 / Sneak Strike attacks Sith Sentry : *hit* : (16 + 4 = 20) / Sneak Strike damages Sith Sentry for 14 damage / Stealth Mode Deactivated (Run Enabled) / Sith Sentry attacks Sneak Strike : *miss*". The reveal appears once |
| 5 | Flurry family | **PASS**. Blade Tiers: Flurry (x1) three swings at "− Flurry 4", Whirlwind (x2) three at "− Whirlwind 2", Barrage (x3) three at "− Barrage 1". Gun Tiers: Rapid Fire (x1) three shots at "− Rapid Fire 4" (the second a confirmed critical, "2d8 1+1 + Dexterity 3×2 × 2 critical"), Open Fire (x2) three at "− Open Fire 2" (six rounds), Volley of Bolts (x3) three at "− Volley of Bolts 1" |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 61 ("reg224"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 113 of 196) |

Seen, not filed:
- In one Open Fire, shots 2 and 3 read the same, "d20 15 … 1d8 4" (366 then 359 left, so two separate hits). Five more Open Fires gave varied rolls, so I'm calling it chance.
KNOWN, not filed: "holds — none:no-target" (not reached this test); a double-blade's second end on an ordinary attack.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
