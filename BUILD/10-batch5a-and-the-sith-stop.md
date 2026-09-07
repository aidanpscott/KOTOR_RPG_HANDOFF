# 10 · Batch 5a, three rulings applied, and the Sith stop searched

**`KOTOR-RPG-APP` `a271f73` · `MAIN_WORK` `45a58a1`.** 119 tests pass, analyze
clean. **The Sith stop holds. It is genuinely unwritten.**

---

## 1 · The re-run — and the records did not change

Source `a04516b6`, 165 lines. `check_extracts.py`: **current 23, stale 0**.

`available`, `universal`, `closed_to_all`, `chassis_dependent` and `unruled` are
**byte-identical** across the re-run, exactly as predicted. Two fields moved:

| Field | Before | After |
|---|---|---|
| `stated_total_superseded_by` | absent | `PT-1405`, on all four |
| `contested` | `["Athletics"]` on Assassin and Battle | empty |

> **⚠ `stated_total` STILL SAYS WHAT `§2.4` LITERALLY SAYS** — 14 and 12. The
> ruling is named *beside* the number, not substituted for it. Nothing is
> quietly rewritten.

### ⚠ The ruling is read from the document, not hard-coded

`superseded()` looks for `PT-1405`'s own correction line in the source.

**Control:** the rewritten extractor run against the **pre-correction** source
(`50e08129`) reports `superseded_by = None` and `contested = ["Athletics"]` on
both — exactly what it reported before. So a ruling can never be applied to a
source that does not carry it.

### ⚠ A new variety of staleness, and it earns a name

**A stale count hidden by an invariant sum.** `9+6+8` and `9+5+9` both make 23,
so `§2`'s title *"The 23, ruled"* survived `PT-319` intact while three of its
four component counts went stale. The invariant is what stopped anyone noticing.

---

## 2 · Athletics is offered; Skill Focus keeps one reason

The **Assassin droid sees 15** skills and the **Battle droid 13**. Nothing is
withheld for the `§2.3`/`§2.4` disagreement any more. **Science and Survival are
still unruled and still withheld**, and the screen still says so.

**Skill Focus is still not takeable — for one reason now.** `SKILLS-01 §12` says
twenty-three exist, one per skill; the library holds **one generic record with
no skill on it**, so there is nothing to name. `PT-1405` removed the second: the
aptitude applies from level 2 and **Skills are not repriced**, and the screen
says that rather than the old objection.

---

## 3 · ⚠ THE SITH STOP — searched, and it holds

**Everywhere checked, in order:**

| Where | Result |
|---|---|
| `ATLAS/decisions/` — **all 34 files, fetched and read** | ⚠ **Nothing.** Five files contain the letters `feat`; every hit is *defeat*, *featured*, or a species bonus feat. Zero mention any Sith base class |
| `KOTOR_RPG_Library` — live tree, not `_dead/` | `C17-FEATS-AND-ACTION.md` carries `FEAT-SCHEDULE-01` **verbatim** — same 15-column grid, same summary, same "Seven schedules". No new information |
| `CLASS-TABLES-AUTHORED` (both copies) | Sith Warrior, Sith Assassin, Sith Inquisitor each have a level table: **`Level · BAB · Fort · Ref · Will`. No Feats column** |
| `CLASSES-FORCE-PHB` | Says so itself: *"⚠⚠ NO LEVEL TABLES. They are in `CLASS-TABLES-JEDI` and `CLASS-TABLES-AUTHORED`"* |
| `PLAYTEST-RULINGS-01` / `PT-INDEX-01` | `PT-126` and `PT-996` — below |
| `FEATS-SURVEY-01`, `feat_tables.md` | Per-class **granted** tables, from the game. *"27 feats granted free · 56 selectable at level-up"* — a lifetime total from the source system, not our per-level count |

**`PT-126`** assigns the Sith Assassin **12 feats at 30, by owner instruction** —
a *total*, amending `PT-125`'s 15. **It does not give a cadence and does not
give a first-level count.**

**`PT-996`** ruled the gap *"a missing DOCUMENT, not two missing entries"* — all
six Force base classes lacked a player-facing chapter. That chapter now exists
as `CLASSES-FORCE-PHB`, **and it explicitly holds no level tables.** The three
Jedi base classes are fine: `CLASS-TABLES-JEDI` gives them a Feats column, and
all three carry `feat_levels`. **The Sith side's authored tables omit it.**

### ⚠ And the one thing that looks like an answer is not one

`FEAT-SCHEDULE-01`'s **"Seven schedules"** table has a row reading
**`Every third from 1 | Sith Assassin | 10`**.

- Its own summary table gives **Sith Assassin 12** at level 30, not 10.
- The per-level grid's last column is headed **`Assassin`** and reaches **10**,
  on exactly that cadence.
- The prose four lines below calls it **"The Assassin"**, not the Sith Assassin.
- But `§`'s prestige note lists `sas` among the codes that *"grant a feat
  immediately"* — and `PT-130` reads `sas` as the Sith Assassin's own column.

> **⚠ So the row either mislabels the prestige Assassin, or gives the Sith
> Assassin a cadence its own total contradicts.** **Reported, not resolved.**
> Taking the 10-column across would also overturn `PT-126`'s owner-instructed
> 12, which is not mine to do.

### The need

**How many feats `Sith Warrior`, `Sith Inquisitor` and `Sith Assassin` gain at
1st level is not written anywhere.** Level-30 totals exist for all three;
**no cadence and no first-level count does.**

`featsAtFirstLevel` stays **null, not zero**. Every other class gains one — and
that is the pattern that makes inventing it tempting, not evidence.

**What was NOT done:** nothing was authored. I did not extract
`FEAT-SCHEDULE-01`'s grid, and I did not build steps 7–9.

### Scope of this negative

Read: all 34 `ATLAS/decisions/` files in full; the `KOTOR_RPG_Library` live tree
listing plus `C17-FEATS-AND-ACTION`, `C10-CLASSES`, `REQUEST-FEATGAIN-K2`,
`FEAT-SCHEDULE-01` and `CLASS-TABLES-AUTHORED` from it; every `rules/`,
`design/` and `playtest/` file in `MAIN_WORK` naming a Sith base class — 21
files. **Not read:** the Library's `_dead/` tree, and `tools/gen/feats_class.json`,
which returned empty over the API.
