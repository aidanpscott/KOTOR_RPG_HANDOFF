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

## LIVE-APP PROOF (owner order, 2026-10-03) — the running release build, read against K2 pixel for pixel

**What was run.** `flutter build linux --release` from a **fresh clone of `origin/main`** (`KOTOR-RPG-APP-live3`, never the conflicted folder), head `83f9134`; launched at 1920×1080 on a virtual display, window title **"Knights of the Old Republic RPG"**, PID **286975**; played Library → Endar Spire → Continue → Equip (`q`), and the five states captured exactly as K2's final set (filled slot, empty belt slot, the item list, the robe's description, the can't-use popup on Jamoh Hogra's). Images, list-panel crops side by side with K2's `k2-*.png`, description-pane crops and one full-screen pair per state are in `HANDOFF/BUILD/screens/pt2721-equip-loop/live-app/`.

**The earlier `final/` captures came from the running app** (a debug build driven by `drive.sh` and xdotool), **not a test harness** — but they were read by eye, and the running-app proof read them by pixel. That is where these came from:

| # | difference found in the running app | cause | fix (test first, mutation-checked) |
|---|---|---|---|
| 1 | The selected row **breathes** (border, text) — a still frame cannot show it | K2's HILIGHT pulses on the screen clock | `_breath`; `PulseClock` |
| 2 | Wash not flat | ring/interior opacity | `K2Border` wash |
| 3 | Row side edges squashed | edge tile | solid side edge |
| 4 | Canvas boxes on fractions of a pixel: every 2 px line anti-aliased to ~82% | the frame's opening origin was fractional (241.6) | opening snapped to whole pixels; `equip_k2_layout_test` |
| 5 | Portrait art had its own left edge | owner: "no left and right edges, it touches the bars" | art flush; `equip_portrait_flush_test` |
| 6 | **Scrollbar was a solid bright bar** | K2's is a framed track: 1 px dim frame, 2 px black, 8 px thumb; arrows native 16×16 in the dim line colour; thumb rows 261→875 in both now | `_scrollbar`; pinned |
| 7 | Selected row fill was constant | K2's fill breathes *against* the border: (5,26,22) at the dimmest, (0,12,10) at the brightest | `_breathFill` |
| 8 | Can't-use popup 456×214 at (410,443) | K2: 456×217 at (411,441) | `_atNudged`; pinned |
| 9 | "None" printed a line of its own | K2 prints **nothing** in the pane for None | blank pane |
| 10 | Description line pitch 24 px | K2: 19.2 (16 × 1.2) | `lineHeight 1.2` |
| 11 | Description first line 2 px high | K2's glyph rows start 2 px lower | top inset 13 |

After 4–11 the measured bands agree to within 1 px: description text rows (257, 276, 333, 371, 409 vs K2's 257, 276, 332, 371, 408), scrollbar thumb 261–875 in both, popup border (411,441)–(866,657) in both.

**What still differs, and why it is not a fail.** (a) The outer chrome frame — row 1, `ASSET-REPLACEMENT-01` / `PT-1309`. (b) The slot grid's shape and cell size — rows 13/14, owner `PT-2721` / `PT-2725` DECISION A. (c) Glyph widths: our two faces are the owner-picked OFL fonts (`PT-2722`), not K2's atlas — the prose line "Members of the Jedi Order…" measures 603 px against K2's 631 (−4.4%), the UI face's list rows are slightly wider-spaced; **the font ruling covers it, but the number is recorded so it can be re-opened.**

## The non-energy weapon (vibroblade) — read from K2 on the owner's save, 2026-10-02

K2 prints, for the Vibroblade: `Feats Required: Weapon Proficiency -  Melee Weapons` / `Damage: Physical, 1-10` / `Critical Threat: 19-20,x2` / `Balanced: +2/+0 vs. two-weapon penalty if used in the off hand` / **`Fully Upgradeable`** / the description. No `Range:` line (melee).

- **Fixed:** K2 names the damage *flag group*, not the blade. Ours printed `Piercing`; it now prints `Physical`.
- **Where the labels come from, and what has been seen.** `dialog.tlk` 38552–38562 is the damage-**flag** name table, eleven entries in bit order — **Physical** (flags 1|2|4 together: *one* entry for bludgeoning, piercing and slashing), Universal 8, Unstoppable 16, Cold, Light Side, Electrical, Fire, Dark Side, Sonic 1024, Ion 2048, Energy 4096 (`iprp_damagetype.2da` is a *different* table, the item-property one, which names the three physical kinds separately). The weapon rows' `damageflags` column picks the entry.

| row | label | status |
|---|---|---|
| piercing (Vibroblade, flag 2) | Physical | **OBSERVED in K2** |
| energy (flag 4096) | Energy | **OBSERVED in K2** |
| slashing (flag 4) | Physical | sourced from TLK, **not observed** |
| bludgeoning (flag 1) | Physical | sourced from TLK, **not observed** |
| Sonic (1024), Ion (2048) | Sonic, Ion | sourced from TLK, **not observed** |
| Unstoppable (16, disruptors) | Unstoppable | sourced from TLK, **not observed** |

  Observing the unseen rows is on the agenda for when a save holds such a weapon.
- **Balanced** now holds on a second size-2 weapon (observed). **Unobserved on size 4** (and 1); on the agenda. The Lightsaber (size 3) remains the control (no line).
- **`Fully Upgradeable` — CLOSED, it has a source, and it is not a computed line.** It is the **first paragraph of the item's own description** in the installed K2 `dialog.tlk`: strref **127076** reads `Fully Upgradeable\n\nSmall size makes this a good off-hand weapon. Echani vibroblades…`, and the same pattern runs across the K2 weapons (127011–127093: `Fully Upgradeable\n\n…`), with `Not Upgradeable` on others (127098). The shelf's K2 vibroblade (`w_melee_05`) already carries exactly that text and so prints it; K1's copy of the item (`g_w_vbroshort01`, strref 31899) has no such line. **That is why the armours print nothing — their descriptions never carried it — and why no UTI field separates the cases.** Searched: the installed `dialog.tlk` (every string, case-insensitive: "upgradeable", "upgradable", "fully upgrad"), `upgrade.2da`, `upgradetypes.2da`, `baseitems.2da` (no upgrade column), the Linux executable's strings (`UpgradeType`, `UpgradeLevel`, `UpgradeSlot0–5` and GUI control names only — no such phrase). Proven by a byte-for-byte test on the real shelf item (`describe_base_type_test`): K2's captured pane, with the `Balanced` → `Fully Upgradeable` gap of two blank lines and one before the prose.

## Closing suites (final head)

Run one at a time (the first parallel attempts filled `/tmp`; the first full app run on this tree was discarded because files were edited while it ran, and its one real failure — `equip_has_two_states_test`, from the blank-None-pane change — is fixed and guarded).

| suite | head | result |
|---|---|---|
| app (`KOTOR-RPG-APP`) | `66a5fbf` | **2011 passed, 0 failed** |
| Lodestar | `df81340` | **1870 passed, 0 failed** |
| Lens | `2bad745` | **13 passed, 0 failed** |
| Loom | `083e570` | **430 passed, 0 failed** (with the default `TMPDIR`; `the_identity_survives_a_fault_test` fails under a redirected one, as before) |

## Row ledger, at close

**EXCUSED (each names its ruling):** row 1, outer chrome frame — `ASSET-REPLACEMENT-01` / `PT-1309`; row 13, slot grid shape — owner, `PT-2721`; row 14, slot cell size — owner, `PT-2725` DECISION A. **Recorded, covered by the font ruling `PT-2722`:** glyph widths (prose −4.4% against K2's atlas).

**Observations owed from K2 (agenda, none blocks sign-off):** damage labels Physical-for-slashing/bludgeoning, Sonic, Ion, Unstoppable (*sourced from TLK, not observed*); `Balanced` on size 4 and 1; a slot whose list is "None" alone; hover pixel under a real pointer.
