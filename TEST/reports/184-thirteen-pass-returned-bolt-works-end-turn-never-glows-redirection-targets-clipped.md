# TEST 184: chargen against K2, the returned bolt (PT-2753), naturals, companion deflection, party rest and regression

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-184/` (MAIN_WORK `746eb9bf`), one prefix per item. The step-by-step log is `TEST/reports/184-running-log.md`.

## Build

App `dbc037c` (the gate read "FOR TESTER — CORE at dbc037c", CORE 3788 passed), git archive to `~/kotor-tester/builds/test184`. Lodestar `340b4cb776372a5262315c2f68868eec757e51e0` = lock = compiled. Lens `5fe60a9c2be41852fd8818c1ca579a2077808d79`. Loom has no entry in the lock. Shelf `0cf2242`; check_shelf clean (118 blueprints). `tool/env.sh` sourced. The build (10.2 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. The bundle was launched outside it. Fresh fixtures: chargen characters (Org Four, Cap Three, RX-184) and authored saves (Bolt Redir, Bolt Defl, Rest Party, Two Four). New local bed `tester-bolt`: a 12x5 range, three gunmen with blaster rifles (1d12), a cover square at (8,3) beside the (9,3) gunman, and Vela (a Consular 6 henchman knowing Deflection).

## Summary: thirteen pass, three partial, one fail, one recorded

| # | Check | Result |
|---|---|---|
| 1 | Entry screen | **PASS**: the bottom button reads "Back" and returns to the package menu. Quick is dimmed, with its reason in the pane |
| 2 | Species | **PASS**: a new "Racial Skill — 0 of 1" pick. Neither Nautolan nor Twi'lek shows an empty "Low-light vision" heading. Notes: the help box came up again on a second visit, and Cancel from Class back to Species forgot the species |
| 3 | Class | **PASS**: one face, our list, the pane. A droid chassis bars Force classes with "a droid chassis holds no Force class" |
| 4 | Hub | **PASS**: only the current step opens. Back undoes the last step. Cancel asks K2's "All settings for this character will be lost. Proceed?" |
| 5 | Each step | **PARTIAL**: Portrait, Origin, Background and Name PASS. **Attributes FAIL** against abchrgen: no Point Cost box, no description pane, a plain list. Skills: the plus goes at the cap, but the rows aren't K2's boxed rows. Feats: no "granted" popup for the Consular (the droid got one, for Jury Rig). Powers: refused powers are left out of the list, not shown with their reason, and Force Crush (no prerequisite in powers.toml) can be taken at level 1. Equipment: "kit" is lower case, plus "1 tier-1 saber upgrade" and, for the droid, "1 Parts" |
| 6 | Help boxes | **PASS**: one on the first visit to each step. They show once per app session, not once per character |
| 7 | Home-made sentences | **Recorded**: the list is in the running log (for example "Racial Skill — 0 of 1", "homeworld", "upbringing", "profession", "kit", "6 skills, 20 ranks", "Try another", "CLEAR") |
| 8 | Droid name refusal | **PASS**: refused as you type, and every refusal ends with the whole rule. '"HK-47" belongs to somebody — pick another.' Ctrl+A and BackSpace don't reach the field |
| 9 | Play / save / load / Continue | **PASS**: after F4, kill and Continue, the square, the portrait and Persuade 2/+6/8 are all kept |
| 10 | Sheet Bonus column | **PASS**: Cap Three: Persuade 0/+6/6, Appraise 2/+2/4, Streetwise 2/+4/6, Stealth 0/+3/3 (Human +2 plus DEX +1) |
| 11 | Continue mid-fight | **PASS** for both F4 and Escape > Save: after a kill -9, "the fight resumes — round 2, Rest Party's turn" with the same health, Force, initiative and spent action. The combat log comes back empty |
| 12 | End Turn glow | **FAIL** at 1920x1080 and at 1280x720 (fresh window): a fresh turn, an action spent, and 0 moves with the action spent all draw End Turn the same, pixel for pixel. End Turn is only reachable by scrolling the hotbar sideways, at both sizes |
| 13 | AUTO Kael, Rx Two Triggers | **PASS**: he closes, swings at the Backer every round ("Kael attacks Backer : *hit* : (8 + 4 = 12)"), takes his opportunity attacks, and follows it across the room to the kill |
| 14 | The returned bolt | **PARTIAL**: a success rolls a new hit with my ranged bonus, and the damage fits half the bolt with a minimum of 1. Deflection offers only the shooter. Redirection offers every enemy, but **the buttons are clipped to "Yes — back"**. The cover target and "already down" were not confirmed. Lines below |
| 15 | Naturals | **PASS** for attacks, the returned bolt included. The hit chance is clamped to 5–95% ("95% (needs 2+)" seen). Saves weren't seen in play, and the code words them differently (below) |
| 16 | Companion deflection | **PARTIAL**: MANUAL with Ask: a box naming Vela, paid from her own pool. MANUAL with Always: no box, and the bolt goes back at the shooter. **AI not observed**: AUTO Vela charged and every shot at her missed |
| 17 | Party rest | **PASS**: Vela goes 9 → 40 of 40 and Force 7 → 51 of 51; I go 50 → 146 of 196 (a day's rest) and Force 10 → 97 of 97. Kept after F4, kill and Continue |
| 18 | Quick regression | **PASS**: four-way movement (the numpad does nothing), the path line, opportunity attacks, Ask/Always, "there is nothing to dash for", and Escape then F4 rewrites the one quick save. F4 does nothing while the Escape menu is open |

## Findings, most important first

1. **End Turn never glows** (item 12). `play_screen.dart:21339` lights it only when `!budgets.anythingLeft`. The "gear" pip stays lit in every state I saw, so "anything left" probably never goes false. It's also off the row at both sizes (the 1920 case is known).
2. **Redirection's target buttons are clipped** (item 14). The label is "back at <name>, <hit chance>" (`play_screen.dart:9754`), but each button shows only "Yes — back", so the player can't see where the bolt will go or its chance. Hovering shows nothing. Separately, three enemies all called "Gunman" couldn't be told apart even unclipped. The third button hit the (8,0) gunman, not the shooter, so the choice does work.
3. **Natural saves are worded differently from attacks** (item 15). `k2_feedback.dart:121` writes "automatic success" (K2 1415) on a 20 and "automatic failure" (our term) on a 1, where attacks read "Automatic Hit!" / "Automatic Miss!". MAIN said saves the same: for a ruling.
4. **Chargen differs from K2** (item 5): the Attributes layout, Skills rows, refused powers left out of the list, Force Crush at level 1, and the Equipment wording.
5. Small: a companion's MANUAL/AUTO label can't be changed during a fight. After a deflect, the status line names the terms "attack 4 + Strength 1", while the log reads "Vela deflects projectile with 20 + 5". The rest status line names only the player. The combat log is empty after a mid-fight Continue.

## Item 14 and 16 log lines, verbatim

Redirection (Bolt Redir, Ask, third button):
- `Gunman attacks Bolt Redir : *hit* : (15 + 3 = 18)`
- `Deflection Breakdown: Bolt Redir deflects projectile with 12 + 16 = 28 vs. attack 18`
- `Deflected!`
- `Bolt Redir sends the bolt back at Gunman`
- `Bolt Redir attacks Gunman : *hit* : (16 + 14 = 30)`
- `Bolt Redir damages Gunman for 6 damage`

+14 is my ranged bonus (BAB 12 + DEX 2). Returns dealt 1, 3, 4, 5 or 6 against a 1d12 rifle; one Deflection return dealt 8, probably a critical bolt. The code halves the rolled bolt (`attack.dart`, "half the bolt's N", not shown on screen). A natural 1 on a return: `Bolt Redir attacks Gunman : *miss* : (1 + 14 = 15 Automatic Miss!)`. A failed deflect: `... deflects projectile with 1 + 16 = 17 vs. attack 19`, then `Gunman damages Bolt Redir for 2 damage`. After 8 casts, Force was 1 of 73 "exhausted from 97" (each cast lowers the ceiling by 3).

Deflection only (Bolt Defl, Ask): "Force Deflection / Gunman fires at you / 6 Force points · 97 left · spent only if the shot would hit / back at Gunman, 95% (needs 2+)", with one Yes. All 30 boxes named the shooter.

Vela, MANUAL, Ask: "Force Deflection / Gunman fires at Vela / 6 Force points · 51 left · …  / back at Gunman, 80% (needs 5+)". 51 is her pool; mine was 1. Then:
- `Gunman attacks Vela : *critical hit* : (20 + 3 = 23 : Threat Roll: 18 Automatic Hit!)`
- `Deflection Breakdown: Vela deflects projectile with 20 + 5 = 25 vs. attack 23`
- `Deflected!` / `Vela sends the bolt back at Gunman`
- `Vela attacks Gunman : *hit* : (6 + 5 = 11)` / `Vela damages Gunman for 6 damage`

Vela, MANUAL, Always: no box, and one return killed the shooter (`Vela damages Gunman for 6 damage`, `Gunman dies`). Her spends are in the save as `power.cast` with `subject: vela.range.01`.

Not reached: a cover target's chance (the clipped buttons hide it, and the log prints no Defence), and a target already down (no "who is already down" line in about 40 rounds).

## How it was run

Fights were run from pre-fight quick saves, with a loop that answers each box and saves the log panel whenever it changes; I merged those snapshots with OCR. Redirection cycled its three buttons. The Rest Party save was authored hurt and drained through `encounter.ended` events. Deflection was set to Ask through settings.json with the app stopped. Each chance result here comes from several rounds, not one replayed roll.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
