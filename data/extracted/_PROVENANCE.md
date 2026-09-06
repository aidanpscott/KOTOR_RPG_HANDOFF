# data/extracted — provenance and status

## ⚠ `skills.json` is EXTRACTED FROM A STALE SOURCE. Do not trust its membership.

**Status: 24 records, and the live list is 26.**

`skills.json` was extracted from `docs/SKILLS-01.md` in **this** repository
(md5 `53fcd1b2269d9c5a41958245f27e5114`, 538 lines, unchanged since well before
the extraction). That copy is **the pre-`PT-552` skill list**.

### What it is missing

```
my 24  +  Survival  +  Fly  =  26     the live table total
my 24  +  Survival          =  25     the character skills
```

- **`Survival`** — retired and readmitted at **`PT-552`**. Absent from the copy
  here; the string `Survival` and the string `PT-552` do not appear anywhere in
  `docs/SKILLS-01.md`.
- **`Fly`** — **beast-only**, not on a character's skill list. Arrived after the
  copy here was written.

### How this was established

**⚠ Owner-confirmed on 2026-09-06.** The count of **26 — 25 character skills
plus `Fly`, beast-only** is confirmed by the project owner, who also records
that the stale figure of 24 was wrong in **eleven places** across the corpus,
because `Survival` was readmitted at `PT-552` and the count never propagated.
The section below is how it was first established here, independently, before
that confirmation.

Not from the source document — from the corpus's own reconciliation, written by
other agents against the live copy in `KOTOR_RPG_MAIN_WORK`:

| where | says |
|---|---|
| `to-library/TO-LIBRARY-20.md` §2 | *"24 the pre-PT-552 list — missing `Survival` · 25 the character skills · 26 the table total — 25 + `Fly`, which is BEAST-ONLY"* |
| `to-library/TO-LIBRARY-20.md` §2 | quotes the **live** `SKILLS-01 §1` heading as *"Twenty-six skills — 25 character + `Fly`, beast-only"* |
| `to-main/TO-MAIN-02-ATLAS.md` | *"`SKILLS-01` header … its own table has **26 rows**, **6** marked `new`"* |
| `to-main/TO-MAIN-10-ATLAS.md` ③ | the same three-number reconciliation, kept verbatim |
| `to-main/TO-MAIN-18-ATLAS.md` | *"25 / 24 / 22 — `Survival`, three correct measures at three moments"* |

Corroborating, on the copy here: its §1 heading reads **"Twenty-two skills"**
(not "Twenty-six"), and it carries **5** `**new**` markers where the live table
carries **6**.

### What is and is not wrong with the file

- **The 24 records it does contain were read correctly.** Names, attributes and
  line citations are accurate *for the version they came from*.
- **The membership is wrong** — it is short by two.
- **19 of 24 `description` fields are `null`**, because the copy here has no
  descriptions section. A "Descriptions — one line per skill" section is
  reported to exist in the live document; it is not in this repository.

### What is needed to fix it

The live `rules/SKILLS-01.md` from `KOTOR_RPG_MAIN_WORK`. That repository
returns **403 — "Write access to repository not granted"** with the token
available here, and no `rules/` directory has ever existed in this repository on
any branch.

**Nothing was synthesised.** `Survival` and `Fly` are *named* in the
cross-reference documents but their governing attributes and descriptions are
not, so they were not added. A guessed attribute is indistinguishable from a
read one.
