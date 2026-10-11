# K2-PARITY-INVENTORY-PT2741 — the Inventory screen against K2, element by element (first pass PT-2742; the owner's rulings PT-2743)

Sources: K2's `inventory_p.gui` (800×600 canvas, read with `scripts/gffparse.py`), its strings from `dialog.tlk`, and the live K2 captures in `MAIN_WORK media/screens/pt2741-k2-session/` (a save with 22 items, every count 1, the player alone). Ours: the live app at 1920×1080, `MAIN_WORK media/screens/pt2742-inventory/` (K2 left, ours right). The owner's list of what differs: `design/INVENTORY-K2-CONTROLS.md`.

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
| Empty list | both panes blank | both panes blank, every tab (`PT-2743` ruling 3; `PT-2493`'s sentence retired on this screen) | = |
| Worn items | not listed ("items not currently equipped") | **listed, pinned at the top**: in each tab, the equipped items that belong to that tab come first, marked "(Equipped)", then the rest; in All, every equipped item first (`PT-2743` ruling 2) | **owner-ruled difference**. "Regardless of which category" was read as: pinned at the top of every tab THEY BELONG TO, not shown in tabs they don't belong to |
| Credits (`LBL_CREDITS` 5766, value right-aligned) | "Credits" and the amount | same; **0** with no purse ever recorded (`PT-2743` ruling 6; `PT-2491`'s dash retired here). No other screen showed the dash: the Store always shows a number | = |
| Use Item (`BTN_USEITEM`, 333) | dim unless the selected item is usable; pointer: pale border | live for medpacs, adrenals and shield generators; **dim for grenades, rockets and mines**, as K2. A medpac heals its amount and an adrenal gives its timed ability bonus to the player: the rules' Gear use (ACTION-ECONOMY-01 §3), free outside a fight, one Gear in it (Lodestar `useGear`, new `useAdrenal`); a shield goes up as the Gear key raises it. Spent only when the use goes through; a refusal is said in K2's box | = (`PT-2743` ruling 4). Treat (`t`) unchanged |
| Close (`BTN_EXIT`, 1582) | yes | yes; Escape too | = |
| First-open help box (42136) | yes, once | yes, once, for a new game, K2's box, font and OK; **owner-ruled wording**: "The INVENTORY screen shows a list of all the items this character carries. Items currently equipped are listed first, at the top of each list." (our inventory is the character's own bag, not shared by the party) | `PT-2743` ruling 5 and its addendum |
| Portrait footer | name, class and level, portrait | shared with Options and Equip | = |
| Keys | not captured | the arrows move the selection, Escape closes, **no key reaches the map** | tested |
| Hide Unequippable | K2's help: the Equip screen only | the Inventory ignores it | = |
| Quests | items whose type is a quest item | **a tag the adventure sets** (the package: a blueprint's `quest = true`; or the giving event: `item.acquired` with `quest = true`), removed by `item.quest-done`; a tagged item shows under its own tab AND Quests, All once; carried by save, load and bookmarks. The Strongroom's Sith Keycard is tagged | owner-ruled (`PT-2743` ruling 1) |
| Item sorting into tabs | by item type | by the base type's section and the item's own category. **Fixed here:** catalogued items (the starting kit, store items) all landed in Misc | = |

## Not capturable yet (the owner's Telos save)
Stacks and how K2 shows a count; party switching in the footer; a droid's inventory (T3-M4).

## Tests (real play)
- `a_new_item_stays_new_until_selected_test.dart`: a character buys a vibroblade from the Store Bed merchant. It is under New and under Weapons; opening and closing keep it; F4, then selecting it clears it (New blank, no sentence); F5 to the quick save brings it back; selecting again, leaving and Continue keep it cleared; with the Inventory open, arrows, S and Space move nobody; the text guard covers the screen. Plus the rule on its own (the starting kit is never new; a second pickup after looking is new again). **Mutation-checked six ways**, each failing: selection writes nothing; written but not saved; opening clears the first row; an empty New says a sentence; examining never clears; the starting kit counts as new.
- `the_inventory_screen_test.dart` (K2's strings), `nothing_escapes_the_frame_test.dart`, `emitted_kinds_test.dart` (72 kinds).

## The help boxes, reworded where K2's words describe what this game does not have (`PT-2743` ruling 5, for the owner)
Every K2 first-open box from `tutorial.2da` whose screen exists here, shown once for a new game (chargen marks the character), K2's box (`confirm_p.gui` grown to fit), the screen's quick-menu icon, the text in the description face, OK. K2's Scripts screen (41878) has no box: the screen does not exist. The gameplay tutorials (grenades, mines, pausing, kolto tanks…) are not screen boxes and are not built.
| Screen | K2 (string) | Reworded line | Why |
|---|---|---|---|
| Inventory | 42136: "…not currently equipped by other party members or the companions back at your base. This inventory is shared by all party members." | "The INVENTORY screen shows a list of all the items this character carries. Items currently equipped are listed first, at the top of each list." | owner's wording: worn items are listed, no base, not a party bag |
| Messages | 41880: "…experience points gained, attack and damage rolls and Dark Side/Light Side shifts." | "…experience points gained and attack and damage rolls." | no alignment shifts yet. **Restore K2's line when Light/Dark Side lands (PT-2744 2a)** |
| Map | 41881: "…the explored area of the level… map notes… Some levels (such as city areas) are fully mapped…" | "The Map screen shows the area and your party's location." | no exploration fog, no map notes. **Restore K2's line when map fog and notes land (PT-2744 2b)** |
| Party Selection | 47886: "…without having to return to your base. Characters switched out of your party will wait for you back at your base." | "…This is done instantly." | no base |
| Skills (and chargen's) | 42533 / 41885: "Security + Wisdom modifier" | "Security + Intelligence modifier" | our Security uses Intelligence |
| Feats | 42534: "some feats (POWER ATTACK) are used during combat" | "some feats are used during combat" | no Power Attack feat |
| Force Powers (and chargen's) | 42535 / 41887: the Light/Dark Side cost sentences | **K2's own line, restored** (2026-10-11) | Light/Dark costs are built (`ALIGNMENT-01 v3 §1.3`, D-AQ), so the reworded line went |
Word for word: Equip (49018), Journal (41882), chargen Attributes (41884), chargen Feats (41886).
