# TEST 174 — recheck of the TEST 173 fixes, the feat tier icons and the companion faces

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-174/` (MAIN_WORK `9d6b0b57`). Read first: Coder's entry for the tier icons and the TEST 173 fixes.

## Build

App `aa27d234a94ab20658015fbcd8909a7cf4735d9a` (git archive, snapshot `/tmp/test174-build`). Lodestar `be1319a5020337e561e6094bd7d2784e866d0045` = lock. Shelf `4162b8943a0943632f86b4e519dfe02503757ee1` (my data dir). check_shelf clean (31 rules, 111 blueprints). Fresh fixtures.

## Summary: five pass, one fails on the party bar

| # | Check | Result |
|---|---|---|
| 1 | Store boots | **PASS**: in Store Bed, Dockworker's Treads and Spacer's Magboots each show K2's empty slot frame, not a blank; "Spacer's Magboots" keeps its apostrophe and costs 75 (`1a`). Inventory and Equip read "Spacer's Magboots" and "Dockworker's Treads" (`1b`, `1c`, `1d`). No lost apostrophe and no "Spacer S" found. The only apostrophe item names a character can reach are these two: every other one is in base-rules `items.toml` and no store or start kit uses it |
| 2 | Feat tier icons | **PASS**: Feat Bed (Jedi Sentinel 1): Two-Weapon Fighting → Advanced Two-Weapon Fighting draws K2's icon; Force Jump → Force Jump Advanced and Unarmed Specialist I → Unarmed Specialist II–VIII also draw theirs (`2a`, `2b`, `2c`). None of the three was out of reach |
| 3 | World text | **PASS**: Korriban now reads "…Czerka keeps its sector headquarters here…" (lower case). Dantooine, Tatooine, Kashyyyk, Manaan, Lehon, Yavin, Telos IV and Onderon all read without shouting (`3a`, `3b`) |
| 4 | Faces | **FAIL (party bar only)**: footer: Kael, Mate, Shooter, Grunt and Guardian each have their own face, no two alike, none the default (`4a`). Bookmarks on a manual save: each one's own face (`4b` Guardian + Grunt, `4c` Kael, `4d` Mate, `4e` Shooter). **The party bar draws no portrait for anyone**, the player included: empty squares (`4g`). Also: **Auto Save bookmarks never show companions**, only the player in the middle slot, even a fresh Auto Save written beside a manual save that does show them (`4f`) |
| 5 | Abilities quick look | **PASS**: Skills, Powers and Feats tabs; Feat Bed (Sentinel 1, no powers) shows an empty Powers list and only its own feats (`5a`, `2a`); clicking Kael's tile in the footer switches the name and face to Kael (`5b`); the list panes show a scroll bar |
| 6 | Quick regression | **PASS**: boots off and on (`6a`). Help box after a zoom, closed by Escape: board zoomed out with the wheel first, then Inventory, Map, Abilities and Journal first-open boxes each closed by Escape and the screen stayed open (`6b`, `6c`, `1d`). "Kael is surprised" (`6d`). Enemy-turn hold: Options open 10 s on a Sentry Droid's turn; frames taken every 0.1 s after closing show the old line for about 1 s, then the hit lands (Zed 8 → 6) (`6e`, `6f`). Escape+F4 ×3: one quick.mark rewritten each time, nothing else written, no error |

## Notes (not failures)

- **The Map shows the hidden droid.** In Precognition Ambush, before any fight, the board shows one droid east of you and the Map shows two (column 7, rows 3 and 4) (`6c`, lower panels). The turn order later lists the second one as "hidden".
- Weapon Proficiency: Blaster has an empty icon cell in the Feats list (`2b`, second row).
- The board zoom only zooms out: the wheel up stops at the fitted size. My first "zoom" did nothing until I scrolled down (Tester-side note).
- Every new human character I made (Ion Tess, Zed Moor, and the earlier Ren Volt) got the same player portrait.
- Base-rules item names carry a double space before "UNIQUE" ("Bastila's Lightsaber  UNIQUE") and one is "<FullName>'s Armband". No character can reach these yet.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
