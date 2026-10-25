# TEST 198: batch 4, the scrolling Party Selection with its lock, and the TEST 197 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-198/` (MAIN_WORK `e025222c`). The step-by-step log is `TEST/reports/198-running-log.md`. Compared against `MAIN_WORK/media/study/pt2752/k2-capture-run/` and `k2-ingame/`.

## Build

App `78997e6` (origin/in-game-batch-4), a git worktree beside my own clone. `gate.py --at 78997e6`: "FOR TESTER — CORE at 78997e6, 5105 tests, 0 failed"; ARCHIVE last green at 78997e6. Lodestar `8350846` = lock = compiled (on origin/main). Lens `5fe60a9`. Shelf `a0b9a0d`; check_shelf clean (33 rules files, 125 blueprints). The build (10.8 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Fixtures (`notes/fixtures/specs198/`):
- **Thirty**: 30 Vela clones joined and 29 left, plus the area's own Vela, which makes a 31-row roster and a full party after one Add.
- **Lang Four**: species written "Twi'lek".
- **Talk Eight**: in a local bed, `tester-talk`, a copy of Store Bed whose greeting has nine replies. Ten replies are refused by the app's own nine-reply ceiling.

Note: I had left Brightness at 0.40 since TEST 197, which halved my first store measurement. I backed up settings.json, reset it to the defaults, and measured again.

## Summary: most pass; three findings

| # | Check | Result |
|---|---|---|
| 1 | Party Selection list | **PASS**: K2's list rows with a portrait cell and a bar. With 31 rows the wheel scrolls and the bar moves. In-field rows are white and the rest teal. A row lights on selection only, never on hover. Add then Cancel, or Add then Escape, leaves the party unchanged. Add then OK applies |
| 2 | Party lock | **PASS** for the fight lock: Add and Remove are greyed, "You are unable to change your party at this time." is under them, and rows stay browsable. **PASS** for a full party: "The party member you have selected is currently unable to join the party." **FINDING**: a downed companion shows the lock line, not its own reason (below). The package lock wasn't reached: no installed bed writes `party.locked` |
| 3 | Lit rows | Inventory **PASS**: hover lights nothing; a click lights the row and the pane follows. Equip **PASS**: hovering the weapon slot switches the list to Weapon R; hovering a row lights nothing. **FINDING**: a lit NEW row loses its amber frame (below) |
| 4 | Store wash | **PASS** at default brightness: stats box (35,29,12) against K2's (33,28,12); list background (36,29,12) against (29,25,11) |
| 5 | Letterbox | **PASS**: "Dressa: …" centred in the top bar, whole (TEST 197's clipping fixed). Replies are numbered in the bottom bar; the lit one is pale and the pointer moves it. Digit 1 opens the store and, after it, presses "[Leave.]". Nine replies grow upward; the long one wraps with a hanging indent and nothing is clipped. The recognition line sits under the line ("that is: Do you buy as well as sell?", or "nothing here means that"). The reactions at the bar's right weren't reached |
| 6 | Game over | **PASS** for the case with no save: K2's popup; Load Last Saved Game is absent and its place reads "the newest save is this one — it already records the defeat". **FINDING** for the case with saves (below). No K2 game-over still exists to compare |
| 7 | Confirm boxes | **PASS**: Exit Game ("Do you really want to quit?"), overwrite, delete, and the Force Deflection reaction prompt are all K2's box, with buttons at K2's size, matching K2's 98-exit-confirm. The reaction prompt's buttons read Yes and No |
| 8 | Terminal | **PASS**: right-click > Slice opens it on K2's `computer_p` frame, with the transcript, the dimmed unaffordable options, and four readouts (Slicing 1, Spikes 0, Repair 1, Parts 0) |
| 9 | TEST 197 fixes | **All PASS**: Hide shows held (pale frame) and dim together; Switch Weapons shows its pale pressed frame while held; Escape closes the Doctrine chooser first; no stale "V" after a remove and re-add (Icon Nine, out of a fight); the queue's text sits inside its arrow; End Turn clears "waiting on you"; "A fight begins." appears once; column 2's hover box is on screen; "twi-lek", "twi'lek" and "Twi'lek" all load as Twi'lek with Languages |
| 10 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185 line for line. Regression: Save (slot 33, "reg198"), overwrite, F4 from the play view (one quick save), Load, and a fight to its end |

## Findings, most important first

1. **A downed companion shows the lock line, not its own reason.** Thirty's fight left one Vela down: her card reads "0 of 40" and the message box "Vela: -2 of 40". All three in-field rows showed "You are unable to change your party at this time.", and none showed "down — not until this fight is over" (`play_screen.dart:2702`). This is a hypothesis, not proven: `_isDown` tests the sidebar's `current == 0`, while vitality goes below zero.
2. **After a defeat, Load Last Saved Game never appears while the defeat writes an autosave.** Icon Nine had a Quick Save (22:09:19) and "33 : reg198" (22:08:51), both from before the fight. The popup still omitted the button and said "the newest save is this one — it already records the defeat".
3. **A lit NEW row loses its amber frame.** The bought Vibroblade's frame is amber (149,122,71) when unlit and turns pale (186,187,169) when lit. K2's 04a/04c keep the NEW frame amber when lit (the Comlink); only the words go pale.

## Small

- A teal frame line runs through the middle of the red reason line under Add/Remove (both the lock line and the full-party line). K2 has no line there.
- In a conversation, the digit for the typed-reply row both focuses it and types itself into it ("2. 2"). With nine replies the typed row is numbered "10.", which no single digit reaches.
- The terminal: Escape opens Options over it instead of closing it, and it has no visible Leave (a tap anywhere closes it, by design per the code, but nothing on screen says so). The play view's red message box is drawn over the frame's top edge.
- A left click on a console says "there is no way there", and a bump says "the Security Console is in the way". Only the right-click menu opens it.
- Force Deflection defaults to Always, so the reaction prompt appears only after setting it to Ask.
- After an Add with OK, Thirty's companions draw two ways on the board (letter circles and a party disc), and the bottom right shows two portraits for three companions.

Known and not filed: "[Cut in]", "say something…", "costs a reaction — you have …"; the store's "Buying Items", tall rows and taller pane; the list boxes' right-edge gap; the combat queue's look; no K2 capture of the combat bar.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
