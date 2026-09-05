# STUDY 02 — DEFINITION LAYER

The rules layer of KOTOR 1 and KOTOR 2 — 2DA tables and the TLK string table.

| file | what it is |
|---|---|
| `RECORDS.md` | 2 format records (2DA, TLK) + 6 table records |
| `README.md` | this file — format, reference mechanisms, census, TLK, global coupling |
| `FLAWS.md` | F13–F23, plus an amendment to batch 1's F09 |
| `NAMING.md` | batch-2 vocabulary additions |

**Method.** All 209 K1 and 424 K2 tables were parsed, with zero failures, using
a parser written for this pass. Claims about "every table" mean every table.
Inferences are marked. Negatives name what was searched.

**Sits on:** `STUDY/01-container/` — the BIF/KEY layer, override precedence
(F02, still open) and the game-global Override folder (F03).

---

## 0 · ⚠ The correction you asked for, resolved first

Batch 1 said the 13 differing `rims/` tables differ "only in the column
delimiter", implying **two shipped serialisations of 2DA**.

**There is one serialisation.** Parsing both forms of all 13 tables gives
identical column lists, identical row counts and identical cell values. The
delimiter between column headers and between row labels is `\t` in one copy and
`\0` in the other; everything after the label block — the offset table, the data
block — is byte-identical.

Two refinements to the batch-1 statement:

- The delimiter is a **per-file** property, not a per-layer one. The BIF layer of
  **both** games is 100% tab-delimited for multi-column tables. Only K1's
  `rims/` carries NUL copies: **13 distinct tables × 2 archives = 26
  occurrences**, in `global.rim` and `miniglobal.rim`.
- A first pass here mis-flagged 12 K1 and 52 K2 BIF tables as NUL. All are
  **single-column** tables, where there is no separator to observe. Only
  multi-column tables carry the distinction.

Every sample in `RECORDS.md` is labelled with its variant.

---

## 1 · The 2DA format

Full record in `RECORDS.md`. The five answers to the batch questions:

**Binary or text?** Binary, always. Magic `2DA V2.b\n`. **No text-form 2DA ships
anywhere** — searched BIF, `rims/`, `patch.erf`, `Override` and every module
archive in both games. 633 tables, zero text files, zero parse failures.

**Header and layout.**
```
"2DA V2.b\n"  ·  column headers (delimited, empty terminator)  ·  row count u32
row labels (delimited)  ·  cell offsets rows×cols u16  ·  data size u16  ·  data
```

**Column typing: there is none.** Every cell is a string in a shared data block.
No column declares a type. The reader coerces by context, which is why the same
mechanism can carry `"0"`, `"-1"`, `"****"`-as-empty and `"c_drdastro"`.

**Empty vs zero vs `****`.**
- Empty is the empty string — 39,034 K1 cells, 66,430 K2.
- Zero is the string `"0"` — an ordinary value. **Empty and zero are
  distinguishable.**
- **`****` never appears in the binary form.** Zero occurrences in 111,521 K1
  and 211,281 K2 cells. It is a text-source convention the compiler collapses to
  empty. **Empty and `****` are therefore indistinguishable in shipped data** —
  see `FLAWS.md` F14.

**Row addressing: both, and the label is usually redundant.** Row labels are
exactly the decimal row index in **189 of 209** K1 and **367 of 424** K2 tables.
Where they differ they are meaningful — `dialogtokens` uses `<abutton>`,
`droiddischarge` uses creature ResRefs, `bindablekeys` uses `key0…`. And they
are not required to be unique: K2's `debugvariables` has **every row label set
to `1`**.

**One efficiency worth noting:** cells sharing a value share a data-block
offset. 169 of 205 K1 tables and 253 of 419 K2 tables intern strings this way;
K1's `acbonus` stores 126 cells as 4 distinct strings.

---

## 2 · ⚠ Reference mechanisms — the batch's main question

**Six distinct mechanisms**, found by classifying every column of every table.

| # | mechanism | K1 cols | K2 cols | example |
|---|---|---|---|---|
| 1 | **row index** into another table | ~463 | ~754 | `feat.prereqfeat1` → `feat.2da` row |
| 2 | **StrRef** — integer into the TLK | 103 | 142 | `racialtypes.name`, `movies.strrefname` |
| 3 | **ResRef** — string naming a resource | 123 | 144 | `traps.resref`, `chargenclothes.itemresref` |
| 4 | **2DA name** — string naming another table | 15 | 14 | `classes.attackbonustable` = `"CLS_ATK_1"` |
| 5 | **row position IS identity** | 53 tables | 102 tables | tables with no `label`/`name` column |
| 6 | **column position IS identity** | 3 tables | 5 tables | per-class column families |

Counts for 1–4 come from automatic classification (numeric range, TLK range,
resolution against the KEY) and are **approximate at the boundaries** —
mechanism 1 is a residual category and will contain some plain numeric values.
Mechanisms 5 and 6 were counted structurally and are exact.

### Where position IS identity — the extensibility walls

This is what the brief asked to enumerate. Already known: **skills**, where the
creature record stores 8 ranks with no skill id. Everything else found:

**A · Tables with no name at all — 53 in K1, 102 in K2.**
Neither a `label` nor a `name` column exists, so a row can only be addressed by
its index. Includes `acbonus`, `cls_atk_1/2/3`, every `cls_st_*`,
`cls_spgn_jedi`, `bindablekeys`, `ambientmusic`, `ambientsound`, `categories`,
`chargenclothes`.

**B · Level-indexed tables — row index *is* the character level.**
`cls_atk_1/2/3` (a single `bab` column), all nine `cls_st_*` saving-throw
tables, `acbonus`, `xptable`, `featgain`, `classpowergain`, `cls_spgn_jedi`.
The level cap is not a value anywhere — **it is the row count of these tables**,
which is why raising it from 20 to 50 in K2 meant growing eight-plus tables in
lockstep (`xptable` 20→50 rows and 22→52 cols; `acbonus` 21→51).

**C · Per-class column families — adding a class changes other tables' schemas.**

```
K1   feat        8 class families,  24 of  60 columns
     featgain    8 class families,  16 of  17 columns
     skills      8 class families,  16 of  30 columns

K2   feat       15 class families,  48 of  91 columns
     featgain   15 class families,  30 of  31 columns
     skills     15 class families,  30 of  44 columns
     acbonus    10 class families,  10 of  13 columns
     classpowergain  9 families,     9 of  10 columns
```

A class is a **row** in `classes.2da` and a **column-name prefix** in five other
tables. The prefix (`sol_`, `jgd_`, `drx_`…) appears nowhere in `classes.2da` —
searched all 49 K1 and 29 K2 columns. The binding is a naming convention with no
declaration anywhere.

Going 9 → 17 classes is visible as `feat.2da` +31 columns and `skills.2da` +14
columns **with its row count unchanged at 8**.

**D · `repute.2da` — a square matrix indexed positionally on both axes.**
Row labels and column names are the same faction list in the same order.
Adding a faction means adding a row **and** a column, kept in sync by hand.
K1 21×21 → K2 24×24. Full record in `RECORDS.md`.

**E · The creature record's skill array** — established in earlier work,
restated for completeness: `SkillList` is 8 entries of `{Rank}` with no id.
`FeatList`, `ClassList` and `KnownList0` all carry explicit ids by contrast.

---

## 3 · The table census

**K1: 209 tables. K2: 424.** Grouped by what they govern (name-prefix grouping;
"unclassified" is real, not a rounding):

| domain | K1 | K2 |
|---|---|---|
| packages / presets (`pack*`, chargen) | 2 | **155** |
| items & upgrades | 62 | 68 |
| character rules | 24 | 32 |
| audio | 10 | 12 |
| appearance & models | 9 | 9 |
| UI & GUI | 8 | 8 |
| AI & scripting | 7 | 4 |
| world & modules | 7 | 6 |
| animation & camera | 3 | 5 |
| unclassified | 77 | 125 |

K2's growth is overwhelmingly the `pack*` family — **155 of the 229 K2-only
tables** are per-class equipment and feat packages, one table per class per
variant (`packeqsoldr1`, `packftjedig1`, …). This is mechanism 6 taken further:
rather than a class column, a class gets its own *table*, named by convention.

Full records on `classes`, `skills`, `feat`, `spells`, `appearance` and
`repute` are in `RECORDS.md`.

---

## 4 · The TLK

Full record in `RECORDS.md`. Headline answers:

| | K1 | K2 |
|---|---|---|
| entries | **49,369** | **136,329** |
| size | 5.41 MB | 10.16 MB |
| LanguageID | 0 | 0 |

**A StrRef resolves by fixed-stride array index** — entry *n* is at
`20 + 40n`, carrying an offset and size into a data block. No search, no name.

**An entry carries six fields besides text, and four are dead:**
`SoundResRef` is live (K1 66.6% of entries, K2 1.2%). `VolumeVariance`,
`PitchVariance` and `SoundLength` are **zero in every entry of both games** —
136,329 K2 entries, no exceptions — despite the SNDLENGTH flag bit being set on
74,039 of them.

**One flag value is undocumented and enormous.** `0x8000` appears on 307 K1
entries and **61,777 K2 entries — 45% of the table**. Every sampled instance has
string size 0 and no sound. Meaning not established; needs a disassembly.

**Second TLK: no evidence of support.** Scope of the negative — searched both
install trees for `*.tlk` (exactly one hit each), and both binaries for `.tlk`,
`dialogf`, `customtlk`, `usertlk`, `TalkTable`, `TLK`. K1 yields only `TLK `,
`Tlk`, `tlk`. K2 additionally has class names `9CTlkTable` and `11CSWTlkTable`,
which shows a table abstraction but not a second file. **No female TLK, no user
TLK, no override-TLK path found.** I did not disassemble the loader, so this is
"no mechanism visible", not "provably impossible".

---

## 5 · ⚠ The global coupling

The batch's second flagged question. The finding is stronger than expected.

**There is no module-local rules table. Not one, in either game.**
Searched every archive under `modules/` in both games — 398 K1 files and 246 K2
files — for resources of type 2017. **Zero.** Every 2DA in both games lives in
the game-global layer (BIF, `rims/`, `patch.erf`, or `Override`).

So **the entire rules layer is a single global namespace**, and a mod changing
any rule must replace a whole game-wide file. There is no scoping mechanism to
reach for, because none exists.

**`globalcat.2da` verified exactly as previously established:**

| | K1 | K2 |
|---|---|---|
| rows | **1,185** | **999** |
| Boolean | 809 | 160 |
| Number | 369 | 834 |
| Location | 5 | 3 |
| **String** | **2** | **2** |

Two string globals in the entire game, in both games. Confirmed, and the engine
reads this table by name — the literal `globalcat` is present in both binaries.

**Which tables are single points of truth a mod must overwrite wholesale?**
All of them, by the finding above. But a useful sub-answer: **107 of 209 K1 and
104 of 424 K2 table names appear as literal strings in the binary.** Those are
engine-named — they cannot be renamed, replaced by a differently-named table, or
scoped. The remaining 102 K1 / 320 K2 are reached only by reference from another
table or by a name the engine builds at runtime.

The worst instances, ranked by how much a mod must take ownership of to change
one thing:

1. **`globalcat.2da`** — one row per variable, game-wide. Two mods each adding a
   variable must merge or one loses every variable the other added.
2. **`repute.2da`** — square. Adding a faction touches every row.
3. **`skills.2da` / `feat.2da` / `featgain.2da`** — adding a class means editing
   the *schema* of tables you had no interest in.
4. **`appearance.2da`** — 509/671 rows, referenced by index from every creature
   in the game; two mods adding a creature body collide on row numbering.
5. **`spells.2da`, `classes.2da`, `baseitems.2da`** — same shape, smaller.

---

## 6 · K1 vs K2

Recorded per-table in `RECORDS.md`; collected here.

| dimension | K1 | K2 |
|---|---|---|
| 2DA tables | 209 | **424** |
| shared / unique | — | 195 shared, 14 K1-only, **229 K2-only** |
| TLK entries | 49,369 | **136,329** |
| classes | 9 | **17** (incl. `BountyHunter(CUT!!!)`) |
| level cap (as row counts) | 20 | **50** |
| delimiter drift | 13 tables, `rims/` only | none |
| tables changing shape | — | **76 shared tables** |

**Largest column growth on shared tables:**

```
feat            125 -> 245 rows    60 -> 91 cols   (+31)
xptable          20 ->  50 rows    22 -> 52 cols   (+30)
appearance      509 -> 671 rows    80 -> 94 cols   (+14)
featgain         20 ->  50 rows    17 -> 31 cols   (+14)
skills            8 ->   8 rows    30 -> 44 cols   (+14)
videoeffects      3 ->  16 rows     7 -> 15 cols    (+8)
acbonus          21 ->  51 rows     6 -> 13 cols    (+7)
spells          132 -> 282 rows    53 -> 60 cols    (+7)
classpowergain   20 ->  50 rows     4 -> 10 cols    (+6)
repute           21 ->  24 rows    21 -> 24 cols    (+3)
```

Two patterns visible in that table alone: **column growth tracks the class
count** (feat, featgain, skills, acbonus, classpowergain) and **row growth
tracks the level cap** (xptable, featgain, acbonus, classpowergain).
`classes.2da` is the only major table where columns *shrank* — 49 → 29.

**K1-only tables (14):** `actions`, `areaeffects`, `caarmorclass`, `categories`,
`catype`, `chargenclothes`, `combatmodes`, `defaultacsounds`, `dialogtokens`,
`domains`, `effectanim`, `effecticons`, `encumbrance`, `tutorial_old`.

**K2-only (229):** dominated by `pack*` (155). Also `influence`,
`chemicalcreate`, `itemcreate`/`itemcreatemira`, `emotion`, `facialanim`,
`autobalance`, `debugvariables`, the six new `cls_st_*` tables, and the
`itmwiz*` family.

---

## 7 · Scope — what was and was not checked

**Read and parsed in full:** all 209 K1 and 424 K2 2DA tables from the BIF
layer; all 2DA copies in K1's `rims/`, `patch.erf` and `Override`; both
`dialog.tlk` files header-to-entry across all 185,698 entries; `globalcat.2da`
and `classes.2da` in both games; both binaries via string extraction.

**Searched, negative:** module archives in both games for 2DA resources (zero
found, 644 archives); both install trees for additional `.tlk` files (one each);
both binaries for second-TLK mechanisms.

**Not checked:**
- Any running process. No claim about which of the duplicate table copies loads,
  or whether the engine bounds-checks row counts.
- Disassembly. All engine claims come from string literals and class names.
- The **meaning** of TLK flag `0x8000`, and where K2's per-line voice
  association moved to — that is batch 5 (DLG).
- The internals of GFF-family `.res` files in saves (`GLOBALVARS`, `PARTYTABLE`)
  — deferred to batch 4.
- Which specific column of which table feeds which engine subsystem. Mechanism
  classification here is structural, not semantic.
- NWN's 2DA/TLK layer — scoped to batch 7.
