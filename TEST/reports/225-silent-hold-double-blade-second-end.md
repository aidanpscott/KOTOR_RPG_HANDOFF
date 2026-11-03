# TEST 225: the silent no-target hold, the double-blade's second end

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-225/` (MAIN_WORK `116f48d7`).

## Build

- **App**: main `fad3245`, a worktree beside my clone. `gate.py --at fad3245`: "SENDABLE"; "FOR TESTER — CORE at fad3245, 5489 tests, 0 failed"; ARCHIVE last green at fad3245. Lodestar `4f97619` = lock = compiled; built through the lock; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `194cc43`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test224_saves.dart` rerun (Dual Double), with pristine copies kept. Pristine Sneak Strike (221 script). My own, in tester-attacks, since Dual Double holds only the Dual Strike tiers: **Flurry Double** (Soldier 8, Str 16, Flurry, Whirlwind and Barrage, a Vibro Double-Blade alone) and the control **Flurry Two** (the same, with two Vibroblades and Two-Weapon Fighting).

## Summary: one finding (the Flurry order is P P P O, not P O P O, for two weapons too)

| # | Check | Result |
|---|---|---|
| 1 | Silent hold | **PASS**. Sneak Strike walks in seen (the fight starts on sight); on her turn, s → "hidden — d20 5 + Stealth 8 + Dexterity 4 = 17 beat 13"; End Turn four times. Combat log: "A fight begins. / Round 1 / Sneak Strike is hidden. / Round 2 / Round 3 / Round 4", with no sentry line. A grep for "word:word" in the log finds nothing. The box is empty after the turns; she stays at 32 of 32 |
| 2 | Double-blade's second end | **PASS on Strike and Dual Strike; FINDING 1 on the Flurry family**. Dual Double, ordinary Strike: "Vibro Double-Blade · rolled 28 — d20 20 + attack 8 + Strength 3 − dual-wield 3 · … threat confirmed … 4d8 1+1+1+5 + Strength 3×2 × 2 critical", then "off-hand: Vibro Double-Blade · rolled 11 — d20 3 + attack 8 + Strength 3 − dual-wield 3 · … hit · damage 12 — 2d8 3+6 + Strength 3"; again "… d20 15 … damage 11 — 2d8 4+4 + Strength 3", then "off-hand: … d20 1 … miss". Each is at −3 with the whole Strength 3. Dual Strike: "Dual Strike · Vibro Double-Blade · … − dual-wield 3 − Dual Strike 3 · … hit · damage 7 — 2d8 3+1 + Strength 3", then "off-hand: Vibro Double-Blade · … − Dual Strike 3 · … miss". Flurry family: **FINDING 1** |
| 3 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 62 ("reg225"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 129 of 196) |

## Findings

1. **The Flurry family's off end comes last, P P P O, not P O P O, and two weapons do the same.**
   - Flurry Double, Flurry (x1): "Flurry · Vibro Double-Blade · … − dual-wield 3 − Flurry 4 · hit", "Vibro Double-Blade · … − Flurry 4 · hit", "Vibro Double-Blade · … − Flurry 4 · miss", "off-hand: Vibro Double-Blade · … − Flurry 4 · hit · damage 11 — 2d8 2+6 + Strength 3".
   - Whirlwind (x2) and Barrage (x3) are the same: three main swings, then one "off-hand:" swing (`t225-fd-t1/2/3-crop.png`).
   - The control, Flurry Two (two Vibroblades), Flurry: "Flurry · Vibroblade · … hit", "Vibroblade · … hit", "Vibroblade · … miss", "off-hand: Vibroblade · … miss" (`t225-ft-t1-crop.png`).
   - So the double-blade does add the off end as two weapons do, but both give four swings in the order P P P O, against the order's P O P O.

Seen, not filed:
- Kept for Coder, as MAIN asked: TEST 224's identical Open Fire shots. The save is `notes/saves225/gun-tiers-dupe.sav` (= the 222 Gun Tiers, gunSeed 1, md5 fa624aac…), and the steps are load, bump, End Turn, x1 swing, End Turn, x2 swing.

KNOWN, not filed: the flee and breakoff raw keys (not reached).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
