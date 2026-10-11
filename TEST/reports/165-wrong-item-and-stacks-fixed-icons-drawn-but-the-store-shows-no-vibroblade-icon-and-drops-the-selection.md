# TEST 165 — recheck of the TEST 164 fixes and the item icons

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. **No images in HANDOFF** (owner ruling 2026-10-11): every screenshot named below is in `~/kotor-tester/shots/test-165/` on the Tester machine. Read first: commits 708dd17, 4730f98, 39e7648, fd39756 and `docs/ITEM-ICONS-COVERAGE.md`. Fresh tester-buyer / tester-looter / tester-no-purse.

## Build

App `fd397564388675ec1ef43b771e125f39708627e5` (git archive, lock unchanged). Lodestar `361f1774f35ecec38eadfe36bf7b98a800763bde` = lock. Shelf `8028a26ac0683bc7ebc69d569e9cea5982decca2` (my data dir; not in the lock). MAIN_WORK `f0b887a7`, HANDOFF `f8843ad` at start. check_shelf clean.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Wrong-item bug | **PASS**: Medpac picked in NEW stays listed, selected and described; Use Item acts on it (full-health refusal), Adrenal untouched. Picking the Adrenal then removes the Medpac from NEW. Swapped order on a fresh buyer: Adrenal picked, used ("+4 Strength for 20 rounds · none left"), Medpac untouched and still new. Used up: nothing selected, blank description, Use Item dim (`1ab`, `1c-box`, `1de`, `1gh`, `1i-swap-status`) |
| 2 | Selection under a changing list | **FAIL (store)**: after a purchase the store drops the selection ("nothing selected"); no wrong item is acted on (`z2a`, `z2b`, `z2cd`). Equip: picking None and OK empties the slot as chosen (`2hk`); equipping another item could not be tried (both fixtures lack the weapon proficiencies) |
| 3 | Stacks | **PASS**: buying a second Medpac shows one "Medpac ×2" row under NEW; picking it clears the whole stack from NEW (`3abc`) |
| 4 | Dialogue tags | **PASS**: Store Bed reply is "Show me what you have." (no [Opens-store]) (`4a-merchant`); Endar Spire trooper: no ids or underscores. "[Lie]" still shows (from the dialogue's `tag = "lie"`; K2 shows [Lie] too); [Persuade], [Human], [Bribe · 50 credits] come from gates (`4b-c`) |
| 5 | Item icons | **FAIL, one**: the **store's Vibroblade row has an empty icon cell** (Store Bed; catalogue `g_w_vbroshort01`, not in the no-icon list). The same Vibroblade has its icon in the Inventory and Equip. Every other item seen has its icon: Buyer (Adrenal Strength, Medpac), Looter (Vibroblade, looted Blaster Rifle), droid T3-27 (Ion Blaster, Computer Spike, Repair Kit), Quin Tal (Telos Mining Shield, Frag Grenade, Medpac) (`5cd`, `5e-s`, `7cd`) |
| 6 | Regression | **PASS**: medpac refused at full health; Adrenal outside a fight (free) and **in a fight** (Quin Tal vs Guard Droid: Gear spent, action kept, "+4 Strength for 20 rounds") (`7f-c`); Nopurse Credits 0 (`6a-credits`); droid T3-27's portrait in Inventory, Equip and Options footers (`6-footers`) |

## Notes

- **A hazard named by its tag:** Strongroom status line "you notice mine.strongroom.10 — 14 against 5" (`7a-s`). The name-not-tag sweep (PT-2739 item 3) didn't cover hazards.
- **Store "In Inventory 0"** for the Medpac while Buyer carried one: the store counts a different item id (stim-pack vs starting medpac).
- **Looter cannot re-equip its own Vibroblade** after unequipping ("You cannot equip this item. You don't have the prerequisites"), and Buyer can't equip it at all: the fixtures carry weapons without the proficiency feats.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
