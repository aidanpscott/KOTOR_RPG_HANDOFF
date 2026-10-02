# TESTER-STATE — rewritten each report; a fresh session resumes from this alone

**Last filed report: TEST 147** (2026-10-02). Next number: 148. Nothing half-done.
Work order done in TEST 147: environment proof; class Defence L1 (11 classes); fight start at DEX 8/12/18; death path; play view under menus; plus an armour-off Defence re-check.

## Where things are (Aaron's PC; commands run on the HOST via `flatpak-spawn --host sh -c '…'` from the VS Code sandbox)
- Clones (all fresh 2026-10-02): `~/kotor-tester/{KOTOR-RPG-APP,Lodestar,Lens,Shelf,KOTOR_RPG_MAIN_WORK,KOTOR_RPG_HANDOFF}`. HANDOFF has `core.hooksPath=.githooks` (blocks font files). Never use `~/kotor-home/` (Coder's) or `/mnt/ga/...` (stale).
- **Last build block:** app `origin/main` = `0b474daadef286d19aa939b956ccbe2447eca699`; lock Lodestar `df81340ec1278f1dd4ab0192969070a3667cda90` = Lodestar HEAD = `~/.pub-cache/git/Lodestar-df81340…`; Lens `2bad745`; Shelf `55cefa7`; MAIN_WORK `676328fd`; HANDOFF `ddd1c96` at clone. The `linux/` runner is committed — a snapshot needs NO `flutter create`; window opens 1920×1080.
- Build: `git archive origin/main | tar -x -C /tmp/test147-build` (host /tmp), then `. tool/env.sh && flutter build linux --debug` (~30 s cold). Re-snapshot from a fresh `origin/main` for the next work order; record the new head.
- Data dir: `XDG_DATA_HOME=$HOME/.local/share/tester-data` (app appends `kotor-rpg/`). Seeded from Shelf `main`; the prior Tester's dir is at `~/.local/share/tester-data.old-prior-tester-2026-10-02` (not used). Ten TEST 147 saves are in `tester-data/kotor-rpg/saves/` (avel-malick = the defeat save). Re-seed, then `XDG_DATA_HOME=… python3 KOTOR_RPG_MAIN_WORK/scripts/check_shelf.py` before testing (run bare it checks the *shared* dir, not yours).
- Display: own `Xvfb :2` (1920×1080); PIDs in `~/kotor-tester/run/xvfb.pid` and `app.pid`. Kill only those PIDs. Other agents' `Xvfb :99` is not yours.
- Helpers in `~/kotor-tester/run/` (not committed): `c.sh X Y [btn]` (pointer by `xdotool --window`, click without it), `k.sh KEY`, `s.sh NAME` (→ `~/kotor-tester/shots/`), `cg1.sh CLASSY STR DEX CON INT WIS CHA` (chargen to the ability step), `cg2.sh TAG` / `cg2j.sh TAG` (Equipment → Play → round the Dummy → arena → fight; `j` for Force classes), `cgj1.sh`, `openarena.sh`, `launch.sh`.

## Traps learned (each cost time)
- The app grows a **10×10 helper window at (−100,−100)**; `xdotool search --pid | tail -1` picks it and offsets every click by −100. `c.sh` picks the window whose geometry is 1920x1080.
- **Menu layout moves**: in a fight the icon bar / Options rows sit at different coordinates than out of a fight, and vary with the fight HUD height. Take a screenshot before clicking Options → LEAVE SESSION → the red LEAVE SESSION confirm.
- Esc from play opens Options; if a menu is already open Esc closes it (my leave script then clicked into the fight). The top bar only exists after Esc.
- Skill rows shift up as ranks go in; click bottom-to-top and check "0 of N" before OK. Selecting a power expands its text and moves the rows below.
- Equipment step: OK stays disabled until the "Standard Gear" tab is clicked.
- Enemy attack lines are overwritten by the next actor's status line; the *current actor's* Defence line ("defence base 10 + …") is always printed and is the readable breakdown. An enemy-first fight (Agent, DEX 8) keeps the enemy's line on screen.
- Equipping is refused in combat; armour changes go slot icon → row → OK, out of combat. Initiative is deterministic per campaign seed (identical after a reload).
- `tester-xp-bed-arena`: the Veteran Dummy next to the start gives 3000 XP and would level the character — walk the bottom row (tiles (1,2)→(4,2)→(5,2)) to the door at (5,1). The Sparring Partner (60 vit, unarmed) in the arena is the fight.

## Still untested / open for a later order
DEX 18 fight where the enemy wins initiative; Defence above level 1; classes outside the CLASS-DEFENCE table; re-equipping armour and any armour but the Padawan Robe; mine tiers above Minor; the companion sheet with levelled data. Findings awaiting rulings are in TEST 147 ("Seen, not in the order").

## Skills (MAIN → TESTER work order, 2026-10-02) — user-level, NEVER committed into any KOTOR repo
Found already installed on this PC (not reinstalled):
- Matt Pocock's skills: git clone at `~/.local/share/agent-skills/mattpocock-skills` (head `d81f3a1`, "release v1.3"), symlinked into `~/.claude/skills` (the skills.sh/tinkerer route; the README's alternative is `claude plugins install mattpocock-skills`).
  Tester's set from it: `diagnosing-bugs` (narrow to a smallest repro), `research` (check what a rule says in the corpus), `writing-for-agents` (reports a fresh reader can act on), `handoff` (run before the session grows).
  Not used by Tester: tdd, implement, implement-spec, to-spec, to-tickets, triage, code-review, setup-matt-pocock-skills (nothing here writes code or tickets; setup would write config into a cwd).
- obra/superpowers `verification-before-completion`: `~/.claude/skills/verification-before-completion` (installed by Coder, PT-2722; SOURCE.txt: commit `8ca22db`, MIT).
Not installed, on purpose: obra/superpowers `systematic-debugging` (overlaps `diagnosing-bugs`; its Phase 4 is about implementing fixes). To add it later:
`git clone --depth 1 https://github.com/obra/superpowers.git <scratch> && cp -r <scratch>/skills/systematic-debugging ~/.claude/skills/ && cp <scratch>/LICENSE ~/.claude/skills/systematic-debugging/`
To reinstall Matt's set on a fresh machine: `claude plugins install mattpocock-skills` (or `npx skills@latest add mattpocock/skills`, run from a scratch folder, not a repo).
Rules: every CONFIRMED carries its evidence; every FAILED its smallest repro; "cause, shown" only when demonstrated, otherwise "likely cause, not shown"; verdict first; end the report with which skill was used where.
