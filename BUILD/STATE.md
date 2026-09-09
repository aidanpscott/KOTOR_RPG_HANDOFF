# STATE — every repository and package, as of the last push

**⚠ Rewritten in full each time, never appended.** If a line here disagrees
with a slice report, this file is the later one.

> **⚠ THIS FILE WENT ELEVEN SLICES STALE.** It was last rewritten at `BUILD 25`
> and slices **26–36 landed without it being touched** — every repository head
> in it was wrong, it still said *"70 app tests"* against 206, it carried a row
> struck through as answered **and the same row live below it**, and it knew
> nothing of dialogue, doctrines or the first playtest. **The one file whose
> whole contract is *what is true right now* was the stalest thing in the
> tree.** Rewritten at `BUILD 37` from the slice reports and from the code.

---

## ⚠ Where everything is — this changed at `BUILD 37`

    /mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT   the real path
    /home/aidan/kotor-repos                                   the same folder (a SYMLINK)

**It moved from `/home/aidan/step1` into a Steam library**, because the owner
wants the code where the games are. **Use `~/kotor-repos` in anything you
write** — it is the stable name and it is why the move cost one symlink.

**⚠ Steam can delete things under `common/` on a verify.** ✓ **Everything is
now on GitHub** — the app's last uncommitted work went in at `BUILD 38` — so
the exposure is a re-clone and nothing else.

**⚠ Packages and saves did NOT move and are not repo paths.**
`~/.local/share/kotor-rpg/`, derived from `XDG_DATA_HOME`/`$HOME` by
`Locations.desktop()`. Verified from all three repos after the move.

**⚠ `env.sh` is not optional and neither is its `clang` shim.** Flutter, CMake,
Ninja and Clang live under `~/spike`; clang is installed as `clang-19` with no
plain `clang`. Without the shim a **cold** build dies with *"CMAKE_CXX_COMPILER
not set"* — earlier builds only worked because CMake had cached the compiler.

## Repository heads

| Repo | Head | Visible to the owner? |
|---|---|---|
| `KOTOR_RPG_MAIN_WORK` | `8884ac8` — `PT-1443`, the first real playtest | ✓ |
| `KOTOR_RPG_HANDOFF` | this commit | ✓ |
| `Lodestar` | `f7fe50d` — `DOCTRINE-FORMAT-01`'s reader | ⚠ no |
| `Lens` | `04e4061` — the board re-fits when its space changes | ⚠ no |
| `Loom` | `b2308e1` — authoring tests write to a copy of the bed | ⚠ no |
| `KOTOR-RPG-APP` | `3d97d52` — `PT-1445`, a log records the id | ⚠ no |

**All six clean and level with origin.** ⚠ The app's 10 uncommitted files were
committed at `BUILD 38` once `PT-1445` decided what was blocking them.

## Tests, as measured

**`Lodestar` 270 · `Lens` 4 · `Loom` 111 · `KOTOR-RPG-APP` 206 — 591, all
green.** ⚠ **All four suites are hermetic**: a full run of every one leaves
`~/.local/share/kotor-rpg/` untouched, verified by mtime snapshot. `BUILD 38`
did the app, `BUILD 39` did Loom.

⚠ **But USING either program is not a test** — it writes real saves to the real
folder, because that is the product working.

## What each repository is

**`Lodestar`** — the rules engine. Pure Dart, no Flutter. Packages, areas,
characters, the ledger and replay, combat, `PLAY-STATE-01`, the dialogue reader
and validator, the doctrine reader; `Locations` answers where things live.

**`Lens`** — the shared view layer, `PT-1381`. The area board, its palette, its
metrics and the pan/zoom viewport. Exists because `AREA-FORMAT-01 §2b` governs
how an area looks in **both** Loom and the app.

**`Loom`** — the Builder. Packages and properties, areas, tile painting,
placing, connections and arrivals, creatures with equipment, **the conversation
editor** and **the doctrine editor**, and `validate` on open.

**`KOTOR-RPG-APP`** — the play client. Console Home, the Package Main Menu, all
nine chargen steps, save/load/continue, the walk, **the dialogue screen**, and
a fight an author started.

## The shelf — `~/.local/share/kotor-rpg/packages/`

| Package | What it is |
|---|---|
| `base-rules` | ⚠ **Generated, not authored.** 22 TOML files. `PACKAGE-FORMAT-01 §3c`. Rebuild with `scripts/gen_base_rules.py` in MAIN_WORK. **301 worlds.** |
| `endar-spire` | The two-area test bed, made entirely in Loom |
| `taris-undercity` | A second package, so the library holds more than one tile |

## What runs end to end

Console Home → a package → the Main Menu → New Game → the pre-hub → the hub's
nine steps → Play → the area and the walk → walk into the trooper and a
**conversation** opens → an option starts a **fight** → initiative, turns, a
doctrine the author wrote → quit, reopen, **Continue**, the same character.

---

## ⚠ What is open

### ⚠ The live wall is clear

| | Need |
|---|---|
| **Nothing is open here** | ✓ `PT-1443`'s save work and the suite's writes into live data both closed at `BUILD 38`. What remains of `PT-1443` is design — the next section |
| ⚠ **A temp-directory test passed where the real path failed — three times** | `PT-1382`, `PT-1425`, `PT-1417`. **The pattern, not the instances, is the finding** — and it is why `BUILD 38` kept every real-shelf READ rather than sandboxing the suite wholesale |

### Asked for at the playtest, and not built

| | Need |
|---|---|
| ⚠ **The side panel** | Confirmed wanted **at the machine**. The panel runs full-width along the bottom, so ~70% of the width is black; down one side gives a **66px tile against 29px**. Measured at `BUILD 32`, decided at `PT-1443` |
| ⚠ **Click-to-move, and there is no settings surface** | NWN/BG3 style, keys as an alternative. **Needs key bindings and an options screen that do not exist**, and `PT-1425` made walking-into-something the attack affordance *on the arrow keys* — that gesture needs re-answering |
| ⚠ **Baldur's Gate 3 as a fourth source** | Movement limits, where you can go in combat, rounds, dice-roll visuals. **The first modern one** — every study so far has read a 2002–2005 engine |
| **Nothing has been designed** | `UI-STYLE-VALUES-01 §7`'s sizes are re-derived against a real viewport (`BUILD 32`); **typography, palette and framing have never been touched.** Not a defect |

### Blocked on a format that does not exist

| | Need |
|---|---|
| ⚠⚠ **A reaction has no home and no format** | `ATTACHMENT-01 §3` specifies `on: <kind> then: <response>` and **nothing says where one is declared.** `BUILD 34`'s stop. The doctrine half was answered at `BUILD 35`; **reaction was not** |
| ⚠ **The door template** | `[[connections]] from` names a file in `blueprints/doors/` — **a folder in the layout with no format behind it.** Same stop one level down |
| ⚠ **Path or handle is undecided** | `AUTHORED-CHARACTER-01` writes a path, `ATTACHMENT-01 §2` writes a bare handle. `DOCTRINE-FORMAT-01` settled it for doctrines; **the general ruling is still owed** |
| ⚠ **`format = 1` is read by nobody** | `§4` shows it, `PT-1366` ruled it, and `package_open` does not read it. **A ruled field neither side implements** |
| ⚠ **Equipment is authorable but not read in play** | The bed's trooper carries a blaster rifle, made by clicking. `strike()` still uses a hardcoded fist. **`PT-1425`'s fist is now a code gap, not a data gap** |

### Save and load

| | Need |
|---|---|
| ⚠⚠ **What a save is NAMED, and how many** | `§5a` settles *where*. The header carries **no time, no name, no character and no package** — so `Continue` cannot order saves, and nothing can tell which package a save belongs to without a full read. **`SaveStore.listFor` reads every log to answer it; the right fix is a fifth header field, and that is the format's call** |
| ⚠ **"The same place" is the entry area** | `character.moved` and `area.entered` are **`session`** lifetime. **By the vocabulary's own rules a save cannot know where you were standing** |
| ⚠ **Loading is step 3 of five** | `§5`'s sequence is resolve · snapshots · replay · validate · open. **Only replay is built** |
| ⚠ **Save slots and rewind** | `§5·0` specifies a slot as a point in the log with a rewind event. **Specified, not built** |
| ⚠ **Three of `§4`'s twelve rules cannot be checked** | derived-aptitude skill caps, granted feats against a class schedule, feat prerequisites. **Returned, not skipped** |
| ⚠ **The compressor is `gzip`, not `zstd`** | `PT-1328` measured the gap at 0.09 MB on 16.3 MB. Dart ships no zstd. **The header records which**, so switching orphans nothing |

### Data that is missing or contradictory

| | Need |
|---|---|
| ⚠ **`ATLAS/decisions/`** | **34 files `MAIN_WORK` has never read.** `D-MENU4` sat there superseding a ruling three documents still carried |
| ⚠ **Skill Focus** | `SKILLS-01 §12` says 23 exist, one per skill; the library holds **one generic record with no skill on it**. Still unbuildable |
| ⚠ **`attack_chains` / `attack_picks_at_30`** | Populated for **14** classes. **`picks` is derivable from `rate`; `chains` is not** — `§2.3` makes it a per-class assignment |
| ⚠ **Three Sith base classes at LEVEL-UP** | Level-30 totals are authored; **when they gain the other eleven is unwritten** |
| ⚠ **Science and Survival for droids** | On the 25-skill roster and **nowhere in the chapter**. Withheld, and said on screen |
| ⚠ **`PT-621`'s Protocol carve-out** | Opens `Persuade` to a chassis that is not one of `§2.3`'s four bodies |
| ⚠ **Route 2, the purse** | Needs the array's own credit value, which is **not written**. Only 18 of 41 names resolve to one row |
| ⚠ **Three grants name no item** | `Augmented`, `Dancer`, `Initiate` depend on the character. 13 of 16 slot-fillers resolve |
| ⚠ **Reported, not resolved** | The Jedi Guardian attack row transposed · `PT-126` (`Specialist`) vs `classes.json` (`Middle`) · `FEAT-SCHEDULE-01`'s "Seven schedules" row · `DEATH-AND-DIFFICULTY-01` Hard −10 vs `§5b` · `CHARACTER-RECORD-01 §2` vs `§5` on abilities · five stale `ITEMS` headers · `STARTING-EQUIPMENT-01` saying 18 where `§4` carries 19 |

### Assets — nothing is ours

| | Need |
|---|---|
| ⚠ **There is no portrait set** | `UI-ASSETS-01 §2` asks for presets per species — *"the largest art commitment in the flow"*. The screen shows a filled circle. **The first place a player can see we ship no source assets** |
| ⚠ **An import cannot fill it** | K1's 181 `po_*` portraits are named for **the games' own characters**, not for a species |
| ⚠ **The custom-portrait spec is unwritten** | `PT-1180` wants a player-side folder. **The half of this that needs no drawing** |
| ⚠ **The icon pairing must count ICONS, not items** | 183 `ii_*` across 38 classes against 557 `.uti`. Counted against items it can never balance |
| ⚠ **K2's item icons not located** | ⚠ **Checked:** K2's `chitin.key` and this build's `TexturePacks/`. **Not checked:** module `.rim`/`.erf`, `override/` |

### Rulings that are Claude's, flagged not made

| | Need |
|---|---|
| ⚠ **`down → dead` in one blow** | Writes only `character.died`. **The last of the six had-to-behave-somehows.** The other five are ruled — `PT-1420` took two, `PT-1422` two, the brief one |
| ⚠ **The re-lock discard list** | `character.step-reopened` carries its own, so an old log replays the same way after the flow changes |
| ⚠ **Walk into it to attack** | A step onto an occupied square strikes instead of moving. **No document rules it** |
| ⚠ **Powers at 1st level** | `MULTICLASS-01 §2.2a` states 2; `POWER-COSTS-01 §6` calls acquisition open. **Read as compatible, and that reading is Claude's** |
| ⚠ **The dialogue panel holds up to seven options** | `STUDY 18` found source nodes offering that many; **nothing rules the number** |
| ⚠ **14 emitted kinds are not in `EVENT-KINDS-01`** | Now **asserted** rather than reported: check A names them as an exception list and a fifteenth fails the build. **Writing them into the document is the owner's** |
| ⚠ **A droid model has no `id`** | `DROID-MODELS-01` is keyed by chassis; `character.model-set` records the **name** because there is nothing else |
| ⚠ **A fight can always be left, and never lost by leaving** | Fleeing is not built. **This is what transience gives you** |
| ⚠ **`recommend_order`** | Unauthored. Scoped negative across all staged files |

---

## ⚠ Closed since `BUILD 25` — so nobody re-opens them

| | |
|---|---|
| **`PLAY-STATE-01`, the second projection** | ✓ `BUILD 26`. A **second fold over the same log**, beside `replay()`. No new store, no snapshot, **no new event kind** — the outcome rides on `encounter.ended`, already declared and already `campaign` |
| **The wound survives leaving the area** | ✓ `BUILD 26`, and it closed **as a consequence** rather than as a feature. `Fight.abandon()` now writes the outcome first. **This was a ⚠⚠ open row for four slices** |
| **The dialogue reader and validator** | ✓ `BUILD 27`. Refuses what is not a conversation; reports one that loads and is still wrong; **says what it could NOT check**, so "clean" never means "nothing was looked at" |
| **`SHOW ALL` vs `PICK ONE`** | ✓ `PT-1432`/`PT-1434`. `replies` shows all, `then` picks one, **never both** — and the ruling took the conversion from 54.9% to **99.5%** expressible across both games |
| **The empty `say`** | ✓ `PT-1433` refuses it. **59% of K1's player nodes are blank** because K2's `Logic` joined exactly two conditions; `all_of`/`any_of` nest, so the node has nothing left to do |
| **The dialogue screen** | ✓ `BUILD 30`, `§4c`'s colours drawn. **No numbers on a check**; a shut option is not drawn at all; the bracket is derived, so nothing an author typed can disagree with what rolls |
| **The option list cannot be clipped** | ✓ `BUILD 32`. **There is no cap** — a clipped row is still hit-testable, so a tap landed on the wrong option silently. Asserted at seven option counts across three viewports |
| **A conversation may end in a fight** | ✓ `BUILD 31`, `PT-1437`. `Beat.startsFight` is **derived from the events**; the effect IS the fact |
| **Loom's conversation editor** | ✓ `BUILD 31`/`33`. The creature dialog had been **silently erasing** a hand-added `conversation` line — *anything the Builder cannot write, the Builder eventually destroys* |
| **The audit of the bed** | ✓ `BUILD 33`. Every file traced to the Loom action that made it; **only the conversation had been hand-written**, and it is authorable now |
| **`[requires]`, `[continues]`, `cover`, equipment** | ✓ `BUILD 34`. Four of the five unwritable fields, plus a sixth found by looking again |
| **The doctrine format** | ✓ `BUILD 35`, `DOCTRINE-FORMAT-01`. **`never` is not a preference that lost** — and that survives *by construction*: two sections, an unknown key is a load failure, and the dialog has two verbs |
| **The `plainAggression` fixture** | ✓ `BUILD 35`. The bed's trooper carries an **authored** doctrine, made by clicking. A scaffold since `PT-1423` |
| **Every dialog scrolls, and `New Creature`'s 58px overflow** | ✓ `BUILD 34`, one fix. ⚠ **And the rule it produced:** anything you can click must be laid out where it can be seen — **three times this session** a scroll turned *content you cannot see* into *content you can click by accident* |
| **The `Lens` board re-fits** | ✓ `BUILD 32`. `_tile` was cached so a player's zoom survives a rebuild, and it therefore never re-fitted when the **view** changed. **A deliberate zoom is still the player's** |
| **On the machine, runnable** | ✓ `BUILD 36`. `run-app.sh`, `run-loom.sh`, `env.sh` |
| **`PT-1445` — a log records the id, never the name** | ✓ `BUILD 38`, and **the four failing tests were RIGHT.** `hub.dart` had two paths to one record and only the log half had moved to the id; `recordFromChoices` still carried the name. **One line, zero test edits.** `replay()` cannot map an id back to a name, so the record had to move and the log could not |
| **`SaveStore.listFor`'s both-ways read** | ✓ recorded as a **migration allowance** — reads both, writes one. **When it can go is checkable:** when no save remains whose `package` is not an id in the library |
| **Loom's tests writing into the test bed** | ✓ `BUILD 39`, and **`BUILD 38` had only fixed the app.** Loom rewrote `endar-spire` — **the fixture every other suite loads** — on every run. Its sandbox **copies** where the app's **symlinks**: a reader wants a link, a writer wants a copy |
| **`HANDOFF/TEST/` and the Coder→Tester protocol** | ✓ `BUILD 39`. ⚠ `requests/` is `Coder`'s and `reports/` is `Tester`'s, because `PT-1446` gives both the same directory. **A request is a journey, not a suite** |
| **The suite writing into live data** | ✓ `BUILD 38`. ⚠ **The split is READ versus WRITE, not real versus temp** — every real-shelf read was kept, because that coupling is what caught `PT-1382`, `PT-1425` and `PT-1417`. Only the 6 writers were sandboxed. **Controlled**: breaking the sandbox's shelf link makes those tests fail |
| **The tree moved to the Steam library** | ✓ `BUILD 37`. Baseline before, identical after. **No path dependency existed** — `Lens` and `Lodestar` are git dependencies through `~/.pub-cache` |
