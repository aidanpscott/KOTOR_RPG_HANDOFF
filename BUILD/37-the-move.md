# 37 · The tree moves to the Steam library

**No code was built.** All six repositories moved from `/home/aidan/step1` to
`/mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT`, because the owner
wants them where the games are.

**270 Lodestar · 4 Lens · 111 Loom · 202 app +4 failing.** ⚠ **The four
failures are pre-existing and are not the move** — §5.

---

## 1 · ⚠ The control came first, and it is the whole reason this is trustworthy

**Every suite was run BEFORE the move and the numbers written down**, because a
move that breaks something and a tree that was already broken look identical
afterwards.

| | before | after |
|---|---|---|
| `Lodestar` | **270** pass | **270** pass |
| `Lens` | **4** pass | **4** pass |
| `Loom` | **111** pass | **111** pass |
| `KOTOR-RPG-APP` | **202** pass · **4 fail** | **202** pass · **4 fail** |

**Identical, and the four failures are the same four by name.** The move
changed nothing, and that is a measurement rather than a hope.

---

## 2 · What actually broke, which was less than expected

**⚠ THERE IS NO PATH DEPENDENCY, AND THE BRIEF SAID THERE WAS.** `Lens` and
`Lodestar` are consumed as **git dependencies** —

```yaml
  lens:
    git: {url: https://github.com/aidanpscott/Lens.git, ref: main}
```

— so they resolve through `~/.pub-cache/git/`, which is under `$HOME` and did
not move. **Zero `step1` references in any `package_config.json`**, checked in
all four packages. Nothing about the inter-repo wiring depended on where the
tree sat.

**⚠ And that has a consequence worth writing down: `Loom` and the app consume
`Lodestar` and `Lens` from GitHub at `ref: main`, not from the sibling folder.**
An uncommitted change in `Lodestar` does not reach either front-end until it is
pushed. That is true today and was true before the move.

**Two things did break, both hardcoded absolute paths:**

    KOTOR-RPG-APP/test/capture_test.dart           '/home/aidan/step1/HANDOFF/BUILD/screens'
    KOTOR-RPG-APP/test/capture_dialogue_test.dart  same

**⚠ A capture test does not assert, so this would have failed silently** — it
creates its output directory, writes 29 PNGs into it and passes. After the move
it would have made a folder somewhere useless and reported success.

**Fixed as `../HANDOFF/BUILD/screens`, relative, and the justification was
already in the file.** `font = 'assets/fonts/DejaVuSans.ttf'` sits three lines
below `out` and has always worked, **which proves `flutter test` runs with the
package root as CWD.** The sibling constant was the control; the path shape was
known-good and only `out` disagreed. Relative also encodes the invariant the
tree really has — six repositories as siblings — so it survives the next move.

**Six `extract/*.py` scripts** also carried absolute paths. Those are run
ad-hoc from an unknown working directory, so **absolute is the right shape
there** and they were repointed rather than made relative. Different answer for
a different caller, on purpose.

---

## 3 · ⚠ `~/kotor-repos` is the load-bearing piece

The symlink was repointed, **not deleted**, and it is why the move was cheap:

    /home/aidan/kotor-repos -> /mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT

**Every instruction in `README.md`, `RUNNING-ON-THIS-MACHINE.md` and
`PLAYTEST-S01-FEEDBACK.md` says `cd ~/kotor-repos`** — so all of them stayed
correct without being touched. **The playtest document the owner is about to
use did not need a single edit.**

**⚠ `BUILD/36` was NOT rewritten**, though its paths are now wrong. `README.md`
in this directory says a slice file is *"appended, never rewritten"* — it was
true when it was written, and `STATE.md` is the file whose job is *now*.

---

## 4 · ⚠⚠ The thing that had to NOT move, and it did not

**Packages and saves are not repo paths and never were.** `Locations.desktop()`
in `Lodestar/lib/src/locations.dart` derives the root from `XDG_DATA_HOME`, or
`$HOME/.local/share` when that is unset. **It is a pure function of the
environment and consults neither the repository nor the working directory**, so
the move could not have broken it.

**Verified rather than reasoned**, by running it from inside each repository at
the new location — the same check `BUILD/36` used, repeated:

    root     : /home/aidan/.local/share/kotor-rpg
    packages : …/packages   exists=true
    saves    : …/saves      exists=true
    sees     : [base-rules, endar-spire, taris-undercity]

**Identical from `Lodestar`, from `KOTOR-RPG-APP` and from `Loom`.** All three
packages still visible, `kaeda-vos.sav` still there. `XDG_DATA_HOME` is unset
on this machine and `env.sh` does not set it.

---

## 5 · ⚠ The four failures are the previous session's, not mine

**`KOTOR-RPG-APP` carried 12 uncommitted files when this session began** — an
in-flight fix for `PT-1443`, unpushed and unreported, and **red.**

`hub.dart` now logs `widget.packageId` (`endar-spire`) where it used to log
`packageName` (`Endar Spire`), which is right by `PACKAGE-NAMING-01`. **Four
assertions still expect the name:**

    test/ledger_test.dart          × 3
    test/save_round_trip_test.dart × 1

**The constructor argument was added to both test files — enough to compile —
and the downstream expectations were never updated.**

**⚠ NOT FIXED HERE, DELIBERATELY.** Whether the log records the id or the name
is a `PACKAGE-NAMING-01` question, and `SaveStore.listFor` already carries a
back-compat concession matching **both**, for saves written before the change.
Editing those four assertions decides that question. **That is step 4 of the
resolution rule and it is not an agent's to spend.**

**The work was preserved through the move byte-identically** — diff checksums
compared on both sides before the source was deleted — and patch copies were
taken first, because it is the only thing in the tree that is not on GitHub.

**⚠ So the owner's "everything is pushed, the risk is a re-clone" was not true
when this started.** It is closer to true now: this session's own change is
pushed, and the 10 remaining files are still only on disk.

---

## 6 · Found on the way — the suite writes to the real save folder

**19 of the app's test files call `Locations.desktop()`, the real one.**
`kaeda-vos.sav`'s timestamp moved every time the suite ran.

**Measured:** the file's SHA is **identical** before and after — the suite
rewrites it with the same bytes, which is `PT-1265`'s guarantee working. **But
it is a write into the owner's live data directory during `flutter test`**, and
a save that happened to share a name would be overwritten.

**⚠ It is the mirror of `PT-1443`'s finding.** That one was a temp-directory
test passing where the real path failed, three times. This is the other
direction: tests using the real path, and therefore mutating real data.
**Reported, not fixed** — hermetic tests are a change to 19 files and nobody
asked for one.

---

## 7 · The move, and Steam

`/mnt/ga/SteamLibrary` **is a registered Steam library** — it is listed in
`~/.steam/steam/steamapps/libraryfolders.vdf` alongside two others. So the
owner's worry is the right one to have.

**What was observed:** `KOTOR_APP_PROJECT` has no `appmanifest`, so no game
owns it, and a *Verify integrity of game files* run targets one installed
game's own folder. **Nothing seen this session suggests it bites harder than
the owner said.** Both filesystems are `ext4`, so permissions, symlinks and git
survived intact — `git fsck` clean in all six.

**The real exposure is the 10 uncommitted files**, not the repositories.

**⚠ And one incidental gain:** `/` was at **92%** full. The tree was 1.4 GB and
is now on a volume with 280 GB free.

---

## 8 · What was done to the tree

- **`build/` deleted in all four Flutter packages before copying** — gitignored,
  zero tracked files, and their CMake caches hold absolute paths that would have
  been wrong anyway. 1.4 GB → 964 MB copied.
- **`rsync -aHAX`**, 9,236 files including 3 symlinks, then a dry-run diff, a
  file count, `git fsck` and a head/dirt comparison on all six **before** the
  source was removed.
- **Both programs cold-built at the new location** — app 21.9s, Loom 31.2s.
  ⚠ **That is the first cold build since the `clang` shim was folded into
  `env.sh`, and it is what proves the shim works**: every `build/` was gone, so
  CMake had nothing cached to hide behind.
- **`README.md` and `docs/RUNNING-ON-THIS-MACHINE.md`** updated with the new
  path — and **the `clang` shim written into both**. It had been recorded
  nowhere but a comment inside `env.sh`, in an unversioned tree root.
