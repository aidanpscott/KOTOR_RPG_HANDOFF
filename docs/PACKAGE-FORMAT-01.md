# PACKAGE-FORMAT-01 — what a package is

**Tier 1 of `AGENDA-DRAFTING-01`, and the thing the seven-batch study was for.** Deferred at `PT-1248` as "a much larger project"; the study removed every reason to keep deferring it.

**⚠ Addressing is `PACKAGE-NAMING-01` and is not repeated here.** This document is what a package **contains**, how it **declares** itself, and what it means to **open one**.

---

## 1 · The one sentence

> **A package is a folder. The manifest says what is in it and what it needs. Nothing is discovered by scanning.**

**That is `TRACE-89`'s central mechanism**, and it is the single thing NWN did that KOTOR removed:

> *A module declares what it needs, by name, in its manifest. Nothing is discovered by scanning a folder.*

**Why it matters more than it sounds.** `TRACE-81` spent two full batches trying to determine KOTOR's precedence and **closed it as not determinable** — four shadowing layers with nothing declaring their order. `TRACE-89` answered the same question for NWN **by reading one field.** That is the cost of putting a rule in code rather than in data.

---

## 2 · A folder, not an archive

**Packages ship as folders.** Compression is a distribution concern, not a format one.

**⚠ Three reasons, and the third is the one that decides it:**

- **`git diff` works.** A package is versionable by ordinary tools.
- **A modder can look.** You said they will, and `PT-1282` designs for it.
- **⚠ `TRACE-86`'s retraction is impossible here.** Two study batches concluded `.mod` files shipped when the engine writes them, because **shipped and runtime-written files sat side by side in one directory and the format did not distinguish them.** A package folder is authored content only. **Runtime state never lives inside it.**

---

## 3 · Layout

```
my-campaign/
  package.toml            the manifest
  items/
    weapons/
    armor/
  areas/
    a01-endar-spire/
  blueprints/               ⚠ PT-1374 — the nine categories, one folder each
    characters/  doctrines/  doors/  items/  placeables/
    encounters/  sounds/  stores/  triggers/  waypoints/
  quests/
  dialogue/
  scripts/
  tilesets/                ⚠ NEW at PT-1363 — art and prefabs, never rules
  rules/                  ⚠ package-local rules
  strings/
  assets/
```

**⚠ `rules/` is the folder KOTOR does not have.** `TRACE-82`: **no module-local rules table exists in either game — not one.** Every archive under `modules/` in both games was searched; zero. **A campaign could not say "in my content this weapon hits harder" without changing it for every campaign installed.**

**Every folder is optional.** A package with three items and no areas has three folders.

---

## 3a · ⚠ Video — declared in the package, stored beside it, `PT-1308`

**Owner ruling: packages carry prerendered video, and any mp4 can go in a slot.**

**⚠ The problem this creates, and `TRACE-94` supplies the fix.** `§2` says a package is a folder you can `git diff`. **Hundreds of megabytes of binary in a versioned tree defeats that.** But KOTOR never put movies in its archive system: **a movie is named by a plain string** — *not* a resref, though the format has that type, and not an index into `movies.2da`. It sits in its own directory and a script names it.

**So the package DECLARES its movies; the files sit BESIDE it.**

```
my-campaign/
  package.toml          declares the slots
  movies/               excluded from versioning
    endar-spire-fall.mp4
```

```toml
[movies]
endar-spire-fall = { file = "endar-spire-fall.mp4", skippable = true }
```

**⚠ A slot is a NAME. The payload is whatever sits at that name** — so any mp4 works, and swapping one is a file operation rather than an edit.

**Loading fails loudly on a missing file**, per `§6`. **A declared movie that is not there is an error, not a silent skip** — `F35`'s lesson.

### ⚠ The queue, taken from K2

**`TRACE-94`: K1 made 63 `PlayMovie` calls and zero queue calls. K2 made 10, plus 26 `QueueMovie` and 7 `PlayMovieQueue`.** K1 played one movie and forgot it; **K2 built sequences from reusable pieces.**

**So 1,600 MB across 67 files did not buy longer movies — it bought movies that COMBINE.** K2's `a_playpermov` picks one of **seven** files by script parameter, which is how you get branching cinematics **without seven full renders.**

**We take the queue.** A sequence of named slots, played in order, then control returns.

### ⚠ Movies may play MID-SCENE, not only at an ending

**`TRACE-94`'s clearest K1→K2 shift.** K1's five movie-calling dialogue nodes are **all terminal** — the movie ends the conversation. **K2 has four that CONTINUE.** **The movie is a beat inside the scene rather than the end of it**, and that is the better model.

### ⚠ A slot's file is a BEAT, not a SCENE

**The queue only works if the pieces were cut to combine.** Matching first and last frames, consistent letterboxing, **no fade baked into the file** — the queue supplies those. **A file that fades to black at its own end cannot sit mid-sequence.**

**⚠ This must be met at render time and cannot be fixed afterwards.** K2 got seven combinable `permov` variants out of exactly this discipline. **Tracked in `ASSET-REPLACEMENT-01`.**

### ⚠ One thing NOT taken: the hard cut

**`FadeType` is 0 on all sixteen movie-calling nodes across both games, without exception.** That reads as an engine limit rather than a choice.

**⚠ We fade.** KOTOR cut straight to video from an already-cinematic 3D scene. **Ours would cut from a dialogue bar over a 2D grid**, and the jump is far larger. **Open: the fade's shape and length.**

---

## 4 · The manifest

**Modelled on NWN's, which is the only one in the study that works.**

```toml
[package]
format      = 1                      # ⚠ NEW at PT-1366 — which FORMAT, not which package
id          = "my-campaign"          # identity — never changes
name        = "Shadows of Taris"     # what a player reads
version     = "1.2.0"
authors     = ["..."]                # ⚠ REQUIRED from PT-1358
summary     = "..."                  # ⚠ NEW — one line, required
cover       = "cover.png"            # ⚠ NEW — optional

[requires]
engine      = ">=1.0"
packages    = [
  { id = "base-rules", version = ">=2.0" },
]

[continues]
chain       = "my-first-campaign"    # ⚠ cross-campaign carry

[order]
areas       = ["a01-endar-spire", "a02-taris-hideout"]

[entry]
area        = "a01-endar-spire"
```

### ⚠ `[requires].packages` is ordered, and that IS the precedence

**One ordered list. Later entries win.** That is `Mod_HakList`, and it is the whole mechanism.

**⚠ NWN's own flaw is fixed here.** `TRACE-89` found NWN's precedence direction expressed as **a naming convention** — `_top` and `_core` suffixes in two unrelated projects. **A convention is not a declaration.** Ours is positional and explicit.

### ⚠ `[order]` is why nothing but areas carries a number

`PACKAGE-NAMING-01 §4` numbers areas because modders read raw folders. **The manifest carries the authoritative order**, so an inserted area gets `a03` out of sequence and **the manifest still knows the truth.**

**Order is a field. It is never inferred from a name.**

> **⚠⚠ AND IT IS MEMBERSHIP AS WELL AS ORDER — `PT-1505`.** The section is named `[order]` and **two of three programs already read it as the package's roster:** `targetAreaUnknown` exists as a fault, and Loom refuses to author a connection to an unlisted area.
>
> **⚠ The play client does not read it at all.** `TEST 017` removed an area from the list, left the file on disk, walked into its door, **and the app took it there.** Board, arrival point, everything. **Nothing said anywhere.**
>
> **⚠ AND THE HARM IS NOT "A BROKEN PACKAGE LIMPS":** a player can be taken into **content the package declares is not part of it**, and **removing an area from the manifest has no effect on what a player can reach.**
>
> **RULED: an area not in this list is not in the package.** The manifest is the roster; **the folder is storage.** A package's contents are **declared, not discovered** — otherwise a stray file left in a folder becomes content, and `PT-1368`'s missing-versus-degraded distinction has nothing to measure against.
>
> **⚠⚠ AND `§1` ALREADY REQUIRED THIS — `PT-1507`.** *"A package is a folder. The manifest says what is in it and what it needs. **Nothing is discovered by scanning.**"* Line 11, and **`TRACE-89`'s central mechanism.**
>
> **So `PT-1505` is not a sentence I added.** `[order].areas` is the only field saying which areas a package has, **so membership was always the manifest's job** — and **the play client is the one program that never implemented `§1`.** Two of three were already obeying it.
>
> **⚠ That changes what kind of fix it is:** not a new rule reaching a program that disagreed, **but a rule that never reached one program at all.**
>
> **⚠ The section name is misleading and it stays.** Renaming it breaks every package written, and `format = 1` exists for changes that earn it. **This one is a sentence, not a version.**
>
> **⚠⚠ AND `§1` ALREADY REQUIRED THIS — found at the build, and it changes what kind of thing the fix was.** *"A package is a folder. The manifest says what is in it and what it needs. **Nothing is discovered by scanning**."* `[order].areas` is the only field that says which areas a package has, so **membership was always the manifest's job.** `validateConnections` reads areas that way and always has; `Loom` refuses to author past it. **The play client was not disagreeing with a new rule — it was the one program that never implemented `§1`.** The ruling names what was already required rather than adding to it.

---

## ⚠ 4·1 What a library tile shows — `PT-1358`

**`PT-1355` found the gap and `PT-1357` made it concrete: a tile could show a name and a version, because that is all the manifest carried.** Ten packages would be ten near-identical boxes.

**⚠ And the sharpest form of it: `APP-UI-VISION-01 §0` SPECIFIES THE FIELDS FOR THE PUBLIC GAMES LIST AND NOT FOR THE LIBRARY.** A listed multiplayer game shows **package name, host and seat count** — specified, and sourced from NWN's own browser. **The library tile, which is the app's main content, had no field list at all.** One of the two got designed.

### The tile's fields

| | | |
|---|---|---|
| **`name`** | required | already there |
| **`version`** | required | already there |
| **⚠ `authors`** | **now REQUIRED** | was optional. **Every store tile in existence shows an author**, and a tile cannot rely on an optional field |
| **⚠ `summary`** | **required, NEW** | **one line.** A tile with only a name cannot tell you what a package *is* |
| **⚠ `cover`** | **optional, NEW** | a path to a still image. **Optional because a package must be makeable without art** |

**⚠ `summary` is required and `cover` is not, and that asymmetry is the point.** A package with no summary is unbrowsable; **a package with no cover is plain.** One breaks the screen, the other does not.

### ⚠ Nothing temporal, deliberately

**No `created`, no `modified`, no `last-played`.** An author writing a date into a manifest is **writing a claim, not a fact** — and the app can read a filesystem timestamp for its own sorting without the format asserting anything.

**This is the same refusal as need A**, where `Continue` could not know which save was latest and **the answer was not to let the app guess from `mtime`.** Here the app may guess, because **which tile sorts first is not a fact about the package.**

### For the Builder

**⚠ CLOSED at `PT-1383` — DEFERRED, not defaulted.** `§4·1` offered either. **Defaulting was available and is dishonest:** the OS account name for `authors` **attributes a credit to someone who did not claim it**, and the package name repeated as `summary` **tells a browser nothing while looking answered.** Both **write a claim the author never made.**

**So both live in Package Properties, and `validate` reports them outstanding until answered.** **⚠ A required field left empty cannot be SAVED as empty** — that would write the absence rather than leave it outstanding.

**⚠ And `New Package` is untouched, with a test asserting the created manifest contains NEITHER field** — so a future change that adds a third question **fails a test that says why.** `TRACE-106` measured Aurora's path at two typed things and ours still matches.

**⚠ AND THIS NEVER REACHED LOOM — `PT-1382`.** `PT-1358` made `authors` and `summary` **required** and **New Package still writes neither.** Every package Loom has made is missing two required fields. **A ruling filed and not propagated, which is this project's most repeated failure.**

**⚠ `summary` becomes a third thing New Package asks**, which breaks `PT-1356`'s two-name path. **It should be defaulted or deferred, not added as a question** — `TRACE-106` measured Aurora's path at two typed things and ours matched. **Losing that to a description box would be a poor trade.**

---

## ⚠ 6a A missing ASSET degrades. A missing DEPENDENCY fails — `PT-1368`

**`§6` loads loudly and refuses at every step. That is right for RULES and wrong for PICTURES**, and the line is:

> **A missing rule breaks the game. A missing picture does not.**

| | | |
|---|---|---|
| **a declared package dependency** | **FAILS LOUDLY** | `§6`. Rules are missing; nothing downstream is trustworthy |
| **a declared movie** | **degrades** | `PT-1308` already ruled this — *"sharing anything with a cutscene would require shipping the cutscene"* |
| **⚠ a declared tileset** | **degrades** | `PT-1368` |

**⚠ And a package may legitimately require textures a player does not have** — because they came from KOTOR and **the player does not own it.** `PT-1350` ships no source assets and offers extraction from the user's own copy; **someone without the games simply cannot extract them.**

**That must not make the package unplayable.** It is **a picture, not a rule.**

### ⚠ And the fallback is not a placeholder — it is the drawn look

**`PT-1364` and `PT-1366` already built it: walls are mass, floor is a lit surface, and it STANDS ALONE.** `§2b` required exactly that — *"a default that looks unfinished makes every package without art look broken."*

**So a missing tileset does not need placeholder art invented for it. The board draws itself.** The player gets **the untextured default, which is complete, ours, and a preference rather than an absence** (`PT-1366`).


**⚠ CORRECTED at `PT-1369`: there are TWO rungs below extraction, not one.** **Our own textures** — tier 2 of `PT-1366`, aiming at the same feel and honestly plainer — **and the drawn look beneath those**, for a package declaring no tileset at all.

**So someone without the games gets a TEXTURED board, not a diagram.** That is a materially better outcome than the single fallback originally ruled.
**⚠ It degrades LOUDLY though, not silently.** The package says which tileset it wanted; **the app says it is not installed and why.** `F35`: an engine that quietly substitutes is an engine nobody can debug.

**⚠ Assets with no drawn equivalent still need placeholders** — icons, portraits, chrome. **`PT-1351` remains open for those**, and `PT-1157` governs: a placeholder must be visibly a placeholder.

---

## ⚠ 3c · What is IN `rules/` — `PT-1386`

**`§3` gave the folder nine words and one paragraph on why it exists. Nothing said what goes in it, and chargen stopped on that.**

### A rules file is the extraction, shipped

```
rules/
  species.toml      classes.toml     skills.toml
  feats.toml        powers.toml      models.toml
  professions.toml  upbringings.toml programmings.toml
  equipment.toml
```

**⚠ One file per KIND, named for the kind.** `data/extracted/` already produces exactly these — **the extraction was the hard half and it is done** (`TRACE-96`–`TRACE-100`, `PT-1385`).

**⚠ TOML, not JSON, for one reason: it is what every other file in a package is**, and a format an author can hand-edit is the point of the whole design. **The extraction's JSON is an intermediate, not the shipping shape.**

### ⚠ `base-rules` is a package, and it is OURS

**`§4a`'s example — `{ id = "base-rules", version = ">=2.0" }` — is real.** It is **a package with no areas, no characters and no entry**, carrying only `rules/`.

**⚠ `PT-1380` already made room for it:** *a package that declares areas must declare an entry; a package with no areas need not.* **That conditional was written for exactly this.**

**And it ships with the product** rather than being downloaded — **the app is unusable without it**, which is different from every other package.

### ⚠ How a campaign's `rules/` combines with `base-rules`

**`§4`'s `[requires]` is already ordered and `PT-1282` rules that order IS the precedence: later entries win.** A campaign declaring `base-rules` and carrying its own `rules/species.toml` **is a later entry.**

> **⚠ Merge per RECORD, not per FILE.** A campaign adding one species must not have to restate thirty-four.

**A record with an id `base-rules` already used REPLACES it. A new id ADDS.** **⚠ And nothing deletes** — a campaign cannot remove a species from the game, only replace or extend. **Removal would break any other package that references it.**

### ⚠ The record shape — `PT-1389`

**`PT-1386` left this open and it is the last thing before `base-rules`. The rule is one line:**

> **A rules record carries what the RULE says. It does not carry how we came to know it.**

**⚠ The extraction is not the shipping shape**, and the gap is measurable: **a class record has 30 fields and SIX are provenance** — `source`, `phb_source`, `phb_status`, `abilities_source`, `class_skills_source`, `feat_levels_source`. **A fifth of the record is bookkeeping about where a value was read.**

| stays | drops |
|---|---|
| `vitality_die`, `skill_points`, `class_skills_ranked`, `saves_at_20`, `save_ladders`, `feat_levels`, `primary_ability` | `source` and every `*_source` — **a line number in a document a player does not have** |
| `availability` on a feat — **`PT-1387`: a flat list would GRANT rather than offer** | `counted_in_summary` — **`TRACE-111`: it reconciles a file to a table, and neither ships** |
| `is_chain_head` — **chains are mechanics** | `phb_status` — build status, not a rule |
| `marked_in_source` where its meaning is known | `table` — which markdown table a row sat in |

**⚠ The test, and it settles the arguable cases:** **would a package author writing this record BY HAND fill this field in?** They would write a vitality die. **They would not write which line of `CLASS-ROSTER-01` it came from**, because they are not copying from it.

### ⚠ Subraces are RECORDS, and the picker filters — `PT-1391`

**`base-rules` shipped 35 species and dropped 22 subraces, flagged as a known gap. ⚠ They are load-bearing, not a picker nicety.**

**`CHARGEN-FLOW-MAP-01 §4`: *"SPECIES → subrace/chassis → resolves ability, skills, senses, trait."*** **The subrace is what resolves the mechanical values** — an `Aqualish, Aquala` carries `ability_adjustments`, `skill_bonuses`, `speed` and `fins`. **Without it, eight species cannot produce a character.**

> **`species.toml` carries all 57 — 35 parents and 22 subraces, flat, each with its own `id` and a `parent` where it has one.**

**⚠ And the concern that motivated dropping them is answered by the PICKER, not by the FILE.** The worry was *a rules file listing 52 would put `Aqualish Quara` beside `Human` at the top level.* **It would not: the picker shows records with no parent.** Filtering is a display decision; **the file's job is to hold the rules.**

**⚠ And flat beats nested because of `PT-1386`'s merge.** Per-record replacement turns on `id`. **A campaign adding one subrace to an existing species writes one record** — nested under a parent, it would have to restate the parent to reach it.

---

### ⚠ And an id is the only identity

**`PACKAGE-NAMING-01`: the path is identity.** So a rules record needs `id` and nothing else to be found. **`PT-1386`'s per-record merge turns on that id** — a repeated id replaces, a new one adds.

**⚠ Provenance does not vanish, it MOVES.** `data/extracted/` keeps every `source` field and its fingerprints. **The JSON is the audit trail; the TOML is the rule.** That is the same split as `PT-1369`'s ours-versus-theirs — **two records of one thing, for two different questions.**

### ⚠ What this makes possible, and it is the reason to rule it now

**A rules file becomes hand-writable.** A package adding one species writes **seven fields**, not seven plus a citation to a document it has never seen. **`PT-1386` chose TOML precisely so an author could do that**, and a record full of extraction bookkeeping would have made it a lie.

### ⚠ What this does NOT settle

- **The record shape per kind.** `CHARGEN-DATA-01 §3` specifies some; **`classes.json` proves the extraction does not meet it** (`PT-1385`).
- **⚠ Whether a package may replace a rules record at all**, or only add. Replacement is where two packages genuinely conflict, **and `§4a` gives dependencies an order precisely so that has an answer** — but nobody has tested it.
- **Who writes a rules file.** Loom has no editor for one, **and `STUDY 17` found Aurora had none either — not one form in 105 mentions 2DA.** No precedent either way.

---

## ⚠ TO DO — a package may CLOSE a choice, `PT-1412`

**Owner ruling, queued rather than built. A package author decides what a player may start as.**

```toml
[creation]
species_closed = ["droid", "rakata"]
classes_closed = ["sith-warrior"]
```

**⚠ CLOSED, not removed.** `PT-1361`'s vocabulary is ours and fixed — **a package cannot delete a species from the game**, only refuse it at creation. **The same distinction as `§3c`'s merge: a package replaces or adds and never deletes.**

**⚠ And a closed choice must say it is closed rather than vanishing.** `DROID-SKILLS-01`'s five states settled this shape already: **closed by rule is a positive statement and reads as one.** A species silently absent looks like missing data; a species marked *"this campaign does not admit droids"* is authoring.

### ⚠ It lands in BOTH programs

**Loom needs the surface** — a package properties tab, where `PT-1380` put `[entry]` and `STUDY 16` found Aurora's haks.

**The app needs the filter**, at Species and Class in the pre-hub.

**⚠ And `validate` needs a rule nobody has written: what happens when a package closes every class a species can take?** `PT-92` already bars droids and Rakata from Force classes — **a package closing the rest could make a species unplayable without saying so.**

---

## ⚠ AN AUTHORED ARTIFACT IS A COPY OF THE DATA — `PT-1480`

**`TEST 012` found one item with two spellings on two screens, and the cause was not what either of us guessed.** Not title-casing: **Loom's own tool authored the blueprint carrying the then-current `Hold-Out Blaster`, and `PT-1477` corrected the DATA and not the COPY.**

> **⚠ Every blueprint Loom writes is a SNAPSHOT of the corpus at authoring time, and nothing compared them.**

**That generalises past one hyphen.** `PT-1346` made the Builder's output the test bed **precisely so content is reproducible** — and reproducible is not the same as **current.** **A blueprint authored in March against a rule corrected in April is wrong and nothing anywhere says so.**

**⚠ It is `check_extracts` one register over:** that compares an extract to its source; **nothing compares an AUTHORED artifact to the rules it was authored from.**

---

## ⚠ 3d · AN ITEM BLUEPRINT NAMES A BASE TYPE — `PT-1452`

**`BUILD 42` stopped here: `[equipment]` names `items/weapons/blaster-rifle`, `blueprints/items/` is in the layout, and **no document defines what an item blueprint contains.** Third time a folder has existed with no format behind it.

**⚠ And it refused the shortcut for three right reasons** — resolving a path by its last segment would make `items/weapons/` decorative and `PACKAGE-NAMING-01`'s *identity and location are the same thing* **false**; the shapes differ; and **`values` is an untyped positional array whose meaning lives only in a prose column order.**

### The two halves already exist and nobody joined them

| | | |
|---|---|---|
| **`EQUIPMENT-01`** | **base weapon TYPES** — 11 melee, 11 ranged, 3 lightsabers | **carries the dice** |
| **`ITEMS-01..09`** | **1,425 specific items**, converted by seven rulings | tier, cost, properties |

**⚠ That is `baseitems.2da` and `.uti` — the structure both source games use, sitting in our corpus with the join never stated.**

### The ruling

> **`[equipment]` names a PATH to an item blueprint. Always. There is no second form.**
>
> **An item blueprint names a BASE TYPE from the rules, and the base type carries the dice.**

**⚠ One form, because two would be ambiguous** — a path resolving to *either* a blueprint or a base record puts the reader in the business of guessing which. **And it matches the source: a `.utc` references a `.uti`, always. There is no creature carrying a raw baseitem.**

**⚠ AND THE POSITIONAL ARRAY IS A DEFECT IN THE EXTRACTION, NOT AN INTERFACE.** `equipment.json` stores `values` positionally because that is how the table reads; **it must be re-extracted with NAMED fields per section.** Nothing should ever infer a schema from a prose column order — that is `TRACE-83`'s position-as-identity, in our own data.

---

## ⚠ 4·0a `[entry]` is a PACKAGE property, and Loom must ask — `PT-1380`

**Step 6 stopped here: the test bed has no `[entry]`, so `New Game` has nowhere to begin.** `Loom` made that package and **never asked the question.**

**⚠ A package can therefore be made complete-looking in Loom and be unplayable, and Loom will not say so.**

### Where the question goes

**Not `New Package` — no areas exist yet when it runs.** Not `New Area` — **`[entry]` is a property of the package, not of any area.**

**⚠ It belongs in a PACKAGE PROPERTIES dialog**, which `PT-1376` already established as the home for manifest-level settings and which **Aurora had as Module Properties** (`STUDY 16` found the hak list living there with Move Up / Move Down).

**A second route is worth having:** an area in the tree offering **"set as entry"**, since that is where an author is when the thought occurs.

### ⚠ And `validate` must refuse it

> **⚠⚠ `validate` SAYS NOTHING ABOUT A BLUEPRINT REFERENCE, AND THE SILENCE IS STRUCTURAL — `PT-1494`.**
>
> **`TEST 014` counted `PackageProblem`'s nine members and NOT ONE is about a blueprint's contents.** So an unresolvable `from` and a `weapon_r_1` naming an item in a package with no items **both pass**, and `verify` reports *"No problems found"* **about a room you can walk through.**
>
> **⚠ THE SHAPE IS NAMED AND IT IS THE ONE THAT MATTERS: Loom refused an unresolvable check and wrote an unresolvable item path THE SAME AFTERNOON.** The refusal was in the dialogue editor because that editor happens to check; **nothing checks a blueprint reference anywhere.**
>
> **⚠ RULED: a reference that names a file which is not there is a `PackageProblem`.** Every `from`, every `conversation`, every `doctrine`, every equipment path. **`PT-1379` already governs this one file type over** — the area loader refuses a dangling connection and says *did you mean* — and **the same rule stops at the blueprint boundary for no reason anyone chose.**
>
> **⚠ And it is not enough for the checker alone.** `Lens/board.dart` **draws `area.contents` with no reference to whether anything resolved** — *there is no bad `from` the board will not render.* **A thing drawn by one program and unknown to the other, in the same frame,** is the defect `TEST 014` walked through twice.

**`ENGINE-INTERFACE-01` has `validate(path) → report`, and the agent already built `validateConnections`. This is the same shape.**

> **A package that declares areas must declare an entry. A package with no areas need not.**

**⚠ That second half matters — a rules-only or asset-only package is legitimate and has nowhere to begin by design.** `base-rules` is exactly that. **So the rule is conditional rather than absolute.**

### ⚠ And the app was right to refuse rather than guess

**`New Game` did not fall back to the first area in `[order]`.** The agent's reasoning, which is `§2·0`'s rule one level up: **guessing would make an absence into a default — and it would hide a Builder gap behind an app convenience.**

---

## ⚠ 4·0 A package declares which FORMAT it was written against — `PT-1366`

**The agent found this under a migration question and it is the more important half.** `§4` gives the **package** a version — *its own claim about itself* — and **nothing records which version of the FORMAT a file was written against.**

**⚠ `SAVE-LOAD-01 §2` already does exactly this for saves** — a format version and a rules version in the header, **precisely so a change does not orphan old files.** Packages had no equivalent.

> **Without it, every future format change is the same conversation with no way to tell an OLD file from a BROKEN one.**

**That sentence is the whole argument.** A package missing `[tiles]` might be **written before the rule existed** or **corrupt**, and the loader cannot distinguish them. **With a format number it can: an older format is migratable, an unreadable current one is an error.**

**⚠ And a format from the FUTURE is refused rather than read optimistically** — which is what the agent already built for saves at `PT-1354`, and the same rule applies here.

---

## ⚠ 3b · `tilesets/` — need G closed, `PT-1363`

**`AREA-FORMAT-01 §2a` calls a tileset *"a package resource, not a global index"* and the layout had no folder for one.** The agent guessed `tilesets/`, marked the guess in source, and **declined to extend the format itself.** The guess was right.

**⚠ A tileset holds ART and PREFABS. It holds no rules.** `PT-1361`: **types are ours and fixed; art and prefabs are anyone's and unlimited.** So `tilesets/` is **the one place in a package a stranger's contribution can land without being read** — which is what makes `PT-1334`'s exchange tractable.

**It sits beside `rules/` deliberately**, and the contrast is the point: `rules/` is package-local *rules*, and **a tileset is precisely the thing that must never contain one.**

---

## 4a · ⚠ Sharing — three format decisions, `PT-1336`

**`PT-1334` queued a community exchange and named five unsolved problems. Three are FORMAT questions and are settled here. Two are PRODUCT questions and are not — see `§8`.**

### 1 · A dependency must be identifiable without its author

**`[requires].packages` names an `id` and a version range. That is enough to LOAD and not enough to FIND.** If a package disappears from an exchange, **a holder of the dependent package has a name and nothing else.**

```toml
[[requires.packages]]
id       = "base-rules"
version  = ">=2.0"
digest   = "sha256:…"      # ⚠ what was actually depended on
```

**⚠ The digest is what makes a dependency verifiable rather than merely named.** Two packages claiming `base-rules 2.1` may differ; **a digest says which one this package was built against.** And a copy found anywhere — a friend, an archive, a backup — **can be checked rather than trusted.**

**A missing dependency still fails loudly** (`§6`). **But it fails with something a person can search for.**

### 2 · A version is the package's own claim, and the digest is the fact

**Ecosystem versioning does not need a registry to be coherent.** `version` is what an author says; **`digest` is what the bytes are.** Resolution prefers the digest and falls back to the range.

**⚠ That means an exchange is a convenience, not an authority.** Packages remain shareable by any means — **a folder on a drive works** — which matters for a format that outlives whatever platform hosts it.

### 3 · Video is NOT part of the package for transport

**`PT-1308` put video *beside* the package, excluded from versioning. That decision does the work here too.**

**A shared package is the folder without `movies/`** — a few hundred kilobytes rather than a few hundred megabytes. **The manifest still declares each slot**, so a recipient knows exactly what is missing and what it was called.

**⚠ And a package with unfilled video slots must still open.** `§6` fails loudly on a missing *declared dependency*; **a missing movie is a missing asset, and the campaign runs without it.** Otherwise sharing anything with a cutscene requires shipping the cutscene.

---

## 5 · ⚠ The Builder writes more than the app reads

**`TRACE-89`'s thesis, and the reason this is a format rule rather than a Builder feature:**

> **Aurora's important property is not any feature. It is that the tool and the game read the same file, and that file carries everything the tool needs to reconstruct the author's intent — source, comments, palettes, config — none of which the engine reads.**

**The evidence is decisive. 26,317 script sources against 26,180 compiled across 30 NWN modules — 93% of modules carry their own source.** Every KOTOR module script is **compiled-only**, while BioWare kept source for their own engine scripts. **Applied precisely where reopening matters most.**

**That is why twenty years of KOTOR modding has been decompilation and NWN's has been editing.**

**So:**

- **Source ships.** Cost is ≈2× on the script layer — *a rounding error against an 866 MB models archive.*
- **Comments ship.** The app ignores them.
- **Editor state ships** — grouping, collapse, layout. **⚠ Per `PT-1284`, grouping is a view and means nothing to the model.**

**⚠ The rule: a Builder that writes what our app reads is only safe if the artifact also carries what the Builder needs to read it back.**

---

## 6 · Loading

```
1  read the manifest
2  resolve [requires] in order — fail loudly on a missing package
3  layer content, later packages winning
4  validate
5  open
```

**⚠ Failure is loud at every step.** `F35`: **KOTOR's engine wrote an appearance index past the end of the table it indexes and nothing rejected the write.** A silent bad reference is worse than a refusal to load.

**And a file that disagrees with its own location says so** — `PACKAGE-NAMING-01 §3` puts the path inside the file for exactly this.

---

## 7 · What a package does NOT contain

**⚠ No runtime state.** `TRACE-85` found KOTOR's save carrying **a replacement copy of every visited module** — 112 fields inline per creature. **Ours does not, because `PLAY-STATE-01` makes state a projection of an event log.** A package is authored content; a save is a log. **They never live in the same folder.**

**No compiled-only content.** `§5`.

**No global anything.** `TRACE-86` found the journal is **one game-wide file**; `TRACE-82` found the rules layer is **one global namespace**. **Both are the same mistake and both are excluded by `§3`.**

**⚠ Video is the ONE exception to "a package is a folder you can diff"** — declared inside, stored beside, excluded from versioning. `§3a`.

**No per-file export metadata.** `PT-1282 §7` — the study found **four dead capabilities**, and a field for a declined exporter is how a fifth is born.

---

## 8 · Open

- **The file format inside a package** — TOML for the manifest is shown; whether content files are TOML, JSON or something else is undecided.
- **Asset handling** — `assets/` is named, not specified. Waits on the presentation-layer decision.
- **⚠ Versioning and compatibility.** `[requires].engine` is shown; what a version *means*, and what breaks compatibility, is unruled. **`§4a` settles identification; it does not settle what a version NUMBER means.**
- **⚠ Discovery and search** — needs content to exist before it can be designed. **A product question, deferred at `PT-1336`.**
- **⚠ Trust and moderation** — same. **Policy needs a platform; there is no platform.**
- **Whether a package can be partially loaded**, and what a broken dependency does to content that does not use it.
- **⚠ How a chain is read** — `[continues]` names it; `QUEST-MODEL-01 §5` says conclusions cross. **The mechanism is not specified.**
