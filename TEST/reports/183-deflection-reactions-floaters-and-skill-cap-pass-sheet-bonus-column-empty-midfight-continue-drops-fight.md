# TEST 183: the TEST 182 fixes, the skill cap, Human skill bonuses and chargen wording

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-183/` (MAIN_WORK `5ea74389`), one prefix per item. The step-by-step log is `TEST/reports/183-running-log.md`.

## Build

App `b557d8a` (FULL stamp per Coder), git archive to `~/kotor-tester/builds/test183`. Lodestar `a114e1bbd9bed98ce3917e9c484bb82aac9ee80d` = lock = compiled. Lens `5fe60a9c2be41852fd8818c1ca579a2077808d79` = lock = compiled. Loom has no entry in the lock. Shelf `1626462` (= origin, with the four rx beds); check_shelf clean (118 blueprints). `tool/env.sh` sourced. The build (10.7 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. The bundle was launched outside it. Fresh fixtures: authored Jedi (Deflection only; Deflection + Redirection), saves for the four rx beds, `kind-183`, and chargen characters.

## Summary: six pass, two partial, one fail, one recorded

| # | Check | Result |
|---|---|---|
| 1 | Force Deflection | **PASS**: 25 shots under Always: 19 missed, 6 would hit, 3 deflected, 3 landed. Each try has its own "Deflection Breakdown: … deflects projectile with 20 + 13 = 33 vs. attack 17" line; a success reads "Deflected!". Force 97 → 61 = 6 × 6, spent on every would-hit shot. Knowing both: the rows say Redirection is used instead; play asks Redirection (12 points), and its rolls carry the +3 (16 vs 13). **For a ruling**: a redirected bolt does no damage to the shooter (the trooper stays 18 of 18; only the status line adds "and sent back") |
| 2 | MANUAL companion | **PASS**: Kael's pip was lit first. "Opportunity attack / Backer leaves Kael's reach / one reaction · 1 left / 65% (needs 8+)". Yes swings, No doesn't, Always swings with no box, Never does nothing. AUTO Kael isn't asked (my box only) |
| 3 | Floater colours | **PASS**: fire #ea8027, cold #86caed, electrical #e7e057, sonic #a190f2, ion #4a93ee, energy #4bd8bb, light_side #f6e09d, dark_side #c64cce, universal #ea769c, unstoppable #add336; plain (piercing) K2's red #b72d0a. All match Coder's table |
| 4 | Two triggers | **PASS**: two boxes before the Backer moves, one at a time, in initiative order (Kael 18, then me 10) |
| 5 | Gone target | **PASS**: both boxes come first; Kael's swing kills the Frail Backer, mine is dropped, and the fight ends cleanly |
| 6 | Key legend | **PARTIAL**: the key line is gone and the hotbar hides under Equip. End Turn reads lit with nothing left, but I couldn't see it differ from a fresh turn ("glows" not confirmed). Board height not measured |
| 7 | Skill cap | **PASS** in chargen: (a) Taris + Appraise aptitude stops at rank 2, the plus dims, hover "Rank 2 plus a bonus of 2 is the maximum of 4. A +2 from a species or a homeworld does not raise it."; (b) a +2 without aptitude, cap 2, no ranks; (c) Twi'lek from Ryloth, Persuade: "Rank 0 plus a bonus of 4 is the maximum of 4", no ranks; (d) CHA 18 doesn't block Streetwise ranks; (f) the cost line reads as ordered. (e) level-up was not run. The sheet total going above the cap can't be shown: see finding 1 |
| 8 | Human skill bonuses | **PARTIAL**: "Skill Bonuses — 0 of 2"; OK waits for two; a re-click un-picks it; a third isn't taken; both count against the cap and are saved (`skill_bonuses: ["persuade","stealth"]`). **FAIL**: not on the sheet (Bonus 0) |
| 9 | Chargen wording | **Recorded**: the Origin box says "Aptitude / pick one — it gains +2 and aptitude". Other labels are listed below |
| 10 | Regression | **PASS** except one: the prompt under Ask/Always/Never, Deflection defaults to Always, pips, tokens slide (and the Walker turned the corner on Rx L Approach), step away gives one opportunity attack, Escape+F4 gives one save. **FAIL**: Continue after a mid-fight F4 drops the fight. Stunned and hotbar refusals were not re-run (they passed on 7a863fc) |

## Findings, most important first

1. **The Abilities sheet's Bonus column ignores species, homeworld and ability bonuses.** Cap Three (Human, Persuade +2 and Stealth +2 chosen; Taris Appraise +2; CHA 18) in play shows Persuade 0/0/0, Stealth 0/0/0, Appraise 2/0/2, Streetwise 2/0/2 (`i08c`). Item bonuses do reach that column (TEST 179's Silenced Motivator). So the cap counts the +2s, but the sheet and possibly the rolls don't show them.
2. **Continue after a mid-fight F4 and a killed app drops the fight.** Rx L Approach, round 4, F4, kill, Continue: I'm on my square, but there's no fight and the Walker is back at its start (`i10b`). Loading the same Quick Save resumes round 4 (`i10c`). The Auto Save row shows the Quick Save's time, but `autosave.world.json` is from before the fight.
3. **A redirected bolt isn't sent back** (item 1): no damage to the shooter, and "Deflected!" is the only log line. MAIN to rule.
4. **AUTO Kael backs off and swings at nothing every round** (Rx Two Triggers): "Kael backs off 2 squares — 1 to 3", then for 14 rounds "Kael: unarmed · out of reach — unarmed reaches 1 square and Backer is 5 away".
5. Small: "100% (needs 1+)" for a swing a natural 1 misses. The Redirection box is asked before every shot, misses included (Force is only spent on a would-hit shot). A resized running window doesn't relayout (from TEST 182).

## Chargen labels, verbatim (item 9, for MAIN)

- Hub: "steps — nine of ten" (unchanged as steps were done); "powers — absent — this class grants none".
- Origin: "homeworld", "271 worlds", "Upbringing ▸". Upbringing: "grants nothing — flavour only", "◂ change world".
- The hub step reads "Background" but its screen says "BACKSTORY". Also "profession", "it grants one of these, and you choose which", "a tier above", "one starting item, one band above", "Neither is picked here. You choose at Equipment …".
- Equipment: "This gear is worth 320cr.", "empty by design — implant · head · hands · arms · belt", "This profession grants an aptitude in Appraise and no starting item, so there is nothing to weigh it against." (The Backstory step said you choose at Equipment.)
- Feats: an unheaded "+2" column; "195 feats are granted, not bought  They arrive with your class as you level and cost nothing, so none of them is offered here."
- Name/Story: "A name is required. Everything else on this step is not.", "Story ▸", "YOUR STORY", "assembled from your choices", "Try another", "CLEAR", "BACK" (mixed capitals).
- Twi'lek: a "Low-light vision" heading with no text. Attributes: "A species adjustment applies AFTER generation — it attaches to what you bought and never touches the budget."
- Not seen: the racial aptitude pick on the Species step (ruled by MAIN, not yet built in b557d8a).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
