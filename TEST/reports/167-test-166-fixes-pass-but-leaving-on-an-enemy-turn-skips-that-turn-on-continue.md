# TEST 167 — recheck of the TEST 166 fixes, the area label, the slower-enemy pause and the F4 fix

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only here; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-167/`. Read first: commits a515b4a, 4d86492, 9dbb6e1, 00417e3.

## Build

App `0f61ae7` (git archive, lock unchanged). Lodestar `7624fbdb06b56a594c2a3d5bb821f0d2554064dc` = lock = pub-cache (origin is at 0200dbd; not built). Shelf `62a1423` (my data dir). MAIN_WORK `7f42b27a`, HANDOFF `6d0cb39` at start. check_shelf clean (31 rules files, 105 blueprints). Fresh fixtures; Quin Tal re-authored.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Medpac | **PASS** (partly shown): Buyer buys the store's Medpac: one "Medpac ×2" row in Inventory, one Medpac row in the sell list; Use Item on it reaches the medpac (K2's full-health refusal, not dim) (`1abc`, `1d-useable`, `1e-s`). Buyer can't be wounded in Store Bed, so heal-and-spend was shown on Quin Tal instead: "Medpac — 33 of 33 (was 27) · 2 left", row ×3 → ×2 (`1fg`, `1h-quin-heal-line`). The second heal on the bought stack was not shown |
| 2 | Mine | **PASS**: poison mine "goes off — d20 13 = 13 vs 15 · 6 damage · 27 of 33 · 2 more rounds" (vitality bar turns yellow-green); condition mine "goes off — d20 17 = 17 vs 15 · you shake it off". No backticks, warning sign or "states no" (`2ab`, `2cd`). Minor: the line has no subject ("goes off", not "Mine goes off") |
| 3 | Take off / put back | **PASS**: Quin Tal's Neural Band and the Looter's Vibroblade come off normal (not red) and go straight back on; the Stabilizer Mask stays red (`3abc`, `3de`) |
| 4 | Area label | **PASS**: bottom-left shows "Market" (Store Bed), "Command Deck" (Endar Spire), and nothing / status lines only in Strongroom; never an id or square. The Map caption reads "map — ⟨Strongroom⟩" (`4a-s`, `4d-bl`, `4b-strong-bottomleft`, `4c-s`) |
| 5 | Leaving on an enemy's turn | **FAIL** (below) |
| 6 | Keys after closing | **PASS**: Escape+F4 ×10: `quick.mark` rewritten once each time, one file, no error in the app log; a 60 fps capture of one round shows one Saving picture (91 frames, 1.5 s). Escape+I: Inventory opens and stays. Escape+Right: one square (`6a-s`, `6be`) |
| 7 | Regression | **PASS**: store selection stays through a buy, icons in the border, In Inventory 1 → 2 (`1abc`, `1ab-n`); [Lie] shows, [Opens-store] doesn't (`7b-lie`, `7a-c`). NEW-tab Use Item not re-run |

## FAIL: leaving during the enemy's turn skips that turn

Launched with `KOTOR_ENEMY_TURN_PAUSE_MS=4000` (confirmed in the process environment). Looter vs the Endar Spire trooper, "Stand aside.": initiative Looter 20, trooper 7. Space ends my turn; while waiting, the turn-order arrow moves to the Sith Trooper, my action shows spent, and nothing else changes on screen (no "waiting" text) (`5b-waiting-s`). Within 1.5 s: Escape → Exit Game → OK (`5c-esc-s`). The autosave holds `fight: round 2, turn Looter`, both at full vitality (40/40, 18/18). Continue: **"the fight resumes — round 2, Looter's turn"**, 40 of 40, trooper 18 of 18, still Looter's turn after 7 s (`5def`). The trooper's round-1 turn never happened. Expected: the trooper's turn, it acts, then back to me.

## Notes

- A named-save Saving picture was 17 frames in TEST 158; the quick-save one here is 91 frames (1.5 s).
- Owner, during this run: the Map should show the whole area as in K2 (not a small grid), with fog of war, so unexplored parts stay black until visited. Passed on to Main.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
