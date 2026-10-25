# TEST 203 running log (draft, text only)

Started 2026-10-25. Known, don't file: piles at fight end for dying enemies (ruled); the four K2 capture items reasoned.

## Build
- Settings: no settings.json (defaults); brightness default. Shelf 88d0d8f unchanged; all packages identical.
- App main 8cb9c31, worktree builds/test203. Gate: "FOR TESTER — CORE at 8cb9c31, 5152 tests, 0 failed, 12m38s at -j 3, peak 1814 MB"; "ARCHIVE last green at 8cb9c31".
- Lodestar ffa3e09 = lock = compiled; Lens 5fe60a9.
- Fixtures specs203/: Lock Four (Soldier 8, strongroom, for the poison mine), Fight Ten (Soldier 1 + Vela, Tester Bolt).
- Build through the lock 10.1 s; pubspec.lock unchanged.

## 6 (part). HUD hover / press — PASS (one small)
Fight Ten out of a fight: left panel gone. Hover the player's portrait: 'Fight Ten / Soldier · 1 / Vitality 12 of 12'; Vela's: 'Vela / Jedi Consular · 6 / Vitality 40 of 40 / Force 63 of 63 / MANUAL'. Pressing Vela's portrait: 'you are now controlling Vela'; my own portrait: 'you are now controlling Fight Ten'. Small: after pressing Vela the large portrait still shows Fight Ten. (hover-me, hover-vela, press-vela, press-me)
## 3. Action row — PASS
Right-click a Vela: five K2 boxes above her (Wait here lit and named in the strip); hover names Wait here, Dismiss, Give Item, AGGRESSIVE (current behaviour), MANUAL. Behaviour arrows: down -> Jedi Support -> Healer, up -> Jedi Support (in place). Mode arrow: HANDS OFF -> AUTO -> MANUAL. Press on the behaviour box: 'Vela — Jedi Support', row closes. Reopened: shows JEDI SUPPORT; mode to HANDS OFF + press: her portrait hover reads HANDS OFF. Escape closes the row; a tap outside closes it. (row-0, row-hover-*, row-beh*, row-mode*, row-apply-beh, row-apply-mode, row-esc, row-tapout)

## 4. Select Behavior — PASS (from Party Selection's 'Select Behavior' button)
Title 'Select Behavior'; Aggressive, Jedi Support (lit, current), Healer; pane 'Jedi Support / Keep the party standing before anything else.'; 'Vela' under the list; Close. Escape returns to Party Selection. No refused behaviour for Vela (none dim). From the action row, pressing the behaviour box applies the shown behaviour directly; I found no way from the row to open the picker page (MAIN to say if one is meant). (picker, picker-healer, picker-esc)

## 5. Personal Notes — layout PASS; FINDING: typing does not enter text
Journal > Notes: title 'Personal Notes', a full-width text box, Back and Save (Save shows 'saved'); Back returns to the Journal. FINDING: the text box takes focus (the caret blinks — blink diff at its top-left) but typed keys enter nothing: 'xdotool type' and single 'xdotool key A/s/k' both leave it empty. The same synthetic input types into the save-name box and the conversation's typed reply, so the Notes field (a raw EditableText, notes_screen.dart:123) is the odd one out. No privacy help box for Fight Ten (authored: help boxes off — helpBoxesOn needs the chargen flag). (notes-0, notes-typed, notes-saved, notes-back, notes-reopen, notes-keys)
Twi Seven (chargen, help on): first Notes open shows the privacy box 'Personal Notes are fully private: no scripted content can read them, and they are not kept in your save.' with OK; reopening: no box (once). PASS. Typing 'hello' after a click: still nothing entered (finding confirmed on a second character). (twi-notes1, twi-notes2, twi-notes-type)

## 2. Initiative strip (Twi Seven mid-fight, 1920) — partly PASS, FINDING
K2 frames: enemies red 'G', Twi Seven teal (portrait '?', no art), Vela's portrait; the one acting (Vela) larger and lit; the first gunman (acted) dimmed. Hover on a gunman: 'Gunman / Gunman · Level 3' (no numbers). FINDING: the vitality bar beside each frame is an empty grey pipe for everyone — inside samples grey (87) or black, no fill — though Vela is 25/40, a gunman 9/18 and Twi Seven 13/13. (strip-1920, strip-hover)

## 1. Banners (part) — PASS
'Your Turn' / 'Combat Round 3' at top centre under the strip (ban b01). Enemy attack: 'Gunman attacks Vela' / '*hit* : (18 - 1 = 17)' on two lines (ban c01). Note: a gunman's hover banner (from resting the pointer on the strip) stayed up after the pointer moved away (c01, c05).
'Enemy Sighted' as the fight began, under 'Your Turn / Combat Round 1' (stacked, top centre). Three-line message box ('Fight Ten: 12 of 12 · Gunman … / initiative — Fight Ten 16 · Gunman 16 · Vela 4 · Gunman 1'): strip and banners sit below it, nothing covered; words clear of the border. (ban/s00, s01) Small: the prompt's first line runs right up to the name 'Fight Ten' ('Gunman 16Fight Ten').

## 1b. 'Party Member Down' — FINDING
Fight Eleven (specs203/fight11.json), End Turn repeatedly with every frame kept (shots/203/down, 340 frames): Vela went 1 of 40 -> -13 of 40 on one gunman hit (floater '-13'); the player went to -2 earlier. No frame shows 'Party Member Down' (OCR of all frames over the whole board area: 0 hits); the attack banner 'Gunman attacks Vela / *hit* : (10 + 3 = 13)' shows instead (f0322). Likely cause (hypothesis): play_screen.dart:21212 tests `current + amount > 0`; here -13 + 13 = 0 (she lost 14: the 13-point hit plus one more), so a companion knocked from 1 to below zero does not count as 'up before the blow'.
Strip at 1280x720: under the message box, Vela larger/lit, acted gunman dim; same empty bars. (strip-1280)

## 7. TEST 202 fixes (strongroom, Lock Three's mid-fight save) — PASS
Right-click menu open; Escape -> menu closes (play); Escape again -> Options. (menu-open, menu-esc1, menu-esc2) Right-click menu open, then Up: the menu closes and the player walks. (menu-walk) Three-line message box words clear of the border (see 1/2).
## 6 (rest). Marks / hover / enemy state — PASS
Walking onto the poison mine: 'goes off — d20 20 = 20 vs 15 · 3 damage · 69 of 76 · 2 more rounds'; a red bad-mark arrow on the portrait's corner. Hover: 'Lock Three / Soldier · 8 / Vitality 69 of 76 / poisoned / move 2 of 5 · reactions 2 of 2'. Board hover on the Probe Droid: top banner 'Probe Droid · Level 1' with its bar and '24 of 24', plus the odds box '95% (needs 2+) …'. Small: that banner's top overlaps the bottom of the lit strip frame. (poison-1, poison-2, poison-hover, poison-mark-hover, enemy-hover)
Note: the teal up / red down arrows above the HUD portraits are unexplained (no hover text); possibly the good/bad summary.

## 7b. Party list rows — 1920 PASS, 1280 small finding remains
1920: row line 924-926 -> list line 933-934: 926->934 = 8 (as the others). 1280x720: row line 617-618 -> list line 622-624: 618->624 = 6 px (others 5); the list line is 3 px wide (622-624) where the other lists' is 1 (622). Was 7 in TEST 202. (party-rows, party-rows-1280)

## 8a. Dice — PASS (Messages > Combat rounds 1-3 = TEST 185)
Typing control: the same 'xdotool type' entered 'reg203' into the save-name box, so the Notes finding is the field's, not the input method's. (reg/name-typed)

## 8b. Regression (Icon Nine) — PASS
reg202 loaded; Save > New Slot '40 : reg203' (16:24:36); Escape then F4: one quick.mark (16:24:41); Load lists Auto, Quick, '40 : reg203'; loaded reg203 at the start; a fight to its end (total defeat; my fightbolt.py reads the turn from the retired left panel, so it only ended turns — to be updated). (reg/load-list, reg/start, reg/end)
