# TEST 278: single spaces, aptitudes, locked programmings, Droid Upgrade 4

Real game, my Xvfb `:2`, no K2 running. Text only. Frames (one at every Load click), the load log, both gate outputs, the sweeps with their gap checks, the programming walks, the dev logs, my scripts and every scratch save are in `MAIN_WORK/media/screens/test-278/a5a2cfd/` (MAIN_WORK `f4c89265`; see its PROVENANCE.txt).

Received since my last report: MAIN's first TEST 278 order on 5b2642d (logged HANDOFF `1c77dfb`); MAIN's order to fix og277.py (logged `18535af`, fixed in MAIN_WORK `f319ca38`); MAIN's reissued TEST 278 order on a5a2cfd (logged `fa5cd0a`).

## Build

- **App**: main `a5a2cfd`, a fresh clone from GitHub in `builds/test278`, built debug through `tool/one_at_a_time.sh` (10 s, pubspec.lock unchanged). Lens `e449221` and Lodestar `a554b93` are the locked refs.
- **Heads**: at 12:31 Coder's push sitting was still running (app 4 ahead, MAIN_WORK 5 ahead, shared HANDOFF 1 ahead and 1 behind). I touched nothing. By 12:32:55 every shared tree was at origin and clean.
- **Gate**: `scripts/gate.py --at a5a2cfd` twice from the project MAIN_WORK (`gate278-1.txt`, `gate278-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at a5a2cfd, 6124 tests, 0 failed".
  - Both state lines: "MAIN_WORK 8523893a · HANDOFF 054bcbd · KOTOR-RPG-APP a5a2cfd · Lodestar a554b93 · Loom 9a1c3ef · Shelf b9bc862 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages checked out at `b9bc862`, nothing tracked changed. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: nothing used the real data dir. The live saves equal `notes/saves275` apart from the four known, at the start and at the end.
- **Characters made on a5a2cfd**: BM-278 (Battle droid Engineer, Medical Droid) and Tor Vessan (Human Smuggler, Taris, Upper City, Noble, Doctor, made at 1440x900). Three more droid chargens (Assassin, Remote, Astromech) went to Equipment and were not finished.
- **Scratch saves**, each in its own data dir with packages at b9bc862:

  | Dir | Save | What | md5 |
  |---|---|---|---|
  | 278a | bm-278 | made on a5a2cfd | a36f12c0 |
  | 278f | ex-277 | TEST 277's Engineer 12 | fd6ad393 |
  | 278g, 278l | sx-275 | TEST 277's Scout 6 | d26252e1 |
  | 278h | sx-275 | Scout 6 plus the eight named feats as held (addfeats275.py, source granted) | 10f28443 |
  | 278i | tor-vessan | made on a5a2cfd | 1ba3083c |
  | 278j, 278k | tor-vessan | authored to level 2 with 3000 XP (mksave273.py) | 35486514 |

- **Loads**: 5, each with BEFORE and AFTER md5 in `loads.txt` and a frame at the Load click. Every scratch save is unchanged at the end.
- **Window sizes**: 1920x1080 and 1440x900.

## How I checked spaces

OCR collapses repeated spaces, so I measured them. `sp278.py` crops a pane, takes tesseract's word boxes and flags any gap between neighbouring words wider than 1.5 times the pane's median word gap. Ordinary gaps run 32 to 35 px at 3x.

- **Positive control**: TEST 277's Plating Medium frame (Shelf ab30306, "Medium plating.  Character level 7.") flags at 1.79. The other nine TEST 277 pane frames pass.
- Every pane in the sweeps below carries its result line.

## Step 1: single spaces — PASS

- **Droid level-up grid** (SX-275, Scout 6 to 7): 76 panes, all clean. The titles equal TEST 277's sweep of the same grid less one, Droid Upgrade 4.
- **Organic chargen grid** (Human Smuggler): 96 panes, all clean. The titles equal TEST 277's.
- **Battle droid Engineer chargen grid**: 67 panes, all clean.
- **Medium plating**: "Medium plating. Character level 7." with one space.
- **By name**: Installation 1 to 3, Master Guard Stance, Salvage Charge, Live Placement, Nothing Wasted and Momentum are on no grid I can reach. Installation belongs to Droid Master and the Salvage chain to Saboteur (`granted_feats.dart`). Momentum and Master Guard Stance aren't granted by any class there. So I wrote all eight onto a scratch SX-275 as held and read them on Abilities > Feats: all eight clean.
  - Each pane's first line gave one hit, the scroll arrow at the pane's right edge. With the box stopped short of the scrollbar all fifteen panes are clean, and the control still flags.
  - Installation 1: "Allows you to install level-1 upgrades into any droid you own. Granted at Droid Master 1." Installation 2: "Level 1-2. Droid Master 3." Installation 3: "Level 1-3. Droid Master 7."
  - Master Guard Stance: "−2 attack, +6 Defense, +6 on saves. And you may move your full speed without ending it. Level 8."
  - Salvage Charge, Live Placement and Nothing Wasted read with single spaces too.
  - Momentum: "… Stacks with itself, to a maximum of +1."

## Step 2: Medicine and Scavenging aptitudes — Background PASS, Equipment see FINDING 1

| Chassis | Medical Droid, Background pane | Medical, Equipment | Salvage Droid, Background pane | Salvage, Equipment |
|---|---|---|---|---|
| Battle | 2 Medpacs; Chassis: Any chassis | Medpac; Aptitude: — | Parts; Aptitude: Scavenging | (not opened) |
| Assassin | 2 Medpacs; Chassis: Any chassis | Medpac; Aptitude: — | Parts; Aptitude: Scavenging | Parts; Aptitude: Scavenging |
| Remote | 2 Medpacs; Aptitude: Medicine | Medpac; Aptitude: Medicine | Parts (no aptitude) | Parts; Aptitude: — |
| Astromech | 2 Medpacs; Aptitude: Medicine | Medpac; Aptitude: Medicine | Parts (no aptitude) | Parts; Aptitude: — |

The other closed aptitudes go the same way. On the Remote and Astromech, War Droid shows no Intimidate and Military Droid no Athletics.

## Step 3: the help box and the granted list — PASS

- **Tutorial Popups on**: on chargen Feats for the Battle, Assassin, Remote, Astromech and the Human Smuggler, the help box came up alone, with nothing under it, both at once and 3 s later. The granted list came up when I closed it. Seen at 1920, and for the Smuggler and the Battle droid at 1440x900 too.
- **Tutorial Popups off** (Options > Feedback): no help boxes anywhere in chargen. Chargen Feats opened with the granted list up at once (Smuggler's Luck, Quickdraw, Killer's Instinct).

## Step 4: Droid Upgrade 4 — PASS

- **Battle droid chargen grid**: the Droid Upgrade row is 1, 2, 3 (held, locked, locked), with no fourth cell. It isn't among the 67 titles.
- **Droid level-up grid**: 1, 2, 3 only, and not among the 76 titles.
- **Granted lists**: Droid Upgrade 1 at chargen for all four chassis, Droid Upgrade 2 at level 7, Droid Upgrade 3 at level 13. No 4 anywhere.
- Both featscans end "page4 repeats page3; end".

## Step 5: locked programmings — PASS

- **Battle and Assassin**: 14 programmings. Security Droid is there ("Chassis: Battle - Assassin"); no Navigation, Utility or Probe.
- **Remote**: 14. Probe Droid is there ("Remote only"); no Security, Navigation or Utility.
- **Astromech**: 15. Navigation Droid ("Aptitude: Pilot", "Astromech only") and Utility Droid ("Astromech only") are there; no Security or Probe.
- Medical Droid and every unlocked programming read "Chassis: Any chassis" on all four. "Aptitude: Pilot" appears only on the Astromech's Navigation pane.

## Step 6: the level-up hub — PASS

- **Droid** (EX-277 at 13, SX-275 at 7): Origin shows Species, Chassis and Model; Background shows Medical Droid. No Homeworld or Upbringing row.
- **Organic** (Tor Vessan, 2 to 3): "Homeworld: Taris", "Upbringing: Noble", "Background: Doctor".

## Step 7: whole-screen look — no faults

I saw no clipping, overlap or cut-off text at either size, viewing scaled copies.

- **1920**: droid chargen for all four chassis, the Human Smuggler's chargen, and the droid and organic level-ups.
- **1440x900**: the Human Smuggler's whole chargen, the Battle droid's chargen to the Feats granted list, the organic level-up hub, Skills and Attacks, and the droid level-up's granted list, hub and Feats.

## FINDING 1: an empty aptitude is still offered against the item, and taking it gives nothing

Where the aptitude is closed, Equipment still offers the choice, with "Aptitude: —" as the second row:

- Medical Droid on the Battle and the Assassin: Medpac or "Aptitude: —".
- Salvage Droid on the Remote and the Astromech: Parts or "Aptitude: —".

OK stays dim until a row is picked, and "Aptitude: —" counts as a pick; its pane is empty. I took it on BM-278, finished chargen and played. The inventory holds Ion Blaster, Computer Spike and Repair Kit, with no Medpacs (`bat-eq-apt*`, `bat-inv*`). "Aptitude: Medicine" is gone as ordered, but a player can still trade the Medpacs away for nothing.

## FINDING 2 (pre-existing): design notes on the Upbringing page

The chargen Upbringing page shows each entry's `note` from upbringings.toml as its pane:

- Bastard: "Added at PT-706. Sits beside Noble deliberately — acknowledged enough to be fed, never enough to inherit. …"
- Unknown: "No longer special. PT-694 gave it a skill menu because it could not predict a skill; …"

The other seven upbringings, Noble included, have empty panes (`o-upb-bg.txt`). The page has shown `playerProse(u.note)` since 2026-10-22 (`origin_screen.dart:162`), so this isn't new in this hash.

## Odd, not filed

- **After a Background change resets the later steps**, chargen Feats opened with neither the help box (already seen) nor the granted list (Assassin, second pass, `asns-feats-*`).
- **Recommended is dim on the organic Attributes and Skills pages** (Human Smuggler) and does nothing when clicked, so I spent the points by hand. It is also dim on Feats and Attacks for droid Engineers, as in TEST 277.
- **Item panes print "Weapon Proficiency -  Blaster Pistol"** with two spaces (inventory). A comment at `play_screen.dart:160` says K2 prints it so; items.toml has 14 such lines. That's a code comment, not a ruling.
- **Double spaces elsewhere in the Shelf, not seen on screen**: programmings.toml Salvage Droid's upgrade line ("Components  and"), feats.toml line 454's note ("feat.2da.  Scout"), and lines in worlds (315), items (245), two_weapon (25), event_kinds (10), species (5), class_arrays (5), equipment (5), profession_grants (4) and three others.
- **Momentum's pane**: "Stacks with itself, to a maximum of +1."
- **The Battle droid's portrait page offers only "?"**, the same as on TEST 277's EX-277.

## What I got wrong

- **My first scan of media scripts wrote its list into `~/.cache/kotor-coder`**, Coder's cache. I moved it to my scratchpad.
- **My first live-saves check compared the wrong folder** (`~/.local/share/kotor-rpg`). The right one is tester-data's.
- **Assassin, Salvage, first try**: changing the Background asks "Every step after this one will be lost. Proceed?" and my next click hit its Cancel. I redid it with OK.
- **Remote, Salvage, first try**: I started from the Equipment page, not the hub, so my clicks opened Purchase Gear's store. I closed it, cancelled to the hub and redid it.
- **Not covered**: Equipment for a droid at 1440x900; Salvage at Equipment on the Battle droid (the Background pane shows Aptitude: Scavenging); sweeps of the Remote's and Astromech's chargen grids (their granted lists have no Droid Upgrade 4).
- **The Engineer at 13 has no Feats step**, so the droid level-up sweep is SX-275 Scout 6 to 7, as in TEST 277.
