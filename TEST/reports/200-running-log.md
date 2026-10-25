# TEST 200 running log (draft, text only)

Started 2026-10-25. Tester, Xvfb :2, own data dir.
Known, don't file: digits inside the typed field; '[Continue]' without a full stop; no K2 combat-bar capture.

## Build
- Settings: no settings.json present (TEST 199 left defaults) — defaults; brightness default.
- App main 184bdc2, git worktree builds/test200. Gate: "FOR TESTER — CORE at 184bdc2, 5141 tests, 0 failed, 12m50s at -j 3, peak 1947 MB"; "ARCHIVE last green at 184bdc2".
- Lock: Lodestar e1b6ed9 (on origin/main) = compiled; Lens 5fe60a9. Build 12.9 s through the lock; pubspec.lock unchanged.
- Shelf pulled to b2de52b. Packages in my data synced to it: rx-two-triggers (adds energy-shield.item), base-rules (had no party.locked/unlocked event kinds), precognition-ambush (my copy had extra droid motivator items). Old copies in notes/rx-two-triggers-before-test200 and notes/packages-before-test200/. All Shelf packages now identical in my data. check_shelf 33/125 identical.
- Beds: tool/author_tester_test200_saves.dart wrote gear-hand.sav (15 events) and no-pool.sav (14 events), rx-two-triggers.

## 6. Beds — gear-hand PASS
Gear Hand (rx-two-triggers): bump the Backer -> fight, my turn, 'Reactions (out of turn): one'. G then 1: 'gear yourself — Energy Shield up, 40 against electrical, energy · ion goes straight through · none left'; Gear slot dims (brightness 27 -> 8). End Turn: 'Opportunity attack / Backer leaves your reach / one reaction · 1 left / 70% (needs 7+)' Yes / No -> Yes (Backer 30 -> 26); 'Backer leaves Kael's reach' -> No. Line now 'Reactions (out of turn): none'. (gh-q0, gh-g, gh-shield, gh-backer-prompt, gh-kael-prompt, gh-after-no)
no-pool PASS: in the fight (Kael's turn) no reactions line; only 'Defense base 10 = 10'. (np-fight)

## 3. Four portraits — PASS (one small)
Four Up (specs200/four.json: Soldier + 2 joined Velas + the area's Vela): HUD bottom right shows the active member large and three small slots stacked above (four in all). One member (No Pool / Gear Hand with Kael = 2) shows two; Fight Nine (3) three. Bars: Vela at 25/40 -> her red bar ~60% from the foot; full Velas full; the player at 0 of 12 shows an empty bar. On Tester Bolt's board the fourth slot sits right of the board, not over its corner (the board ends left of it). (four-0, four-hurt)
Small: at load Four Up's companions draw two ways (two 'V' circles and one red party disc with a halo).

## 2. Click to use — PASS
Term Two (Locked and Trapped): plain click on the console from 2 squares walks beside it and opens the terminal. Plain click on the locked footlocker: Open Lock first -> 'you cannot use Security untrained — it needs at least one rank'. Plain click on the Shipping Crate (fixture) walks beside and examines ('examine Shipping Crate — d20 20 + Science 0 + Intelligence 1 = 21 …'). Step into the crate: 'the Shipping Crate is in the way'. Doors here are locked: 'Door is locked — heroic security' (as before). (click-console, click-footlocker, click-crate, step-into, door2)
## 4a. Terminal '[Leave.]' one full stop — PASS (click-console)
Doors: Endar Spire, Saber Hand: plain click on the Command Deck door walks there and crosses: 'Starboard Hold — arrived at north · saved'. PASS. (endar-0, endar-door)

## 1. Typed reply — PASS
Tab Ten (Pool One copy, specs200/tab.json) at the Warden: '1. [Interrupt.] …', '2. [Continue]', '[Type a reply.]' unnumbered (dim). Tab -> the row lights (pale). Digit 2 with the row focused -> Continue (no typing). Then '1. [Leave.]' (one full stop) + '[Type a reply.]'; a click on the row lights it; digit 1 -> leaves. Letters 'wh' (Pool Two) start typing in the row and light it. (tab-0, tab-tab, tab-2, tab-click, tab-1, tw-letter)
## 4b. Conversation '[Leave.]' one full stop — PASS

## 5. Rows — re-measured (small finding stands, 2 px)
Abilities > Skills at 1920 (Tab Ten), same y on the row and on the list line, vs K2 05c:
- ours y258 (row top-curve band): row line 925 (88,99,88), 926 (140,147,132), 927 (124,133,118); dark 928-931 (9,36,30); list line 932-933 (29,119,99); bar 935.
- ours y300 (row side): 925 (21,91,76), 926 (26,108,90), 927 (19,82,69); dark 928-931; list line 932-933.
- K2 y258: row line 923 (93,102,92), 924 (121,129,116), 925 (97,109,97); 926 faint (21,47,39); dark 927-930; 931 faint; list line 932-933.
- K2 y300: 923 (25,103,86), 924 (27,114,94), 925 (21,85,70); dark 926-930; list line 932-933.
So the row line's last lit pixel is 927 (ours) vs 925 (K2): ours 2 px nearer the list line. Coder's '925' matches the first pixel of our row line, not its last. (skills-rows.png)

## 7a. Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), walk, 3 Spaces, Messages > Combat: Rounds 1-3 identical to TEST 185; 'A fight begins.' once. (dice/combat-tab, combat.txt)

## 7b. Regression (Icon Nine) — PASS
reg199 loaded; Save > New Slot '36 : reg200' (10:36:14); Escape then F4: one quick.mark (10:36:19); Load lists Auto, Quick, '36 : reg200'; loaded reg200 at the start; a fight to its end: total-defeat popup with Load Last Saved Game / Go to Load Game List / Main Menu. (reg/load-list, reg/start, reg/end)
