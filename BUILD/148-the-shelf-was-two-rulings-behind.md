# BUILD 148 — yes, it is read; and the extractor had gone blind to §8

---

## 1 · ⚠⚠ THE ANSWER: `equipment.toml` IS READ AND IT IS THE DICE. `items.toml` IS NOT READ AT ALL.

    equipment.toml  →  ChargenSource.baseTypes  →  combatantsIn  →  every attack
    items.toml      →  ChargenData.items        →  NOTHING

**`equipment.toml` is exactly the gap `BUILD 147` found for droid skills**, and it
was **two rulings deep**:

| | shipped | ruled |
|---|---|---|
| Vibrosword | `2d6` | **`1d12`** — `PT-1747` |
| Lightsaber | `2d10` | **`2d8`** |
| Blaster Carbine | `1d8` | **`1d12`** |
| Disruptor Pistol · Rifle | `1d4` · `1d6` | **`1d6`** · **`1d10`** |
| Ion Blaster · Rifle | `1d4+1d10` · `1d6` | **`1d6+1d10`** · **`1d10`** |
| Sonic Rifle | `1d6` | **`1d10`** |
| Droid plating | `+4 / +6 / +8` | **`+3 / +4 / +9`** — `PT-1734` |

**⚠ `items.toml` IS A GENUINE NON-ISSUE.** It is parsed into
`ChargenData.items` and **read by nothing in the app, Loom or the engine** —
`declared-and-read-by-nothing`, filed rather than fixed. Re-shipped for
hygiene; its staleness had no gameplay consequence.

## 2 · ⚠⚠ AND RE-SHIPPING BLIND WOULD HAVE **DELETED** DROID PLATING

`PT-1734` — my own slice — replaced `§8`'s placeholder with the real
`baseitems.2da` rows and retitled the section:

    ## 8. ⚠ Droid plating                              the anchor's regex
    ## 8. ⚠⚠ Droid plating — EXTRACTED, and the placeholder is gone

The extractor requires `^## 8\. ⚠ Droid plating`. **One extra `⚠` and it
matched nothing.** Every run since produced **zero** plating rows, printed a
`0` in a column of counts nobody diffs, and wrote the file anyway.

> **The shelf was not stale here because nobody re-extracted. Had anybody
> re-extracted, plating would have vanished from the shelf entirely** — and the
> correction `PT-1734` was opened to make would have been replaced by nothing
> at all.

**Three repairs, not one:**

* **anchored on the section NUMBER**, which is the part of a heading that does
  not editorialise.
* **`table_at` gained an optional header match.** `§8` now holds **two**
  tables — the `2da` read above the rule derived from it — so *the first table
  under the heading* had silently become the wrong one. **A position is not an
  identity.**
* **a declared section that finds nothing is now a HARD FAILURE.** Every entry
  in `SECTIONS` is there because the document has one; zero rows means the
  anchor drifted off it. ⚠ **Watched refusing to write before it was kept** —
  it exits non-zero and leaves no file.

## 3 · ⚠⚠ SECOND SIGHTING IN TWO SLICES OF AN INSTRUMENT GOING SILENT

`BUILD 147` found `extract_droid_skills.py`'s number-word map stopping at ten,
so *"Eleven skills"* parsed as `None`. This is the same failure one document
over: **a check whose subject moved, reporting nothing instead of reporting
that it could not look.**

    the pattern     a check keyed to a SPELLING of its subject
    what happens    the subject is edited, the key misses, the check returns empty
    what it looks   like a clean result
    what it is      a dead instrument

Both are now loud: the word map covers twenty, and a section with no rows
refuses to write.

## 4 · ⚠⚠ AND THE OLD CATALOGUE COUNT WAS `PT-1762`'s FINDING, WRITTEN DOWN AND UNREAD

`equipment_test` asserted:

    1,427 items and 1,425 distinct resrefs

**Two rows sharing a resref, carried as a fact of the catalogue.** They were
`a_shockarm_01` and `a_shockarm_02`, each naming **two different designs** —
the free auto-upgrading Shock Arm and the purchasable one. That is exactly the
contradiction `PT-1762` found **by reading the documents**, and **this number
had been recording it for as long as the case existed.**

`PT-1765` deleted the free version and the gap closed itself. The counts are
equal now, **and the equality is the better assertion**: one resref, one item.

## 5 · ⚠ NOTHING IN THE SUITE PINNED A DIE

Eight wrong damage values changed and **not one case moved.** Two are pinned
now — deliberately the two with a history of being wrong rather than all
eleven: the **plating ladder**, wrong in *both directions* before `PT-1734`
(Medium two low, Heavy one high, because the jump is at the medium/heavy
boundary), and the **Vibrosword**, changed and withdrawn and changed again
across `PT-1747`/`PT-1748`.

---

## What ran

    Lodestar   659 tests   exit 0
    Loom       261 tests   exit 0
    app        533 tests   exit 0   (+2, and two counts updated)
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings

⚠⚠ **`check_extracts` IS AT ONE STALE COMPARISON, DOWN FROM FIVE.** The
remaining one is `event_kinds.json`, which `STATE.md` already records as *"the
lag is in the code, and re-stamping would hide it."*

## Heads

    Lodestar        95bc648   (unchanged)
    Loom            5ed6185   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   7de0ee2
    MAIN_WORK       d726cbe

⚠ The shelf's `equipment.toml` and `items.toml` were replaced. The whole
generated package was diffed against the installed one first: **those two were
the only differences.**
