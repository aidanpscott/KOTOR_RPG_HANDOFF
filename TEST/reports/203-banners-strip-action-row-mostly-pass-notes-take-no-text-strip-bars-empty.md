# TEST 203: banners, the initiative strip, the action row, Select Behavior, Personal Notes, the retired left panel, TEST 202 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-203/` (MAIN_WORK `ffd5da59`). The step-by-step log is `TEST/reports/203-running-log.md`. Compared against `media/study/pt2752/our-own-screens/`.

## Build

App main `8cb9c31`, a git worktree beside my own clone. `gate.py --at 8cb9c31`: "FOR TESTER — CORE at 8cb9c31, 5152 tests, 0 failed"; ARCHIVE last green at 8cb9c31. Lodestar `ffa3e09` = lock = compiled. Lens `5fe60a9`. The build (10.1 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. Settings: defaults. Brightness: default. Shelf `88d0d8f`, unchanged; all packages identical.

Characters (`specs203/`): Fight Ten and Fight Eleven (Soldier 1 with Vela, Tester Bolt), Lock Four. Also Twi Seven (chargen), Lock Three's mid-fight save, Icon Nine and Dice One.

## Summary: most pass; three findings

| # | Check | Result |
|---|---|---|
| 1 | Banners | **PASS** for: "Your Turn" / "Combat Round 3"; the enemy attack on two lines ("Gunman attacks Vela" / "*hit* : (18 - 1 = 17)"); "Enemy Sighted" under "Your Turn / Combat Round 1" as a fight began, stacked at top centre. **FINDING**: "Party Member Down" never showed (below) |
| 2 | Initiative strip | **PASS** for K2 frames (teal for the party, red for enemies), the one acting larger and lit, those who've acted dimmed, the hover naming "Gunman · Level 3" with no numbers, the same at 1280×720, and a three-line message pushing the strip and banners down with nothing covered. **FINDING**: the vitality bars are empty (below) |
| 3 | Action row | **PASS**. Right-click a Vela: five K2 boxes, with "Wait here" lit and named in the strip; hovering names Wait here, Dismiss, Give Item, AGGRESSIVE and MANUAL. The behaviour arrows step Jedi Support → Healer and back; the mode arrows step HANDS OFF → AUTO → MANUAL, in place. Pressing applies ("Vela — Jedi Support"; her hover then reads HANDS OFF). Escape, or a tap outside, closes the row |
| 4 | Select Behavior | **PASS** from Party Selection's button: "Select Behavior"; Aggressive, Jedi Support (lit, current) and Healer; the pane "Keep the party standing before anything else."; "Vela"; Close; Escape returns. No refused behaviour to see. From the row, the behaviour box applies directly; I found no way to open this page from the row |
| 5 | Personal Notes | **PASS** for the title, text box, Back and Save ("saved"), and the privacy box once on first open (Twi Seven; authored characters have help boxes off). **FINDING**: the box takes no text (below) |
| 6 | Left panel gone | **PASS**. Portrait hover: "Lock Three / Soldier · 8 / Vitality 69 of 76 / poisoned / move 2 of 5 · reactions 2 of 2"; Vela's adds Force and MANUAL or HANDS OFF. Poison from the mine shows as a red bad mark on the portrait. A portrait press switches control ("you are now controlling Vela"). The enemy hover shows "Probe Droid · Level 1", its bar and "24 of 24" |
| 7 | TEST 202 fixes | **PASS**: Escape closes the right-click menu first and opens Options only after; walking closes the menu; the three-line message stays clear of the border; the party list is 8 px at 1920. **Small**: at 1280 the party list still measures 618 → 624 (6 px, against 5 on the others; its list line is 3 px wide) |
| 8 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185. Regression: Save (slot 40, "reg203"), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings

1. **Personal Notes takes no text.** The box takes focus (the caret blinks) but nothing typed appears, both from `xdotool type` and from single keys, for Fight Ten and for Twi Seven. As a control, the same input typed "reg203" into the save-name box in the same session. Save then reports "saved" with an empty note. (`notes_screen.dart:123`, a raw `EditableText`.)
2. **"Party Member Down" never showed.** I kept every frame (340) across a fight: Vela went from 1 to −13 of 40 on one gunman hit (floater "−13"), and the player had fallen earlier. No frame has the banner; the attack banner shows instead. Likely cause (a hypothesis): `play_screen.dart:21212` requires `current + amount > 0`, and here −13 + 13 = 0 because she lost 14 (the hit plus one more), so the blow doesn't count as taking her from up to down.
3. **The strip's vitality bars are empty.** Beside every frame there's a grey pipe with grey or black inside and no fill, whether the member is at 13/13, 25/40 or 9/18, at 1920 and 1280.

## Small

- After pressing Vela's portrait, the large HUD portrait still shows the player, though the line says "you are now controlling Vela".
- The enemy hover banner stays up after the pointer leaves the strip, and its top edge overlaps the bottom of the lit strip frame.
- The prompt's first line runs into the speaker name ("…Gunman 16Fight Ten").
- The party list at 1280: 6 px against 5.
- The teal up and red down arrows above the HUD portraits have no hover text; I couldn't tell what they are.

Known and not filed: piles appear only once a fight ends for dying enemies (ruled); the four K2 capture items are reasoned.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
