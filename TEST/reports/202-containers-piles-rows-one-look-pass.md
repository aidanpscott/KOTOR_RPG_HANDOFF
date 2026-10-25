# TEST 202: container_p, corpse piles, in-fight costs, rows, one look

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-202/` (MAIN_WORK `5db2d26a`). The step-by-step log is `TEST/reports/202-running-log.md`.

## Build

App main `d680dc2`, a git worktree beside my own clone. `gate.py --at d680dc2`: "FOR TESTER — CORE at d680dc2, 5165 tests, 0 failed"; ARCHIVE last green at d680dc2. Lodestar `7801a13` = lock = compiled. Lens `5fe60a9`. Shelf `88d0d8f`; check_shelf clean (33 rules files, 125 blueprints). The build (9.9 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Packages: synced to `88d0d8f`; only locked-and-trapped had changed (old copy in `notes/`). Settings: defaults (no settings.json). Brightness: default.

Characters, from `specs202/`:
- Lock Two and Lock Three: Soldier 8, Security 11, Awareness 8, in the strongroom.
- Icon Nine for the Tester Bolt fights. A small helper (`run/fightbolt.py`) walks to the nearest gunman and bumps it each turn, so the fight can be won.

## Summary: all pass; four small items

| # | Check | Result |
|---|---|---|
| 1 | Containers | **PASS**. A plain click on the locked footlocker tries Open Lock first ("d20 5 + Security 11 + Intelligence 2 = 18 vs 18 (hard) · open"). Clicking again opens K2's page titled "Footlocker" with the Medpac and Vibroblade. Down lights the Vibroblade and Enter takes it; Get Items takes the Medpac; Escape and Close shut it. Re-opened, it shows "Container is Empty" under a dim Get Items. Both items show in Inventory as NEW (amber 149,122,71). Saved "38 : taken202", loaded it, and the footlocker is still empty |
| 2 | Corpse piles | **PASS**. After a won fight, three piles. A click opens the page titled "Gunman" with "Blaster Rifle". Stepping onto a pile took nothing (no "took" line). A click on the pile under me opens the same page with the rifle still there; Get Items took it, and it shows in Inventory as NEW |
| 3 | In a fight | **PASS** (Lock Three against the strongroom's Probe Droid). The first opening paid the interaction: Move was already dim from walking (28), while Action (5) and Gear (27) stayed lit. Taking the Medpac with Enter was free. The second opening said "your second interaction this turn, so it cost your Action", and the Action slot went 5 → 1. The third was refused: "opening the Footlocker — you have spent your interaction and your Action" |
| 4 | Right-click Search | **PASS**: "search — d20 16 + Awareness 8 + Intelligence 2 = 26 · 2 to take", with no "walk onto it" |
| 5 | Rows | **PASS at 1920**: from the row line's last lit pixel to the list line's last, 8 px on Inventory (925 → 933), Equip (925 → 933), Skills (925 → 933) and the party list (926 → 934). K2's 05b and 05c measure 925 → 933, also 8 px. At 1280×720: Inventory, Equip and Skills 617 → 622 (5 px; 8 × 2/3 = 5.3); **the party list 617 → 624, 7 px** (its line is 2 px wider) |
| 6 | One look | **PASS**: in rx-two-triggers, Kael (placed as a henchman) is a "K" token at load and the Backer stays red. In Tester Bolt, the area's own Vela is a "V" token |
| 7 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185 line for line. Regression: Save (slot 39, "reg202"), Escape then F4 (one quick save), Load, and a fight to its end (won, three piles) |

## Small

1. **The party list at 1280×720**: the row line ends at 617 and the list line at 624, so 7 px, where Inventory, Equip and Skills measure 5. At 1920 all four are 8.
2. **The right-click menu ignores Escape.** With it open, Escape opened Options and left the menu open.
3. **The right-click menu stays open while the player walks, and keeps its old distances.** Picking Search after walking up beside the footlocker refused with "Search (Awareness) — 3 squares away". A fresh right-click shows the entries live.
4. **The message box cuts off its third line** ("…so it cost your Action" is half shown, both times).

Noted, not a finding: in a fight, a struck-down enemy leaves no pile on the board until the fight ends. Clicking its square mid-fight just walks there.

Known and not filed: the container page's title, row click and 36 px rows are reasoned; no capture of the combat bar.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
