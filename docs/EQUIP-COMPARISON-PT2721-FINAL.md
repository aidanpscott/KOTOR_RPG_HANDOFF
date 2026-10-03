# EQUIP COMPARISON — FINAL PASS (PT-2725): ONE ROW STILL FAILING (+ TEST 149 FIXES)

Paired screenshots (four states and the can't-use popup, K2 and ours): `HANDOFF/BUILD/screens/pt2721-equip-loop/final/` (`k2-1…5`, `app-1…5`, and the portrait zooms). K2 was played read-only (no slot written) and quit through its menu.

## The portrait block (owner's list) — measured, fixed, pixel-tested

Every figure is a pixel of K2's 1920×1080 picture, y off the window's 27 px title offset (anchored on the footer's top rule).

| Row | K2 | Ours before | Ours now |
|---|---|---|---|
| bars flush with the portrait | health x 1285→1314, portrait frame 1314→1484, force 1484→1515, all y 858→992; no gap | 3 px gap left, 1 px right; bars 857→993 | **PASS** — same boundaries; the new capture's pixel runs match K2's run for run (1285 AA, 1286–1288 (204,51,0), 1289 AA, fill 1290–1308, … 1314–1315 teal, 1484–1489 teal, fill 1491–1509) |
| portrait frame | (29,119,99): 4 px top, 2 px left and bottom, art 168×126 at (1316,863) | bright (26,178,140) 2 px rounded, inset 4 px | **PASS** |
| the green top lines (tab strips) | line (29,119,99) 2 px, fill (10,42,36); footer rule rows 910–912 | fill (6,25,21); rule rows 909–910 | **PASS** (fill by an alpha scale of the texture, rule 1 px lower) |
| bar colours | health outline (204,51,0) over (97,53,34); force outline (29,119,99) over (12,54,46) | same colours, 3 px outlines | **PASS** (with K2's anti-alias layers) |
| fill = current ÷ maximum | the bar fills from the bottom | same rule, tested at 0.5 and 1.0 | **PASS by rule** — a character below full was not reachable in K2 without a fight; `000008`'s struct reads full |
| name and class text | name x 1094→1194, class x 1077→1218 | 1094→1193, 1074→1218 | **PASS** within 3 px (the class line is 3 px wider in ours: letter spacing) |

Tests: `equip_portrait_flush_test.dart` (K2's pixels as literals); each of four mutations (a gap, the frame colour, the tab alpha, the footer rule) fails it.

## The two remaining items

| Row | Status |
|---|---|
| row hover | **PASS, owner-described (PT-2725)** — white, the same (187,188,168) as K2's selected-row border; the pointer-hover pixel is not verified (K2 would not show a hover under xdotool); verify against an owner screenshot with the pointer hovering |
| `Balanced` = `weaponsize` 2 | **checked on the Lightsaber (size 3), captured WITHOUT the line, and the Short Lightsaber and Blaster Pistol (size 2) WITH it.** A size-4 rifle or the double-bladed lightsaber was not reachable. Rule unchanged |
| non-energy damage line | **FAIL — not reachable.** Played K2 on foot from `000008`: the starting rotunda, the corridor and the medical bay (a container holding two Medpacs). No weapon pickup in reach without a long scripted stretch of the Peragus level. The owner supplies a save with a vibroblade or a sonic/ion weapon |

## EXCUSED rows and their rulings

- row 1 (frame) — `ASSET-REPLACEMENT-01` / `PT-1309`
- row 13 (grid shape) — owner, `PT-2721`
- row 14 (slot cell size) — owner, `PT-2725` (DECISION A)

## TEST 149 — the two blockers, fixed (screens re-captured after both)

1. **Menus take the whole frame.** The status row, the left party column, the turn-order column, the fight HUD, the area name and the hint line are not drawn under Equip, Inventory or Character; an Equip refusal is K2's popup shape on the Equip screen (it was drawn inside the item list box). `menus_take_the_whole_frame_test.dart`: each of the three menus, out of a fight with nothing to say, out of a fight with a status pending, and in a fight, draws none of the chrome and sits in the same rectangle in all three. Three mutations (sidebar back, status row back, refusal routed to the status line) each fail it. ⚠ Consequences: the left column no longer switches characters from Inventory or Character (until each has its own pass), and a status message such as "took hold-out-blaster" no longer shows on a menu; two tests followed the ruling (`open_portrait_switches_control_test`, `looting_test`).
2. **Two shield families, two slots**, from `baseitems.2da`'s equipable-slots column, read in both games: `Forearm_Bands` 0x180 = arm_l + arm_r; `Droid_Shield` 0x400 = **belt**. My `shield-generator` base-level `forearms` was right for 17 shields and wrong for the 14 droid ones. Each shield item now states its own `worn_at` (`gen_base_rules.py`, the `EQUIPMENT-01 §9` note), `slotsForBaseType(itemWornAt:)`. Test: 14 droid shields → belt, 17 forearm → arms; the droid filter test now uses the belt list. **Fixture:** `droid-shield-bed` on the shelf — a merchant whose stall sells a droid shield (Droid Deflector Mark I) and an organic one (Telos Mining Shield); not in any campaign package.

## Closing suites (run one at a time; `TMPDIR` on disk for Lodestar)

| suite | result |
|---|---|
| app (`2f5abd9`) | **2001 passed, 0 failed** |
| Lodestar | **1870 passed, 0 failed** |
| Lens (`2bad745`) | **13 passed, 0 failed** |
| Loom (`083e570`) | **430 passed, 0 failed** |

The first full app run found two real failures (both from the whole-frame ruling) and Loom found three stale ones: its palette counts (`65`→`87` shipped with the 22 loadout blueprints PT-2722 added, `910`→`923` poured with the 13 `Stealth_Unit` belts, `81`→`92` skill rows) and its writer, which did not yet add the item's `Armor N` to an armour class; it does now, so Loom and `gen_base_rules.py` write the same bytes. ⚠ Lodestar's first run reported 37 failures that were all `No space left on device` in the 793 MB `/tmp` tmpfs, not tests.

NOT READY FOR SIGN-OFF: the non-energy damage line remains the one FAIL (no reachable weapon).
