# TEST 166 — recheck of the TEST 165 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only here; screenshots are in the private repo at `KOTOR_RPG_MAIN_WORK/media/screens/test-166/` (MAIN_WORK b0b9ba55). Read first: commit f15f07e (store selection, icons, stack count, names, fixture feats), 4e45cd7, Shelf af1e4b3.

## Build

App `f15f07e` (git archive, includes 4e45cd7; lock unchanged). Lodestar `361f1774f35ecec38eadfe36bf7b98a800763bde` = lock. Shelf `af1e4b3` (my data dir). MAIN_WORK `31efba4b`, HANDOFF `c0462eb` at start. check_shelf clean. Fresh fixtures from `tool/author_tester_inventory_saves.dart`; Quin Tal re-authored.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Store selection | **PASS**: Medpac picked, bought twice (credits 500 → 460 → 420; In Inventory 1 → 3), still selected; in the sell list, sold from a row of two: still selected (In Inventory 2 → 1), sold the last: the row leaves and the pane says "nothing selected" (`1bcd`, `1d-stats`, `1lmn`, `1lmn-n`) |
| 2 | Store icons | **PASS**: Vibroblade and Medpac rows draw their icons inside the row border, Inventory size (`1a-z`) |
| 3 | Names | **PASS**: "you notice Mine", "goes off — … Mine …", "Door is locked — heroic security", keyed door into the Vault, "you take off Neural Band" (`3fh`, `3be`, `3k-unequip-line`). Bumping the crate prints nothing. Bottom-left corner shows the area id and square: "a01-strongroom · 2, 1" (the known item) |
| 4 | In Inventory count | **PASS**: 1 before buying, 3 after two buys, down to 0 after selling |
| 5 | Equipping | **PASS**: Buyer equips the Vibroblade; Looter equips the looted Blaster Rifle, then the Vibroblade again; the list reorders after each and the pick and description stay on the chosen item (`5bc`, `5eh`). Lightsaber refusal: **not tested** (none of these characters carries one) |
| 6 | Library cards | **PASS**: Strongroom "…a crate and four mines…"; Tester Probe "Eleven small rooms joined by 18 doors…" (`6ab`) |
| 7 | Regression | **PASS** for NEW: picking the Vibroblade keeps it listed and selected, picking the Medpac then drops the Vibroblade from NEW (`7a-new`, `7b-vibro-picked`). [Lie] / [Opens-store]: not re-captured this build. Stacks: see FAIL |

## FAIL: a store-bought Medpac can't be used, and doesn't stack with a carried one

Store Bed sells `items/misc/stim-pack.item` (named "Medpac", catalogue `g_i_medeqpmnt01`, **`base = "stimulant"`**). Bought, it shows the medpac's description but **Use Item stays dim** (`7c-s`, `7de`). In the sell list it is a separate "Medpac" row from Buyer's own `items/consumables/medpac` (`1e-z`), while the store's "In Inventory" counts both together (3). Likely cause, not shown: two blueprints for one item; Use Item and stacking key on the blueprint/base, the count on the catalogue row.

## Notes

- **Mine trigger line shows an authoring warning:** "goes off — ⚠ \`Mine\` states no kinds" (backticks and all) (`3fh`).
- **An item goes red right after taking it off:** Quin Tal's Neural Band is "(Equipped)" and normal, then red (unequippable) once removed (`3ij`). Same pattern as Looter's Vibroblade in TEST 165.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
