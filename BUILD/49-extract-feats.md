# 49 · `extract_feats.py`, and what the disambiguation leaves

**637 green.** `MAIN_WORK 890db53`. **`feats.json` can be re-run for the first
time**, and the sizing question is answered with a measurement that corrects
the shape of the blocker rather than its size.

---

## 1 · The extractor, and the control that mattered

**`extract_feats.py` did not exist.** `feats.json` was produced ad hoc at batch
3c — exactly as `equipment.json` was before `PT-1452` — so **the largest
extract in the corpus could not be refreshed at all.** `PT-1462`'s marks made
that visible: the file went stale and there was nothing to run.

**⚠⚠ THE CONTROL IS EXACT REPRODUCTION, AND IT PASSES.** `PT-1463` moved the
annotation out of the Effects cell, so **no data cell changed** — which means a
faithful extractor must reproduce the existing 320 records byte for byte.

    320 extracted · 320 committed · 0 field differences
    §1 16 · §2 9 · §3 68 · §4 39 · §5 109 · §5a 9 · §5b 24 · §5c 46

**The only thing that changed in the written file is `source` on 295 records**,
whose line numbers genuinely moved when the eight-line note was inserted.

**⚠ `source` is excluded from the diff, and that is not a loosened test.**
Comparing it reports 289 differences that are **the document being edited**,
and hides any that are **the script being wrong.**

### ⚠ Three things the first attempt got wrong — all found by the diff

- **The middle column is not always `Level`.** §5b's granted chains head it
  `⚠ Granted at` and carry *"Droid Master 1"*. Matching the literal word **lost
  six records.**
- **⚠⚠ An authored chain is named by its HEADING, not by a `›` prefix.**
  `Hold the Deck`'s links carry `⚠` instead, so prefix-detection made every row
  its own chain.
- **A heading's chain name runs to its first em dash** — `Sadism → Sated`.

**Each was invisible in the output and obvious in the diff.** A new extractor
against an existing extract is the only cheap way to find them.

---

## 2 · ⚠⚠ What `item_disambiguation` leaves — and it is a different obstacle

**The count is not the answer.** Its 14 rows cover **7 of the 8** names my
parse finds genuinely ambiguous in the catalogue.

**⚠ But the dominant remaining obstacle is not unresolved NAMES. It is that ten
of the forty-two array cells are not values at all:**

    consumable = "1 Sensor Probe — was Adrenal Stamina"
    weapon     = "Blaster Pistol — its Long Sword is unusable"
    weapon     = "NONE — the class feature is the weapon"
    weapon     = "Ion Blaster — w_blaste_02, 50cr"

> **That is `PT-1463`'s defect in a second file: an editorial note living
> inside a data cell.**

**So a resolver cannot match these until the annotations move out** — and
matching them by stripping prose is `TRACE-83` again, which is precisely the
argument `PT-1463` just settled for `FEATS-LIBRARY-01`.

**⚠ And it has already surfaced as a symptom**: `PT-1464` reports *"1 Sensor
Probe, was Adrenal Stamina"* **printing to players**, now that something reads
the table. **Invisible while nothing read it** — `BUILD/48`'s class arriving
from the other side.

### The honest sizing

**Arming the player was never blocked by 23 unresolved names.** It is blocked
by, in order:

1. **⚠ Ten array cells that mix a value with an annotation** — the same fix
   `PT-1463` just demonstrated, in a second file.
2. **One genuinely ambiguous name** the 14 rows do not cover.
3. Then the resolution itself, which is ordinary work.

**⚠ My parse is crude and its 42/20/8 are approximate** — the corpus's own
figures are 41/18/14. **The shape of the answer holds; the counts are mine and
should not be quoted as the corpus's.**

---

## 3 · ⚠⚠ `PT-1464` — read, and NOT started

**The acceptance landed**: `t3-k9.sav` opens, the Astromech at exactly STR 8
round-trips, and `[Persuade]` rolls and passes.

**And my `droid_arrays` wiring hard-blocks four classes** — Soldier, Marksman,
Brawler, Saboteur — **with Soldier the pre-selected default**, so picking Droid
and leaving the class alone cannot create a character.

**⚠ I called null "the honest answer" and asserted it in a test. It is honest
and it is enforced at the wrong step.** `STARTING-EQUIPMENT-01 §3` says nine of
eighteen classes are open to a droid and means it: **a missing droid array is
not a missing kit, it is that line.** The bar belongs at the **class** step, as
`PT-92` greys out the Force classes there rather than failing later.

**Not started — it is its own slice and ruled as one.** ⚠ **But it is a hard
block on the default path and I caused it**, so it is the one I would take
next. The nine open classes are already on disk: `droid_arrays.toml` has
exactly nine rows.

**And `starting_equipment.json` is now stale** from the same edit.
