# TEST 195 running log (draft, text only)

Started 2026-10-24. Tester, Xvfb :2, own data dir. In-game batch 1 (frame, menu bar, Equip, Inventory, Character, store, help boxes).
Known, don't file: End Turn over meditation (batch 3); forms on Abilities, droid Attacks tab (batch 2); store gold reasoned; Inventory/Equip lit rows; scroll bar width.

## Build
- App ec4c190, git archive from my own clone to builds/test195. Built through the lock: 10.0 s. pubspec.lock unchanged.
- Gate: "gate.py --at ec4c190" -> "FOR TESTER — CORE at ec4c190, 5004 tests, 0 failed, 12m00s at -j 3, peak 1738 MB"; "ARCHIVE last green at ec4c190" (after the fcf7d0c milestone).
- Lodestar 240bc46 = lock = compiled. Lens 5fe60a9. Loom: no entry.
- Shelf 9706207 (as ordered). check_shelf: 33 rules files, 125 blueprints, identical.
- K2 captures: MAIN_WORK/media/study/pt2752/k2-ingame/ (01..91).

## Items

### Frame One (Human Female Soldier, Store Bed, new game)
User note (owner, relayed live): "The store looks quite good actually. I may want to consider using ours honestly, but maybe having more filters." Recorded for MAIN.
6. Chargen Purchase Gear store: restyled K2 store (gold), labels whole. FINDING: Weapons lists items, but ARMOR and MISC tabs show EMPTY lists (MAIN: all three now list items). The All tab shows everything (Quarterstaff, Short Sword, ...).
2. Menu bar (Options page): eight buttons and the title box like K2's 90-options; fifth = Party Selection. PASS. Note: Options keeps the old bronze frame (not in this batch's list?).
3. EQUIP: K2 frame (stretched), opens on Body (Clothing equipped), help box on first open. Slot group: Head on top, Implant/Body/Hands, L-arm/Belt/R-arm, Boots below Belt (Dockworker's Treads), Config 1/2 with weapons; Attack Modifier/Damage at K2's size; DEF 13 shield. Empty slots full strength on black. PASS for the arrangement. Each empty slot opens an empty list ("nothing equipped in this slot"): this package's merchant sells no head/hands/belt/implant/arm items, so only Boots/Body/weapons could be filled; nothing overlapped.
6. Merchant store (Dressa) at 1920: K2 gold, labels whole (Item Cost / Credits / In Stock / In Inventory). Bought a Medpac: Credits 100 -> 60, In Inventory 2 -> 3 (In Stock stayed 10). Sell list: Adrenal Strength, Frag Grenade, Medpac; sold a Medpac: Credits 60 -> 100, In Inventory 3 -> 2. PASS. Note: the buy price and sell price are both 40.
4. INVENTORY: like K2's 20-inventory (filters, list, description, Credits 100, Use Item, Close); an extra "New" filter tab. Help box on first open. PASS.
(Withdrawn: my clicks on the help-box OK were at half-scale coordinates; a click at the real OK works.)
5. CHARACTER: K2 frame, alignment slider (Light/Dark), arcs, table, Experience 0 / Needed 1000, footer "Frame One / Soldier 1", tabs Stats / Character Info / Backstory. Character Info: Alignment Neutral (50), Species Human, Class Soldier, Gender Female, Feats (Squad Tactics granted, Cautious chosen). FINDINGS: (a) no Auto Level Up / Level Up anywhere on the page; (b) Character Info has no languages, gear notes or Defense reason line; (c) the Experience/Needed box shows no numbers on the Character Info tab; (d) the portrait's left edge does not meet the alignment bar (a gap). No "Armour" seen on Stats or Character Info (OCR): PASS for parked item 2.
7. Help boxes: first visits showed them on Party Selection ("In most areas you can use the PARTY SELECTION screen..."), Messages (from Journal > Messages Log), Map. After F4, kill -9, relaunch, Continue: Party, Messages, Map open with no help box. PASS (once per new game, not every session).
Note: Party Selection, Journal and Messages still use the old frame/fonts (not in batch 1).
6. Store at 1280x720: labels whole and readable (Item Cost 40, Credits 100, In Stock 10, In Inventory 2), description 'Single Use / A medpac contains ...'. PASS (parked item 1 closed).
8. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 29 "reg195", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
