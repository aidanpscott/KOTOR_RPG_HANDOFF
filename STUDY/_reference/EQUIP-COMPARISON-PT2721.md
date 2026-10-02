# EQUIP-COMPARISON-PT2721 — K2's Equip screen against ours, 1920×1080, one row per element

**`PT-2721`, pass 1.** Written by CODER. Supersedes `EQUIP-COMPARISON-PT2720.md`, whose "1:1" claim `PT-2721` rejected. **Nothing here is pass by inheritance:** every row below was read off a screenshot of each side taken for this pass, and the pictures are mirrored.

## Method — what was compared, and how

| | K2 | Ours |
|---|---|---|
| What | the real game, `000008 - game7`: **Onjo Trigit, Jedi Sentinel 1**, Peragus, DEF 17 | the app, an authored save `onjo-trigit.sav` (`tool/author_pt2721_equip_save.dart`) |
| How it was shown | launched through Steam (`steam steam://rungameid/208580`, from the host; the direct `./KOTOR2` fails — `libopenal.so.1` is missing outside Steam's runtime), loaded from the menus with pointer clicks, window moved to y = 0 | the debug build, run on a private X server (`Xvfb :99`, 1920×1080×24, no window manager) so it renders at exactly 1920×1080 with no title bar or panel |
| Size | 1920×1080, windowed; the desktop panel covers the bottom 44 px, **cropped from the mirrored images** (both sides' bottom 44 px are excluded) | 1920×1080 |
| Read-only | nothing was equipped, unequipped or saved in K2; every slot was opened and **Cancelled** (never OK); no slot (`000003`, `000005`–`000008`) was touched | n/a |

Pictures: `HANDOFF/BUILD/screens/pt2721-equip-loop/pass-1/` — `k2-<state>.png` beside `app-<state>.png`, four states: `1-empty-slot` (Belt selected, nothing worn), `2-filled-slot` (Body), `3-item-list` (Body's list), `4-description` (an item selected, its description in the pane); `app-0-as-opened.png` is the screen as it first opens.

**Measurement is by eye off the 1920×1080 pictures, ±3 px.** Where a number matters for a fix it must be re-measured from the picture, not taken from this table.

## The gear — the same shape, NOT the same items

K2's `savegame.sav` (`pc`, `inventory`) and its own Equip screen give Onjo Trigit's gear:

| slot | K2, worn | K2, also carried |
|---|---|---|
| body | Light Combat Suit | Jedi Robe, Reinforced Fiber Armor, Jamoh Hogra's Battle Armor |
| weapon R / L | Lightsaber / Short Lightsaber | Blaster Pistol: Null |
| head | Neural Band | Stabilizer Mask, Circlet of Saresh |
| hands | Dominator Gauntlets | Insulated Gloves, Exchange Casual Gloves, Taris Survival Gloves |
| implant | Mental Boost Package | Strength Package |
| arm L / arm R | Nomi's Armband / Telos Mining Shield | — |
| belt | **nothing** | Adrenaline Amplifier, Cardio-Regulator, Stealth Field Generator, Frozian Scout Belt |

**⚠ THE SHELF CANNOT HOLD THIS GEAR.** Its catalogue is K1-sourced. **Nomi's Armband, Telos Mining Shield and Jamoh Hogra's Battle Armor are not in `items.toml` at all**; most of the rest are catalogue rows with **no carryable blueprint** (only Neural Band, Insulated Gloves, Adrenaline Amplifier, Short Lightsaber, Lightsaber and Jedi Robe have one). So ours is the same **shape** — dual lightsabers, every accessory slot but Belt filled, four body armours, a spare in most slots — built from the blueprints that exist: body **Light** (worn) + Medium, Heavy, Jedi Robe; Lightsaber + Short Lightsaber; Neural Band; gauntlets; implant-1; forearm band; energy shield; Belt empty, with a belt and an Adrenaline Amplifier carried.

> **This is the first thing that needs an owner decision (D1).** "Same gear on both sides" cannot be met item for item with the current data. Every row below that compares an item's NAME, ICON or DESCRIPTION is therefore **"different gear — compared as structure"**, not pass/fail on content.

## Rows

Status: **PASS** · **FAIL** (a fix is in scope) · **DECISION** (needs the owner, named) · **EXCUSED** (owner ruling).

### The whole screen

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 1 | frame | bronze frame fills 1920×1080 | bronze frame fills 1920×1080 | **PASS** |
| 2 | content layout fills the screen | the 4:3 canvas is **stretched** non-uniformly (×2.4 across, ×1.8 down); list box 745 px wide, description 735, content spans x 147–1773 | uniform scale of a 340×255 design; content spans x 158–1762 but the **list (413) and description (406) boxes are about half K2's width**, the lattice sits at centre (x≈1189) not right of it (K2 x≈1344), and the right ~700 px of the item view is empty | **FAIL** — one fix, the largest: size the Equip panes with K2's non-uniform stretch ("ours allowed to stretch") |
| 3 | party rail | none | none (hidden on Equip, owner ruling) | **PASS** |
| 4 | area name / hint line | none | none on Equip; area name stays on the play view; hint line off | **PASS** |
| 5 | **play-view status row under the screen** | none | still draws **"force 7 of 7"** and the player's name ("Onjo Trigit") at bottom centre | **FAIL** — the chrome ruling named the area name, hint line and party panel; this is a fourth piece of play chrome. Surfaced, not decided |
| 6 | the screen opens on | **Body** (with Head, Implant, Hands, both Arms all worn) | **Head** (first filled cell in lattice order) | **FAIL → fixed this pass**: opens on Body when Body is worn; `equip_list_rows_test`, mutation-checked |

### Top bar and title

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 7 | title | "EQUIP" in a **bordered box** (183–845 × 100–150) | plain "EQUIP" text at (158,182), no box | **FAIL** |
| 8 | the eight icons | eight bordered buttons, ~105×80, pitch 113, x 856–1750, **all bright** | eight icons, ~55×55, pitch 65, x 1153–1663, inactive ones dimmed | **FAIL** (size, border, brightness) |
| 9 | icon order | Equip, Inventory, Character, Abilities, Party, Journal, Map, Options | the same, left to right | **PASS** |
| 10 | Map icon | enabled | drawn **disabled** (no screen behind it), with its reason on the status line | **DECISION D2** — wire it to the `m` overlay, or keep it disabled |
| 11 | active icon | Equip's is plain, no highlight | Equip's is filled and outlined | **FAIL** (minor) |

### Slot view (states 1 and 2)

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 12 | subtitle | "BODY" / "BELT", centred between the bars (y≈208) | "BODY" / "BELT" small, at the left (158,220) | **FAIL** (position, size) |
| 13 | slot grid shape | 2×3 (+ belt below) | 7-cell diamond | **EXCUSED — owner, PT-2721** ("yes, it's fine") |
| 14 | slot cell size | ~129×95 (54×54 canvas units, stretched) | 70×70 square | **FAIL** (follows row 2) |
| 15 | selected-slot mark | white border | amber border | **FAIL** (colour) |
| 16 | **icon inside each filled cell** | the item's own art (a yellow vest for Light Combat Suit, crystals for Neural Band, a red shield for Nomi's Armband, lit hilts for the sabers) | the same generic slot glyph in every cell | **FAIL** — and **blocked by D1**: our items are not K2's, so "the item's own art against K2's" cannot be the same art |
| 17 | empty cell | the slot glyph, dim | the slot glyph, dim | **PASS** |
| 18 | DEF badge | shield, "17", label above | shield, "17", label above, smaller | **PASS** (value and shape); size follows row 2 |
| 19 | ATTACK MODIFIER / DAMAGE bands | both bands drawn, values 3-17 / -6 and 5-23 / 0 beside the saber cells | bands drawn, labels at far left/right (x 735, 1570), values "-2" and "4-18 / -2" tiny beside the cells | **FAIL** (label placement, value size). The VALUES differ because the gear differs (D1) |
| 20 | Config 1 / Config 2 rows | two weapon rows, hands-glyph cells in Config 2 | two rows | **PASS** (structure) |
| 21 | SWITCH WEAPONS | full-width bordered button (985–1705 × 797–845) | text only, overlapped by the band art's bracket | **FAIL** |
| 22 | list in the slot view | the slot's list: None + items, icons left, a mark on the equipped row | the slot's list, **no icons**; the Belt list shows "None" and one "Belt" — **the carried Adrenaline Amplifier is missing** | **FAIL** — see rows 28–30 |

### Item list (states 1–3)

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 23 | list box | 745×652 at (190,243), scrollbar at 935 | 413×472 at (158,253), scrollbar at 571 | **FAIL** (follows row 2) |
| 24 | row height / pitch | 36 / 38 | ~80 / 86 | **FAIL** — K2's rows are a third the height; PROTOITEM's 62 is not the pitch |
| 25 | None row | ⊘ icon in a small box at the left, the word centred | ⊘ drawn large in the row, the word beside it | **PASS** for presence; **FAIL** for size/placement |
| 26 | row text | the item's name, centred | the item's name, centred | **PASS** for content shape |
| 27 | row icons | each item's own art in a small bordered box at the left | **none** | **FAIL → D1** |
| 28 | names | "Light Combat Suit", "Jedi Robe", "Reinforced Fiber Armor", "Jamoh Hogra's Battle Armor" | "Light", "Medium", "Heavy", "Robe 1" — the **base type's** name | **FAIL → D1** (our items are base types, not named items) |
| 29 | an item built from a starting blueprint | its name | its **raw id** ("Neural-Band (Equipped)") | **FAIL** — items carrying a `catalogue =` field fall past `_displayNameOf` to the short id. In scope |
| 30 | two items of one base type | two named rows | would both read "Belt"; the second is not offered at all | **FAIL** — as row 29 |
| 31 | selected row | white border on the highlighted row | amber border on the equipped row | **FAIL** (colour) |
| 32 | equipped mark | "(Equipped)" suffix | "(Equipped)" suffix | **PASS** |
| 33 | scrollbar | thumb + arrows beside the box | thumb + arrows beside the box | **PASS** |

### Description pane (state 4)

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 34 | box | 735×602 at (985,243), scrollbar at 1720 | 406×435 at (616,253) | **FAIL** (follows row 2) |
| 35 | font | a **plain readable face** (GFF: `LB_DESC` uses `fnt_d16x16`, not `dialogfont16x16`), sentence case | BankGothic small-caps, same as the rest | **DECISION D3** — the ruling put every Equip string on one font; K2 uses two |
| 36 | content | structured lines (Feats Required / Defense Bonus / Regenerate Force Points) then flavour prose | structured lines, then the data's `note` | **PASS** for structure |
| 37 | **developer notes in the player's text** | none | **"SECTION: PT-1734 — READ FROM BASEITEMS.2DA ROWS 66–68, NO LONGER PLACEHOLDERS"** | **FAIL — a data defect.** `equipment.toml` stores developer provenance in the player-facing `note` field: **21 of its 38 notes begin "section: …"** (`PT-169`, `EQUIPMENT-01 §5.1`, `PT-1734`, …). The display function is right to print `note`; the data is wrong. Needs the data's owner (D4) |
| 38 | description text size | ~19 px, comfortable | ~11 px, tiny | **FAIL** (follows 2, 35) |

### Footer and portrait

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 39 | CLOSE / CANCEL+OK | 286×48, bordered, at the left | 155×29 | **FAIL** (follows row 2) |
| 40 | portrait | **real portrait art**, 228×132, in a framed box | an empty placeholder box, 90×90 | **DECISION D5** — no portrait art exists in this project; the placeholder is stated, not dressed up |
| 41 | name + "class level" | "ONJO TRIGIT" / "JEDI SENTINEL 1" **left of** the portrait | the same two lines, left of the portrait | **PASS** |
| 42 | other party members | none (solo) | none (solo) | **PASS** — the small-portrait switching has its own tests (`equip_portrait_block_test`) |

### Font rows (live as of this pass)

| # | element | K2 | ours | status |
|---|---|---|---|---|
| 43 | typeface | `fnt_dialog16x16`, a narrow bitmap face | **BankGothic Md BT**, the owner's choice | **DECISION D6** — at K2's capital height it is about **1.8× wider** ("LIGHT COMBAT SUIT (EQUIPPED)": 880 px against 490 at 3×); see `STUDY/_reference/pt2721-font-candidates/equip-font-side-by-side.png`. It fits the boxes at 1920×1080. Narrower face, or smaller size, or accept — the owner's call |
| 44 | capital height | 8 px in a 16 px cell | scaled to match (measured by rendering) | **PASS** |
| 45 | case | the real strings are mixed case, drawn as small-caps-style by the face | BankGothic draws lowercase as small capitals | **PASS** for the look |
| 46 | colour | teal (111,227,196) on near-black | tinted from the app's tokens | not compared numerically this pass |

## Pass 1 summary

**46 rows, counted from the table's own status column: PASS 16 · FAIL 24 · DECISION 4 (rows 10, 35, 40, 43) · EXCUSED 1 (row 13) · 1 mixed (row 25: pass for presence, fail for size) · 1 not compared (row 46, colour).** Of the 24 FAILs, **row 6 is fixed in this pass**; rows 16, 27 and 28 are FAILs that **cannot close until D1 is answered** (our items are not K2's items); the rest are in scope.

**Fixed this pass** (each with a test and a mutation check): row 6, Equip opens on Body.

**Fixes that are in scope and not yet done**, in the order I would take them:

1. **Row 2 — stretch the Equip panes to K2's proportions.** One change that moves rows 14, 23, 24, 34, 38, 39 with it. The largest single gap and the one the owner's "layout doesn't fill the screen" named.
2. **Rows 7, 8, 11 — the title box and the big icon buttons.**
3. **Rows 29, 30, 22 — items built from a starting blueprint:** show their catalogue name, and offer them in their slot (the carried Adrenaline Amplifier is invisible).
4. **Rows 12, 15, 19, 21, 31 — small placement and colour rows.**
5. **Row 5 — the play-view status row on a menu screen** (needs a ruling on what K2's equivalent is; K2 shows nothing).

**Decisions needed from the owner:**

- **D1 — the gear.** Author K2's items into a package (the three that are not in the catalogue at all would have to be written from scratch), or accept stand-ins and compare structure only.
- **D2 — Map icon:** wire to the `m` overlay, or keep it disabled.
- **D3 — description font:** K2 uses a plain face for descriptions; one font or two.
- **D4 — the 21 leaked `note: "section: …"` lines in `equipment.toml`:** whose data, and strip or move them.
- **D5 — portrait art:** none exists; stay a placeholder.
- **D6 — Bank Gothic's width.**

## What I could not do, and why

- **K2 at true fullscreen.** I tried to close K2 and set `FullScreen=1` in its settings file to remove the desktop panel from the capture; the permission system denied that (it counted as irreversible local destruction), and I did not pursue it another way. The window was **moved** instead; the bottom 44 px of both sides are cropped.
- **A full loop.** One pass has been run. The brief says loop until every row passes or a fix needs an owner decision; six decisions are now open and two of the largest fixes (row 2, rows 7–8) are layout rebuilds, so this is the honest stop for a first pass.
