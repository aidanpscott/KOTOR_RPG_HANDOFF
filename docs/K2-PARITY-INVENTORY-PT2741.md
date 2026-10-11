# K2-PARITY-INVENTORY-PT2741 — the Inventory screen against K2, element by element (first pass, PT-2742)

Sources: K2's `inventory_p.gui` (800×600 canvas, read with `scripts/gffparse.py`), its strings from `dialog.tlk`, and the live K2 captures in `HANDOFF/BUILD/screens/pt2741-k2-session/` (a save with 22 items, every count 1, the player alone). Ours: the live app at 1920×1080, `HANDOFF/BUILD/screens/pt2742-inventory/` (K2 left, ours right). The owner's list of what differs: `design/INVENTORY-K2-CONTROLS.md`.

Excused, as for every K2 screen: the frame (`PT-1309`), Orbitron's glyph widths and slashed zero for K2's `dialogfont16x16`, Liberation Sans Bold for `fnt_d16x16`.

| Element | K2 | Ours | Status |
|---|---|---|---|
| Title "Inventory" (48621), the eight quick-menu icons | yes | the shared K2 chrome | = |
| FILTER block (`LBL_BAR6`/`LBL_FILTER`, 48548) | filled teal block, "Filter" | same | = |
| Tab strip between `LBL_BAR1` and `LBL_BAR2` | All, Datapads, Weapons, Armor, Useable, Quests, Misc (48549, 48543-48547, 48783), text only; the lit tab pale (216,216,195), the others teal; pointer: `HILIGHT` #CCCCB2 | same, measured colours | = |
| **New tab** | not in K2 | right after All, K2's tab art (text only, same states); K2's word 238 "NEW", drawn as "New" so it sits in the small caps like its neighbours | **owner-ruled difference (`PT-2742`)**. Lists items picked up (looted, bought, recovered; never the starting kit) and not yet selected here; selecting clears it, opening and closing does not; stored in the log (`item.examined`, campaign), so save, load, Continue and bookmarks carry it. Empty: both panes blank |
| The tabs' spacing | seven at the `.gui`'s lefts and widths across 155-736 | eight across the same span, each 94% of K2's width | **difference made by New**: the strip is squeezed to fit it |
| `LB_ITEMS` box and its scroll bar | 78,134 318×329; arrows and a thumb that rides the list | same; the thumb follows the list's scroll | = |
| A row | 34 px icon cell (rounded, the row's line) beside a bar; bronze line (122,105,63), fill (5,24,21), name in teal, centred | same, measured | = |
| Item icons | K2's own art | the Equip pipeline's (`assets/extracted/items/`); an item with no extracted art has an empty cell | = where extracted; the rest wait on `PT-2701` (all item art) |
| Hovered row | pale name (186,187,169), a darker inset (0,12,10) inside the bar; the description follows the pointer | same | = |
| Chosen row | teal line (30,121,100), dark fill | same | = (K2's opening frame also showed the first row with a bright gold line, possibly a pulse; **not modelled**) |
| On opening | the first row selected, its description shown | same (choosing it is not "selecting" it for New) | = |
| `LB_DESCRIPTION` | 410,134 313×300; requirements, numbers, flavour text, in `fnt_d16x16` | same layout, filled from OUR rules' numbers | MEANS (the owner's list) |
| Empty list | both panes blank | New: blank. Other tabs: our `PT-2493` sentence ("nothing here under …", "carrying nothing …") | **waiting on the owner** (question 3) |
| Worn items | not listed ("items not currently equipped") | listed with "(Equipped)" (`PT-1251`) | **waiting on the owner** (question 2) |
| Credits (`LBL_CREDITS` 5766, value right-aligned) | "Credits" and the amount | same; "—" with no purse (`PT-2491`) | = (question 6 asks to keep the dash) |
| Use Item (`BTN_USEITEM`, 333) | dim unless the selected item is usable; pointer: pale border | same; live for medpacs, adrenals, shield generators, grenades, mines, rockets (what our rules call consumables) | = for the look. **What it does is waiting on the owner** (question 4); today it still says the board's keys spend it |
| Close (`BTN_EXIT`, 1582) | yes | yes; Escape too | = |
| First-open help box (42136) | yes, once | none | **leave out recommended** (Tutorial Popups ruled out at `PT-2734`; question 5) |
| Portrait footer | name, class and level, portrait | shared with Options and Equip | = |
| Keys | not captured | the arrows move the selection, Escape closes, **no key reaches the map** | tested |
| Hide Unequippable | K2's help: the Equip screen only | the Inventory ignores it | = |
| Item sorting into tabs | by item type | by the base type's section and the item's own category. **Fixed here:** catalogued items (the starting kit, store items) all landed in Misc | = |

## Not capturable yet (the owner's Telos save)
Stacks and how K2 shows a count; party switching in the footer; a droid's inventory (T3-M4).

## Tests (real play)
- `a_new_item_stays_new_until_selected_test.dart`: a character buys a vibroblade from the Store Bed merchant. It is under New and under Weapons; opening and closing keep it; F4, then selecting it clears it (New blank, no sentence); F5 to the quick save brings it back; selecting again, leaving and Continue keep it cleared; with the Inventory open, arrows, S and Space move nobody; the text guard covers the screen. Plus the rule on its own (the starting kit is never new; a second pickup after looking is new again). **Mutation-checked six ways**, each failing: selection writes nothing; written but not saved; opening clears the first row; an empty New says a sentence; examining never clears; the starting kit counts as new.
- `the_inventory_screen_test.dart` (K2's strings), `nothing_escapes_the_frame_test.dart`, `emitted_kinds_test.dart` (72 kinds).
