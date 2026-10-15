# TEST 182 running log (draft, text only)

Started 2026-10-14. Tester, Xvfb :2, own data dir, no K2, no BG3.
Read first: Coder's step 3 entry (app bb3b732: reaction prompt, Always/Ask/Never, K2 message box, Space does not answer, built reactions: Opportunity attack, Force Deflection, Force Redirection), the step 3 rulings (6efcc15: Deflection default Always, stunned no reactions, replay dice kept), step 4 built (209eba0: sidebar move/pips, portrait red fill, white damage chunk 800 ms, K2's four condition icons, hotbar, floater colours, tokens slide 546 ms a square) and the step 4 real-app fault (7a863fc: Overlay at the root, hover box sized to text).

## Build
- App 7a863fc, git archive to ~/kotor-tester/builds/test182. Built through tool/one_at_a_time.sh: 2446 s (waited behind Coder's flutter test -j 1). pubspec.lock unchanged.
- Lodestar 5c676c45e857af5661301e4feeeffb140f8a6c76 = lock = compiled. Lens 5fe60a9c2be41852fd8818c1ca579a2077808d79 = lock = compiled. Loom: no entry in the lock.
- Shelf 1e3ffb4 (= origin); check_shelf below. tool/env.sh sourced. Bundle launched with & outside the lock.
- Fixtures (one locked dart run, specs notes/fixtures/specs182/): rx-182 (tester-pass, Soldier 3 CON 30, sword + rifle), kind-182 (tester-kinds), defl-182 (Tester Save Bed, Jedi Guardian 12 with force_deflection + force_redirection, CON 30).
- New local bed tester-kinds (row 1: 2-point mines of fire, cold, electrical, sonic, ion, energy, light_side, dark_side, universal, unstoppable, piercing; row 3: condition mines stunned, slowed, held, paralysed, shaken, panicked, cowering, blinded, dazed, entangled, sickened; all dc 100 on_save none). tester-pass gained a stun mine at (7,1) (rounds 3).

## Items

### Item 8 (part): Options > Gameplay (i08a, i08b)
- K2-look page "Gameplay Options": rows "Opportunity attack: Ask", "Force Deflection: Always", "Force Redirection: Ask", each with K2 arrows; help pane: "A ranged attack at you would hit: turn the bolt aside, or send it back, for the power's Force points. / ALWAYS: taken without asking. / ASK: the game pauses and asks. / NEVER: let it land."; Close and Default. Arrows cycle Ask -> Never -> Always -> Ask. Default restores Deflection to Always and the others to Ask (settings.json "reactions":{}). PASS. Survives load: every replay below loaded a save made before the change and kept the setting. Restart: below.

### Item 1: the opportunity-attack prompt (tester-pass, Rx One authored; scripted replay run/rxrun.sh from one pre-fight quick save, same inputs each time: me to (6,1), Kael draws droid B, Kael retreats to (2,0), B chases and leaves my reach)
- Ask: the game stops BEFORE B moves (B still on (7,0)). Centred K2 box: "Opportunity attack / Sentry Droid leaves your reach / one reaction · 1 left / 80% (needs 5+)" with Yes / No (i01a). PASS. (Note: a title plus three lines; the box is drawn over the log column.)
- Space: nothing, box stays (i01b). PASS.
- Enter: "Opportunity attack: Rx One attacks Sentry Droid : *hit* : (7 + 5 = 12)" / "Rx One damages Sentry Droid for 6 damage", then B's turn goes on (i01c). Escape: no swing (i01d). Y: swing; N: no swing (i01e). PASS.
### Item 2: Always: no box, the swing happens (i02a). Never: no box, no swing (i02b, i02c). PASS.
### Item 7: same dice: the Always run and the Ask-then-Yes run give the identical log line for line, rounds 1-3 (i07). PASS. (No/Never runs differ after the decision point only, since my swing spends dice.)
### Item 4 (part): empty pool: after Yes spent my one reaction, I stood beside B again and Kael drew B away (round 4): B left my reach, no box (i04a). PASS. My sidebar pip goes dark once spent (i10a). Two triggers at once / target gone before the second box: NOT REACHED (needs a third party member in reach at once; my fixtures have two).
### Item 5: stunned: NOT REACHED. I got Rx stunned (stun mine, sidebar shows the stun icon) with the reaction unspent, but the droids then stayed on me, so no enemy left my reach while I was stunned (i05). No box appeared during those rounds.
### Item 3 (part): Defl One (Jedi Guardian 12, knows Force Deflection AND Force Redirection), Sith Trooper with a rifle, Tester Save Bed:
- Defaults (Deflection Always, Redirection Ask): the box asks for REDIRECTION: "Force Redirection / Sith Trooper fires at you / 12 Force points · 73 left · spent only if the shot would hit" (i03a). No: the shot hits for 4; no deflection although Deflection is Always (i03b).
- Redirection Never, Deflection Always: no box; the shot hits for 4, no deflection, force 73 untouched (i03c).
- FINDING (code, play_screen.dart:4867 _deflectFor / :9645 _deflectionReady): a character who knows Force Redirection is decided ONLY by the Redirection row; the Deflection row is never read. So "Deflection: Always" (default) does nothing for such a Jedi, and Redirection Never or No means no deflection at all. Deflection alone: authoring a Deflection-only Jedi (defl-only-182), queued behind Coder's suite.

### Item 3 (rest): Deflection only (Defl Two, authored Jedi Guardian 6 with force_deflection only; same scripted fight vs the Sith Trooper, deterministic dice)
- Always (default): rounds 1-3 miss, force 37 untouched; round 4 the shot HITS for 10 AND force 37 -> 31 (max 36): the points are spent but no deflection shows and the damage lands (i03d).
- Ask: box "Force Deflection / Sith Trooper fires at you / 6 Force points · 37 left · spent only if the shot would hit" (i03e). Yes each round: identical log and outcome to Always — misses spend nothing; round 4 spends 6 and the hit still lands (i03f). No each round: round 4 hit lands, force untouched (i03g).
- Never (written to settings.json while the app was stopped, since my Gameplay clicks kept being taken by the open box): no box; 14 rounds, 5 hits land, force 37 untouched (i03h).
- FINDING: Deflection spends its Force points on a hit and never deflects; no "Deflected" anywhere in 4 hits under Always/Ask-Yes. (Coder's Ask Yes test: "a landing shot costs the power"; I never saw the deflect roll succeed — it may be a roll vs the attack that failed each time, but no roll is shown in the log or status line either way.)
- FINDING (earlier): a Jedi who knows Redirection is governed by the Redirection row only; Deflection: Always does nothing for them.
- Note: my setrow.sh Gameplay clicks only work with no box open; settings.json is the reliable check.
- **Item 3: PARTIAL** (defaults, Ask box, Yes/No/Never behave as wired; no deflection ever lands; Redirection-knower ignores the Deflection row).

### Item 6: companions — Kael MANUAL beside droid A at (6,3)/(5,4) diagonal; I walked away to (1,3) and A chased me, leaving Kael's reach: no box; the log shows A's opportunity attack on me only, and nothing from Kael (i06). FAIL against the order ("a companion you control is asked"): MANUAL Kael was neither asked nor swung. AI companion: not run (the AUTO setting reached in TEST 180 bed; no time).

### Item 8 (rest): Redirection: Never survived an app restart (i08c); Default then wrote "reactions":{} (Deflection back to Always, others Ask). **Item 8: PASS.**

### Item 9: hotbar
- Common tab: Use the Force f, Dash h, Disengage d, Hide s, Scan c, Treat t, Repair r, Aim a, Stand up u, Rest e, One hour of meditation b, Eight hours of meditation n, End Turn space (scrolls sideways); Items tab: Gear g, Throw a grenade o (i09d). Names as ordered, Dash not Hurry. PASS.
- Hover: small box above the button, name, document line, refusal in red, cost footer (Rest: "Eight hours of ordinary rest. / not in the middle of a fight / eight hours · not in a fight"; Scan: "nothing here is hidden from you / Action in a fight · free outside one"; Aim: "Blinded: name a square and swing at it. / you can see — walk into what you mean to hit / Action"; Dash: "Double your movement this round. / Action"; Use the Force: "A power targeting an enemy or an ally. / Action · Force points") (i09a, i09c). PASS.
- Refused presses (button at y 812): Rest "not in the middle of a fight", Scan "nothing here is hidden from you", Aim "you can see — walk into what you mean to hit"; nothing spent (move 5, action lit). Dash press: "dashing — 10 squares this round", 10 move, Action spent (i09b). PASS. (Aim's refusal is "you can see", not "Action spent".)
- Hidden in a conversation (i09e) and at a terminal (i09f). PASS.
- 1280x720: a fresh window at 1280x720: one row, the board, sidebar and strip intact (i09g). PASS. Note: resizing a running 1920x1080 window down to 1280x720 does NOT relayout — the app keeps painting its 1920 layout cropped (i09h); a fresh window sized after launch is fine.
- **Item 9: PASS** (resize note).

### Item 10: sidebar: "move N of S" per member ("move 5 of 5", "move 0 of 5", "move 10 of 5" after Dash) and one pip per reaction, dark when spent (i10a). PASS. Note: "move 10 of 5" after Dash.

### Item 11: portraits (tester-kinds, Kind One, Floating Numbers on)
- Red fill rises from the bottom of the portrait as vitality is lost (52 -> 30: about 40% red) (i11a, i11c). PASS.
- White chunk on the vitality bar for ~0.8 s after each hit, then it settles (i11c). PASS.
- Floaters: "-2" above the token on every mine. EVERY kind drew the same red (#b02c0b measured): fire, cold, electrical, sonic, energy, light_side, dark_side, universal; ion/unstoppable/piercing not captured cleanly (i11d). **FAIL**: no per-type colour for hazard damage. (Untested: weapon damage of non-plain types — none of my beds has one.)
- Enemy wounds float nothing: hits on droids showed no number (all fights). PASS.
- Conditions: stunned, slowed, held, paralysed, shaken, panicked, cowering show K2 icons (skull variants, the slowed cube, the held icon); sickened, entangled, dazed, blinded show by name; every icon names itself on hover ("stunned", "slowed", "held", "paralysed", "shaken", "panicked", "cowering"; names hover as "dazed" etc.) (i11a, i11b). PASS. An enemy card also shows the slowed icon (i09g).
- **Item 11: PASS except floater colour by type.**

### Item 12: walking: tokens slide square by square (my token between squares mid-step at 0.1 s frames, i12a; 15 fps tracking shows the droid passing intermediate positions 10.0-10.6 s and 13.3-13.8 s). PASS for sliding. L/staircase approach: in tester-lshape the droid at (5,0) moved down column 5 then... tracked positions (in quarter-scale px) go (272,78)->(272,106) then (272,105)->(272,118): straight down only, then it stopped; no L observed in this bed (its route had no turn). NOT OBSERVED.

### Item 13: regression: OA walk-up none / step-away one (item 1 runs); log column (all fights); flanking ("· Flanking +2", Rx runs); Continue after F4 + kill: back on (6,0) (i13); four-way (numpad unbound, all routes orthogonal); Escape+Escape+F4 twice rewrites one quick.mark (21:02:58, 21:03:07). PASS.
