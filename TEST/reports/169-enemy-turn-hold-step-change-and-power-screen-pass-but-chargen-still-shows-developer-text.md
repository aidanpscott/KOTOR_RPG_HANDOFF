# TEST 169 — recheck of the TEST 167 and 168 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-169/`. Read first: Coder's PT-2743 entry (fixes 1, 3, 4).

## Build

App `e78cf7d` (git archive, lock unchanged). Lodestar `83454bf297565540239b261ac2e81899ddddb621` = lock = pub-cache. Shelf `784864a` (my data dir). check_shelf clean (31 / 105). Fresh fixtures (Force ones included).

**Note on builds:** checks 1, 2 and 4 were run on app `7bd569c` (Main's first TEST 169 order) before the order moved to `e78cf7d`. The only change between them (`e78cf7d`) moves Verify sentences and the "drawn and not present" status line to the dev log (library_row.dart, 13 lines of play_screen.dart, a test); the fight hold, pricing and Abilities code are untouched, so those results stand. Checks 3, 5 and 6 ran on `e78cf7d`.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Leaving on an enemy's turn | **PASS**: Options held ~10 s during the trooper's turn, then closed: the trooper acts only after it closes. Options held ~11 s, Exit Game, Continue: autosave `round 2, turn sith-trooper…`; screen "the fight resumes — round 2, Sith Trooper's turn"; the trooper fires (crit, 40 → 27) and the turn comes back (`1def`, `1ghi`, `1i-line`) |
| 2 | Grise's Heal | **PASS**: before: Neutral 50, Heal 8 + 0 = 8 (screen and cast menu). Shock "6f — 223 → 217 · ceiling −1". After: Neutral 49; Heal 8 + 2 = 10 on the screen and "Heal 10f" in the menu; cast "10f — 217 → 207". Force Shock drops to 5f at step 4 (`2a-s`, `2bc`, `2de`, `2e-heal-after`, `2fg`) |
| 3 | Text sweep | **FAIL**: list below. Clean: low-Force cast menu ("Heal 14f — you have 13", no warning sign), refusal "Heal costs 14 and you have 13", cast and combat lines, Inventory, Equip, Map, Store, the library (only the "N problems" count) |
| 4 | Force Powers screen | **PASS**: inside the frame; BASE COST / ADJUSTMENT / COST PER USE and the ceiling line all visible; known powers draw icons (Force Push, Force Shock, Heal) (`4b-s`, `4c`) |
| 5 | Help box | **PASS**: new Jedi Consular (Vel Arun): first open of Force Powers shows K2's box ("…The further you stray to the Dark Side, the more expensive Light Side powers become…"); second open, none. Same line on chargen's Powers page (`5ab`, `cg-09-powers-s`) |
| 6 | Regression | **PASS**: store selection through a buy, one Medpac row in the sell list, "Medpac ×2" in Inventory; Escape+F4 ×3 = one quick.mark rewritten each time, no app error; "you notice Mine" line clean (`6abc`, `6d-stack`, `6ef`) |

## Check 3 findings (player-facing text that shouldn't be there)

1. **Chargen Class page:** "not extracted · vitality die, skill points, class skills, priority abilities and the feat schedule are not in **classes.json**. The hub needs them; the pre-hub does not." (file name + developer prose, on every class) (`3h-cg-class-s`, `3j-consular-s`).
2. **Pre-hub page:** "what the strip is shaped by · … the Powers step exists and the strip has nine steps · what the hub carries · The strip comes next… the marker in the area still stands in for one." (developer prose) (`3k-hub-s`). The hub itself says "what is not built · Every step is built… It does not lead anywhere yet".
3. **Portrait page:** "Portraits are not drawn yet, so there is nothing to choose from… Importing artwork from a copy of the games will not fill this either…" (`cgA`).
4. **Backstory page:** "**see §2**" (a citation) (`cgB`).
5. **Powers page:** "withheld — no cost · Precognition have no Force cost written for them yet, so there is nothing to spend to use them." (`cg-09-powers-s`).
6. **Heal's description** (Abilities > Powers): "…The source reads a flat +5… a port that silently changes a number is what **PT-297** exists to forbid, and an owner ruling…" (`4c`).
7. **Status line after combat:** "Vel Arun: 4 of 7 — in your campaign, **a01-room** left you at 4" (area id; same pattern seen with a01-command-deck in TEST 164) (`lv2`).

**Not checked:** level-up feats (Tester XP Bed's single-row room: the companion blocks the way to the dummy, "Mate is with you — there is no way past without walking round"); a message box after a refused action on e78cf7d (the medpac box was K2's text in TEST 167).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
