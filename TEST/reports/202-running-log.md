# TEST 202 running log (draft, text only)

Started 2026-10-25. Known, don't file: container page title, row click and 36 px rows reasoned; no combat-bar capture.

## Build
- Shelf pulled to 88d0d8f; my data's locked-and-trapped synced (adds medpac/vibroblade items, strongroom footlocker contents); old copy in notes/packages-before-test202/. All other Shelf packages identical.
- Settings: no settings.json (defaults); brightness default.
- App main d680dc2, worktree builds/test202. Gate: "FOR TESTER — CORE at d680dc2, 5165 tests, 0 failed, 13m00s at -j 3, peak 1823 MB"; "ARCHIVE last green at d680dc2".
- Lodestar 7801a13 = lock = compiled; Lens 5fe60a9.
- Fixture specs202/lock.json: Lock Two (Soldier 8, Security 11, Awareness 8), locked-and-trapped a01-strongroom.
- Build through the lock 9.9 s; pubspec.lock unchanged. check_shelf 33/125 identical.
Small finding: with the right-click menu open, Escape opens Options and leaves the menu open (and the arrow keys then do nothing). (menu-escape)
Small finding: the right-click menu stays open while the player walks and keeps its old distances; picking Search then refused with 'Search (Awareness) — 3 squares away' while adjacent. A fresh right-click shows the entries live. (fl-menu2, fl-search, fl-menu3)

## 4. Right-click Search — PASS
'search — d20 16 + Awareness 8 + Intelligence 2 = 26 · 2 to take' (the Medpac and Vibroblade); no 'walk onto it'. (fl-searched)

## 1. Containers — PASS
Plain click on the locked footlocker: 'open lock — d20 5 + Security 11 + Intelligence 2 = 18 vs 18 (hard) · open'. Plain click again: K2 container page titled 'Footlocker' with Medpac (lit) and Vibroblade, Get Items, Close. Down lit the Vibroblade, Enter took it; Get Items took the Medpac ('took Medpac'); Escape shut it. Re-opened: empty list, 'Container is Empty' under a dim Get Items; Close shuts. Inventory: Medpac and Vibroblade both with the amber NEW frame (149,122,71). Saved '38 : taken202', loaded it, re-opened: still 'Container is Empty'. (fl-click1, cont-0, cont-down, cont-enter, cont-getall, cont-esc, cont-empty, inv-taken, load-list, reload-cont)

## 2/3 notes
In a fight a struck-down gunman ('struck down · 0 of 18') leaves no pile on the board until the fight ends; at the end of a lost fight two piles were drawn where gunmen had died (piles-in-fight). Clicking the struck-down gunman's square mid-fight just walks there (kill2, my-turn, fight-pile-click). So in-fight opening is tested with the footlocker.

## 3. In a fight — PASS (Lock Three vs the strongroom's Probe Droid)
Lock opened out of the fight (29 vs 18). Bumped the droid; my turn: plain click on the footlocker from across the room walks the full 5 squares toward it ('there is no way there' when out of move). Next turn: plain click opens the page (Medpac, Vibroblade); Enter took the Medpac free ('took Medpac'); slots after: move dim 28, action 5 (lit), gear 27. Second click: page opens, 'opening the Footlocker — your second interaction this turn, so it cost your Action'; Action slot 5 -> 1. Third click refused: 'opening the Footlocker — you have spent your interaction and your Action'. (strong-fight, fight-fl1, fight-fl2, fight-take1, fight-after1, fight-open2, fight-after2, fight-open3)
Small: the message box cuts off its third line ('cost your Action' / 'Action' half shown).

## 2. Corpse piles — PASS (Icon Nine won the Tester Bolt fight with run/fightbolt.py)
Three piles drawn after the fight. Plain click on a pile: page titled 'Gunman' with 'Blaster Rifle'. Stepping Right onto a pile: no 'took' line, nothing taken. Clicking the pile under me opens the same page, rifle still there; Get Items took it; Inventory shows Blaster Rifle with the amber NEW frame. (bolt-end, pile-page, stepped-on, pile-under, pile-taken, inv-rifle)

## 5. Rows — PASS at 1920; 1280 party list 2 px wider
Pixel sums along the middle of the first row (row line, dark gap 75, list line), last lit pixel each:
1920: Inventory row 922-924 (925 faint 135) -> list 932-933: 925->933 = 8. Equip 924-925 -> 932-933: 8. Skills 923-925 -> 932-933: 8. Party list 924-926 -> 933-934: 8. K2 05c skills 924-925 (926 faint) -> 932-933 = 8; K2 05b inventory 922-925 -> 932-933 = 8. Match.
1280x720: Inventory 616-617 -> 622 = 5; Equip 616-617 -> 622 (623 faint) = 5; Skills 616-617 -> 622 = 5; Party list 616-617 -> 622-624 = 7. (8 x 2/3 = 5.3.) Small: the party list's line is 2 px wider at 1280. (rows-*.png, rows-*-1280.png)

## 6. One look — PASS
rx-two-triggers (Gear Hand, Kael placed as henchman): Kael is a 'K' token, the Backer red. Tester Bolt (Icon Nine): the area's Vela is a 'V' token at load. (onelook-rx, icon-0)

## 7a. Dice — PASS (Messages > Combat rounds 1-3 = TEST 185) (dice/combat-tab, combat.txt)

## 7b. Regression (Icon Nine) — PASS
reg201 loaded; Save > New Slot '39 : reg202' (12:59:07); Escape then F4: one quick.mark (12:59:12); Load lists Auto, Quick, '39 : reg202'; loaded reg202 at the start; a fight to its end, won this time (three piles). (reg/load-list, reg/start, reg/end)
