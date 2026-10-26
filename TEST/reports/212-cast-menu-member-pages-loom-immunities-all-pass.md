# TEST 212: the companion's cast menu, the selected member's pages, Loom's reasons, immunities by text

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-212/` (MAIN_WORK `5b5528c9`). The step-by-step log is `TEST/reports/212-running-log.md`.

## Build

- **App**: main `33661f8`, a git worktree beside my own clone. `gate.py --at 33661f8`: "FOR TESTER — CORE at 33661f8, 5275 tests, 0 failed"; ARCHIVE last green at 33661f8. Lodestar `0fe5bff` = lock = compiled. The build (10.1 s) went through the lock, and git status was clean.
- **Loom** `e9528e2`, built through the lock; `pubspec.lock` unchanged, git status clean.
- **Settings**: defaults. Brightness: default.
- **Shelf** `b71849e`: base-rules synced.

Beds:

- **tester-align**, reused. The player knows Heal, Force Affliction and Force Push (3 powers). Both mates get theirs from subject-tagged power-taken events: 2 powers (fewer-212), 3 (equal-212) or 4 (more-212, adding Force Stun).
- **tester-immune**, a new local package with two guards, each given an immunity feat by a subject event in the save: Para Guard (Force Immunity: Paralysis) and Stun Guard (Force Immunity: Stun). It also holds a flash mine and then a frag mine, both "stunned 2 rounds". The player, Stasis Jedi, holds Force Immunity: Stun.

## Summary: all pass

| # | Check | Result |
|---|---|---|
| 1 | Companion's cast menu | **PASS** for fewer, equal and more, with no crash. The menu is on its own top row with the vitality row beneath, and shows her pool ("force 105 of 105"). It lists her own powers at her prices: Dark Mate "Heal 12f · Force Affliction 10f"; Plain Mate's four (with Force Stun) wrap to two lines, nothing cut. Each cast spends her pool (105 → 95, 97, 99). The player's own menu is "1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f", 155 |
| 2 | Selected member's pages | **PASS**. In a fight, pressing Plain Mate's HUD portrait on my turn opens her Equip (the PT-2524 line), then her Character page: her stats, Force 97/105, marker mid-bar, Info "Neutral (50)", and her Abilities. Dark Mate's Character shows Force 95/105, the marker toward Dark, and Info "Committed Dark (18)", her 20 less her own cast. Outside a fight her Info and Powers are hers. q opens my own Equip |
| 3 | Loom | **PASS**. 101, −1, 20.5, abc and 150 each show "alignment must be a whole number from 0 to 100"; 20 clears it. "needs a species" shows with Create dim until Human is picked |
| 4 | Immunities by text | **PASS**. Flash mine: "you shake it off". Frag mine: "stunned for 2 rounds". Stasis on Para Guard: "resists" with no effect, and he attacks the next round. Stasis on Stun Guard: "Stun Guard has been affected by Force Stasis", and it loses its turn |
| 5 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save (slot 49, "reg212"), Escape then F4 (one quick save), Load, and a fight won |

## Small and notes

- Plain Mate's Equip shows DEF 11 while her Character page shows Defense 15 (base 10 + Dex 1 + class 4).
- Outside a fight, f while controlling a mate lists the player's powers and "force 155 of 155". The order covered only her turn in a fight.
- In a fight, the small portraits inside the menus don't switch member; the HUD portraits do.
- Stasis's hold is named "stunned" in the lines ("Stun Guard is stunned.").
- The GTK open dialog in Loom keeps mangling typed `/tmp` paths. I opened a scratch copy from my own packages folder and removed it afterwards (nothing written).

KNOWN, not filed: Nomi's Armband's missing +1, the Equip gate's unseen reason, the double-bladed saber in the left hand, a companion's equipment from the bag (PT-2524), and enemies listing powers. A MAIN → CODER message (the TEST 212 hash acceptance and ruling 3a) landed here mid-test; I didn't act on it.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
