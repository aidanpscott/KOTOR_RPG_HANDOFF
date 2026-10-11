# TEST 163 — the Inventory screen and the Options highlight (PT-2742, PT-2743, PT-2739 item 6)

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Screens: `BUILD/screens/test-163/`. Read first: PT-2742, PT-2743, Coder's results, `K2-PARITY-INVENTORY-PT2741.md`, the K2 captures.

## Build

App `d41d9df4df0b3935902b89e804a53a4a22db8f8a` (git archive, lock unchanged). Lodestar `361f1774f35ecec38eadfe36bf7b98a800763bde` = the app's lock = pub-cache. Shelf `b85d1b99fbf6f7354800475ff8052554521a296a` (my data dir checked out at it; the lock does not pin Shelf). MAIN_WORK `909f30e1`, HANDOFF `8f24291` at start. check_shelf clean.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Layout vs K2 | **PASS** with one FAIL below: title, Filter block, 8 tabs, icon cells, rows, scroll bar, description, Credits, Use Item, Close, footer, first row chosen on open. Empty icon cells noted (adrenal, grenade, medpac, keycard) |
| 2 | NEW tab | **PASS** (picked-up items): selecting clears it at once; reopen and F4/F5 keep it cleared; a new character's NEW is blank. Not checked: a bought/looted item (Dressa dropped nothing) |
| 3 | Quests | **PASS**: Sith Keycard under Misc and Quests, once in All; same after F4/F5. It also opens the vault door |
| 4 | Equipped items | **PASS**: All has every equipped item first; Weapons has both lightsabers (equipped) first; the equipped Light Combat Suit is in Armor, not Weapons |
| 5 | Empty tabs | **PASS**: Datapads blank both panes, no sentence |
| 6 | Use Item | **FAIL**: a medpac at full health is spent (×3 → ×2, nothing healed); K2 refuses it ("This character does not need to use a medical pack since they are already at full health."). In a fight: PASS (1 → 11 of 12, ×3 → ×2; a second use refused: "Medpac cannot be used — gear has already been used this turn"). Adrenal and grenade/mine dimming **not verified** (see notes) |
| 7 | Help boxes | **PASS**: new droid T3-63 got a box once on Attributes, Skills, Feats (chargen), Inventory, Equip, Abilities/Skills, Feats, Force Powers, Journal, Party, Map, Messages; second opens none; the authored older character (Quin Tal) none; Tutorial Popups off → none, on → shows. Inventory text exactly the owner's wording |
| 8 | Credits | Not checked with a purse-less character (every fixture has 100) |
| 9 | Options highlight | **PASS**: in-game menu, main-menu Options and Feedback: row 1 lit on open, only the hovered row lit; never two |
| 10 | Keys and text | **PASS** keys: arrows, WASD, space with the Inventory open moved nothing; I and Escape close. Text: no tags; but "No Description Set" shows in the Ion Blaster's description (see notes) |

## FAILs

1. **A medpac is spent at full health.** Repro: Quin Tal (33/33), Inventory → Useable → Medpac ×3 → Use Item: count becomes ×2, HP unchanged, no message. K2's capture (`06-K2-medpac-full-health-refusal`) refuses with a box. Unlisted difference from K2.
2. **A droid's portrait is missing in the Equip and Inventory footers.** Chargen droid T3-63: Options footer shows the astromech portrait; Equip and Inventory footers show an empty teal box (`FAIL-droid-portrait-...`). An organic's portrait shows in all three. Likely cause, not shown: the droid fallback added for PT-2736 is only in the Options footer. (Asked by the owner during the run.)

## Notes

- **Adrenal:** the one I gave Quin Tal is Shelf `consumables/adrenal.item`, which has no catalogue row, so it has no description and Use Item is dim. That's likely right for that blueprint; a real adrenal (e.g. the Soldier kit's Adrenal Strength) was not tested.
- **Grenades/mines dim:** not checked (I didn't select the Frag Grenade).
- **"No Description Set"** in the Ion Blaster's description (droid start kit), and "this item carries no description" for items without text. The first looks like a raw placeholder string; worth a look.
- **The K2 medpac capture's row says "Adrenaline Amplifier" but its description is a medpac's** (owner noticed). Same in both captures in `signoff-saveload-options/k2-medpac/`: the selected row is the amplifier, the pane shows "Single Use … A medpac contains…". Most likely the pane is showing the medpac that was just used up (the list no longer has it). It is a K2 capture, not our app.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
