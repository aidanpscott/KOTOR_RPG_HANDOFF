# K2-PARITY-ABILITIES-PT2747 — K2's Abilities screen against ours, first pass

**`PT-2747`.** Each part of K2's Abilities screen, K2 against ours, with the cause of every difference.
**K2 side:** `abilities_p.gui` (`data/gui/k2/`, read with `gfffull.py`). Live captures at 1920×1080 of save `000008 - game7` (read-only; never saved): Onjo Trigit, Jedi Sentinel 1, no powers known. Private: `media/screens/pt2747-abilities/k2-*.png`.
**Our side:** the release app on the same 1920×1080, with Onjo Trigit (Jedi Sentinel 6, `tool/author_pt2747_abilities_save.dart`). Private: `ours-*.png`, `side-by-side-{skills,powers,feats}.png` (K2 left, ours right, full size) and `pt2747-abilities-signoff.mp4`.

**Classes:** **=** matches. **(a)** authored, ruling cited. **(b)** unintended, fixed at the cause with a test. **(c)** to confirm: K2's side cannot be seen on this save.

---

## 1 · Frame and tabs

| # | Part | K2 | Ours | Class |
|---|---|---|---|---|
| 1 | Frame, title "Abilities", the eight menu icons | K2's chrome | the shared K2 frame (Inventory's) | = |
| 2 | Tabs | Filter (lit) · Skills · Powers · Feats | same words, same lit Filter | = |
| 3 | Close | bottom left, "Close" | same | = |
| 4 | Portrait footer | portrait, name, class and level | same; a companion's portrait switches the screen to that companion | = |
| 5 | First-open help box per tab | K2's help text, OK | K2's text (`help_boxes.dart`), OK, Enter and Escape (PT-2743, TEST 172) | = |

## 2 · The list (`LB_ABILITY` 78,134 318×364)

| # | Part | K2 | Ours | Class |
|---|---|---|---|---|
| 6 | Skill row pitch at 1080 | 43.3 px (the PROTOITEM's 36 units drawn at 1.2×) | 43.3 px | **= after fix (b)**: was 36.5 |
| 7 | Power and feat grid pitch at 1080 | 46.2 px | 46.2 px | **= after fix (b)** |
| 8 | Icon cell | 41 px, rounded | 41 px, rounded | **= after fix (b)**: was 34 |
| 9 | Row line, normal | teal 0x1A6E5B on near-black | same | **= after fix (b)**: was Inventory's bronze |
| 10 | Row line, selected (bar and cell) | bone 0x8C9384, lighter fill | same | **= after fix (b)**: was teal |
| 11 | Unknown power cell | `ip_secret`, the glowing teal "?" (named by K2's binary; no .gui names it) | not drawn: unknown powers are not listed (row 17). The art is `ip_secret` (was `lbl_iquest`, the journal's quest book) wherever an unknown row is still handed to the screen | **(a)** |
| 12 | List scroll bar | the thin teal bar with K2's arrows | same; the arrows scroll | = |
| 13 | Skills listed | K2's 8 | our 26 (`SKILLS-01`) | **(a)** our skill list |
| 14 | Skill icons | every K2 skill has one | 6 of 26 by exact name; the rest draw K2's empty slot (owner ruling 3) | **(a)** |
| 15 | Feats listed | the held feats only, one to a line | **the held feats only** (owner, 2026-10-12), each chain's held tiers on one line in order (Two-Weapon Fighting → Improved → Master) | **(a)** chain lines; the earlier "held first, then the rest unavailable" ruling is replaced |
| 16 | Precognition, Battle Precognition | shown when held | only when held | = |
| 17 | Powers listed | unknown powers as "?" cells, in chain lines | **the known powers only** (owner, 2026-10-12, replacing PT-1250's "present and anonymous"), Light, Universal, Dark, each chain's known tiers on one line; a power two paths share is drawn once | **(a)** |
| 18 | Power icons | K2's own | 106 of 106: the games' own; 7 from the Full Force Mod where it has one (owner ruling); 13 approved stand-ins | **(a)** |
| 19 | **A known power's cell** | not visible on this save (no power known) | the power's icon in a bone-or-teal cell | **(c) to confirm on the Telos save** |
| 20 | **A live chain arrow** (between two known tiers) | not visible on this save | `uibit_abi_arrow` between cells (K2's own art, named for this screen) | **(c) to confirm on the Telos save** |

## 3 · The right-hand column

| # | Part | K2 | Ours | Class |
|---|---|---|---|---|
| 21 | Name box (`LBL_NAME` 410,134 300×42) | the name, centred | same; a power adds "Dark · Tier 2" under it | = ; tier line **(a)** |
| 22 | Unknown power | "Unknown Force Power"; "Some Force Powers cannot be learned through normal means..." | the same two lines (`dialog.tlk`) | = |
| 23 | Description pane (`LB_DESC` 410,183 313×221; Feats 287) | its own scroll bar (707,183, 16 wide) | its own scroll bar; the arrows scroll it | **= after fix (b)**: had none |
| 24 | Skill pane | "Related Attribute: X", blank line, description | same | = |
| 25 | Power pane | "Prerequisites:", the list, description | same, then the ceiling line ("Each use lowers your Force ceiling by N.") | = ; ceiling line **(a)** |
| 26 | Feat pane | "Prerequisites:", the list, description | same, then the effect | = ; effect **(a)** (description then effect, TEST 172) |
| 27 | Dominate Mind | — | marked "Conversation power" | **(a)** |
| 28 | Skills readout | Skill Rank · Bonus (amber) · Total Rank | same | = |
| 29 | Powers readout | Base Cost · Adjustment · Cost Per Use ("--" when unknown) | same; the numbers are the Force Cost Table's at the character's step | = |
| 30 | Feats | no readout; the pane runs to 287 | same | = |

## 4 · Proof

- `test/abilities_k2_test.dart`: coverage (every skill, feat and power reached on the real screen and read); render at 1920×1080, 1280×720 and 800×600; real play (each tab, list scroll, Close, no key reaches the map); a companion's portrait; costs; **K2's rows** (43.3 and 46.2 pitch, teal and bone lines); **the description pane's own bar**.
- `test/the_abilities_screen_test.dart` (12), `powers_reach_the_abilities_screen_test.dart`, the frame guard and build_talk on every frame.
- Mutations killed: unknown powers listed again; unheld feats listed again; every feat on its own line; pitch back to 36.5; one pitch for every tab; the selected and normal lines swapped; the pane's bar removed. A reset-to-top on a new pick was built, could not be told apart from the clamp that already does it, and was removed rather than kept untested.
