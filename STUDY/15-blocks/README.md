# STUDY 15 — Daggerfall's prefab and block system

**Why:** `PT-1360`/`PT-1361` admit tilesets carrying prefab pieces — corridor
sections, junctions, rooms — painted at a larger grain than a tile. Daggerfall
is the named model. This is `TRACE-95` again, borrowing **structure** from
Daggerfall rather than KOTOR, for space instead of conversation.

---

## What ships

```
BLOCKS.BSA   1,295 records    920 .RMB exterior · 187 .RDB dungeon
                              187 .RDI (always exactly 512 bytes) · 1 named FOO
MAPS.BSA       248 records    62 regions × MAPPITEM/MAPDITEM/MAPTABLE/MAPNAMES
```

Both parse **self-validatingly** — the records end exactly where the directory
begins, in both files, with no slack.

## The three findings

**1 · ⚠ ROTATION IS TWO BITS, AND IT IS THE ANSWER TO REUSABILITY.**
Every placed piece inside a block carries a quarter-turn. Proven across all 920
files — **29,440 entries, exactly four values**: `0x0000`, `0x4000`, `0x8000`,
`0xC000`. A corridor section is authored once and used four ways. For a palette
an author browses, that is the difference between 225 entries and 900.

**2 · ⚠ SHAPE AND IDENTITY ARE SPLIT ACROSS TWO FILES.**
The block carries shape **and props** — its first four bytes count 3D objects
and *flat* objects, which is Daggerfall's furniture and people. The **location**
carries the instances: a per-building array and a door list. Same tavern
everywhere; different shopkeeper. **We drew the same seam independently** —
`AREA-FORMAT-01 §3`'s template-path versus per-instance tag.

**3 · ⚠ THE DOOR, AND THREE GAMES DISAGREE.**

| | Where it lives | What it carries |
|---|---|---|
| Daggerfall | a list on the **location** | **8 bytes**; a third of locations have none |
| Aurora / Odyssey | its own blueprint type, `UTD` | **56 fields**, 16 of them script hooks |
| Ours | a `[[connections]]` entry | tag, position, destination, arrival point |

Eight bytes against fifty-six fields is not a disagreement about doors. It is a
disagreement about what a game is — and **we are building the second kind and
have written the first.**

## What not to copy

The region file split, `RDI`, the `TVRN`/`BANK`/`RESI` function taxonomy, and
variable-size blocks in a fixed grid. All four serve generation. The taxonomy in
particular is a generator's lookup key, and adopting it as a naming convention
would import exactly the failure `PACKAGE-NAMING-01 §5a` calls *a category
posing as a thing*.

## ⚠ What this study did not establish

**The block-to-grid mapping.** I could not find the arrays that say which block
sits in which cell, after three approaches; `MAPDITEM` was not opened. So
**determinism is unanswered** — the natural follow-on to `TRACE-95`'s seeded
dialogue — and the 8×8 city grid is folklore here, not a finding.

That gap is the generation half, which `FLAWS.md` argues we should not copy
anyway. Lucky rather than clever, and said plainly rather than let pass.

## Reading order

- **`RECORDS.md`** — description only, `R15.01`–`R15.11`.
- **`FLAWS.md`** — judgement, `F15.01`–`F15.06`.

## ⚠ Scope

Shipped data only, from `DF/DAGGER/ARENA2/`, plus one cross-reference to KOTOR
2's shipped `UTD` blueprints and two to this project's own design documents.
**No reimplementation source was read** — Daggerfall Unity is not on this
machine, and nothing here is borrowed from it. Daggerfall was **not run**.
