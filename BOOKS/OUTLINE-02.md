# OUTLINE-02 — eight books, chapter by chapter. Supersedes OUTLINE-01

**From AUTHOR. Rebuilt against `PT-1705`'s identity ruling, relayed by MAIN.**
**⚠ NO PROSE IS DRAFTED HERE. Same standard as `OUTLINE-01`.**

**⚠⚠ SUPERSEDED — `MAIN_WORK` IS REACHABLE AND HAS BEEN ALL ALONG ON THIS MACHINE.**
This document was written believing `MAIN_WORK` was not present, and that belief was
carried forward from the cloud-container era across a move to the owner's own machine —
where `MAIN_WORK` sits at
`/mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT/MAIN_WORK`. **Its live ledger
runs to `PT-1786`, not `PT-1548`**, so every ruling this document treats as relayed-only
(`PT-1705`, `PT-1744`, `PT-1747`, `PT-1783`) is directly readable. **And `rules/` holds
the authoritative versions of every source this book drafts against.** Marks below that
read `RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)** were measured against `HANDOFF` alone and need re-auditing — at
least 27 of those documents are present in `MAIN_WORK/rules/`.

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

**⚠⚠ WALL 2 IS CLOSED.** `MAIN_WORK/data/books/` exists and is readable: both D&D 3.5
structural references (`PHB`, `DMG`, `MM`), both 5E references (`PHB`, `Equipment
Manual`), the KOTOR Campaign Guide as searchable OCR text (`KOTOR-CG-OCR.txt`), *The New
Essential Guide to Alien Species*, and `Force-Users.pdf`. **"Cite folio and line" is now
possible** — the constraint this outline has carried since its first draft is gone.

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
| **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | Mechanics exist per `WHERE-IS`, **document unreachable from here.** |
| **`PROSE`** | Original prose. Nothing mechanical at stake. |
| **`DRAFTED`** | Player-facing prose **already exists** — revision and placement, not authorship. |
| **⚠ `GAP`** | Needs a mechanic that **does not exist anywhere I can see**, held or unheld. |
| **⚠⚠ `UNPLACED`** | New this round. **The source exists and is marked elsewhere in this document, but the brief does not say which of two or more plausible books it belongs to.** Not a gap — a filing question. |

---

# 1b · ⚠⚠ REQUIRED IN EVERY BOOK — `PT-1813`

**Three elements, every book in this set, present and future. Not optional and not
per-book judgement.**

**1 · The disclaimer**, on **page two or three, before any content**. **Reproduced word for
word** — it may not be paraphrased, shortened, or reworded:

> This is an unofficial, non-commercial fan project. It is not affiliated with, endorsed
> by, or produced by Lucasfilm Ltd., Disney, BioWare, or any rights holder of Star Wars or
> Knights of the Old Republic. All Star Wars trademarks, characters, and copyrighted
> material referenced herein remain the property of their respective owners. This work is
> created by fans, for fans, and is distributed free of charge. No part of it is sold, and
> no revenue is generated from it in any form.

**2 · A sourced bibliography**, **scoped to what that book actually used** — real author and
publisher credit. **Per book, not one project-wide list**; each book's author writes its
own from the sources that book drew on.

**3 · A `[INSERT PERSONAL NOTE HERE]` placeholder**, left **empty**. This is the owner's
own acknowledgment in his own voice. **Mark it clearly and do not draft it.**

**Implemented in all three books that exist:**

| Book | Disclaimer | Bibliography | Personal note |
|---|---|---|---|
| **Galactic Timeline** | ✔ `timeline/00-front-matter.md` | ✔ `timeline/09-bibliography.md` | ✔ |
| **Armory** | ✔ `armory/00-front-matter.md` | ✔ same file — **⚠ covers 11 chapters; revisit when the remaining five land** | ✔ |
| **Player's Handbook** | ✔ `phb/00-front-matter.md` | **⚠ owed** — must be scoped to what the finished book cites, and it is one chapter in | ✔ |

**⚠ Owed by every book drafted from here.** **Verify the disclaimer programmatically rather
than by eye** — copy it from an existing front-matter file and diff it. "Word for word, no
exceptions" is not a thing to satisfy by reading it over.

**The verified/unverified marking is standard practice for every bibliography**, ruled.

**One practice worth carrying forward from the Timeline's bibliography:** mark each entry
**verified** or **unverified** against a source actually held. A credit page names real
people who did the work, and mixing checked and assumed credit silently is the one place in
a book where that failure is least acceptable.

---

# 1c · ⚠ FLAG RESOLUTION — STANDING PRACTICE, EVERY BOOK

**When a flag raised in a chapter is later resolved — by a ruling, by a fix at source, or
by the author — leave the flag where it is and APPEND how and when it resolved.** Mark it
**✔**. **Never silently delete a flag, and never rewrite it to read as though it had never
been raised.**

**Why:** the same reason the ruling ledger preserves its corrections rather than editing
history away. A flag that vanishes takes with it the evidence that anyone checked.

**The failure this prevents was found in this project's own work.** The Galactic Timeline's
consistency pass found **eight flags describing defects that had already been fixed** —
several fixed at source by MAIN after the chapters were written. A reader would have been
sent hunting bugs that no longer existed, and would have trusted the chapter over the
corpus. **That is `PT-961`'s shape** — *"when a ruling changes a table, it does not change
the sentences that read from it"* — **and flags turn out to be a table like any other.**

---

# 2 · THE EIGHT BOOKS

---

## CORE

### BOOK ONE — PLAYER'S HANDBOOK

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | What this game is | **`PROSE`** | Mine. Dice conventions `DICE-01` — **present in `MAIN_WORK/playtest/` (`AUDIT-01`)** |
| — | Making a character — creation order | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `CHARACTER-CREATION-01` (`C25`) absent. Partial recovery: `SPECIES-CHAPTER-v2:131` — *"SPECIES BEFORE ANYTHING ELSE, `PT-594`"* |
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
| — | Influence | **`RULED` — partly. **⚠ Present in `MAIN_WORK` except `RCR-REPUTATION-FINDINGS`, which is Library-held (`AUDIT-01`)**** | `INFLUENCE-01` (`D-AH`); `PORT-02-v2 §5`; `RCR-REPUTATION-FINDINGS` |
| — | Factions | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `FACTIONS-01` — SETTLED for both packages |
| — | Awarding experience | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `EXPERIENCE-01` — SETTLED, `PT-660` |
| — | Encounter design | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)** — ⚠⚠ UNPLACED, see note** | `ENCOUNTER-01` (`C22-CREATURES`). **⚠ Filed by the Library under creatures, not engine or GM tools — the same shelf as every `BEASTS-*` document — which weakly argues for Threat Database instead. Named explicitly under Holocron in the brief, so kept here, but the Library's own filing disagrees and that disagreement is worth knowing.** **⚠⚠ AND `ENCOUNTER-01 §5c` depends on an `openness` field that `PT-1051` found on ZERO of 298 swept world records — `D-OPEN-01` defines it, no world record carries it. A live defect in the source this chapter would draft against, not mine to fix, cited so it is not rediscovered.** |
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
| — | Hostile beasts — combat stats | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `BEASTS-ATTACKS-01`, `BEASTS-LEVELS-01`, `BEASTS-SKILLS-01`, `BEASTS-FEATS-01` |
| — | Beast quick reference | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `BEASTS-REFERENCE-01` |
| — | Beast stat entries | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)** — ⚠⚠ ONE SOURCE, TWO BOOKS** | `BEASTS-ENTRIES-01` — *"27 creature companions... type, size, traits and a defining ability."* **Its fields mix combat data (defining ability) with lore data (type, size, traits) in one document. The new split sends lore to Species Compendium and stats here — meaning this single source needs restructuring across two books when drafted, not a copy into either.** |
| — | How adversaries behave — ⚠⚠ UNPLACED, see Book Two | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `GROUND-AI-01`, `SPACE-AI-01` — four faction doctrines, `PT-806`/`807`. Placed here as the more natural fit for a hostile-facing book; not named in either book's brief explicitly |
| — | Running a creature — ⚠⚠ UNPLACED, see Book Two | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `GM-CREATURES-01`. Candidate for either this book or Holocron's procedural material; not named in either brief |

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
| — | Currency and trade | **⚠ `GAP` — both original citations were wrong** | Checked while drafting Armory's Chapter Eleven: `D-CURRENCY-01` is a corpus-governance ruling for which Atlas world-record source is authoritative, not a currency ruling; `D-URKUPP-01` is a species-eligibility reconciliation (the Dashade homeworld question), also unrelated. Neither says anything about currency or trade. **No confirmed source for this row's actual subject** — credits-as-currency itself is `STARTING-EQUIPMENT-01`'s territory, already placed in Book One/Two, but *trade between worlds* specifically has no citation I can find |

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

**⚠⚠ RE-MEASURED AND RE-MARKED, and the earlier header was wrong twice over.** *"Nothing
for this book is in this repository"* was carried unexamined from `OUTLINE-01`. **Most of
this book's real content is held**, at rank 2, in `MAIN_WORK/data/books/KOTOR-CG-OCR.txt`
— a searchable 21,339-line OCR of the Campaign Guide with per-page markers. The eight-
chapter structure below supersedes the seven rows this table used to carry.

**⚠ Folio convention for every Campaign Guide citation in this book: the OCR's
`=== PAGE n ===` markers are NOT printed folios.** Pages 1–3 are cover, title and credits,
which carry no printed number. **Printed folio = OCR marker − 3**, verified exactly
against two existing corpus citations (`D-W42`'s *"Timeline p.113"*; this table's own
*"pp. 112–113"*).

| # | Chapter | Mark | Source |
|---|---|---|---|
| 1 | What this timeline is, and isn't | **`DRAFTED`** | `CANON-01-v2 §§2, 2.1, 2.2, 4, 10.0`; `METHOD-RECORD-01 §§2–3`; `WORLDS-REGISTER-01` `D-W3`, `D-W32`, `D-W42`. **⚠ Corrected: this row previously cited `CANON-01-v2 §3.4`, which is *"`requires` is a predicate, not a list"* — the canon ledger's predicate, nothing to do with the timeline** |
| 2 | Deep history | **`DRAFTED`** — **⚠ previously marked `RULED · NOT HELD`, which understated what is held** | **Campaign Guide at rank 2, ff. 16, 110, 145** — Adas by name, the ~28,000 BBY unification, the Rakatan invasion and its outcome, the dark side as the Infinite Empire's bequest, the Hundred-Year Darkness exiles, Ajunta Pall, Jen'jidai/Jen'ari, Tund, the interbreeding. `METHOD-RECORD-01 §3` for the standard. `SPECIES-CHAPTER-v2` + `D-Q` for the Flesh Raider/Rakata relation. ⚠ Plague, Tython, Corbos at rank 6, relayed |
| 3 | The Tales of the Jedi era | **`DRAFTED`** | **Campaign Guide f. 5 (war narrative) and ff. 112–113 (dated timeline)**; `EVENTS-01`. ⚠ Same-rank conflict between the two CG sections — `PT-946` |
| 4 | The Mandalorian Wars | **`DRAFTED`** | **Campaign Guide "The Mandalorian Wars" f. 5 (3,965–3,960 BBY) and ff. 112–113**; `EVENTS-01` incl. the Mandalorian correction (`PT-675`, `PT-681`). **⚠ Should also absorb the orphaned Restoration Period, f. 5 (3,995–3,966 BBY) — see the era-alignment note below** |
| 5 | The Jedi Civil War | **`DRAFTED`** | **Campaign Guide "The Jedi Civil War" f. 6 (3,959–3,956 BBY) and f. 113**; KOTOR 1 at rank 1; `EVENTS-01` |
| 6 | The Sith Lords' return | **`DRAFTED`** | **Campaign Guide "The Dark Wars" f. 6 (3,955–3,951 BBY) and f. 113**; KOTOR 2 at rank 1; `EVENTS-01` |
| 7 | The Reconstruction | **`DRAFTED`** — ⚠ scope settled by sweep, not assumed | **⚠⚠ SWEEP RESULT: the Campaign Guide contains NO post-3,950 BBY content anywhere in its 21,339 lines** — zero instances of any date 3,949–3,900 BBY, and every era-divided section (factions ff. 146/168, starships f. 143) stops at the Dark Wars. **So the chapter is the reconstruction as the REPUBLIC-SIDE VIEW of 3,956–3,950 BBY** — the same window as Chapter Six, from the other side. Sources: G0-T0 f. 210, Bao-Dur f. 176, Telos IV f. 123 (⚠ known-defective per `D-W33`), Atris f. 141, the era-divided Republic sections f. 168, `EVENTS-01 §1`'s 3,955 G0-T0 row (`PT-604`). **⚠ Corrected: the 3,985 BBY Coruscant Financial Exchange act belongs to the *Restoration Period*, NOT here** — two different recoveries, and `TO-MAIN-44` conflated them |
| 8 | The unwritten future | **`DRAFTED`** | Mine. No fixed roster by design (`PT-1802`). Epigraph from the CG at f. 6; `CANON-01-v2 §§2, 5–5.1`; `WORLDS-REGISTER-01`'s improvisation ruling |

**⚠ Supporting documents still `NOT HELD`** — Library-held, confirmed absent from
`MAIN_WORK` (`AUDIT-01`), and none of them blocks a chapter above:
`RULING-SWTOR-DEEP-HISTORY`, `ERA-VITIATE-01`, `D-VIT-01`, `TEMPORAL-SWEEP-TOTJ-*`,
`TEMPORAL-SWEEP-LEGENDS-01`, `TEMPORAL-ENUM-01`, `D-REVAN-04`, `GAZETTEER-PART-D`.
**`GAZETTEER-PART-D` is specifically a transcription of the Campaign Guide timeline at
pp. 112–113, which is now readable directly at rank 2** — so its absence costs nothing.

**Structure, `PT-1802`:** Chapters 3–7 each carry a short framing paragraph, the events
narrative, and a **Major Figures** section that cross-references back into the narrative
rather than re-telling it. **Not applied to Chapter 2** (the deep-history standard is
evocative rather than tracked, and a roster would fight it) **or Chapter 8** (no fixed
roster exists by design).

**Ranks 7 and 8, `PT-1800`:** rank 7 is reserved for `D-W32`'s local Wookieepedia
extension (worlds register only); *Jedi vs. Sith* and *The New Essential Guide to Alien
Species* sit at rank 8 — descriptive lore only, never mechanics, nothing after 3,956 BBY.

**⚠⚠ ERA ALIGNMENT — the Campaign Guide has five eras, this book has five era chapters,
and they do not line up.** Found while drafting Chapter Three; full detail at that
chapter's Flag 4.

| Campaign Guide era, ff. 5–6 | Years | Chapter |
|---|---|---|
| The Great Sith War | 4,000–3,996 BBY | 3 ✔ |
| **The Restoration Period** | **3,995–3,966 BBY** | **⚠ orphaned** |
| The Mandalorian Wars | 3,965–3,960 BBY | 4 ✔ |
| The Jedi Civil War | 3,959–3,956 BBY | 5 ✔ |
| The Dark Wars | 3,955–3,951 BBY | 6 ✔ |
| *(no CG era exists)* | 3,950 BBY onward | 7 |

**Recommended, not decided:** the Restoration Period opens **Chapter Four** — it is that
war's direct set-up, containing the Republic's economic rebuild and the Mandalorians
rearming in secret, and reads as an opening movement rather than a chapter. **Owner's
call.**

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
| — | Beast encyclopedia — ecology, habitat | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `BEASTS-NATURE-01` (temperament) is the closest existing candidate; the lore-half of `BEASTS-ENTRIES-01` (see Book Three) also belongs here once split |

---

### BOOK SEVEN — ARMORY

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Weapon damage and the defence formula | **`DRAFTED`** | `EQUIPMENT-01`. `PT-339`/`340`/`341`/`169`. **Text at `BOOKS/armory/01-weapon-damage-and-defence-formula.md`, approved by MAIN** |
| — | Melee weapons | **`DRAFTED` — full catalogue** | `ITEMS-01`, both games, `PT-342` applied. Eleven base-type families, 67 entries, Base/Advanced split by tier. **⚠ Four weapons still carry the pre-`PT-1747` Vibrosword die; three written as `1d12`, `GenoHaradan Poison Blade` flagged pending a `BaseItem` check.** **Text at `BOOKS/armory/02-melee-weapons.md`** |
| — | Ranged weapons | **`DRAFTED` — base table current, catalogue pending** | Drafted against `MAIN_WORK/rules/` (authoritative). 14 base weapons incl. `Heavy Blaster`, `Marksman Rifle`, `Sniper Rifle` (`PT-1783`), perception extension (`PT-1782`), `Hold Out Blaster` naming (`PT-1477`). **⚠ `Sniper Rifle` is ruled but has no `ITEMS-01` row.** 94 pistols + 78 rifles catalogue is the next increment. **Text at `BOOKS/armory/03-ranged-weapons.md`** |
| — | Lightsabers | **`DRAFTED`** | `EQUIPMENT-01 §4b`, K1 standard-Lightsaber die corrected against raw `data/k1_baseitems.2da` (2d8, not the stated 2d10); crystals `PT-345`. **Text at `BOOKS/armory/04-lightsabers.md`** |
| — | Armour | **`DRAFTED`** | `ITEMS-02` — 173 items, six categories. Defence formula and droid plating taught in Chapter One, pointed back to rather than restated. **Text at `BOOKS/armory/05-armour.md`** |
| — | Upgrades and the upgrade tree | **`DRAFTED`** | `ITEMS-03` — 164; `ITEMS-09`, refiled `PT-781`. Confirms and refines Chapter One's Bonded Plates/Flexible Underlay citations; resolves what the Bacca's/Cassus Fett's unique-weapon variants actually are. **Text at `BOOKS/armory/06-upgrades-and-the-upgrade-tree.md`** |
| — | Droid equipment | **`DRAFTED`** | `ITEMS-04` — 135 items, eight categories. **Text at `BOOKS/armory/07-droid-equipment.md`. ⚠ Proposed split from the combined row below into four chapters — not yet confirmed** |
| — | Worn gear | **`DRAFTED`** | `ITEMS-05` — 241 items, five categories, two mixing authored content with extracted. **Text at `BOOKS/armory/08-worn-gear.md`** |
| — | Usable items | **`DRAFTED`** | `ITEMS-06` — 58 items. Medpac healing values are `PT-1`'s deliberate replacement of the source game's own WIS/skill-scaled mechanic. **Text at `BOOKS/armory/09-usable-items.md`** |
| — | Quest and miscellaneous items | **`DRAFTED`** | `ITEMS-07` + `ITEMS-08`. Two authored categories, one (`boots`) inventing an equipment slot KOTOR never had (`PT-690`). **Text at `BOOKS/armory/10-quest-and-miscellaneous-items.md`** |
| — | Tiers, pricing, availability | **`DRAFTED`** | `PT-308` (loot tiers — agreed in concept, character-vs-area gate undecided), `PT-327` (unique items), `PT-384` (feat remap). Currency is `STARTING-EQUIPMENT-01`, not `D-CURRENCY-01` — see note. **Text at `BOOKS/armory/11-tiers-pricing-and-availability.md`** |
| — | The weapon matrix / crafting | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `WEAPON-MATRIX-01`; `CRAFTING-01` |
| — | Loot | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)** — see Book Two's UNPLACED list** | `LOOT-01` |
| — | Starships / space combat | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `STARSHIPS-01` — 21 hulls; `SPACE-COMBAT-01`, derives from `MOUNTED-COMBAT-01` |
| — | **Droid construction and upgrade** | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)** — moved here per the brief** | `DROID-CONSTRUCTION-01`, `DROIDS-UPGRADE-01` (both `C21`). Droid *items* are held — `ITEMS-04` |

---

### BOOK EIGHT — ADVANCED PLAYER'S GUIDE *(the after-you've-played book)*

| # | Chapter | Mark | Source and ruling |
|---|---|---|---|
| — | Prestige classes — nineteen | **⚠ `GAP`, unchanged** | `CLASS-ROSTER-01 §3`/`§4` for the roster; entry rules `PT-573`, droids `PT-577`. `MANIFEST`: *"no lists anywhere... do not synthesise."* Skill lists exist (`SKILLS-01 §9.2c`, `PT-1322`) — the gap is class *features*, all nineteen |
| — | Deeper multiclassing — entry requirements | **`RULED` for 11/19, `NOT WRITTEN` for 8/19 — ⚠⚠ SOURCE CONTRADICTS ITSELF** | `CLASS-ROSTER-01 §475`: *"THREE ENTRY REQUIREMENTS TESTED... `PT-628`."* `MULTICLASS-01 §5` calls these requirements *"the real brake"*; that same document's own `§6` calls them *"NOT WRITTEN."* Eleven are: `Commando`, `Gunslinger`, `Shadow Hunter`, `Juggernaut`, and seven more per `§6`'s count. **Eight of nineteen remain genuinely unwritten — not all nineteen, as a first read of `§6` alone would suggest.** Whether Book One's *base* multiclassing ruling also moves here or stays split — flagged in Book One, not resolved here either |
| — | Beast ownership — obedience | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `BEASTS-OBEDIENCE-01` — per-beast obedience DCs |
| — | Beast ownership — upkeep | **⚠ `GAP`, and a sharper one than "not held"** | The word `upkeep` returns **zero hits** anywhere in this repository's rulings ledger or the Library's own index (`WHERE-IS.md`). Every other `NOT HELD` mark in this document means *"indexed elsewhere, unreachable from here"* — this one may mean the mechanic has not been authored **anywhere**, which is a different, sharper kind of gap |
| — | Beast Master — the class | **⚠ `GAP`, cross-references the Prestige chapter above** | `Beast Master` is one of the nineteen prestige classes with no features written. Not a second, separate gap — the same one, reached from a different chapter |
| — | Beasts a player can take | **`RULED` — **present in `MAIN_WORK/rules/` (`AUDIT-01`)**** | `BEASTS-PLAYER-01` |

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
