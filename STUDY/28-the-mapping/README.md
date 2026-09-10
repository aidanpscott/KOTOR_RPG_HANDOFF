# 28 · The mapping — what ours needs that Aurora never had

**From `Tester`.** Closes the last three gaps from `STUDY/27`'s own not-looked-at
list, then does the thing no study has done: **map our formats onto Aurora's
surfaces and name what has no surface at all.**

`STUDY/26` looked at the toolset. `STUDY/27` used it. **This one points it at
us.** Part A is the last Aurora pass; **Part B is the mapping and is the point.**

**⚠ NOTHING WAS SAVED.** Verified by file count and mtime before and after:
the NWN install held **8298 files** at the start and **8298** at the end, newest
mtime `2026-02-05`, unchanged. `Build Module` and `Test Module` were
**deliberately not run** — both write. The process was killed, not closed.

---

# PART A — the last three gaps

## A1 · Tile painting — the one thing we both have

`09`–`18`. Ran on a fresh **Forest** exterior area, 8×8, made from nothing.

### ⚠ The units, measured rather than assumed

Scanning the status bar across one row (`12`):

| screen x | `Mouse x` | `Grid col` | `Tile` |
|---|---|---|---|
| 300 | 11 | 1 | `ttf01_o01_01` |
| 460 | 22 | 2 | `ttf01_g05_03` |
| 620 | 32 | 3 | `ttf01_o01_01` |
| 860 | 47 | 4 | `ttf01_o01_01` |
| 940 | 52 | 5 | `ttf01_p04_01` |

> **⚠ One tile is exactly 10 area units.** An 8×8 "Medium" area is **80×80
> metres**. The creature `STUDY/27` found at X 38.31 / Y 43.58 sits inside col 4,
> row 5.

**So the author sizes in TILES and places in METRES**, and the status bar showing
both at once is the entire mechanism by which those two units are reconciled.
**We have one unit. This is the divergence the owner flagged, stated exactly.**

### ⚠⚠ There are THREE brush kinds, not one

`10`, `11`, `15`.

| root | what it paints |
|---|---|
| **Terrain** | Bridge · Cliff · **Eraser** · Forest · Pit · Road · Stream · Wall |
| **Features** | single-tile set pieces — Big Tree, Camp, Graveyard, Portal, Ruin, Tower, Wall Gate, Webbed Forest |
| **Groups** | **multi-tile stamps** — Camp 1 **2x2**, Exit 1 **2x3**, Graveyard **1x2**, **Grove 3x3**, Lodge 2x2, Meeting Area 1x2, Ruin 1 2x2, Shack 1 2x2, Temple **3x2** |

**⚠ Every Group carries its footprint in its name**, because a multi-tile stamp
needs somewhere to say how big it is. **And the brush cursor previews that
footprint on hover** (`16`) — a green outline over exactly the 3×3 block that
will be replaced, before you commit. One click then lands a **designed
composition** (`17`): the grove arrives with stone paving, heavier canopy and a
log-ringed clearing — not nine repeated tiles.

**⚠ `Eraser` is a member of the Terrain list**, alphabetically between Cliff and
Forest. **Erasing is a brush you pick, not a mode you enter or a key you hold.**
One interaction for the whole tool.

**And erasing writes the tileset's default tile, not emptiness** (`18`):
`ttf01_g01_02` → `ttf01_p02_01`. **There is no "no tile" state** — which is
exactly our `[tiles] default` and `PT-1365`'s *"an area IS a grid"*.

### ⚠⚠ The finding that matters most: the STROKE is the unit of intent

Two adjacent single clicks with `Road` produced **two disconnected parallel
stubs** (`13`) — `g05_03` and `g05_01`, and painting the neighbour did **not**
re-transition the first tile.

**One drag across the same ground produced a continuous, curving, connected
road** (`14`), with correct corner variants.

> **The same brush behaves differently by gesture. Aurora's drag traces a PATH.
> `PT-1367`'s drag fills a BOX. Same gesture, two different meanings.**

**⚠ And that is a decision to make deliberately, not inherit.** Ours is a box
because `PT-1367` reasoned *"a 3×4 of floor is one gesture"* — filling a room.
Theirs is a path because a road is a line. **Both are right for what they paint,
and a Builder could offer both** — box-fill for rooms, path-trace for corridors —
**but only if it says which one a drag is doing.**

### ⚠ And the deeper difference: the brush paints an INTENT; the toolset resolves the GEOMETRY

Aurora's brush says *"make this Road"* and the toolset chooses a specific tile
model that transitions to its neighbours. **Ours writes a `TileType` character
into a text map and that character IS the answer.**

**`PT-1371` already saw this and split it three ways — TYPE / VARIETY /
VARIANT — and our split is better for our purpose**, because
`AREA-FORMAT-01 §2·0e` puts the *engine* in charge of VARIANT (seeded by
position, never re-rolled) and the *author* in charge of VARIETY. Aurora
conflates them: the toolset picks the model, the author cannot, and
**re-painting a neighbour does not revisit the choice** — which is why two
clicks leave a broken road and the author must know to drag.

> **We already do better here and should not give it up: a square's type is one
> character in a file, and what it looks like is a separate, seeded decision.**

### ⚠ What the status bar gives an author that ours does not

`Mouse(x:24 y:42) Grid(row:4 col:2) Tile(ttf01_g05_03)` — **and a fourth field
I missed in `STUDY/27`**: the right-hand pane names the current **mode**
(`Select` → `Paint`), and the left names the current **action**
(`Select Terrain`).

**Four continuous facts: where the pointer is, which cell that is, what is in
that cell, and what clicking will do.** For us the transferable ones are the
middle two — **the grid cell and the tile type under the cursor** — because
`PT-1439` measured that eleven pixels is the difference between a working panel
and a click landing on the wrong row. **A readout that names the square makes an
off-by-one visible instead of silent.**

**Scoped negative:** the **red lines** overlaid on the viewer lie on a *subset*
of tile boundaries (the fine grey lines are the actual tile grid). **I did not
determine what selects them** and am not guessing.

---

## A2 · `File > New Module` and the Module Wizard

`02`–`08`. TRACE-106 read *"a corridor with two blanks"* out of the binary.
**Confirmed, and the shape of the other half is the finding.**

**The Welcome dialog** (`02`) offers **three entry states** — *Create a new
Module* / *Open an existing Module* (preselected, last module highlighted) /
*Start normally*. That preselection is why `STUDY/26`'s OK reopened the last
module instead of making a new one. *(Minor: the module list under the second
radio stays fully enabled and highlighted when the first radio is chosen —
everything else in Aurora greys aggressively; this does not.)*

**The wizard is four steps, and only two take input:**

| step | asks |
|---|---|
| 1 · Welcome | **nothing** — "This wizard will take you step by step through the creation of a basic module…" |
| 2 · Module Name | **one field**, prefilled `module000` |
| 3 · Create Areas | **gated** — `Next` *and* `Finish` greyed until one area exists |
| 4 · Finish | **nothing** — "Congratulations! You now have a playable module…" |

> **⚠ Half of Aurora's module-creation corridor is communication, not input.**

**Three things worth taking:**

**⚠ The wizard calls a wizard.** Step 3 does not reimplement area creation — it
launches the **Area Wizard** (`05`), which runs modally, and on return the parent
updates its list and lifts its gate (`06`). **Composition, not duplication** —
`STUDY/27`'s rule 1 one level up.

**⚠ The prose states the rule the gate enforces**, and then removes the pressure:
*"Every module needs at least one area… You can always create more areas later by
accessing the wizard in the main menu."* **Say the constraint, enforce it, and
say it is not your only chance.**

**⚠⚠ The wizard ends by teaching the next thing** (`07`). The final step is an
**annotated screenshot of the real palette UI** with arrows and a callout:
*"The terrain and game object palettes contain all kinds of interesting things
like creatures and items, which you can place in your area."* Not "done" —
**"here is what you now have, and here is where to look next."** Our New Package
has nothing like it.

**And `Area Size` (`08`) binds three controls together**: presets
(Tiny/Small/**Medium**/Large), Height/Width spinners, and a live green preview
that tracks the numbers. **Medium resolves to 8×8, so you never have to know what
"Medium" means.** Directly applicable to our `size = [w, h]`.

**Two guards, both three-way** (`01`, `23`): the crash-recovery prompt
(*"The toolset did not close properly… Pressing 'No' will destroy the backup"* —
Yes/No/**Cancel**) and the save guard (*"Would you like to save your changes to
the module?"* — Yes/No/**Cancel**). **The third option aborts the action
entirely rather than forcing save-or-discard.**

---

## A3 · The Build menu — our validate-and-package step

`19`–`21`. **Four verbs where we have one.**

| verb | what it is |
|---|---|
| **Verify Area** | validate **one** area |
| **Build Module** | the package step *(not run — it writes)* |
| **Test Module** (F9) | **launch the game on this module** *(not run — it writes)* |
| **Area Statistics** | a **cost report** |

**⚠ `Verify Area` reports into a LOG, not a dialog** (`20`). The wide empty band
at the bottom of the main window — which `STUDY/27` noted and could not
explain — **is the build output pane.** It filled with:

```
Loading Tiles
Loading Tiles
Area verified successfully.
```

**Success is a plain sentence that does not interrupt.** And validation is
scoped to **one area**, not the whole module — you can check the thing you are
working on without waiting for everything.

**⚠ `Test Module` has no analogue in our tooling at all.** Loom and the play
client are separate programs and the author switches by hand. **F9 is the
shortest gap between authoring and playing in the entire toolset.**

**⚠ `Area Statistics` is a memory budget** (`21`): `Model 1241 kB`,
`Texture 5808 kB`. It tells the author what the area will *cost*. That exists
because of a 2002 VRAM constraint we do not share — **`PT-1496`'s limit applies
and this one does not transfer** — but the *germ* does: **the Builder telling you
the cost of what you just made.**

---

# PART B — THE MAPPING

Three columns. **The third is the one nothing has produced.**

## B0 · The summary table

| our format | THEIRS → OURS | OURS ✗ — no Aurora answer |
|---|---|---|
| `PACKAGE-FORMAT-01` | module ↔ package; `Build Module` ↔ validate-and-package | **`[requires]` / `[continues]` / `[order]` / `[creation]`** |
| `AREA-FORMAT-01` | tile painting; Groups ↔ prefabs; area properties | **`difficult` / `hazard` as costed types; `tag_seq`; `[[arrivals]]`** |
| `AUTHORED-CHARACTER-01` | creature blueprint; template/instance; `override` ↔ HP escape hatch | **species + subrace + chassis spread; `[protection]`'s three booleans; Force** |
| `DIALOGUE-FORMAT-01` | conversation editor; `replies`/`then` ↔ their link lists | **the closed gate vocabulary; `attitude`; `alignment`; `pinned`** |
| `DOCTRINE-FORMAT-01` | *(nothing — theirs is scripts)* | **⚠ the whole file. `[[never]]` vs `[[prefer]]`, `want_range`, `[break_off]`** |
| `EVENT-KINDS-01` | *(nothing — theirs is savegame state)* | **⚠ the whole ledger. Every kind, and the three lifetimes** |

---

## B1 · `PACKAGE-FORMAT-01`

### THEIRS → OURS

| Aurora | ours | note |
|---|---|---|
| a **module** (`.mod`) | a **package** (a folder) | **⚠ theirs is an archive, ours is a folder** — `§2`: *"`git diff` works. A modder can look."* |
| Module Wizard step 2, `module000` | `[package] name` | prefilled with a working default; ours should be too |
| `File > Export…` / per-blueprint `Export` | — | see OURS ✗ below |
| `Build > Build Module` | validate-and-package | **theirs has four verbs; see A3** |
| `Build > Verify Area` | `PackageProblem` per area | **⚠ theirs validates ONE area on demand** |
| the Welcome dialog's module list | the **library** | ours is a first-class tab (`PT-1375`); theirs is a startup listbox |

### THEIRS ✗

- **`Test Module` (F9)** wants an answer but not this one — theirs launches a
  separate game executable against a built file. Ours would be *"open this
  package in the play client"*, and that is a different mechanism.
- **`Area Statistics`' VRAM budget** — a 2002 constraint.
- **The 16-character ResRef limit** and its silent truncation
  (`STUDY/27`: `Area Transition 001` → `areatransitio001`).
  `PACKAGE-NAMING-01` opens by naming exactly this: *"a resref IS a filename
  inside an archive, and it was capped at 16… **We have no such constraint.**"*
- **Localised-string `...` buttons** on every name field.

### ⚠ OURS ✗ — what Aurora has no answer for

- **⚠⚠ `[requires]`.** Aurora has **haks**, and a hak is a content bundle with
  no version constraint, no ordering semantics, and no digest. We have
  `packages = [{ id, version = ">=2.0", digest }]`, **ordered, and the order IS
  the precedence** (`§4·1`). *The nearest Aurora surface is the `Select
  Resource` picker's **provenance filter** — All / Module Only / Hak Pak Only
  (`STUDY/27`) — which is a **read** of where content came from, never a
  **declaration** of what is required.*
  → **Shape it wants:** a dependency editor with a version constraint per row,
  reorderable, showing the resolved digest. Nothing in Aurora to copy.
- **⚠ `[continues] chain`** — cross-campaign carry. Aurora has no concept of one
  module continuing another's state.
- **`[order] areas`** — `§4·1` makes area order explicit *because* nothing else
  carries a number. Aurora's areas are an unordered set.
- **⚠ `[creation] species_closed` / `classes_closed`** (`PT-1412`) — **a package
  closing a character-creation choice.** Aurora's module cannot restrict
  chargen; NWN did it in the game, not the toolset.
- **`[movies]`** with a queue and mid-scene beats (`PT-1308`).
- **`rules/`** — `PT-1376` already recorded the honest finding here:
  *"NOT ONE FORM IN 105 MENTIONS 2DA, and `TRACE-82` found NO MODULE-LOCAL RULES
  TABLE IN EITHER GAME. **Aurora's silence is not a judgement that rules need no
  surface — it is that Aurora had no such thing to give one to.**"*
  → **No precedent in either direction. This is ours to design.**

---

## B2 · `AREA-FORMAT-01`

### THEIRS → OURS

| Aurora | ours |
|---|---|
| tileset picker in the Area Wizard | `[area] tileset` (`PT-1360`) |
| Area Size — presets + spinners + live preview | `[area] size = [w, h]` |
| **Terrain** brush | painting a `TileType` |
| **`Eraser` as a terrain entry** | **⚠ take this** — one interaction, no mode |
| **Groups** (multi-tile stamps) | **prefabs** (`PT-1367`) — *"a prefab is a saved selection"* |
| Features (single-tile set pieces) | a 1×1 prefab; we need no separate kind |
| Area Properties → Basic/Visual/Audio/Events/Advanced | area properties |
| **`Tileset`, `Length`, `Width` disabled after creation** | **⚠ our identical limit is not a gap we invented** |
| `Variables …` per area | — see OURS ✗ |
| status bar `Grid(row/col)` + `Tile(...)` | **⚠ take this** |

**⚠ Our prefabs are strictly better and the reason is already written.**
Aurora's Groups are **tileset-supplied and fixed** — thirteen of them, authored
by BioWare. `PT-1367` makes ours **a saved selection**: *"Paint a room, drop art
on it, select it, save it… premade rooms for people who do not want to paint one,
made by people who did."* **Theirs ship with the tileset; ours are made by
authors.** And ours **paste** rather than overlay, so there is no second source
of truth.

### THEIRS ✗

- **⚠⚠ Continuous metre positions.** Aurora's grid is tiles-only and every
  instance sits at a fractional metre position. **`PT-1103` ruled us a 2D grid,
  a digital tabletop mat**, and `PT-1319` removed the geometry that would need
  metres. **One unit, deliberately. Do not reopen this.**
- **The toolset choosing the tile model.** See A1 — `PT-1371`'s TYPE / VARIETY /
  VARIANT split is the better answer and we keep it.
- **Environment Schemes**, ambient day/night audio, weather, terrain-type
  radio triples (Interior/Exterior, Natural/Artificial, Underground/Above) —
  all 3D-world properties for a board that has none.
- **`Check Modifier — Listen` / `Spot`**, `No Rest`, `Player vs. Player`,
  `Loading Screen` — engine features we do not have.
- **The 24-checkbox AM/PM schedule grid** on a Sound — no clock.

### ⚠ OURS ✗

- **⚠⚠ `difficult` and `hazard` as COSTED tile types.** `STUDY 19` already
  established the negative and this pass confirms the shape of it: Aurora's
  terrain vocabulary is **materials and structures** — Cliff, Road, Stream,
  Wall — and `surfacemat.2da`'s `walk`/`walkcheck` are **booleans in both K1 and
  NWN with no cost column**. **Neither source engine ever modelled movement
  cost, and neither toolset has a surface for it.**
  → **Shape it wants:** the palette entry must show the cost, because
  `PT-1513`'s whole argument is that *"an author paints it expecting it to
  bite."* And per that ruling **the multiplier lives on the CREATURE, not the
  tile** — so the Builder needs a creature-side surface for exemptions that
  Aurora has no row for either.
- **⚠ `hazard` is offered and unruled.** No Aurora analogue to borrow a meaning
  from. `§2·0a` leaves it open on purpose; the Builder must not present it as
  finished.
- **⚠ `tag_seq`** — one monotonic integer so a retired tag is never reused
  (`PT-1377`). Aurora reuses freely: its Tag is a **derived, editable, non-unique
  string** (`Hard 001` → `Hard001`), and `STUDY/27` found **six stock blueprints
  all named `Blackmarket Store`**. **`PT-1331`'s never-reassigned rule has no
  Aurora counterpart at all.**
- **⚠ `[[arrivals]]` — a named landing point the area DECLARES.**
  `AREA-FORMAT-01 §4·0` is explicit that this is *"neither of Aurora's two
  waypoints"*. Aurora's waypoint is an instance at a metre position with a tag;
  ours is a **declared name a connection can be validated against**, and
  `PT-1378`'s argument is that *"you cannot fail loudly against a rule that says
  any coordinate is fine."*
  → **Shape it wants:** arrivals are a **list on the area**, edited as a list,
  not objects scattered on the board. Aurora's `Create Waypoint` context verb is
  the wrong shape for us.
- **The text map itself.** `PT-1345` makes the area hand-writable and
  diff-readable. Aurora's area is binary. **The Builder must round-trip the map
  byte-faithfully** — a requirement no Aurora surface has ever had.

---

## B3 · `AUTHORED-CHARACTER-01`

### THEIRS → OURS

| Aurora | ours |
|---|---|
| Creature blueprint + palette | `blueprints/characters/*.toml` |
| **template → instance, `Update Instances`** | template/instance (`§4`) — **⚠ and their explicit button is the right answer** |
| `Add To Palette` on a placed instance | **⚠ we have no instance→blueprint direction at all** |
| Levelup Wizard (class + level, 1–8 classes) | `class` + `level`; `MULTICLASS-01` |
| creature inventory / equipment | `[equipment]`'s locked lattice (`PT-1252`) |
| faction dropdown | `faction` |
| `Edit Copy` | — worth taking |
| Portrait picker | portraits (`PT-1137` — a token IS the portrait) |

**⚠ `override` ↔ nothing exact.** `§3` takes the HP escape hatch from
`TRACE-84`. Aurora's equivalent is that **every stat is directly editable**, so
it needs no escape hatch — **and that is precisely what we rejected.** Ours is
*"store the choice, derive the consequence"* with **one visible, explicit
`override = 0`**. Keep it.

### THEIRS ✗

- Appearance Type, Portrait model, Cursor, body-part sliders — 3D.
- **Hardness / saving throws on furniture** — `STUDY/27` found a placeable is a
  combatant-shaped object. Ours is inert.
- Per-creature **script hooks** (OnSpawn, OnDeath, OnPerception…) — see B5.

### ⚠ OURS ✗

- **⚠⚠ SPECIES, SUBRACE AND CHASSIS.** `PT-1490` found *"a placement has no
  KIND"* and that a blueprint **names no species**. Aurora's creature sheet has
  **a race dropdown and nothing else** — no subrace records, no ability
  adjustments carried by the record, no chassis spread. Ours has
  `PACKAGE-FORMAT-01 §3c`'s **subrace RECORDS with the picker filtering**
  (`PT-1391`), and **speed lives on the species** (`PT-1424`).
  → **Shape it wants:** a species picker that is **a record lookup, not an
  enum**, showing the adjustments it will apply, and a blueprint field that
  stores the *choice* while the sheet shows the *derived* result. **`STUDY/27`
  found the Encounter shipping "Hard 001" with Difficulty "Easy" — a derived
  display that disagreed with its own label is exactly the failure mode to avoid
  here.** *(And `PT-1533` already caught our own version of it: the species
  adjustment not reaching the fight, proved as `Strength 2` where the sheet said
  STR 18.)*
- **⚠ `[protection]`'s three booleans** — `plot`, `min_1_hp`, `raiseable`.
  Taken from KOTOR, **not from NWN**, and Aurora's creature sheet has **`Plot`
  (a single checkbox) and no other two.** We have three orthogonal states where
  Aurora has one.
- **⚠ Force.** No powers, no pool, no alignment-gated access, no
  `FORCE-AWAKENING-01`. Aurora has spell lists; **a spell list is not a pool with
  a cost model.**
- **⚠ `[attachments] doctrine` as a PATH, and `reaction` INLINE** (`PT-1441`).
  See B5.
- **The handle/path/tag/role split** (`PACKAGE-NAMING-01 §1`). Aurora has
  ResRef/Tag/Name — **three, and one of them is capped at 16 characters and
  silently truncated.** Ours has **four**, and the fourth — **`role`, refillable,
  where a `tag` is not** (`PT-1331`) — has no Aurora counterpart whatsoever.

---

## B4 · `DIALOGUE-FORMAT-01`

### THEIRS → OURS

| Aurora | ours |
|---|---|
| Conversation editor (a real editor, owns its lifecycle) | the Conversation tab (`PT-1375`, `PT-1376`) |
| NPC line / PC line alternation | `[[npc]]` / `[[player]]` |
| link lists | `replies` (**SHOW ALL**) and `then` (**PICK ONE**) |
| `Edit Conversation` from a placed creature | **⚠ take this — the tree is not the only entry point** (`PT-1376`) |
| speaker override | `by` (`§6`) |
| **`Store Setup Wizard`** | **⚠⚠ take this — see below** |

**⚠⚠ The Store Setup Wizard is the single best idea to steal for our
conversation authoring.** `STUDY/27` §8: it asks **"What does the shopkeeper say
when the conversation begins?"** and prefills **"Welcome to my shop. Would you
like to see my wares?"**, then **generates a working conversation and the script
that opens the store.** It asks in the domain's language and hands back working
content.

> **Our conversation editor asks for nodes, replies and links — the schema.
> Aurora's asks the question the author is actually thinking about.**

### THEIRS ✗

- **The script that the Store Wizard also generates.** We have no scripts; the
  effect vocabulary is `§5`'s declared event kinds.
- Aurora's arbitrary conditional/action scripts on every link — the whole reason
  `§4` exists is to refuse this.

### ⚠ OURS ✗

- **⚠⚠ THE CLOSED GATE VOCABULARY.** This is the sharpest one in the section.
  Aurora's gate is **a script name in a text field** — arbitrary code, checkable
  by nothing. Ours is **data with a fixed vocabulary**: `skill`+`dc`,
  `skill`+`opposed`, `flag`, `quest`+`status`, `attitude`, `payment`, `party`,
  `species`, `background`, `alignment`, `all_of`/`any_of`, `not`.
  **`§4`'s guarantee is that an unknown key is a load failure, not an extension
  point** — and `§4`'s own reasoning is the same as `DOCTRINE-FORMAT-01 §2`'s:
  **a rule you can only state correctly cannot drift.**
  → **Shape it wants:** a **gate builder with a closed dropdown**, not a text
  field. And **`§4c`'s colour coding has no Aurora analogue at all** — amber for
  *it rolls*, teal for *who you are*, invisible for *not a check*,
  **`[Bribe · 50 credits]` as the one surviving number.** Aurora shows the author
  a script name and the player nothing.
  *(And `PT-1326`'s never-rolling `[Persuade]` gate — 12/12 passes at 55% — is
  the reason this matters: a gate that displays as a roll and does not roll is a
  lie to the player. Aurora cannot even detect that class of fault.)*
- **⚠ `attitude`** — `RULES-02 §5`'s five bands. No Aurora surface.
- **⚠ `alignment`** — derived per `ALIGNMENT-01-v2`. NWN had alignment; **Aurora's
  conversation editor gates on it only through a script.**
- **⚠ `pinned`** (`§4b`) — *never rephrase this line*. This presumes a rephrasing
  layer that Aurora has no concept of.
- **⚠ `effect` on NODES and never on links** (`§5`). Aurora puts actions on
  links. **Ours cannot, structurally — the link table has no `effect` key** —
  because a node's effect fires *when the line plays*, not while a list is being
  built. **That is a correctness property Aurora does not have.**
- **`note`** — an author comment read by nobody at runtime. Aurora's `Comments`
  tab is the same idea and we should keep ours per-node rather than per-object.

---

## B5 · `DOCTRINE-FORMAT-01` — ⚠⚠ the whole file is column three

> **Aurora's AI is scripts. Ours is doctrines. There is no mapping.**

Aurora attaches `OnPerception`, `OnAttacked`, `OnDamaged`, `OnDeath`,
`OnHeartbeat` to a creature and each names a compiled `.nss` script. The stock
behaviour is a shipped script everyone reuses. **There is no declarative surface
anywhere in the toolset for "what does this creature want and who does it
attack".**

**So every field below has no Aurora answer, and the shapes are ours to design:**

| ours | why Aurora has nothing | shape it wants |
|---|---|---|
| `goal` | a script has no stated goal | **⚠ `§7` says it is inert** — either a vocabulary or a ruling that it is narration. **The Builder must not present an inert field as a live one** (`PT-1500`) |
| `want_range` `close`/`medium`/`long` | scripts move by code | a three-way radio **with a sentence each** — Aurora's own Sound wizard proves that shape |
| `[break_off] when` = `never`/`alone`/`below`+`fraction` | — | **`never` is a real answer, not an absence.** The default must read as a choice |
| **`[[never]]`** | — | **see below** |
| **`[[prefer]]`** ordered, `rule` = `nearest`/`weakest`/`any` | — | an **ordered list**, because the order IS the preference |
| `match` closed vocabulary — `role`, `handle`, `handle_starts`, `below` | — | closed dropdown, same as the dialogue gate |

### ⚠⚠ `[[never]]` and `[[prefer]]` are two arrays BY CONSTRUCTION

**`PT-1442`, and the reason is a rule Aurora never needed.**

`PT-1423`: **"never is not a preference that lost."** An exclusion applies
**before every preference**, so an excluded target is not chosen *even when it is
the only thing left* — and the decision then records `none:all-excluded`, which
**says which kind of nothing happened.**

> **`DOCTRINE-FORMAT-01 §2`: "A file with an exclusion written last in
> `[[prefer]]` is not expressible. There is no `never` value for `prefer.rule`
> and no `match` semantics that exclude. The distinction cannot be lost by an
> author, because the author has no way to write it wrongly."**

**⚠ This is the same principle as the dialogue gate's closed grammar, and it is
the thing we have that Aurora most conspicuously lacks: correctness by
construction.** A script can express "prefer X, and also never Y" only as
control flow, where the two are indistinguishable and the ordering is a bug
waiting to happen.

**⚠ AND IT IS A BUILDER REQUIREMENT, NOT JUST A FORMAT ONE.** The editor must
present them as **two separate lists that cannot be dragged into each other.**
*(`TEST 016` is the live warning: I filled `match`/`value`/`because` and pressed
`prefer nearest`, and the file carried none of them — because those five are
**add** buttons and `prefer match` and `never` consume the match. That was my
misuse, and a UI in which the misuse is possible is the thing to fix.)*

**Also with no Aurora answer:** `§5`'s **no randomness** rule
(*"given a log, the same fight must play the same way"* — the die is injected by
the caller and **there is no seed field and there must not be**), and
`DoctrineView` being **"a state and a declaration, never a world."**

---

## B6 · `EVENT-KINDS-01` — ⚠⚠ also entirely column three

> **Aurora has a savegame. We have a ledger.**

NWN stores **current state**. We store **what happened**, and
`PLAY-STATE-01` makes state a **projection of the log**. **There is no Aurora
surface for an event kind, because Aurora has no events** — it has variables
(`int`, `float`, `string`, per `STUDY/27`) and a save file.

**The nearest thing Aurora has is the per-object `Variables` editor**, and the
comparison is instructive:

| Aurora `Variables` | our ledger |
|---|---|
| three types: `int`, `float`, `string` | **~45 declared kinds** with payloads |
| no history — a variable holds its current value | **an append-only log**; state is derived |
| no lifetime — a variable lives as long as the save | **three lifetimes: `transient` · `session` · `campaign` · `permanent`** |
| scoped to one object | scoped by kind |

### ⚠ What has no Aurora answer, and what shape it wants

- **⚠⚠ The three lifetimes.** `transient` (until the encounter/duration ends),
  `session`, `campaign`, `permanent`. **This is the single most Aurora-less
  concept in our whole format set.** `quest.flag-set` is **permanent** because
  `PT-1284` ruled *flags are never unset*; `character.alignment-shifted` is
  permanent because `PT-1279` ruled *alignment history is not compactable*;
  `character.moved` and `area.entered`/`.left` were **promoted from `session` to
  `campaign` at `PT-1417`.**
  → **Shape it wants:** wherever the Builder lets an author name an event kind —
  a dialogue `effect`, a reaction's `on` — **the lifetime must be visible**,
  because "this is remembered forever" and "this is forgotten when the fight
  ends" are different promises to the player.
- **⚠ Author-writable vs engine-written kinds.** `DIALOGUE-FORMAT-01 §5`:
  *"`dialogue.node-reached` / `dialogue.choice-made` are written by the ENGINE,
  not by an author… an `effect` naming one of them is a load failure."*
  → **The effect picker must not offer them.** A closed dropdown that lists only
  the author-writable kinds. **Aurora's script field would happily accept
  anything.**
- **⚠ `note.written` — campaign, and unreadable.** `PT-1253`: Personal Notes are
  private; **the event records that a note exists, never its content.** There is
  no Aurora concept of an event that deliberately withholds its own payload.
- **⚠ `§3b`: what a kind CARRIES is mostly unwritten** (`PT-1516`). Only three
  kinds have a payload anything actually reads. **This is an open gap in our own
  format and the Builder will hit it the moment an author picks a kind that needs
  a field nobody has specified.** Named here so the rebuild finds it rather than
  discovering it.

---

# PART C — already decided. Do not quietly reopen

**These are ours, they were argued, and the rebuild inherits the conclusion.**

| ruling | decided | Aurora did |
|---|---|---|
| **`PT-1340`** | **The Builder is ONE WINDOW.** | 105 forms, 77 dialogs, many windows. **The ruling explicitly survived the script-editor test**: `TdlgScriptEditor` is 760×540 with a splitter — *"not an IDE, a text area over a compile-output pane. It fits in a tab."* |
| **`PT-1375`** | **FOUR TABS, BY KIND** — Packages · Area · Conversation · Script. Fixed, never growing; **which** area comes from the left tree. | one area viewer, switched via the tree. **Beamdog added area tabs twenty years later and shipped them OFF by default.** |
| **`PT-1376`** | A surface is an editor **only if the thing in it can be created, saved and closed independently** — 3 of Aurora's 105 forms qualify. | `TdlgTriggerEdit` has four splitters, six tabs and a status bar — **more furniture than the script editor** — and is a dialog with OK/Cancel. **⚠ Richness proves nothing.** |
| **`PACKAGE-NAMING-01`** | **THE PATH IS IDENTITY.** Two levels, lowercase, hyphens, no numbers except areas. | `blstrpstol01`, capped at 16 chars, **and six stock blueprints all called `Blackmarket Store`.** |
| **`PT-1331`** | A **tag** names one placed thing and is **never reassigned**; a **role** is refillable. | Tag is derived from Name, editable, and freely duplicated. |
| **`PT-1361`** | **A package invents NOTHING.** Tile TYPES are ours and fixed; tile ART and PREFABS are anyone's. | `Terrain` was **Standard-only** — Aurora refused custom terrain entirely. **⚠ Our departure is deliberate and safe *because* our entries carry no rules.** |
| **`PT-1103` / `PT-1319`** | **2D grid, a digital tabletop mat.** One unit. | tiles + continuous metres. **A2/A1 above is the measurement; it is not an invitation.** |
| **`PT-1367`** | Paint works on a **REGION** — drag a box. Prefabs are **saved selections** that **paste**. | drag traces a **path**; Groups ship with the tileset. **⚠ A real fork — see A1.** |
| **`PT-1366`** | **The drawn look is a CHOICE, not a fallback.** | fully textured tilesets. **Our flat board is a preference, not a missing file.** |
| **`PT-1345` / `PT-1370`** | The text map, and the five canonical glyphs `.` `#` `~` `:` `!`. | binary. |

---

# PART D — the rule out of my own finding

> ## ⚠⚠ A CATEGORY IS WHERE A THING LIVES. A PROPERTY IS WHAT A THING IS.
> ## A category must never be mechanical.

**The evidence, from `STUDY/27` §6:**

- For a **Trigger**, the palette category **set `Trigger Type` and locked it
  immutable**. The category was mechanical.
- For an **Encounter**, the palette category was **decorative**. I filed a
  blueprint under **Hard**; Aurora named it **`Hard 001`**, set its `Category`
  field to **`Hard`** — and set its **`Difficulty` to `Easy`**.

**Three things on one screen said Hard and the mechanical field said Easy, and
nothing in the UI distinguished the binding case from the decorative one.**

### What this means for the rebuild, concretely

1. **A palette folder is a view.** It may be renamed, moved, or deleted without
   changing what any blueprint *is*. `PACKAGE-NAMING-01` already says this in
   its own terms — *"the path says what a thing IS. Not what it is worth"*, and
   **`slot` and `weight` are fields precisely because they get tuned.**
2. **Anything mechanical is a field on the object**, shown on the object's own
   sheet, editable there.
3. **⚠ Never derive a name from a category and then let the two drift.** If the
   Builder prefills a name from a folder, that name is a **starting value the
   author owns**, and the folder must never be re-read afterwards.
4. **⚠ And if a field IS immutable after creation, say so where it is shown.**
   Aurora greys `Trigger Type`, `ResRef`, `Tileset`, `Length` and `Width` with
   **no reason given anywhere** — and `STUDY/27` found four more greyed controls
   whose enabling control was on a **different tab**. Our `base-rules` hub
   already says *why* a row is disabled. **Keep doing that.**

---

## Appendix · What was NOT looked at

- **`Build Module` and `Test Module`** — deliberately not run; both write.
- **`Tools`, `Environment`, `View`, `Edit` menus.** Only `Wizards`, `Build` and
  `File` were opened across studies 26–28.
- **The script editor.** `PT-1340` cites `TdlgScriptEditor`'s dimensions from the
  binary; **nobody has opened it.** It is the fourth of our four tabs and the
  least observed.
- **The Journal and Faction editors.** `PT-1376` cites them from the form census;
  not opened. **Our `QUEST-MODEL-01` has no mapping in this document as a
  result** — that is the largest remaining hole in Part B.
- **What selects the red overlay lines** in the area viewer.
- **Whether `Update Instances` and `Update instances in current area` differ in
  behaviour** — still only the labels were compared.
- **Import/Export.** Present on the File menu and on every blueprint context
  menu; never exercised. **`PT-1334`'s exchange has no Aurora comparison yet.**
