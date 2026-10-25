# TEST 204 running log (draft, text only)

Started 2026-10-25.

## Build
- Settings: no settings.json (defaults); brightness default. Shelf 88d0d8f unchanged; all packages identical.
- App main 0233f17, worktree builds/test204. Lodestar ffa3e09 (lock), Lens 5fe60a9.
- Fixtures specs204/: Fight Twelve, Fight Thirteen (Soldier 1 + Vela, Tester Bolt), Note Taker (same, for Notes).
- Gate: "FOR TESTER — CORE at 0233f17, 5162 tests, 0 failed, 12m49s at -j 3, peak 1846 MB"; "ARCHIVE last green at 0233f17".
- Build through the lock 10.3 s; pubspec.lock unchanged; Lodestar ffa3e09 = lock = compiled.

## 1. Notes — PASS
Note Taker: typed 'Ask the Warden', Enter, 'jump then', 5 x BackSpace -> 'Ask the Warden / jump' (new line, Space, 'j' did not close the Journal, Backspace works). Save, Back, Close, reopen: the note is kept. Escape leaves Notes to the Journal. (notes-typed, notes-saved, notes-reopen, notes-esc)
## 4/8. Portraits — PASS (outside a fight)
Press Vela's small portrait: Vela goes large, the player drops to a small slot; press the player's small portrait: 'you are now controlling Note Taker', the player large again. No arrows above the portraits. (hud-0, press-vela, press-back, press-player)

## Fight Twelve (End Turn only, every frame kept: shots/204/f12, 240 frames; seq in shots/204/f12-seq.txt)
## 9. Companion's manual turn — PASS
My turn: 'Reactions (out of turn): one' / 'Defense base 10 + Dexterity 2 = 12'. Vela's turn ('Vela is waiting on you'): 'Reactions (out of turn): one' / 'Defense base 10 + Dexterity 1 + class 2 = 13'; her slots; her hover 'move 0 of 5 · reactions 1 of 1 · MANUAL' matches the dim Move slot. The large slot shows Vela on her turn (item 4 in a fight PASS). Note: at the start of her manual turn her move is already 0 of 5 and the action slot dim. (q-mine, q-vela, q-vela-hover)
## 3. Strip bars at 1920 — PASS
Fill is dark red (70,17,0) inside the pipe from the foot up. Vela at 29/40: fill y 146-207 of frame 122-208 = 72% (29/40 = 72.5%). Gunmen at 18/18: filled the whole pipe. (f12/f0226)
## 2. Party Member Down — FINDING (one of two falls)
Player Fight Twelve 5 -> -2 on a 7 hit ('Gunman damages Fight Twelve for 7 damage'): 'Party Member Down / Fight Twelve' shown (f0046-f0052), once. PASS.
Vela 1 -> -13 (f0225 -> f0226) on 'Gunman attacks Vela : *critical hit* : (19 + 3 = 22 : Threat Roll: 20)' / 'Gunman damages Vela for 13 damage' (floater -13): NO 'Party Member Down' in any frame f0222-f0240.
## 10. WATCH — reproduced
Same die stream as TEST 203 (one sample). Vela lost 14 from a 13 hit: before 1 of 40 (f0225), after -13 of 40 (f0226), in one step; the other Vela 40 -> 29 = the 3 + 8 hits ('damages Vela for 3' after the crit, round 9 'damages Vela for 8'). The player's own fall (5 -> -2 from a 7 hit) had no extra point; the player then bleeds 1 per round (-2,-3,…,-9). Save: notes/fixtures/specs204/fight12.json (fight12-204.sav, Tester Bolt): tap (1194,338), bump Right, then End Turn 16 times; the fall is at turn 16. The extra point is what makes the banner check fail (-13 + 13 = 0).
Bars at 1280: Vela's fill 36 px tall (y 104-140) beside her lit frame (83-140); gunmen full. Proportional by eye; exact share measured at 1920. (strip-1280)
## 5. Enemy strip hover — PASS: banner 'Gunman · Level 3 / bar / 18 of 18' sits below the strip (name 'GUNMAN' under the frame), clear of the strip; gone when the pointer leaves. (strip-hover, strip-leave)
## 6. Long prompt — PASS: 'Gunman: Blaster Rifle · rolled 12 / — d20 13 + attack 3 + Dexterity / …' wraps in its own column; the speaker name sits clear on its own row. (f12/f0016)
## 7. Party list at 1280 — PASS: row line 617-618, dark 619-621, list line 623 (1 px; 622 faint 130), bar from 625: 618 -> 623 = 5 px, as the other lists. (party-rows-1280)
## 11a. Dice — PASS (Messages > Combat rounds 1-3 = TEST 185)
## 11b. Regression (Icon Nine) — PASS
reg203 loaded; Save > New Slot '41 : reg204' (19:09:49); Escape then F4: one quick.mark (19:09:54); Load lists Auto, Quick, '41 : reg204'; loaded reg204; fight with the updated run/fightbolt.py: WON ('FIGHT OVER 35', three piles). (reg/load-list, reg/start, reg/end)
