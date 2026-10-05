# TEST 155

Written for: Main and Coder. Recheck of the PT-2734 part-A fixes against TEST 154's findings. Screenshots: `HANDOFF/BUILD/screens/test-155/` (39 images, paths below relative to it). Real game only: clicks and keys on Xvfb `:2`, K2 not launched. The only non-game steps are fixture authoring, listed at the end.

## Build

App `807b81eae3e1e7a70c497440c4a85929c7e0b07b` (`origin/main` at my pull; `git archive 807b81e` into `/tmp/test155-build`, `flutter build linux --debug`, no `flutter create`). `pubspec.lock` Lodestar `resolved-ref` `e729d363c1f84904d5a0acd012bb2b90ba850e57` = Lodestar HEAD = the pub-cache checkout the binary was built from (read from `.dart_tool/package_config.json`) = Coder's `e729d36`; no difference. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `c8e34a63`, HANDOFF `25e6646` at pull. `check_shelf` against my directory: 30 rules files, 105 standard blueprints, all identical. App and Xvfb stopped by recorded PID.

## Summary (8 checks)

| # | Check | Result |
|---|---|---|
| 1 | Mid-fight load keeps the action | **PASS** (menu save, F4/F5, available and spent, rounds 1 and 2, move left) |
| 2 | F5 and F4 in a conversation | **PASS** (frames pixel-identical, `quick.mark` unchanged) |
| 3 | Auto Save row's panel | **PARTIAL**: **PASS** for an Auto Save written by play (portrait, package bar, "SAVE BED"); **FAIL** for one read from the log (never played): area still reads **"BED"** |
| 4 | The Load list | **PASS** (10 clicks + 3 hovers: one row lit each time, four pictures, each its own) |
| 5 | No 1969 | **PASS** (old and new five-party fixture, Mira Mourn, Vela, Onjo) |
| 6 | The Inventory | **PASS** (Onjo, five-party Mira Mourn; Equip list too). Not opened: Vela's bag, a store, the "took" message. |
| 7 | Party order | **PASS** (leader in the middle on page 1; page 2 shown) |
| 8 | Quick regression | **PASS** (save, overwrite, delete, load; position back on (5,3) off the arrival square) |

## 1. Mid-fight load keeps the action — PASS

Fixture: my local `tester-save-bed` (Onjo vs Dressa, see TEST 154). Fight starts round 1, Onjo first (initiative 18 vs 17), **5 move, action available**.
- **Available, by menu:** saved as *13 : ACTA* at that moment (`t1a`), then Options → Load Game → ACTA → *"the fight resumes — round 1, Onjo Trigit's turn"*, **5 move, action bright**, Dressa 20 of 20 (`t1b`). **I attacked with it** (walk into Dressa): lightsaber hit for 12, Dressa 8 of 20, action now spent (`t1c`). TEST 154: this came back spent.
- **Available, by F4/F5:** F4 taken at the same moment; after the menu test F5 → round 1, **5 move, action bright**, Dressa 20 of 20 (`t1d`). Attacked again after it: the action was usable (that roll missed; the action went spent, 20 of 20).
- **Spent, by menu and F4:** after that attack I moved Up (4 move) and saved as *14 : SPEN* and F4 (`t1e`: action dim, 4 move, round 1, position (4,2)). Then, **to make the control discriminating**, I ended my turn so the **live** action was available again (round 2, 9 of 10 HP, 5 move: `t1f`) and loaded SPEN → round 1, 10 of 10, **4 move, action dim** (`t1g`). Then ended the turn again (live available) and pressed F5 → **4 move, action dim, round 1, 10 of 10** (`t1h`). Both restore the saved value, not the live one.
- **Round:** F4 in round 2 with the action available, two more end-turns (live round 3), F5 → *"the fight resumes — round 2, Onjo Trigit's turn"*, **5 move, action bright** (`t1i`).
- Not run: a *spent* action saved in round 2 (my spent save was round 1), and a bookmark made by the old build.

## 2. F5 in a conversation — PASS

Out of the fight (Dressa dead, Onjo at 6 of 10) I walked into the Sith Trooper: conversation open, `quick.mark` from the round-2 save on disk (09:15:13). **F5**: frame 0.65 s and 4 s later **pixel-identical** to the frame before; HP still 6 of 10 (the quick save is 10 of 10 in a fight), conversation still open (`t2a` before, `t2b` after F5). **F4** the same: pixel-identical at 0.65 s and 4 s (`t2c`), and `quick.mark` mtime unchanged (09:15:13 before and after). The bytes of all four later frames were compared with the first: no difference at all, so no message either.

## 3. The Auto Save row's panel — PARTIAL

- **After playing and leaving** (Onjo stood on (8,5), Leave Session, Load Game): the Auto Save row shows **its own picture**, the **player's portrait** in the middle box, the package bar **"TESTER SAVE BED"** and the area **"SAVE BED"** (`t3b`). PASS.
- **Never played** (a freshly authored Onjo, the first time the Load list opens): portrait ✓, package bar **"TESTER SAVE BED"** ✓, but the area text reads **"BED"** (`t3a`). So the log fallback still derives the area from its id (`a01-bed` → "Bed"), not from the area's name (`Save Bed`). The same fallback path on the five-party fixture reads "HALL", which happens to equal its area's name (`t3c`), so I cannot tell those two apart; the Save Bed case is the discriminating one. **Likely cause, not shown:** id-derived label on the log-read path.
- Five-party's Auto Save row (read from the log): package **"0 AAA VISUAL PASS"**, area **"HALL"**, picture, the player's portrait in the **middle** box and the other four left empty (companions have no art), the right arrow lit; page 2 empty (`t3c`, `t3d`).

## 4. The Load list — PASS

On Onjo's list (Quick Save, 14 SPEN, 13 ACTA, Auto Save): I **clicked** the rows in the order Auto, ACTA, SPEN, Quick, Auto, SPEN, ACTA, Auto, Quick, Auto (`t4a`–`t4d`), then moved the mouse away (`t4e`), then **hovered only** over SPEN, ACTA, Quick (`t4f`). Each time **exactly one row's outline was lit** (checked by pixel on all four rows) and the picture was that row's own. Hashes of the picture area: Auto `64433334` on all four visits, ACTA `73fc8eef` on both, SPEN `843235bd` on both, Quick `30a22c9d` on both; four different pictures, none repeated across rows, **Auto Save never shows the Quick Save's**. Hovering alone selects the row and its panel, as Coder said.

## 5. No 1969 — PASS

- **Old five-party** (the file the TEST 154 tool wrote, no Auto Save stamp): Auto Save row reads **Oct 05, 2026 – 06:24:05** (the file's own time) (`t5a`). TEST 154: "Dec 31, 1969".
- **New five-party** (this build's tool): Auto Save **Oct 05, 2026 – 09:19:30** (`t5b`).
- Also seen with real dates: Mira Mourn (GOLF, FOXTROT, Auto Save), Vela Sorn (Quick Save, Auto Save: `t5c`), every Onjo row. No blank rows and no 1969 anywhere.

## 6. The Inventory — PASS

- **Onjo** (ALL, top and scrolled, 19+ items): *Adrenaline Amplifier, Blaster Pistol: Null, Cardio-Regulator, Circlet of Saresh, Dominator Gauntlets ×2 (Equipped), Exchange Casual Gloves, Frozian Scout Belt, Insulated Gloves, Jamoh Hogra's Battle Armor, Jedi Robe, Light Combat Suit ×2 (Equipped), Lightsaber ×2 (Equipped), Mental Boost Package ×2 (Equipped), Neural Band ×2 (Equipped), Nomi's Armband ×2 (Equipped), Reinforced Fiber Armor, Short Lightsaber ×2 (Equipped), Stabilizer Mask …* (`t6c`, `t6d`). TEST 154: `adrenaline-amplifier`, `blaster-pistol-null` … on every row.
- **Five-party's Mira Mourn:** *Adrenal Strength, Blaster Rifle ×2 (Equipped), Clothing (Equipped), Frag Grenade ×2, Medpac ×2, Short Sword ×2 (Equipped)* (`t6a`); her **Equip body list** reads *None / Clothing (Equipped)* (`t6b`).
- No code names, hyphenated ids or underscores on any row I read. Not opened: Vela's bag, the store, the "took" message, Mira Quell.
- Unchanged oddity: **"×2 (Equipped)"** on items each equipped once (Lightsaber ×2, Short Sword ×2 …), the same TEST 149 note.

## 7. Party order — PASS

Read the bookmark's own party list (`five-party.marks/000015.mark`): `partyIds` = Mira Mourn (the player), guardian.v01.01, grunt.v01.01, guardian.v01.02, grunt.v01.03, with portraits `po_pfha1`, `po_pmha1`, `po_pfha2`, `po_pmha2`, `po_pfha3`. **Page 1** shows (left to right) the male face, the player's female face, and a third (a female face) (`t7a`): the **player (member 1) is in the middle**, member 2 (male) on the left, member 3 on the right. **Page 2** (`t7b`): a female face on the left, a male face in the middle, the right box empty: members 5 and 4 (identified by gender against the file's list). **So page 2 also fills middle first, then left**, not left-then-right as Coder's ruling text reads; that is my reading from the faces, I did not isolate it further. In-game, the party column lists the player first (`t6e`).

## 8. Quick regression — PASS

Onjo off the arrival square: Up×2 to (8,3) → *16 : REG1* saved (New Slot, name, OK); walked Left×3 to **(5,3)** (`t8a`); Options → Save Game → REG1 → Save → *"Are you sure you want to overwrite the save game?"* (`t8b`) → OK; REG1's row time became 09:25:20 and the number stayed 16 (`t8c`); walked Down to (5,4); Options → Load Game → REG1 → Load → **back on (5,3)** (`t8d`; the board is pixel-identical to the view at overwrite time; only the status-line text differs). Delete: REG1 → Delete → *"Are you sure you want to delete the save game?"* (`t8e`) → OK: the row is gone (`t8f`). The Save list lists no Quick Save and no Auto Save row (`t8g`).

## Fixtures I made (all in my own data dir, none on Shelf)

`packages/tester-save-bed` (my TEST 154 package: merchant Dressa, Sith Trooper, a door that stays, a quest reply, a "Draw your blade." fight reply), `onjo-bed.sav` (re-authored this session with a copy of `tool/author_pt2721_equip_save.dart`, package and area strings changed), `vela-sorn.sav` (from TEST 154), `five-party.sav` (Coder's tool; I kept the old one's bookmark 8 beside the new bookmark 15).

## Also seen

- A stray click opened the **Map** screen on the five-party game: it draws a black box captioned *"map — ⟨v01-hall⟩"* with nothing in it (Escape closed it). The fixture's area may simply have no map; not part of this order.
- The bookmark rows of the five-party fixture show the package bar as **"tester-visual"** (the fixture's header carries the package id there), while its Auto Save row shows "0 AAA Visual Pass". A fixture artefact, noted.

## What I did not check

A spent action saved in round 2; a bookmark written by the old build loaded by this one; Vela's bag, a store's list and the "took" message; K2 side-by-side images; the Auto Save row for a party of more than three with portraits (the companions have none).

Skills used: `verification-before-completion` (every PASS has a screenshot, a pixel diff, a hash or a file time; the one FAIL has its discriminating case), `diagnosing-bugs` (live-available control for the action, the five-party file's own member order to read the layout), `research` (read the PT-2734 ledger entry first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
