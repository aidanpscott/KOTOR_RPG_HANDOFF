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
| `KOTOR_RPG_MAIN_WORK` | `c4ee0ec` — `PT-1539`, 38 of 38; the defence track's structure | ✓ |
| `KOTOR_RPG_HANDOFF` | this commit | ✓ |
| `Lodestar` | `e00ca7f` — `PT-1541`/`PT-1544`, two curves and a named track | ⚠ no |
| `Lens` | `9ca5982` — `PT-1502`, travel re-fits the board | ⚠ no |
| `Loom` | `e0bf5ee` — level with `Lodestar` | ⚠ no |
| `KOTOR-RPG-APP` | `6b0e096` — `PT-1543`, components and total on one row | ⚠ no |

**All six clean and level with origin.** ⚠ The app's 10 uncommitted files were
committed at `BUILD 38` once `PT-1445` decided what was blocking them.

## Tests, as measured

**`Lodestar` 389 · `Lens` 5 · `Loom` 131 · `KOTOR-RPG-APP` 321 — 846, all
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

### ⚠⚠ THE NOBLE'S DEFENCE INTERIOR — AN RCR READ I CANNOT REACH

`PT-1541` reports the RCR PDF on the owner's machine, verified from the title
page. **It is not on any path this build can read** — searched by filename and
by title across the home and library trees; `data/books/` holds three files and
not that one.

**The structure is built so reading it is a DATA change, not a code change:** a
named track, the Consular as an **offset** from the Noble, the Soldier as a
**computed rule**, and `bonusAt` returning **null** rather than interpolating.

### ⚠⚠ A RULE APPLIED AT ONE OF TWO MOMENTS — `PT-1538`

`_here` was filtered for the dead **in `_enter` alone**, so a creature killed
during a visit stayed on the board until you walked out and back — and could be
fought again, and buried again. **The rule was right and it ran at one of the
two moments a creature can die.** Arrival was the one I had a reason to think
about.

⚠ **And a fixture depended on the defect:** `fightAndRead` kept pressing after
the fight and the corpse absorbed those presses as fresh fights, so a roll line
was always on screen. A test that passed because a defect kept the screen busy.

### ⚠⚠ THREE CLASSES, THREE UNRELATED TYPOGRAPHIC REASONS — `PT-1535`

`Marksman` and `Engineer` were **never missing**: a filename that says *droid*
over two *classes*, a table of **two classes side by side** with a
`\multicolumn` artifact and a blank line inside it, and headers that are
**initials** (`CD`/`ED`) so the class name matches nothing. **35 → 37 of 38.**
The `Saboteur`'s heading carries a **warning glyph**, which defeats a
`^# ([A-Za-z ]+)$` reader — the same shape, a third file.

### ⚠⚠ A DERIVATION IS FURTHER ALONG THAN THE PLAY SCREEN SUGGESTS — three times

`PT-1424` found **speed** derived from species rather than stored. `PT-1531`
found the **base attack bonus** in four rules files the extractor was dropping.
`PT-1533` found the **species ability modifier** parsed, tested and applied —
**in chargen, and nowhere else.**

> **The pattern: a complete path on one side and a constant on the other.** The
> thing to check first is not *"is this written?"* but ***"who calls it?"***

⚠ **And the same shape one field over:** the reaction pip was grey from the
first frame of every fight because `_playerCombatant` hardcoded
`reactionsLeft: 0` — while `PT-1517`'s *"a grey pip is a promise"* had been
applied to the bonus pip beside it.

### ⚠⚠ THE CLASS DEFENCE BONUS IS A READ OF RCR CHAPTER 3 — `PT-1531`

**Not an extraction gap.** `classes.json` **already carries a `defence` key**
for the three Jedi classes and **every value in it is an em dash** — the column
was extracted and there was nothing in it. `CLASS-TABLES-JEDI §5A` says where it
lives: *"the Jedi progressions are in RCR Chapter 3 and have not been read."*

**One data point is attested in the whole corpus: the Noble, +2 at 1st to +10 at
20th.** Nineteen base classes plus prestige across thirty levels. **The
expression is ruled and one of its terms has nowhere to read from.**

### ✅ BASE ATTACK BONUS WAS AN EXTRACTION GAP — FIXED, 25 → 35 of 38

The extractor's merge was **first-wins**, and the PHB tables (`attack_picks`)
claimed `progression` before the source tables (`BAB`) could contribute.
`CLASS-TABLES-BASE`'s own progressions were read by **nothing**. ⚠ **Three still
have no table anywhere**: `engineer`, `marksman`, `saboteur`.

### ~~⚠⚠ TWO DERIVED VALUES HAVE NO ARITHMETIC~~ — `PT-1528`, superseded above

**`defence`** — `CHARACTER-RECORD-01 §3` names the inputs and **no document
states the sum**; no class carries a defence column. The only defence sum in
the corpus is **KOTOR's own**, quoted in three documents to argue a derivation
should be SHOWN. `defence: 10` stays with the gap named beside it.

**`base attack bonus`** — `§12.5` names it and `rate` is *"how fast you acquire
ATTACK PICKS"*, a count of chains. Taken as **nullable and omitted**, because a
zero claims the term was computed.

⚠ **Removing the invented `Term('attack', 2)` changed the game:** a Sith
Trooper is all tens, so **+0 against defence 10**, and a `Str/Dex 14` soldier
now wins the fight it used to lose. **Every creature is markedly worse at
hitting until that term has a source.**

### ✅ THE FLAKE WAS A PATTERN AND IT IS CLOSED

**Four occurrences, two slices, one cause:** a **fixed millisecond budget around
a real disk read** — ample alone, not ample in a full run with four isolates.
`Loom` already had the rule and the app had never adopted it: *wait for it
rather than sleeping at it.*

⚠ **The brittle wait and the reported symptom were in different places.**
`play_walk_test` reported a failure at the round trip and the short wait was the
**first assertion**. Three consecutive clean full runs, then two more.

### ⚠⚠ A SAVE KNOWS WHERE YOU STOOD — `PT-1523`, BUILT, and it had THREE ends missing

`character.moved` was declared `campaign` **with the reason in its own
comment**, folded into a `Position` — **and `.position` had zero uses in the
whole app** while `_open` set `_entry` to the package entry unconditionally.
**Declared, folded, unread AND unwritten.** Writing it alone would have fixed
nothing visible.

⚠ **Two moments, not every keypress:** `onAppend` rewrites the whole file, so a
`moved` per arrow key is a **file write** per arrow key. The volume question is
settled; the **write-frequency** one was not.

### ⚠⚠ NOTHING DIED — `PT-1515`, BUILT, and it had THREE causes

    1  Role had four members and EVERY ONE was a party role, so
       combatantFrom's Role.player default made every placement party.
    2  ⚠ THE REVIVE ASKED A RAW NUMBER — `current <= 0` — and stood
       everything up at 1. Tester's sentinel at −2 was DYING, never dead:
       making death work would not have fixed this on its own.
    3  character.died had no CONSTANT, so nothing could switch on it and
       no projection folded it. A death could not have survived a quit.

⚠ **A recorded death outranks the arithmetic** — a death floors the pool at 0
and `stateOf` calls 0 `down`, so re-deriving state from the pool would have
handed the creature back at 1. **The event is the fact.**

⚠⚠ **A DEAD CREATURE LEAVES NOTHING**, and that is a consequence: no corpse in
the five tile types, `[[contents]]` is authored, and `§4` bars the engine from
writing a package. It is removed from `_here` **once** rather than skipped in
four places — the difference between *gone* and *ignored by whichever list
someone remembered*. **`PT-1511`'s vacated square is now walkable.**

### ⚠⚠ WHAT AN EFFECT CARRIES IS MOSTLY UNWRITTEN — `PT-1516`

`EVENT-KINDS-01` declares ~40 kinds and `PLAY-STATE-01 §6` leaves every payload
**deliberately unspecified**. **Three have a shape something reads:**

    quest.flag-set    flag                    flagsFrom
    quest.concluded   quest, conclusion       questsFrom
    encounter.began   (none)                  PT-1437

⚠ **`item.lost` is the sharp one:** `§9`'s own worked example writes it with
`item` and `count` and **nothing reads it** — an author following the format's
own example writes an effect that does nothing. **Named in `EVENT-KINDS-01 §3b`,
not filled**: a payload column belongs written *when a consumer exists*.

### ⚠ A COST WRITTEN AND NEVER SPENT — `PT-1513`, BUILT

`difficult` costs **two**, and the multiplier is on the **creature**:
`moveCostMultipliers` plus **one** `ignoresMoveCostMultipliers` flag that clears
every source. The tile names what kind of hard it is and sets no number, so a
hover droid, a Force power or a boot each state their exemption **once**.

⚠ **Stacking cannot arise** — `PT-1366`: a text-map cell is one character and
therefore one type, so a square names at most one costed source.

⚠⚠ **AND THE PRICE EXPOSED AN ORDER BUG INVISIBLE AT PARITY:** the spend ran
**before** the impassable check, so **walking into a wall cost a point of
movement and then refused.** Unseeable while every square cost one.

### ⚠⚠ A SKILL GATE ON A `replies` LINK ROLLS ON COMMIT — `PT-1501`, BUILT

**How a flag and a skill are told apart was already in the runtime.**
`_gateVerdict` returns a third verdict, `Verdict.isACheck`, instead of
pass/fail — **that exists so a check is OFFERED rather than filtered**, and
`Option.check` is the term it kept for the amber bracket. `PT-1432` is not at
risk from the fix; a test asserts the flag-gated reply is hidden while the
skill-gated one is offered, in the same fixture as the roll.

    a gate on a `replies` link, flag       HIDES
    a gate on a `replies` link, skill      SHOWS, and ROLLS ON COMMIT
    a gate on a `then` link                ROUTES the committed outcome

⚠ **ONE ROLL, NOT TWO.** `§9` gates the outbound link as well — that is how an
author says which node is the pass, not a second check — so the committed
outcome is carried into `_pick` and routes there. **Order is meaning.**

⚠ **Nothing rolls while the list is merely shown**, or opening a conversation
spends the check. Asserted.

**Measured against the shipped bed, 4000 commits per rank: 35.9% at rank 0
(expected 35.0%) and 56.2% at rank 4 (expected 55.0%).**

### ✅ THE SAVE HEADER — **BUILT**, and it is `format = 2`

`SaveEntry` gains `savedAt`, `package`, `character`, `className`, `level`,
`area`. **Every one has a named consumer**; `package` alone removes a
decompress-and-replay **per save** from drawing the package menu.

⚠⚠ **THE BUMP IS MECHANICAL, NOT CEREMONIAL.** The header is positional and its
length is derived from the fields a reader knows, so a `format = 1` build
reading a `format = 2` save computes the payload offset short and reports
**"Damaged save"** — a wrong reason for a good file, which is `PT-1366`'s
motivating case exactly. `formatFromTheFuture` already exists and **only fires
if the number moves.**

⚠ **And moving it is what keeps old saves readable.** A `1` still parses and
still yields its log; absent means *older than the field*, never a time
invented from the filesystem.

⚠ `Load Game` and `Continue` **sort by the same comparator** now, so the first
row is the one the button takes. A save with no recorded time sorts **last** —
*unknown* is not *oldest*.

### ~~⚠⚠ A SAVE HEADER CARRIES NOTHING ABOUT THE GAME~~ — closed above

`SaveEntry` is `handle`, `formatVersion`, `compressor`, `rulesVersion`. **No
name, no character, no level, no place, no time.** Both of `TEST 018`'s
observations fall out of that single fact:

- **`Load Game` lists the older save first and `Continue` takes the newer.**
  The screen that offers a choice and the button that makes one **disagree
  about which is first.**
- **The only distinguishing field on a save row is the id.**

⚠⚠ **AND THE SHARP EDGE: `Continue` ALREADY DOES THE THING THE ENGINE SAYS
CANNOT BE DONE HONESTLY.** `SaveListing` refuses to supply a "most recent" —
*"ordering by file mtime would be the caller's filesystem guessing at a fact
the format does not record"* — and `SaveStore.mostRecentHandle` orders by file
mtime. **One surface refuses the guess and the other is built on it**, which is
exactly why they disagree.

⚠ **Not built, and deliberately.** Making the two agree is one line; making
them agree *honestly* is a **format** change — `SAVE-LOAD-01` giving the header
a time and an identity — and that is a ruling, not a UI decision. **The owner
called these observations rather than defects; this is the root under both, for
whenever they are ruled.**

### ⚠⚠ A HELPFUL CLAUSE ASSERTED RATHER THAN CHECKED — THREE INSTANCES

`TEST 016 F3`, `TEST 017 F3`, and `016`'s was **still live when `017` found the
second**. A sentence added to make a fault kinder, asserting the thing it did
not test:

    "which this package does not list"       — it was listed, and unreadable
    "it has never been placed"               — the fault above it was its placement

⚠ **Each was added to help an author, and each is the part of the message that
is false.** Both are checked now. **Worth looking for a fourth** the way
`PT-1494`'s shape was — the family is *a clause that reads like evidence and is
not*.

### ⚠⚠ `tester-probe/sentinel-challenge` IS REFUSED, AND THE FIX IS CONTENT

`PT-1501`: `stand-down-i` is offered as a `Persuade` DC 14 check and its `then`
carries no check, so it never rolls. `§9`'s form needs a **failure node** —
where a failed Persuade against the sentinel lands — and that is the owner's
choice. **`tester-probe` is Tester's package.** Until it has one, `validate`
refuses that conversation and Loom will not write it.

`endar-spire` was fixed: `§9` is a worked example of **that file by name** and
authors its failure node, so the content was not invented.

### ⚠⚠ `§9`'s OWN FAILURE NODE RE-OFFERS THE CHECK

`not-on-my-board` carries `replies = ["back-off", "push"]`, so a failed Persuade
returns the player to the same check **with nothing spent** — passed eventually,
always. `PT-1501`'s defect by a longer road. **The bed's failure node is
terminal instead, and that divergence is reported, not decided:** whether a
failed check may be retried is a rule and it is the owner's.

### ⚠⚠ A DECLARED EVENT KIND NOTHING EMITTED — `PT-1501`

`check.resolved | transient` has been in `EVENT-KINDS-01` since `PT-1418` and
**no code wrote it.** `PT-1418` found fourteen emitted kinds undeclared; this is
the mirror, and it is why a free check could only be found by counting twelve
outcomes. **A check that rolls and records nothing is indistinguishable from a
check that does not roll.** Emitted now from all three `_pick` sites and said on
screen, verdict first.

### ⚠⚠ A GATE ON A `replies` LINK COLOURS; A GATE ON A `then` LINK ROLLS

`PT-1432`'s distinction, and the runtime tells them apart **by position** —
`Verdict.isACheck` and `_pick`. The same gate is written **twice** in `§9`, on
the reply and on the outbound link, and that is not duplication: one is the
amber bracket, the other is the dice. **Any fix that merges them flattens
`PT-1432`.**

⚠ **And the ORDER of the outbound links is meaning.** `_pick` returns on the
first **ungated** link, so the gated one must come first.

### ⚠⚠ A RULE THAT FIRES ON NOTHING REAL IS A RULE NOBODY HAS TESTED

`PT-1459` checked only whether a gated reply had a `then` **at all** — a shape
no author produces. It was green for four slices while **every shipped
conversation in the project** carried the fault it was written to catch.

### ⚠ THE BUILDER COULD NOT REPAIR WHAT IT WROTE

`ConversationDraft.link` only ever appended; there was no `unlink`. `PT-1379`
stopped Loom **creating** a detectable fault and left it unable to **correct**
one. Added at `PT-1501` — but **the editor has no button for it**, so a
conversation authored by clicking still cannot be corrected by clicking.

### ⚠⚠ A `find.textContaining` TEST PASSES ON ELLIPSED TEXT

`PT-1501`: the widget's `data` is whole and the **render** truncates, so a
presence test cannot see a line a player cannot read. The panel is one `Text`
with `maxLines: 2`; **one 203-character sentence fits and two do not**,
measured.

⚠ **The rule that came out of it: WHEN A LIST CAN BE ELLIPSED, LEAD WITH THE
COUNT.** Truncation can then hide *which*, never *that*. Anywhere else joining
a list into one capped `Text` has the same exposure.

### ✅ `PT-1500` — THE PALETTE. **BUILT.**

Three kinds have a home and **none of the three was invented**: `creatures` →
`blueprints/characters`, `doctrines` → `blueprints/doctrines`, `items` →
`blueprints/items`. Each is a constant `Lodestar` already declares, a `Loom`
writer already writes, and a folder the shipped bed already has.

⚠ **THE OTHER SEVEN GET NOTHING AND THAT IS THE ANSWER.** `doors`,
`encounters`, `placeables`, `sounds`, `stores`, `triggers`, `waypoints` have
**no format, no reader, no writer, no folder constant.** They report *cannot
list*, in the Builder's own terms. Inventing homes to make the pane look
complete would be the same move as the hardcoded `const []`, one step along.


### ⚠⚠ `PT-1367`'s PREFABS ARE UNBUILT AND WERE UNTRACKED — `TEST 017`

**A prefab is a saved selection** — *"paint a room, drop art on it, select it,
save it — it is now in the palette and anyone can drag it into any map."* It is
`PT-1367`'s third size, and it carries the stated accessibility goal: **premade
rooms for people who do not want to paint one, made by people who did.**

⚠ **None of it exists, anywhere.** `Tester` grepped all four repos: **one
occurrence of the word**, and it is a note saying there are none —

    Loom/lib/area/new_area.dart:18
    /// ⚠ NOTHING BELOW THIS. No grid, no tile map, no prefabs — 4b and 4c.

No `Prefab` type in `Lodestar`, no prefab widget, dialog or writer in `Loom`, no
test, **and no selection tool, copy, paste or saved-selection surface of any
kind**. It is also what `PT-1371`'s single-area decision leaned on: prefabs are
the named reason two areas side by side are not needed.

⚠⚠ **IT IS HERE BECAUSE IT WAS NOWHERE.** A ruled feature that is neither built
nor tracked is the one that gets forgotten — **that is the difference from
`NewItemDialog` below, which is unbuilt AND written down.**

### ⚠⚠ LOOM CANNOT READ A RULES FILE — `PT-1493`

`NewItemDialog` is built, tested and **constructed nowhere in `lib/`**, because
it needs `baseTypes` from `base-rules/rules/equipment.toml` and **Loom has no
TOML reader at all**: it writes TOML by hand and reads through `Lodestar`'s
typed openers, none of which opens a rules file. ⚠ Its own test hardcodes three
base types, which is how it passed while being unreachable.

⚠ So `PT-1480`'s aim is **unanswered, not passed** — `Tester` could not author
the artifact it is about. `dialogs_reachable_test` names which assertion turns
red the day this changes.

### ⚠ A CREATURE'S CONVERSATION CANNOT BE CHANGED AFTER CREATION

Set in `NewCreatureDialog` and nowhere else. The dialog now says so, which
turns a dead end into an order — ⚠ **it does not rescue `probe-sentinel`.** The
fix is a creature editor, which is a new surface.

### ⚠ `endar-spire`'s PROVENANCE

`RUNNING-ON-THIS-MACHINE` says the bed is Loom's output, and the bed carries
the **correct** `characters/` form while Loom wrote the wrong one. **They
cannot both be true.** `Tester` would not regenerate the fixture and neither
would I — which one moved is worth knowing before either is overwritten.


### ✓ `PT-1491` — the gate declines rather than blessing on half (was: it could not tell friend from enemy)

`targets` and `excludes` say what KIND a power may affect. **Nothing says
whether it is aimed at a friend or an enemy**, and six powers heal — three of
them **party members**. So `PT-1488`'s gate would let you Force Push an ally
and Heal a trooper with equal confidence. ✓ **Fixed before the column exists.** A kind that agrees now returns **silent**,
naming what it could not check, and **tightens into permission or refusal the
day `PT-1489` authors `affects`** — a test builds the authored shape by hand so
that day is a change rather than a discovery.

### ✓ `PT-1490` — a character blueprint names its species (was: it did not)

`AUTHORED-CHARACTER-01` gives it a name, a class, a level, a faction,
abilities, vitality and protection **and no species and no chassis.** The Sith
Trooper's file names none, `Loom`'s writer offers none, `OpenedCharacter` has
no field for one.

✓ Both symptoms closed. A placement has a kind, so `excludes` has something to
refuse; and `combatantsIn` reads speed from the species, per line 144. ⚠ **It
happens to be 10 for a human, which is why the hardcoding survived every
slice** — and where a species states none, `speedNote` says the default was
used.

⚠ **`loom_can_write_test` caught the writer before it had the fields** — the
first time that guard has fired on a field added the same day.


### ⚠⚠ THE CAST PAYS AND DOES NOTHING — `PT-1487`, and the effect half needs AUTHORED COLUMNS

⚠ **Alongside, not first, and neither is first.** `_cast(PowerRecord p)` has
**no target parameter**, so a gate has no input and an effect has nothing to
land on. One slice whose subject is the target: choose, check eligibility,
resolve. `excludes` landing early was right because it is **data rather than
behaviour**.

⚠ **The gate must answer SILENT for 15 of the 22 powers open at 1st level** —
4 have `excludes`, 3 have `targets`. Treating silence as either permission or
refusal is wrong fifteen times.

⚠⚠ **And the effect half is not extractable.** 53 saves in **19 phrasings**,
with three genuine formulas — `DC 5 + character level`, ⚠ `DC 10 + attacker
level` (the Force Scream chain), ⚠ `DC 5 + FORCE levels` (Affliction,
Contagion, Plague) — and `Force Resistance` is an **opposed roll, not a save**.
Damage dice appear in 25 of 104 and movement in **3**. **Authored columns
first; that is a rules slice.**

The verb landed at `PT-1478` and **the effect half does not exist.** The cost
derivation is complete — pool, ceiling, true maximum, all three projected for
the first time — and then the line prints the power's prose, **which promises
an outcome**: *"1d6 per two Force levels, maximum 12d6"* reads as a promise. A
trooper hit by Force Push was 18 of 18, in the same square, unmoved.

⚠ Filed as the next question rather than a regression, which is right: nothing
claimed the effects were built.

### ⚠ `PT-1484` IS UNBLOCKED

`Tester`'s Guardian confirmation has landed and resolves the open question the
same way: **a build difference, not a class path.** The fix is ruled and
recorded in `grant_reaches_class_test.dart`.


### ⚠ QUEUED, BOTH WAITING ON `Tester`'s GUARDIAN RUN

**`PT-1484` — the item half is NOT OFFERED AT ALL** where it cannot reach this
character. `PT-695` gives a profession one grant with the player choosing the
form; where the item form cannot reach them **there is no choice to make**.
Recorded in `grant_reaches_class_test.dart`; **its last assertion turning red
is the fix working.**

**`PT-1485` — an Acolyte who is not a Force user needs an item of their own.**
⚠ The OPPOSITE operation to `PT-1484`: that one withholds an item a class
cannot use, this one adds one a class can. `Acolyte` teaches **Mysticism**, a
knowledge skill, and its grant is `Padawan Robe → Jedi Robe`; withholding would
empty the item half for most of the roster.

### ✓ `professions.teaches` — split at `PT-1486` (was: a value used as a key)

**11 of 28 values are not a skill name.** Ten are a skill with flavour fused on
— *"Athletics — they marched it into you before they trusted you with a
rifle"* — and ⚠ **all ten resolve to a real skill when trimmed.** The eleventh
is `Mysterious Stranger`'s `ANY SKILL`, which is a value.

✓ Split into `teaches` and `teaches_flavour`. ⚠⚠ **`flavour` is a THIRD KIND OF
FIELD** — rendered, and never a key — and it is the category the corpus was
missing through four slices of annotation work: every sweep had two boxes, and
the fused cells that kept resisting were the ones that were **both**.
**`flavour` is NOT exempt from `check_annotations`**, because it is shown.

### ✓ `targets` — the negative is transcribed (`PT-1486`)

*"Populate from the prose"* does not survive contact. The prose states a
**negative** (*"does not affect droids"*) and `targets` is a **positive** list;
of the 21 silent powers the cells name **no positive kind at all**. Converting
needs the closed set of kinds and ⚠ **nothing declares it** — the four in use
appear only inside individual cells.

✓ **`excludes` is built.** 25 powers carry it; a droid question is answerable
for **41 of 104 rather than 17**, with nothing inferred. Three sentences are
deliberately not transcribed — a conditional, a word outside the four kinds,
and a quotation of the source. ⚠ **63 are still silent, and that is the
document, not the extractor.**

### ⚠⚠ `§4a` — RULED AT `PT-1484`, PINNED UNTIL THE GUARDIAN RUN

`grantFor` keys on the **profession alone and never looks at the class**, so
`Tester`'s open question is settled: **Agent and Guardian are one path, not
two.** Sixteen of nineteen classes are offered `Hunter`'s upgrade.

⚠ **Two grants, not four.** `Hunter` names Soldier/Scout/Duelist and `Veteran`
names Smuggler/Bounty Hunter. `Conscript` and `Acolyte` name **no** class and
that is correct — *"the best armour the character's Armour Proficiency
allows"* applies to any of them.

**The ruling needed:** when an upgrade names classes the character is not — do
not offer the item half at all · offer it and apply nothing (today) · or apply
it to whatever the class's array carries. **Three different games.**

`grant_reaches_class_test.dart` changes nothing and pins the current behaviour,
naming in its own body which assertion turns red when the fix lands.


### ✅ THE THIRD DIRECTION IS CHECKABLE, AND IT IS CHECKED — `PT-1523`

**Three ways a kind and the code can disagree. Two were checked; the third was
not, and it is the one that shipped a player-facing defect.**

    A  ⚠ EMITTED and UNDECLARED           check A, PT-1418 — 14 of 15
    B  ⚠ DECLARED and replay IGNORES IT   check B, PT-1418
    ⚠⚠ DECLARED, FOLDED, and NOBODY WRITES  — unseen until PT-1523

**Why neither could see it:** both compare the DOCUMENT against a set of kinds
**the code declares it handles**. Neither ever asks *is there a construction
site* — and that is a plain source-level fact.

`scripts/check_event_producers.py` asks it: a `CharacterEvent(...)` whose first
argument names the kind. **95 files, 50 declared kinds.**

⚠ **ITS HONEST LIMIT IS DATA-DRIVEN EMISSION**, which `PT-1435` already named.
A package's `effect` may name any declared kind and the runtime writes it
through `CharacterEvent(e['kind'] as String)` — **a site that names no kind at
all.** Four such sites exist. So the check carries an **explicit allowance
list** with a reason per entry, rather than letting one dynamic site excuse
every kind: *a check that excuses whatever it finds checks nothing.* The
allowance is verified **both ways** — an entry for a kind that IS constructed
is reported as a stale excuse.

⚠ **Controlled:** with `character.moved`'s only producer removed it exits 1 and
names the kind; with it restored, 0.

⚠⚠ **AND IT FOUND SOMETHING WORTH KNOWING WHILE PASSING:**
**`character.faction-changed` is folded by `projectPlayState` and NO ENGINE CODE
EVER WRITES ONE.** `PlayState.faction` is only ever what a package's effect set.
`FACTIONS-01 §4b` gives a character one handle and explicitly **not** a standing
track, so there is nothing for the engine to move — **allowed, with that as the
reason, so the day something should change a faction this line is the
argument.**

### ⚠⚠ A CITATION ASSEMBLED AT RUNTIME FALLS BETWEEN THE TWO GUARDS

    check_annotations      reads base-rules/*.toml      — the DATA half
    check_player_strings   reads Dart string literals   — the LITERAL half

**Neither sees `'you fall — ' + ruleName + ' (' + ptNumber + ')'`.** The data
half has no cell to read; the literal half sees only `'you fall — '`, which is
clean.

⚠ **Nothing in the tree does this today — checked.** So it is a gap between two
guards rather than a defect, and it is written here because the person who
built both is the only one who can see where they stop. What would close it: a
rule that citations live in one named place and are never interpolated is
checkable; *"never assemble player text from a variable that could hold one"*
is not.

### ✓ `PT-1482` — the column is `kit` (was: misnamed)

**16 of 44 entries in `class_arrays.consumable` / `droid_arrays.consumable` are
durable gear**, across 9 distinct items: Sparring Gloves (`gauntlets`), Stealth
Field Generator (`belt`), Glow Rod (`light-source`), Recording Rod (`misc`),
Repair Kit (`tool`), Computer Spike / Security Tunneler / Parts (`spike`), and
a tier-1 saber upgrade with no catalogue row at all.

Renamed in both tables at `PT-1482`; the extractor's field and the app's label
follow. A test asserts the label is `kit`, `consumable` is gone, and **the
gloves are still there** — renamed, not emptied.


### ⚠⚠ `PT-1468` — the content half is done; the PRODUCER is next

`PT-1471` authored **nine** item blueprints into the bed through `ItemWriter`,
so a chargen `[equipment]` reference now has something to point at. **Eleven
distinct weapons across both arrays, not forty-one.**

⚠ **One weapon name is genuinely unresolved** — `Blaster Rifle`, two catalogue
rows, both 300cr, not among the 14 disambiguation entries. `Training
Lightsaber`'s five cells were never ambiguous: the array reads
`Training Lightsaber  blue` because the source separates the colour with `⚠`
and `_tables.clean()` strips it. **An extractor fix, not a content gap.**

⚠⚠ **A THIRD NEED, UNDERNEATH THE OTHER TWO.** The Ion Blaster is authored and
still arms nobody: `EQUIPMENT-01` gives it `1d4 + 1d10 vs droid` and
`weaponFromBase` refuses a conditional expression rather than truncating it.
**The engine has no model for damage that depends on the target** — the exact
case `TEST 007` opened with.

⚠ Two are unauthored because the rules lack a base type: `Marksman Rifle` (no
`marksman-rifle` anywhere) and `Training Lightsaber` (`lightsaber` is 2d10, the
war blade). Both need a ruling.

⚠ And `authored` is keyed by the array's spelling in `Loom/tool`, where the app
cannot read it. **When the producer lands the table must move to data** —
`item_disambiguation.toml` is the shape.

### ✓ `PT-1468` — THE PRODUCER IS BUILT (`PT-1475`)

Chargen writes `weapon_r_1 = "items/weapons/<base>"`, the same shape a
blueprint uses. **23 of 28 arrays arm a character**; 1 is the Brawler's `NONE`,
a value. Proved end to end: the producer's output goes through `equippedFrom`
and comes back **Blaster Rifle 1d12**. `item_disambiguation.toml` has its first
reader.

⚠⚠ **AND THE LOG IS THE DURABLE THING.** The first version wrote the reference
into the derived record and not into the EVENT; `ledger_test`'s replay caught
it in the same run. One `equipmentPayload()` now, called by both.

⚠ **A taken grant names which item** — `taken: "item"` named nothing. An item
taken with no grant row resolving writes `item_unresolved`.

### ⚠ `targets` IS UNDER-POPULATED BY 21 AGAINST ITS OWN PROSE

**23 powers say *"does not affect droids"* in prose and 2 carry it in the
`targets` column.** A gate built on `targets` today would block 17 and
**silently permit 21 the prose says should be blocked** — a wrong answer with a
machine's confidence. ⚠ The column is not under-read, it is under-populated,
and nothing could know because nothing read it. **The check comes before the
gate**; conditional damage then shares the *"a combatant knows its kind"* half.

### ✓ `PT-1478` — THE THREE SITH FORCE DICE ARE RULED

Warrior d4, Assassin d6, Inquisitor d8 — mirrored pairwise, and **attested
rather than assumed**: `PT-126` states the Assassin's directly. They were
stated in a **blockquote table under a different shape** from the per-class
rows, so `read_phb` returned null for all three until `PT-1478` taught it to
read the table the document actually wrote.

✓ `PT-1477` — the hyphen is gone and **27 of 28 arrays arm a character**; 1 is
the Brawler's `NONE`, a value, and 0 refuse.

### ⚠ `§4a`'s GRANT REACHES CLASSES IT DOES NOT NAME — `TEST 008` D3

The label names Soldier, Scout and Duelist; a Jedi Guardian is none of them and
is still offered the grant. A selection defect in which grant reaches which
class. **Not fixed** — the log now makes it visible in any save it happens in.

### ⚠ A CONDITIONAL-DAMAGE MODEL — costed, not built

`1d4 + 1d10 vs droid` is the **only** conditional damage in 36 base types, and
needs four structural things: a damage expression that is a LIST of conditioned
terms (`Weapon` is three scalars); a target predicate the engine can evaluate
(**`Combatant` does not know whether it is a droid**); a grammar inferred from
more than one example, with `PT-1452`'s refusal surviving it; and a damage line
that can say *"1d10 because it is a droid"*. ⚠ `PT-1474`'s `targets` column is
the same fact from the other side — whoever builds one should build both.

### ⚠ `PT-1468` — what is left

**A producer is still missing.** `EquipmentChoice` is a single `bool
takesItem` and `hub.dart` writes `items: const <String>[]`. ⚠ Scoped negative:
**all seven saves** carry `{"route":"standard","items":[],"credits":100}` and
not one has a weapon slot.

⚠ **Ruled at `PT-1471`: content first, and it is done.** A dangling reference
is no worse than the fist ON SCREEN — `PT-1452` makes every link fail out loud
— but it is worse IN THE RECORD, which is a log: the path shape would be fixed
into every save written before anything could resolve one.


### ⚠ `PT-1467` — 48 cells remain, and the count is honest rather than good

⚠⚠ **The check could not see a citation that named a DOCUMENT** until
`PT-1474`. It matched `PT-\d+`/`TRACE-\d+` and nothing else, so `ATTACKS-07`
and `FEATS-LIBRARY-01` were invisible — **33 cells across 7 files, in the
instrument built to find exactly them.**

⚠⚠ **And its splitter had damaged five shipped cells**, removing a citation
that was the object of a preposition — `cap lowered at.`, `AUTHORED at.`,
`… only by.` Wrong in `base-rules` for two slices; restored verbatim by
re-extraction. A citation is removable only when something SEPARATES it.

`species` 8 → 3, `professions`/`programmings` → 0, `powers` 44 → 7.
`items`/`feats`/`worlds` ROSE, because the broadened mark can finally see them.
**Everything left is a citation doing grammatical work** — an authoring
decision, not a formatting one. Two are named: the Droid/Assassin
design-rationale paragraph, and Wookiee `extraordinary_recuperation`.

### ⚠ `PT-1467` — `equipment.section` is the last mechanical one

`MAIN_WORK/scripts/check_annotations.py` reports them. **It is red on four
files and three of those are deliberate.**

| what | cells | why it is still open |
|---|---|---|
| `equipment.section` | 6 | ⚠ slice 2, ordered. A value used as a KEY — `Wield classes - PT-169`. Anything filtering on it matches nothing, as `records.dart:879` already does for `feats.section`. A latent defect, not cosmetics. |
| ~~`powers.effect` + `prerequisites`~~ | ~~43~~ → 7 | ✓ `PT-1474` — 17 powers have a `targets` column; 87 are null, which is the document being silent. |
| ⚠ an authoring decision | 2 | The citation is the sentence's SUBJECT — `and PT-559 removed the second pool`. Removing the token leaves `and removed the second pool`, so the splitter refuses and reports. `species.extraordinary_recuperation` and `feats.effect`'s Sneak Attack. |

⚠ **The extractors disagree about their own first argument, and it is not six
— it is fourteen in four shapes**, measured by `Tester` at `PT-1470`. `argv[1]`
is **the file I will overwrite in seven** and the file I will read in six:
near-equal populations, which is why no habit protects you.

`_paths.dest()` refuses a `.md` destination **and** a `.json` that belongs to a
different extract — the script derives its own expected output from its
filename. **The orders themselves are still inconsistent**, recorded and
deferred.


### ⚠ Open from `Tester`'s fourth report — the droid run

| | Need |
|---|---|
| ~~⚠⚠ **`PT-1464` — my droid wiring HARD-BLOCKS four classes**~~ | ✓ **closed at `BUILD 50`** — the bar is at the class step, and a test asserts the two halves cannot drift |
| ~~⚠ **Ten array cells mix a VALUE with an ANNOTATION**~~ | ✓ **closed at `BUILD 50`, both tables.** ⚠ The organic one carried a **resref** — *"Ion Blaster — w_blaste_02, 50cr"* — on screen, which is `D3` from inside a value |
| ⚠ **A test can pass only because a rule is unenforced** | `subrace_test` drove a droid into **Soldier** and completed — the behaviour `PT-1464`'s bar removes. **The first sign was a failure that looked like a regression.** Worth naming as a shape |
| ⚠⚠ **`PT-1464` — my droid wiring HARD-BLOCKS four classes** | Soldier, Marksman, Brawler and Saboteur, **with Soldier the pre-selected default** — pick Droid, leave the class alone, and you cannot create a character. ⚠ **I called null "the honest answer" and asserted it in a test; it is honest and enforced at the WRONG STEP.** `STARTING-EQUIPMENT-01 §3` opens nine of eighteen classes to a droid and means it. **The bar belongs at the CLASS step**, as `PT-92` greys out the Force classes there. The nine are on disk — `droid_arrays.toml` has exactly nine rows |
| ⚠ **Ten array cells mix a VALUE with an ANNOTATION** | *"1 Sensor Probe — was Adrenal Stamina"*, *"NONE — the class feature is the weapon"*, *"Ion Blaster — w_blaste_02, 50cr"*. **`PT-1463`'s defect in a second file**, and `PT-1464` reports it now printing to players. ⚠ **This, not unresolved names, is what actually blocks arming the player** |
| ⚠⚠ **`item_disambiguation.toml` — 14 rows, ZERO readers** | ⚠ **It is the answer to a blocker I cited twice.** `STATE` has said arming the player is blocked because *"only 18 of 41 array names resolve to exactly one catalogue row; §2c disambiguates 14"* — **those 14 ship in `base-rules` and nothing opens them.** The remaining gap is 41 − 18 − 14 |
| ⚠ **`two_weapon.toml` — 19 rows, ZERO readers** | The per-class two-weapon kit. Authored, shipped, unread |
| ⚠⚠ **23 of 30 duplicated documents have DIVERGED** | `HANDOFF/docs/` is **the copy visible to the owner's token** and is stale in 23 of 30 — `PLAYTEST-RULINGS-01` is **11,781 lines there against 54,233** at source. ⚠ **`sync_docs.py` was built for exactly this at `PT-245` and its paths no longer exist**: it globs a directory that is not there and prints *"docs/ matches the working tree"*, rc 0. **Its own slice** |
| ⚠ **`starting_equipment.json` is stale** | From `PT-1464`'s edit. `event_kinds` stays stale deliberately |
| ⚠ **`Environmental Sealing` says `selectable` and means `granted`** | Its own description reads *"Granted at 1st level to every droid"*, and `availability` **already has a `granted` value used by 188 feats.** A wrong value, not a missing field — **and deriving it from prose is `TRACE-83` again.** This is why a droid is still charged for a feat it already has |
| ⚠ **`Plating Proficiency: Light` is misfiled at source** | Line 80 of `FEATS-LIBRARY-01`, under **§3 Organics only**, its own text saying **DROID ONLY**. **The extraction is faithful; the source row belongs in §4.** ⚠ Marked at source as `PT-1462`. *(My earlier claim that it was absent from the document was wrong — I grepped `HANDOFF/docs/`'s stale copy.)* |
| ⚠ **Feat groups 2 and 5 are still offered to everyone** | Group 2 is *"organics and combat droids"* and **nothing says which chassis is a combat droid**; group 5 is restricted by class or chassis and **the extract carries no field naming which.** Left offered rather than guessed at, with a test asserting they still are |
| ~~⚠⚠ **The bed's own conversation is INVALID**~~ | ✓ **closed at `BUILD 47`** — four answers, authored in Loom. |
| ⚠⚠ **The bed's own conversation is now INVALID, and the fix is authoring** | `PT-1459` refuses a check that cannot roll, and **Loom authors one.** What a successful `Persuade` LEADS TO is content — **not code, and not `Coder`'s to invent.** The Loom test asserts the one known problem by name so it cannot grow quietly. **Owed a decision** |
| ⚠ **A feat record has no eligibility field — the Feats wire is a STOP** | `FeatsScreen` has the same missing chassis as Equipment, **and wiring it changes nothing**: `feats.toml` says *"Granted at 1st level to every droid"* in **prose** and carries `availability = "selectable"`. Filtering on prose is `TRACE-83` again. **Not wired — a parameter nothing can use is building ahead** |
| ⚠ **The front-ends silently run an older engine** | `PT-1458` shipped and **the app stayed pinned to the commit before it**, so the save went on being refused by a build containing the fix nowhere. `BUILD/37` wrote this down and it still caught me. **`droid_loads_test` now asserts the RESOLVED engine behaves** |
| ~~⚠⚠ **The droid path is TWO causes**~~ | ✓ **the Equipment half closed at `BUILD 46`.** |
| ⚠⚠ **The droid path is TWO causes, not six bugs** | `BUILD 45` swept it. **A screen consults `isDroid` when the answer changes WHETHER it renders, and not when it would only change WHAT IT OFFERS** — `equipment_screen` and `feats_screen` mention a droid **zero** times. ⚠ **And underneath: there is nothing to filter on.** `feats.toml` says *"Granted at 1st level to every droid"* in **prose** and still carries `availability = "selectable"`; `class_arrays.toml` is keyed by class and mentions a droid **not once**. `droid_skills.toml` is a whole file, **which is why `SKILLS` is the best screen in the app** |
| ⚠ **A feat record has no field for who may take it** | `id · name · chain · is_chain_head · section · description · effect · availability`. **One missing field, two symptoms**: a droid is charged for a feat it already has, and an organic is offered `Droid Upgrade 1`. `U2` from both sides |
| ⚠ **`[Persuade]` offered to a droid — a RULING, not a bug** | `_rank` returns 0 for an absent skill so a droid rolls untrained, which may be legal. **`SKILLS` says *"closed to every droid"* and nothing reconciles the two** |
| ⚠ **Four of six conversation options are dead ends** | **The bed's content** — four player lines carry no `then`. ⚠ **But the validator reports ZERO problems on that file**: it checks unreachable nodes and dead links and **not *a check with nothing to roll toward*.** A show-all reply with a `skill` term renders amber and never rolls, so **the bracket promises a roll the structure cannot deliver.** Fix the validator first |
| ⚠ **A conversation that ends says nothing** | `Tester` took `[Persuade]`, the panel closed, and nothing said whether it passed |
| ⚠ **Raw resrefs reach the player** | Five of seventeen programmings — `Parts — g_i_parts01`. **Upstream in `gen_base_rules.py`**, and `Protocol Droid`'s grant is the only fully upper-case one of the seventeen |
| ⚠ **The abilities screen explains a Remote using Battle's numbers** | A hardcoded example in a screen that otherwise knows about droids — **the one true screen bug of the six** |
| ⚠ **Losing a fight is never stated** | Tester went to −4 of 12; the marker is drawn as before and it still offers *arrows to move*. Outside a fight the player has no working line at all |

### ⚠ Open from `Tester`'s first report

| | Need |
|---|---|
| ⚠ **Eight defects and three questions are open** | `BUILD 41 §4` names them all. The sharpest: **the hub tells the player nothing is saved directly above the button that saves** — the sentence that produced `PT-1443` — and **Loom's entry-area chooser sits below the fold**, which is `BUILD/34`'s rule a fourth time |
| **23 test files lie about their viewport** | ✓ **sized at `BUILD 42`, and it is hygiene rather than re-verification.** `MediaQuery` claims 1280×720 while the surface stays **800×600**. ⚠ **NONE of the 23 asserts a geometric fact** — all are text-and-interaction; the single `getCenter` is positioning a mouse, not claiming a layout. So **no published layout number rests on them**, and **the side panel is not among them**: its tests set the surface, and its tile figure was cross-checked against a real capture (56px computed, ~57px on screen). The cost of the fix is 23 one-line additions; the gain is removing spurious overflow noise like the 78px one at `BUILD 41` |
| ⚠ **Three `check_*.py` exit 0 having examined nothing** | From an empty tree `check_derived`, `check_absence_claims` and `check_stale_claims` print *"0 declared pairs"* / *"0 documents known"* and **still exit 0**. A reader sees the zero; **automation reads the exit code** |
| ⚠ **`check_citations` exits 1 today** | `TEMPORAL-LEAKAGE-FINDINGS-01 §2` unresolved; `check_extracts` reports `stale 1`. **Pre-existing, found while auditing, not touched** |

### ⚠ The live wall is clear

| | Need |
|---|---|
| **Nothing is open here** | ✓ `PT-1443`'s save work and the suite's writes into live data both closed at `BUILD 38`. What remains of `PT-1443` is design — the next section |
| ⚠ **A temp-directory test passed where the real path failed — three times** | `PT-1382`, `PT-1425`, `PT-1417`. **The pattern, not the instances, is the finding** — and it is why `BUILD 38` kept every real-shelf READ rather than sandboxing the suite wholesale |

### Asked for at the playtest, and not built

| | Need |
|---|---|
| ~~**The side panel**~~ | ✓ **built at `BUILD 40`, `PT-1447`.** ⚠ **The tile is 56px, not the 66px promised** — `Lens` insets a board by one tile all round and the estimate divided by the room's size instead. Still nearly double the 29px recorded before |
| ⚠ **The replies start at five different x positions** | Each bracket is a different width and two options carry none, so the left edge is ragged in a narrow column in a way it never was in a wide band. **`§4c` rules colour and says nothing about alignment.** Found by a capture, reported not decided |
| ⚠ **Two agents share one data folder** | `BUILD 38`/`39` stopped the suites WRITING to live data. **Reads are only deterministic while nobody else writes** — `Tester` made a package mid-slice and three of my assertions failed on correct work. Fixed by naming packages instead of counting them; **the general hazard stands** |
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
| ⚠ **`subrace_test` passes only because its viewport is wrong** | The one file the hygiene sweep did NOT get. A real 1280×720 surface makes the Zabrak tap land at y≈616 and miss; Zabrak is both a species and its own subrace so the finder is ambiguous and neither end of it reaches the right row. **Whether that row is reachable at all at 1280×720 is a PRODUCT question** — the clipped-reply shape again. Named in the file, not diagnosed |
| ⚠ **The player's log `subject` is their DISPLAY NAME** | `identity['name']`, where creatures use a tag — **`PT-1445` ruled a log records the id, never the name**, and this is a permanent entry breaking it. Found in the owner's saves. **Re-keying orphans every existing player outcome**, so it is a migration and a ruling, not a patch |
| ⚠ **`check_extracts` stale 1 — and re-stamping would hide it** | `event_kinds.json`, **not equipment**. Two copies of `EVENT-KINDS-01.md` have diverged; the rows are byte-identical, so the DATA is current. **The lag is in the code**: `PT-1435` says check A must compare against the **union of what every projection folds**, and `emitted_kinds_test` still uses `handledByReplay` alone |
| ⚠ **`[requires] packages` and multiclass: never tested with two** | `§4` makes the order the precedence; `PT-723` caps classes at three. **Chargen writes one and one rules package exists**, so both folds have only ever seen a single element |
| ~~⚠⚠ **`PT-1453` — the wound is HALF fixed**~~ | ✓ **closed at `BUILD 44`.** | `BUILD 41` fixed the path it tested, not the one the request quoted. **My reading of the third exit:** `_endFight` and `_enter` persist; **leaving the screen with `esc` goes through neither.** Plus **N1** a second fight in an area with outcomes in the log ends immediately, and **N2** the working line grows without bound — six from one fight. **Not started; its own slice** |
| ⚠ **The player is unarmed, and it is TWO fixes** | The seam half is done and shared. The other is chargen writing an `[equipment]` reference, which needs the class arrays' prose names to resolve to blueprint paths — **the same 18-of-41 problem that keeps Route 2's purse unoffered.** Not a seam change |
| ⚠ **The viewport hygiene, 23 one-line additions** | Sized at `BUILD 42` as hygiene, not re-verification. **Deferred deliberately at `BUILD 43`**: a sweep across two repos folded into a feature slice makes both harder to review |
| ~~⚠⚠ **Equipment is authorable and CANNOT be read**~~ | ✓ **closed at `BUILD 43`, `PT-1452`.** | `items/weapons/blaster-rifle` names `blueprints/items/…`, **a folder in `PACKAGE-FORMAT-01`'s layout with no format behind it and no reader** — the third instance of `BUILD/34`'s stop. The one thing that looks like an answer, `base-rules`'s `equipment.toml`, is the wrong shape: resolving a path by its last segment would make `PACKAGE-NAMING-01`'s *"identity and location are the same thing"* false, and its damage sits in an **untyped positional `values` array** whose shape changes by section. **Needs: what an `[equipment]` value refers to, and the format of whatever that is** |
| ⚠ **`unarmed` is still ours** | `EQUIPMENT-01` has 25 base weapons and **no unarmed row**, so those dice are invented. `PT-1425` named it a placeholder; `PT-1452` did not change that. **Defined once now**, so the next search for invented numbers finds one hit |

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
| **The item blueprint, and the equipped weapon** | ✓ `BUILD 43`, `PT-1452`. `[equipment]` → item → base type → dice, and **every link fails out loud**. The trooper's hardcoded vibroblade is gone — **a melee weapon swung at range by a creature holding a rifle.** ⚠ And the extraction's positional array **silently shifted**: a dropped em-dash put the Stun Baton's `attacks` in `balanced`'s place |
| **The bar at the class step** | ✓ `BUILD 50`, `PT-1464`. ⚠ **The regression was mine** — I called `null` the honest answer and it was, at the wrong step. `§3` opens nine of eighteen and **a missing droid array is that line, enforced** |
| **The player's own attack line** | ✓ `BUILD 50`. It was **computed and never rendered** — `_playerStrikes` set `_said` and `_enemyTurns` overwrote it in the same synchronous call. ⚠ **That is why `PT-1326` was verified on NPC attacks only**: not a different format, no screen |
| **`extract_feats.py`** | ✓ `BUILD 49`, `PT-1463`. The corpus's largest extract **could not be re-run at all** — ad hoc at batch 3c, like `equipment.json` before it. ⚠ **The control is exact reproduction and it passes**: 320 of 320, zero field differences, only `source` lines moved. Three bugs in the first attempt were invisible in the output and obvious in the diff |
| **The Builder refuses what `validate` refuses** | ✓ `BUILD 47`, `PT-1379`/`PT-1461`. The tab showed the problems the whole time **and wrote anyway** — which is why `PT-1459` made the bed invalid: **Loom wrote it.** Refuses on ANY problem, so a later check needs no wiring |
| **The feat eligibility field** | ✓ `BUILD 47`, `PT-1460` — ⚠ **and it already existed.** `section` IS `FEATS-LIBRARY-01`'s five groups, counts matching 16/9/68, **and nothing read it.** Same shape as `droid_arrays.toml`, one slice apart |
| **A front-end pinned behind the engine** | ✓ `BUILD 47`. `check_engine_pin.py` catches **the class, not the instance** — a test can only fail on behaviour it already knows to look for. Compares each lock to the engine's `origin/main`; `PT-1451`'s three exit codes, all controlled |
| **`droid_arrays.toml` is read** | ✓ `BUILD 46`, `PT-1459`. It shipped in `base-rules` since the extraction with **exactly the droid kit per class** and **nothing anywhere opened it** — a disconnected wire, not a missing feature. ⚠ **And the boots were a HARDCODED ROW**, which is why a hoverer got treads |
| **A dead check, and the end of a conversation** | ✓ `BUILD 46`, `PT-1459`. `_pick` returns null **before any dice are touched**, so amber promised a roll that could not happen. And the runtime **manufactured `NpcLine(id: '', say: '')`** — the shape `PT-1433` refuses from an author — which the app sniffed to notice the end **and then said nothing** |
| **`PT-1458` — a droid bases at 10** | ✓ `BUILD 45`. The validator applied the **organic** point-buy floor to an authored production spread and refused a character the app had built and called final. ⚠ **Verified on `Tester`'s own `t3-k9.sav`**, which now validates legal. And the spreads are **authored to parity at 72**, not derived from the base — deriving would have made every droid twelve points weaker than any organic |
| **The attack line carries its derivation** | ✓ `BUILD 45`, `PT-1326`. It named the roll and what was LEFT and never what fired or what was subtracted |
| **The third exit, N1 and N2** | ✓ `BUILD 44`, `PT-1453`. ⚠ **Three shapes of one class**: a CONSUMER with no producer (`character.revived` was handled and never emitted — N1), a PRODUCER with no guard (`_endFight` re-entrant, six outcomes from one fight), and a FOLD whose value and narration disagree (N2). **All three are invisible until a sequence exists** |
| **The wound surviving a quit** | ⚠ **half** — `BUILD 41`, `PT-1448`. `PT-1427` built the projection and **nothing wrote what it folds** — two paths end an encounter and only one persisted, and the log was discarded after replay. **The question the code called undecidable was already answered**: `encounter.ended` is `campaign` and `PT-1415` makes the log one per character per campaign |
| **The runner faking a pass** | ✓ `BUILD 41`. It built only when the binary was **missing**, so after the first run it never rebuilt again — for any change, ever. ⚠ **The third instrument to report success without looking** |
| **The dialogue side panel** | ✓ `BUILD 40`. The board keeps FULL height and gives up width it was not using. ⚠ **`maxLines` was the click bug in a second costume** — ample in a 1280px strip, truncating in a 480px column |
| **`§4c`'s colours** | ✓ **asserted at `BUILD 40`**, and nothing guarded them before. `TRACE-93`'s defect had been reproduced twice and caught by a person looking both times |
| **The tree moved to the Steam library** | ✓ `BUILD 37`. Baseline before, identical after. **No path dependency existed** — `Lens` and `Lodestar` are git dependencies through `~/.pub-cache` |
