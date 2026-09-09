# BUILD 59 — `PT-1481` the seven, `PT-1482` the column, and a gap between two guards

**681 green** — Lodestar 303 · Lens 4 · Loom 120 · app 254.

---

## The seven, on your test

> **An aside about HOW THE ENTRY CAME TO SAY SOMETHING goes. A citation
> attached to something the entry SAYS keeps the something.**

**Four went entirely** — Beast Control's rename-and-DC note, Drain Life's
comparison to Death Field, Force Enflame's dropped-insanity note, Force
Strangle's *AUTHORED* note — plus **Spear of Midnight Black's shouted absence**,
which the cell already states as **One target.**

**Three kept the rule and dropped the token** — Force Choke and Force Strangle
keep **two rounds**; Death Field keeps **20d4** and Drain Life **15d4**.

⚠ **Moved, not deleted.** All of them are preserved verbatim in a blockquote
above the table, **with the test that split them written beside them**, so the
next person reading the file sees what left and why.

⚠ **And the edit is in the SOURCE, not the extractor.** `PT-1467`'s convention
lives in the extractor for things a machine can name; **these are the ones it
could not**, which is the same fact as your observation that the three I kept
are the population my splitter damaged at `PT-1474`.

**`powers.toml` is off the annotation check entirely** — 52 shipped cells → 45.

## `PT-1482` — the column is `kit`

The extractor's field follows the column; the app followed in one line. A test
asserts the label is `kit`, that `consumable` is gone, and ⚠ **that the gloves
are still there** — the column was renamed, not emptied.

## And three extracts were stale against your own edits

`CHARGEN-DATA-01` and `SPECIES-CHAPTER-v2` moved in your recent pushes, so
`chassis`, `first_level_feats` and `species` lagged. Re-extracted. **`stale 1`**,
which is `event_kinds` and is deliberate.

---

## ⚠⚠ The gap between the two guards, named

You asked for this in `STATE` rather than carried in a report. It is there now.

    check_annotations      reads base-rules/*.toml      — the DATA half
    check_player_strings   reads Dart string literals   — the LITERAL half

**A citation assembled at runtime from pieces is covered by neither.**

```dart
    'you fall — ' + ruleName + ' (' + ptNumber + ')'
```

Neither guard sees that: the data half has no cell to read, and the literal
half sees only `'you fall — '`, which is clean.

⚠ **Nothing in the tree does this today** — checked. So it is a gap, not a
defect, and the only reason it is written down is that the person who built
both checks is the only one who can see where they stop.

**What would close it:** the format strings are the seam. A rule that
player-facing text is never assembled from a variable that could hold a
citation is not checkable; **a rule that citations live in one named place and
are never interpolated is.** Neither is worth a slice until something actually
does it.

## Still open

- The seven are closed. **45 cells remain**, in `feats`, `items`, `skills`,
  `species`, `worlds`, `professions` and `profession_grants`.
- `targets` under-populated by 21 against its own prose — populate first, gate
  after.
- ⚠ A citation assembled at runtime falls between the two checks.
- Conditional damage; `§4a`'s grant offer reaching classes it does not name.
