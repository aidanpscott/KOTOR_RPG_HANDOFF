# TEST 147

First report of the new Tester session (the previous Tester froze after TEST 146). Screenshots: `HANDOFF/BUILD/screens/test-147/` (paths below are relative to it).

## Build

- App `KOTOR-RPG-APP` `origin/main` = `0b474daadef286d19aa939b956ccbe2447eca699` (fresh clone, `~/kotor-tester/`; no older clone or snapshot reused).
- `pubspec.lock` Lodestar `resolved-ref` = `df81340ec1278f1dd4ab0192969070a3667cda90`; my fresh Lodestar clone HEAD = `df81340`; pub-cache checkout `~/.pub-cache/git/Lodestar-df81340ec1278f1dd4ab0192969070a3667cda90` is present — all three match. Lens lock `2bad745a…` = Lens HEAD. After `flutter build` the snapshot's lock still reads `df81340…`.
- **The `linux/` runner IS committed** (`0b474da`): the snapshot built with NO `flutter create`, and the window opened at **1920×1080** (checked with `xdotool getwindowgeometry`).
- Built from `git archive origin/main` into `/tmp/test147-build`, `flutter build linux --debug` (host, `tool/env.sh`). Own Xvfb `:2` (1920×1080, PID recorded), app run with `XDG_DATA_HOME=$HOME/.local/share/tester-data`.
- Data directory seeded from Shelf `55cefa7`; `check_shelf.py` run **against my own directory** (`XDG_DATA_HOME` set): `✓ 30 rules files and 82 standard blueprints, all identical to what the extracts generate`. (Run bare it checks the shared `~/.local/share/kotor-rpg`, not mine — I caught that and re-ran.) The earlier Tester's old data dir was moved aside, not reused.
- Real KOTOR II was not launched. MAIN_WORK `676328fd`, HANDOFF `ddd1c96`.

## Verdict

Nothing severe. **Class Defence at level 1 agrees between the Character Sheet and a real fight's printed breakdown for every class in the work order's table (11 of 11, no mismatch).** A fight starts and plays at DEX 8, 12 and 18. The death path writes a real death, the defeat panel appears, Load Game lists the save and opening it shows the same panel. Armour was also changed for real (a Jedi robe taken off): Equip badge, Character Sheet and the fight line all moved 17 → 16 together — the check TEST 146 could not do. Two things were **not** seen: a DEX 18 fight where the *enemy* wins initiative (all 8 DEX 18 characters' fights went to the player), and anything above level 1. Several UI/save oddities are listed under "Seen, not in the order" for Main to rule on.

## 1. Environment — CONFIRMED

Chargen by real clicks (Human → class → Portrait, Origin, Gender, Background, Abilities, Skills, Feats, [Powers], Equipment, Name, Story → Play), into the package area, save, reload. Evidence: `01-library-own-data-dir.png` (20 packages in my directory), `02-package-menu-no-saves.png` ("no saves" on a fresh root), `06-play-entered-package-area.png`. The save landed in my directory only: `~/.local/share/tester-data/kotor-rpg/saves/avel-malick.sav` (and nine more by the end); the shared `~/.local/share/kotor-rpg/saves/` has no `avel-malick`. Reload: `23-reload-smuggler-restored.png` (Oreth Malick, Smuggler 1, 8 of 8, back in the arena, enemy at 51 of 60 — "a02-arena left you at 51").

## 2. Class Defence at level 1 — CONFIRMED, 11 of 11

Source read first: `MAIN_WORK/rules/CLASS-DEFENCE-01.md` (the offsets −1/−2 floor at 0, so Scout/Bounty Hunter/Medic read 0 at level 1; Jedi `k2-jedi-step` +2). Each row: Character Sheet "Defence", and the Defence line printed in the fight HUD. **Cause of the number is read from the printed line; no mismatch anywhere.**

| Class | DEX | Expected class bonus | Sheet | Printed fight line | Evidence |
|---|---|---|---|---|---|
| Soldier | 18 | 0 | 14 | `defence base 10 + Dexterity 4 = 14` | `08-sheet-soldier-defence-14.png`, `11-fight-starts-dex18-soldier.png` |
| Scout | 18 | 0 | 14 | `defence base 10 + Dexterity 4 = 14` | `36-…`, `37-…` |
| Bounty Hunter | 18 | 0 | 14 | `defence base 10 + Dexterity 4 = 14` | `38-…`, `39-…` |
| Medic | 18 | 0 | 14 | `defence base 10 + Dexterity 4 = 14` | `30-…`, `31-…` |
| Smuggler | 12 | +2 | 13 | `defence base 10 + Dexterity 1 + class 2 = 13` | `20-…`, `21-…` |
| Agent | 8 | +2 | 11 | `defence base 10 + Dexterity -1 + class 2 = 11` | `34-…`, `35-…` |
| Brawler | 18 | +2 | 16 | `defence base 10 + Dexterity 4 + class 2 = 16` | `32-…`, `33-…` |
| Jedi Sentinel | 18 | +2 | 17 | `10 + Dexterity 4 + armour 1 + class 2 = 17` | `40-…`, `41-…` |
| Jedi Guardian | 18 | +2 | 17 | same | `42-…`, `43-…` |
| Jedi Consular | 18 | +2 | 17 | same | `44-…`, `45-…` |

Notes (each is something I saw, not inferred): the printed line **omits the class term when it is 0** (Soldier/Scout/Bounty Hunter/Medic print no "class 0"), so from the line alone "0" and "not computed" look the same — the sheet equal to 10 + DEX modifier is what shows it is 0. The Jedi's "armour 1" is the Padawan Robe in their starting kit; the class term is still `class 2`. The Agent's DEX 8 fight also printed the *enemy's* attack against it: `sparring.arena.02: unarmed · rolled 11 — d20 8 + attack 1 + Strength 0 + closed on a ranged weapon 2 · needed 11` — "needed 11" equals the Agent's Defence 11 (`34-agent-dex8-enemy-first-needed-11.png`).
**Not checked:** any level above 1; the classes outside the table (Engineer, Marksman, Machinist, Treasure Hunter, Duelist, Saboteur, the three Sith, all prestige classes).

## 3. A fight starts whatever the Dexterity — CONFIRMED (one combination not seen)

- **DEX 18** — eight characters (Soldier Avel, Medic Nyla Mourn, Brawler Cassar, Scout Garon, Bounty Hunter Deneb Ordo, Jedi Sentinel Nyla Sabek, Guardian Teyla, Consular Veya): each fight started, drew the HUD and let me act. `11-fight-starts-dex18-soldier.png` (initiative Avel 19, Sparring Partner 5), `12-soldier-first-attack.png` (Blaster Rifle hit for 6, 54 of 60 left), then enemy turn, Mate's turn, back to the player.
- **DEX 12** (Smuggler Oreth): started, a full round played — my shot hit (51 of 60), enemy turn, Mate's turn, back to me (`20-…`, `25-smuggler-round-completes-dex12.png`).
- **DEX 8** (Agent Deneb Halcyon): the **enemy won initiative** (Sparring Partner 14, Deneb 9, Mate −3), acted first, and hit (10 → 8) — also starts and plays (`34-…`).
- **Not seen: DEX 18 with the enemy winning initiative.** In all eight DEX 18 characters' fights the player was first (their initiative against the enemy: 19–5, 22–4, 15–0, 5–(−2), 17–7, 9–(−1), 15–(−2), 10–10 tie). I did not engineer that case.
- Also seen: initiative is **identical after a reload** (Oreth 19 / Partner 12 / Mate 7 both before and after: `20-…` vs `24-reload-same-initiative.png`); a **10–10 tie** (Consular vs Sparring Partner) listed the player first (`44-…`).

## 4. The death path in real play — CONFIRMED

Soldier Avel Malick (DEX 18, 12 vitality), passing every turn, Mate also passing, against the arena's unarmed Sparring Partner. Avel went down (`13-…`), Mate fell later; the panel appeared: **"Your entire party has been killed. … Nobody is left standing, so there is no end of battle. the newest save is this one — it already records the defeat."** with "Go to Load Game List" / "Main Menu" (`15-defeat-panel-in-play.png`). **The death is real, from the save file I parsed** (`avel-malick.sav`, 44 events): `character.dying` ×1, `character.died` ×2 — `{"subject":"Avel Malick","encounter":"a02-arena"}` and `{"subject":"mate.room.01","encounter":"a02-arena","x":3,"y":2}`. Load Game lists "Avel Malick — level 1 soldier · a01-room · 6 minutes ago" (`17-…`); clicking the row opens **the same panel text** (`18-defeat-panel-after-load.png`), on a plain black backdrop instead of the dimmed play view.
Three things on this path, for Main (none blocks it):
- **"Go to Load Game List" does not go to the list.** It lands on the package menu (Continue / New Game / Load Game…), and the list is one more click (`16-go-to-load-game-list-lands-on-package-menu.png`). PARTIAL against the label.
- **The defeat save's location reads `a01-room`, though the party fell in `a02-arena`.** A live save made while in the arena lists `a02-arena` (`60-load-list-raw-class-ids.png`). In the file: Avel's save has **no `character.moved` for the player** at all (only Mate's, in `a01-room`); Oreth's has one into `a02-arena` (4,1). *Likely cause, not shown:* the defeat write doesn't update the area/position the way the leave-session write does. Whether a stale area is intended on a defeat save is Main's ruling.
- **Damage keeps landing on a downed character.** The sheet/panel stop at "0 of 12", but the status line read `Avel Malick: -11 of 12` and later `-41 of 12` (`13-…`, `14-status-line-minus-41.png`) while the enemy went on hitting Avel and Mate. Question for Main: is continued damage to a character already at 0 intended, and should the line show a negative number?

## 5. The play view under menus — CONFIRMED for the two named things; the rest listed

Opened Options (Esc), Character, Inventory, Equip from play (`07-menu-options-from-play.png`, `08-…`, `09-…`, `10-…`). **The keyboard hint line ("arrows to move…") is not drawn on any of them, and the area name (`Room`/`a01-room · 1, 2`) is not drawn on any of them** — it does appear at the bottom-left of the plain play view (`06-…`). Still showing through, as seen:
- **The status line** (last event text) on all four, including a stale one: `mate.room.01 is with you — there is no way past without walking round` (left by my own first click) sits under Options, Character, Inventory and Equip.
- **The party column** ("your party", portraits, Mate's Wait here / Dismiss from party / Trade / Change Doctrine) on Options, Character and Inventory — not on Equip.
- **In a fight, the fight HUD** shows through under every menu: turn order, the move/action/gear/reaction legend, the Defence line and the hotkey line `f powers · c scan · d disengage · s hide · h hurry · t treat · r repair · o throw · g gear · space to end your turn` (`21-smuggler-sheet-defence-13.png`, `22-save-game-not-built.png`).
- **The menu layout is not the same size in a fight as out of one, and it moves with the HUD height** (icon bar at x≈1166–1631 out of a fight; ≈1265–1655 in most fights; ≈1222–1676 in the Agent's fight). I did not test Equip's look, as ordered.

## 6. Armour changed for real, three readers re-checked — CONFIRMED for taking armour off (re-equip not tested)

TEST 146 could not change armour. A Jedi starts in a Padawan Robe, so I did it. Jedi Sentinel Nyla Sabek, **out of combat** (loaded from her save): Equip badge **17** (`52-armour-before-badge-17.png`) → slot icon → None → OK → status "you take off robe-1", badge **16** (`53-robe-off-badge-16.png`); Character Sheet Defence **16** (`54-robe-off-sheet-16.png`); the next fight's printed line `defence base 10 + Dexterity 4 + class 2 = 16` — the armour term gone (`55-robe-off-fight-line-16.png`). All three read 17 before (sheet `41-…`, line `40-…`). **In combat the game refuses**: `equipping is refused in combat — change your gear before or after the fight` (`51-equipping-refused-in-combat.png`). The pick only applies from the slot icon → row → OK; a row click alone, Return and a double-click did nothing (Equip is mid-rebuild, so I am noting this, not filing it). **Not tested:** putting the robe back, or any armour other than the starting robe.

## Seen, not in the order (observations for Main; I ruled nothing)

- **Equipment step shows authoring text as a player label:** `TAKES THE CLASS'S OWN melee UPGRADE FROM §4a — Soldier → Long Sword + Short Sword or a Double-Bladed Sword; Scout → …` (`05b-equipment-step-authoring-label.png`, every class).
- **Equipment step: OK stays disabled with no reason given** until the "Standard Gear" tab is clicked; choosing the profession option alone leaves it grey (`05-equipment-ok-disabled-until-standard-gear.png`; enabled after clicking the tab: `05c-equipment-ok-enabled-after-standard-gear.png`). The tab shows no selected state before that click.
- **Stale hub copy:** "Every step is built, so Play unlocks once all of them are done. It does not lead anywhere yet: your character is not written down and nothing is saved." — Play does enter the game and does write a save (`03-chargen-hub-stale-play-copy.png`, `61-force-hub-stale-play-copy.png`).
- **Load Game rows show raw class ids** for two classes: `level 1 jedi_sentinel`, `level 1 bounty_hunter`, against plain `smuggler`/`scout`/`agent` (`60-load-list-raw-class-ids.png`).
- **Inventory lists item ids, not names**, and `blaster-rifle ×2 (Equipped)` / `short-sword ×2 (Equipped)` for a kit of one each (`09-inventory-from-play.png`) — possibly the party's counts merged; not shown.
- **"N rules about this character not checked"** appears on every fight and the count changes across a reload for the same character (Oreth 2 → 1 after reload; Nyla 1 → 2) — meaning not shown.
- **In-game SAVE GAME still reads "not built yet"** (`22-save-game-not-built.png`), as in TEST 146; the saves here are the autosaves. "Recommended" on Background/Abilities/Skills/Feats says "no recommended choice is in the rules yet" (PT-2679, expected).
- **Characters** (library top bar) says "nothing is built beyond this screen yet".

## What I did not check

DEX 18 + enemy-first; levels above 1; the classes outside the table; re-equipping armour; any armour but the Padawan Robe; K2 comparisons (not asked); Equip's appearance (ordered not to).

## Method note

One false start of mine, found and fixed: the app grows a 10×10 helper window at (−100,−100), and `xdotool search --pid | tail -1` picked it, offsetting every click by −100 for a stretch (the Story button looked dead). It was my helper, not the app — I confirmed it by listing the PID's windows with geometry, and the helper now picks the 1920×1080 window. A stray click of mine also moved Nyla one tile (status `a02-arena · 4, 0`), which I checked against her save before not reporting it.

Skills used: `verification-before-completion` (every CONFIRMED above has a screenshot or a parsed save line; the save-header finding is labelled "likely cause, not shown"); `diagnosing-bugs` method for the dead-click narrowing; `research` reading of `CLASS-DEFENCE-01.md` before judging the numbers; `writing-for-agents` for this report. `handoff` not run: `TEST/TESTER-STATE.md` is current and this session ends with the filing.
