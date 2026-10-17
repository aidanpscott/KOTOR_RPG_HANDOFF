# TEST 184 running log (draft, text only)

Started 2026-10-17. Tester, Xvfb :2, own data dir, no K2, no BG3. I never ran on :97, so Coder's 10-second run there did not touch my work.
Read first: rules/K2-PARITY-CHARGEN-PT2752.md (33 rows, 7 deliberate differences); k2-live has 47 pictures.
Known, per MAIN (recorded if seen, not new findings): End Turn off screen at 1920; droid bar shows Force/meditation; "N rules ... not checked"; Random Name ignores gender; Endar Spire trooper one-shots a level-1 Consular; "?" feat icons; "HK-" twice in the designation refusal; "Medical Supplies" wraps; same closing Story line; stale Load-list thumbnail.

## Build
- App dbc037c (gate "FOR TESTER — CORE at dbc037c", CORE 3788 pass), git archive to ~/kotor-tester/builds/test184. Built through the lock: 10.2 s. pubspec.lock unchanged.
- Lodestar 340b4cb776372a5262315c2f68868eec757e51e0 = lock = compiled. Lens 5fe60a9c2be41852fd8818c1ca579a2077808d79 = lock = compiled. Loom: no entry in the lock.
- Shelf 0cf2242 (= origin newest). check_shelf: 31 rules files, 118 blueprints, identical. tool/env.sh sourced. Bundle launched with & outside the lock.

## Items

### Organic chargen (Store Bed, Custom: Human Male, picks Persuade/Stealth +2, racial skill Persuade; Jedi Consular; Taris · Upper City · Appraise; Noble; Merchant; STR/DEX/CON 12 INT 10 WIS 8 CHA 18; "Org Four")
1. Entry: Quick Character (dimmed; pane "Select this option to have your character's creation handled for you. You will only choose your character's appearance and name. / Not available yet: no class has a recommended build written, so there is nothing to fill it in from."), Custom Character, Premade Character (dimmed, "0"); no subtitle (i01a, i01b). The bottom button is "Back" (not "Cancel"); it goes to the package menu (i01c). PASS.
2. Species: description pane holds the facts; Human "Skill Bonuses — 2 of 2" with two different picks; NEW: a "Racial Skill — 0 of 1" pick appears after the Human's two (and for the Twi'lek: Persuade/Streetwise); Nautolan and Twi'lek show no empty "Low-light vision" heading (i02c, i02d). Cancel -> entry (i02b). PASS. Notes: the Species help box showed again on the second Custom in the same session; Cancel from Class back to Species forgot the species and picks (back on Aqualish).
3. Class: one face, "CHOOSE YOUR CLASS", our list left, the pane (tier, force powers, description) (i03a). Cancel -> Species (i03b). PASS. (Droid's Force-class reason: in the droid run.)
4. Hub: only the current step opens; Back dimmed at the start, then undoes the last step (Portrait reopened) (i04c); Cancel asks "All settings for this character will be lost. Proceed?" OK / Cancel (i04b); order Gender, Portrait, Origin, Background, Attributes, Skills, Feats, Powers, Equipment, Name, Play (i04a). PASS. (The order says Gender/Voice: the human shows "Gender".)
5. Steps:
   - Portrait: arrows, "Portrait", "1 of 31", male faces only (i05a). PASS.
   - Origin: "homeworld" list, "Aptitude" box; stage two (upbringing) has Back / OK (i05b, i05c). PASS.
   - Background: title BACKGROUND (i05d). PASS.
   - Attributes: **does not match abchrgen.** K2 (k2-live/15): Point Cost box, Remaining Points box, each row modifier + score + arrow buttons, a description pane on the right, the K2 frame. Ours: a plain list (name, minus/score, "-", total, bonus) under "Remaining Points 30 of 30", no Point Cost, no description pane even on hover (i05e, i05f). The plus is removed when no points remain (i05f). FAIL (layout).
   - Skills: rows are a plain list, not K2's boxed rows with Point Cost and Class/Cross-class boxes (k2-live/23); ours puts "Point Cost 1 · maximum rank 4" and "Aptitude: homeworld, profession" in the pane. Plus REMOVED at max rank (Appraise 2, Persuade 2; Stealth 0 with no plus) (i05h). Help box: "...With aptitude a rank costs 1 skill point; without, 2. Maximum rank in a skill with aptitude is character level + 3; without, half that. A +2 from a species or a homeworld does not raise it." (i05g). PARTIAL (rows not K2's; cap rule PASS; the help says "+2 does not raise it" rather than "ranks plus species and homeworld bonuses").
   - Feats: three-tier grid with arrows, Remaining Feats 1 of 1, Description, Add Feat; the help box on entry; Add Feat -> 0 of 1 (i05i, i05j). "?" icons (known). The "granted" message (K2 42258) did NOT appear. PARTIAL.
   - Powers: "CHARACTER GENERATION / POWERS", "Remaining Powers 2 of 2", Select, Select again gives it back (1 of 2 -> 2 of 2) (i05k, i05l). Refusals: no refused power is shown at all — powers with gates (Battle Meditation "Character Level 6", Breath Control "Jedi" ...) are left out of the list instead of showing their reason in the pane (i05m). Force Crush (30 FP, tier 1, no prerequisite in powers.toml) can be taken at level 1. PARTIAL.
   - Equipment: "Armor Padawan Robe", "Weapons Training Lightsaber", "kit Adrenal Stamina · 1 tier-1 saber upgrade", "Medical Supplies" (wraps — known), "Boots", "Credits" (i05n). "kit" is lower case; no "Repair" or "Clothing" row for a Consular (expected for a Soldier). PASS with the "kit" note.
   - Name: popup over the hub, pre-filled ("Cassar Tarkis"), Random Name, Cancel / OK; then YOUR STORY (Try another, CLEAR, Back, OK) (i05o, i05p). PASS.
6. Help boxes: Species, Origin, Background, Attributes, Skills, Feats, Powers (K2's 41887 text), Equipment, each on first open; none on Gender, Portrait, Name. PASS (note the Species repeat above).
7. Coined-looking words outside panes/help: Species "Subrace", "Skill Bonuses — 0 of 2", "Racial Skill — 0 of 1"; Origin "homeworld", "upbringing"; Background "profession" tab; Attributes unlabeled "-" column; Equipment "kit", "1 tier-1 saber upgrade"; hub summary labels "homeworld", "aptitude", "upbringing", "gender", "skills", "abilities", "profession", "6 skills, 20 ranks"; Story "assembled from your choices" (gone? not seen this time), "Try another", "CLEAR".
9. Play: Org Four enters Store Bed (force 11 of 11). F4, kill -9, Continue: same square, portrait, and Persuade Rank 2 / Bonus +6 / Total 8 (i09b). PASS.
10. Sheet Bonus column: Org Four Appraise 2/+2/4, Persuade 2/+6/8 (Human +2, CHA +4; total above the cap of 4), Stealth 0/+3/3, Streetwise 0/+4/4 (i09a). Cap Three: Appraise 2/+2/4, Persuade 0/+6/6, Stealth 0/+3/3, Streetwise 2/+4/6 (i10). PASS (Stealth is +3, not MAIN's +2: Human +2 plus DEX 12's +1).
