# TEST 220: fights on sight, Hide outside a fight, parley at range, the Acolyte robes, "if_", the Jedi Defense robes, named lines

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-220/` (MAIN_WORK `e3743c59`).

## Build

- **App**: main `83f6c4b`, a worktree beside my clone. `gate.py --at 83f6c4b`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 83f6c4b, 5443 tests, 0 failed"; ARCHIVE last green at 83f6c4b. Reads SENDABLE, as expected. Lodestar `4e71520` = lock = compiled; built through the lock in 10.0 s; git status clean.
- **Settings**: defaults. **Shelf** `dd00ad7`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test220_saves.dart` (Sight One, Sneak One, Parley One). My own **tester-220** (faction Republic): "Stranger Yard" with a faction-less Stranger 6 squares off; Stranger Watch (Soldier 4) and Robe Soldier 220 (Soldier 10, no Jedi Defense, carrying Star Forge Robes and Darth Revan's Robes). Reused Armor Jedi (armor-219) and Twin One. Chargen: Open Soldier 218 and Frail Sage 218 rebuilt with TEST 218's steps; a Human Sith Warrior Acolyte.

## Summary: one finding (the "if_" fix doesn't hold), one small item, one part not reachable

| # | Check | Result |
|---|---|---|
| 1 | On sight | **PASS, one part not reachable**. Sight One: the fight is on at arrival, "initiative — Sight One 10 · Sith Lookout 2", no step or bump. Sneak One: s → "hidden"; one step right → "hidden — d20 9 + Stealth 8 + Dexterity 4 = 21 beat 2"; four more steps, no second roll; walking into the sentry → "initiative — Sneak One 22 · Sith Sentry 14", log "Sneak One is hidden. / A fight begins.". Parley One: on arrival, 7 squares off, "Sith Officer: This deck is sealed. Turn around." with the six replies; "5. Stand aside." → "Then you die here." and the initiative. The Stranger: 3 squares off in plain sight, no fight; walking into it starts one ("Stranger: unarmed … — miss"). Loading a mid-fight quick save (Sight One and Parley One): "the fight resumes — round 2, … turn", no new fight, no second call. **Not reachable**: Sneak Attack dice from hiding: Sneak One holds no Sneak Attack (Feats: Blaster, Blaster Rifle, Light armour, Melee only); its first swing read "Vibroblade · rolled 8 … needed 10 — miss" |
| 2 | The opening | **PASS**. Open Soldier 218: room 3 starts as I come through ("initiative — Open Soldier 218 20 · Trask Ulgo 18 · Sith Soldier −3"), room 4 too ("… 19 · Sith Soldier 10 · Trask Ulgo 3"), the hall ("Trask Ulgo is waiting on you"), the bridge ("… 17 · Trask Ulgo 12 · Sith Soldier 11"). Trask still waits in the quarters until stepped into ("We've been ambushed…"). Survival: no moment I could have died before acting; she finished the bridge at 12 of 12 |
| 3 | Chargen Acolytes | **PASS**. Jedi Consular: "Jedi Robe — Regenerate Force Points: 1". Sith Warrior: "Dark Jedi Robe — Regenerate Force Points: 1", and she starts in "Dark Jedi Robe (Equipped)". Soldier: "Acolyte's Vestments — Saves: Will +2", worn ("Acolyte's Vestments (Equipped)"), pane "Defense Bonus: 0 · Saves: Will +2 · Plain vestments for one who serves the Force without the Jedi's training.". The aptitude row reads "Aptitude: Mysticism", no robe |
| 4 | "if_" | **FAILS — finding 1** |
| 5 | Jedi Defense robes | **PASS**. Robe Soldier 220: Star Forge Robes and Darth Revan's Robes both red; OK on each: "You cannot equip this item. You don't have the prerequisites. Please see the item description." with "Jedi Defense" under it |
| 6 | Lines | **PASS on the lines, small item 1 on the sheet**. Armor Jedi with Force Aura up: her Defense line "Defense base 10 + Dexterity 1 + class 6 + Force Aura 2 = 19"; the Ironhide's line "needed 19 (+2 Force Aura) — hit". Twin One's off hand: "damage 2 — 1d10 1 + Strength (off hand) 1". No "power" anywhere |
| 7 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 57 ("reg220"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 89 of 196) |

## Findings

1. **The "if_" underscore still moves with the name.** Rebuilt with TEST 218's exact steps (Human Soldier / Bith Jedi Consular, Taris, Upper City Persuade, Noble, Acolyte), the summary story box reads:
   - Open Soldier 218 (`t220-story-os.png`): "Ask where Open Soldier 218 is from and you get Taris, eventually. Ask what they did there and you get Acolyte, immediately. The Noble part comes la_st, if at all. Soldier: The professional."
   - Frail Sage 218 (`t220-story-fs.png`): "… The Noble part comes last, if_ at all. Jedi Consular: The Force is the weapon."

   The same two texts as TEST 218, character for character.

## Small

1. With Force Aura up, Armor Jedi's Character sheet reads Defense 17 (10 + 1 + 6) and names no Force Aura anywhere (Stats, Character Info), while the fight's own Defense line reads 19 with "Force Aura 2". The order asked for it by name "on her own sheet"; it shows on her fight line only.

Seen, not filed:
- My first pass at the Tester Attacks card opened Opportunity Attacks (a script fault; fixed).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
