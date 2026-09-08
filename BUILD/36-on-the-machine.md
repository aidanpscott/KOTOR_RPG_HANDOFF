# 36 · On the machine, and runnable

**Nothing was cloned, because nothing needed cloning.** All six repositories
were already on this machine and pointing at the right remotes. **Cloning again
would have made a second tree that goes stale** — the exact problem the brief
warns about — so what was missing was **findability and a way to run them**, and
that is what was added.

---

## 1 · Where everything is

    /home/aidan/step1            ⚠ the real path — all six, one tree
    /home/aidan/kotor-repos      the same folder, obvious name (a SYMLINK, not a copy)

| folder | remote |
|---|---|
| `Lodestar/` | `aidanpscott/Lodestar` |
| `Lens/` | `aidanpscott/Lens` |
| `Loom/` | `aidanpscott/Loom` |
| `KOTOR-RPG-APP/` | `aidanpscott/KOTOR-RPG-APP` |
| `MAIN_WORK/` | `KOTOR_RPG_MAIN_WORK` |
| `HANDOFF/` | `KOTOR_RPG_HANDOFF` |

**⚠ `MAIN_WORK` and `HANDOFF` are in the same tree as the other four.** There is
one place to find, not two.

**The other contents of that folder are working files, not repositories** — 86
loose `.png` captures and `extract/`.

**⚠ A full map is at `/home/aidan/step1/README.md`**, copied here as
`docs/RUNNING-ON-THIS-MACHINE.md`. It is not in any repository otherwise,
because the tree root is not itself a repo.

---

## 2 · ⚠⚠ Running them — and the thing that would have stopped you

    cd ~/kotor-repos
    ./run-app.sh      the play client
    ./run-loom.sh     the Builder

**Both were run and screenshotted. Both work.**

> **⚠ `flutter build linux` fails on this machine with *"CMake is required for
> Linux development. It is likely available from your distribution."* — and
> CMake IS installed.**

**Flutter, CMake, Ninja and Clang are all under `~/spike`, not on the system
PATH**, and CMake additionally needs `librhash.so.1` from `~/spike/prefix`.
Three lines fix it and they are in `~/kotor-repos/env.sh`:

```sh
export PATH="$HOME/spike/flutter/bin:$HOME/spike/prefix/usr/bin:$HOME/spike/tools:$PATH"
export LD_LIBRARY_PATH="$HOME/spike/prefix/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
```

**⚠ That is the single thing most likely to have made this look broken**, and
the error message points the wrong way.

**For hot reload:** `. ./env.sh` then `flutter run -d linux` from `Loom/` or
`KOTOR-RPG-APP/`.

**What appeared:**

- **Loom** — three panes, `no package open`, **New package / Open package**.
  The tree shows areas, conversations, blueprints (ten kinds, `doctrines` among
  them) and scripts.
- **The play client** — ⚠ **it resumed.** It opened straight into **Character
  Generation · Ability Scores on Taris Undercity**, because the console
  remembers the last screen. **That is working as designed and will surprise
  you if you expect Console Home.**

---

## 3 · ⚠ The seam, verified on the real folder rather than a temp one

    ~/.local/share/kotor-rpg/packages/    base-rules · endar-spire · taris-undercity
    ~/.local/share/kotor-rpg/saves/
    ~/.local/share/kotor-rpg/console/

**Both programs resolve `/home/aidan/.local/share/kotor-rpg/packages` and both
see all three packages.** Checked by running `Locations.desktop()` from inside
each of the two repositories, on this machine, against the real directory —
**not the temp directory `PT-1382`'s own test uses.**

**And the strongest evidence is incidental:** the app resumed onto **Taris
Undercity**, a package Loom's world sits in, without being told where to look.

**⚠ The folder is named for the PRODUCT** — `kotor-rpg` — **not for either
program**, which is `PT-1382`'s point and is why the seam holds.

---

## 4 · What works, and what is scaffolding

**Both lists are in the README** and are the part worth reading before touching
anything. **In short:**

**Loom authors:** a package and its properties · an area, its tiles, its
doorways and arrival points · a creature with equipment, a conversation and a
doctrine · a placement · **a conversation from nothing** · **a doctrine**.

**The client does:** Console Home · import · all nine chargen steps, organic and
droid · save, load, continue · walking and travelling between two areas · a
conversation with checks and a typed box · a fight that starts because an author
said so.

**⚠ Nine things look like defects and are placeholders**, each with the ruling
that made it one — a circle for a character (`PT-1319`, no portrait art), a flat
board (`§2b`'s untextured default), **a fist** (nothing resolves equipment in
play yet, though the trooper carries a rifle in its blueprint), a talking Sith
trooper, a hardcoded purse, and four more. **The full table is in the README.**

**⚠ AND THE BIGGEST ONE IS NOT A BUG AT ALL: nothing has been designed.**
`UI-STYLE-VALUES-01 §7`'s sizes are re-derived against a real viewport now —
that was `BUILD/32` — **but typography, palette and framing have never been
touched.** What you will see is structure at a correct scale.

---

## 5 · Nothing was built

No code changed. **Three files were added to the tree root** — `README.md`,
`env.sh`, `run-app.sh`, `run-loom.sh` — and one symlink, `~/kotor-repos`. **The
tree root is not a repository**, so the README is copied into `docs/` here to
keep it somewhere versioned.
