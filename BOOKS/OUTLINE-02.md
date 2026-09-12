# OUTLINE-02 — eight books, chapter by chapter. Supersedes OUTLINE-01

**From AUTHOR. Rebuilt against `PT-1705`'s identity ruling, relayed by MAIN.**
**⚠ NO PROSE IS DRAFTED HERE. Same standard as `OUTLINE-01`.**

**⚠ `PT-1705` was not independently read.** The copy of `docs/PLAYTEST-RULINGS-01.md`
in this repository tops out at `PT-1548`; `sync_docs.py`'s own header confirms it is
synced from a sibling `MAIN_WORK` checkout, which is not present on this machine. This
is not a block — MAIN has the access and the authority `PT-1349` describes, and the
brief given is treated as the authoritative statement of the ruling, the same way a
stop's resolution is communicated back rather than re-derived. **Flagged once, here,
so it is not mistaken for independent verification later.**

---

# 0 · What changed, and what carries forward unedited

**Eight books, not seven. Five core, three supplementary.** `Bestiary` is cut; nothing
it held is lost — redistributed by function across three books. Droids and beasts each
now split three ways: **play it** (Species Compendium), **fight it** (Threat Database),
**build or tame it** (Armory or Advanced Player's Guide).

**Wall 1 is closed.** `OUTLINE-01 §3` predicted three readings; the ruling took the
second — *"the chapter numbering is current... the Species Compendium is a reprint or
an expansion rather than the home of Chapter One."* Playable species returns to the
Player's Handbook as its own chapter, drafted against the single-PHB spine
`SPECIES-CHAPTER-v2` and `CLASSES-STANDARD-PHB` already carry. **No renumbering.**

**Wall 2 stays open, and is unrelated to this rebuild** — `data/books/` is not staged
into `HANDOFF` yet; Coder is doing that separately. Every `RULED` mark below still means
*"the mechanic exists and the document is in this repository,"* not *"citable to RCR."*

**Carried forward without re-measuring, per this project's own rule against re-running
a closed check:** the 61-of-260 document inventory (`OUTLINE-01 §2.1`), the doubled-`PT`-id
hazard (`PT-1446`/`BUILD 94`), the three unresolved counts (species, Force powers, items —
`§7` below), and the `F-STEREOTYPE` caution. None of these changed with identity; none
was re-run this round.

---

# 1 · How every chapter below is marked

| Mark | Meaning |
|---|---|
| **`RULED`** | Mechanics exist **and the document is in this repository.** Ruling cited. |
| **`RULED · NOT HELD`** | Mechanics exist per `WHERE-IS`, **document unreachable from here.** |
| **`PROSE`** | Original prose. Nothing mechanical at stake. |
| **`DRAFTED`** | Player-facing prose **already exists** — revision and placement, not authorship. |
| **⚠ `GAP`** | Needs a mechanic that **does not exist anywhere I can see**, held or unheld. |
| **⚠⚠ `UNPLACED`** | New this round. **The source exists and is marked elsewhere in this document, but the brief does not say which of two or more plausible books it belongs to.** Not a gap — a filing question. |

---

# 2 · THE EIGHT BOOKS

---

## CORE

### BOOK ONE — PLAYER'S HANDBOOK

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | What this game is | **`PROSE`** | Mine. Dice conventions `DICE-01` — `NOT HELD` |
| — | Making a character — creation order | **`RULED · NOT HELD`** | `CHARACTER-CREATION-01` (`C25`) absent. Partial recovery: `SPECIES-CHAPTER-v2:131` — *"SPECIES BEFORE ANYTHING ELSE, `PT-594`"* |
| — | Abilities | **`RULED`** | `EQUIPMENT-01 §6`. Primary/secondary `CLASS-ROSTER-01 §PT-717`, **⚠ superseded on saves by `PT-119` via `PT-1387`** |
| — | **Playable species** | **`DRAFTED` — WALL 1 CLOSED** | `SPECIES-CHAPTER-v2`, 1,274 lines, as Chapter One of this book. `PT-594` order, `PT-623` size. **No renumbering — drafted against the existing spine, per the ruling** |
| — | The standard classes — thirteen | **`DRAFTED`** | `CLASSES-STANDARD-PHB`, 1,269 lines. **⚠ Own header: eight of thirteen carry unconfirmed rulings** |
| — | The Force classes — six | **`DRAFTED`** | `CLASSES-FORCE-PHB`, `PT-997` |
| — | Skills | **`RULED`** | `SKILLS-01` — 26 (25 character + `Fly`, beast-only) |
| — | Using a skill — the DC ladder | **`RULED`** | `SKILL-RESOLUTION-01` |
| — | Feats | **`RULED`** | `FEATS-LIBRARY-01` — 221/90 chains. `FEAT-SCHEDULE-01`. **`PT-618`/`627`: hand-maintained, do not regenerate** |
| — | Action economy and combat | **`RULED`** | `ACTION-ECONOMY-01`; `ATTACKS-01`/`-04`/`-05`/`-06`/`-07`; `CLASS-ATTACKS-01` |
| — | Death and difficulty | **`RULED`** | `DEATH-AND-DIFFICULTY-01`, `PT-152` — three modes |
| — | The Force — sensitivity, pool, powers, forms | **`RULED`** | `FORCE-AWAKENING-01`, `FORCE-POOL-01-v3`, `PARTITION-01`, `POWER-COSTS-01`, `FORCE-POWERS-01`, `FORCE-TRAINING-01`, `FORMS-01` |
| — | Multiclassing | **`RULED` — ⚠ scope UNPLACED** | `MULTICLASS-01`. Base ruling (three-class cap `PT-723`, credit rules) held here — **but the brief names "deeper multiclassing" as Advanced Player's Guide content and does not say whether the base ruling stays or the whole topic moves. See §3, Book Eight** |
| — | Alignment and drift | **`RULED`** | `ALIGNMENT-01-v2` — SETTLED |
| — | Your character sheet | **`RULED`** | `CHARACTER-RECORD-01` |
| — | Starting equipment, for buying | **`RULED`** | `STARTING-EQUIPMENT-01`, CLOSED `PT-724`–`779`. **⚠ The brief says "for buying" — the source's own `§1` names three routes (Assortment, Purse, GM decides); not narrowing to one without confirmation** |
| — | Nine worked characters | **`DRAFTED`** | `PREGENS-01` |

**Removed from this book, moved to Book Eight:** the prestige classes. No longer a `GAP`
inside the PHB — it is now correctly homed with the rest of Advanced Player's Guide's
content, though the gap itself (features do not exist) is unchanged. See §3.

---

### BOOK TWO — GAMEMASTER'S HOLOCRON

**⚠ The brief's own list is narrower than what the old Book Five carried: "DCs,
influence, factions, XP, encounter design, scenarios."** Six items named. What the old
book held beyond those six is flagged `UNPLACED` below rather than dropped or kept by
assumption.

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Setting a DC | **`RULED`** | `SKILL-RESOLUTION-01` |
| — | Influence | **`RULED · NOT HELD`** | `INFLUENCE-01` (`D-AH`); `PORT-02-v2 §5`; `RCR-REPUTATION-FINDINGS` |
| — | Factions | **`RULED · NOT HELD`** | `FACTIONS-01` — SETTLED for both packages |
| — | Awarding experience | **`RULED · NOT HELD`** | `EXPERIENCE-01` — SETTLED, `PT-660` |
| — | Encounter design | **`RULED · NOT HELD` — ⚠⚠ UNPLACED, see note** | `ENCOUNTER-01` (`C22-CREATURES`). **⚠ Filed by the Library under creatures, not engine or GM tools — the same shelf as every `BEASTS-*` document — which weakly argues for Threat Database instead. Named explicitly under Holocron in the brief, so kept here, but the Library's own filing disagrees and that disagreement is worth knowing.** **⚠⚠ AND `ENCOUNTER-01 §5c` depends on an `openness` field that `PT-1051` found on ZERO of 298 swept world records — `D-OPEN-01` defines it, no world record carries it. A live defect in the source this chapter would draft against, not mine to fix, cited so it is not rediscovered.** |
| — | Eight playtest scenarios | **`DRAFTED`** | `SCENARIOS-01`, with `PREGENS-01`/`DICE-01` |

**⚠⚠ UNPLACED — not named in the brief's six, home unconfirmed:**

- **Death and difficulty** — was in both the old Book One and old Book Five. **Now
  explicit only in Book One's list. Treating as PHB-only** unless told otherwise; not
  duplicated here.
- **Rest and meditation** (`REST-AND-MEDITATION-01`, `D-AI`) — Force-pool-adjacent, and
  the Force moved fully to Book One. Could belong to either book. **Flagged, not placed.**
- **Companions and henchmen** (`FEATS-LIBRARY-01 §5b`, `PT-145`/`571`) — ties into
  controlled droids and beasts, which the new structure splits three ways. **Flagged,
  not placed.**
- **Diversions — pazaak, swoop** (`PAZAAK-01`, CLOSED `PT-809`–`811`; `SWOOP-01`) — not
  named anywhere in the eight-book brief. **Flagged, not dropped.**
- **Loot and reward** (`LOOT-01`) — GM-facing reward guidance, but also Armory-adjacent
  pricing. **Flagged as a candidate for either book, not placed.**

---

### BOOK THREE — GALACTIC THREAT DATABASE *(new — nothing drafted anywhere in the corpus)*

**In-universe framing — a maintained registry, not a dry appendix — is unauthored
anywhere in the corpus** (`grep`'d for *"bounty board," "maintained registry,"
"intelligence dossier"* repository-wide: zero hits). **This is entirely mine to write.**

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Front matter — the registry framing | **`PROSE`** | Mine. No precedent to draft against |
| — | Humanoid adversaries | **⚠ `GAP` — see note** | **No dedicated statblock document exists anywhere, held or unheld — checked `C22-CREATURES` in full, thirteen entries, none of them this.** The coherent reading, given the corpus's general practice of reusing rather than duplicating systems, is that a humanoid adversary is built with Book One's own class rules rather than a parallel NPC system. **That is my inference, not a ruling — flagged as such, not drafted as fact.** |
| — | Droid opponents — the seven chassis | **`RULED`** | `DROID-MODELS-01`; `§7b` LORE ONLY `PT-605`; `§9`. **New supporting citation found this round:** `docs/PLAYTEST-RULINGS-01.md:52865` — droid chassis ability scores are ruled **NPC statblocks, not player values** *("Labor averages Constitution 18 and ranges to 22; an organic PC cannot exceed 18")* — the mechanical basis for presenting them as adversaries distinct from playable chassis |
| — | Hostile beasts — combat stats | **`RULED · NOT HELD`** | `BEASTS-ATTACKS-01`, `BEASTS-LEVELS-01`, `BEASTS-SKILLS-01`, `BEASTS-FEATS-01` |
| — | Beast quick reference | **`RULED · NOT HELD`** | `BEASTS-REFERENCE-01` |
| — | Beast stat entries | **`RULED · NOT HELD` — ⚠⚠ ONE SOURCE, TWO BOOKS** | `BEASTS-ENTRIES-01` — *"27 creature companions... type, size, traits and a defining ability."* **Its fields mix combat data (defining ability) with lore data (type, size, traits) in one document. The new split sends lore to Species Compendium and stats here — meaning this single source needs restructuring across two books when drafted, not a copy into either.** |
| — | How adversaries behave — ⚠⚠ UNPLACED, see Book Two | **`RULED · NOT HELD`** | `GROUND-AI-01`, `SPACE-AI-01` — four faction doctrines, `PT-806`/`807`. Placed here as the more natural fit for a hostile-facing book; not named in either book's brief explicitly |
| — | Running a creature — ⚠⚠ UNPLACED, see Book Two | **`RULED · NOT HELD`** | `GM-CREATURES-01`. Candidate for either this book or Holocron's procedural material; not named in either brief |

**Explicitly removed from this book by the brief:** droid construction and upgrade —
moved to Armory. **Not a `GAP` here; it is correctly homed elsewhere.**

---

### BOOK FOUR — PLANETARY ATLAS

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | What counts as a world | **`RULED`** | `WORLDS-REGISTER-01 §1`–`§3` |
| — | Access, permission and refusal | **`RULED`** | `WORLDS-REGISTER-01 §4`–`§5` |
| — | Choosing a homeworld | **`RULED`** | `WORLDS-REGISTER-01 §7`. Origin vs. homeworld — `SKILLS-01 §10` |
| — | The entries | **⚠ `NOT HELD` — and the count needs a correction** | See §4 below. Not resolving the count; citing what the corpus itself already disputes about it |
| — | Sith space / Ord worlds / Twenty Wonders | **`NOT HELD` (partial)** | `to-main/findings/F-SITH-ROADS`, `F-ORD-CRUSADE`, `F-WONDERS` held; the rest of each thread is not |
| — | Currency and trade | **`RULED`** | `D-URKUPP-01`; `D-CURRENCY-01` — AMENDED |

**Kept from `OUTLINE-01`: the `F-STEREOTYPE` caution.** *"The menus default to the
tier's cliché whenever the world is thin"* — measured across 292 menus, and this book's
prose is exactly where that would recur.

## 2.1 · ⚠⚠ The 301 figure needs a correction before it is used again

**The brief states *"301 world entries confirmed in `data/extracted/worlds.json`."***
**Checked rather than accepted:**

- **`data/extracted/worlds.json` does not exist** — not in this repository, at any
  commit, on any branch (`git log --all --diff-filter=A --name-only` for that filename:
  zero hits). The three files actually in `data/extracted/` are `class-skills.json`,
  `_PROVENANCE.md`, `skills.json`.
- **The real file is `ATLAS/data/selection.json`, in the Atlas agent's own repository —
  not staged into `HANDOFF`.** `BUILD/RECON-worlds.md:34` names it directly.
- **And 301 is not one number even there.** `to-atlas/TO-ATLAS-JOINT-01.md:98,101`:
  *"301 SELECTED AGAINST 290 IN THE JSON. THIRTEEN SELECTED WORLDS HAVE NO JSON MENU."*
  `PT-1051` (above) separately swept **298** world records for an unrelated field.
  **Three counts — 301, 298, 290 — none of them interchangeable.**
- **And the Atlas's own correspondence explicitly warns against treating 301 as a
  measure of drafted content:** `to-main/TO-MAIN-24-ATLAS.md:29` (same text also at
  `to-library/TO-LIBRARY-21-ATLAS.md:29`) — *"Not 301 worlds. Roughly the 36 dense ones
  plus the richest of the open ones — call it 60–80 worlds carrying real sites, and I
  will not know the number until I read them."*

**Not disputing the book's Core status — that is decided.** Flagging so whatever number
reaches print is the right one: 301 is a **selection list**, not a confirmed entry count,
and the Atlas's own agents have already said so once.

---

### BOOK FIVE — GALACTIC TIMELINE

**⚠ Nothing for this book is in this repository. Unchanged from `OUTLINE-01` — not
re-measured this round.**

| # | Chapter | Mark | Source |
|---|---|---|---|
| — | How this timeline was built | **`PROSE`** over **`NOT HELD`** | `CANON-01-v2 §3.4`; `METHOD-RECORD-01` (**held**) |
| — | The dated spine | **`RULED · NOT HELD`** | `EVENTS-01` |
| — | Eras | **`RULED · NOT HELD`** | `TIMELINE-01`; `CLOCK-01`; `EVENTS-PLAN-01` (PLAN ONLY, `PT-676`) |
| — | Deep history | **`RULED · NOT HELD`** | `RULING-SWTOR-DEEP-HISTORY`; `ERA-VITIATE-01`; `D-VIT-01` |
| — | The Tales of the Jedi sweeps | **`RULED · NOT HELD`** | `TEMPORAL-SWEEP-TOTJ-*` (12 deep + batch); `TEMPORAL-SWEEP-LEGENDS-01`; `TEMPORAL-ENUM-01` |
| — | Revan | **`RULED · NOT HELD`** | `D-REVAN-04` — current in the chain |
| — | The Campaign Guide timeline | **`RULED · NOT HELD`** | `GAZETTEER-PART-D` — pp. 112–113 |

**⚠⚠ New production note, from the brief's own instruction:** *"link the two by having
timeline entries reference world names."* **This makes Book Five's authoring order-
dependent on Book Four's** — a Timeline chapter naming a world needs that world's name
settled first. Not a blocker; a sequencing note for whoever schedules the drafting.

---

## SUPPLEMENTARY

### BOOK SIX — SPECIES COMPENDIUM *(no longer chargen — the encyclopedia)*

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Old Republic overview | **`PROSE`** | Mine. `SPECIES-CHAPTER-v2:7`'s opening line is the only existing precedent, and it is one sentence |
| — | The species — lore entries | **`DRAFTED` — ⚠⚠ ONE SOURCE, TWO BOOKS** | `SPECIES-CHAPTER-v2`'s 31-entry body **already mixes lore (culture, appearance, homeworld) with mechanics (ability adjustments, size, traits).** The new split sends mechanics to Book One and lore here — the same document needs restructuring across both books, not a copy into either. Count conflict (31 vs. 32) carried forward, `§3` below |
| — | Non-playable species | **⚠ `GAP` — confirmed, not merely unheld** | Searched `C06-SPECIES` in full (sixteen entries) — every one is about the playable roster or droids. **`DECISION-FLESH-RAIDERS` is the one name that might be relevant** — Flesh Raiders are a known KOTOR hostile-humanoid faction — but it is `NOT HELD` and its content is unconfirmed from here |
| — | Playing a droid — seven chassis, droid skills | **`RULED`** | `DROID-MODELS-01`; `DROID-SKILLS-01`. Same sources as `OUTLINE-01`'s old Book Two, relocated here per the brief |
| — | Beast encyclopedia — ecology, habitat | **`RULED · NOT HELD`** | `BEASTS-NATURE-01` (temperament) is the closest existing candidate; the lore-half of `BEASTS-ENTRIES-01` (see Book Three) also belongs here once split |

---

### BOOK SEVEN — ARMORY

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Weapon damage and the defence formula | **`DRAFTED`** | `EQUIPMENT-01`. `PT-339`/`340`/`341`/`169`. **Text at `BOOKS/armory/01-weapon-damage-and-defence-formula.md`, approved by MAIN** |
| — | Melee weapons | **`DRAFTED`** | `EQUIPMENT-01 §2`–`§3`; `ITEMS-01`. **Text at `BOOKS/armory/02-melee-weapons.md`. Split from a single combined chapter — MAIN ruled Melee/Ranged/Lightsabers are three chapters, not one: different mechanical shapes, lightsabers carry their own crystal layer, and the book's own browsable-reference identity argues against one chapter covering all of `ITEMS-01`'s weapon count** |
| — | Ranged weapons | **`DRAFTED`** | `EQUIPMENT-01 §4`, corrected against `ITEMS-01` directly — six of eleven base-table rows didn't match the game data. **Text at `BOOKS/armory/03-ranged-weapons.md`** |
| — | Lightsabers | **`DRAFTED`** | `EQUIPMENT-01 §4b`, K1 standard-Lightsaber die corrected against raw `data/k1_baseitems.2da` (2d8, not the stated 2d10); crystals `PT-345`. **Text at `BOOKS/armory/04-lightsabers.md`** |
| — | Armour | **`DRAFTED`** | `ITEMS-02` — 173 items, six categories. Defence formula and droid plating taught in Chapter One, pointed back to rather than restated. **Text at `BOOKS/armory/05-armour.md`** |
| — | Upgrades and the upgrade tree | **`DRAFTED`** | `ITEMS-03` — 164; `ITEMS-09`, refiled `PT-781`. Confirms and refines Chapter One's Bonded Plates/Flexible Underlay citations; resolves what the Bacca's/Cassus Fett's unique-weapon variants actually are. **Text at `BOOKS/armory/06-upgrades-and-the-upgrade-tree.md`** |
| — | Droid equipment | **`DRAFTED`** | `ITEMS-04` — 135 items, eight categories. **Text at `BOOKS/armory/07-droid-equipment.md`. ⚠ Proposed split from the combined row below into four chapters — not yet confirmed** |
| — | Worn gear | **`RULED`** | `ITEMS-05` — 241 items (belts, forearms, gauntlets, implants, masks). **⚠ Proposed as its own chapter, not yet drafted** |
| — | Usable items | **`RULED`** | `ITEMS-06` — 58 items (adrenals, medical, trap kits). **⚠ Proposed as its own chapter, not yet drafted** |
| — | Quest and miscellaneous items | **`RULED`** | `ITEMS-07` + `ITEMS-08` — roughly 60 combined. **⚠ Proposed as one chapter, not yet drafted** |
| — | Tiers, pricing, availability | **`RULED`** | `PT-308`/`327`/`384`. Currency `D-CURRENCY-01` |
| — | The weapon matrix / crafting | **`RULED · NOT HELD`** | `WEAPON-MATRIX-01`; `CRAFTING-01` |
| — | Loot | **`RULED · NOT HELD` — see Book Two's UNPLACED list** | `LOOT-01` |
| — | Starships / space combat | **`RULED · NOT HELD`** | `STARSHIPS-01` — 21 hulls; `SPACE-COMBAT-01`, derives from `MOUNTED-COMBAT-01` |
| — | **Droid construction and upgrade** | **`RULED · NOT HELD` — moved here per the brief** | `DROID-CONSTRUCTION-01`, `DROIDS-UPGRADE-01` (both `C21`). Droid *items* are held — `ITEMS-04` |

---

### BOOK EIGHT — ADVANCED PLAYER'S GUIDE *(the after-you've-played book)*

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Prestige classes — nineteen | **⚠ `GAP`, unchanged** | `CLASS-ROSTER-01 §3`/`§4` for the roster; entry rules `PT-573`, droids `PT-577`. `MANIFEST`: *"no lists anywhere... do not synthesise."* Skill lists exist (`SKILLS-01 §9.2c`, `PT-1322`) — the gap is class *features*, all nineteen |
| — | Deeper multiclassing — entry requirements | **`RULED` for 11/19, `NOT WRITTEN` for 8/19 — ⚠⚠ SOURCE CONTRADICTS ITSELF** | `CLASS-ROSTER-01 §475`: *"THREE ENTRY REQUIREMENTS TESTED... `PT-628`."* `MULTICLASS-01 §5` calls these requirements *"the real brake"*; that same document's own `§6` calls them *"NOT WRITTEN."* Eleven are: `Commando`, `Gunslinger`, `Shadow Hunter`, `Juggernaut`, and seven more per `§6`'s count. **Eight of nineteen remain genuinely unwritten — not all nineteen, as a first read of `§6` alone would suggest.** Whether Book One's *base* multiclassing ruling also moves here or stays split — flagged in Book One, not resolved here either |
| — | Beast ownership — obedience | **`RULED · NOT HELD`** | `BEASTS-OBEDIENCE-01` — per-beast obedience DCs |
| — | Beast ownership — upkeep | **⚠ `GAP`, and a sharper one than "not held"** | The word `upkeep` returns **zero hits** anywhere in this repository's rulings ledger or the Library's own index (`WHERE-IS.md`). Every other `NOT HELD` mark in this document means *"indexed elsewhere, unreachable from here"* — this one may mean the mechanic has not been authored **anywhere**, which is a different, sharper kind of gap |
| — | Beast Master — the class | **⚠ `GAP`, cross-references the Prestige chapter above** | `Beast Master` is one of the nineteen prestige classes with no features written. Not a second, separate gap — the same one, reached from a different chapter |
| — | Beasts a player can take | **`RULED · NOT HELD`** | `BEASTS-PLAYER-01` |

---

# 3 · THE GAP AND UNPLACED REGISTER

**Carried forward from `OUTLINE-01 §7`, unresolved and not re-litigated: the species
count (31 vs. 32), the Force power count (88/112/213), the item count
(1,251/1,385/1,425), and droid plating's placeholder values. None of these changed with
identity; all are still Extractor's or the owner's, not mine.**

**New this round:**

- **Humanoid adversaries have no source, held or unheld** (Book Three).
- **Beast "upkeep" appears authored nowhere in the corpus**, sharper than the usual
  `NOT HELD` (Book Eight).
- **`BEASTS-ENTRIES-01` is one source that the new split cuts across two books** — its
  lore fields and its combat fields no longer share a home (Books Three and Six).
- **`SPECIES-CHAPTER-v2` is the same shape of problem, at larger scale** — one
  1,274-line document, lore and mechanics interleaved throughout, now needing to serve
  two books (Books One and Six) rather than being copied whole into either.
- **`MULTICLASS-01` contradicts itself internally** on whether prestige entry
  requirements are written (§5: yes, the real brake / §6: no) — resolved by
  `CLASS-ROSTER-01`, which shows both are true for different classes: eleven written,
  eight not.
- **Six chapters are `UNPLACED`** rather than gapped — the source exists and is marked,
  but the brief's per-book lists don't say which book owns them: encounter design's
  library-shelf disagreement, rest and meditation, companions and henchmen, diversions,
  loot, and the humanoid-adversary-behaviour pairing (`GM-CREATURES-01`/`GROUND-AI-01`/
  `SPACE-AI-01`) between Books Two and Three.
- **Book Four's 301-world figure needs correction before print** — it names the wrong
  file, and the right file's own maintainers have already disputed the number twice.

---

# 4 · STOP REPORT

**Not a full stop — this is a completed rebuild, delivered as asked. Recorded per
`PT-1349`'s shape because six new things were found that the brief did not anticipate,
and none of them was resolved unilaterally.**

**What was NOT done:** no chapter numbering was assigned across the eight books — same
discipline as `OUTLINE-01`, since nothing in the brief fixed an order beyond the
core/supplementary split already given. No `UNPLACED` chapter was assigned a book by
guessing. No count was run to settle species, Force powers, or items. `PT-1705` was not
read directly and nothing was drafted as if it had been.

**What this rebuild is confident about:** the eight-book identity, the Bestiary's cut,
the three-way droid/beast split, and Wall 1's closure are all applied exactly as given —
none of those needed a judgment call, only correct placement.

**Ready to draft Book One and most of Book Seven the moment this is reviewed** — both
were already the most complete books before this round, and nothing in the rebuild
reduced what they hold.
