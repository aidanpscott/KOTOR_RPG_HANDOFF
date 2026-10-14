# K2-PARITY-MAP-PT2746 — K2's Map screen against ours

**PT-2746 Part C, first pass (2026-10-13).** K2: `map_p.gui` (800×600) and the Peragus captures in `MAIN_WORK media/screens/pt2746-map/`; the study is `design/MAP-K2-CONTROLS.md`. Ours: the live app on the same canvas, with side-by-sides and the sign-off video in `media/screens/pt2746-map/ours/` (all private). Rulings: the PT-2746 entry in `PLAYTEST-RULINGS-01` (MAIN's picks on the owner's direction; the owner can overturn any when he reviews).

**Status:** `=` matches · `MEANS` built with a ruled difference · `X` excused (ruled or structural) · `OPEN` not resolved, not guessed.

## The screen
| K2 control | Ours | Status |
|---|---|---|
| Title "Map" (32181), the quick-menu icons, bars, Close, portrait footer | the shared K2 chrome, as Inventory and Options | = |
| `LBL_Area` 145,104 510×22, #CCCCB2: the area's name | the area's own `name` | = |
| `LBL_MapNote` 78,134 645×28, teal text in a framed bar: "Map Note: <name>" | the same; empty when no note is listed | = |
| `BTN_UP` / `BTN_DOWN` 92,138 and 690,138: step through the notes | the same, clicked; shown when more than one note is listed | = (keys: the play screen keeps every key but the menu toggles while a menu is open, `PT-2728`, so the notes step by the buttons, as K2's are buttons) |
| `LBL_Map` 106,168 588×294: a green grid with the explored part painted, a soft edge into the grid | the grid drawn at our square size, explored squares painted floor-grey and wall-dark from the area's tiles, a blurred dark edge into the grid; unexplored squares bare grid | MEANS (ruling 1: drawn from our grid in K2's map style; K2 paints one picture per area) |
| Doors | green ticks on the explored exits | = |
| Map notes: a teal ring; the selected one orange | the same | = |
| The party's location | the played character as a pale dot, companions teal; no one else | MEANS (K2's single arrow was not confirmed in the captures; enemies dropped by ruling: occupants are discovered) |
| `BTN_RETURN` 78,470 "Return to Spaceport/Hideout" | hidden, as K2 hides it on Peragus; the slot carries our line of areas entered (`PT-1509`), 306 wide | X (no such place) |
| Help box 41881 | K2's full line restored (`PT-2744` item c) | = |
| The minimap | not built | X (ruled: not now; agenda) |

## The exploration
| K2 | Ours | Status |
|---|---|---|
| Stored per area in the save (`AreaMap` bitmask); only ever adds; a load keeps it | `map.revealed` events in the log, per area and per played character, only the new squares; the save is the log, so load, Continue and bookmarks keep it | MEANS (ruling 3: the party reveals, kept on the played character's record) |
| About one map cell (≈10 m) round where the party walked | 5 squares round each party member, through no wall (AREA-FORMAT-01's line rule) | MEANS (ruling 2) |
| "Fully mapped" levels, by script or terminal ("Area map downloaded") | `mapped = true` on the area; a `map.revealed` with no squares also maps the whole area | MEANS (the terminal is on the agenda) |
| An arrival in a new area | explored at once on screen; written with the first step, so loading and quitting writes nothing (`PT-1605`) | = |
| Map notes: author-placed waypoints, switched by script | `[[map_notes]]` (name, square), listed once their square is explored; every exit listed too, by its own `map_note`, else by where it leads once that area has been visited, else "Exit" (`PT-1509`: the map does not name a place nobody has seen) | MEANS |
| **Which notes K2 lists** | listed once explored | **OPEN: K2's own listing rule is not resolved** (it is not "the note's square is explored": the 102PER exit sat on an explored cell unlisted, and Morgue was listed off the painted part). Ours is the ruled rule, not a reading of K2's. |
| The board in play | never fogged (`PT-1550`) | = (K2's fog is a map feature too) |

## Words on screen
K2's own words only: "Map", "Map Note", the area's name, the notes' names, "Exit". No name for the fog; the help line says "explored" and "fully mapped". No ids or grid coordinates (the text guard, `the_map_explores_test`).

## Not checked against K2
A fully explored level, companions revealing, and the party arrow: none of the Peragus saves shows them (`MAP-K2-CONTROLS`, "What I could not capture").
