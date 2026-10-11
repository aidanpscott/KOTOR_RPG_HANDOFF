# TEST 164 — recheck of the TEST 163 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Our-app screens only: `BUILD/screens/test-164/`. Coder's answer read first (PT-2743 "TEST 163 fixes DONE", app 50cd20f).

## Build

App `50cd20f52371fdc8af19038cf5a7f7f3d04a8302` (git archive, lock unchanged). Lodestar `361f1774f35ecec38eadfe36bf7b98a800763bde` = lock. Shelf `8028a26ac0683bc7ebc69d569e9cea5982decca2` (my data dir). MAIN_WORK `66ca7e2b`, HANDOFF `46e0ba2` at start. check_shelf clean. Fixtures from `tool/author_tester_inventory_saves.dart`.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Medpac at full health | **PASS** at full: Buyer 13/13, K2's line in a box, Medpac still listed. One below full: not re-run on this build (the in-fight heal passed in TEST 163) |
| 2 | Portraits | **PASS**: droid T3-27's portrait in Options, Equip and Inventory footers; organic (Onjo Proof, Nopurse, Buyer) too; companion tiles show the generic face, not the player's |
| 3 | No placeholder text | **PASS**: Ion Blaster, Computer Spike, Repair Kit, Medpac, Adrenal Strength, Blaster Rifle all have real text; no "No Description Set" seen |
| 4 | Fixtures | **PASS**: Nopurse Credits 0; Looter beats the trooper, its Blaster Rifle shows under NEW; Buyer buys a Medpac (500 → 460), it shows under NEW; Adrenal used outside a fight: "+4 Strength for 20 rounds", free. Adrenal in a fight not checked |
| 5 | Regression | **PASS** for empty tabs, NEW, Options highlight (row 1 lit). Quests, help boxes not re-run (same code as TEST 163) |

New, **FAIL**: selecting an item in the NEW tab moves Use Item onto another item (below).

## FAIL: selecting in NEW, then Use Item, spends a different item

Repro: tester-buyer (fresh), Inventory → NEW shows "Adrenal Strength" and "Medpac". Click Medpac: it leaves the NEW list at once (correct: selected = no longer new), and the selection and description jump to Adrenal Strength (`FAIL-select-in-new-...`). Press Use Item: the **Adrenal** is used ("Adrenal — +4 Strength for 20 rounds · none left"). Seen once by accident, then reproduced up to the jump (I did not press Use the second time). The player picked the Medpac and lost the Adrenal.

## Notes (not failures)

- **"[Opens-store]" in a reply** at Store Bed: the dialogue's `tag = "opens-store"` is shown like [Lie] or [Persuade] (`note-opens-store-tag-in-reply`). Looks like an authoring tag on screen.
- **Two "Medpac" rows** after buying a second one (one new, one seen), where three seen ones stack as "Medpac ×3" (`4-two-medpac-rows`).
- **Store description pane** shows only "Single Use" for the Medpac; a black inner box covers the pane (store screen is not yet K2-styled).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
