# TEST 222: tiers 2 and 3 of the five attack chains, level-up refusals, hidden and reveal, save terms, the Force Slow line

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-222/` (MAIN_WORK `758fad49`).

## Build

- **App**: main `238f68e`, a worktree beside my clone. `gate.py --at 238f68e`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 238f68e, 5472 tests, 0 failed"; ARCHIVE last green at 238f68e. Lodestar `46a00fb` = lock = compiled; built through the lock in 10.4 s; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `194cc43`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test222_saves.dart` (Blade Tiers, Gun Tiers). Pristine 221 copies of Power One, Fearless One and Sneak Strike (the 221 script changed only in its comment). My own, in tester-attacks: **Immune Tiers** (Gun Tiers' build holding Precise Shot, Sniper Shot and Assassinate, with the brute holding Force Immunity: Stun, as in Immune One); **Lu Three** (Soldier 2, tier 1s, a level-up to 3 waiting), **Lu Sevenb** (Soldier 6, tiers 1 and 2, a level-up to 7 waiting), **Lu Eight** (Soldier 7, tiers 1 and 2, a level-up to 8 waiting).

## Summary: all pass; two small items; two parts not reached

| # | Check | Result |
|---|---|---|
| 1 | Blade tiers | **PASS, one part not reached**. Whirlwind (x2): three swings, "Whirlwind · Vibroblade · rolled 23 — d20 14 + attack 8 + Strength 3 − Whirlwind 2 · needed 10 — hit", the next two "Vibroblade · … − Whirlwind 2"; Defense "Whirlwind -1 = 13". Barrage (x3): three swings at "− Barrage 1"; Defense "Barrage -1 = 13". Wounding Strike (x5): one swing, "damage 11 — 1d10 5 + 1d6 2 + Strength 4 · 330 left · d20 12 + fortitude 2 = 14 vs 21 · stunned"; Defense "Wounding Strike -2 = 12"; a d20 17 threatened and confirmed ("2d10 10+2 + 2d6 4+1 + Strength 4×2 × 2 critical"). Deathstroke (x6): "damage 23 — 1d10 9 + 2d6 5+5 + Strength 4 · … stunned"; a confirmed critical "3d10 7+7+9 + 6d6 … + Strength 4×3 × 3 critical · … d20 14 + fortitude 2 = 16 vs 21 · stunned"; d20 17 threatened, d20 15 didn't; Defense "Deathstroke -3 = 11"; the brute's line "needed 11 (-3 Deathstroke)". **Not reached**: a d20 16 under Deathstroke (the one roll that tells +3 from +2) in about 20 swings over two runs |
| 2 | Gun tiers | **PASS, one part not reached**. Open Fire (x2): three shots at "− Open Fire 2"; Defense "Open Fire -1 = 14". Volley of Bolts (x3): three at "− Volley of Bolts 1"; Defense -1. Sniper Shot (x5): "1d8 4 + 1d6 6 + Dexterity 3 · … d20 1 + fortitude 2 = 3 vs 20 · stunned", Defense -2. Assassinate (x6): "1d8 7 + 2d6 3+3 + Dexterity 3 · … 11 vs 20 · stunned", Defense -3. Power Shot (x8): "− Power Shot 3", "1d8 1 + 2d6 6+2 + Dexterity 3 · 325 left · prone — d20 16 = 16 vs 21 · takes hold"; the brute knocked 4 squares, clicked where it landed. Blast (x9): "1d8 8 + 3d6 5+1+4 + Dexterity 3"; confirmed critical "3d8 8+6+8 + 9d6 … + Dexterity 3×3 × 3 critical · 260 left · prone — d20 20 = 20 vs 21 · shaken off", and again "… × 3 critical · 95 left · prone — d20 10 = 10 vs 21 · takes hold". Immune Tiers (brute holding Force Immunity: Stun): Precise Shot "12 vs 20 · resists", Sniper Shot "13 vs 20 · resists", Assassinate "15 vs 20 · resists" (failed saves); passed saves also "resists". **Not reached**: Power Shot's × 3 (a Blaster Pistol threatens on 20 only; no 20 in 23 Power Shots) |
| 3 | Level-up | **PASS**. Lu Three to level 3: Power Shot, Sniper Shot, Open Fire, Wounding Strike, Whirlwind and Forceful Slash each read "Prerequisites: Character Level 4", red; Add Attack on Power Shot and on Whirlwind leaves "Remaining Attacks 1". Lu Sevenb to level 7 (holding the tier 2s): Blast, Assassinate, Volley of Bolts, Deathstroke, Barrage and Crushing Blow each read "Character Level 8" and nothing else, red; Add Attack leaves "Remaining Attacks 1". Control: Lu Eight to level 8, Blast → "Remaining Attacks 0" |
| 4 | Hidden and reveal | **PASS, small items 1 and 2**. Sneak Strike: s → "hidden"; ten steps right; walking into the sentry: the box heads "Stealth Mode Deactivated (Run Enabled)", then "Sith Sentry: unarmed · rolled 5 … needed 16 — miss". Messages shows "Stealth Mode Deactivated (Run Enabled)". The seen Sneak Attack: "damage 9 — 1d10 8 + Strength 1", no 2d6 (KNOWN). In the fight, s on her turn: "hidden — d20 15 + Stealth 8 + Dexterity 4 = 27 beat 6"; three turns passed beside the sentry, and it never swung: Combat log "Round 3 / Sith Sentry holds — none:no-target", the same for rounds 4 and 5 |
| 5 | Save lines | **PASS**. Power One: "Horror at Power One · Power One — d20 18 + will 1 = 19 vs 7 · shaken", then "d20 14 + will 1 − power 2 = 13 vs 7 · shaken", then "Force Slow … d20 4 + will 1 − power 2 = 3 vs 7 · slowed". Each adds up; "power" is the KNOWN name |
| 6 | Force Slow | **PASS**. Fearless One: Force Slow lands twice ("d20 4 + will 1 = 5 vs 7 · slowed", "d20 1 + will 1 = 2 vs 7 · slowed"), then the apprentice's attacks read "needed 9 (-2 Force Slow)", once. Her Defense line "Force Slow -2 = 9". Messages → Effects: one "slowed — 8 round(s) left" |
| 7 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 59 ("reg222"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 120 of 196) |

## Small

1. **The Combat log still says she is hidden after the reveal.** Sneak Strike's bump: the box and Messages show "Stealth Mode Deactivated (Run Enabled)", but the Combat log for the same moment reads "Sneak Strike is hidden. / A fight begins. / Round 1 / Sith Sentry attacks Sneak Strike : *miss*".
2. **A raw key in the hold line.** "Sith Sentry holds — none:no-target" in the Combat log, each round she is hidden.

Seen, not filed:
- The Vibroblade's damage adds Strength 4 against Strength 3 on the attack (Str 16), every swing: probably a one-handed weapon held in both hands.

KNOWN, not filed: the Velocity count at three; the seen Sneak Attack's missing 2d6; "power" on a save.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
