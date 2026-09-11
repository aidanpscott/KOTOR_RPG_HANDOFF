# OUTLINE-01 — the seven books, chapter by chapter

> **⚠⚠ SUPERSEDED — `OUTLINE-02.md`.** MAIN ruled book identity (`PT-1705`, relayed —
> not independently read; the copy of `docs/PLAYTEST-RULINGS-01.md` in this repository
> tops out at `PT-1548` and does not carry it). **Eight books now, five core three
> supplementary, not seven.** Species returns to the Player's Handbook — **this closes
> Wall 1 below**, by returning to the single-PHB spine rather than away from it, which
> was one of this document's own three predicted readings (**§3.1**, second bullet).
> The Bestiary named at **§3, BOOK THREE** below is cut entirely; nothing it held is
> lost — redistributed by function across the new Threat Database, Species Compendium,
> and Advanced Player's Guide. **Retained here in full, unedited below this notice,
> because it is the record of how Wall 1 and Wall 2 were first found and it is cited
> by that number from later work.**

**From AUTHOR. First deliverable. ⚠ NO PROSE IS DRAFTED HERE and none will be until this is reviewed.**

**Scope of this document:** a chapter list for each of the seven books, with every chapter
marked for whether the mechanics underneath it already exist — and, where they do, which
document and which ruling carry them.

**⚠ What this document does NOT do:** it does not choose a chapter number where two
existing documents disagree, does not name a species trait, a class number, a weapon stat
or a creature's mechanics that is not already ruled, and does not resolve any of the nine
items in **§7**. Those are the owner's, per `PT-1349`.

---

# 0 · Three things the brief located differently, and where they actually are

**Stated as corrections to my own starting position, not as complaints — each changes what
I could read.**

| Brief says | Actually |
|---|---|
| `design/BUILD-ORDER-01.md` | **Not in this repository.** No file named `BUILD-ORDER-*` exists anywhere on this filesystem. The stop protocol it governs by is **`PT-1349`** in `docs/PLAYTEST-RULINGS-01.md:51499`; its outbound half is **`PT-1388`** at `:52463`, which records itself as *"Recorded in BUILD-ORDER-01 beside the stop protocol."* **I have followed the protocol from the rulings, not from the file.** |
| `playtest/PLAYTEST-RULINGS-01.md` | **`docs/PLAYTEST-RULINGS-01.md`.** 56,185 lines. |
| *"~900 numbered rulings"* | **1,547 `## PT-` headings spanning `PT-1`–`PT-1548`.** Not a correction to make — an understatement, and the larger number is the one I worked from. |
| `data/books/` holds RCR, the Campaign Guide, D&D structural references | **`data/books/` does not exist.** See **§2.3**. This is the single largest constraint on what I can do next. |

## 0a · And a citation hazard I inherited rather than found

**`PT-1446` / `BUILD 94` already record it and I am not re-opening it: some `PT` ids resolve
to two live headings** — `PT-21`, `PT-29`, `PT-30`, `PT-31`, `PT-32`, `PT-394`, `PT-426`,
`PT-484`, `PT-1085` — **and some numbers in the range are unissued** (`PT-44`, `PT-46`–`53`,
`PT-87`, `PT-264`, `PT-411` among them).

**Consequence for this outline, which is the only part that is mine:** where I cite one of
the doubled ids I give the **line number** beside it, because the id alone does not resolve.
**`BUILD 94` states the rule I am obeying —** *"a ruling with a shared number is one
everybody cites wrongly."*

---

# 1 · Where I filed this, and why there

**The brief says `HANDOFF/BOOKS/`. This repository *is* the handoff** — `README.md` line 3:
*"Files here are pushed by the main agent and fetched by specialist agents."* **So I read
`HANDOFF/BOOKS/` as `BOOKS/` at this repository's root, and created it.**

**No `BOOKS/` convention existed before this file.** `grep -rn "HANDOFF/BOOKS\|BOOKS/"` across
every `.md` in the repository returns nothing. **If the intended target was a directory in
`MAIN_WORK` instead, this is in the wrong place and moving it costs one `git mv`.**

---

# 2 · What I can actually draft against

## 2.1 · The inventory, measured

**`from-library/WHERE-IS.md` indexes 260 documents across 26 category files.** I matched
every indexed name against every `.md` filename in this repository:

    LIBRARY DOCUMENTS INDEXED     260
    PRESENT IN THIS REPOSITORY     61
    ABSENT                        199

**⚠ And `WHERE-IS.md`'s own warning applies to that measurement and I have honoured it:**
*"a document that exists as `FOO-01.md` in another repo exists here as a SECTION INSIDE a
category file… `find`, `ls` and a filename `grep` will all return nothing for it. That is
not absence — it is the wrong shape of search."*

**So the 199 are absent FROM THIS REPOSITORY, and that is the only claim I am making.**
They are held by the Library, consolidated into `C01`–`C26`, and this session cannot open
that repository. **They are not lost. They are not reachable from here.**

## 2.2 · The 61 that are here, by book

**This is the real constraint, and it does not fall evenly across the seven books.**

| Book | Mechanical ground truth held here | Verdict |
|---|---|---|
| **Player's Handbook** | `SKILLS-01`, `SKILL-RESOLUTION-01`, `CLASS-ROSTER-01`, `CLASSES-STANDARD-PHB`, `CLASSES-FORCE-PHB`, `CLASS-TABLES-{BASE,JEDI,DROID,AUTHORED}`, `CLASS-ATTACKS-01`, `MULTICLASS-01`, `FEAT-SCHEDULE-01`, `FEATS-LIBRARY-01`, `ATTACKS-01`/`-04`/`-05`/`-06`/`-07`, `ACTION-ECONOMY-01`, `ALIGNMENT-01-v2`, `DEATH-AND-DIFFICULTY-01`, `PARTITION-01`, `FORCE-POOL-01-v3`, `POWER-COSTS-01`, `FORCE-POWERS-01`, `FORCE-TRAINING-01`, `FORCE-AWAKENING-01`, `FORMS-01`, `PREGENS-01`, `CHARACTER-RECORD-01` | **DRAFTABLE** |
| **Species Compendium** | `SPECIES-CHAPTER-v2`, `DROID-MODELS-01`, `DROID-SKILLS-01`, `UPBRINGING-01`, `PROFESSIONS-01`, `PROGRAMMINGS-01`, `STARTING-EQUIPMENT-01` | **MOSTLY** — nine `SPECIES-*` supporting documents absent |
| **Armory** | `EQUIPMENT-01`, `ITEMS-01`–`09`, `STARTING-EQUIPMENT-01` | **PARTLY** — ten supporting documents absent |
| **Bestiary** | `DROID-MODELS-01`, `DROID-SKILLS-01` only | **⚠ BLOCKED on the beasts half** |
| **Gamemaster's Holocron** | `DEATH-AND-DIFFICULTY-01`, `SKILL-RESOLUTION-01`, `ALIGNMENT-01-v2`, `SCENARIOS-01`, `PREGENS-01`, `D-CURRENCY-01` | **PARTLY** |
| **Galactic Timeline** | **none** | **⚠ BLOCKED** |
| **Planetary Atlas** | `WORLDS-REGISTER-01` (admission and permission rules — **not world entries**), `ATLAS-SEED-v3`, `to-atlas/`, `to-main/findings/` (4 of 16) | **⚠ BLOCKED on world entries** |

## 2.3 · ⚠ The source books are not here — a scoped negative, stated as one

**`data/` holds 27 files: 24 BioWare `.2da` tables and three files under `data/extracted/`.
There is no `books/` subdirectory and no book text of any kind.**

**Where I looked:** `find / -type d -name "books"` (whole filesystem, `/proc` excluded) — no
hit. `find data -type f` — 27 files, listed above. `grep -rli "revised core rulebook\|\bRCR\b"`
and `grep -rli "campaign guide"` across every `.md` — **both return only documents that
*cite* those books, never the books themselves.**

**What exists is second-hand and mostly not here either:** `RCR-DARKSIDE-FINDINGS`
(pp. 180–182), `RCR-REPUTATION-FINDINGS` (pp. 111, 122–123), `GAZETTEER-PART-D` (*"KOTOR
Campaign Guide Timeline, pp. 112–113"*), `A1-A4-FINDINGS`, and the `TO-EXTRACTOR-RCR-*`
chain. **All five are in the Library's consolidated files. None is in this repository.**

**⚠ So the instruction *"read them the way Extractor does — cite precisely, folio and line
where you can"* cannot be carried out from here.** I cannot cite a folio in a book I cannot
open, and **I will not cite one from memory** — that is the exact failure `PT-1354` names
twice in one session: *"I reasoned from a summary I held rather than from the document."*

**This is a need, not a proposal:** **the Author needs either the book texts, or the
Library's derived-findings documents, or read access to the Library.** Which of the three
is the owner's call and I have not assumed one.

---

# 3 · ⚠⚠ THE ONE THING THAT BLOCKS DRAFTING, AND IT IS STRUCTURAL

**Two documents already in this repository are written as chapters of a single Player's
Handbook, and the seven-book structure in my brief puts them in two different books.**

    STUDY/_reference/SPECIES-CHAPTER-v2.md:1     "# Chapter One: Species of the Old Republic"
    STUDY/_reference/CLASSES-STANDARD-PHB.md:7   "Star Wars: Knights of the Old Republic —
                                                  Player's Handbook, Chapter 3"
    STUDY/_reference/CLASSES-STANDARD-PHB.md:9   "The six Force classes are Chapter 4;
                                                  the prestige classes are Chapter 5."

**That is a drafted, numbered, four-chapter spine: Species 1, ? 2, Standard classes 3,
Force classes 4, Prestige classes 5.** `SPECIES-CHAPTER-v2` is 1,274 lines of finished
player-facing prose. `CLASSES-STANDARD-PHB` is 1,269 lines with all thirteen classes
written up. **These are not sketches.**

**⚠ And my brief says Species is its own book** — *"Species Compendium is what a PLAYER
reads to build a character"* — **which means `SPECIES-CHAPTER-v2` is not Chapter One of
anything in the seven-book structure, and the PHB's Chapter 2 slot has no occupant and
never had one named.**

## 3.1 · Why I am not resolving it

**Three readings are available and they produce three different books:**

- **The seven-book structure supersedes the chapter numbering.** `SPECIES-CHAPTER-v2`
  becomes the Species Compendium's opening and loses its number; the PHB renumbers from 3/4/5
  down to 1/2/3 or similar.
- **The chapter numbering is current and the seven books are an outer shelf structure** —
  i.e. the "Player's Handbook" of `CLASSES-STANDARD-PHB:7` and the "Player's Handbook" of
  my brief are the same book, and the Species Compendium is a *reprint* or an *expansion*
  rather than the home of Chapter One.
- **Both are current and `SPECIES-CHAPTER-v2` is simply stale on its own header**, the way
  `CLASS-ROSTER-01`'s *"Standard base — 13"* heading sat at *"12"* until `TRACE-98`, and
  its *"Force prestige — 6"* heading sat at *"8"* while the text below it already said six.

**⚠ I cannot tell which from the documents, and picking one is step 4 smuggled in.**
`PT-1349`: *"an agent working on one screen does not have the whole system in view — and if
it resolves the wall alone it will always reach step 4, because writing the thing is what is
in front of it."*

**What it costs to be wrong:** every cross-reference in seven books. A chapter reference is
the most-repeated sentence in a sourcebook and the most expensive thing to renumber late.

**⚠ What I did NOT do about it:** I did not renumber anything, did not draft against either
reading, and did not pick a provisional numbering *"to be fixed later."* **The outline below
names chapters and does not number them across books** — each book's chapters are listed in
reading order, and the numbers go in when this is answered.

---

# 4 · How every chapter below is marked

| Mark | Meaning |
|---|---|
| **`RULED`** | Mechanics exist **and the document is in this repository.** I can draft prose against it now. Ruling cited. |
| **`RULED · NOT HELD`** | Mechanics exist per `WHERE-IS`, **the document is not in this repository.** I can outline it; I cannot draft it. |
| **`PROSE`** | Original prose. Nothing mechanical at stake — framing, voice, worked examples, how-to-read. **This is the part of the job that is actually mine.** |
| **`DRAFTED`** | Player-facing prose **already exists** and the chapter's work is revision and placement, not authorship. |
| **⚠ `GAP`** | The chapter needs a mechanic that **does not exist anywhere I can see.** Goes to §7, not into a draft. |

---

# 5 · THE SEVEN BOOKS

---

## BOOK ONE — PLAYER'S HANDBOOK

**The only book with enough ground truth here to draft end to end.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **What this game is** — the Old Republic at 3956 BBY, what a session looks like, what dice you need | **`PROSE`** | Dice conventions are `DICE-01` — **`NOT HELD`**. The framing is mine. |
| — | **Making a character** — the creation order, end to end | **`RULED · NOT HELD`** | `CHARACTER-CREATION-01` — *"the twelve-step creation order"*, `C25`. **⚠ Absent here.** Order partly recoverable: `SPECIES-CHAPTER-v2:131` — *"⚠ CHARACTER CREATION ORDER — SPECIES BEFORE ANYTHING ELSE. `PT-594`"* |
| — | **Abilities** | **`RULED`** | `EQUIPMENT-01 §6` — *"Ability score generation — the blocker is closed."* Primary/secondary per class at `CLASS-ROSTER-01 §PT-717`, **⚠ superseded on saves by `PT-119`'s three ladders via `PT-1387`** |
| — | **Species** — *pointer chapter, or the whole thing* | **⚠ see §3** | `SPECIES-CHAPTER-v2`, `PT-594`, `PT-623` |
| — | **The standard classes** — thirteen | **`DRAFTED`** | `CLASSES-STANDARD-PHB`, 1,269 lines. Derived from `SKILLS-01 §9.2b` (`PT-1299`). **⚠ Its own header: *"eight of the thirteen carry rulings the owner has not yet confirmed."*** |
| — | **The Force classes** — six | **`DRAFTED`** | `CLASSES-FORCE-PHB`, `PT-997`. Gap named by the document itself: `PT-996` found *"the whole Force tier had no chapter"* |
| — | **The prestige classes** — nineteen | **⚠ `GAP`** | `CLASS-ROSTER-01 §3` (13 standard) and `§4` (6 Force), entry rules at `PT-573`, droids at `PT-577`. **⚠ `MANIFEST.md`: *"Prestige classes have no lists anywhere. That is an open design question, not an omission. Do not synthesise."*** Skill lists arrived later at `SKILLS-01 §9.2c` (`PT-1322`) — **that section is in the copy here.** The gap is class *features*, not skills. |
| — | **Skills** | **`RULED`** | `SKILLS-01`. **26 — 25 character + `Fly`, beast-only.** Descriptions `PT-1291`, count `PT-1292`/`PT-1293`, text map `PT-1345`, consolidations `PT-1302`. **⚠ Armour check WITHDRAWN, `PT-1323`.** Aptitude `§11`, skill feats `§12` |
| — | **Using a skill** — the DC ladder | **`RULED`** | `SKILL-RESOLUTION-01`. **⚠ `§5.3` puts Medicine in Effect mode with no numbers; medpac values are `PT-1`'s B3** |
| — | **Feats** | **`RULED`** | `FEATS-LIBRARY-01` — **221 entries, 90 chains.** Schedule `FEAT-SCHEDULE-01` (`Saboteur` added, `PT-1387`-era). Granted-not-bought `§5a`. Reaching a character `PT-353`. **⚠ `PT-618`/`PT-627`: DO NOT REGENERATE — hand-maintained** |
| — | **A turn** — action economy, initiative, surprise | **`RULED`** | `ACTION-ECONOMY-01`. **⚠ `§6.1` makes Action the default;** `PT-1`'s B1 rules **no power is a Bonus action** because no entry marks one |
| — | **Attacks** — the three currencies | **`RULED`** | `ATTACKS-01`; rosters `ATTACKS-04` ranged, `-05` melee, `-06` lightsaber, `-07` unarmed. Per-class grants `CLASS-ATTACKS-01` |
| — | **Damage, dying, and difficulty** | **`RULED`** | `DEATH-AND-DIFFICULTY-01`, `PT-152` — three modes |
| — | **The Force** — sensitivity, the pool, powers, forms | **`RULED`** | `FORCE-AWAKENING-01`; `FORCE-POOL-01-v3` (**⚠ v1 and v2 superseded — `PT-102` closes the pool-formula fork**); `PARTITION-01`; `POWER-COSTS-01`; `FORCE-POWERS-01`; `FORCE-TRAINING-01`; `FORMS-01` |
| — | **Multiclassing** | **`RULED`** | `MULTICLASS-01` — **no entry credit** |
| — | **Alignment and drift** | **`RULED`** | `ALIGNMENT-01-v2` — SETTLED |
| — | **Equipment for players** — *a précis; the Armory is the book* | **`RULED`** | `STARTING-EQUIPMENT-01`, CLOSED `PT-724`–`PT-779`. **Three routes — the Assortment, the Purse, the GM decides (`§1`)** |
| — | **Your character sheet** | **`RULED`** | `CHARACTER-RECORD-01` |
| — | **Nine worked characters** | **`DRAFTED`** | `PREGENS-01` |

---

## BOOK TWO — SPECIES COMPENDIUM

**What a player reads to build a character. ⚠ Creature lore does not enter this book — that
is Book Three, and the separation is the brief's, not mine.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **How species work** | **`DRAFTED`** | `SPECIES-CHAPTER-v2 §"How Species Work"` (line 13) |
| — | **Size is mechanical** | **`RULED`** | `SPECIES-CHAPTER-v2:103`, **`PT-623`** |
| — | **The thirty-one** — one entry each | **`DRAFTED`** | `SPECIES-CHAPTER-v2 §"The Entries"` (line 95). **⚠ Count conflict — see §7.4** |
| — | **The awkward cases** | **`DRAFTED`** | `SPECIES-CHAPTER-v2:1243` |
| — | **Species traits and racial feats** | **`RULED · NOT HELD`** | `RACIAL-FEATS-01` (`C17`), `SPECIES-FEATS-DRAFT` (**⚠ DRAFT**), `SPECIES-RACIAL-SKILL`, `SPECIES-SKILLS-TABLE` (*"adds the three Aqualish subspecies rows"*). **Five traits CLOSED at `SKILLS-01 §5` — *"and not the way this section predicted."*** Species bonuses `SKILLS-01 §6` |
| — | **Ages and lifespans** | **`RULED · NOT HELD`** | `SPECIES-AGES-01` — *"age bands COMPLETE for 32 of 32 base species"* (`TO-ATLAS-01`) |
| — | **Languages** | **`RULED · NOT HELD`** | `SPECIES-RECORDS-01-20-LANGUAGE-CHECK`; `D-AN-DROID-LANGUAGES`; `D-X`/`D-Z` — *"`speaks_basic: individual`"* (`SPECIES-PACKET-46`) |
| — | **Playing a droid** — the seven chassis | **`RULED`** | `DROID-MODELS-01` — `Battle`, `Assassin`, `Labor`, `Astromech`, `Protocol`, `Probe`, `Remote`. Manufacturer `PT-586`; backtracking `PT-589`; kiosk stock `PT-592`; reserved designations `PT-595`; **model price is the only price `PT-608`**; **model feats, one per model, `PT-610`**. **⚠ `§7` — the `Remote` chassis has NO FILE ENTRY** |
| — | **Droid skills** | **`RULED`** | `DROID-SKILLS-01` — `§2.1` universal, **`§2.2` closes some to every chassis** (*"`Streetwise` stays closed to every chassis"*), `§2.4` the per-chassis gate. **⚠ `PT-1405`: `§2.4` says 14 and 12 where the grid computes 15 and 13 — a recorded discrepancy, not mine to fix** |
| — | **Droids buy feats, they do not learn them** | **`RULED · NOT HELD`** | `DROID-INSTALLATION-01` (`C06`) — owner decision. **⚠ The droid-bay exception is here: `FEATS-LIBRARY-01:1654`** |
| — | **Upbringing** | **`RULED`** | `UPBRINGING-01` — **9, SETTLED AS FLAVOUR, `PT-705`. ⚠ No mechanical grant** |
| — | **Professions** | **`RULED`, prose ⚠ not mine** | `PROFESSIONS-01`. **⚠⚠ `PT-1003` supersedes the *"prose is unwritten"* status: `PT-704` ruled the prose is ENGINE WORK — *"`28 × 8 × 292 × 52` is a template system, and a template system is code."*** **I must not write it.** Owner's vision `PT-690`, additions `PT-691`, the Hermit `PT-693`, random `PT-777`, upgrade `PT-772`. **⚠ Droids get no lifestyles, `PT-692`** |
| — | **Programmings** — the droid's profession | **`RULED`** | `PROGRAMMINGS-01` — **17** |
| — | **What you own at level one** | **`RULED`** | `STARTING-EQUIPMENT-01` — 18 organic arrays, 9 droid arrays (LOCKED `PT-724`), 28 profession grants (`PT-762`). `Two-Weapon Fighting` rows `PT-744`; training-saber colour by class `PT-755` |

---

## BOOK THREE — BESTIARY

**⚠ NAMED. MAIN ruled this title over the brief's "Field Guide to Beasts and Machines" —
the collision named in this outline's first draft. Retired here; use `Bestiary` in every
future reference to this book.**

**What a GM reads to run an encounter. ⚠ The droid half is draftable. The beast half is not
reachable from here.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **Running a creature** | **`PROSE`** over **`RULED · NOT HELD`** | `GM-CREATURES-01` (`C22`) |
| — | **How a beast fights** | **`RULED · NOT HELD`** | **`BEASTS-ATTACKS-01`** (`C22`, md5 `800ca906`) — **named in the brief as already ruled, and absent from this repository** |
| — | **Beast levels** | **`RULED · NOT HELD`** | `BEASTS-LEVELS-01` |
| — | **Beast skills** | **`RULED · NOT HELD`** | `BEASTS-SKILLS-01`. **⚠ The `Fly` skill is beast-only and IS held — `SKILLS-01 §1`** |
| — | **Beast feats** | **`RULED · NOT HELD`** | `BEASTS-FEATS-01` |
| — | **Temperament** | **`RULED · NOT HELD`** | `BEASTS-NATURE-01` |
| — | **Obedience** — per-beast DCs | **`RULED · NOT HELD`** | `BEASTS-OBEDIENCE-01` |
| — | **The entries** — 27 statted creature companions | **`RULED · NOT HELD`** | `BEASTS-ENTRIES-01` — count from `TO-ATLAS-01`: *"27 creature companions, statted… type, size, traits and a defining ability"* |
| — | **Beasts a player can take** | **`RULED · NOT HELD`** | `BEASTS-PLAYER-01`. Related: the `Beast Master` prestige class, `CLASS-ROSTER-01 §3` |
| — | **Quick reference** | **`RULED · NOT HELD`** | `BEASTS-REFERENCE-01` |
| — | **Building an encounter** | **`RULED · NOT HELD`** | `ENCOUNTER-01` (re-spliced at the engine-phase open, cites to `PT-1051`) |
| — | **Droids as opponents** — the seven chassis from the other side | **`RULED`** | `DROID-MODELS-01`; **`§7b` LORE ONLY — attested, not ownable, `PT-605`**; `§9` what a model is and is not |
| — | **Droid construction and upgrade** | **`RULED · NOT HELD`** | `DROID-CONSTRUCTION-01`, `DROIDS-UPGRADE-01` (both `C21`). Droid items ARE held — `ITEMS-04`, 135 items |
| — | **Two anomalies in the source data** | **`RULED`** | `DROID-MODELS-01 §8` |

**⚠ Nine of fourteen chapters are `NOT HELD`. This book cannot be drafted from this
repository** — see §7.1.

---

## BOOK FOUR — ARMORY

**Weapons, armor, gear, starship hardware. ⚠ `EQUIPMENT-01` and `ITEMS-01`–`09` are the
mechanical ground truth and both are here. The starship half is not.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **How an item is described** | **`RULED · NOT HELD`** | `PROPERTY-VOCAB-01` (`C21`) — the property vocabulary every entry uses |
| — | **Weapon damage and the defence formula** | **`RULED`** | `EQUIPMENT-01`. **Base dice adopt the game's — `PT-339`, supersedes `§105`.** Ranged adds Dexterity to damage — **`PT-340`.** Massive Criticals, capped `2d6` — **`PT-341`.** Wield classes — **`PT-169`** |
| — | **Melee weapons** | **`RULED`** | `EQUIPMENT-01 §2`–`§3`; entries in **`ITEMS-01` — 418 weapons, 74 in both games** |
| — | **Ranged weapons** | **`RULED`** | `EQUIPMENT-01 §4`; `ITEMS-01`. **Range cross-checked against `baseitems.2da` and identical** |
| — | **Lightsabers** | **`RULED`** | `EQUIPMENT-01 §4b`; crystals `PT-345` |
| — | **Armour** | **`RULED`** | `EQUIPMENT-01 §5`; **`ITEMS-02` — 173 items.** **⚠ `§8` droid plating carries NAMED PLACEHOLDER VALUES** — see §7.6 |
| — | **Upgrades and the upgrade tree** | **`RULED`** | `ITEMS-03` — 164 items; **`ITEMS-09`, the tree, refiled at `PT-781`.** `Upgradeable` `PT-349`. **⚠ `UPGRADES-01` (`C21`) NOT HELD — CLOSED at `PT-781`/`PT-783`, 143 rows refiled, plot drops 147 → 13** |
| — | **Droid equipment** | **`RULED`** | `ITEMS-04` — 135 items |
| — | **Worn gear** | **`RULED`** | `ITEMS-05` — 241 items |
| — | **Usable items** | **`RULED`** | `ITEMS-06` — 58 items, 30 in both games. **⚠ Re-spliced S24: *"`CastSpell — subtype dropped` cells replaced with durations"*.** Medpac values `PT-1` B3 |
| — | **Quest and plot items** | **`RULED`** | `ITEMS-07` — **20 items** (`datapad` 2, `droid` 5, `plot` 13). **⚠ Header corrected 154 → 20 at `PT-871`** |
| — | **Everything else** | **`RULED`** | `ITEMS-08` — 42 items, 36 in both games |
| — | **Tiers, pricing and availability** | **`RULED`** | Tiers `PT-308`; unique `PT-327`; the feat remap `PT-384`. **⚠ `cost_tables` and `SCOPE-ITEMS-01` NOT HELD.** Currency `D-CURRENCY-01` **is** held |
| — | **The weapon matrix** | **`RULED · NOT HELD`** | `WEAPON-MATRIX-01` (`C21`) |
| — | **Crafting** | **`RULED · NOT HELD`** | `CRAFTING-01` (`C21`) |
| — | **Loot** | **`RULED · NOT HELD`** | `LOOT-01` — derives an area's tier from encounters and lock DCs (`TO-ATLAS-01`) |
| — | **Starships** | **`RULED · NOT HELD`** | `STARSHIPS-01` — **21 hull rows, era batches `PT-804`** (`C23`) |
| — | **Space combat** | **`RULED · NOT HELD`** | `SPACE-COMBAT-01`, re-spliced at `PT-879`. **⚠ It derives from `MOUNTED-COMBAT-01`, the shared-turn mount system — also NOT HELD** |

---

## BOOK FIVE — GAMEMASTER'S HOLOCRON

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **Running this game** | **`PROSE`** | Mine |
| — | **Difficulty and what dying means** | **`RULED`** | `DEATH-AND-DIFFICULTY-01`, **`PT-152`** — three modes |
| — | **Setting a DC** | **`RULED`** | `SKILL-RESOLUTION-01` — the ladder |
| — | **Awarding experience** | **`RULED · NOT HELD`** | `EXPERIENCE-01` — **SETTLED, `PT-660`** (`C25`) |
| — | **The party** | **`RULED · NOT HELD`** | `PARTY-01` — **LOCKED, `PT-655`–`PT-659`** |
| — | **Companions and henchmen are different things** | **`RULED`** | `FEATS-LIBRARY-01 §5b` — **`PT-145`, amended by `PT-571`** |
| — | **Influence** | **`RULED · NOT HELD`** | `INFLUENCE-01` (`D-AH`); `PORT-02-v2 §5` attitude model; `RCR-REPUTATION-FINDINGS` |
| — | **Alignment, drift, and the dark side** | **`RULED`** | `ALIGNMENT-01-v2` — SETTLED. Supporting: `RCR-DARKSIDE-FINDINGS`, `CORRECTION-01` — **NOT HELD** |
| — | **Rest and meditation** | **`RULED · NOT HELD`** | `REST-AND-MEDITATION-01` — `D-AI`, an overlay on `FORCE-POOL §4` |
| — | **Factions** | **`RULED · NOT HELD`** | `FACTIONS-01` — SETTLED for both packages |
| — | **Encounters and enemy behaviour** | **`RULED · NOT HELD`** | `ENCOUNTER-01`; `GROUND-AI-01`; `SPACE-AI-01` — four faction doctrines, `PT-806`/`PT-807` |
| — | **Loot and reward** | **`RULED · NOT HELD`** | `LOOT-01` |
| — | **Diversions** — pazaak and swoop racing | **`RULED · NOT HELD`** | `PAZAAK-01` — **CLOSED `PT-809`–`PT-811`, no skill applies.** `SWOOP-01` (`C24`) |
| — | **Eight playtest scenarios** | **`DRAFTED`** | `SCENARIOS-01` — with `PREGENS-01` and `DICE-01` |
| — | **Nine pregenerated characters** | **`DRAFTED`** | `PREGENS-01` |

---

## BOOK SIX — GALACTIC TIMELINE

**⚠ Nothing for this book is in this repository. Every row below is `NOT HELD`.**

| # | Chapter | Mark | Source |
|---|---|---|---|
| — | **How this timeline was built** | **`PROSE`** over **`NOT HELD`** | `CANON-01-v2 §3.4` — the predicate grammar; `METHOD-RECORD-01` (**held**, in `to-atlas/reference/`); `AMENDMENT-DEEP-HISTORY-BOUND` — the pre-April-2014 Legends bound, **⚠ one named exception exists** |
| — | **The dated spine** | **`RULED · NOT HELD`** | `EVENTS-01` — re-spliced at `PT-890`, the Atlas era read |
| — | **Eras** | **`RULED · NOT HELD`** | `TIMELINE-01`; `CLOCK-01`; `EVENTS-PLAN-01` (**⚠ PLAN ONLY, nothing researched, `PT-676`**) |
| — | **Deep history** | **`RULED · NOT HELD`** | `RULING-SWTOR-DEEP-HISTORY` (`D-R`); `ERA-VITIATE-01` — 5113–4999 BBY; `D-VIT-01` — **the SWTOR exception and its bounds, owner-ruled** |
| — | **The Tales of the Jedi sweeps** | **`RULED · NOT HELD`** | `TEMPORAL-SWEEP-TOTJ-DEEP-01`…`-12`; `TEMPORAL-SWEEP-TOTJ-BATCH` (14 records); `TEMPORAL-SWEEP-LEGENDS-01` (11 records); `TEMPORAL-ENUM-01` (37 records / 29 subjects) |
| — | **Revan** | **`RULED · NOT HELD`** | `D-REVAN-04` — **CURRENT in the chain; `-01` and `-03` superseded.** *"Corrects 03 on Malak"* |
| — | **The Campaign Guide timeline** | **`RULED · NOT HELD`** | `GAZETTEER-PART-D` — *"rank 2, book transcription. KOTOR Campaign Guide Timeline, pp. 112–113"* |
| — | **What the narrative clock does** | **`RULED · NOT HELD`** | `RED-TEAM-REPORT-NARRATIVE-CLOCK` — *"the verdict: the claim holds"* |

---

## BOOK SEVEN — PLANETARY ATLAS

**⚠ The rules for admitting a world are here. The worlds are not.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | **What counts as a world** | **`RULED`** | `WORLDS-REGISTER-01 §1` objects, `§2` evidence, `§3` sub-locations |
| — | **Access, permission and refusal** | **`RULED`** | `WORLDS-REGISTER-01 §4` permissions, **`§5` refusal.** Supersedes the ban-list proposal (rejected, `D-W1`) |
| — | **Choosing a homeworld** | **`RULED`** | `WORLDS-REGISTER-01 §7` chargen interface. **⚠ Origin world and homeworld are different things — `SKILLS-01 §10`** |
| — | **The entries** | **⚠ `NOT HELD`** | **The world records live in the Atlas agent's own repository.** What is here is correspondence — `to-atlas/TO-ATLAS-01`…`-26`, `TO-ATLAS-JOINT-01`, `to-main/TO-MAIN-*-ATLAS` — and **4 of 16 findings** (`F-ORD-CRUSADE`, `F-SITH-ROADS`, `F-STEREOTYPE`, `F-WONDERS`) |
| — | **Sith space** | **`NOT HELD` (partial)** | `to-main/findings/F-SITH-ROADS.md` **is held** — *"the road map of Sith space, and why sixteen worlds should stay blocked."* `F-SITH-EMPTY`, `F-ZIOST-REFINE`, `F-KORRIBAN-REFINE` are **not** |
| — | **The Ord worlds** | **`NOT HELD` (partial)** | `to-main/findings/F-ORD-CRUSADE.md` **is held** — *"the Ords are crusade infrastructure."* `F-ORD-NETWORK` is not |
| — | **The Twenty Wonders of the Galaxy** | **`PROSE` over `RULED`** | `to-main/findings/F-WONDERS.md` **is held** — *"a canonical closed list of twenty destinations, three already in the selection"* |
| — | **Currency and trade** | **`RULED`** | `D-URKUPP-01` (resolves the `LIBRARY-39` three-way conflict); `D-CURRENCY-01` — **AMENDED** |

### ⚠ 7.0 · A finding this book must not repeat

**`F-STEREOTYPE` is held here and it is about the Atlas's own method:** *"the menus default
to the tier's cliché whenever the world is thin… derived from a floor-distribution count
across all 292 menus — **it is the same failure three times and I only saw it the third**."*

**That is an authorship warning aimed directly at me.** A thin world tempts an author into
the genre-default sentence, and the Atlas measured that happening 292 times. **Whatever
prose this book eventually gets, a thin world must read as thin rather than as a cliché
dressed up.** `F-INDEX` also records that this finding *"no other agent has ever seen"* —
**one has now.**

---

# 6 · What is actually draftable today

**Stated plainly, because §5 is long and the answer is short.**

| | |
|---|---|
| **Draftable now** | **Book One** end to end, except the prestige-class features (`GAP`) and the species chapter's placement (§3). **Book Two** except six supporting chapters. **Book Four**'s ground-weapon, armour, upgrade and item chapters — thirteen of eighteen |
| **Outline only** | **Book Three** (9 of 14 absent), **Book Five** (9 of 15 absent), **Book Seven** (the entries) |
| **Not startable** | **Book Six** — every chapter absent |

---

# 7 · THE GAP REGISTER — nine items, none of them mine to close

**Stated as needs, per `PT-1349`: *"what is missing stated as a NEED rather than as a
proposed solution, because a proposed solution is step 4 smuggled in."***

**7.1 · The Author needs the 199 absent documents, or read access to the Library.**
Four of seven books cannot be drafted without them. **`BEASTS-ATTACKS-01` is named in my own
brief as already-ruled ground truth and is not here.**

**7.2 · The Author needs RCR, the Campaign Guide, and the D&D structural references** —
or the Library's derived findings from them. **§2.3.** Without one of the two, *"cite folio
and line"* is not a thing I can do honestly.

**7.3 · The chapter-numbering collision needs a ruling.** **§3.** Blocks every
cross-reference in seven books.

**7.4 · The species count is stated three ways and I did not pick one.**
`SPECIES-CHAPTER-v2:7` — *"Thirty-one of them are available to player characters."*
`MANIFEST.md` — *"31 organic + droid chassis."* `TO-ATLAS-01` — *"`SPECIES-AGES-01` — age
bands COMPLETE for **32 of 32** base species."* **31 and 32 are both asserted. A species
compendium cannot open on a number nobody has confirmed.**

**7.5 · The Force power count is stated four ways.** `FORCE-POWERS-01:3` — **88 powers.**
`MANIFEST` — *"`PT-1317` counted **112**… **112 powers** is from a ruling, not a count —
verify it."* `PT-1` B1 — `POWER-COSTS-01` carries **213 table rows.** `PARTITION-01` is a
fourth roster. **⚠ I did not run the count myself, because a count run by the Author becomes
the number by accident.** That is an Extractor job and the `MANIFEST` already asks for it.

**7.6 · Droid plating carries named placeholder values.** `EQUIPMENT-01 §8`. **Placeholder
values in a shipped Armory become real by publication.** Naming the gap rather than writing
around it.

**7.7 · Prestige class features do not exist.** **§5, Book One.** `MANIFEST`: *"Prestige
classes have no lists anywhere. That is an open design question, not an omission. **Do not
synthesise.**"* Nineteen classes, one chapter, no crunch.

**7.8 · Eight of thirteen standard classes carry unconfirmed rulings.**
`CLASSES-STANDARD-PHB:11`, the document's own header. **Drafting revision passes over those
eight before the owner confirms them spends the work twice.**

**7.9 · The item count is stated two ways.** `MANIFEST` — *"`ITEMS-01..09` hold **1,425
distinct resrefs across 1,251+ items**."* `TO-ATLAS-01` — *"`ITEMS-01` to `-08` — **1,385
items**."* **The per-file headers here sum to 1,251 across `ITEMS-01`–`08`, which matches
`MANIFEST`'s second figure and neither of the other two.** Flagged, not resolved — `ITEMS-09`
is a refiled tree rather than a ninth bucket, which may be the whole explanation, and *may*
is not a finding.

---

# 8 · SCOPED NEGATIVES — exactly where I looked

**Per `METHOD-RECORD-01 §1.5`: *"a correctly scoped negative that searched the wrong place is
still wrong."* So the scope is stated rather than the conclusion.**

| Claim | Where I looked | ⚠ Where I did NOT |
|---|---|---|
| `data/books/` does not exist | `find / -type d -name books` (whole filesystem, `/proc` excluded); `find data -type f` (27 files) | — |
| No `BUILD-ORDER-*` file exists | `find / -name "*BUILD-ORDER*"` | — |
| 199 of 260 Library documents absent | Every indexed name in `WHERE-IS.md` against every `.md` filename in this repository | **⚠ Filename matching only.** `WHERE-IS.md` warns this is the wrong shape of search for the Library itself. **The claim is about THIS repository and nothing else** |
| No `BOOKS/` convention existed | `grep -rn "HANDOFF/BOOKS\|BOOKS/" --include=*.md .` | **⚠ `MAIN_WORK` — I cannot open it** |
| Chapter numbering appears in two documents only | `grep -rhno "Chapter [0-9]*\|Chapter [A-Z][a-z]*:"` across `STUDY/_reference/` and `docs/` | **⚠ Not `BUILD/`, `TEST/`, `STUDY/*/`, or the exchange directories** — a chapter assignment ruled in a BUILD or TEST report would not be in this scope, and §3 would change if one exists |
| Beast, timeline and starship documents absent | `find . -name "BEASTS*" -o -name "TIMELINE-01*" -o -name "STARSHIPS*"` etc. | — |

---

# 9 · STOP REPORT — `PT-1349`'s four things

**⚠ This is a stop, and `PT-1349` says a stop is the system working rather than failing:
*"an agent that never stops is more worrying than one that stops often."***

**1 · What was being built, and what stopped it.**
The outline was built and is complete for all seven books. **Two things stop the next step
— drafting.** The chapter-numbering collision (**§3**), which would put a wrong number in
every cross-reference in seven books; and the absence of the source books and 199 of 260
corpus documents (**§2.3**, **§7.1**), which makes four of seven books unwritable and makes
*"cite folio and line"* impossible for all seven.

**2 · What is missing, as a need.**
**§7**, nine items. Each states the need. **⚠ None proposes a fix, and specifically: I have
not proposed which chapter numbering to adopt, have not proposed a species count, have not
proposed a Force power count, and have not proposed values for droid plating.**

**3 · What was NOT done about it.**
**No prose was drafted** — the brief forbids it before review, and drafting against an
unresolved chapter spine would have spent the work twice. **Nothing was renumbered.**
**No provisional numbering was assigned** *"to be corrected later."* **No count was run to
settle §7.4, §7.5 or §7.9** — a count run by the Author becomes the number by accident, and
those are the Extractor's, which `MANIFEST` already says. **No ruling was overturned, and
where a ruling and a document disagreed** (`PT-717` vs `PT-119` on saves; `SKILLS-01`'s
count; `CLASS-ROSTER-01`'s two stale headings) **the disagreement was recorded with both
sides cited and left standing.**

**4 · What was learned about a spec.**
**Four things.**

- **The seven-book structure and the drafted chapter headers are in conflict, and neither
  side knows it.** `SPECIES-CHAPTER-v2` and `CLASSES-STANDARD-PHB` were written to a
  single-PHB spine and have sat unchallenged. **The conflict is invisible from inside either
  document** — each is internally consistent. It only appears when a seven-book outline is
  laid over them, which is what this document is, and **that is the one thing this outline
  bought that could not have been bought any other way.**
- **`PROFESSIONS-01`'s status line says the prose is unwritten and `PT-1003` supersedes it:
  `PT-704` ruled that prose is ENGINE WORK.** An Author reading only the status line would
  have written 28 profession entries that a template system was already ruled to generate.
  **The superseding note is three lines below the line that would have caused it.**
- **`F-STEREOTYPE` is an authorship finding filed in a world-notes directory.** It measured
  genre-cliché defaulting across 292 menus and `F-INDEX` records that no other agent had
  seen it. **It is the sharpest prose-quality constraint in the corpus and it is filed where
  no author would look** — which is `F-INDEX`'s own point: *"a finding is delivered when it
  is named to someone who can act on it."*
- **The `MANIFEST`'s two traps both apply to authorship, not only to extraction.**
  *"Read for what a document ASSERTS, not what it QUOTES"* — this corpus records its
  corrections in place, so a sourcebook drafted by lifting sentences will publish overturned
  rulings as current. **`SKILLS-01` line 15 is the live example: it contains the words
  *"twenty-two skills"* and the live count is 26.**

---

**⚠ Nothing below this line is drafted, and nothing above it is a decision.**
