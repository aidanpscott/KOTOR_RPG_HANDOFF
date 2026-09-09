# BUILD 51 — `PT-1467`: a value field carries a value

**149 shipped cells carried an editorial aside. 98 are out. 51 remain, and 44
of those are the two slices you ordered separately.**

---

## What was built

**The convention**, in both languages, naming the same fields:

    MAIN_WORK/scripts/_annotation.py     the rule, and apply_to() applying it
    Lodestar/lib/src/annotation.dart     isAnnotationField / withoutAnnotation

`note`, `ruling` and any `*_superseded_by` are annotation. **Identified by
name**, so `species_screen` skips them without a per-file list — which is your
addition, and it is what made the species cells fixable at all. Their aside had
nowhere to go until the screen could recognise one.

**The check** — `MAIN_WORK/scripts/check_annotations.py`. Two scopes: the
shipped `base-rules/*.toml`, which is what a screen can render, and
`data/extracted/*.json`, which is where the fix goes. Extract-only fields are
excluded by measuring which field names actually ship, rather than by a list.
Exit codes per `PT-1451`; zero scope exits 2.

**⚠ Its control is that it went red on nine files the day it was written**, and
it is still red on four.

## The numbers

| | cells | files |
|---|---|---|
| the check found, reading rather than matching | **149** | 9 |
| moved into a sibling `note` | **98** | 7 |
| `equipment.section` — your slice 2 | 6 | 1 |
| `powers.effect` + `prerequisites` — your slice 3 | 43 | 1 |
| ⚠ left for an authoring decision | **2** | 2 |

The hand sweep reported 140. **The check found nine more**: five in
`powers.prerequisites`, a column I had not listed; one hyphenated key
(`species.cold-adapted`) my regex could not see; three shouted absences. Two
counts, and the instrument beat the hand.

## ⚠ The splitter moves TOKENS, not tails, because the first draft was wrong

The first version moved an em-dash tail wholesale. **The dry run caught it
turning `Small — +1 Defence, PT-623.` into value `Small`, note
`+1 Defence, PT-623.`** — it moved a defence bonus off the player's screen.
`Frag Grenade — g_w_fraggren01, ×2` would have lost the `×2`.

It also **refuses a citation doing grammatical work**. In
`... and PT-559 removed the second pool it also doubled` the token is the
sentence's subject, and removing it leaves `and removed the second pool`. A
citation followed by a lower-case word is left alone and reported. That is one
of the two authoring decisions; the other is `Sneak Attack`'s effect.

**Nothing in any corpus document changed.** The convention lives in the
extractor, as you ruled, so a re-extraction keeps it. Verified idempotent: a
second run produces byte-identical extracts.

---

## ⚠ Two defects found while doing this, both in instruments

**1 — `check_engine_pin` silently lost half its scope.** It printed
`2 compared · all level` where it had compared **4** the slice before. `pub`
quotes `resolved-ref` only when the hash starts with a digit — `04e4061…` is
quoted, `b7e9198…` is not — and the regex required quotes. **So a pin left
scope depending on what a commit hash happened to begin with.** Underneath,
`None` meant both *"does not consume this engine"* and *"could not parse it"*.
Now three outcomes, and an unreadable pin exits 2. Controlled: an unquoted
**stale** hash — the case that was invisible — now reports BEHIND at 4 compared.

**2 — an extractor will write its JSON over its own source.** Four take
`(source, dest)`; `extract_feats` and `extract_starting_equipment` hardcode the
source and take `(dest)`. Running the second pair the first way **replaced
153 KB of `FEATS-LIBRARY-01.md` with its own extract, silently, exiting 0.**

⚠ **I did that.** Restored from git — which worked because the corpus is
tracked and was clean, and that is luck, not a safety net.
`_paths.dest()` now refuses a `.md` destination and every extractor that writes
goes through it. The argument orders are still inconsistent; unifying them is
six scripts and their callers, and is not this slice.

**3 — and re-running an extractor erased its `_notes`.** Eight paragraphs of
provenance for `species`, six for `professions`, four for `programmings`, all
of which existed **only in the committed JSON**. One of them read *"Pilot's
grant … is preserved verbatim rather than nulled"* — about the exact cell this
slice changed. They are in the scripts now, the way `extract_feats` and
`extract_items` already carried theirs.

---

## Tests

**649 green** — Lodestar 297 · Lens 4 · Loom 115 · app 233.

`annotation_test.dart`'s second case is the control: **a field nobody
anticipated is still shown.** A predicate returning true too readily would pass
a names-only test and silently blank a species trait.
`annotation_hidden_test.dart` was **verified red with the fix reverted** before
being trusted.

## Still open

- `equipment.section` (6) — your slice 2. A value used as a key.
- `powers.effect` (43) — your slice 3. `targets:` needs a column.
- 2 cells needing an authoring decision, reported by the check, not mangled.
- ⚠ `PT-1468` is unstarted and is the larger thing: the player fights unarmed
  while carrying a blaster, and what a person understands on death is nothing.
