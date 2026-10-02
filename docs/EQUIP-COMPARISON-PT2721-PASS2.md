# EQUIP-COMPARISON-PT2721 — PASS 2 (2026-10-02, `KOTOR-RPG-APP` `f7e3320` + the commits after it)

*K2's Equip screen beside ours, 1920×1080, the same character, four states, one row per element. Pictures: `HANDOFF/BUILD/screens/pt2721-equip-loop/pass-2/` (`app-*.png` ours, `side-*.png` K2 over ours). **K2's side is `pass-1/k2-*.png`, reused**: it is the same save (`000008 - game7`), read-only, and K2 does not change; ours is fresh. Numeric extents below were scanned off both pictures, not read by eye.*

**Same gear on both sides now (D1):** the 22 items of `000008 - game7` (8 worn, 14 bagged) are in the catalogue (19 `k2`, 3 `both`, 0 `k1`); 20 are built as blueprints and carried by our character. Two belts are not (see D1 below).

## The numbers (1920×1080, scanned)

| element | K2 | ours |
|---|---|---|
| title box (top / bottom line) | 100 / 148 | 101 / 150 |
| the eight buttons, left edges | 855, 968, 1081, 1193, 1306 … | 854, 967, 1080, 1193, 1306 … |
| list box (left / right line) | 188 / 933 | 187 / 933 |
| description box (left / right line) | 985 / 1718 | 984 / 1718 |
| list rows (top lines) | 249, 287, 325, 363, 401 | 249, 287, 325, 363, 401 |
| row height / pitch / icon cell | 36 / 38 / 34 | 36 / 38 / 34 |
| footer buttons | 181–468, 493–684 | 180–467, 492–683 |
| wash inside a box | (8,36,29) | (8,36,29) (pixel-tested) |
| border line | (29,119,99), 2 px | (29,119,99), 2 px |
| "Attack Modifier" width | 143 | 144 |

## Rows (the 46 of pass 1, re-read)

**47 rows, counted from the table's own status column: PASS 42 · EXCUSED 3 (rows 1, 13, 36b) · DECISION 2 (rows 8b and 14) · FAIL 0.** (The 46 of pass 1, plus 8b, 31b and 36b, with 43–45 merged.) Outside the rows, three **data** items need a ruling (below): two belts and the mining shield's slot, and the shield's name.

| # | element | status | note |
|---|---|---|---|
| 1 | frame | **EXCUSED** | the bronze is recreated (`ASSET-REPLACEMENT-01`); K2's is a photographed texture. Position and size match |
| 2 | content layout fills the screen | **PASS** | boxes at the GFF's extents on the stretched canvas; 747/735 px |
| 3 | party rail | PASS | none, owner ruling |
| 4 | area name / hint line | PASS | none |
| 5 | play-view status row, fight HUD | **PASS** | status line, defence line, key line and pip strip are not drawn under any menu; the message row is not drawn under Equip (a refusal is carried on the screen), so a menu mid-fight is the same box (`PT-2723` item 1) |
| 6 | opens on Body | PASS | |
| 7 | title | **PASS** | bordered box, ±2 px, "Equip" centred in it |
| 8 | the eight icons | **PASS** | size, pitch and border ±1 px; the textures drawn × tint so the black detail (the map's N, the character's ?) shows |
| 8b | the Inventory icon is dimmer in K2 | **DECISION** | K2 draws only Inventory at (36,146,123) against the others' (49,196,165). Reason unknown; not replicated. Replicate it? |
| 9 | order | PASS | |
| 10 | Map | **PASS** | enabled, opens the `m` overlay, tested from two screens (D2) |
| 11 | active icon | **PASS** | bone (217,217,196), no fill or outline |
| 12 | subtitle | PASS | centred between the rules |
| 13 | grid shape | **EXCUSED** | owner, `PT-2721` |
| 14 | slot cell size | **DECISION A** | see below: ~80 px cells, not K2's 130×97 |
| 15 | selected-slot mark | **PASS** | bone (196,196,176), 2 px |
| 16 | icon inside each filled cell | **PASS** | the item's own K2 art, derived from each `.uti` |
| 17 | empty cell | PASS | |
| 18 | DEF badge | PASS | shape and label; the number differs (18 / 17): a rules difference |
| 19 | Attack Modifier / Damage | **PASS** | K2's strings and extents, K2's size (144 vs 143 px); values differ (gear/rules) |
| 20 | Config 1 / 2 | PASS | |
| 21 | Switch Weapons | **PASS** | a bordered button at `BTN_SWAPWEAPONS`, plus `LBL_BAR5`'s tab strip in both states |
| 22 | list in the slot view | **PASS** | icons, a mark on the equipped row, "None" without its bar as K2 draws it |
| 23 | list box | **PASS** | |
| 24 | row height / pitch | **PASS** | 36 / 38; the GFF's `PROTOITEM` (270×62) is not what K2 draws |
| 25 | None row | **PASS** | ⊘ in a 34 px cell |
| 26 | row text | PASS | |
| 27 | row icons | **PASS** | |
| 28 | names | **PASS** | "Light Combat Suit", "Jedi Robe", … (the document's UNIQUE marker cut) |
| 29 | built from a starting blueprint | PASS | |
| 30 | two items of one base type | PASS | |
| 31 | selected row | **PASS** | bone border, (5,15,12) fill |
| 31b | hover row | **PASS** | orange (204,51,0); NOT "equipped" — K2 says equipped in the text |
| 32 | equipped mark | PASS | |
| 33 | scrollbar | PASS | 14 px beside the box |
| 34 | description box | **PASS** | |
| 35 | description font | **PASS** | Liberation Sans Bold on K2's `fnt_d16x16` (D3, ruled) |
| 36 | description content | **PASS** (shape) | K2's paragraph layout: "Feats Required:" over the feat, blank lines, bare "Defense Bonus", "Max Dexterity Bonus: +5", prose |
| 36b | description numbers | **EXCUSED** | "Defense Bonus: 4" against K2's 3 — a rules difference (ruled) |
| 37 | developer notes in player text | **PASS** | never rendered (D4) |
| 38 | description text size | PASS | |
| 39 | CLOSE / CANCEL+OK | **PASS** | 288×50, K2's strings ("Close", "Cancel") |
| 40 | portrait | **PASS** | Onjo Trigit's own face (`po_pmha01`), 168×126, with the vitality and force bars either side |
| 41 | name + class + level | **PASS** | class right-aligned to 498, the level its own label at 506 |
| 42 | other members | PASS | |
| 43–45 | font | **PASS** | Orbitron small caps, widths within ~1% |
| 46 | colour | **PASS** | text (49,196,165), selected (187,187,167), line (28,119,98), measured |

## The open items — each needs a ruling

- **DECISION A — the slot cells.** Ours are about 80 px square, K2's 130×97. The cause is the owner's arrangement: our lattice is seven rows tall (`PT-2695`, "I know this breaks a bit with the original game") and K2's is five, so at K2's cell size ours does not fit K2's pane; the figure is scaled to fit, and its text is kept at K2's size. **Recommend:** keep the arrangement and accept smaller cells (**EXCUSED, owner PT-2721 diamond**), or move to K2's three-column grid (`implant head hands / arm body arm / · belt ·`, Boots in an empty cell) where every cell is K2's size. The second matches the picture; it reverses a deliberate owner choice, so it is the owner's.
- **D1 gap — two belts cannot be built.** The Stealth Field Generator and the Frozian Scout Belt are `Stealth_Unit` in `baseitems.2da`, which the catalogue gives no base type, so no blueprint can be made. K2's Belt list has four items; ours two. Needs a base type ruled for `Stealth_Unit`.
- **D1 gap — the mining shield cannot be offered for an arm.** `100_fore01`'s base type, `shield-generator`, is "worn AND spent" and carries no `worn_at`, so a carried one is never offered for the arm slots (a worn one now shows its icon and name). Needs `worn_at = "forearms"` ruled for it.
- **D1 conflict — the shield's name.** The catalogue (the corpus documents) says "Peragus Mining Shield"; K2's own `dialog.tlk` (the installed game) says "Telos Mining Shield". The corpus's `k2_dialog.tlk` has 136,551 strings and the installed game's 136,329, so the two TLKs differ, and **item descriptions (`items.toml`, `description`) were resolved from the corpus copy**. Worth a check whether any other description differs.
- **8b — the Inventory icon's dimness** (above).

## Fixes made this pass (each with a test that failed first and a mutation check)

K2 border wash; nav icons × tint; the row icon cell and the icon's size; the selected slot cell; the lattice text size; K2's own label strings; the class and level labels; the vitality and force bars; `LBL_BAR5` and the Switch Weapons button; the paragraph layout of the description; `ItemRecord.displayName` and `.base` (the Jedi Robe was missing from Body's list); the catalogue join for items whose base type is also consumable; the "None" row in the slot view; the title text (a first reading, which put it high, was corrected by the side-by-side).
