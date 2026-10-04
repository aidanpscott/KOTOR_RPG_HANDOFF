# K2-PARITY-SAVELOAD-PT2729 — K2's Save/Load screens against ours

**PT-2729 / PT-2732.** Element by element, K2 (`saveload_p.gui`, `savename_p.gui`, captures in `HANDOFF/BUILD/screens/pt2729-saveload/k2/`) against our live app (side-by-sides in `.../sbs/`, our shots in `.../live/`, K2 on the left, ours on the right, K2 cropped of its 28px title bar).
**Status:** `=` matches · `X` excused (ruled or structural) · `GAP` known, listed for a later slice.

## 1 · Screens

| # | Element | K2 | Ours | Status |
|---|---|---|---|---|
| 1 | Title bar "Save Game" / "Load Game" | full-width bar, Orbitron | same bar and text | = |
| 2 | Row list (340 wide, scroll bar, 2px green rows, selected = white border) | newest first, Auto Save last | same order; rows `N : NAME` + date | = |
| 3 | Row text: `[Modded]` tag | printed by K2 itself | never printed (no mod concept) | X |
| 4 | New Slot row (Save only) | top row, StrRef 1590 | same | = |
| 5 | Detail pane: picture, name bar, area bar, class line, Time `0H 9M`, three portrait frames (square 2px) | as shown | same fields; Time from `session.played` | = |
| 6 | Picture of the save | per-area load art K2 renders | the play view captured at save; Auto Save: view when play was left, else latest bookmark's, else default art | X (we have no per-area art) |
| 7 | Buttons Cancel / Save (or Load) / Delete / Switch Characters | four bottom buttons | same; Delete disabled on New Slot | = |
| 8 | Naming popup (savename_p): title, edit box with caret, OK, Cancel | as shown | same (double border, rounded box fixed live) | = |
| 9 | Overwrite prompt (StrRef 1591) OK / Cancel | message box | same text and buttons | = |
| 10 | Delete prompt (StrRef 1592) | message box | same | = |
| 11 | Saving screen (quick save / save): load art, KOTOR2 logo, "Saving" label (StrRef 42528), progress bar, tip | as shown | same layout; art is K2's default load art (ruling: accepted, no per-area art) | X |
| 12 | Quick Save F4 / Quick Load F5; F5 with none says so | box with OK | same | = |
| 13 | F4 in a conversation | nothing, no box | nothing, no box; Options cannot be opened there | = |
| 14 | Auto Save row | last row, StrRef 1593 | present, with a picture (chain above) | = |
| 15 | Window frame (PT-1309 border) | K2 ornate frame | our frame | X |
| 16 | Orbitron glyph widths | K2 renders its own face | same face, ±1px | X |
| 17 | Cloud Save tick | present | none (no cloud) | X |
| 18 | Autosave tick | present | none; ours writes continuously, K2 throttles | X |
| 19 | Quick Save row appears in both lists | Load only | both lists | GAP |
| 20 | Options screen (doorway to Save/Load) | optionsingame/optionsmain | old layout | GAP — next slice, 1:1 |
| 21 | Auto Save pane fields | name/area/time only | same (no class/level, as K2) | = |

## 2 · Model (what a save is)

The character log stays one append-only `.sav`. A bookmark is a sidecar `<character>.marks/NNNNNN.mark` (global slot number, first = 2; Quick Save = `quick.mark`; Auto Save picture = `autosave.png`) with the row fields, a compressed PNG picture and, mid-fight, a gzip'd JSON combat snapshot. Loading writes `character.rewound {to}`; replay is `effectiveLog` (a tree walk), so branches are safe. Proofs: `bookmark_branching_reaches_the_app_test`, `bookmarks_through_the_app_test`, `combat_bookmark_resumes_the_fight_test`, `quick_save_test`, `in_game_save_and_load_test`, `save_load_screen_test`.

## 3 · Size report

Measured in the live app (Xvfb, a real play session on one character, seven saves):

| Item | Bytes |
|---|---|
| One bookmark, real board picture | 12,164 – 12,243 |
| Quick Save (picture + combat snapshot) | 14,429 |
| Bookmark in the test layout | 21,841 |
| Budget per bookmark (writer-refuses, in-game assertion) | 65,536 |
| Character log after the whole session (7 saves, ~10 min) | 1,056 |

- **Growth per hour of play:** the log is event-driven — walking writes nothing, a bookmark writes one `character.rewound` on load and one `session.played` per save. The measured session grew the log by well under 1 KB; the log is ~1 KB per save-and-load cycle of events, not per hour. For a heavy hour (about 200 recorded events) at the PT-1328 rate (120,000 events → 0.34 MB compressed, ~3 bytes/event) that is under 1 KB. Assumption stated: little real content exists yet, so this is a floor, not a long-run measurement.
- **100 saves:** 100 × ~12–22 KB ≈ 1.2–2.2 MB, plus the log once. Bookmarks never copy the log.
- **Compaction:** not proposed. Bookmarks are bounded (65,536 each, writer-enforced); the log grows with events only. Revisit if a real hour exceeds ~100 KB.

## 4 · Known gaps for "Save/Load ready"

Options screen still the old layout (next slice); Quick Save listed in both lists. Remaining flaky: `whole_loop_test` in full runs.
