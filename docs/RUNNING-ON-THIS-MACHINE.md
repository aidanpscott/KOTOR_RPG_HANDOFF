# KOTOR RPG — where everything is, and how to run it

**Everything is already on this machine.** Nothing needed cloning; the six
repositories below were cloned here as the work was done, and they all point at
`github.com/aidanpscott`.

    /home/aidan/step1            ⚠ the real path
    /home/aidan/kotor-repos      the same folder under an obvious name (a symlink)

---

## The six

| folder | repo | what it is |
|---|---|---|
| `Lodestar/` | `aidanpscott/Lodestar` | **the engine.** Every format reader, the ledger, combat, projections. No UI. |
| `Lens/` | `aidanpscott/Lens` | **the shared draw layer.** The board, drawn once for both programs. |
| `Loom/` | `aidanpscott/Loom` | **the Builder.** Makes packages. |
| `KOTOR-RPG-APP/` | `aidanpscott/KOTOR-RPG-APP` | **the play client.** |
| `MAIN_WORK/` | `KOTOR_RPG_MAIN_WORK` | **the design corpus** — `design/`, `rules/`, `playtest/`, `scripts/`. |
| `HANDOFF/` | `KOTOR_RPG_HANDOFF` | **what you read** — `BUILD/`, `STUDY/`, `docs/`, `BUILD/screens/`. |

**⚠ All six are in one tree.** `MAIN_WORK` and `HANDOFF` are not somewhere else.

**The other things in this folder are working files, not repositories:** 86 loose
`.png` captures from earlier passes, and `extract/` from the data extraction.

---

## Running them

    cd ~/kotor-repos
    ./run-app.sh      the play client
    ./run-loom.sh     the Builder

**Each builds on first run (a minute or two) and starts instantly after.**

**⚠ WHY THERE IS A SCRIPT RATHER THAN A COMMAND.** Flutter, CMake, Ninja and
Clang are installed under `~/spike`, **not on the system PATH**, and CMake needs
a library from the same place. Run `flutter build linux` without that
environment and it stops with **"CMake is required for Linux development"** —
which is misleading, because it is installed. `env.sh` is those three lines;
the scripts source it.

**To develop rather than just run** — hot reload, from either repo:

    cd ~/kotor-repos && . ./env.sh
    cd Loom            # or KOTOR-RPG-APP
    flutter run -d linux

**To run the tests:**

    cd ~/kotor-repos && . ./env.sh
    cd Lodestar && dart test          # 270
    cd ../KOTOR-RPG-APP && flutter test   # 206
    cd ../Loom && flutter test            # 111
    cd ../Lens && flutter test            # 4

---

## ⚠ Where the packages are

    ~/.local/share/kotor-rpg/packages/
        base-rules/          the rules the game ships with
        endar-spire/         the two-area test bed
        taris-undercity/     a second package

    ~/.local/share/kotor-rpg/saves/     save files
    ~/.local/share/kotor-rpg/console/   which screen you were last on

**⚠ The folder is named for the PRODUCT, not for either program** — `PT-1382`.
Loom writes there and the app reads there; **verified on this machine**, both
resolving `/home/aidan/.local/share/kotor-rpg/packages` and seeing all three.

**Open that folder and you will see directories, not archives.** A package is a
folder of TOML files — `PACKAGE-FORMAT-01 §2`: *"`git diff` works. A modder can
look."*

---

## What works today

**Loom — you can author:**

- a **package** (New package), and its properties: authors, summary, cover,
  requires, continues, entry area
- an **area**: a grid, tiles painted square by square, doorways and arrival
  points placed on the grid
- a **creature**: name, class, level, abilities, hit die, protection,
  equipment, a conversation and a doctrine
- a **placement** — a creature put on a square
- a **conversation**: lines, replies, links, gates, effects — from nothing
- a **doctrine**: a goal, a break-off rule, exclusions and preferences

**The play client — you can:**

- open **Console Home**, import a package, pick one
- run **all nine character-generation steps**, for an organic or a droid
- **save and load**, and continue where you left off
- **walk** a grid and travel between two areas through a door
- **talk** to a creature that has a conversation — options, checks, a typed box
- **fight** — initiative, turns, damage, dying, and a wound that survives
  leaving the room

---

## ⚠ What is scaffolding, so you are not surprised

**These look like defects and are placeholders with a reason.**

| what you will see | why |
|---|---|
| **the player is a circle, enemies are dots** | `PT-1319` ruled a character is a portrait and nothing animates; **no portrait art exists yet.** |
| **the board is flat colour with thin lines** | `AREA-FORMAT-01 §2b`'s untextured default. **No tileset art exists.** It is a preference, not a missing file. |
| **you punch** | nothing resolves equipment in play yet. The trooper *carries* a blaster rifle in its blueprint; `strike()` still uses a fist. |
| **the trooper talks before it shoots** | it is the only creature in the bed, and its conversation ends in a fight when you push it. |
| **`[Bribe · 50 credits]` always shows** | nothing projects a purse; the credits are a named placeholder constant. |
| **50 credits does not leave your pocket** | the effect is written to the log and nothing spends it yet. |
| **conversations look plain** | `UI-STYLE-VALUES-01 §7`'s sizes are re-derived against a real viewport now — **but nothing has been designed.** Typography, palette and framing are all untouched. |
| **`conversati…` in Loom's tree** | the pane is narrower than the word. |
| **Loom's palette cuts off** | it lists ten blueprint kinds and fits about nine. |

---

## Where to read

**`HANDOFF/BUILD/`** — one numbered note per slice, newest last.
**`HANDOFF/BUILD/screens/`** — every capture.
**`HANDOFF/docs/`** — the format documents: `PACKAGE-FORMAT-01`,
`AREA-FORMAT-01`, `DIALOGUE-FORMAT-01`, `DOCTRINE-FORMAT-01` and the rest.
**`HANDOFF/STUDY/`** — the source studies, `01` to `18`.
**`MAIN_WORK/playtest/PLAYTEST-RULINGS-01.md`** — every `PT-` ruling.
