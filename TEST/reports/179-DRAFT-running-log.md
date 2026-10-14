# TEST 179 running log (draft, text only)

Started 2026-10-13 22:30 EDT. Tester, Xvfb :2, own data dir (~/.local/share/tester-data), no K2, no BG3.

## Build
- App 4a9c20c (cf6b705 + tool/one_at_a_time.sh; diff vs cf6b705 = README.md + tool/one_at_a_time.sh only), git archive to ~/kotor-tester/builds/test179 (on disk, not /tmp).
- Lodestar fffb58050d389b297fbd2522d1fac6af47f9094c = lock = compiled (package_config.json).
- Lens ca980549c6b8064038931f5817cbeff0547c080e = lock = compiled.
- Loom: no entry in the app's lock.
- Shelf 83b5bec (data dir; origin HEAD is also 83b5bec). check_shelf clean: 31 rules files, 114 blueprints.
- tool/env.sh sourced. Build through tool/one_at_a_time.sh: 257 s incl. lock wait. pubspec.lock unchanged after build.
- App launches through the lock (run/launch.sh wraps it; lock held while the app runs). First launch waited on Coder's compile.
- MAIN_WORK 2ea6c37 at start; HANDOFF ee47a27 at start.
- Fixtures: fresh (TEST 178's fixture authors were in /tmp and were lost in the reboot).

## Items

### Setup note (22:58): self-deadlock on the lock, cleared
- I launched the app through the lock (old rule), then queued tester_dump.dart behind it: the app held the lock, Coder's build waited on the app, my dump waited on Coder. MAIN flagged it.
- Fix: closed my app (PID 40291). Nothing unsaved was lost; the app was on the library screen only.
- NEW RULE (MAIN): the lock covers compiling only (flutter build/test, big dart analyze, dart run on tool scripts). The built bundle is launched with plain & outside the lock. Never flutter run.
- Local bed made: packages/tester-rough (my data dir only): Rough Field 12x5, ':' rough column 2 and block (5-6, 0-1), Kael henchman, sentry droids at (9,2) and (5,3). For rough ground (items 5, 6) and the path line (11).
- Fixture author: ~/kotor-tester/notes/fixtures/tester_author.dart (JSON spec -> save), copied into the build's tool/.

### Item 1: Config 2 (in progress)
- Fixture: Sol Ninety, fresh chargen Soldier in Store Bed (run/cgrun.sh; Standard Gear: Blaster Rifle C1, Short Sword C2, clothing, Dockworker's Treads).
- Soldier: Equip > Config 2 Short Sword -> None: slot empty; reopened: "Short Sword" offered; picked: back on. Config 1 Blaster Rifle -> None: 2-4 (unarmed); reopened: "Blaster Rifle" offered; back on, 2-13 +2. While the sword sits in Config 2, the Config 1 list offers None + Blaster Rifle only (no sword). PASS. Shots: i01-sol/lists.png, i01-sol/slots.png (+ per-step a-d).
- Medic (Med Ninety, fresh chargen, Store Bed): Config 2 Short Sword off/offered/on; Config 1 Hold Out Blaster off (2-4) / offered / on (2-5 +1); Config 1 list never offers the sword. PASS. Shots: i01-med/lists.png, i01-med/slots.png.
- **Item 1: PASS.**

### Item 4: Names
- Fixtures: fresh chargen in Store Bed: Mark Ninety (Marksman), Sith Ninety (Sith Warrior), plus Sol Ninety's chargen screen.
- Sith Warrior robe: chargen Standard Gear lists "Dark Padawan Robe" (i04-sith-chargen.png); in play, Equip > Body reads "Dark Padawan Robe (Equipped)" (i04-sith-equip.png). Not "Robe 1". PASS.
- Starting items own names: Soldier "clothing, Blaster Rifle, Short Sword, Adrenal Strength, 2 Frag Grenades, 2 medpacs, Dockworker's Treads" (i04-sol-chargen.png); Marksman "Marksman Rifle, Hold Out Blaster, Adrenal Stamina, Dockworker's Treads" (i04-mrk-chargen.png). No "Training Blade" item exists; the nearest is the Sith Warrior's "Training Lightsaber red" (note: colour word lower-case and after the name). PASS.
- Apostrophes: "Dockworker's Treads" on all three chargen screens; "Dockwor ker's Tr..." slot label in Equip. None lost. PASS.
- Marksman Rifle: Config 1 off (2-4) / offered / back on (2-11 +2) (i04-mrk/lists.png, slots.png). PASS. Note: the rifle still draws no icon (empty cell), as in TEST 178.
- Powers screen note: cgrun.sh's power clicks no longer hit two pickable rows; I picked Fear + Force Push by hand. Not an app fault.
- **Item 4: PASS** (notes: "Training Lightsaber red" casing; Marksman Rifle no icon).

### Item 2: Spikes and repair (Locked and Trapped)
- Fixture: Lock Ninety, fresh chargen Soldier (Slicing 1, Repair 1 on the console card).
- Quartermaster: "Spikes and a repair part" -> "Four spikes and a part. That is all I can spare." (i02a-quartermaster.png)
- Console (right-click > Slice (Slicing)): opens free and reads Spikes 4 and Parts 1 at once, no reload; both "[Slicing] Unseal the vault door. (3 spikes)" and "[Slicing] Cycle the corridor lights. (1 spike)" offered (i02b-console-open.png). Lights: "— 1 spike spent" (i02c). Reopened free: Spikes 3, both offered (i02d). Unseal: "— 3 spikes spent" (i02e). Reopened: Spikes 0, both dimmed "— you have 0 spikes" (i02f). Sequence: i02-console-sequence.png. PASS.
- Damaged Power Panel (6,3): right-click shows "Examine (Science)" and "Repair (Repair)" (i02g). Repair opens "POWER COUPLING FAULT — OUTPUT 0%" with "1 [Repair] Reroute the power coupling. (1 part)" (i02h). Picked: "— 1 part spent" (i02i). Reopened: Parts 0, reply dimmed "— you have 0 p..." (i02l). PASS.
- **Item 2: PASS.**
- Notes (not failures): (a) the dimmed panel reply is cut off: "— you have 0 p..."; (b) the panel header still reads "OUTPUT 0%" after the repair; (c) Down from (6,0) put my token ON the console's square (6,1) with no message (con1); (d) a click just left of the grid edge (x 560) walked me to (0,3) straight through both noticed mine squares (2,1)/(2,2): both sprung, HP 11 -> 8 (i02k-click-outside-walked-mines.png); (e) after that the centre line reads "Lock Ninety: 11 of 11" while the party bar reads 8 of 11 (i02k, i02l).
- Console exit: Escape opens Options (Close returns to the console); a click outside the console closes it.

### Item 10 (in progress) and 11 out-of-fight parts. Bed: tester-rough, Rough Ninety (fresh chargen Soldier) + Kael. App relaunched with KOTOR_ENEMY_TURN_PAUSE_MS=4000.
- Numpad out of a fight: 7/9/1/3 (Num Lock off: KP_Home/Prior/End/Next; Num Lock on: KP_7/9/1/3) do nothing: no move, no line (i10a, i10b). Control: Right arrow moves one square and Kael follows (i10c). PASS for "7/9/1/3 do nothing".
- "a diagonal step is refused with its line": NOT SEEN IN PLAY. The line exists ("step up, down, left or right — a diagonal square takes two steps", play_screen.dart:7455) but no play input can send a diagonal step: keys bind only the four arrows (play_screen.dart:19779-19786), the click walker sends orthogonal legs (_walkRoute), and the only diagonal caller is stepForTest (test/path_line_test.dart:319). Numpad keys are silent. Also: KP_6 does not move either (numpad not bound at all).
- 11, outside a fight: hover over a square and over the far droid draws no path line (i11-out-of-fight-no-line.png). Click on the droid is not an attack: "walk into them to act — choose an action first to aim at somebody" (i11-out-of-fight-click-creature.png). PASS.

### Item 3: Turn lines (KOTOR_ENEMY_TURN_PAUSE_MS=4000, confirmed in the app's environ)
- Bed: tester-rough fight (Rough Ninety bumped the droid at (5,3)); order Sentry Droid 19, Sentry Droid 7, Rough Ninety 5, Kael 3.
- Kael's turn (i03a): Equip > Switch Weapons: nothing changes; status line "switching weapons — it is Kael's turn; wait for your own" (i03b). PASS.
- Sentry Droid's turn: Equip > Switch Weapons inside the droid's turn; status line "switching weapons — it is Sentry Droid's turn; wait for your own" (i03c, top half; the bottom half 0.6 s later shows the next droid acting). PASS.
- Note: the line is on the play status line only; inside Equip the press shows nothing (the line is visible after Close).
- **Item 3: PASS.**

### Items 10 and 11 in a fight (tester-rough, Rough Ninety Soldier + Kael manual, 2 sentry droids)
- 11 path line, on my turn (i11-six-hovers.png, zooms i11-colours-teal-red-amber.png, i11-straight-row-lines.png):
  - Straight up a column: (4,2),(4,1),(4,0) teal, "3 squares · 2 left", one straight line. Straight along row 2: "3 squares · 2 left", "4 squares · 1 left". PASS.
  - L to (7,4): one rounded bend, 4 squares marked, "4 squares · 1 left". PASS.
  - Past movement (11,4): 5 teal then red-tinted squares with a red dashed line, "Not enough movement". PASS.
  - Rough ground: (2,4) and (2,0) drawn with an amber inset; past movement amber+red. PASS.
  - Occupied squares: target (8,3) with a droid on (5,3) in the straight row: detours down row 4 and back up; target (1,3) with Kael on (3,3): detours via row 4. Never through an occupied square. PASS.
  - Provokes: "Provokes an attack from Sentry Droid" on paths leaving the droids' reach. After d (Disengage: "disengaging — your movement provokes nothing this turn") the same hovers show no provoke line (i11-disengage-line.png, i11-disengage-no-provoke.png). PASS.
  - Click walks exactly: clicked the 4-square L to (7,4): landed on (7,4), move 5 -> 1 (i11-click-walked-4.png). PASS.
  - Count vs marked squares on rough ground: hover (5,1) from (6,2): 2 squares marked ((5,2), (5,1) rough) but the label reads "3 squares · 2 left / rough ground costs extra" (i11-rough-count-and-provoke.png). The count is movement spent, not marked squares. FAIL against the order's wording ("The label's count equals the marked squares").
  - Move-and-attack (Short Sword): hover the droid at (4,2) from (6,2): ghost on (5,2), "Sentry Droid / 65% (needs 8+) / +1 attack · +1 Strength, against Defence 10 / 1 square · 4 left" (i11-move-attack-hover.png). PASS (note: the tooltip box covers most of the ghost). Clicking it not done; the in-place diagonal attack was clicked instead (below).
  - Stale move counter: at the start of a turn the legend read "5 → 3 move" with the pointer off the board, and later "2 → 0" with 2 left; the real allowance was 5 ("4 squares · 1 left") (i11-stale-move-counter.png). Looks like the last hover's preview kept after the click/turn change.
- 10 diagonal adjacency:
  - Enemy: the far droid closed 4 squares along row 2 to (5,2), diagonal to me at (4,3), and attacked me from there ("1 square — hit"). A droid stepped (5,2)->(4,2), diagonal to Kael (3,3), and attacked him (i10-enemy-diagonal-attack.png). PASS (stops on the diagonal and strikes).
  - Me hitting a diagonal neighbour in place: from (5,1) clicked the droid at (4,2): "Short Sword · rolled 13 — d20 11 + attack 1 + Strength 1 · needed 10 — hit · damage 2", no move spent (i10-diagonal-hit-in-place.png). PASS.
  - Walking away from a diagonal neighbour provokes: (5,2) -> (5,1) leaves the droid at (4,3) (diagonal): "Sentry Droid catches Rough Ninety leaving — ... miss" (i10-diagonal-leave-provokes.png). PASS.
  - Flanking: NOT SHOWN. Kael at (3,3) and me at (5,1) are diagonally opposite across the droid at (4,2); neither the hover reasons nor the attack line has a flanking term (i10-diagonal-hover-no-flank-term.png). The app has no flanking bonus code: "flank" appears in lib only in comments (play_screen.dart:7452, fight.dart:1154). Cannot be checked in play.
  - Follower stops on the diagonal: out of a fight, one Right step from (0,2) put me at (1,2) and Kael (from (0,4)) at (0,3), diagonal (i10c-arrow-control.png). PASS.
- 9 (part): own-turn Switch Weapons in Equip: 1st "you switch weapons" (free, action still lit); 2nd "switching weapons — your second interaction this turn, so it cost your Action"; 3rd "switching weapons — you have spent your interaction and your Action" (i09-switch-free-action-refused.png, i09-switch-slots.png). PASS.

### Item 12: Stack numbers (Rough Two, fresh chargen Soldier: 2 Frag Grenades, 2 medpacs, 1 Adrenal Strength)
- Inventory: Frag Grenade and Medpac icons each carry a bare teal "2" at the bottom right, no dark box behind it (i12-stack-icons-zoom.png). Names read "Frag Grenade", "Medpac", no "x2". Single items (Adrenal Strength, the worn ones) show no number (i12-inventory.png). **PASS.**
- Note: Dockworker's Treads draws no icon (empty cell) in Inventory and in Equip's list.

### Item 9 (rest), Rough Two in a fight in tester-rough
- Escape + F4: Escape opens Options; F4 with Options open writes nothing (known since TEST 175). Escape again (closes Options) + F4: rough-two.marks/quick.mark written 23:38:32; two more Escape, Escape, F4 cycles rewrote the one quick.mark (23:38:46, 23:38:55), no second file. PASS.
- Auto Save shows companions: Options > Load Game, Auto Save row: faces of Kael and Rough Two, area Rough Field, package Tester Rough Ground (i09-autosave-companions.png). PASS. Notes: Kael's face is first and the leader second; the Auto Save time equals the Quick Save time (23:38:55).
- Party bar faces: Kael's and the player's portraits in the play sidebar and the Equip footer throughout (i03b, i12-inventory). PASS.
- Boots off/on: refused in a fight ("...gear cannot be changed in a fight — only weapons"), as expected; to be done out of a fight.

### Item 10 (rest)
- Enemies close in on L-shaped paths: NOT OBSERVED. In two fights every droid approach was a straight run that ended diagonal to its target ((9,2)->(5,2); (5,2)->(4,2); (5,3)->(7,3)) (i10-droid-approach-straight.png). My bed did not force an L. Companion approach not observed (Kael is MANUAL).

### Fixtures for items 5-8 (authored fresh with notes/fixtures/tester_author.dart, specs in notes/fixtures/specs/, one locked dart run):
- bolt-ninety (Store Bed, astromech Engineer, 1000 credits, Dockworker's Treads in bag); c79-astromech/-remote (Engineer), c79-assassin/-battle (Marksman, male), c79-tread (astromech wearing a Treaded Motivator) all in tester-rough; ivy-ninety (Store Bed, Soldier 3, all three Cybernetic Implantation feats, three implants in bag); ivy-none (same, no feats).

### Item 6: Droid speed by chassis (fresh authored c79-* saves in tester-rough; fight started by bumping the droid at (5,3))
- Move legend on the droid's own turn: Assassin 5, Battle 5, Remote 6 (i06-speeds.png). Astromech: 4 move diamonds (frame on Kael's turn; the legend shows the player's allowance, same as the Treaded run where it read 3 on both Kael's and the droid's turn). PASS.
- Remote on rough ground (its own turn, 6 move): to rough (5,1) via (4,2),(4,1): "3 squares · 3 left"; to rough (2,1): "4 squares · 2 left"; no "rough ground costs extra", no amber inset (i06-remote-rough-free.png). PASS.
- **Item 6: PASS.**
- Mishap (mine, not the app): my first loop ended the astromech's own turns too, because the status line "Kael is waiting on you" stays up into the player's turn; the droids took it to "-14 of 18". Fixed the loop to read the turn-order marker (run/turn.py).

### Item 5 (part): Treaded Motivator in play (c79-tread, astromech wearing it, tester-rough)
- Move: 3 diamonds (astromech 4, one less). PASS.
- Rough ground: path to rough (5,1) from (4,3), 3 squares: "3 squares · 0 left", no "rough ground costs extra", no amber inset (i05-treaded-3-and-rough-free.png). A plain 4-square path reads "Not enough movement". PASS.

### Item 5: Motivators (Store Bed)
- Fixtures: bolt-ninety (authored astromech Engineer, 1000 credits, Dockworker's Treads in bag); Med Ninety (fresh chargen Medic, 100 credits).
- Quick Fix (Dressa, "Show me what you have.") stocks Treaded Motivator (75) and Silenced Motivator (400) (i05a-store-stock.png). Bolt Ninety bought both: credits 1000 -> 925 -> 525, each "In Inventory 1" (i05b-bought-both.png). PASS.
- Droid's Motivator list: None, Treaded Motivator, Silenced Motivator; the Dockworker's Treads in its bag are not offered (droid refused boots, by omission, no line) (i05c). PASS.
- "MOTIVATOR" header on one line (i05d-motivator-label.png). PASS. Note: the slot's own label is cut: "Silenced Motivato...".
- Silenced worn: Abilities > Skills > Stealth: Rank 0, Bonus +2, Total 2 (i05e). Control, motivator taken off: Bonus 0, Total 0 (i05f). PASS.
- Treaded: 3 move and rough ground free (logged above from c79-tread). PASS.
- Organic: Med Ninety bought a Treaded Motivator (100 -> 25); the store's row says "In Inventory 1 · replaces Dockworker's Treads" (i05g) although an organic cannot wear it; Equip > Boots then offers only None and Dockworker's Treads (i05h): refused by omission, no line. PASS (refusal), with that store note.
- Note: both motivators draw no icon (empty cells in the store and in Equip).
- **Item 5: PASS** (refusals are "not offered", as in TEST 178).

### Item 9 (boots), Med Ninety out of a fight
- Boots -> None: slot reads "BOOTS"; reopened, "Dockworker's Treads" offered; picked, back on (i09-boots-off-on.png). PASS.
- **Item 9: PASS** (Auto Save companions, own-turn swap free/Action/refused, party bar faces, boots off/on, Escape+F4 one save).

### Item 7: Boots Defence
- NOT REACHABLE. Sith Trooper Greaves, Mandalorian Battle Greaves, Krath War Boots and Vanguard Assault Boots exist only as rows in base-rules/rules/items.toml (lines 29170, 29229, 29504, 29527). No package has an item blueprint for any of them, no store stocks them (grep of every .item/.shp/.toml/.area in my Shelf 83b5bec data dir), and both Sith Trooper creature blueprints (endar-spire, tester-save-bed) carry only a blaster rifle. Note the shipped names are "Greaves" for the Sith Trooper and Mandalorian pairs.

### Item 8: Implants (Store Bed)
- Fixtures: ivy-ninety (Soldier 3, all three feats, three implants in bag); ivy-none (Soldier 1, no implant feat, same implants).
- Abilities > Feats (Ivy Ninety): a chain of three cells (no icons). Each selected: "Cybernetic Implantation" (Prerequisites None; "Surgical grounding for cybernetic hardware. Without it, implants cannot be installed." / "Allows Cybernetic Implants."), "Advanced Cybernetic Implantation" (Prerequisites Cybernetic Implantation; "Further surgical grounding allows the use of Advanced Cybernetic Implants." / "Allows Cybernetic Implants and Advanced Cybernetic Implants."), "Master Cybernetic Implantation" (Prerequisites Advanced Cybernetic Implantation; "The fullest surgical grounding allows the use of Master Cybernetic Implants." / "Allows Cybernetic, Advanced Cybernetic and Master Cybernetic Implants.") (i08a-three-feats.png). PASS.
- Inventory names: "Advanced Cybernetic Implant", "Cybernetic Implant", "Master Cybernetic Implant"; the Advanced pane reads "Feats Required: Advanced Cybernetic Implantation" (i08b). PASS.
- Ivy Ninety equips the Master Cybernetic Implant: "(Equipped)" (i08c). PASS.
- Ivy None, Advanced implant: the list rows are outlined red; picking it pops K2's generic box "You cannot equip this item. You don't have the prerequisites. Please see the item description." and the side pane reads "Feats Required: Advanced Cybernetic Implantation" (i08d). Refused: PASS. "Told which feat they need": the pane names it, the refusal line does not (same as TEST 178). PARTIAL.
- Note: the three feats and three implants draw no icons.
- **Item 8: PASS except the refusal line not naming the feat (PARTIAL).**
