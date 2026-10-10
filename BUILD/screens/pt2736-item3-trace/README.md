# PT-2736 item 3: hit feedback scored against the rules' own record (CODER, 2026-10-10)

MAIN closed item 3 on TEST 158's takes. This is CODER's independent run on the new machine, filed as supporting evidence. It is not a redo.

## Method
- App with `KOTOR_ATTACK_TRACE=<file>` (commit 7b8b9e1). Every attack appends one JSON line before the screen is told: wall-clock µs, target, hit, amount (`take1-trace.jsonl`).
- Capture: `ffmpeg -f x11grab -framerate 60 -copyts`. Frame timestamps are wall clock, so each traced attack is matched to its frames.
- `frames.dart` measures per frame: change of Onjo's HP text (both card positions, since initiative decides which card is on top), red excess in the play pane's bottom edge band (the flash), damage-colour pixels over Onjo (the number), miss-colour pixels over Onjo ("miss").
- `score.py` takes hit or miss **from the trace, not from the pixels**. A hit passes only if HP, flash and number first appear on the same captured frame and no "miss" shows. A miss passes only if "miss" shows with no flash, no number and no HP change.
- Bed: Endar Spire, Onjo Proof (author tool, DEX 8, CON 200 = 103 HP, a [Modded] save) next to the trooper. Space ends each of Onjo's turns, so only the trooper attacks.

## Result, take 1 (build 7b8b9e1, the a845f96 behaviour plus the trace)
**13 of 13 hits PASS** (HP, flash and number on one captured frame; `take1-table.txt`). **53 of 53 misses PASS.** The traced damage sums to 85, which is 103 − 18, the HP left on screen.

## The instrument can fail (mutation)
- Mutant 1, a845f96's `_floatTick++` removed: **equivalent here, killed nothing.** The float ticker starts at once and ticks on the frame that draws the HP.
- Mutant 2, floater and flash added in a post-frame callback (one app frame late): **all 7 hits FAIL**, flash and number +6 to +10 captured frames after the HP. All 22 misses also FAIL, because this mutant also stops "miss" from ever painting. `mutant-table.txt`.

## Caveats
- **The app ran at about 7–8 fps on Xvfb** (software GL, no GPU): content changes every ~120–150 ms. The capture is 60 fps. "Same frame" therefore means the same app frame. A one-app-frame lag shows as +6 to +10 captured frames, as mutant 2 shows. A GPU-display take would show the same test at the app's real frame rate.
- 9 of 66 events have a capture gap over 20 ms near the frame. One missed 17 ms capture frame cannot merge two app frames ~120 ms apart.
- The rules resolve an attack 202–753 ms (median 366) before its frame is drawn. That is the delay before an enemy's turn is drawn, not hit feedback.
