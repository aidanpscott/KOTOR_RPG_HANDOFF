# STUDY 02 — DEFINITION LAYER — FLAWS

F13–F23, continuing batch 1's numbering. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

Opens with an amendment to a batch-1 entry, since this batch's first job was to
check it.

---

### ⚠ AMENDMENT to F09 (batch 1) · "two shipped serialisations" was too strong
**Follows from:** `02-definition/RECORDS.md` → 2DA; `README.md` §0

F09 said K1's `rims/` copies of 13 tables differ from the BIF copies "only in
the column delimiter", and framed that as **two serialisations of 2DA**.

Parsing both forms of all 13 shows **identical columns, identical row counts,
identical cell values**. It is one format with a delimiter the reader tolerates.

Two factual corrections to F09 as written:
- The delimiter is a **per-file** property, not a per-layer one. The BIF layer of
  both games is 100% tab-delimited for multi-column tables.
- Single-column tables have no observable delimiter at all — a first pass here
  wrongly counted 12 K1 and 52 K2 BIF tables as NUL variants on that basis.

**The substance of F09 stands and is unchanged:** 13 core tables ship twice, in
byte-different copies, with nothing declaring which is authoritative. That is a
precedence problem (F02), not a format problem. F09 should be read as an
instance of F02 rather than as a finding about 2DA.

---

### F13 · Cells are untyped strings; the schema exists only in the reader
**Follows from:** `RECORDS.md` → 2DA

Every cell in every 2DA is a string in a shared data block. **No column declares
a type.** Whether `"3"` is a row index into another table, a count, a flag or a
literal three is decided entirely by code the file cannot see.

Consequences that cost real work:

Nothing can be validated. A typo that puts a ResRef in a numeric column, or a
row index one past the end of the target table, is not detectable by any tool
reading only the data — and 633 tables ship with no schema anywhere.

The reference graph is unrecoverable. Batch 2 had to *infer* which columns are
StrRefs by testing whether the integers fall in TLK range, and which are ResRefs
by testing whether the strings resolve against the KEY. Those classifications
are approximate at the boundaries and always will be, because the information
was never written down.

*Cheapest fix in the whole study: one declared type per column, including what
it points at. It costs a header row and makes the entire reference graph
machine-checkable.*

---

### F14 · `****` and empty collapse during compilation
**Follows from:** `RECORDS.md` → 2DA; `README.md` §1

The text source of a 2DA distinguishes an explicitly-blank cell (`****`) from an
absent one. The compiled binary does not: **`****` appears zero times across
111,521 K1 cells and 211,281 K2 cells.** Both become the empty string.

So a distinction the authoring format supports is destroyed on the way to the
shipped format, and no consumer of shipped data can recover it. Anyone reading a
blank cell cannot tell "the author declared this inapplicable" from "the author
left it out".

This matters in exactly the place it is most load-bearing: the blank `_reco`
cells in `skills.2da` mean "this class cannot use this skill", which is
semantically an explicit statement, and it is stored as an absence.

---

### F15 · A class is a row in one table and a column-name prefix in five others
**Follows from:** `RECORDS.md` → classes.2da, skills.2da, feat.2da; `README.md` §2C

Adding a class means editing the **schema** of tables that have nothing to do
with classes:

```
K2   feat.2da            48 of  91 columns are per-class
     featgain.2da        30 of  31 columns are per-class
     skills.2da          30 of  44 columns are per-class
     acbonus.2da         10 of  13 columns are per-class
     classpowergain.2da   9 of  10 columns are per-class
```

`featgain.2da` is 97% per-class columns — it is a class table wearing a feat
table's name.

**And the binding is undeclared.** The three-letter prefix (`sol_`, `jgd_`,
`drx_`) appears **nowhere in `classes.2da`** — searched all 49 K1 and 29 K2
columns. The link between class row 3 and the column prefix `jgd_` exists only
as a convention in someone's head and in compiled code.

The cost is measurable: K2 going 9 → 17 classes shows up as `feat.2da` gaining
31 columns and `skills.2da` gaining 14 **while its row count never moved off 8**.

*The relational answer — a `class_id, feat_id, availability, rank` table — was
available and standard well before 2003.*

---

### F16 · The level cap is not a value; it is the row count of eight tables
**Follows from:** `RECORDS.md` → 2DA; `README.md` §2B

There is no "maximum level" setting anywhere. The cap is **implicit in how many
rows the level-indexed tables happen to have**: `cls_atk_1/2/3`, all nine
`cls_st_*`, `acbonus`, `xptable`, `featgain`, `classpowergain`, `cls_spgn_jedi`.

Raising it from 20 to 50 in K2 meant growing every one of those in lockstep —
visible as `xptable` 20→50 rows, `acbonus` 21→51, `featgain` 20→50,
`classpowergain` 20→50, `cls_atk_1` 20→50.

If any one of them is short, the cap is silently whatever the shortest table is,
and nothing reports the inconsistency.

---

### F17 · `repute.2da` requires a row and a column added in lockstep
**Follows from:** `RECORDS.md` → repute.2da

Faction relationships are a square matrix whose row labels and column names are
the same list in the same order. K1 is 21×21, K2 is 24×24 — K2's three new
factions each required a row **and** a matching column, aligned by hand.

Nothing enforces the alignment. There is no id shared between the two axes; the
correspondence is position, and a single insertion in one axis and not the other
silently reassigns every relationship past that point.

The table also carries an asymmetry nothing explains: **the `Player` row has no
matching column**, because column 0 is `label`. So there are 21 faction rows and
20 faction columns.

---

### F18 · ⚠ There is no module-local rules table. Not one, in either game
**Follows from:** `RECORDS.md` → 2DA (SCOPE); `README.md` §5

Searched every archive under `modules/` in both games — **398 K1 files and 246
K2 files** — for 2DA resources. **Zero.**

The entire rules layer is a single global namespace. There is no scoping
mechanism, not one that is unused — one that does not exist. A campaign cannot
say "in my content, this weapon does more damage" without changing the value for
the whole game, permanently, for every other campaign installed.

Combined with batch 1's F03 (Override is one flat game-global folder) and F02
(precedence undeclared), this is the shape of the problem: **the only way to
change a rule is to replace a game-wide file, in a folder with no namespacing,
under a resolution order nobody can read.**

This is the entry this batch exists to produce. Everything else here is detail
around it.

---

### F19 · Every global variable must be predeclared, and there are two strings
**Follows from:** `README.md` §5

`globalcat.2da` must list every variable a script can use, and the engine loads
it by name (the literal `globalcat` is in both binaries). Verified:

| | K1 | K2 |
|---|---|---|
| rows | 1,185 | 999 |
| Boolean | 809 | 160 |
| Number | 369 | 834 |
| Location | 5 | 3 |
| **String** | **2** | **2** |

**Two string globals in the entire game**, in both games.

Two problems compound. The predeclaration itself makes a game-wide table a
prerequisite for any script state — so two mods that each add a variable collide
on the same file, and the loser's variables simply do not exist. And the string
budget means anything a campaign wants to *remember as text* has essentially
nowhere to go.

---

### F20 · Row labels are unconstrained and sometimes meaningless
**Follows from:** `RECORDS.md` → 2DA

Row labels are exactly the decimal row index in **189 of 209** K1 tables and
**367 of 424** K2 — redundant with position, costing bytes and offering nothing.

Where they are *not* redundant they are inconsistent: `dialogtokens` uses
`<abutton>`, `droiddischarge` uses creature ResRefs, `bindablekeys` uses
`key0…`. So a consumer cannot rely on the label being either the index or a
name.

And uniqueness is not enforced: **K2's `debugvariables` ships with every row
label set to `1`.** A field that is sometimes an index, sometimes a name, and
sometimes duplicated is not usable as a key by anything.

---

### F21 · The TLK entry carries four fields; three are dead in every entry
**Follows from:** `RECORDS.md` → TLK

Each 40-byte TLK entry reserves `VolumeVariance` (u32), `PitchVariance` (u32)
and `SoundLength` (float) alongside the sound ResRef.

**All three are zero in every entry of both games** — 49,369 K1 and 136,329 K2,
no exceptions. That is 12 bytes × 185,698 entries ≈ 2.2 MB of guaranteed zeroes
across the two games.

Worse than unused: **the SNDLENGTH_PRESENT flag bit is set on 48,663 K1 and
74,039 K2 entries** whose `SoundLength` is 0.0. The flag asserts data that is
not there, so a consumer trusting the flag reads a zero as a real duration.

Same family as batch 1's F07 (`LanguageCount`, `FixedResCount`,
`DescriptionStrRef`), and the pattern is now consistent enough to name: **these
formats declare capability they never implement, and then set flags claiming
they did.**

---

### F22 · One flag value covers 45% of K2's string table and is undocumented
**Follows from:** `RECORDS.md` → TLK

TLK flags define three bits: TEXT (1), SND (2), SNDLENGTH (4). Value `0x8000`
is none of them, and it appears on **307 K1 entries and 61,777 K2 entries — 45%
of K2's entire table.**

Every sampled instance has string size 0 and no sound ResRef, so they read as
empty slots. But an undocumented flag on nearly half the table is not something
a consumer can safely ignore, and nothing in the data says whether it means
"deleted", "reserved", "placeholder" or something load-bearing.

*Recorded as a flaw rather than an unknown because the cost falls on every
consumer forever, not just on this study.*

---

### F23 · One string table, game-global, with no second-table mechanism
**Follows from:** `RECORDS.md` → TLK; `README.md` §4

Exactly one `dialog.tlk` per install, and no evidence of support for a second.
Scope: searched both install trees for `*.tlk` (one hit each) and both binaries
for `.tlk`, `dialogf`, `customtlk`, `usertlk`, `TalkTable`, `TLK`. K2 has the
class names `9CTlkTable` / `11CSWTlkTable`, showing an abstraction exists; no
path to loading a second file was found.

So **every string in the game shares one integer namespace**, and adding a line
of dialogue means claiming an index in a 136,329-entry game-wide file that every
other piece of content also indexes into.

This was already named in the study README as a known flaw. What this batch adds
is the scoped confirmation that there is **no alternate mechanism to reach for**
— not an unused one, not a partial one. NWN's parallel approach (a custom TLK
starting at a high StrRef base) has no counterpart visible in either KOTOR.
