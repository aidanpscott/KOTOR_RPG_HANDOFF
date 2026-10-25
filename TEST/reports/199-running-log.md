# TEST 199 running log (draft, text only)

Started 2026-10-25. Tester, Xvfb :2, own data dir.
Known, don't file: typed-reply number/digit typing; consoles only from the menu; HUD three portraits for a party of four; Deflection default Always; no K2 combat-bar capture.

## Build
- Settings reset first: settings.json moved to notes/settings-before-test199.json (defaults: brightness default).
- App a4446e8 (origin/in-game-batch-4), git worktree builds/test199.
- Gate: "FOR TESTER — CORE at a4446e8, 5125 tests, 0 failed, 12m43s at -j 3, peak 1838 MB"; ARCHIVE "last green at 47fe0ea" (not at a4446e8).
- Build through the lock 10.1 s; pubspec.lock unchanged; Lodestar 8350846 = lock = compiled. Lens 5fe60a9. Shelf f0a280a; check_shelf 33/125 identical.
- party-lock-bed copied from Shelf into tester-data packages. Fixtures specs199/: Pool One (Consular 1, DEX 12), Pool Two (DEX 16), Pool None (DEX 10), all party-lock-bed a01-deck.

## 2. Conversation words — Pool Two PASS
Warden (DEX 16): '1. [Interrupt.] Which deck is breached?' (red), '2. [Continue]', '3. [Type a reply.]'; right of the bar 'Reactions left: two' and '⟩ enter, when you are ready'. Digit 2 continued to 'Warden: This one. Your party stays…'; then '1. [Leave.]', '2. [Type a reply.]'; digit 1 left. Engineer: '1. [Leave.]', digit 1 left. Small: '[Continue]' has no full stop while '[Leave.]' and '[Interrupt.]' do. (warden-two, warden-hold, after-leave, engineer)
## 5. Package lock — PASS
After the Warden's second line: Party Selection, Mate selected: Remove greyed, 'You are unable to change your party at this time.' After the Engineer's line: Remove live, no reason. (lock-pkg, unlock-pkg)
## 6d. Reason clear of the frame line — PASS (lock-pkg: the line sits above the frame line, smaller).
## 6f. Sent home / one look — PASS
Remove Mate + OK: Mate not drawn anywhere. Add + OK: one party disc beside the player, sidebar card back. (sent-home, readd)
Pool One (DEX 12): 'Reactions left: one' with the interrupt row. Pool None (DEX 10): no interrupt row; '⟩ there is an interruption here and you have no reaction to spend' at the right; '1. [Continue]'; digit 1 continued, then '1. [Leave.]'. PASS. (warden-ONE, warden-NONE, none-after1)

## 3. Store — PASS
Ivy None (Store Bed): button 'Buy Item'; Show Sell List -> button 'Sell Item'; titles 'Buying Items' / 'Selling Items'. Bought a Medpac 100 -> 60. (store-buy, store-sell, store-bought)
## 6c. NEW amber — PASS
Inventory, four NEW rows (amber frame (149,122,71)); Medpac lit: frame stays (149,122,71), words pale. (inv-0, inv-medpac)
## 1. Right edges — bar PASS, rows small FINDING
1920, Inventory / Equip / Abilities Skills vs K2 05b/05a/05c (true 1080): list line x 932-933, 1 px gap (934), bar 935-948 (14 px), thumb 938-945 (8 px) — identical to K2 on all three. Rows: our row frame's right edge 926-927, K2's 924-925 (926 faint): rows end 4 px inside the line, K2 6 px. 1280x720: line 622, gap 623, bar to 632-633, thumb 626-630, rows end at 618 (4 px = 6 x 2/3). (inv-0, equip-0, abil-skills, *-1280)

## 4. Combat queue (Fight Nine fight, Vela 2's turn) — partly PASS, one FINDING
Three slots in the arrow: Move (arrows), action (the weapon), gear (medpac); the oval empty; right of it 'Reactions (out of turn): one' (teal) and under that 'Defense base 10 + Dexterity 2 = 12'; END TURN under the queue in a red frame (pale while hovered). (queue-0, queue-idle)
Preview: hovering a 4-square path on the board shows '5 → 1' at the Move slot's corner (k2_hud.dart:263, only while a path is hovered, not while the slot itself is). PASS. (queue-path-hover)
FINDING: after Vela moved one square (her card 'move 4 of 5'), the Move slot stays fully lit: mean brightness 93 before and after. (queue-moved, side-vela2)
Note: my turn-detect loop ended Fight Nine's turns by mistake; Fight Nine went down (-6 of 12; card '0 of 12').
Correction to the Move finding: the HUD acts only for the player ('not your turn — Vela is acting' on g); the queue may be showing Fight Nine's own (unspent) budget during Vela's turn. To be redone on the player's own turn.

## 6b. Load Last Saved Game — PASS
Fight Nine: F4 at start (Quick 07:34:24), one step up, Save '34 : lls199' (07:34:43), fight to total defeat: popup now offers Load Last Saved Game, Go to Load Game List, Main Menu. Load Last Saved Game loaded lls199 (player one square up), not the defeat or the Quick save. (defeat, lls-loaded)
Redone on Fight Nine's own turn: Move slot 93 -> 28 after one step (dims); after a bump attack the action slot dims (5 -> 1) and the oval shows the sword. PASS — Move finding withdrawn (the queue is the player's; on a companion's turn it shows the player's slots). (q2-0, q2-moved, q2-attacked)
Gear: 'gear — nothing to use' (Fight Nine carries none); gear dimming not reached.

## 6a. Downed companion — PASS at -2 (0 not reached)
Mid-fight (locked), Vela at -2 of 40: selected row shows 'down — not until this fight is over'; the standing Vela (26/40) shows 'You are unable to change your party at this time.' Both lines clear of the frame line. (vela-down, down-party, down-party-r2)

## 6e. Terminal — PASS
Term Two: right-click > Slice: no red message box over the frame; options 1, 2 (dim, 0 spikes), '3 [Leave.].' last. Digit 1 -> transcript prints 'Unseal the vault door. — costs 3 spikes, and you have 0 spikes'. Digit 3 leaves. Reopened, Escape leaves to play (no Options). Small: '[Leave.].' carries a doubled full stop. (term-0, term-refusal, term-left3, term-esc)

## 7a. Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), same walk, 3 Spaces, Messages > Combat: Rounds 1-3 identical to TEST 185; 'A fight begins.' once. (dice/combat-tab, combat.txt)

## 7b. Regression (Icon Nine) — PASS
reg198 loaded; Save > New Slot '35 : reg199' (07:48:13); Escape then F4: one quick.mark (07:48:23); Load lists Auto, Quick, '35 : reg199'; loaded reg199 at the start; a fight to its end: total-defeat popup with Load Last Saved Game / Go to Load Game List / Main Menu. (reg/load-list, reg/start, reg/end)
Not reached: a companion down at exactly 0 (only -2); gear slot dimming (no usable gear); 'Reactions (out of turn): none' after spending, and the no-pool case in a fight (no enemies in party-lock-bed).
