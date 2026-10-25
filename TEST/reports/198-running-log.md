# TEST 198 running log (draft, text only)

Started 2026-10-24. Tester, Xvfb :2, own data dir. Batch 4 (letterbox, game over, confirm, terminal) + scrolling Party Selection with lock + TEST 197 fixes.
Known, don't file: '[Cut in]', 'say something…', 'costs a reaction — you have …'; store 'Buying Items', tall rows, taller pane; list-box right-edge gap; combat queue look; no K2 capture of the combat bar.

## Build
- App 78997e6 (origin/in-game-batch-4), git worktree from my own clone at builds/test198 (detached).
- Commits since 47fe0ea: 7dec471, 66d1fd3, d7a1f7a, afd337b, 5c067c7, 78997e6.
- Lock: Lodestar 835084679e6e…, Lens 5fe60a9.
- No installed package carries party.locked/party.unlocked (grep of tester-data packages): package lock likely not reachable.
- Gate: "FOR TESTER — CORE at 78997e6, 5105 tests, 0 failed, 12m58s at -j 3, peak 1897 MB"; "ARCHIVE last green at 78997e6"; SENDABLE, 6 warnings.
- Build through the lock: 10.8 s; pubspec.lock unchanged; compiled Lodestar = pub-cache Lodestar-835084679e6e… = lock.
- Lodestar 8350846 is on origin/main. Shelf a0b9a0d (pulled); check_shelf: 33 rules files, 125 blueprints, identical.

## 4. Store gold wash — PASS
(Brightness had been left at 0.40 since TEST 197: first measure half as bright as K2. settings.json backed up to notes/settings-test197.json and removed, so defaults.) Default brightness, Store Bed Dressa vs K2 03a: stats box ours (35,29,12) / K2 (33,28,12); list background (36,29,12) / (29,25,11); pane (35,29,12) / (43,37,16, K2 pane holds text). Same wash. (store-0.png)
## 5 (part) — conversation
Dressa: 'Dressa: Looking to trade? I have wares, if you have credits.' centred under the red message box at the top, letters whole (TEST 197 clip fixed). Replies bottom-left: '1. Show me what you have.' lit pale, '2. Just looking, thanks.' teal, '3. say something…' (known). Hover on 2 moves the lit row to 2. Digit 1 opened the store. No recognition line shown (none for this speaker?). (talk-0.png, talk-hover2.png)
After the store: '1. [Leave.]' lit, '2. say something…'. Digit 1 pressed [Leave.] (play returns, HUD back). Small finding: digit 2 on the typed-reply row focuses it AND types '2' into it (the row then reads '2. 2'). (talk-after-store.png, talk-digit2.png, talk-digit1.png)

## 3. Lit rows — Inventory PASS except NEW (FINDING)
Inventory (Lang Three, Medium equipped + NEW Vibroblade bought from Dressa): hovering Vibroblade lights nothing and the pane stays 'Defense Bonus: 4'; clicking lights it and the pane follows (Feats Required … Balanced). Text: unselected teal (38,160,135), selected pale (148,153,138). Row frames: Medium pale when selected -> teal (30,121,100) when not. FINDING: the NEW item's row frame is amber (149,122,71) idle but turns PALE (186,187,169) when lit; K2 04a/04c keep the NEW frame amber when lit (Comlink) and only its words go pale. Our NEW words are teal (not amber), as K2's. (inv-0, inv-hover, inv-click)
Equip — PASS: opens on Body (None, Medium (Equipped)); hovering the right-hand weapon slot switches the list to 'Weapon R' (None, Vibroblade) without a click; hovering a list row lights nothing. (equip-0, equip-hover-slot, equip-hover-row)

## 9i. Species spellings — PASS
Lang Three ('twi-lek'), Lang Four ('Twi'lek', specs198/lu198-twi.json), Lang Two ('twi'lek') all load; Character Info Species 'Twi'lek' with the Ryl/Basic/Lekku Languages line on each. (lang3-info, lang4-info, lang2-info)

## 7a. Exit Game confirm — PASS
In-play Options > Exit Game: 'Do you really want to quit?' in K2's box; box, OK (lit) and Cancel match K2 98-exit-confirm in place and size. K2 adds 'Your progress will not be saved.' (ours autosaves). (confirm-exit.png)

## 1. Party Selection, scrolling (Thirty: 30 Vela clones joined, 29 left, + vela.range.01 from the area; specs198/thirty.json) — PASS
K2 list rows: portrait cell + bar; 31 rows; wheel scrolls to the end, scroll bar moves. In-field rows: white frame (first and last rows); others teal. Selected row: name goes pale; hover lights nothing. Header '1 Available Slots' (cap 3 companions). Add on a teal row -> white, '0 Available Slots'. Cancel: party unchanged (2). Add + Escape: unchanged. Add + OK: party of 3 (sidebar). (party-0, party-scrolled, party-hover, party-sel, party-added1, party-cancel-play, party-escape-play, party-ok-play)
## 2b. Full party — PASS with a small finding
With 0 slots, selecting another Vela greys Add and shows 'The party member you have selected is currently unable to join the party.' under Add. Small: a teal frame line runs through the middle of that red line (party-sel2.png; K2 shows no line there).
Small: after OK the board draws the three companions two ways (two 'V' circles, one red party disc) and the bottom right shows two portraits for three companions. (party-ok-play.png)

## 2a. Lock in a fight — PASS (same line-crossing small)
Mid-fight Party Selection: Remove/Add greyed, 'You are unable to change your party at this time.' under it; rows still selectable (browsable); pressing the greyed button changes nothing. The same teal frame line crosses the red line. (lock-party, lock-party-sel, lock-party-add)
9e. Queue text now sits inside the arrow art (fight-queue.png).

## 2c. Downed companion — FINDING
Mid-fight, one Vela down: her card '0 of 40', the message box 'Vela: -2 of 40' (player 'Thirty: -8 of 12'). All three in-field rows (1, 5, last) show 'You are unable to change your party at this time.', none shows the downed reason 'down — not until this fight is over' (play_screen.dart:2702). Likely cause (hypothesis, not proven): _isDown tests the sidebar's current == 0 while vitality runs below zero. (vela-down, down-r1, down-r5, down-rlast, down-sidebar)
Note: End Turn loop: the box alternated 'Vela is waiting on you' and none, consistent with manual Velas' turns.

## 6. Game over — PASS (no K2 still to compare)
Total party defeat in Thirty's fight: K2 frame popup 'Your entire party has been killed.' (red) + explanation; Load Last Saved Game absent and its place reads 'the newest save is this one — it already records the defeat'; Go to Load Game List, Main Menu. No K2 game-over still in k2-capture-run/k2-ingame (MAIN to say if one exists). (gameover.png) Also: the message box at the top lists everyone 'killed' and the line 'YOU FALL AND NOBODY IS LEFT STANDING…' — readable over the dimmed board.

## 8. Terminal — PASS with a small finding
Term Two (Locked and Trapped): right-click the console -> 'Examine (Science) / Slice (Slicing)'; Slice opens the terminal on K2's computer_p frame (blue frame). Transcript 'STRONGROOM CONTROL — AWAITING INSTRUCTION'; options '1 [Slicing] Unseal the vault door. (3 spikes) — you have 0 spikes', '2 [Slicing] Cycle the corridor lights. (1 spike) — you have 0 spikes' (dim, unaffordable); four readouts Slicing 1, Spikes 0, Repair 1, Parts 0. No K2 computer still to compare in pt2752. Small: the play view's red message box ('there is no way there / Term Two') is drawn over the frame's top edge. (term-0.png)
Note: a left click on the console says 'there is no way there' and a bump 'the Security Console is in the way'; only the right-click menu opens it.
Small: Escape on the terminal opens Options over it instead of closing it; the terminal has no visible Leave/Close; a tap anywhere closes it (by design per the code comment, but nothing on screen says so). (term-escape.png)

## 7b. Delete confirm — PASS
Load list > select '33 : del198' > Delete -> 'Are you sure you want to delete the save game?' in K2's box with OK/Cancel at the same size as Exit Game's; OK removes the row. (confirm-delete, after-delete)

## 7c. Reaction prompt — PASS
Bolt Defl (Tester Bolt): Force Deflection defaults to ALWAYS (app_settings.dart:36), so first deflections fired with no prompt. Set to Ask in Gameplay mid-fight; next gunman shot: K2 box 'Force Deflection / Gunman fires at you / 6 Force points · 73 left · spent only if the shot would hit back at Gunman, 95% (needs 2+)' with Yes / No (K2 button size, same as the other confirms). Yes -> fight continues (force unchanged at 73: the shot did not hit, as the line says). Note: buttons read Yes/No, not OK/Cancel. (confirm-reaction, reaction-after)

## 9 (fixes, Bolt Defl fight)
- 9f End Turn clears 'waiting on you': after End Turn on Vela's turn, the box line is empty. PASS.
- 9b Switch Weapons: works ('you switch weapons'); pale pressed frame while the button is held (switch-held.png vs hover). PASS.
- 9h Hover boxes: column 2 'Use the Force (f) …' box fully on screen at the left edge (hover-col-168.png). PASS.
- 9c Doctrine: chooser open, Escape closes the chooser and leaves Party Selection open (doctrine-open, doctrine-esc1). PASS.
- 9g 'A fight begins.' once at the top of Messages > Combat (combat-tab-defl.png). PASS.
- 9a Hide: Watch Four hidden with her action spent: toggle frame pale (held) and icon dim together (hide-state.png; TEST 197 showed only dim). PASS.

## 10a. Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), same walk, 3 Spaces, Messages > Combat: initiative and Rounds 1-3 identical to TEST 185 line for line; 'A fight begins.' once. (dice/combat-tab.png, combat.txt)
- 9d Stale 'V': Icon Nine from reg197 (out of a fight): Remove Vela + OK -> 'V' where she stood; Add + OK -> one party disc beside the player, the 'V' gone. PASS. (v2-0, v2-removed, v2-readded) [Twi Seven's newest save is mid-fight, so the lock refused the remove — correct.]

## 7d. Overwrite confirm — PASS
Save Game > select '33 : reg198' > Save -> 'Are you sure you want to overwrite the save game?' in K2's box, OK/Cancel at K2 size. (confirm-overwrite.png)

## Local bed for 5 (long reply list)
No installed dialogue has more than two replies. Made packages/tester-talk (copy of store-bed, id/name changed) whose merchant greeting has ten replies (one long, wrapping); fixture Talk Eight (specs198/talk.json).

## 10b. Regression (Icon Nine) — PASS
reg197 loaded (start); Save > New Slot 'reg198' (33); overwrite confirmed (22:08:51); F4 from the play view: one quick.mark (22:09:19) [an earlier F4 with Options still open wrote nothing — known behaviour]; Load lists Auto Save, Quick Save, '33 : reg198'; loaded reg198 at the start; a fight to its end: total-defeat popup. (reg/start.png, reg/end.png)
## 6b. Game over with saves — FINDING
Icon Nine had a Quick Save (22:09:19) and '33 : reg198' (22:08:51), both from before the fight, yet the popup still omits Load Last Saved Game and says 'the newest save is this one — it already records the defeat' — the autosave written at the defeat is counted as the last save. So Load Last Saved Game never appears after a defeat while an autosave is written at it. (reg/end.png)
Note: 10 replies refused with the app's own message ('… 9 is the ceiling … no key for a tenth'); bed trimmed to 9.

## 5 (rest) — conversation, Tester Talk / Talk Eight — PASS with smalls
Nine replies + the typed row: the list grows upward from the bottom bar, the long reply wraps with a hanging indent under its text, nothing clipped (talk-long.png). Line at top: 'Dressa: Looking to trade? …' centred. Typed reply 'do you buy' + Enter -> recognition line under the line: 'nothing here means that'; 'do you buy as well as sell' + Enter -> 'that is: Do you buy as well as sell?' and reply 4 lights (talk-recog, talk-recog2). Small: with nine replies the typed row is numbered '10.', which no single digit can reach. Reactions at the bar's right not reached (no fight/interrupt in a conversation here).
