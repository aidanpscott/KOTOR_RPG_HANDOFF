# Sign-off video: Save/Load and Options, re-recorded (app at the hash in the commit message)

Two MP4s, H.264, 1920x596, ~7 MB total. K2 still LEFT, our live footage RIGHT, caption bar on top; "K2: none captured" where no K2 still exists. K2 side is a still. Recorded on a throwaway data folder, no new code during recording.

## signoff-1-save-load.mp4 (4:12)
| Start | Clip | Look at |
|---|---|---|
| 0:00 | SL1 | Main-menu Load list: **Auto Save pinned first** (owner ruling; K2 lists it last), Switch Characters, [Modded] row (Dax Orlo). |
| 0:31 | SL2 | Continue, in-game Options with the party footer. |
| 0:42 | SL3 | Save Game > New Slot > name > OK. The Saving picture shows for 0.23 s: K2's named save, re-measured at 60 fps (14 frames). |
| 0:57 | SL4 | Overwrite prompt (Cancel, OK) and delete prompt (Cancel, OK). |
| 1:34 | SL5 | Clicking rows: picture, place, time, party. Pictures are there at once. |
| 1:46 | SL6 | F4 quick save, walk, F5 back to the saved square. |
| 2:02 | SL7 | Load list, Auto Save first, then Quick Save and saves newest first. |
| 2:18 | SL8 | Five-member party, arrows page 3 + 2 (owner-ruled). |
| 2:43 | SL9 | Mid-fight save. |
| 3:06 | SL10 | Play on, load it: Loading picture, then the same turn, 11 of 11, 5 moves. |
| 3:47 | SL10b | Walk away after the save, load: square, turn and moves come back. |
The earlier "wrong mid-fight load" was a click landing on the board while the load was still in flight; every load now shows the Loading picture from its first frame and takes the clicks.

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
