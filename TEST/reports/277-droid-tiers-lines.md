# TEST 277: moved lines, Hardened Chassis, and K2's droid tiers

Real game, my Xvfb `:2`, no K2 running. Text only. Frames (one at every Load click), the load log, both gate outputs, the pane OCR, the dev logs, my scripts and every authored scratch save are in `MAIN_WORK/media/screens/test-277/ee3a63b/` (MAIN_WORK `68acb0bc..b558d123`; see its PROVENANCE.txt).

Received since my last report: MAIN's TEST 276 answers (logged HANDOFF `654cadb`); MAIN's TEST 277 order (logged HANDOFF `6624226`).

## Build

- **App**: main `ee3a63b`, a fresh clone from GitHub in `builds/test277`, built debug through `tool/one_at_a_time.sh` (10 s, pubspec.lock unchanged). Lens `e449221` and Lodestar `a554b93` are the locked refs.
- **Heads**: at 19:15, `ee3a63b` and Shelf `ab30306` were not yet on origin, and the shared HANDOFF and MAIN_WORK held Coder's commits from 19:14 that weren't pushed yet. This was Coder's push sitting. I waited, touched nothing, and by 19:17 every shared tree was at origin and clean. Then I built and ran the gate.
- **Gate**: `scripts/gate.py --at ee3a63b` twice from the project MAIN_WORK (`gate277-1.txt`, `gate277-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at ee3a63b, 6117 tests, 0 failed".
  - Both state lines: "MAIN_WORK 1265c4fd · HANDOFF d720d15 · KOTOR-RPG-APP ee3a63b · Lodestar a554b93 · Loom 9a1c3ef · Shelf ab30306 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages checked out at `ab30306`, nothing tracked changed. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: nothing used the real data dir. At the end the live saves equal `notes/saves275`, apart from the four known (same md5s as at the start).
- **Characters**: made on ee3a63b: EX-277 (Battle droid Engineer, scratch-277a) and Vel Orrin (Bith Smuggler, scratch-277q). BX-275 and SX-275 are TEST 275's chargen saves, made on 87207e4.
- **Scratch saves**, each in its own data dir, authored with mksave273.py. Copies at 10 and up also carry Droid Upgrade 2 and Plating Medium at 7 (addfeats275.py, source granted), as a real character on this build would hold them.

  | Dir | Character | Authored at | md5 |
  |---|---|---|---|
  | 277b-g | BX-275 | Bounty Hunter 4, 5, 6, 10, 11, 12 | abd04009, 94d68d87, f052c70d, 7c4553ae, ff0453b9, 37d07431 |
  | 277h-m | EX-277 | Engineer 4, 5, 6, 10, 11, 12 | 217f0d05, 95c428d6, 31569fe9, 6980760e, 0a1b8d19, fd6ad393 |
  | 277n | SX-275 | Scout 6 | d26252e1 |
  | 277o | SX-275 | Scout 12 | 0da651d4 |
  | 277p | SX-275 | Scout 6, levelled into Bounty Hunter | d26252e1 |
  | 277r | Vel Orrin | Smuggler 2 | 3c2de373 |

- **Loads**: 19, each with BEFORE and AFTER md5 in `loads.txt` and a frame at the Load click. Every scratch file is unchanged at the end.
- **Window sizes**: 1920x1080 and 1280x720.

## Step 1: droid tiers — PASS

Granted popup on each level-up (my authoring re-grants class feats below the authored level, as before, so those rows repeat):

- **Droid Bounty Hunter**: 4 to 5 and 5 to 6: Quarry and Run to Ground only. 6 to 7: Droid Upgrade 2 and Plating Proficiency: Medium. 10 to 11 and 11 to 12: no tier. 12 to 13: Droid Upgrade 3 and Plating Proficiency: Heavy.
- **Droid Engineer**: the same: nothing at 5 or 6; both at 7; nothing at 11 or 12; tier 3 at 13. At chargen the Engineer gets Droid Upgrade 1, Plating Proficiency: Light and Field Override.
- **Droid Scout**: 6 to 7: Droid Upgrade 2 and Medium. 12 to 13: Droid Upgrade 3 and Heavy.
- **Class mix**: SX-275 at Scout 6 taking Bounty Hunter 1 (character level 7): Droid Upgrade 2 and Plating Proficiency: Medium granted; the box reads Bounty Hunter, level 7. Bounty Hunter 1 adds nothing of its own (Quarry is a level 2 grant in feats.toml).
- At 1280x720, BX-275's 6 to 7 popup fits and lists the same.

## Step 2: the panes — PASS

Each line shown once, by OCR of the pane:

- Hardened Chassis, Improved and Master: "The droid equivalent of Tenacity — organics cannot take this chain, droids cannot take that one." Once on each.
- Self-Diagnostic: "Droids have no Medicine; this is the equivalent."
- Master Tenacity (organic Smuggler grid): "Constitution drain shrinks the death threshold directly — this protects the band it widens."
- Master Killer's Instinct (Smuggler grid): both lines, once each.
- Boresight (droid Scout's level-up grid): "The damage half of KOTOR's Precise Shot is an attack you declare, not part of this feat."
- Integrated Toolkit: "This comes on top of what your Slicing, Security or Repair total already saves, and the job still costs at least one."
- **Sweeps**: every cell in all three columns of the droid level-up grid (77 panes, `p-lu-panes.txt`) and the organic chargen grid (96 panes, `q-cg-panes.txt`). No PT number, no document name, no "K2". No sentence repeats within a pane. No droid feat appears on the organic grid, and Tenacity doesn't appear on the droid grid.

## Step 3: Droid Upgrade 2 and 3, Plating Medium and Heavy — PASS

- Droid Upgrade 2: "Character Level 7 … Granted at level 7."
- Droid Upgrade 3: "Character Level 13 … Granted at level 13. Closed to Astromech and Remote."
- Plating Medium: "Character Level 7 … Medium plating. Character level 7."
- Plating Heavy: "Character Level 13 … Heavy plating. Character level 13. Closed to Astromech and Remote."
- None of them says "or earlier by class".

## Step 4: TEST 275's fixes — PASS

- **Designation warning at 1280x720** (Assassin HK-24): "HK-4" gives the two-line warning, and it clears Random Name's border by 4 rows. "HK-47" clears it by 7. "HK-71": no warning.
- **Remote portrait**: the page opens on the Remote's own face; G0-T0 is offered second. The Assassin opens on HK-47.
- **Astromech Attacks**: Recommended is dim, and clicking it changes nothing on screen, so there's no empty popup.

## Step 5: whole-screen look — no faults

Chargen and level-up, droid and organic, at 1920 and 1280x720 (frames `a-*`, `q-*`, `r-*`, `s-*`, `o720-*`, `d720-*`, `r720-*`). I saw no clipping, overlap or cut-off text at either size, viewing scaled copies (montages at about a fifth to two fifths of full size) and closer crops of the popups and the name dialog. TEST 275's gaps are covered: step 5 now has the Battle droid's chargen grid and a droid level-up grid, and step 8 now has full chargen and level-up for a droid and an organic at 1280x720.

## FINDING 1: a level 1 droid can take Droid Upgrade 4

On the droid Engineer's chargen grid, Droid Upgrade 4 is takeable. Its pane reads "Prerequisites: None … Allows level 4 droid upgrades." Add Feat took it at level 1: Remaining Feats went to 0 and the button became Remove Feat (`a3-du4-added`). feats.toml has it as section 4, `selectable`, with no level and no Droid Upgrade 3 prerequisite. Under the owner's ruling, upgrade tiers come at 1, 7 and 13 only, yet this gives level 4 upgrades at level 1. Its pane shows the same on the droid level-up grid; I didn't try adding it there.

## FINDING 2: a Medicine aptitude offered to chassis where Medicine is closed

The Medical Droid programming shows "Chassis: Any chassis" on the Background page (it has no `chassis_locked` in programmings.toml), and at Equipment it offers "Aptitude: Medicine" against a Medpac. droid_skills.toml has Medicine `chassis-closed` for the Battle and Assassin chassis. Both chassis are offered the aptitude. EX-277 (Battle) took it; on its level-up Skills page there is no Medicine row, so the choice does nothing. TEST 275's Battle droids were offered it too, and I didn't catch it then.

## Odd, not filed

- **Killer's Instinct and Master Killer's Instinct disagree on Sneak Attack.** The head pane ends "Stacks with the Sneak Attack chain."; Master's says "Sneak Attack is an attack tree that competes for the declaration."
- **Recommended is dim on the Attacks page of the Battle droid Engineer and the Assassin Engineer**, with 3 attacks to spend and some takeable (Charged Shot, Point Blank Shot, Precise Shot all added by hand). Clicking it does nothing. That fits "dimmed when it would pick nothing" if its list has nothing for them. The organic Smuggler's Recommended is lit and picks Precise Shot.
- **The Feats page help popup sits over the granted popup**, hiding the granted list until it's closed, at both sizes (TEST 275 has a frame of it too).
- A droid's level-up hub shows empty Homeworld and Upbringing rows.

## What I got wrong

- **I emptied my own st.sh** by redirecting a sed of it onto itself. I restored it from the TEST 275 media copy.
- **My ledger commit was made while my clone was 3 behind**, so the push was refused. I rebased my one commit in my private clone and pushed (`6624226`).
- **My first gate call used the wrong path** (gate.py at the root). It failed at once, and I ran it again correctly twice.
- **My Xvfb `:2` and xsettingsd were gone** when I first launched. I restarted them detached (Xvfb 191568, xsettingsd 191591).
- **The featscan repeat check is still broken.** Pages 4 to 9 of `a-scan` repeat page 3 and are left out of the media.
- **A failed Boresight search wrote a stale pane file** (Integrated Toolkit's text under Boresight's name). I removed it; the real Boresight pane is `p-pane-bs.txt`.
