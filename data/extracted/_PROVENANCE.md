# data/extracted — provenance and status

**Status: CURRENT.** Both files were extracted on 2026-09-06 from fingerprinted
sources in `STUDY/_reference/`, and each output carries its source fingerprint
inline so a later run can tell whether it read the same document.

| output | records | source | md5 | lines |
|---|---|---|---|---|
| `skills.json` | 26 (25 character + 1 beast-only) | `STUDY/_reference/SKILLS-01.md` | `e157dea6` | 735 |
| `class-skills.json` | 20 (14 standard + 6 Force) | `SKILLS-01.md` §9.2b + `STUDY/_reference/CLASSES-FORCE-PHB.md` | `e157dea6`, `ebc82531` | 735, 222 |

`CLASSES-FORCE-PHB.md` hashes to `ebc82531`, **matching `from-library/WHERE-IS.md`
exactly** — the Library's index and this copy are the same file.

---

## ⚠ The earlier extraction was stale. This one supersedes it.

The pilot run extracted **24** skills from `docs/SKILLS-01.md`
(md5 `53fcd1b2`, 538 lines, §1 heading *"Twenty-two skills"*, zero occurrences
of `Survival`). That was the **pre-`PT-552`** list, short by `Survival` and
`Fly`.

```
pilot 24  +  Survival (PT-552)  +  Fly (PT-554, beast-only)  =  26
```

**`docs/SKILLS-01.md` must not be used for extraction.** It is an old snapshot
retained for the study batches that already cite it.

The count is owner-confirmed at **26 — 25 character skills plus `Fly`, which is
beast-only**. The stale figure of 24 was wrong in eleven places across the
corpus because `Survival` was readmitted at `PT-552` and the count never
propagated.

---

## ⚠ The parsing trap in `SKILLS-01 §1`, recorded because it will recur

**The master table is interrupted.** Rows run from line 25 to line 48, then
**lines 49–52 are prose** — a blockquote and a paragraph about `Survival` — and
the table **resumes at lines 53–54** with `Swim` and `Xenology`.

A parser that reads *consecutive* rows stops at line 48 and returns **24**,
silently losing `Swim` and `Xenology`. That is the exact failure the owner
described: two independent 24s that differed by four names.

`scripts/extract2.py` collects every table row within a bounded line window
instead, and the interruption is visible in the committed data — `streetwise`
cites line 46, `survival` line 48, and `swim` line 53.

---

## What was verified, and how

**Run 1 — skills**

- master-table rows read: **26**; records: **26**; unique ids and names: **26**
- character skills **25**, beast-only **1** (`Fly`)
- descriptions populated **26 of 26**; null attributes **none**
- **diff by name** against the Descriptions table: **no difference in either
  direction** — a count was not treated as a set
- independent `grep` count of both tables: 26 and 26, agreeing with the parser

**Run 2 — class skill lists**

- standard classes from **`§9.2b`, lines 350–363**: **14**
- each row's declared skill count matches its actual list length: **all 14 agree**
- Force classes from `CLASSES-FORCE-PHB`: **6**
- **agreement verified, not assumed**: all six lists are byte-identical to
  `SKILLS-01 §9.2` — Guardian 5, Sentinel 8, Consular 7, Warrior 6, Inquisitor
  8, Assassin 8
- every class skill resolves to one of the **25 character skills**; **no
  unrecognised name**
- **`Fly` appears on no class list**, as the source requires

---

## Deliberate omissions

**Prestige classes carry no skill lists in any source.** That is an open design
question, not a gap to fill. None were synthesised.

**`§9.2` and `CLASSES-STANDARD-PHB` were not used for standard classes.** Both
are superseded by `§9.2b` per `PT-1299`. `§9.2` was read **only** to verify the
Force six.

---

## One field added beyond the agreed shape, flagged for approval

`skills.json` records carry **`beast_only`** (boolean) in addition to
`id`/`name`/`attribute`/`description`/`source`.

It was added because the brief asks for a character-versus-beast count, and
without the field that count is not verifiable from the data — `Fly` would be
indistinguishable from `Swim` on a character sheet.

**Still without a home, and unchanged from the pilot report:** the master table's
`Armour` column (✱ on Acrobatics, Athletics, Sleight of Hand, Stealth, Survival,
Swim) and its `Consolidates` column. Both are real and both were dropped.
`class-skills.json` also carries `category` (`standard`/`force`) and
`declared_count`, since it merges two sources with different provenance.
