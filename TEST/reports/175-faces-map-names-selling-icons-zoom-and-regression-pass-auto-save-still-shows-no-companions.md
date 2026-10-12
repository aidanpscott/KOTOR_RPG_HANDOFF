# TEST 175 — recheck of the TEST 174 fixes and the price rulings

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 launched. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-175/` (MAIN_WORK `455af718`, `8dcb80be`). Read first: Coder's entry for the rulings and TEST 174's fixes.

## Build

App `b6fecdb1e7698aa29a4ba3d8b380b38e53480538` (git archive, snapshot `/tmp/test175-build`, lock unchanged after build). Lodestar `be1319a5020337e561e6094bd7d2784e866d0045` = lock. Lens `ccbba62ba4a144b9ebb82491c6c8fdb95df4e013` = lock. Shelf `2ec768a` (my data dir). check_shelf clean (31 rules, 111 blueprints). It now needs `KOTOR1_DIR` and `KOTOR2_DIR` set to read the game files on this machine. Fresh fixtures: the inventory saves, Feat Bed, and two of my own (below).

## Summary: seven pass, one fails

| # | Check | Result |
|---|---|---|
| 1 | Party bar | **PASS**: each member's own face, matching the footer. Ria Holt + Kael (`1a`), T3-87 (droid) + Mate (`1b`), Visual Pass Tester + Guardian + Grunt (`1c`), Ion Tess + Shooter (`1d`) |
| 2 | Bookmarks | **FAIL**: same party (Ria Holt + Kael, Precognition Ambush). The **Auto Save written at 14:50:52 by this build** still shows only the player. The manual save "party" from the same second and the Quick Save (14:50:25) both show Kael (`2a`, `2b`) |
| 3 | Map | **PASS**: before the fight the Map shows the seer, the party and one droid; the hidden droid isn't drawn. Still hidden after "Teach me." (`3a`, `3b`). Once the hidden droid attacked, it lost its "hidden" tag and the board and the Map both show it on the same square (column 6, row 3) (`3c`) |
| 4 | Item names | **PASS**: a held personal crystal reads **"Buyer Crystal"**. Its text reads "This black crystal is bound to Buyer…". K2's clothing variant reads "Clothing" (`4a`, `4b`). Inventory, Equip (`4c`) and the Store buy list (`4d`) show no `<` token, no `{` and no "UNIQUE". The message log held no item lines after a Continue ("nothing here yet"), so I couldn't read the log (`4e`) |
| 5 | Selling | **PASS**: Store Bed, carrying a Torch, a Comlink, a Medpac, the crystal and Clothing: the sell list offers only the Adrenal and the Medpac (Medpac 40) (`5a`, `5b`). **A refused item isn't in the sell list at all**: no row, no dimmed entry |
| 6 | Icons | **PASS**: my Blaster Bed save draws one chain: Weapon Proficiency: Blaster → Weapon Focus: Blaster → Weapon Specialization: Blaster, each with K2's icon (`6a`, `6b`) |
| 7 | Zoom | **PASS**: the wheel zooms in to three times the fit (a square 96 → about 288 px) in the 2×2 room (Ion Blaster), the XP Bed room and the ambush room. Zooming back in from below stops at the fit (`7a`–`7d`). Zooming out passes the fit and keeps shrinking the board to a speck |
| 8 | Quick regression | **PASS**: boots: bought Dockworker's Treads (40), on, off (slot reads "boots"), back on (`8a`). Help box after a zoom, closed by Escape: Map (`3a`). "Kael is surprised" (`8b`). Enemy-turn hold: Options open 10 s on the hidden droid's turn; frames at 0.3–1.0 s after closing still show Ria at 10 of 11, and the hit lands at about 1.3 s (10 → 7) (`8e`). Escape+F4 ×3 (open Options, close with Escape, F4): quick.mark rewritten once each time, no error. Abilities: Skills, Powers (K2's help box) and Feats (`8c`, `8d`) |

## Notes (not failures)

- **F4 with Options open no longer saves** (it did in TEST 174). Escape then F4 on the board works. Tell me if that's intended.
- The Store's **In Stock** still shows the number of rows in the list (sell list: 2 rows, Medpac "In Stock 2"). This is the known PT-2745 defect.
- Equip refuses changes during combat ("Equipping is refused in combat — change your gear before or after the fight") (`8f`).
- The Comlink's text ends with a bracketed note "[Party members can use it to contact you…]". These are square brackets, not braces.
- The Torch has no icon (K2's empty slot).
- My fixtures (both in the snapshot only): `tool/tester_author_seller.dart`, the Buyer save plus `items/plot/comlink`, `items/misc/g_i_torch01`, `items/plot/qcrystal_1_0` and `items/armour/g_a_clothes010`, written as `tester-seller` (the character is also named "Buyer"); and `tool/tester_author_feats2.dart`, Feat Bed plus `weapon_focus_blaster` and `weapon_specialization_blaster`, written as `blaster-bed` (Tester Strongroom).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
