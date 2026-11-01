# TEST 218: level-up skills, Trask fighting, the Experience line, Sith names after a load, and "if_ at all."

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-218/` (MAIN_WORK `2e72d2e4`).

## Build

- **App**: main `6640492`, a worktree beside my clone. `gate.py --at 6640492`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 6640492, 5415 tests, 0 failed"; ARCHIVE last green at 6640492. Lodestar `2d438df` = lock = compiled. Built through the lock (55.7 s, a cold cache); git status clean.
- **Settings**: defaults. **Shelf** `411c1e2`, synced.
- **Characters**: both remade through chargen in Endar Spire — The Opening; the 216 saves weren't touched.
  - **Open Soldier 218**: Human Soldier, Taris / Upper City Persuade / Noble / Acolyte, Str 16 Dex 14 Con 14 Cha 12. Skills at creation: Alertness 4, Athletics 2, Awareness 2 (both capped at 2), 4 points left unspent.
  - **Frail Sage 218**: Bith Jedi Consular, the same origin, Con 8, 5 vitality. Skills at creation: Alertness 4, Archaeology 4, Awareness 4, 12 points left unspent.
  - Leaving points unspent gives K2's "You have not spent all of your skill points. These will be saved and you may spend them the next time you gain a level." Both carried into the level-up (4 + 3 = 7; 12 + 6 = 18).

## Summary: all pass; no findings, no small items

| # | Check | Result |
|---|---|---|
| 1 | Level-up skills | **PASS**. At the panel's level-up the Skills page opened on the held ranks, not 0. Open Soldier: Alertness 4, Athletics 2, Awareness 2, 7 points; I raised Alertness by 1 and left the rest. Sheet after: Alertness 5, Athletics 2, Awareness 2, Acrobatics 0. Frail Sage: page opened on 4 / 4 / 4 with 18 points; I raised Awareness by 1. Sheet after: Awareness 5, Alertness 4, Archaeology 4, Acrobatics 0. A companion's level-up isn't reachable: Trask reads Experience 3000, Needed 3000, with no level waiting |
| 2 | Trask fights | **PASS**. He's in every fight's initiative ("initiative — Open Soldier 218 15 · Trask Ulgo 15 · Sith Soldier 6 · Sith Soldier 2"), and on his turn (he's MANUAL, "Trask Ulgo is waiting on you") a click on a Sith attacks: "Trask Ulgo: Blaster Pistol · rolled 12 … hit · damage 5". The log has him killing Sith in the hall ("Trask Ulgo damages Sith Soldier for 6 damage", "Sith Soldier dies") and in Frail Sage's room 3. On the bridge Open Soldier fell to "0 of 20" with Trask at 21 of 22: no defeat box; the fight went on to "Trask Ulgo is waiting on you" |
| 3 | Experience line | **PASS**. After the panel, Feedback reads "Experience: 1000." |
| 4 | Sith names after a load | **PASS**. A quick save after the hall's deaths, loaded: the Combat log reads "Sith Soldier falls." on every line, no tags |
| 5 | "if_ at all." | **SEEN twice, steps below** |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 55 ("reg218"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 130 of 196) |

## 5. "if_ at all." — steps

Both times on the summary page that chargen's Play opens (the story box top left), before OK:

- **Frail Sage 218** (`t218-story-if_.png`): Library → Endar Spire — The Opening → New Game → Custom Character → Species Bith (no skill picks follow) → Class Jedi Consular → Gender Female → Portrait default → Origin: Taris, Upper City Persuade, Noble (each OK on its default) → Background Acolyte (default) → Attributes Str 12 Dex 14 Con 8 Int 12 Wis 16 Cha 16 → Skills → Feats → Forms → Attacks → Powers → Equipment (the Acolyte robe) → Name "Frail Sage 218" → Play. The box reads: "Ask where Frail Sage 218 is from and you get Taris, eventually. Ask what they did there and you get Acolyte, immediately. The Noble part comes last, if_ at all. Jedi Consular: The Force is the weapon."
- **Open Soldier 218** (`t218-story-la_st.png`): the same origin and background, Human Soldier, name "Open Soldier 218". The underscore moved: "The Noble part comes la_st, if at all."

The underscore sits in a different word for a different name length, the same in both runs for the same steps. In 216 Frail Sage (name 10 letters) and Open Soldier (12) both read "if_".

## Seen, not filed

- The bridge Sith's confirmed critical did 2: "Sith Soldier attacks Open Soldier 218 : *critical hit* : (20 + 0 = 20 : Threat Roll: 15 Automatic Hit!)" then "Sith Soldier damages Open Soldier 218 for 2 damage" (twice). This is the 216 bridge 2 that stayed unseen.
- Trask is MANUAL, so on his turns my own keys move him; a fight script that bumps a direction walks him away. Not a defect.

KNOWN, not filed: Sith don't start fights on sight; an out-of-range party member isn't pulled in; the Acolyte robe upgrade does nothing.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
