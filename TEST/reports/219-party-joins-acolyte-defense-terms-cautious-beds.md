# TEST 219: the whole party joins, the Jedi Acolyte's robe, named Defense terms, Cautious's terms, the Twin and Charged beds

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-219/` (MAIN_WORK `627af16e`).

## Build

- **App**: main `934c76c`, a worktree beside my clone. `gate.py --at 934c76c`: "FOR TESTER — CORE at 934c76c, 5423 tests, 0 failed"; ARCHIVE last green. The verdict line read "DO NOT SEND — 2 blocking failure(s)": `check_shelf.py` and `check_shelf_repo.py`, "items.toml — 185 line(s) differ" in the shared tree, not the build. My data dir's shelf checks clean (33 rules files, 126 blueprints). Lodestar `2d438df` = lock = compiled; built through the lock in 9.9 s; git status clean.
- **Settings**: defaults. **Shelf** `de0eeee`, synced.
- **Beds**: `author_tester_test217_saves.dart` rerun (adds Twin One, Charged One), pristine copies kept. My own:
  - **tester-219** "Far Hall": 24×5, a wall at column 19 from top to bottom; Far One (Jedi Consular 1, 5 vitality) at the arrival, a Sith Trooper (blaster rifle, its talk removed) 3 squares east, and the companion Far Mate (Soldier 4) at column 22 behind the wall.
  - **armor-219** (Armor Jedi, Jedi Consular 16 holding Force Aura, Force Shield and Force Armor) in tester-attacks.
  - Four chargen Humans in the opening, all Acolyte: Guardian, Sentinel and Consular taking the profession item, and a Consular taking the aptitude.

## Summary: all pass; no findings, no small items

| # | Check | Result |
|---|---|---|
| 1 | Whole party joins | **PASS**. Bumping the trooper with Far Mate behind the wall: "initiative — Far One 15 · Far Mate 3 · Sith Trooper 1". I passed turns until Far One fell to "−8 of 5"; play went on to "Far Mate is waiting on you", no defeat box |
| 2 | Jedi Acolyte | **PASS**. Taking "Padawan Robe → Jedi Robe — Regeneration Force Points 1", the Guardian, the Sentinel and the Consular each start in "Jedi Robe (Equipped)" (pane: "Defense Bonus: 1 · Regenerate Force Points: 1"). The Consular taking "Aptitude: Mysticism" starts in "Padawan Robe (Equipped)" |
| 3 | Defense terms | **PASS**. Against Flurry One after a Flurry: "Brute: unarmed … needed 12 (-2 Flurry) — miss". Against Twin One after Critical Strike: "Gunman: Blaster Pistol … needed 13 (-1 Critical Strike) …". Against Armor Jedi after Force Armor: "Ironhide: unarmed … needed 23 (+6 Force Armor) — hit". No "force_armor" anywhere |
| 4 | Cautious | **PASS**. "hidden — d20 15 + Stealth 4 + Dexterity 4 + Master Cautious 3 = 26 beat 4" |
| 5 | Beds | **PASS**. Twin One: "Critical Strike · Vibroblade · rolled 12 … dual-wield 4 · needed 16 — miss", then "off-hand: Vibroblade · rolled 25 … — hit · threat not confirmed … damage 2"; no stun line. Charged One: "threat confirmed: rolled 22 … damage 41 — 3d8 7+5+7 + 3d6 6+3+4 + Dexterity 3×3 × 3 critical · 359 left · prone — d20 18 = 18 vs 21 · takes hold" |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 56 ("reg219"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 109 of 196) |

Seen, not filed:
- Armor Jedi's own Defense line under the reactions reads "Defense base 10 + Dexterity 1 + class 6 + power 6 = 23": the generic "power", not "Force Armor" (and not "force_armor"). The enemy's line names it.
- Twin One's critical-strike damage on the off hand reads "Strength 1" against "Strength 3" on the attack: the off hand's half Strength (ruled earlier).

KNOWN, not filed: enemies don't start fights on sight; Hide outside a fight; talking hostiles at range; the non-Jedi and Sith Acolyte robes; "if_ at all.".

Skills: `verification-before-completion`. Kept small per the simplicity rule.
