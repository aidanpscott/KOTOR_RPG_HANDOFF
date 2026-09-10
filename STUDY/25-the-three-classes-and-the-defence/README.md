# STUDY 25 — the index rule, the three missing classes, and the Defence column

---

## 1 · IS THE STALE INDEX CHECKABLE? ⚠ YES, AND IT IS CHEAPER THAN `check_extracts`

**Three occurrences is a pattern:** `BUILD/README` stopped at 25, `STATE.md` went
eleven slices stale, and `STUDY/README` listed seven batches while sixteen more
landed. **All three are the same defect — an index whose contents grew past it.**

**`check_extracts` compares a recorded digest to the file on disk.** An index
against its own directory is **the same shape one register over, minus the
digest** — it is *set membership*, not content equality:

```
declared = the folder names in the index table
present  = the directories on disk
red if   present - declared   (something exists and is unlisted)   ← all three failures
warn if  declared - present   (something listed and gone)
```

**⚠ Why it is cheaper than `check_extracts`:** no fingerprint to record, no
source to follow, no staging step. **The index already names the thing; the
directory already exists.** Nothing new has to be written down for the check to
work — which is exactly why the omission survived: **the evidence was always
sitting there uncompared**, `check_extracts`'s own opening complaint.

**⚠ What it cannot see, stated so it is not over-trusted:** that a listed row
*describes* its directory correctly. `STUDY/README` could list
`24-one-file-deeper` against the wrong summary and the check would pass. **It
catches absence, not wrongness** — the same boundary `check_derived` draws.

**⚠ And the three known instances are not one script.** `BUILD/`, `STUDY/` and
`STATE.md` are three different index shapes: a numbered-file list, a folder
table, and a prose document with no enumerable contents at all. **The first two
are checkable by the rule above. `STATE.md` is not** — it answers *what is true*,
which no directory listing can verify. **That one stays a discipline.**

**Not built — `MAIN_WORK/scripts/` is `Coder`'s path.** The rule is written into
`STUDY/README` and the index is repaired.

---

## 2 · ⚠⚠ TWO OF THE THREE ARE NOT MISSING — AND THEY ARE ATTESTED THREE TIMES

> `CHARACTER-RECORD-01:146`: *"⚠ Three have no per-level table anywhere —
> `engineer`, `marksman`, `saboteur`."*

**The Marksman and the Engineer both have complete per-level BAB tables.** They
were unreachable for three compounding reasons, and each is a shape this project
already knows.

### Where they are

**`CLASS-TABLES-DROID.md` — a file whose title is "Marksman and Engineer".**

```
| Level | \multicolumn Marksman | | | | Engineer | | | |
|---|---|---|---|---|---|---|---|---|

| Level | **CD** BAB | Fort | Ref | Will | **ED** BAB | Fort | Ref | Will |
```

### ⚠ Three reasons nothing reached it

1. **The filename says `DROID` and the contents are two classes.** Its own §
   *"Chassis is not class"* explains why: *"`DROID-SKILLS-01 §2.3` names four
   droid **species**… `k1_classes.2da` names two droid **classes** — Combat and
   Expert. They are different axes and both apply."*
2. **The table is two classes side by side**, with a stray `\multicolumn` LaTeX
   artifact and a **blank line inside the table**. Any markdown table reader
   produces garbage columns or stops at the blank line.
3. **The column headers are `**CD** BAB` and `**ED** BAB`** — initials, not class
   names. Nothing searching for `Marksman` finds the Marksman's own column.

### ⚠⚠ The control — three independent attestations that agree

| source | Marksman | Engineer |
|---|---|---|
| `CLASSES-STANDARD-PHB.md` record | **d12** | **d8** |
| `CLASS-TABLES-DROID.md` summary | **d12, full — `CLS_ATK_1`** | **d8, three-quarters — `CLS_ATK_2`** |
| **`k1_classes.2da`, read from the game** | row 6 `CombatDroid` **d12, `CLS_ATK_1`** | row 7 `ExpertDroid` **d8, `CLS_ATK_2`** |

**`CD` and `ED` are `CombatDroid` and `ExpertDroid` — K1's own row labels.** The
hit dice match across all three, independently, which is what makes this an
identification rather than a guess.

**⚠ Staged against source:** `HANDOFF/data/k2_classes.2da` was compared to the
game's own binary for these rows — **identical, no drift.** *(It is a plain-TSV
export, a **third** 2DA representation in this project beside V2.b binary and
NWN's V2.0 text.)*

### ⚠ AND K2 CANNOT SUPPLY THIS — THE DISTINCTION EXISTS ONLY IN K1

| | K1 | K2 |
|---|---|---|
| `CombatDroid` | d12 · **`CLS_ATK_1`** | d12 · `CLS_ATK_1` |
| `ExpertDroid` | d8 · **`CLS_ATK_2`** | d8 · ⚠ **`CLS_ATK_1`** |
| every other class | mixed `_1`/`_2` | ⚠ **`CLS_ATK_1`, all seventeen** |

**`BRIEF-CLASS-DESIGNER` already recorded the general fact (`PT-72`): *"`k2_classes.2da`
gives every class `CLS_ATK_1`… BAB carries no information in this source."***
**⚠ What is new here is that it bites the Engineer specifically** — K2 would give
it **full** BAB where K1 gives three-quarters. **The Engineer's three-quarters is
a K1 fact, and reading K2 for it would silently produce a different class.**

---

## 3 · ⚠⚠ THE SABOTEUR IS GENUINELY ABSENT — AND IT IS THE SIXTH OMISSION

**No BAB table anywhere.** Scoped: not in `CLASSES-STANDARD-PHB` (it has a
`## The record` and **no `## Progression`**), not among `CLASS-TABLES-AUTHORED`'s
thirty, not in `-BASE`, `-JEDI` or `-DROID`, and **not in either game's
`classes.2da`** — it is an invented class, `PT-784`, added late.

**The corpus already counts five prior omissions of the same class:**

```
PT-1295's eighteen · the PHB's "thirteen at a glance" · its absent progression
table · the status block saying 18 twice while both tables carry 19 (×2)
```
> *"ONE CLASS, FIVE OMISSIONS, ALL DOWNSTREAM OF `PT-784` ADDING IT LATE."*
> — `PLAYTEST-RULINGS-01`

**⚠ This is the sixth**, and it is the first that blocks build work.

### ⚠ What IS attested for it

| | |
|---|---|
| **Rate** | `Specialist` |
| **Hit die** | **d6** |
| **Attack roster** | `Spray` · `Covering Fire` · `Shoot` — *"the area axis, and nobody else opens on it"* (`CLASS-ATTACKS-01 §297`) |
| **Heading** | ⚠ **`# ⚠ Saboteur`** — the warning glyph is *inside the heading*, so a `^# ([A-Za-z ]+)$` extractor misses the class entirely. **The same shape as `CD`/`ED` above, in a different file.** |

---

## 4 · ⚠⚠ AND THE RATE WORD DOES NOT GIVE YOU THE LADDER

**This is the trap, and it would have produced a wrong Saboteur.**

`CLASSES-*-PHB.md` gives every class a **`Rate`** — `Combat` / `Middle` /
`Specialist`. **It is tempting to read that as the BAB rate. It is not.**

`CLASS-ATTACKS-01 §2` says so outright: the rates are *"derived from
`FEAT-SCHEDULE-01`'s level-30 totals, because that is the only signal the source
gives about how fast a class acquires **anything**."* **It is an attack-**pick**
rate derived from a **feat** signal.**

**Proof from the ladders themselves:**

| class | Rate | BAB |
|---|---|---|
| Engineer | **Middle** | three-quarters |
| Smuggler | **Specialist** | three-quarters |
| Jedi Consular | **Specialist** | three-quarters |

**Two different rate words, one BAB. The mapping does not exist.**

### The whole corpus, surveyed — BAB is BINARY

**36 class tables parsed for BAB at level 1 and level 20:**

| ladder | count | classes |
|---|---|---|
| **Full** (+1 at 1st, **+20** at 20th) | **8** | Soldier · Brawler · Sith Warrior · Jedi Guardian · Blademaster · Commando · Juggernaut · Sith Battlemaster |
| **Three-quarters** (+0 at 1st, **+15** at 20th) | **28** | everything else |
| **Half** (`CLS_ATK_3`) | **0** | — |

**Plus Marksman (full) and Engineer (three-quarters) from `-DROID` = 38 tables**,
which is exactly the 38 `Coder` counted.

> **⚠ `CLS_ATK_3` — the half progression — is used by NO class in either game.**
> Confirmed independently here against both `classes.2da` files, and already
> stated in `CLASS-TABLES-DROID`: *"An earlier correction assigned it to the
> Engineer on the strength of `CLASS-TABLES-BASE` calling it 'the droid-expert
> table.' That description was wrong."*

**So the Saboteur's BAB is a choice between two ladders, not an open field.**
⚠ **Which one is still authoring and still the owner's** — `Specialist` does not
decide it, because `Specialist` decides nothing about BAB.

### ⚠ And `CLASS-ATTACKS-01` contradicts itself about the Marksman

| where | says |
|---|---|
| `§2` rate table, line 33 | **Marksman is `Combat`** |
| `§2.2b`, line 57, 24 lines later | **"⚠ The Marksman is Specialist, not Combat."** *`featgain.2da` gives it 11 at level 30 — the Smuggler's number* |
| `CLASSES-STANDARD-PHB` record | **`Rate` = `Combat`** |

**Two of three say `Combat`, one says `Specialist`, and the dissenter is in the
same file as one of the agreers.** Reported, not resolved — **but note it is a
*pick*-rate dispute and cannot touch BAB**, which `k1_classes.2da` settles as
full (`CLS_ATK_1`) either way.

---

## 5 · THE DEFENCE BONUS — ⚠ ONE DATA POINT, AND NO SECOND ANYWHERE

**Answer to the question asked: no. Nothing else is attested.**

**Scoped negative:** searched `MAIN_WORK` and `HANDOFF/STUDY` — all `*.md`,
`*.json`, `*.toml` — for `defen[cs]e`, `Defense Bonus`, `Defence Bonus`, and
`Noble`. **The only per-level class Defence attestation in the corpus is one
sentence:**

> *"Confirmed on the Noble (RCR pp.42–43), where it runs **+2 at 1st to +10 at
> 20th**."* — `CLASS-TABLES-JEDI §5A`

**Everything else that matches `Defence` is a form or feat modifier** —
`FORMS-01`'s Determination +3, Aggression −2, Ferocity −4, `Well Guarded`'s +1
per adjacent enemy — **a different quantity entirely.** None is a class ladder.

**And the column is empty exactly as reported:** parsed the `**Def**` column
across all three Jedi tables in `CLASS-TABLES-JEDI` — **every value in every row
of all three is `—`.** Not sparse. Uniformly absent.

**No Noble extract exists.** `D-AJ-SENTINEL-AND-CLASS-PLAN` says the Noble was
*"already extracted in full"*, but **`MAIN_WORK/data/extracted/` holds no class
record for it** — the surviving trace is the one prose sentence above, which is
two endpoints, not a ladder.

### ⚠⚠ AND THE THING WORTH SAYING, WHICH `§4` JUST PROVED

**The question — *"would a second and third data point tell us whether every
class shares one progression or several?"* — has a warning attached, and this
study supplies it.**

**`§4` shows the corpus already contains a live counter-example to
one-word-implies-one-ladder:** `Middle` and `Specialist` classes share a BAB
ladder, and the `Rate` word predicts nothing. **A single Noble reading cannot
distinguish *"all classes share +2→+10"* from *"the Noble is one of three
progressions"*, and RCR is a d20 derivative where per-class good/average/poor
tracks are the norm** — the same shape as saves, which this corpus already
models per class.

> **⚠ So one data point is not a weak version of the answer — it is the wrong
> kind of evidence.** What settles it is **two classes expected to differ**: a
> martial class and a caster. **The Noble alone would license exactly the
> inference `§4` disproves.**

**Not authored, and not derivable.** RCR Chapter 3 is a book read and it is the
owner's.

---

## 6 · What was NOT checked — scoped

* **RCR itself was not read** — it is not on this machine in any form searched.
  Every RCR claim here is quoted from our own corpus quoting it.
* **The `-DROID` ladder was read at levels 1–8 and its summary**, not
  transcribed in full. It states *"rows 1–20 are byte-identical between the
  games"* and **that claim was not verified against `cls_atk_1/2.2da`.**
* **The BAB survey parsed 36 tables with one regex** (`| **N** | +X |`). The two
  in `-DROID` were **counted from their summary, not parsed** — their side-by-side
  layout defeats the same regex, which is the finding. **A table in a fourth
  layout would still be missed**, and nothing here proves 38 is the total.
* **Level-25 and level-30 rows were not used** — classification is on the level-20
  endpoint only.
* **`Minion` (K1 row 8, K2 row 8; d10, `CLS_ATK_1`, `playerclass 1`) is in both
  games and in no corpus document searched.** Not pursued; flagged because it
  carries the player flag and would surprise anyone reading `classes.2da` cold —
  as `D-AJ-SENTINEL-AND-CLASS-PLAN` already noted for a different trio.
* ⚠ **`D-AJ-SENTINEL-AND-CLASS-PLAN` says K2 carries "`Marksman` (hit die 12),
  `Engineer` (8), and `Minion` (10)".** The hit dice are right and **the labels
  are ours, not K2's** — K2's rows read `CombatDroid` and `ExpertDroid`.
  **Recorded because a reader grepping K2 for `Marksman` finds nothing** and may
  conclude the class is absent when it is row 6.
* **The `check_index` rule of `§1` was not implemented** — `MAIN_WORK/scripts/`
  is `Coder`'s path.
