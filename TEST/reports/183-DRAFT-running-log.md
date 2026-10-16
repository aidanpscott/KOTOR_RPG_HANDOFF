# TEST 183 running log (draft, text only)

Started 2026-10-16. Tester, Xvfb :2, own data dir, no K2, no BG3. (Coder may be capturing K2 on the owner's desktop: not my display.)
Read first: CODER "TEST 182 FIXES BUILT" (ed8fc9d: deflection rolls logged 42417, "Deflected!"; Redirection replaces Deflection, both rows say so; manual companion not reproduced, check Kael's pip first; mine floaters by kind; four Shelf beds rx-stun-bed, rx-two-triggers, rx-gone-target, rx-l-approach), PT-2752 skill cap (built f4176bc; rulings; b557d8a: K2 verified rank cap, Human's two +2s on the Species step as two different skills).

## Build
- App b557d8a (FULL stamp per CODER: 2561 pass), git archive to ~/kotor-tester/builds/test183. Built through the lock: 10.7 s. pubspec.lock unchanged.
- Lodestar a114e1bbd9bed98ce3917e9c484bb82aac9ee80d = lock = compiled. Lens 5fe60a9c2be41852fd8818c1ca579a2077808d79 = lock = compiled. Loom: no entry in the lock.
- Shelf 1626462 (= origin newest; holds rx-stun-bed, rx-two-triggers, rx-gone-target, rx-l-approach). tool/env.sh sourced. Bundle launched with & outside the lock.
- Authored (one locked dart run, specs notes/fixtures/specs183/): defl-183 "Defl Three" (Jedi Guardian 12, WIS 18, CON 30, Force Deflection only, Tester Save Bed), both-183 "Both Three" (same, Deflection + Redirection).

## Items

### Item 1: Force Deflection (Tester Save Bed, Sith Trooper with a Blaster Rifle; fresh authored Jedi Guardian 12)
- Defl Three (Deflection only, default Always), 25 rounds = 25 shots: 19 missed (no deflection attempt); 6 would hit: 3 DEFLECTED (rounds 16, 19, 23: "Deflection Breakdown: Defl Three deflects projectile with 20 + 13 = 33 vs. attack 17" / "Deflected!"), 3 LANDED (rounds 1, 13, 14: "... with 3 + 13 = 16 vs. attack 19" then "Sith Trooper damages Defl Three for 9 damage"; 4; 12). Every attempt has its own breakdown line; a success reads "Deflected!" (i01a). PASS.
- Force: 97 -> 61 of 91 ("exhausted from 97") = 6 attempts x 6, spent on every would-hit shot whether deflected or not, nothing on misses (i01b). Matches CODER's entry ("spent only if the shot would hit"). PASS.
- Gameplay page: Deflection row help "A ranged attack at you would hit: turn the bolt aside, for the power's Force points. / A Jedi who knows Force Redirection uses Redirection instead, and its row decides."; Redirection row "...turn the bolt aside, or send it back, for the power's Force points. / Used instead of Force Deflection by a Jedi who knows both: it is Deflection's upgrade, +3 to the roll." (i01c). Clicking a row's centre cycles it (as the arrows do); Default restored Ask / Always / Ask (i01d).
- Both Three (Deflection + Redirection, defaults): every shot asks "Force Redirection / Sith Trooper fires at you / 12 Force points · 97 left · spent only if the shot would hit" (13 boxes in 13 rounds, misses included) (i01e). Yes each time: rounds 11 and 12 would hit: "Deflection Breakdown: Both Three deflects projectile with 9 + 16 = 25 vs. attack 18" / "Deflected!" — +16 vs Deflection's +13, the +3 (i01f). Force 97 -> 73 = 2 x 12 (i01g). Play does what the page says. PASS.
- FINDING: a redirected bolt does nothing to the shooter: Sith Trooper 18 of 18 after two redirections (i01h); the log reads only "Deflected!", the status line adds ", and sent back" (attack.dart:1685 is text only). The row help says "send it back". MAIN to say whether Redirection should damage the shooter.
- Note: the box is asked before every shot, even ones that miss (Force is only spent on a would-hit shot).
- **Item 1: PASS** (redirection's return does no damage: for a ruling).

### Items 2 and 4: MANUAL companion and two triggers (Rx Two Triggers; authored Two Three; Kael MANUAL at (3,0), Backer (4,1); scripted replays from one pre-fight quick save, run/tworun.sh)
- Before the trigger Kael's sidebar shows "move 5 of 5" and his one reaction pip lit (i02a).
- Ask: when the Backer backs off, two boxes BEFORE it moves, one at a time, in initiative order (Kael 18, me 10): "Opportunity attack / Backer leaves Kael's reach / one reaction · 1 left / 65% (needs 8+)" (i02a), then "Opportunity attack / Backer leaves your reach / one reaction · 1 left / 80% (needs 5+)" (i04a). Yes, Yes: "Opportunity attack: Kael attacks Backer : *hit* : (8 + 4 = 12)" / "Kael damages Backer for 2 damage" / "Opportunity attack: Two Three attacks Backer : *hit* : (16 + 7 = 23)" / "Two Three damages Backer for 9 damage" (i02b). PASS (items 2 and 4).
- N for Kael, Enter for me: no Kael swing; mine lands (i02c). PASS.
- Always: no boxes, both swing; the log is identical, line for line, to the Ask-Yes-Yes run. Never: no boxes, no swings (i02d). PASS.
- AUTO Kael (Ask): only my box; AUTO Kael is not asked. But on his own turn (he acts first) he "backs off 2 squares — 1 to 3", so the Backer never leaves his reach; then every round "Kael: unarmed · out of reach — unarmed reaches 1 square and Backer is 5 away" for 14 rounds, never closing (i02e, i02f). FINDING (AI): an AUTO unarmed companion backs off and then swings at nothing every round.
- **Item 2: PASS** (MANUAL asked, names the companion, Yes/No/Always/Never); AUTO not asked (the decide-itself swing was shown in the TEST 182 addendum); the AUTO standing-off is a separate finding. **Item 4: PASS.**

### Item 5: gone target (Rx Gone Target; authored Gone Three; Kael MANUAL; Frail Backer 1 vitality)
- Both boxes come first, before anything moves, in initiative order: "Frail Backer leaves Kael's reach / one reaction · 1 left / 85% (needs 4+)" then "Frail Backer leaves your reach / one reaction · 1 left / 100% (needs 1+)" (i05a). Yes to both: Kael's swing kills it ("Frail Backer falls — Kael catches Frail Backer leaving — unarmed · rolled 12 ... hit · damage 2 ... -1 left · Frail Backer backs off 2 squares — 1 to 3 · Frail Backer goes down backing off"); my swing is dropped (no line for it); the fight ends cleanly (i05b). PASS (as CODER's bed note says: both asked first, the second swing dropped). My pip after it can't be read (the fight ended).
- Note: "100% (needs 1+)" while a natural 1 misses (the bed's own note says so): the chance reads 100% but is 95%.

### Item 3: floater colours (tester-kinds; authored Kind Three; Floating Numbers on; 10 fps capture, pixel average of the "-2" per mine)
- fire #ea8027 (table FF8A2A), cold #86caed (8FD8FF), electrical #e7e057 (F2E85A), sonic #a190f2 (A996FF), ion #4a93ee (4F9DFF), energy #4bd8bb (4FE6C8), light_side #f6e09d (FFE6A0), dark_side #c64cce (D04FD8), universal #ea769c (FF7FA8), unstoppable #add336 (B8E03A), piercing (plain) #b72d0a — K2's red (i03). Every kind its own colour, matching the table (anti-aliasing lowers the averages). PASS. (Weapon damage of a non-plain type: no bed.)

### Item 6: legend, End Turn, height, menus (tester-kinds fight with its sentry droid)
- No key line above the board or the hotbar ("f powers · c scan ..." gone); "defence base ..." line remains (i06a). PASS.
- End Turn: with move 0 and the action spent it is drawn lit (i06b, i06c); on a fresh turn it is drawn lit too, and I could not see or measure a difference (the bar shifts a few px between my frames, so my pixel samples were not like for like). NOT CONFIRMED — "glows when you've nothing left" not visibly distinct from its normal state.
- Board height: not measured (no like-for-like frame from 7a863fc to compare).
- Hotbar hidden under Equip in a fight (i06d). PASS.

### Item 7: skill cap (fresh chargen in Store Bed: Cap Three — Human (picks Persuade, Stealth), Soldier, Taris · Upper City · aptitude Appraise, Noble, Merchant, CHA 18; and a Twi'lek from Ryloth taken to the Skills step)
- (a) Appraise (homeworld +2, aptitude): + three times stops at rank 2 (12 -> 10 points); the plus dims; hover: "Rank 2 plus a bonus of 2 is the maximum of 4. A +2 from a species or a homeworld does not raise it." (i07a). PASS.
- (b) without aptitude, +2 present: Persuade and Stealth (Human +2s, no aptitude) cap 2: no ranks, plus dimmed; hover "Rank 0 plus a bonus of 2 is the maximum of 2. A +2 from a species or a homeworld does not raise it." (i07b, i07c). PASS. (This also shows the Human's +2s counting against the cap — item 8.)
- (c) Twi'lek ("Skill bonuses +2 Persuade, +2 Streetwise") from Ryloth with Persuade as aptitude: Persuade 0 ranks, plus dimmed, "Rank 0 plus a bonus of 4 is the maximum of 4. A +2 from a species or a homeworld does not raise it."; Streetwise (+2, no aptitude) dimmed too (i07g, i07h). PASS.
- (d) CHA 18 (+4): Streetwise (Cha, no aptitude, no bonus) takes 2 ranks to "Rank 2 is the maximum of 2." — the ability modifier does not block (i07d). PASS for chargen. The sheet total above the cap: NOT SHOWN — see item 8 finding (the Abilities sheet's Bonus column reads 0 for Streetwise; total 2).
- (e) level-up: not run (no level-up bed used this test).
- (f) cost line verbatim: "With aptitude a rank costs 1 skill point; without, 2 skill points. The maximum rank is 4 with aptitude and 2 without, ranks plus bonuses." (i07f). PASS.
- Rows show "2/rank · cap 2" / "1/rank · cap 4" and a reason under the name ("class", "homeworld · profession", "homeworld").

### Item 8: Human skill bonuses
- Species step, Human: "Skill Bonuses — 0 of 2" with all 23 skills as boxes (i08a). One pick: "1 of 2", OK dim; clicking the same skill again un-picks it (no double pick); two picks: "2 of 2", OK lit, the boxes read "Persuade +2", "Stealth +2"; a third (Awareness) is not taken (i08b). PASS.
- Counted against the cap: Persuade and Stealth capped at 0 ranks (item 7 b). PASS. Recorded: save has species-set skill_bonuses ["persuade","stealth"].
- **FAIL: not shown on the sheet.** In play, Abilities > Skills: Persuade Rank 0 / Bonus 0 / Total 0; Stealth 0 / 0 / 0; Appraise 2 / 0 / 2 (homeworld +2 missing); Streetwise 2 / 0 / 2 (CHA +4 missing) (i08c). The Bonus column does work for items (TEST 179: Silenced Motivator Stealth +2), so species, homeworld and ability bonuses are not reaching it.

### Item 9: chargen wording (first pass)
- Origin: the box reads "Aptitude / pick one — it gains +2 and aptitude" (i09a). PASS.
- Labels recorded verbatim, for MAIN (coined-looking or inconsistent):
  - Hub: "steps — nine of ten" (shown both before and after 6 steps were done), "powers — absent — this class grants none" (i09f).
  - Origin: "homeworld", "271 worlds", "Upbringing ▸"; upbringing page: "upbringing", "grants nothing — flavour only", "◂ change world" (i09b).
  - The hub step is "Background" but its screen title is "BACKSTORY"; "profession" tab; "it grants one of these, and you choose which", "a tier above", "aptitude in Appraise", "Neither is picked here. You choose at Equipment ...", "one starting item, one band above" (i09c).
  - Equipment: "This gear is worth 320cr.", "empty by design — implant · head · hands · arms · belt", "This profession grants an aptitude in Appraise and no starting item, so there is nothing to weigh it against." (contradicts the Backstory step's "you choose at Equipment") (i09e).
  - Feats: a "+2" column on most feats with no heading; "195 feats are granted, not bought  They arrive with your class as you level and cost nothing, so none of them is offered here." (i09d).
  - Name: "A name is required. Everything else on this step is not.", "Story ▸"; Story: "YOUR STORY", "assembled from your choices", "Try another", "CLEAR", "BACK" (capitals mixed with sentence case).
  - Species: Twi'lek "Low-light vision" heading with no text under it.
  - Attributes: "A species adjustment applies AFTER generation — it attaches to what you bought and never touches the budget."
