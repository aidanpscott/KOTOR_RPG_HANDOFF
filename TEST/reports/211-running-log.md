# TEST 211 running log (draft, text only)

Started 2026-10-26. KNOWN, not filed: Equip gates on a COMPANION read the player's record; Stasis vs the immunities. WATCH: the cast menu on a companion's turn (note under the 210 severe item if it crashes; don't refile). Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate: "FOR TESTER — CORE at 029d802, 5265 tests, 0 failed, 13m08s at -j 3, peak 1780 MB"; ARCHIVE last green at 029d802.
- App main 029d802 (worktree builds/test211): built through the lock in 10.0 s; git status clean; Lodestar aa93c7a compiled (= lock).
- Settings: no settings.json (defaults); brightness default. Shelf 270095f: base-rules synced (old copy notes/packages-before-test211); all else identical.
- author_tester_test208_saves.dart rerun: proof-immune 706 B / 35 events; proof-drift 637/33; proof-muster 639/33; proof-locks 638/33. Copies in notes/fixtures/specs211/authored (old proof marks moved to specs211/oldmarks).
- Gear bed: local package tester-gear (copy specs211/tester-gear-package): Light Foe (soldier 3, alignment 90) and Dark Foe (alignment 10), 300 vitality, rifles, beside the arrival. Items: Bastila's Lightsaber (g_w_dblsbr006), Arca Jeth's Robe (Light Side, a_robe_23), Natth Cowling (Dark Side, a_robe_22), Jolee's Robe (Neutral, a_robe_27); base-rules' lightsaber and Nomi's Armband. Characters Gear Neutral (50), Gear Light (3 light tier-5 shifts), Gear Dark (3 dark), each Jedi Consular 10 with Battle Meditation.
## 1. 208 beds — PASS
Proof Immune's sheet: "Jedi Consular 16", Vitality 98/98, Force 239/239, Experience 120000 / Needed 16000; Character Info: Alignment Neutral (50), no "[Modded]" anywhere. (b-sheet, b-info)
## 2. Immunities — PASS
Fresh proof-immune, bump Rock (Right x2). Target numbers follow the list on screen (Steady 1, Rock 2, Thug 3 here).
- Push on Steady (6-5=1 vs 30, success): "Steady is not Force Pushed" / 25 damage — no stun line; Steady attacks in rounds 2-6. Again in round 2: the same.
- Push on Rock: "Rock is not Force Pushed" / "Rock is stunned." / "has been affected by Force Push" / 30 damage; its turn "Rock is stunned".
- Push on Thug (7-5=2): "Thug is Force Pushed" / "Thug is stunned." / 34; its turn "Thug closes 4 squares — 3 to 1 · Thug is stunned".
- Wave: Rock "not Force Pushed" + "stunned."; Steady "not Force Pushed", 26 damage, no stun; Thug "Force Pushed" + "stunned.". (i-c1, i-c3, i-c4, i-c5)
## 3. Reach is the controlled member's — PASS
Fresh proof-locks. Mate's portrait (control), click C: Mate walks to (1002,435), diagonal to C; the leader stops at (810,435), 3 squares from C. The console opens as Mate (Slicing 12, "1 spike"). Right-click C: "Examine (Science) · Slice (Slicing)"; right-click F: "Examine (Science) · Open Lock (moderate) · Search (Awareness)" — no "squares away". Back to the leader ("you are now controlling Proof Locks"), right-click C: "Examine (Science) — 3 squares away · Slice (Slicing) — 3 squares away". (l-c1, l-pos, l-rc, l-rf, l-rc-lead)
## 4a. Bastila's saber vs dark and light — PASS
Gear Neutral, Bastila's Lightsaber in WEAPON R (Equip: damage 17-40, +16). Dark Foe (alignment 10): "damage 36 — 2d10 10+4 + 1d6 energy + 3 energy + 4 universal + 1d6 vs dark side 5 + 5 + 3 + 12 + Strength 2" (g-2). Light Foe (90): "damage 30 — 2d10 7+3 + 1d6 energy + 3 energy + 4 universal + 5 + 6 + 12 + Strength 2" — no "vs dark side" term (g-3).
Small: Equip let the double-bladed saber go in WEAPON L with the right hand empty, and the swing was then "unarmed" (e-bast-on, f-3). K2 puts a double-bladed weapon in the right hand only.
Note: in a fight, changing weapons is refused ("Changing weapons — you have spent your interaction and your Action").
## 4b. Nomi's Armband — sheet PASS; in a fight FINDING: no +1 against the dark attacker
Equip: "+1 vs. Dark Side" in the description; DEF stays 16 with Jolee's Robe (e-nomi) and the sheet's Defense 16 (e-sheet) — never on the sheet. Fresh Gear Neutral with saber + armband, no robe: DEF 15 (e-set). The Dark Foe's (alignment 10) shots read "Dark Foe: Blaster Rifle · rolled 22 — d20 19 + attack 3 + Dexterity 0 · needed 15" (three shots, all "needed 15") — the sheet's 15, no +1 (g-darkshot). The Light Foe's line couldn't be read (the Dark Foe acts last and overwrites the box). fight.dart:1370 adds defenceVersus to the grants; the line doesn't show it.
## 4c. Alignment gates at Equip — PASS for the gate; FINDING: no reason shown
Body slot rows (red outline = refused):
- Gear Neutral (50): Arca Jeth's Robe (Light Side) RED, Natth Cowling (Dark Side) RED, Jolee's Robe (Neutral) allowed and equipped.
- Gear Light (Deep Light 95): Arca allowed; Natth RED; Jolee RED.
- Gear Dark: Natth allowed; Arca RED; Jolee RED.
All three robes list "Feats Required: Jedi Defense" and Jolee's is allowed without it, so the alignment is what refuses. Selecting a refused row in the item view shows only K2's generic popup "You cannot equip this item. You don't have the prerequisites. Please see the item description." and the description names no side (e-arca2). The words exist (play_screen _gateWhy -> blockedWhy) but the popup draws blockedMessage ?? the generic text (equip_screen.dart:809), so "needs to be Light Side/Dark Side" is never on screen.
WATCH (companion cast menu): no companion with powers in these beds; not exercised.
## 5a. Dice — PASS: 17/17 lines = dice-baseline-206 (line-1 OCR only). (dice/)
## 5b. Regression — PASS: '47 : reg210' loaded; New Slot '48 : reg211' (000048.mark 18:06:14); F4: one quick.mark 18:06:17; Load '48 : reg211'; fightbolt WON ('FIGHT OVER 44'; "Gunman and Gunman and Gunman falls"; Icon Nine 84 of 196). (reg/)
## Processes: app, xsettingsd, Xvfb stopped by PID.
