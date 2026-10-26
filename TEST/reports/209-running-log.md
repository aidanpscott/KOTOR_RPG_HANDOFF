# TEST 209 running log (draft, text only)

Started 2026-10-26. KNOWN, not filed: Force Immunity: Stun still stuns; controlled companion's reach from the leader; beds' level-1 sheet. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate: "FOR TESTER — CORE at cab0e62, 5237 tests, 0 failed, 13m34s at -j 3, peak 1979 MB"; "ARCHIVE last green at cab0e62".
- App main cab0e62 (worktree builds/test209): built through the lock in 10.0 s; git status clean; package_config lodestar root = Lodestar-5b1a90e (= lock).
- Settings: no settings.json (defaults); brightness default. Shelf 553002b: all packages identical (no change since TEST 208).
- Beds (notes/fixtures/specs209): stun-209 "Stun Shield" (rx-stun-bed a01-stun; Soldier 1; Energy Shield + Medpac in the bag); nade-209 "Nade Thrower" (tester-push; Soldier 8; three Frag Grenades); push-209 (Push Jedi, as specs207).
- Gear in the app: only the player's own budget spends Gear (play_screen useGear on f.player.budgets); enemy turns never raise a shield, so item 2 is checked on a stunned player (rx-stun-bed's mine stuns for 6 rounds).
## 1a. Message box layout — PASS
1920: the prompt runs at the box's full width on its own row, the name ("Push Jedi") on a row beneath. Out of a fight the same: area name, then the name row (wv-load).
## 1b. Force Wave in a fight — FINDING: the newest part is hidden below the box's edge
tester-push (6 targets): at 1920 the whole prompt fits (box y 8–290, 26%); at 1280x720 the same (y 5–180, 24%) — nothing to trim (w-1920, w-1280).
Local package tester-wave (copy notes/fixtures/specs209/tester-wave-package: the push yard + ten Slowpokes round the caster, 16 targets), wave-209 (Push Jedi), bump Left, f 3:
- 1920: the prompt starts "… stunned · Slowpoke — 8d6 21 · Quickstep — …" (front parts dropped, as meant), but its last visible line ends "Slowpoke — d20 10 =": the newest part is below the prompt's edge. Scrolling the prompt shows the hidden tail "… 6 vs 30 · stunned · Slowpoke — 8d6 36". Box y 8–438 = 41% (under 45%); prompt area ≈ 30%. (wv-1920, wv-1920-scrolled)
- 1280x720 (window resized), round 2: the bottom line is sliced through horizontally ("Slowpoke — d20 14 = 10 vs 30 · stunned · Slowpoke — 8d6 40 · Slowpoke"), and about a line and a half more lies below (scrolled: "— d20 4 = 0 vs 30 · stunned · Slowpoke — 8d6 36"). Box y 5–292 = 40%. (wv-1280, wv-1280-zoom, wv-1280-scrolled-zoom)
So the trim keeps one or two lines more than the share holds; the box clips them instead of dropping more parts from the front.
- Messages > Combat: the full prompt text is there after the per-target lines (wv-combat-end) — PASS for "full text kept".
## 1c. Grenade — PASS
nade-209 (tester-push), bump Left, o: "throw Frag Grenade at Slowpoke — Slowpoke — d20 18 − Dexterity 4 vs 15 · 20 damage · Quickstep — d20 12 + Dexterity 10 vs 15 · 10 damage · Blocked — … 20 damage · Droid Box — … 20 damage · Nade Thrower — d20 4 + reflex 2 + Dexterity 3 vs 15 · 20 damage · 2 left": five caught (four enemies and the thrower, ruled: a blast hits the crowd), whole, full width, name row beneath; box y 8–238 (22%). (n-throw)
## 2. Stunned and Gear — PASS (small: the refusal's reason)
stun-209 (rx-stun-bed): Right onto the mine: "goes off — d20 15 + fortitude 2 + Constitution 2 = 19 vs 100 · stunned for 6 rounds". (Out of a fight G says "nothing to shield against yet".) Right again (bump the Backer) starts the fight; the Backer backs off and hits (12 → 8). My turn, stunned (red mark on the portrait); the queue's Move lit, action and gear dim (g-queue-zoom). G: "gear — Energy Shield cannot be used — gear has already been used this turn" — refused; nothing was used this turn, the stun is why. Right: moved one square (disc 954 → 1050). (g-step, g-f2, g-g2, g-move)
## 1d. Outside a fight — PASS for a long description; scrolling NOT REACHED
bm-209 "Meditation Jedi" (specs209/bm.json: Battle Meditation, Force Push, Force Valor, Force Aura, Force Wave), tester-push, no fight. f 1 (1920): "Battle Meditation · 12f — 239 → 227 · ceiling −2 to 237 · at Meditation Jedi · This power grants +2 to attack rolls … will not affect any droids in the party." — whole, four lines, full width, name row beneath (bm-cast). 1280x720, f 3: Force Valor's description whole on three lines (bm-1280).
A prompt taller than the share outside a fight: no route in play found (Wave out of a fight says "there is no fight to aim it into"; f's list sits on the top line); Coder's test injects one.
## 3a. Dice — PASS
Dice One Quick Save, same walk, two Spaces, Messages > Combat vs dice-baseline-206.txt: all 17 Round/attack/damage lines identical; the only diff is OCR on line 1 ("“A fight begins." vs "A fight begins. i"), as in TEST 208. (dice/)
## 3b. Regression (Icon Nine) — PASS
'45 : reg208' loaded; Save > New Slot '46 : reg209' (000046.mark 16:30:20); Close, F4: one quick.mark 16:30:30; Load lists Auto, Quick, '46 : reg209'; loaded; walk in, fightbolt: WON ('FIGHT OVER 31'; three piles; Icon Nine 135 of 196). (reg/)
## Processes
- app, xsettingsd, Xvfb stopped by PID.
