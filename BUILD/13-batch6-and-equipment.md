# 13 · Batch 6, and Equipment — `PT-1200` resolves

**`KOTOR-RPG-APP` `c85a9c4` · `MAIN_WORK` `c827da5`.** 144 tests pass, analyze
clean. `base-rules` is **21 kinds / 2,497 records**; `check_extracts.py`
**current 34, stale 0**.

---

## 1 · `items.json` — one extractor, nine sources, nine digests

**⚠ And it is NOT the first kind to span files.** `classes.json` already
declares **nine** sources, and `check_extracts.py`'s `declared()` returns a
**list**. Nine digests rather than one over the concatenation, because a change
to `ITEMS-05` alone has to be nameable.

**1,427 items · 1,425 distinct resrefs** — the same 1,425 an independent `grep`
counts. **All 44 category counts are reproduced exactly.**

### ⚠ Three reader bugs, each with a different signature

| Signature | Cause |
|---|---|
| **every category exactly +1** | The **separator row has eight cells too**, and `---` survives `clean()`. One phantom per table |
| **`melee-one-handed` 23 short** | ⚠ **22 rows carry a real resref and an em dash for a NAME** — `propls01`, `propga01`. **A row is an item if it has a resref, not if it has a name.** 85 rows corpus-wide are unnamed and every one has a resref |
| **ten categories one short** | ⚠ **Ten rows are broken across physical lines** — the `PT-1301` shape one layer down. The source put a multi-line `Prerequisites:` block in the **Name** cell, so the row's other seven cells sit three or four lines below. Joined before parsing |

> **The control found all three, and the shape of each error named its cause.**
> A uniform `+1` is a reader counting one extra thing per table; a single
> category 23 short is a whole class of row being skipped; ten scattered
> one-shorts are ten individual defects.

### ⚠ Five file headers disagree with their own category headings

| File | header | its own categories | found |
|---|---|---|---|
| `ITEMS-01` | 418 | **420** | 420 |
| `ITEMS-02` | 173 | **172** | 172 |
| `ITEMS-04` | 135 | **129** | 129 |
| `ITEMS-05` | 241 | **248** | 248 |
| `ITEMS-08` | 42 | **73** | 73 |
| `ITEMS-09` | — | 143 | 143 |

**Every category agrees; only the file headers do not.** `ITEMS-07` documents
the same shape at `PT-871` — *"`PT-781` MOVED 134 UPGRADE ROWS OUT OF `plot`
INTO `ITEMS-09` — AND THE HEADER NEVER MOVED."* **Recorded, not corrected.**

**Nothing was re-converted.** `PT-339`, `PT-341`, `PT-308`, `PT-327`, `PT-345`,
`PT-349`, `PT-384` already did that work; the cells are copied across unchanged.

---

## 2 · `starting_equipment.json`

Three routes · **19** class arrays · 9 droid arrays · **§2c's 14-row pricing
key** · 20 profession grants · **19** two-weapon rows.

### ⚠ The status block says 18 twice, and both tables carry 19

**The nineteenth is the Saboteur, in both.** `§4` and `§4a` each list all 19
base classes — 13 standard and 6 Force. The Saboteur is **new at `PT-784`** and
the header predates it.

> **⚠ `classes.json` already records this class going missing in three places**
> — `PT-1295`'s 18, the PHB's *"thirteen at a glance"*, and its own absent
> progression table. **This is the fourth and the fifth.**

**⚠ And 28 grants is `PROFESSIONS-01`'s count, not a row count here.** `§5`
says so itself: 8 grant something that is not an item and were settled at
`PT-701`/`PT-703`. This file names the other 20 — **16 slot-fillers and 4
upgrades**. Reading 28 as a row count reports 8 missing that were never here.

**13 of the 16 slot-fillers resolve to a resref and a price.** The other three
name no item **and that is the ruling**: `Augmented` grants *"the implant
matching the class's primary Key ability"*, `Dancer` *"two adrenals matching the
one you carry"*, `Initiate` *"one colour crystal, or a tier-1 saber upgrade"*.
Each depends on the character.

---

## ⚠ 3 · A reader fix, and `PT-1408`'s own correction exposed it

`PT-1408` corrected the Jedi Guardian's transposed attack row and appended
`⚠ PT-1408 — was 18, TRANSPOSED` **after the closing pipe**. That makes the row
**three cells**, and `read_phb` required **exactly two**.

> **So the correction silently un-extracted both fields and they came back
> `null`.** `check_extracts.py` flagged the source change; the value loss was
> invisible until the record was read.

The record tables are two-column: **the first two cells are the row and anything
after is a note.** `jedi_guardian` now reads **picks 36, chains 18**, and
`attack_chains` is populated for **14** classes again.

---

## 4 · Step 8 — Equipment, and `PT-1200` resolves

**The two boxes are clickable, and the item side is named and priced.**

    Neural Band                    25cr · a_helmet_01
    aptitude in Survival           applies from level 2 — PT-1200

**There is no default.** Pre-selecting either half would answer the question
`PT-1200` made a choice.

**⚠ Route 1 only, and the screen says why.** `§1` gives three routes. **Route 2,
the purse, spends the array's own credit value — and that value is not
written.** The arrays name items in prose; **only 18 of 41 names resolve to
exactly one catalogue row**, and `§2c`'s disambiguation covers 14. Route 3 is
the GM's, and a campaign package may impose it.

**⚠ The empty slots are named** — `§2`: implant, head, hands, arms and belt
start empty on purpose, *"fill every slot at creation and every profession grant
becomes a sidegrade."*

**⚠ Eight professions have no item half**, and the screen says the step is not a
choice for them rather than showing an empty box.

---

## What was NOT done

**Step 9, Identity, is unbuilt. No character record, no save.** Nothing was
extracted from either game. `ASSET-REPLACEMENT-01`'s corrected pairing unit —
the asset, not the thing it depicts — is the owner's edit and needs nothing
here yet.

**Not captured:** Equipment was verified by test at 1280×720, not by screenshot.
The step strip is down to one padlock and that was not visually checked.
