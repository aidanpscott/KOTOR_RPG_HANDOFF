# TEST 210 running log (draft, text only)

Started 2026-10-26. KNOWN, not filed: Force Immunity: Stun stuns; controlled member's reach from the leader; 208 beds' level-1 sheet. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate: "FOR TESTER — CORE at 71ce94c, 5243 tests, 0 failed, 14m10s at -j 3, peak 2059 MB"; ARCHIVE last green at 71ce94c.
- App main 71ce94c (worktree builds/test210): built through the lock in 10.3 s; git status clean; Lodestar a9265df compiled (= lock).
- Settings: no settings.json (defaults); brightness default. Shelf 553002b: all packages identical.
- Bed: local package tester-align (copy notes/fixtures/specs210/tester-align-package): a01 "Align Hall" — Dark Mate (Jedi Consular 10, alignment = 20, role companion), Plain Mate (Jedi Consular 10, no alignment, companion), Sith Foe (Jedi Consular 10, alignment = 10, enemy, far end). Player align-210 "Align Jedi" (Jedi Consular 10; Heal, Force Affliction, Force Push).
## Route to a companion's cast
A character file has no powers field: on Plain Mate's manual turn f says "Plain Mate knows no Force powers". Companion powers come from subject-tagged events in the save, so specs210/align.json adds character.power-taken {subject: <tag>} (Heal, Force Affliction) for both mates. (Out of a fight f always lists the player's powers and pool, even while controlling a mate.)
## SEVERE — a companion's cast list kills the play screen when it knows fewer powers than the player
align-210 (player: Heal, Force Affliction, Force Push; mates: Heal, Force Affliction): bump the Sith Foe, End Turn to "Plain Mate is waiting on you", f -> red screen "RangeError (length): Invalid value: Not in inclusive range 0..1: 2" (a2-plainf). app.log has no stack. With three powers each (align3-210, + Force Push for the mates) the list opens fine — consistent with the menu counting the player's list and indexing the mate's. Sent to MAIN at once.
## 1. Companion prices — PASS
align3-210. Player: "1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f". Dark Mate (alignment 20), her turn: "1 Heal 12f · 2 For…" (a3-darkf); cast 2 on the Sith Foe: "Dark Mate: Force Affliction · 10f — 105 → 95" (a3-d2). Plain Mate (no alignment), her turn: "1 Heal 8f · …"; cast 2: "Plain Mate: Force Affliction · 12f — 105 → 93" (a5-pf, a5-p2). Light costs Dark Mate more, dark less; Plain Mate = the player's.
Small: on a companion's turn the cast menu shares the top line with the vitality list and is cut ("2 For…"), and that line still reads the player's "force 155 of 155", not the caster's 105.
## 2. Companion's drift line — PASS
After Dark Mate's Affliction, Messages > Feedback ends "Dark Mate has moved closer to the Dark Side of the Force."; no "You have moved" line. The player's sheet marker stays mid-bar (a3-fb, a3-sheet0).
## 3. Companion's sheet marker — NOT REACHED (no route)
The Character sheet only ever shows the player: its small portraits (in a fight and out), controlling Dark Mate from the HUD portrait, and switching to Dark Mate on Abilities (footer reads "Dark Mate · Jedi Consular 10") then pressing Character all show Align Jedi's sheet (a4-ds2).
## 4. Enemy priced at its file's start — NOT REACHED
The Sith Foe (alignment 10) only attacks; an enemy's file can list no powers, so it never casts.
## 5. Recovery toward its own start over quiet sessions — NOT REACHED
No sheet for a companion (item 3) and no way I found to step sessions.
## 6. Loom's alignment box — PASS for the box and writing; FINDING: refusals are silent
Loom 949823c (worktree builds/loom210; built through the lock, pubspec.lock unchanged d22d359a, git status clean, Lodestar a9265df). Scratch store-bed at /tmp/claude-1000/qz210 (typed paths with a prefix shared by another folder get autocompleted wrongly). Palette creatures > custom "+" = NEW CREATURE: an "alignment" box sits between blind and faction (lo10-new).
- Written: 0 -> "alignment  = 0" (align-test.crtr); 100 -> "alignment  = 100" (align-hundred.crtr); empty -> no alignment line (align-none.crtr; absent = 50). (s210/loom-files)
- Refused: 101, -1, 20.5, abc (and 150) each dim Create; no reason anywhere — the box isn't marked, nothing under it, the status line still says the last action (lo10-p2-_101_). Control: the file-name box's refusal does show its reason under the box ("A trailing number carries no meaning. "100" says nothing about what this is.") (lo10-probe-_100_).
- Note: Create stays dim until a species is picked.
## 7a. Dice — PASS: all 17 lines identical to dice-baseline-206.txt; only the line-1 OCR difference. (dice/)
## 7b. Regression (Icon Nine) — PASS: '46 : reg209' loaded; Save > New Slot '47 : reg210' (000047.mark 17:03:25); Close, F4: one quick.mark 17:03:28; Load '47 : reg210'; fightbolt: WON ('FIGHT OVER 41'; "Gunman and Gunman and Gunman falls"; Icon Nine 93 of 196). (reg/)
## Processes: app, xsettingsd, Xvfb, Loom stopped by PID.
