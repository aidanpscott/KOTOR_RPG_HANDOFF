# STUDY 02 — DEFINITION LAYER — RECORDS

Two format records (2DA, TLK) and six table records, all on the template from
`STUDY/README.md`.

Everything was read from the shipped files of both games with a parser written
for this pass (`twoda2.py`, `d6.py`). **209 K1 and 424 K2 tables parsed with
zero failures**, so the format claims below rest on complete coverage, not
sampling. Where something is inferred, the line says so.

---

## ⚠ Correction to batch 1, F09 / RIM record — resolved before anything else

Batch 1 reported that K1's `rims/` copies of 13 tables differ from the BIF
copies "only in the column delimiter — tab versus null", and framed this as
**two shipped serialisations**. Having now parsed both forms:

**It is one format, read with a tolerant delimiter.** Parsing the tab form and
the NUL form of the same table yields **identical column lists, identical row
counts, and identical cell values** — verified on all 13.

Two further corrections to that batch-1 line:

1. **The delimiter is a per-file property, not a per-layer one.** Batch 1 implied
   "BIF uses tab, rims uses NUL". In fact the BIF layer of **both** games is
   100% tab-delimited for multi-column tables, and only K1's `rims/` carries
   NUL-delimited copies — 13 distinct tables appearing in both `global.rim` and
   `miniglobal.rim`, so 26 occurrences.
2. **A first pass here mis-flagged 12 K1 and 52 K2 BIF tables as "NUL".** Those
   are all **single-column** tables, where the header block has no separator to
   observe — there is nothing between one column name and the terminator. Only
   multi-column tables can carry the distinction.

The substance of F09 survives — two byte-different copies of 13 core tables ship
with no declared authority — but "two serialisations" overstated it. Recorded in
`FLAWS.md` as an amendment.

**Every sample in this batch is labelled with the variant it came from.**

---

## 2DA — the rules table

**WHAT IT IS**
A spreadsheet of game rules — one row per thing, one column per property — in a
compiled binary form.

**CONTAINER**
BIF (via `chitin.key`) in both games. Also K1's `rims/` and `patch.erf`, and the
`Override` folder. **Never inside a module** — see SCOPE.

**STRUCTURE**
Binary, magic `2DA V2.b\n`. Layout, verified against shipped files:

```
"2DA V2.b\n"
column headers    delimited strings, terminated by an empty one
row count         uint32
row labels        delimited strings, one per row
cell offsets      rowCount * colCount uint16, into the data block
data block size   uint16
data block        NUL-terminated strings
```

**No text-format 2DA ships anywhere.** Searched the BIF layer, `rims/`,
`patch.erf`, `Override` and every module archive in both games — 633 tables,
all `2DA V2.b`, zero text-form files, zero parse failures.

**Cells are untyped.** Every cell is a string in the data block; the reader
coerces to int, float or resref by context. Nothing in the file says a column is
numeric. The same column can therefore hold `"0"`, `"-1"` and `"c_drdastro"`
without the format objecting.

**Empty, zero and `****`:**
- Empty is the **empty string** — 39,034 cells in K1, 66,430 in K2.
- Zero is the **one-character string `"0"`**, which is an ordinary value.
  So empty and zero **are** distinguishable.
- **`****` does not exist in the binary form.** Zero occurrences across
  111,521 K1 cells and 211,281 K2 cells. It is a convention of the text source
  the compiler turns into an empty string, so **empty and `****` are the same
  thing in shipped data and cannot be told apart.**

**String interning.** Cells that hold the same text share one data-block offset.
169 of 205 K1 tables and 253 of 419 K2 tables reuse offsets — K1's `acbonus`
has 126 cells pointing at just 4 distinct strings.

**Row addressing is by both index and label, and the label is usually
redundant.** Row labels are exactly the decimal row index in **189 of 209** K1
tables and **367 of 424** K2 tables. The rest use meaningful labels.

**REFERENCES OUT**
Six distinct mechanisms — enumerated in full in `README.md` §2. In brief:
row index into another table; StrRef into the TLK; ResRef naming a resource;
a string naming another 2DA; and two positional mechanisms where identity *is*
position.

**REFERENCED BY**
The engine, by table name: **107 of 209** K1 and **104 of 424** K2 table names
appear as literal strings in the binary. Also by other 2DAs, and by blueprint
records (a UTC's `FeatList.Feat` is a `feat.2da` row index).

**SCOPE**
**Game-global, without exception.** Searched every module archive in both games
— 398 K1 files and 246 K2 files — and found **zero 2DA resources**. There is no
module-local rules table anywhere. See `FLAWS.md` F18.

**AUTHORED BY**
Hand-edited as text, then compiled. The `****` convention and the tab/NUL
delimiter drift are both artifacts of that pipeline.

**READ WHEN**
Game start for engine-named tables; on demand for the rest. Inferred from the
literal names in the binary and from `rims/global.rim` bundling 153 tables as a
startup set — not confirmed against a running process.

**K1 vs K2**
- **209 → 424 tables.** 195 shared, 14 K1-only, 229 K2-only.
- **76 shared tables changed shape.** Largest column growth: `feat` +31,
  `xptable` +30, `appearance` +14, `featgain` +14, `skills` +14.
- K2-only is dominated by `pack*` package tables — 155 of the 229.
- Delimiter drift is K1-only.

**SAMPLES**
| # | table | from | variant | why chosen |
|---|---|---|---|---|
| 1 | `cls_atk_1` | K2 `data/2da.bif` | V2.b, single column | minimal — 50 rows × 1 column, row index *is* the level |
| 2 | `appearance` | K1 `data/2da.bif` | **V2.b tab** | large — 509 rows × 80 cols, 98,610 b |
| 3 | `appearance` | K1 `rims/global.rim` | **V2.b NUL** | the same table, other delimiter, identical parse |
| 4 | `acbonus` | K1 `data/2da.bif` | V2.b tab | interning — 126 cells, 4 distinct strings |
| 5 | `debugvariables` | K2 `data/2da.bif` | V2.b tab | oddity — **every row label is `1`**; duplicate labels ship |

**UNKNOWN**
Whether the engine's reader accepts both delimiters by design or whether only
one of the two copies of those 13 tables is ever loaded. Both files ship and
both parse; which one wins is the batch-1 F02 precedence question, still open.

---

## TLK — the string table

**WHAT IT IS**
Every piece of display text in the game, in one numbered list.

**CONTAINER**
Not contained — a loose file at the install root, `dialog.tlk`.

**STRUCTURE**
Binary, magic `TLK `, version `V3.0`.

```
"TLK ", "V3.0", LanguageID u32, StringCount u32, StringEntriesOffset u32
then StringCount entries of 40 bytes:
    Flags u32, SoundResRef char[16], VolumeVariance u32, PitchVariance u32,
    OffsetToString u32, StringSize u32, SoundLength float
then the string data block
```

Flag bits: `1` TEXT_PRESENT, `2` SND_PRESENT, `4` SNDLENGTH_PRESENT.

Observed flag values:

```
K1   7: 48,663    6: 398      32768: 307      1: 1
K2   7: 74,039    6: 513      32768: 61,777
```

**An entry carries more than text — but almost all of it is dead.**
- **SoundResRef** is live: K1 carries one on **32,874 of 49,369** entries
  (66.6%); K2 on only **1,608 of 136,329** (1.2%).
- **VolumeVariance is 0 in every entry of both games.**
- **PitchVariance is 0 in every entry of both games.**
- **SoundLength is 0.0 in every entry of both games** — despite bit 4
  (SNDLENGTH_PRESENT) being set on 48,663 K1 entries and 74,039 K2 entries.
- Flag `6` means SND+SNDLENGTH with the TEXT bit clear — entries with a sound
  and no text.
- Flag `32768` (0x8000) is outside the three documented bits. Every sampled
  instance has string size 0 and no sound resref. **In K2 it covers 61,777
  entries — 45% of the table.** Meaning not established.

**REFERENCES OUT**
To a sound resource **by ResRef**. Nothing else.

**REFERENCED BY**
Everything, **by StrRef — a bare integer index**. 103 K1 and 142 K2 2DA columns
hold TLK-ranged integers; every GFF blueprint's name and description field is a
StrRef; dialogue nodes are StrRefs.

**SCOPE**
**Game-global. One file, one namespace, no partitioning.**

**AUTHORED BY**
Generated from a localisation pipeline. Never hand-edited in the shipped form.

**READ WHEN**
Opened at start and read by offset on demand. Inferred from the header design
(a fixed-stride entry array plus an offset into a data block, needing no full
parse); residency not confirmed.

**K1 vs K2**
| | K1 | K2 |
|---|---|---|
| entries | **49,369** | **136,329** |
| file size | 5,411,927 b | 10,162,930 b |
| data offset | 1,974,780 | 5,453,180 |
| LanguageID | 0 | 0 |
| entries with a sound | 32,874 (66.6%) | 1,608 (1.2%) |
| flag 0x8000 | 307 | 61,777 (45%) |

The sound-resref collapse from 67% to 1% is the largest single difference.
K2 moved voice association out of the TLK; **where it went was not established
in this batch** — that is batch 5 (DLG) territory.

**SAMPLES**
| # | entry | game | why chosen |
|---|---|---|---|
| 1 | strref 0 | both | minimal — the first entry |
| 2 | strref 31479, sound `_globebast06862_`, flag 6 | K1 | oddity — a sound with no text |
| 3 | strref 37458, sound `n_genwook_grts1`, flag 6 | K2 | the K2 equivalent |
| 4 | strref 206 / 207, flag 32768, size 0 | K2 | the unexplained flag, 45% of the table |
| 5 | strref 42258 | K2 | ordinary flag-7 entry with text and a sound |

**UNKNOWN**
What flag `0x8000` means. It is not one of the three documented bits, it is set
on 45% of K2's table, and every sampled entry is empty. Would need a
disassembly or the running game.

**Is a second TLK supported?** **No evidence of one.** Scope of that negative:
searched both install trees filesystem-wide for `*.tlk` (exactly one hit each —
`dialog.tlk`); searched both binaries for `.tlk`, `dialogf`, `customtlk`,
`usertlk`, `TalkTable` and `TLK` literals. K1 yields only `TLK `, `Tlk`, `tlk`.
K2 adds the class names `9CTlkTable` and `11CSWTlkTable` — a base and a
Star-Wars subclass, which shows a table *abstraction* exists but not that a
second *file* can be loaded. **No female/alternate TLK, no user TLK, and no
override-TLK mechanism found.** I did not disassemble the loader.

---

## classes.2da — the character classes

**WHAT IT IS** The list of classes a character can have levels in.

**CONTAINER** BIF, `data/2da.bif`, both games. **V2.b tab.**

**STRUCTURE** K1 **9 rows × 49 cols**; K2 **17 rows × 29 cols**. K2 has *more
rows and fewer columns* — the only major table where columns shrank.

**REFERENCES OUT**
- To other 2DAs **by name, as a string in a cell** — `attackbonustable`,
  `savingthrowtable`, `skillstable`, `featstable` and similar columns hold table
  names like `CLS_ATK_1`, `CLS_ST_JEDI_G`. This is the "a table names a table"
  mechanism.
- To the TLK **by StrRef** for display name and description.

**REFERENCED BY**
- The creature record's `ClassList.Class` — **by row index**.
- **Every per-class column family in other tables — by column-name prefix.**
  `skills.2da`, `feat.2da`, `featgain.2da` in both games, plus `acbonus.2da` and
  `classpowergain.2da` in K2, carry one column family per class, keyed on a
  three-letter abbreviation (`sol_`, `scd_`, `jgd_`…) that appears **nowhere in
  classes.2da itself**. The link is a naming convention, not a reference.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited.

**READ WHEN** Start — `classes` is a literal in both binaries.

**K1 vs K2** 9 → 17 rows. K1: Soldier, Scout, Scoundrel, JediGuardian,
JediConsular, JediSentinel, CombatDroid, ExpertDroid, Minion. K2 adds
TechSpecialist, **`BountyHunter(CUT!!!)`**, JediWeaponmaster, JediMaster,
JediWatchman, SithMarauder, SithLord, SithAssassin.

**SAMPLES**
| # | row | game | why |
|---|---|---|---|
| 1 | 0 `Soldier` | both | the ordinary case |
| 2 | 8 `Minion` | both | a non-player class in the player table |
| 3 | 10 `BountyHunter(CUT!!!)` | K2 | oddity — a cut class shipped in place, label and all, holding a row index everything downstream counts past |
| 4 | 3 `JediGuardian` | both | names `CLS_ATK_1` / `CLS_ST_JEDI_G` by string |

**UNKNOWN** Where the three-letter class abbreviations are defined. They are not
a column of `classes.2da`; searched all 49 K1 and 29 K2 columns. They may be
compiled into the engine or derived by convention — not established.

---

## skills.2da — the skills

**WHAT IT IS** The eight skills, and per class whether each is a class skill and
how strongly it is recommended.

**CONTAINER** BIF, `data/2da.bif`. **V2.b tab.**

**STRUCTURE** **8 rows in both games.** K1 30 cols, K2 44 cols.
Of those, **16 of 30 (K1) and 30 of 44 (K2) are per-class** — two per class
(`<cls>_class`, `<cls>_reco`).

**REFERENCES OUT** TLK by StrRef for name and description; an icon by ResRef.

**REFERENCED BY**
- **The creature record, positionally.** `SkillList` is a fixed 8-entry array
  where each entry holds only a `Rank` — no skill id. **Row index is the only
  identity a skill has.**
- The script API, by `SKILL_*` constants 0–7 plus `SKILL_MAX_SKILLS = 8`.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited.

**READ WHEN** Start.

**K1 vs K2** **Rows unchanged at 8. Columns +14**, entirely from the class count
going 9 → 17. K2 also adds `AdjustCreatureSkills` and `GetSkillRankBase` to the
script API. `patch.erf` retunes K1's copy (1,218 → 1,220 bytes) **without
changing the row count**.

**SAMPLES**
| # | row | game | why |
|---|---|---|---|
| 1 | 0 Computer Use | both | ordinary |
| 2 | 4 Persuade | K2 | `tec_reco` blank — recommendation absent where the class cannot use it |
| 3 | 2 Stealth | K2 | `drx_reco` and `drc_reco` both blank — droid classes |
| 4 | — (the table) | K1 patch.erf | oddity — the official patch edits values but adds no row |

**UNKNOWN** Nothing outstanding. This table is small and fully read.

---

## feat.2da — the feats

**WHAT IT IS** Every feat, its prerequisites, and per class whether it is
available, auto-granted, or recommended.

**CONTAINER** BIF, `data/2da.bif`. **V2.b tab.**

**STRUCTURE** K1 **125 rows × 60 cols**; K2 **245 rows × 91 cols**.
Per-class columns: **24 of 60 (K1)**, **48 of 91 (K2)** — three per class in K1
(`_list`, `_granted`, `_recom`), four for Jedi classes in K2 (adds
`_pc_granted`).

Three distinct per-class semantics, all in the column name:
- `<cls>_list` — availability: `1` selectable, `3` special, `4` unavailable
- `<cls>_granted` — the **level** at which it is auto-granted, `-1` never
- `<cls>_recom` — a **priority rank**, blank if not recommended

**REFERENCES OUT** TLK by StrRef; icon by ResRef; `prereqfeat1/2`,
`orreqfeat0..4` and `successor` **by row index into itself**; `masterfeat` by
row index into `masterfeats.2da`; `reqskill` by row index into `skills.2da`.

**REFERENCED BY** The creature record's `FeatList.Feat` — **by explicit row
index carried in the record**, unlike skills.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited.

**READ WHEN** Start — `feat` is a literal in the K1 binary.

**K1 vs K2** Rows 125 → 245. Columns 60 → 91, **the largest column growth of any
shared table (+31)**, all of it the class count.

**SAMPLES**
| # | row | game | why |
|---|---|---|---|
| 1 | `RAPID_SHOT` | K2 | ordinary — `sol_recom=1`, the soldier's top pick |
| 2 | `TOUGHNESS` | K2 | rank 1 for JediGuardian; shows ranks are per-class |
| 3 | Jedi Guardian column | K2 | oddity — ranks run 1..26 with **12 missing**; a consumer cannot assume contiguity |
| 4 | scoundrel `_granted` | K2 | grants at levels 1,3,5,7,9,11,13,15,17,19 — the sneak-attack ladder as a column of levels |

**UNKNOWN** Whether the engine reads rows past the shipped count. The record
format carries explicit ids, so it *could*; bounds-checking is not observable
from files. Needs the running game.

---

## spells.2da — the Force powers

**WHAT IT IS** Every Force power and its targeting, cost and effects.

**CONTAINER** BIF, `data/2da.bif`. **V2.b tab.**

**STRUCTURE** K1 **132 rows × 53 cols**; K2 **282 rows × 60 cols**.
**No per-class columns** — availability is expressed elsewhere, unlike feats.

**REFERENCES OUT** TLK by StrRef; icon and impact-script by ResRef;
`iprp_spells.2da` by row index.

**REFERENCED BY** The creature record's `ClassList[].KnownList0[].Spell` — **by
explicit row index**, alongside `SpellMetaMagic` and `SpellFlags`.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited.

**READ WHEN** Start.

**K1 vs K2** Rows 132 → 282 (+150). Columns 53 → 60. K1's install carries a
**TSLPatcher-installed override copy** — 132 rows in both shipped and override,
identical column set, so that mod **retunes without extending**.

**SAMPLES**
| # | row | game | why |
|---|---|---|---|
| 1 | 13 | K2 | ordinary, on Vrook's known list |
| 2 | 162 | K2 | large — a K2-only power, past K1's whole range |
| 3 | the table | K1 `Override/spells.2da` | oddity — an installed mod, same shape as shipped |
| 4 | the table | K1 `rims/global.rim` | the second shipped copy |

**UNKNOWN** Same bounds question as `feat.2da`.

---

## appearance.2da — the creature appearance catalogue

**WHAT IT IS** Every creature body: which model, which textures, how it moves,
what it sounds like.

**CONTAINER** BIF `data/2da.bif` (**V2.b tab**) *and* K1 `rims/global.rim` and
`miniglobal.rim` (**V2.b NUL**). One of the 13 double-shipped tables.

**STRUCTURE** K1 **509 rows × 80 cols**; K2 **671 rows × 94 cols**. 98,610 bytes
in K1 — the largest 2DA in either game.

**REFERENCES OUT** Heavy ResRef use — `modela`…`modeln`, `texa`…`texn`, race
textures, all naming MDL/texture resources by string. `soundapptype` by row
index into `appearancesndset.2da`; `racetex` and `normalhead`/`backuphead` by
row index into `heads.2da`; TLK by StrRef for the display name.

**REFERENCED BY** The creature record's `Appearance_Type` — **by row index**.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited, and clearly generated in part — the model/texture
column families run to fourteen letters.

**READ WHEN** Start — `appearance` is a literal in the K1 binary.

**K1 vs K2** 509 → 671 rows, 80 → 94 cols.

**SAMPLES**
| # | instance | from | variant | why |
|---|---|---|---|---|
| 1 | the table | K1 `data/2da.bif` | **tab** | the reference copy |
| 2 | the table | K1 `rims/global.rim` | **NUL** | byte-different, parses identically — the F09 case |
| 3 | the table | K1 `rims/miniglobal.rim` | **NUL** | a third copy of the same bytes |
| 4 | the table | K2 `data/2da.bif` | tab | 671 rows, no second copy anywhere |

**UNKNOWN** Which of the three K1 copies the engine actually loads. Open under
batch-1 F02.

---

## repute.2da — the faction relationship matrix

*Included as the surprise. It is the clearest positional-identity case found
outside the skill array.*

**WHAT IT IS** How every faction feels about every other faction.

**CONTAINER** BIF, `data/2da.bif`. **V2.b tab.**

**STRUCTURE** K1 **21 rows × 21 cols**; K2 **24 rows × 24 cols**. It grows
**square** — K2 added exactly three rows and three columns.

The row labels and the column names are **the same faction list, in the same
order**:

```
rows  Player  Hostile_1  Friendly_1  Hostile_2  Friendly_2  Neutral  Insane …
cols  label   hostile_1  friendly_1  hostile_2  friendly_2  neutral  insane …
```

The columns are offset by one because column 0 is `label`, which means there are
20 faction columns for 21 faction rows — **the `Player` row has no matching
column.** Relations *to* the player are expressed as the player's own row.

**REFERENCES OUT** Nothing by id. **A faction is identified by its position in
two lists at once.**

**REFERENCED BY** The `REPUTE` record inside a save file (batch 1, SAV record),
and by script faction functions — by row index.

**SCOPE** Game-global.

**AUTHORED BY** Hand-edited.

**READ WHEN** Start, and written into every save.

**K1 vs K2** 21 → 24. K2 adds `Self_Loathing`, `One_On_One`, `PartyPuppet` —
each requiring a row **and** a column, kept in sync by hand.

**SAMPLES**
| # | faction | game | why |
|---|---|---|---|
| 1 | 0 `Player` | both | the asymmetric one — a row with no column |
| 2 | 7 `ptat_Tuskan` | both | oddity — a misspelling shipped as a permanent identifier |
| 3 | 23 `PartyPuppet` | K2 | the newest addition; shows row+column lockstep |
| 4 | 14 `Endar_Spire` | K2 | oddity — a K1 level name still occupying a faction slot in K2 |

**UNKNOWN** Whether the `Player` row/column asymmetry is deliberate or whether
column 0 was repurposed as `label` after the fact. Not determinable from files.
