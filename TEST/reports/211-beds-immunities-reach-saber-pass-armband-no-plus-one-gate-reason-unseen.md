# TEST 211: the 208 beds, immunities, a controlled member's reach, alignment items

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-211/` (MAIN_WORK `9a9e5722`). The step-by-step log is `TEST/reports/211-running-log.md`.

## Build

- **App**: main `029d802`, a git worktree beside my own clone. `gate.py --at 029d802`: "FOR TESTER — CORE at 029d802, 5265 tests, 0 failed"; ARCHIVE last green at 029d802. Lodestar `aa93c7a` = lock = compiled. The build (10.0 s) went through the lock, and git status was clean.
- **Settings**: defaults. Brightness: default.
- **Shelf** `270095f`: base-rules synced.
- **Beds**: `author_tester_test208_saves.dart` rerun.

The gear bed is a local package, `tester-gear`, with:

- Light Foe (alignment 90) and Dark Foe (10);
- Bastila's Lightsaber, Nomi's Armband, Arca Jeth's Robe (Light Side), Natth Cowling (Dark Side) and Jolee's Robe (Neutral);
- three Jedi Consular 10s: Gear Neutral (50), Gear Light (95) and Gear Dark.

## Summary: most pass; two findings

| # | Check | Result |
|---|---|---|
| 1 | 208 beds | **PASS**: Proof Immune reads "Jedi Consular 16", Vitality 98/98, Force 239, Experience 120000 / Needed 16000, Neutral (50), with no "[Modded]" |
| 2 | Immunities | **PASS**. Under Push and under Wave, Steady is "not Force Pushed" with no stun line and attacks every round. Rock is "not Force Pushed" and "stunned". The Thug is "Force Pushed" and "stunned" |
| 3 | Reach | **PASS**. With Mate controlled beside the console and the leader 3 squares away, the console opens as Mate. The menus read "Slice (Slicing)" and "Open Lock (moderate)" with no distance. As the leader: "Slice (Slicing) — 3 squares away" |
| 4a | Bastila's saber | **PASS**. On the Dark Foe: "damage 36 — 2d10 … + 4 universal + **1d6 vs dark side** 5 + …". On the Light Foe the same line has no "vs dark side" term |
| 4b | Nomi's Armband | **PASS** on the sheet: Defense is unchanged. **FINDING** in a fight (below) |
| 4c | Equip gates | **PASS** for who's refused, each by their own score. Neutral may wear only Jolee's; Light (95) only Arca's; Dark only Natth. **FINDING**: the reason never shows (below) |
| 5 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save (slot 48, "reg211"), Escape then F4 (one quick save), Load, and a fight won |

## Finding 1: Nomi's Armband adds nothing against a dark attacker

Gear Neutral wore the armband and no robe, DEF 15. The Dark Foe (alignment 10) shot three times, and each line read "Dark Foe: Blaster Rifle · rolled 22 — d20 19 + attack 3 + Dexterity 0 · needed 15". That's the sheet's 15 with no +1.

`fight.dart:1370` adds the defence-versus term, but the line doesn't show it. I couldn't read the Light Foe's lines (the Dark Foe acts last and overwrites the box). Frame: `g-darkshot.png`.

## Finding 2: an alignment refusal never says which side

A refused robe is outlined red. Selecting it shows only K2's generic popup: "You cannot equip this item. You don't have the prerequisites. Please see the item description." The description names no side; it lists "Feats Required: Jedi Defense", which Jolee's Robe also lists while being allowed.

The words exist in the code: `_gateWhy` puts them in `blockedWhy`. But the popup draws `blockedMessage ?? <the generic text>` (`equip_screen.dart:809`), so "needs to be Light Side" never reaches the screen. Frame: `e-arca2.png`.

## Small

- Equip accepts the double-bladed saber in WEAPON L with the right hand empty, and the swing is then "unarmed". K2 puts a double-bladed weapon in the right hand only.

Watch item: no bed here had a companion with powers, so the companion cast menu wasn't exercised. KNOWN, not filed: Equip gates on a companion, Stasis.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
