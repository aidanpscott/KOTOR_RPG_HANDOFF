# TEST 208 running log (draft, text only)

Started 2026-10-26. Known: tall message-box prompts (rebuild next) — capture if 'miss' clips again. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Settings: no settings.json (defaults). Shelf 553002b: tester-208 added (a01-immune, a02-drift, a03-muster, a04-locks); all else identical.
- App main 95765ea (worktree builds/test208); lock Lodestar f6495d3.
## 7b. Fresh Loom clone — PASS
git clone + checkout cc325e5 into builds/loom208-fresh: linux/ is tracked (linux/CMakeLists.txt, …). 'flutter build linux --debug' through the lock: built in 11.0 s with nothing generated; pubspec.lock md5 6b919d6f… unchanged; git status clean (0 lines); Lodestar f6495d3 compiled.
- Gate: "FOR TESTER — CORE at 95765ea, 5233 tests, 0 failed, 13m08s at -j 3, peak 1765 MB"; "ARCHIVE last green at 95765ea".
- App built through the lock in 12.5 s; pubspec.lock md5 d06e247c unchanged, git status clean; package_config lodestar root = Lodestar-f6495d3 (= lock).
- Beds: author_tester_test208_saves.dart wrote proof-immune (596 B, 20 events), proof-drift (529, 18), proof-muster (531, 18), proof-locks (530, 18). Fresh push-208.sav from specs208/push.json (seed push-208; push-207 left as is).
- Library: "45 packages installed · checked, 9 with problems".
## 1. Stun loses the attack, keeps the move — PASS
push-208, bump Quickstep. Initiative: Push Jedi 14 · Quickstep 12 · Slowpoke 3 (every enemy after me, so a stun "after its turn" in the same round can't happen on this roll; Quickstep was stunned in round 2 after its round-1 turn).
- R1: Push on Slowpoke success (18-4=14 vs 30), "Slowpoke is stunned." Slowpoke's turn: "Slowpoke closes 2 squares — 3 to 1 · Slowpoke is stunned" — moved, no attack.
- R2: Slowpoke attacks again: "Slowpoke attacks Push Jedi : *hit* : (15 + 3 = 18) · Flanking +2", 2 damage. Push on Quickstep (1+10=11 vs 30 automatic failure), "Quickstep is stunned."; its turn: "Quickstep closes 2 squares — 3 to 1 · Quickstep is stunned" — no attack (it had hit in R1).
- R3: "Quickstep attacks Push Jedi : *critical hit* : (20 + 3 = 23 : Threat Roll: 17 Automatic Hit!)", 3 damage. (s208/r1-*, r2-*, s-combat1, s-combat4)
## 2. Stun line under its own round, once — PASS
"Slowpoke is stunned." once, under Round 1 (after "is Force Pushed"); "Quickstep is stunned." once under Round 2. The turn line itself ends "· Slowpoke is stunned" (the reason it only moved). (s-combat1, s-combat4)
## Bed note — the proof beds read level 1 on the sheet
Proof Immune's sheet: header and footer "Jedi Consular 1", Vitality 8/8, Experience 0 / Needed 1000; but Force 104/104, Fortitude +12, Reflex +8, Will +15, and the power DC is 30 (level-16 values). The tool writes one classAdded {levels: 16}; my own beds (per-level events) read 16 throughout (Push Jedi: force 239, "Jedi Consular 16"). With 8 vitality each Proof Immune run ends in total defeat by round 3. (s208/i-sheet)
## 3. Immunities — PASS for the push; FINDING: Force Immunity: Stun doesn't stop the stun
Bump Rock (walk Right x2). Each run from the authored bed (backed up in notes/fixtures/specs208/authored; played copies moved to played/, played2/).
- Push on Rock (13-5=8 vs 30): "Rock is not Force Pushed" / "Rock is stunned." / "has been affected by Force Push" / 27 damage. Rock's next turn: "Rock is stunned" (no attack).
- Push on Steady first (13-5=8 vs 30): "Steady is not Force Pushed" / "Steady is stunned." / 27 damage; Steady's turn: "Steady closes 1 square — 2 to 1 · Steady is stunned" — no attack. Steady holds Force Immunity: Stun (the bed's featTaken steady.immune.02 force_immunity_stun).
- Push on Thug (11-5=6 vs 30): "Thug is Force Pushed" / "Thug is stunned." / 32 damage.
- Force Wave in round 1: Rock "not Force Pushed" + "stunned"; Steady "not Force Pushed" + "stunned"; Thug "Force Pushed" + "stunned". (i-c1, i2-c1, i2-c2, i3-c1)
Whether Immovable Object should also stop Rock's stun: MAIN to rule; I report only what's shown.
## 4. Dark power drift — PASS
Proof Drift: bump the Target (Right x2); f lists "1 Force Push 6f · 2 Force Affliction 12f · 3 Force Wave 22f"; 2 casts on the Target ("Force Affliction : 12f — 104 > 92 · … Target — 7 off str · 7 off dex · 7 off con — until rested"). Messages > Feedback: "You have moved closer to the Dark Side of the Force." — the only line. (d-t, d-feedback)
## 5. A join during a fight — PASS
Proof Muster (Ally One/Two/Three fielded). Right = Raider Boss: "This hall is ours." / "1. Recruit, with me!". Answer 1: "Then you both die." and the fight starts at once (initiative Proof Muster 20 · Raider Boss 18; "Your Turn / Combat Round 1" + "Enemy Sighted"). The Recruit's disc leaves the board; the strip is me, the three allies and R. Party Selection doesn't open. Feedback: "Ally One/Two/Three has joined the party." then "Recruit has joined the party." Party Selection opened by hand mid-fight: "0 Available Slots", Ally One/Two/Three ticked, Recruit listed unticked, Remove dim, "You are unable to change your party at this time". (m-a1, m-a3, m-feedback, m-party)
## 6. Skill checks follow the controlled character — PASS (one small)
Proof Locks (Strongroom): leader at start, F(ootlocker) right, C(onsole) 3 right, M(ate) below.
- Leader clicks F: "you cannot use Security untrained — it needs at least one rank". (l-f2)
- Press Mate's portrait ("you are now controlling Mate"), click F: "open lock — d20 5 + Security 10 = 15 vs 15 (moderate) · open". (l-f3)
- Console as Mate: STRONGROOM CONTROL, Slicing 12, Repair 2; "1 [Slicing] Unseal the vault door. (1 spike)", "2 … Cycle the corridor lights. (1 spike)". As the leader: Slicing 0, Repair 0; the vault door "(3 spikes)", lights "(1 spike)". (l-c6, l-c7)
- Fresh bed (authored copy restored): Mate's portrait, then the leader's ("you are now controlling Proof Locks"), click F: refused again, same line. (l2-mate, l2-back, l2-f)
- Abilities > Skills > Security: Mate (Scout 4) Skill Rank 8 · Bonus +2 · Total Rank 10; the leader (Jedi Consular 1) 0 · 0 · 0. (l-sec-mate, l-sec-lead)
Small: while Mate is controlled the console's reach is measured from the leader's disc. Mate stood directly left of C and the leader 2 away: "Slice (Slicing) — 2 squares away" (l-c4); with Mate moved under C and the leader diagonal to it, it opened (l-c5). Also: after Mate unlocks F, the leader opens it freely (it stays unlocked; l-f4).
## 7a. Loom's join refusal — PASS
Fresh-clone Loom (cc325e5) opened a scratch copy of store-bed (/tmp/claude-1000/lsc208/store-bed — the GTK location bar mangles any typed "kotor-" path into "kotorotor-", so the copy sits on a short path). merchant-greeting, "Suit yourself." selected, effect chip party.joined ("— subject, from, role"; the boxes relabel subject / from), subject "recruit.01", from "conversation", effect: the status line reads "refused — party.joined needs subject, from, role: use the wizard". Nothing written (diff -r against the installed store-bed: identical). (lo-pj, lo-refuse)
## 8a. Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), the same walk (Right x4, Up, Right x2), two Spaces. Messages > Combat (after the Journal and Messages help boxes, OK'd — Dice One is a chargen character) vs notes/dice-baseline-206.txt: all 17 Round/attack/damage lines identical; the only diff is OCR on the first line ("“A fight begins." vs "A fight begins. i"), so the md5s differ (f7f92695 vs a01882b3) on that OCR noise alone. (dice/dice-combat.png, .txt)
## 8b. Regression (Icon Nine) — PASS
'44 : reg207' loaded; Save > New Slot '45 : reg208' (000045.mark 13:14:04); Escape then F4 (after closing Options): one quick.mark 13:14:23; Load lists Auto, Quick (13:14:23), '45 : reg208', '44 : reg207'; '45 : reg208' loaded at the start square; walk in, run/fightbolt.py: WON ('FIGHT OVER 43'; three piles; Icon Nine 145 of 196). (reg/*)
## Processes
- app, xsettingsd, Xvfb and Loom stopped by PID.
