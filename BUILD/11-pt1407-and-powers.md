# 11 · `PT-1407` applied, the attack gap surveyed, and Powers

**`KOTOR-RPG-APP` `73b5324` · `MAIN_WORK` `43f2840`.** 128 tests pass, analyze
clean. `base-rules` is **14 kinds / 986 records**; `check_extracts.py` **current
24, stale 0**.

---

## 1 · `PT-1407` — an override, not a schedule

`first_level_feats.json` → `first_level_feats.toml`. **Three records.**

`featsAtFirstLevelFor()` asks the class's **own schedule first** and the
override second. Sixteen base classes still answer from `feat_levels`; the
override adds exactly three keys and changes nothing else.

> **⚠ `featLevels` AND `featsAtFirstLevel` STAY NULL ON ALL THREE.** `PT-1407`
> gave a first-level number and said in the same breath that it sets no cadence,
> so nothing in the record claims to know level 2. `sets_cadence: false` travels
> on the extract. **Creation unblocks; levelling does not.**

**Its source is a design document**, so it is its own kind for the same reason
`chassis.json` is: `classes.json` reads the PHB chapters and `CLASS-TABLES-*`,
and welding a `CHARGEN-DATA-01` ruling onto it would put two sources under one
fingerprint.

`CHARGEN-DATA-01` changing also made **`chassis.json` stale in the same pull**.
Re-run; records unchanged.

---

## 2 · The attack gap — surveyed, not extracted

**⚠ The premise needs one correction, and it makes the gap smaller than stated.**
`attack_chains` and `attack_picks_at_30` are populated for **14 classes**, not
for Jedi Guardian alone: all **13 standard base** classes plus Jedi Guardian.

**Where the values come from.** Not from `CLASS-ATTACKS-01`. Each class
**chapter's record table** carries `| Attack picks at 30 | … |` and
`| Attack chains | … |` as two-cell rows, and `extract_classes.py` already reads
them from `CLASSES-STANDARD-PHB` and `CLASSES-FORCE-PHB`.

**So it is not an unwritten extraction. It is a written one running over an
incomplete source.**

| Missing | Why |
|---|---|
| 5 of 6 Force base classes | `CLASSES-FORCE-PHB` **has** their chapters; only the Jedi Guardian's record table carries the two rows. Sentinel, Consular and the three Sith have `Rate` and no attack rows |
| 24 prestige classes | No PHB chapter at all |

### ⚠ Is it derivable? Half of it is

- **`attack_picks_at_30` — YES, from `rate` alone.** `CLASS-ATTACKS-01 §3`:
  **Combat 36 · Middle 27 · Specialist 18**. One table, three values, and `rate`
  is populated on all 19 base classes.
- **`attack_chains` — NO.** `§2.3` makes chains **a band, not a number**
  (Combat 14–20, Middle 11–17, Specialist 8–14) and each class is **assigned**
  individually. The assignments live in one table, headed **"Assigned so far"**,
  with **ten class rows** — Jedi Sentinel and Jedi Consular among them, **and
  none of the three Sith.**

**So: a one-source extraction for the picks, and a per-class assignment for the
chains that is itself incomplete at source.** Not extracted in this slice.

### ⚠⚠ And the survey found something the gap was hiding

**`CLASSES-FORCE-PHB`'s Jedi Guardian record reads `Attack picks at 30 = 18`
and `Attack chains = 20`.** `CLASS-ATTACKS-01` gives the Guardian **Combat**,
which is **36 picks**, and `§2.3` assigns it **18 chains** with **20 feats at 30**
and **11 capstones**.

> **The capstones match exactly (11), which is what says the row was built from
> `§2.3`.** Read across, the chapter took `§2.3`'s **chains 18** into *picks* and
> its **feats@30 20** into *chains*. **The extraction is faithful; the source
> row is transposed.** Every standard-base row is consistent — Soldier 36/14,
> Scout 27/17 — so it is one row, not a pattern.
>
> **Reported, not fixed.**

### ⚠ A second one, on the same six classes

`PT-126` — *"Sith Assassin: 12 feats and **`Specialist`**, by owner
instruction"* — and *"the Sith side loses its `Middle` class."*
**`CLASSES-FORCE-PHB` and `classes.json` both carry `Sith Assassin · Middle`.**
It does not touch creation, and it does touch attacks. **Reported, not resolved.**

---

## 3 · Step 7 — Powers

`PT-1232`, `PT-1099`. Renders **only where the class grants Force powers** —
six of nineteen base classes. `HubShape` already decided that; it is the one
conditionally-rendered step that is not droid-related.

**Two picks.** `MULTICLASS-01 §2.2a`: *"`cls_spgn_jedi.2da` gives 2 Force powers
at Jedi level 1 and +1 per Jedi level after"*, reasoned from as ours — *"a Scout
8 entering Guardian arrives with 2 powers where a pure Guardian 9 has 10"* — and
`PT-128` **corrected the Sith Assassin to the base tier on exactly that axis**
("`classpowergain.2da` gives every base Jedi 2 powers at 1st level; `sas` and
`sma` print 1 … all corrected for a base-tier Sith Assassin").

> **⚠ AND `POWER-COSTS-01 §6` CALLS ACQUISITION "OPEN".** *"How many picks per
> level per class is not [settled]."* **I read the two as compatible** — §6's
> open item is the per-class schedule *after* level 1, which is why `PT-130` had
> to rule the Inquisitor's level-30 total separately — **and I applied only the
> first number.** ⚠ **That reading is mine. If the level-1 count is also open,
> this step is not buildable and I have built it.**

### The pool is 21

Of 104 powers, **22 have no prerequisites**. One of those, **Precognition**, has
**no cost**.

**⚠ A power with no cost is not offered, and the screen says why.**
`PARTITION-01` put nine powers in `FORCE-POWERS-01`'s description table and not
in `POWER-COSTS-01`'s priced roster — there is nothing to spend to use them.

**⚠ Alignment is shown and not enforced.** 11 universal, 7 dark, 4 light are all
offerable. Nothing in the corpus stops a Jedi taking a dark power at creation,
and `ALIGNMENT-01` carries the consequence, so the screen marks rather than
filters.

**Not extracted, and not needed at creation:** class gates. `POWER-COSTS-01 §6`
defers them, and the three prerequisite strings naming a class name **prestige**
classes, which are not creation choices.

---

## What was NOT done

Steps **8 and 9** are unbuilt. **No character record, no save**, and `Continue`
stays disabled. `attack_chains` and `attack_picks_at_30` were **surveyed and not
extracted**, as the brief said. Nothing was authored.

**Not captured:** Powers was verified by test at 1280×720, not by screenshot.
The step strip is down to two padlocks and that was not visually checked.
