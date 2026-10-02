# ARMOUR DEFENCE — BEFORE / AFTER (PT-2725 pass 3)

**Ruling:** `PT-303` — *"`Armor 5` does NOT mean Defence 5. It means +5 on top of the base item's class"* (checked against the wiki's totals: Mandalorian Assault Armor, `Armor 4` on class 9, Defense Bonus 13); `EQUIPMENT-01 §5` — Defence = 10 + *armour bonus* + capped Dexterity, the armour bonus being the class (`baseac`) the item is on; `PT-2144` — an item whose Defence is not its class's carries the finished number on its blueprint. The generator wrote it for `DecreaseAC` only; `Armor N` was extracted (`stats`) and never joined. **This is a data fix, not a rules change.**

K2 observed on three items (fresh captures, `000008`): Light Combat Suit 4 − 1 = 3, Reinforced Fiber Armor 5 + 2 = 7, Jamoh Hogra's 7 + 4 = 11.

## Which fights actually change

**Three shipped blueprints** (`items/loadout/`: Light Combat Suit 4→3, Reinforced Fiber Armor 5→7, Jamoh Hogra's Battle Armor 7→11). No starting-kit or standard blueprint carries an `Armor N`, so no new game's Defence moves. Every other armour is a palette item an author instantiates; it takes the same number through the same generator when a blueprint is written for it.

## Every armour-class item in the catalogue, class → resulting Defence bonus (before = the class number)

| class | items | items whose number changes | resulting Defence bonus (count) |
|---|---|---|---|
| armour-class-4 (before 4) | 19 | 17 | 3×2, 4×2, 5×8, 6×1, 7×5, 8×1 |
| armour-class-5 (before 5) | 18 | 16 | 5×2, 6×5, 7×5, 8×2, 9×4 |
| armour-class-6 (before 6) | 19 | 16 | 6×3, 7×5, 8×4, 9×4, 10×3 |
| armour-class-7 (before 7) | 14 | 11 | 7×3, 8×4, 9×4, 11×2, 13×1 |
| armour-class-8 (before 8) | 15 | 12 | 8×3, 9×2, 10×4, 11×1, 12×5 |
| armour-class-9 (before 9) | 19 | 17 | 9×2, 10×3, 11×4, 12×2, 13×6, 14×2 |

## ⚠ Items with more than one `Armor N` (sum taken; K2's stacking rule for them is NOT observed)

| resref | name | `Armor` values | resulting |
|---|---|---|---|
| g_a_class8005 | Calo Nord's Battle Armor | [1, 3] | 12 |
| g_a_class9005 | Jurgan Kalta's Power Suit | [1, 3] | 13 |
| g_a_class9009 | Cassus Fett's Battle Armor | [1, 4] | 14 |
| g1_a_class5001 | Light Exoskeleton | [2, 1, 1] | 8 |
| g1_a_class5002 | Baragwin Shadow Armor | [2, 2] | 9 |
| g_a_class4006 | Darth Bandon's Fiber Armor | [1, 2] | 7 |
| g_a_class4009 | Echani Fiber Armor | [1, 2] | 7 |
| g_a_class5007 | Eriadu Prototype Armor | [1, 3] | 9 |
| g1_a_class6001 | Environmental Bastion Armor | [1, 1, 1] | 9 |
| g1_a_class8001 | Heavy Exoskeleton | [2, 4] | 13 |

NWN-style stacking could take the highest instead of the sum for equal subtypes; no K2 capture of such an item exists. None of these is a shipped blueprint.
