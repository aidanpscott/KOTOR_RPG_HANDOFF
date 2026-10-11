# TEST 168 — Light/Dark Force costs on screen and in play (PT-2744)

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only here; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-168/`. Answer key: MAIN_WORK `force/FORCE-COST-TABLE-01.md`.

## Build

App `da1ad41` (git archive, lock unchanged). Lodestar `0200dbde59cbc9ed3c240da9697aacc1a80c7ef8` = lock = pub-cache. Shelf `62a1423` (my data dir). Fixtures from `tool/author_tester_inventory_saves.dart`: Lumen (tester-force-light, 83), Grise (tester-force-grey, 50), Noxa (tester-force-dark, 5), Jedi Consular 20, force 223.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Force Powers screen numbers | **FAIL**: the screen shows the power's name, description and "Each use lowers your Force ceiling by 1" (Force Push, Force Shock, Lumen), but **no BASE COST / ADJUSTMENT / COST PER USE rows are visible**: the Abilities screen runs past the bottom of the frame and the description box is cut off; scrolling doesn't reveal more (`P01`, `Pscr`). Heal's description is so long the ceiling line is below the cut too (`H012`). Known powers draw as blank cells, every other as "?" / "UNKNOWN FORCE POWER", so finding them takes clicking around |
| 2 | Help box | **NOT SEEN**: no box on the Force Powers tab for these authored characters (help boxes are for new games only, by design). Not checked on a new Jedi |
| 3 | In play: Force spent and ceiling | **PASS**, every number matches the expected list and the table (below) |
| 4 | Force Incinerate fixed loss | **PASS**: "11f — 223 → 212 · ceiling −6 to 217" |
| 5 | Cast menu = expected | **PASS** for the in-play menu (below). Can't compare with the Force Powers screen (item 1) |
| 6 | Not enough Force | **PASS**: Noxa at 2 Force: "Heal costs 14 and you have 2"; no id |

## In play (Endar Spire trooper, "Stand aside.")

| Fixture | Cast menu | Cast | Expected |
|---|---|---|---|
| Lumen, step 8 | Heal 6f · Force Shock 9f · Force Push 6f | Shock "9f — 223 → 214 · ceiling −1 to 222"; Heal "6f — 214 → 208 · ceiling −1 to 221" | Heal 6 (−1), Shock 9 (−1), Push 6 ✓ |
| Grise, step 5 | Heal 8f · Force Shock 6f · Force Push 6f | Shock "6f — 223 → 217 · ceiling −1 to 222"; Heal **"10f — 217 → 207"**, ceiling −1 | Heal 8 (−1) — see note |
| Noxa, step 0 | Heal 14f · Force Enflame 8f · Force Combustion 7f · Force Incinerate 11f · Force Push 6f | Incinerate "11f — 223 → 212 · ceiling −6 to 217"; Heal ×15 each "14f … ceiling −2" (212/217 → 2/187) | Heal 14 (−2), Incinerate 11 (fixed −6), Push 6 ✓ |

**Note, Grise:** the cast menu says Heal 8f, but Heal took **10**: 217 → 207. Lumen's Heal took the 6 its menu said, and Noxa's took 14. So at step 5 the cast spends more than the menu and the table say. This needs a second look before calling it: I cast it once.

Heals were cast out of a fight and at full HP (the trooper died before it landed a hit), so "take a hit first" was not done; Force and ceiling are what's being checked.

## Notes

- **Warning signs on a player line:** with too little Force, the cast menu marks each power "⚠ you have 2" (`N5`). TEST 166's guard was meant to refuse warning signs on player lines.
- **"⚠ Force Shock does not say what it may be aimed at"** is printed in the Force Shock cast line (`L4ab`, `G12`): an authoring warning on screen.
- Force Enflame 8f and Force Combustion 7f (Noxa's other two Dark powers) were not checked against the table.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
