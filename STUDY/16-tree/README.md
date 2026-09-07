# STUDY 16 — Aurora's module tree

`STUDY 12` located the pane and never opened it. This opens it, and answers the
two design questions sitting under it.

---

## The short version

**The tree's node list does not exist to be read** — `tvMain` has zero
design-time nodes and no bound ImageList, and the 428-entry string table is
**all VCL runtime strings**, not one toolset category among them.

**But one form enumerates a module's contents as a structure**, and its
checkboxes carry stable tag numbers:

```
Areas
Conversations
Blueprints
   Creatures · Doors · Encounters · Items · Placeables ·
   Sounds · Stores · Triggers · Waypoints
Scripts
```

## What this changes for Loom

Loom shows `areas · characters · quests · scripts`, taken from the package
folders. **Folders are storage, not a tree.**

- **`characters` is wrong as a top level.** It belongs under a **blueprints**
  parent with placeables, doors, items and the rest.
- **`conversations` is missing**, and it is a peer of areas — the wrong branch to
  have omitted, given `TRACE-87`.
- **`quests` has no Aurora counterpart** at this level.
- **`scripts` survives** — right guess, wrong reason.

## The four findings

**1 · ⚠ THE TREE NESTS AREA → CONTENTS, and the evidence is the area size.**
`OnExpanding` for lazy children; one action captioned both *"View Area"* and
*"Focus on Object"*; *"Adjust Location"* and *"Refresh Area"*; and a Find
Instance dialog that filters **"In Area"**. Aurora's areas are **2 to 32 tiles a
side, up to 1,024 tiles**, where a tile is a room-sized chunk. **An area is a
dungeon level, not a room** — so a flat module-wide list of instances was never
viable.

**2 · THE PALETTE IS EXACTLY THE `Blueprints` SUBTREE, PLUS TERRAIN.** Same nine
names, no additions, no omissions. The tree adds Areas, Conversations and
Scripts — **precisely the things you do not paint.** One door between them:
`actAddToPalette`, tree → palette, one direction.

**3 · ⚠ HAKS LIVE IN PROPERTIES, IN AN ORDERED LIST WITH MOVE UP / MOVE DOWN.**
Not the tree. That is `PACKAGE-FORMAT-01 §4`'s ordered `[requires].packages`
with its interface already shipped — so tilesets, rules and dependencies are
**package properties, not tree branches**, which is where
`BUILDER-VISION-01 §6` independently put them.

**4 · ⚠ AURORA'S PALETTE IS ALREADY THE VARIETY SHAPE — COPY IT.**
`Standard | Custom` × nine categories, each holding a tree of entries. A category
is the **type**; an entry is the **variety**. Built in 2002.

Two differences before copying: Aurora's entries are **blueprints and carry
rules**, where ours would carry only art — `PT-1361` makes ours the safer version
of the same shape. And **Terrain is Standard-only**, so Aurora never let terrain
be custom content; our varieties are exactly the thing it refused.

**The five-looking palette today is correct.** With no tileset there is one
variety per type. The structure does not change when a tileset arrives; the
lists get longer.

## Reading order

- **`RECORDS.md`** — description only, `R16.01`–`R16.09`.
- **`FLAWS.md`** — judgement, `F16.01`–`F16.05`.

## ⚠ Scope, and the one caveat that matters

Binary inspection of Beamdog EE `1.5.0.5`. **The toolset was not run.**

**The category list comes from the VERIFY MODULE dialog, not from the tree.** It
is the only place in the binary that enumerates a module's contents as a
structure, and nothing in any form stream ties it to `tvMain`. It is the
strongest available evidence and it is not the same as reading the tree's nodes,
which **do not exist to be read**. If this drives a rebuild, open the toolset
once and look at the pane.
