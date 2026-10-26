# TEST 207 running log (draft, text only)

Started 2026-10-26. Known: a hit for 0 ('not enough to hurt') ruled correct (PT-1622). Dice baseline: notes/dice-baseline-206.txt (md5 a01882b3).

## Build
- Settings: no settings.json (defaults). Shelf 9656671: base-rules synced (attacks.toml, powers.toml); old copy notes/packages-before-test207.
- Gate: "FOR TESTER — CORE at 4611a62, 5214 tests, 0 failed, 13m10s at -j 3, peak 1864 MB"; "ARCHIVE last green at 4611a62".
- App main 4611a62 (worktree builds/test207): built through the lock 9.9 s; pubspec.lock unchanged; Lodestar ec4b24b = lock = compiled.
- Loom 02b6faa (worktree builds/loom207): linux/ generated, pubspec.lock restored, built 6.8 s on the committed lock; Lodestar ec4b24b compiled. (7: builds — opens checked below.)
- Local bed packages/tester-push (copy notes/fixtures/specs207/tester-push-package), 12x9 yard with walls: Slowpoke (DEX 3) right of the player, Quickstep (DEX 30) left, Walled (DEX 3) by the right wall, Blocked (DEX 3) with Crate Dummy behind it, Droid Box (droid). Push Jedi (specs207/push.json): Jedi Consular 16, WIS 20 / CHA 18, Force Push, Whirlwind, Wave.

## 1a. Force Push, failed save, open ground — PASS
Fight started by bumping Quickstep (left). My turn: f, 1 (Force Push), target 1 Slowpoke. Log: 'Push Jedi attempts Force Push on Slowpoke : *success* : (18 - 4 = 14 vs. 30)' / 'Slowpoke is Force Pushed' / 'Slowpoke has been affected by Force Push' / 'Push Jedi damages Slowpoke for 28 damage'; 'Slowpoke is stunned.' Board: Slowpoke's disc x 1158 -> 1286 = 128 px = 2 squares straight right (away from the caster on its left). 200 -> 172. No opportunity attack logged (none adjacent behind; see later). (p1-before, p1-6, log1)
Note: the stun line 'Slowpoke is stunned.' is listed above 'Round 1' in the Combat log.
## 1b. Stopped by a wall — PASS
Push on Walled (at (9,2), the caster at (5,4)): 'Walled — d20 11 = 7 vs 30 · stunned · Walled — 6d6 23' (200 -> 177). Disc (1370,307) -> (1434,243): one diagonal square (right and up), into the corner where both walls stop it — moved 1. (p3-before, p3-after)
## 2. Made save — PASS
Round 3, Push on Blocked: 'Push Jedi attempts Force Push on Blocked : *resisted* : (20 - 4 = 16 vs. 30 automatic success)' / 'Blocked is not Force Pushed' / 'Push Jedi damages Blocked for 8 damage' (0.5 x level 16; 200 -> 192); no move. (p4-before, p4-after, log4b)
## 1c. Stun — FINDING (likely)
'Slowpoke is stunned.' (pushed in round 1 on my turn, initiative 14) yet in round 1 'Slowpoke closes 2 squares — 3 to 1 · Slowpoke: unarmed · rolled 4 … miss' and in round 2 'Slowpoke attacks Push Jedi : *miss*'. 'Walled is stunned.' (round 2) yet in round 2 'Walled closes 5 squares — 5 to 2 …'. A 1-round stun did not stop the stunned creature's next turn. (log1, log4, t2)
## 1d. No opportunity attack on the push — PASS so far: Slowpoke left my reach by the push with no opportunity line in the log.
## 1e. Stopped by a creature — PASS
Fresh Push Jedi; bump Quickstep; first push on Blocked (Crate Dummy directly behind it): 'success (18 - 4 = 14 vs. 30)' / 'Blocked is Force Pushed' / 28 damage / 'Blocked is stunned.'; Blocked's disc did not move (same pixels before and after) — moved 0. Note: the log still says 'is Force Pushed' when it moved 0. (b-before, b-after, logb)
## 4a. Droid and Force Push — PASS
Round 2, Push on Droid Box (at (5,2), caster (5,4)): 'success (11 - 4 = 7 vs. 30)' / 'Droid Box is Force Pushed' / 23 damage; NO 'is stunned' / 'has been affected' line; the prompt reads 'Droid Box — d20 11 = 7 vs 30 · resists · Droid Box — 6d6 23'. The disc moved up to the top floor row (1 square, wall above). (d-before, d-after, logd)
## 3. Force Wave — PASS
Round 3, f 3 (anchored on the caster, no target prompt): Slowpoke (15-4=11 vs 30), Quickstep (5+10=15), Walled (19-4=15), Blocked (1-4 auto fail), Droid Box (14-4=10): each 'is Force Pushed' / 'has been affected by Force Wave' with damage 22/34/30/27/29. Crate Dummy: '*resisted* : (20 - 4 = 16 vs. 30 automatic success)' / 'Crate Dummy is not Force Pushed' / 13 damage ('saved · half'), no stun. Visible discs after: top-right corner, right edge, bottom — pushed outward. (w-before, w-after, logw)
## 4b. Droid and Force Wave — PASS: the prompt reads '… Droid Box — d20 14 = 10 vs 30 · stunned · Droid Box — 8d6 29'.
Small: the Wave's prompt runs to 14 lines and the message box grows down over most of the board (w-after).
## 5. Immovable Object / Force Immunity: Stun — NOT REACHED (no installed bed has a creature holding either; a placed enemy's feats come from its class grants, and no class grants either at the levels used).

## 6. Text seed (setup)
Copied wave-207.sav (original md5 22465886… unchanged, backup notes/fixtures/specs207/wave-207-original.sav) to seed-text-207.sav by hand: decompressed the gzip body, set the created event's payload "seed":"abc" (and name 'Seed Text'), recompressed, patched the header's body length (u32 LE at 74) and name. (writeSave itself refuses a bad seed, so the tool cannot write one.)
## 6. Text seed — PASS
Load lists 'Seed Text' (Tester Push). Load -> 'THIS SAVE WILL NOT OPEN / The campaign seed must be a whole number; this one is "abc", so its dice could not be replayed.' with Back. The hand-made copy was then moved out of saves/ to notes/fixtures/specs207/. (seed-list, seed-load)

## 7. Loom on the new pin — PASS
Loom 02b6faa (Lodestar ec4b24b) launched and opened the scratch store-bed ('opened'). Note: the conversations list shows merchant-greeting twice — the scratch copy holds both the .toml and the .dlg my TEST 206 Write produced. (loom-open)

## 8a. Dice — PASS: Messages > Combat after two Spaces identical to dice-baseline-206.txt (md5 a01882b3 both). (dice/combat.txt)

## 8b. Regression (Icon Nine) — PASS
reg206 loaded; Save > New Slot '44 : reg207' (07:05:47); Escape then F4: one quick.mark (07:05:52); Load lists Auto, Quick, '44 : reg207'; loaded; fight with run/fightbolt.py: WON ('FIGHT OVER 35'). (reg/*)
