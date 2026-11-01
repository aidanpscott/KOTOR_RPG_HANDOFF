# TEST 216: the robe gate for non-Jedi, the Power Attack critical, and Endar Spire — The Opening

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my bed are in `KOTOR_RPG_MAIN_WORK/media/screens/test-216/` (MAIN_WORK `13ee9945`). The step-by-step log is `TEST/reports/216-running-log.md`.

## Build

- **App**: main `c124f76`, a git worktree beside my own clone. `gate.py --at c124f76`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at c124f76, 5395 tests, 0 failed"; ARCHIVE last green at c124f76. Lodestar `69d8d69` = lock = compiled. The build (10.2 s) went through the lock, and git status was clean.
- **Settings**: defaults.
- **Shelf** `701a740`, synced; check_shelf clean (33 rules files, 125 blueprints).
- **Characters for the opening**:
  - Open Soldier, a Human Soldier (d10), 12 vitality;
  - Frail Sage, a Bith (−2 Constitution) Jedi Consular (d6), Constitution 8, 5 vitality.
  - Both took the Acolyte background.
- **Beds**: `author_tester_test215_saves.dart` rerun for a fresh Power One. My own Robe Soldier (Soldier 10, no Jedi Defense, carrying the four robes) in tester-215. Reused Robe Plain, Dice One and Icon Nine.

## Summary: the ordered items pass, except the bridge's 2 on a critical (not seen); two findings outside the order, two small items

| # | Check | Result |
|---|---|---|
| 1 | Robes | **PASS**. Robe Soldier is refused Crado's, the Matukai Apprentice, the K1 Jedi Knight Robe and the Padawan Robe, each with K2's line and "Jedi Defense" under it. Robe Plain's Feats now list Jedi Defense, and she still wears the robes |
| 2 | Power Attack critical | **PASS**. "damage 40 — 3d10 1+5+5 + 3d6 5+4+2 + Strength 6×3 × 3 critical" |
| 4 | Library | **PASS**. The first tile is the opening, with the ordered card text. "Test beds" follows, every bed sits after it, "Tester Visual" is among them, and there's no Base Rules tile |
| 5 | Quarters | **PASS**. "We've been ambushed…", "Who are you?", "Now hurry up…". "Oath or no oath…" brings "Don't be stupid!…", then "We should stick together…"; "Okay, let's go help Bastila!" goes straight to "We should stick together…". Feedback: "Trask Ulgo has joined the party." The footlocker holds Medpac ×2 |
| 6 | Rooms 3, 4, hall | **PASS**. The closed door reads "That cannot be done while there are enemies nearby." Shots read "− weapon 5", and the hit did 0. Each east door opened once its room was clear. Room 3 had 15 and 1, room 4 had 12 and 12, the hall had three at 15. Each room has a west door; I didn't walk back through one |
| 7 | Security panel | **PASS**. "We'll be fighting in close quarters on the bridge. …", then "Okay." The sheet read Experience 1000 and Needed 0, and both characters leveled to 2 there. In the fight: "the Security Panel is in the way". Small 1 is below |
| 8 | Bridge | **PARTLY**. Two Sith with the One damage blade, and each hit did 1. No confirmed critical came in about 14 swings, so the 2 is not seen |
| 9 | Survival | No moment either character could have died before acting. Frail Sage took 0 from every blaster and 1 per blade hit. Open Soldier died only because I passed about 30 bridge turns on purpose |
| 10 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 53 ("reg216"), Escape then F4 (one quick save), Load, and a fight won |

## Findings

1. **A skill raised at level-up loses its creation ranks.** The level-up Skills page starts every skill at 0, and whatever it sets replaces the rank bought at creation.
   - Frail Sage's sheet before the panel's level-up read Alertness 4, Awareness 4, Archaeology 4.
   - At the level-up I added 3 to Alertness and 1 to Awareness; Awareness's plus went dim at 1.
   - Afterwards: Alertness 3, Awareness 1, and Archaeology, untouched, still 4.
   - Open Soldier did the same: the three skills she raised each read rank 1, while untouched Acrobatics kept 2.
2. **Trask never takes part in a fight.**
   - His portrait hover reads "Trask Ulgo · Soldier · 3 · Vitality 22 of 22 · MANUAL".
   - He never appears in a fight's initiative or strip and never acts, in all four fights on both runs. Room 3's initiative was "Open Soldier 6 · Sith Soldier 4 · Sith Soldier 2".
   - When Open Soldier fell on the bridge, the box said "YOUR ENTIRE PARTY HAS BEEN KILLED." and "YOU FALL, AND NOBODY IS LEFT STANDING", with Trask at 22 of 22 beside her.
   - Unverified hint: the opening's `trask.crtr` has `[vitality] override = 0`.

## Small

1. After the panel's +1000, Feedback reads "Experience: —." with no number. The sheet does show 1000.
2. After a load, the Combat log names the fallen hall Sith by tag ("sith-soldier.hall.03 falls."). The fight itself said "Sith Soldier falls."

Seen, not filed:
- No Sith starts a fight. Open Soldier walked from room 3's west door past both Sith to the east door, and the fight began only when I bumped one.
- The Acolyte's "Padawan Robe → Jedi Robe" pick at Equipment never reached Open Soldier: her bag held only the Blaster Rifle, and Body offered only Clothing. Frail Sage started wearing the robe.
- Both backstories read "The Noble part comes last, if_ at all."
- My own Tester 215 package has no shelf line, so it sits before "Test beds". It's my package, not the Shelf's.

KNOWN, not filed: the blasters doing 0; Trask has no portrait; Loom's missing controls. RULED, not filed: Strength 6 on damage against 4 on attack for a one-hander (PT-2222).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
