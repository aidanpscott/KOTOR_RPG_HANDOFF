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
