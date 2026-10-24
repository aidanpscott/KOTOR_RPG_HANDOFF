# TEST 195: in-game batch 1 (frame, menu bar, Equip, Inventory, Character, store, help boxes)

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-195/` (MAIN_WORK `a0a4a87b`). The step-by-step log is `TEST/reports/195-running-log.md`. Compared against `MAIN_WORK/media/study/pt2752/k2-ingame/`.

## Build

App `ec4c190`, git archive from my own clone. `gate.py --at ec4c190`: "FOR TESTER — CORE at ec4c190, 5004 tests, 0 failed"; ARCHIVE last green at ec4c190, after the fcf7d0c milestone. Lodestar `240bc46` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `9706207`; check_shelf clean. The build (10.0 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Character: Frame One, a Human Female Soldier made through chargen in Store Bed (a new game, so the help-box rule could be tested).

## Owner's comment, relayed live during the run

"The store looks quite good actually. I may want to consider using ours honestly, but maybe having more filters." Recorded here for MAIN. For reference: K2's own inventory filters are All, Datapads, Weapons, Armor, Useable, Quests and Misc; our store has All, Weapons, Armor and Misc.

## Summary: most pass; three findings

| # | Check | Result |
|---|---|---|
| 1 | Frame | **PASS** on Equip, Inventory and Character (K2's frame, stretched). Options, Party Selection, Journal and Messages still use the old frame; they weren't in this batch's list |
| 2 | Menu bar | **PASS**: eight buttons and the title box as in K2's capture; the fifth is Party Selection; Messages opens from the Journal's Messages Log |
| 3 | Equip | **PASS** for the arrangement: Head on top, Implant / Body / Hands, arms with Belt between, Boots below Belt, the configs, Switch Weapons. Attack Modifier and Damage at K2's size; empty slots full strength on black; opens on Body. Boots, Body and both weapon configs were filled and nothing overlaps. Head, Hands, Belt, Implant and the arms couldn't be filled: Store Bed's merchant sells none of those |
| 4 | Inventory | **PASS**: as K2's capture (filters, list, description, Credits, Use Item, Close), plus a "New" filter |
| 5 | Character | **PARTIAL**: K2's table, alignment slider, arcs, Experience/Needed, footer ("Frame One / Soldier 1") and tabs are all there. Character Info has the band and score (Neutral 50) and feats with sources. No "Armour" anywhere (parked item closed). **Findings** below |
| 6 | Store | **PASS** at 1920 and 1280×720: labels whole, in K2's face and size, in gold (parked item closed). Bought a Medpac (Credits 100 → 60, In Inventory 2 → 3) and sold one (60 → 100, 3 → 2). **Finding**: chargen's Purchase Gear has empty Armor and Misc tabs |
| 7 | Help boxes | **PASS**: shown on the first visit to Party Selection, Messages and Map. After F4, kill -9, relaunch and Continue, none of the three shows again |
| 8 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 29), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings, most important first

1. **The Character page has no Level Up or Auto Level Up button** (`i05a`). The batch says Auto Level Up dim, and Level Up shown only while a level waits, with its reason under it when dead. Neither appears at all, so the only way to reach level-up from the new page is unclear.
2. **Chargen's Purchase Gear: the Armor and Misc tabs list nothing** (`i06e`, `i06f`). Weapons and All list items.
3. **Character Info is missing several lines.** There are no languages, no gear notes and no Defense "—" reason. The Experience/Needed box shows its labels but no numbers on this tab (they show on Stats). The portrait's left edge doesn't meet the alignment bar; there's a gap.

Small: the merchant's buy and sell prices are both 40 for a Medpac. In Stock stayed at 10 after I bought one.

(Withdrawn during the run: I first thought help-box OKs ignored clicks. My clicks had been at half-scale coordinates; a click on the real OK works.)

Known and not filed: End Turn over the meditation line, forms on Abilities, the droid's Attacks tab, the store's gold being reasoned, Inventory/Equip lit rows, the scroll bar width.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
