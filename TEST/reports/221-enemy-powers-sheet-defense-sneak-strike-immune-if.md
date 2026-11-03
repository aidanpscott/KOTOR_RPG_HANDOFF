# TEST 221: enemy powers, the sheet's Defense, Sneak Attack from hiding, Immune One, "if_"

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my bed are in `KOTOR_RPG_MAIN_WORK/media/screens/test-221/` (MAIN_WORK `eb5543c1`).

## Build

- **App**: main `aa3abbd`, a worktree beside my clone. `gate.py --at aa3abbd`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at aa3abbd, 5458 tests, 0 failed"; ARCHIVE last green at aa3abbd. Lodestar `b3f2b30` = lock = compiled; built through the lock in 10.2 s; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `61163db`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test221_saves.dart` (Power One, Fearless One, Sneak Strike) and `author_tester_test217_saves.dart` rerun for Immune One, with pristine copies kept so each replay starts clean. Reused Armor Jedi (armor-219; her mid-fight autosave set aside so she loads outside a fight). My own **aura-221** in tester-align: Aura Jedi, with Plain Mate knowing Force Aura and Heal (subject-tagged power-taken).

## Summary: all pass; one small item

| # | Check | Result |
|---|---|---|
| 1 | Enemy powers | **PASS**. Power One: on arrival "initiative — Power One 10 · Sith Apprentice 2", the apprentice 4 squares off. Its turns: "Horror at Power One · … d20 18 = 19 vs 7 · shaken", "Horror … d20 14 = 13 vs 7 · shaken", "Force Slow … d20 4 = 3 vs 7 · slowed", then "Sith Apprentice closes 3 squares — 4 to 1 · … unarmed … hit". Its pool on hover after each cast: "Force 15 of 23", "Force 5 of 21", "Force 0 of 20 · exhausted from 25". No Dark Fury, no Stun Droid. The DC is its own: 7 = 5 + Force levels 2 + Wisdom 0 + Charisma 0 (Power One's own would be 5). Horror shaking her on a made save is Horror's rule ("a target that saves is shaken anyway"). Fearless One: Force Slow five times (resists, resists, slowed, resists, slowed), pool 20, 15, 10, 5, 0, then it closes and attacks; never Horror |
| 2 | Sheet's Defense | **PASS**. Armor Jedi, outside a fight, Force Aura ("+2 defense · +2 saves"): Stats Defense 19; Character Info "Defense: +2 Force Aura"; bumping into a fight, her line "Defense base 10 + Dexterity 1 + class 6 + Force Aura 2 = 19" and the Ironhide's "needed 19 (+2 Force Aura)". Plain Mate (controlled, f → "1 Force Aura 6f · 2 Heal 8f"): "Plain Mate: Force Aura · 6f — 105 → 99"; her Stats Defense 17 (15 before); her Character Info "Defense: +2 Force Aura"; on her turn in the fight "Defense base 10 + Dexterity 1 + class 4 + Force Aura 2 = 17" |
| 3 | Sneak Attack from hiding | **PASS, small item 1**. s → "hidden"; one step right → "hidden — d20 19 + Stealth 8 + Dexterity 4 = 31 beat 1"; nine more steps, no second roll; walking into the sentry starts the fight (log "Sneak Strike is hidden. / A fight begins."). x, walk in: "Sneak Attack · Vibroblade · … — hit · … damage 17 — 1d10 8 + Strength 1 +2d6 Sneak Attack 5+3". Next round, x, walk in: "Sneak Attack · … — hit · damage 6 — 1d10 5 + Strength 1", no 2d6 |
| 4 | Immune One | **PASS**. Every Precise Shot hit on the brute ends "· resists", including failed saves: "d20 1 + fortitude 2 = 3 vs 20 · resists", "4 vs 20", "8 vs 20", "10 vs 20". The ironhide control: "d20 12 + fortitude 12 + Constitution 10 = 34 vs 20 · slowed" |
| 5 | "if_" | **PASS**. TEST 220's exact steps. Open Soldier 218: "… The Noble part comes last, if at all. Soldier: The professional._". Frail Sage 218: "… The Noble part comes last, if at all. Jedi Consular: The Force is the weapon._". No "_" mid-text. A click in the text puts the caret under the pointer every time: on line 1 → "eve_ntually", on the line 1/2 border → "_part", on Frail Sage's line 1 → "T_aris" (marked against the click point) |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 58 ("reg221"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 114 of 196) |

## Small

1. **The sentry swings at a hidden Sneak Strike.** In round 1, after the bump started the fight and before her strike, the sentry attacked her: "Sith Sentry: unarmed · rolled 5 … needed 16 — miss". She was still hidden then, since her next swing carried the 2d6. Nothing on the screen or in the Combat log says she is revealed either, before or after the strike. The only sign is that the second hit carries no 2d6.

Seen, not filed:
- A save line hides its modifier: "d20 18 = 19 vs 7" (Power One's Will +1).
- KNOWN: Force Slow's double terms. After two Force Slows on Fearless One, the apprentice's line lists "−1 slowed — Force Slow, −1 slowed — Force Slow, −2 Force Slow, −2 Force Slow" against "needed 9", while her own line reads "Force Slow −2 = 9". The number doesn't stack; only the list does.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
