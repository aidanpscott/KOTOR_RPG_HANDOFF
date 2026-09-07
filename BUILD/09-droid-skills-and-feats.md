# 09 · Batch 5, a droid completes Skills, and Feats

**`KOTOR-RPG-APP` `61d05ea` · `MAIN_WORK` `81ab9ec`.** 119 tests pass, analyze
clean. **Two stops, both narrow, both named.**

---

## Batch 5 — `DROID-SKILLS-01` extracted

`extract_droid_skills.py` → `droid_skills.json` → `droid_skills.toml`.
**Four droid species.** `base-rules` is now **13 kinds / 983 records**;
`check_extracts.py` reports **current 23, stale 0**.

| State | Count | What it means |
|---|---|---|
| `universal` | 9 | `§2.1` — every droid body |
| `closed-to-all` | 5 | `§2.2` — closed by rule, **with the reason it was closed for** |
| `chassis-open` / `chassis-closed` | 9 | `§2.3` — body-dependent, and this body has it or does not |
| `unruled` | 2 | on the roster and **nowhere in the chapter** |

> **⚠ THE CLOSED LIST IS A RULE, NOT AN ABSENCE.** `§2.2` closing Mysticism —
> *"No Force connection"* — is a positive statement. Five states per skill, and
> none of them collapsed into "not available".

**⚠ Four droid SPECIES, not seven chassis.** `§2.3` gates on the **body** —
Astromech, Assassin, Battle, Remote — which is what `SPECIES-CHAPTER-v2` ships.
`chassis.json`'s seven are `DROID-MODELS-01` **model** chassis and gate ability
scores. Two axes, both correct. `classes.json` already said so and I read it
there rather than deciding it.

---

## ⚠ The control, and what it caught

`§2.4` states each species' total. The extractor **recomputes** it from
`§2.1 + §2.3` and compares — the control the batch asked for, built in rather
than run once.

| Species | Computed | `§2.4` says | |
|---|---|---|---|
| Astromech | 13 | 13 | ✓ |
| Remote | 12 | 12 | ✓ |
| **Assassin** | **15** | **14** | ⚠ |
| **Battle** | **13** | **12** | ⚠ |

**The difference is `Athletics`, on both.** `§2.3` opens it to those two bodies
at `PT-319`, reversing a ban *"written from the astromech outward and never
checked against the other three."* `§2.4`'s totals omit it.

**And the section headers disagree with their own tables.** `§2.2` says *six*
and lists five; `§2.3` says *eight* and grids nine. `§2` is titled *"The 23,
ruled"* — and 9+6+8 and 9+5+9 both make 23.

> **One reading fits all of it:** before `PT-319`, Athletics was the sixth
> closed skill and `§2.3` had eight rows. `PT-319` moved it, the grid row was
> added, and the two header counts, `§2.2`'s list and `§2.4`'s totals were not
> updated. **⚠ THAT IS A READING, NOT A RULING. It is recorded and not applied**
> — both numbers are carried and neither is corrected.

**⚠ `PT-621` opens `Persuade` to the "`Protocol` chassis", which is not one of
the four bodies.** `§2.2` still lists Persuade as closed and `§2.3` has no
Persuade row, so the carve-out names an axis the table cannot express. Carried
as `closed-to-all`, which is what the table says.

---

## ⚠ Science and Survival are UNRULED

Both are on the 25-skill character roster. Both appear **nowhere** in
`DROID-SKILLS-01` — not opened, not closed, not body-dependent.

**Scope:** searched the chapter, and every file in `rules/` and `design/`
mentioning `droidcanuse` or `DROID-SKILLS` — ten files. The only hit is
`SKILLS-01`'s **Droid Master** class list, and Droid Master is an organic class
*about* droids. **Not checked:** `ATLAS/decisions/`, the 34 files `MAIN_WORK`
has never read.

---

## A droid completes Skills

It sees its body's list and reads underneath what it may not have, in the three
separate kinds the extract keeps apart. An Astromech: **13 of 25**.

**⚠ Two kinds of skill are WITHHELD rather than offered** — Athletics, and
Science and Survival. **A droid built without them is valid under every reading.
One built with them is valid under only one, and would have to be unbuilt.** The
screen says which is which and why, so the withholding is visible, not silent.

**A droid on a body the gate does not name still stops**, and the panel now says
`§2.3` names four rather than claiming the extract is missing.

---

## Step 6 — Feats

`PT-1228`. **One pick.** Row 1 of `FEAT-SCHEDULE-01`'s per-level grid is a **1
in all fifteen columns**, so a class that gains at level 1 gains exactly one.

**The pool is 52** — the selectable chain **heads**. The other 80 selectable
records are links; they are shown beneath their head so the ladder is visible,
and they are not offered.

> **⚠ "A link needs its head" is read from what a chain IS.** The extract
> carries no prerequisite field. Said here rather than assumed.

### ⚠ The granted/selectable split, said out loud

None of the **188 granted** appears in the list, **and the screen says so** —
`§5a`, *"Restricted chains are GRANTED, not bought."* A player who has read the
library will look for Force Jump and must find out why it is absent rather than
concluding the data is thin.

### ⚠ Skill Focus is not takeable, for two reasons at once

1. **`SKILLS-01 §12` says twenty-three exist, one per skill.** The library holds
   **one generic record with no skill on it**, so there is nothing to name.
2. **It grants aptitude** — *"1 point per rank instead of 2"* — which is a
   **Skills** input arriving at step **6**, after Skills was priced.
   `CHARGEN-FLOW-MAP-01 §4` draws `FEATS → aptitude` and in the same block calls
   Skills *"terminal"* and names **one** backwards dependency. This is a second.
   `PT-1200` ruled the first one forward-looking — *"the aptitude applies from
   level 2 … do not reprice skills."* **Nothing rules this one.**

---

## ⚠ WHAT STOPPED — the three Sith base classes

`Sith Warrior`, `Sith Inquisitor`, `Sith Assassin` have **no feat schedule**.

- `CLASS-TABLES-AUTHORED` covers all three for BAB and saves and **has no Feats
  column at all**.
- `FEAT-SCHEDULE-01`'s per-level grid has **fifteen columns and none is theirs**.
  Its summary table gives them level-20 and level-30 *totals*; its "Seven
  schedules" table names neither Sith Warrior nor Sith Inquisitor.

**The need:** how many feats these three classes gain at 1st level is not
written. `featsAtFirstLevel` is **null, not zero** — zero would claim they gain
none, which the source does not say. Every other class gains one, and **reading
that across to a class the grid does not carry would be inventing the number.**

**What was NOT done:** I did not extract `FEAT-SCHEDULE-01`'s grid — the
schedule for later levels is not needed at creation and was not built. I did not
build steps 7–9. No character record, no save.

---

## Other scoped negatives

- **A droid's aptitude sources.** It skips Origin (`§2`, the model replaced
  homeworld) and `PROGRAMMINGS-01` **has no `teaches` column** — checked all 17
  records and the document (`teaches` appears 0 times). **So a droid's class
  list is its only aptitude source.** Not a stop; the screen works.
- **Per-class feat availability.** `CHARGEN-FLOW-MAP-01` names `<cls>_list = 1`,
  which is `feat.2da` — a game file. The 52 heads are **not** filtered by class,
  and nothing in the corpus filters them.
- **Which granted feat a class receives at 1st level.** Not carried: the granted
  records have no class on them, and `§5a`'s `Class | Ladder | Caps at` table was
  skipped by shape at batch 3c. Not needed for the pick; needed to *display* what
  a character starts with.
- **Not captured.** The Feats screen was verified by test at 1280×720, not by a
  screenshot. The step strip lost a padlock; that was not visually checked.
