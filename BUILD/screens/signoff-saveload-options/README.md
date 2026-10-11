# Sign-off video: Save/Load and Options, re-recorded (signoff-1 on 9a1919f; signoff-2 at the hash in its commit)

Two MP4s, H.264, 1920x596. K2 still LEFT, our live footage RIGHT, caption bar on top; "K2: none captured" where no K2 still exists. K2 side is a still. Recorded on a throwaway data folder, no new code during recording.

## signoff-1-save-load.mp4 (7:04), re-recorded 2026-10-11 on app 9a1919f
Debug build of 9a1919f (clean tree, built 07:11), throwaway data folder, Xvfb 1920x1080 at 30 fps. Three new segments (marked NEW) added to the old ones; every old segment re-recorded on this build.
| Start | Clip | Look at |
|---|---|---|
| 0:00 | SL1 | Main-menu Load list: **Auto Save pinned first**, Switch Characters through Kaeda Vos, Kaeda Vos, Onjo Trigit, [Modded] Dax Orlo. |
| 0:25 | NEW: Auto Save pinned | In-game Load list, Switch through all four characters: Auto Save is the first row in each (owner ruling; K2 lists it last, still on the left). |
| 0:55 | NEW: two of one name | Two characters named Kaeda Vos. Main-menu Load, open the first: in-game Load lists only "a mark of my own". Leave, Switch, open the second: only "her own mark". |
| 1:52 | SL2 | Continue, in-game Options with the party footer. |
| 2:11 | SL3 | Save Game > New Slot > "spare" > OK: the Saving picture, then back to Options. |
| 2:30 | SL4 | Overwrite prompt: Cancel, then OK (the row's time changes). Delete prompt: Cancel, then OK (the row goes). |
| 3:22 | SL5 | Clicking rows: picture, place, time, party. |
| 3:39 | SL6 | F4 quick save, walk 3 squares, F5 back to the saved square. |
| 3:54 | SL7 | Load list: Auto Save first, then the rest newest first. |
| 4:09 | SL8 | Five-member party in the Load pane, arrows page 3 + 2. |
| 4:27 | SL9 | Mid-fight save "mid-fight" (round 1, Onjo's turn, 5 moves, action ready). |
| 4:50 | SL10 | Play on (5 turns pass, Onjo attacks so the action is spent), load "mid-fight": "the fight resumes, round 1, Onjo Trigit's turn", 5 moves, action back. |
| 6:14 | SL10b | Walk 3 squares mid-fight (2 moves left), load: square, turn and 5 moves come back. |
| 6:40 | NEW: leave mid-fight | Move 1 square (4 moves left), Exit Game > OK mid-fight, Continue: "the fight resumes, round 1, Onjo Trigit's turn", same square, 4 moves. |

Seen while recording, not fixed here (PT-2739 item 5, the Loading picture should cover the whole load). Counted frame by frame in the 30 fps recording: every load shows the Loading picture briefly, then **an empty play screen (frame and sidebar, no board)** before the board appears.

| Load | Loading picture | Empty play screen |
|---|---|---|
| SL10, load "mid-fight" | 8 frames (0.27 s) | 23 frames (0.77 s) |
| SL10b, load "mid-fight" | 7 frames (0.23 s) | 26 frames (0.87 s) |
| NEW leave mid-fight, Continue | 9 frames (0.30 s) | 27 frames (0.90 s) |

K2 has no stills for SL8-SL10b and the new mid-fight segment ("K2: none captured").

## signoff-2-options-combat.mp4 (2:48)
| Start | Clip | Look at |
|---|---|---|
| 0:00 | OP1 | Exit Game: Cancel, then OK to the main menu. |
| 0:16 | OP2 | Brightness at min, 25%, default, 75%, max: K2 left, ours right (3.5 s each; numbers in `brightness/README.md`). |
| 0:33 | OP3 | In-game Options: hover help, Feedback ticks. |
| 1:21 | OP4 | Combat at 30 fps: Onjo Proof (103 HP) vs the trooper. The trooper fell in round 1, so this clip has few exchanges. |
| 2:28 | OP5 | Hit feedback at 60 fps (proof take A, 22 turns). |

## Hit feedback at 60 fps (PT-2736 item 3), build a845f96
`hit-feedback-60fps/`: two recordings, the analysis scripts and tables (`table-take-a.txt`). Take A: 22 turns, **11 hits, 11 misses**, per-frame detection of HP text change, red edge glow and the number/"miss" over the token:
- **Flash:** on the same frame as the HP change in 10 of 11 hits (+0 frames); the 11th (turn 2) the detector saw the HP change 34 frames after the log line and no flash: not explained, listed as a failure.
- **Number:** detected on the same frame in 9 of 11 hits; turn 22's number detected 19 frames late; turn 2 not detected. Crops of hits (`stills/proof-60fps-number-crops.png`) show "-2" and "-11" present.
- **Miss:** "miss" detected on the same frame in 9 of 11 misses; turns 19 and 21 were not caught by the detector but the crops show "miss" (`proof-60fps-miss-and-hit-crops.png`).
The detector is a pixel heuristic I tuned during the run (windows moved twice), so these counts are indicative, not a clean pass. The flash is brighter and longer than K2's (not tuned against K2's peak here). Take B (9 turns) had only 1 hit. The earlier fault (the number appearing one app frame after the HP) was fixed in a845f96 and is covered by a unit test.

## NOT done / owed
- **Medpac heal and XP-on-kill pop-up in our footage: not shown.** Treat is ally-only and the sign-off package has no ally; the trooper's kill showed no "+N XP" in the clip (the floater exists and is tested but I did not verify it live). Floating Numbers OFF vs flash in K2: not obtained.
- **K2 side of those four:** K2 session done (see below), but K2's medpac "already at full health" refusal was all I got (K2 saves at full HP; the droids were already dead in the save); no XP pop-up was visible in K2's kill frames either (k2 recordings not kept: 360 MB). A K2 footer with a droid party member (T3-M4) is in `k2-droid/`; K2 shows the droid's own portrait in the Load row and the footer. A K2 footer with a party of several: still owed.
- Two further K2 facts: K2's Saving screen DOES show for named saves (`saving-named/`), 14 frames at 60 fps.
