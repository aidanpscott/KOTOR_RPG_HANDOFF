# STUDY 16 — judgement

Records in `RECORDS.md`, cited by number.

---

## F16.01 · ⚠ Our tree's categories are wrong, and the shape of the error is specific

Loom shows `areas · characters · quests · scripts`. That came from the package
**folders**, and folders are storage. **Aurora's vocabulary is not a folder
list** (`R16.04`):

```
Areas
Conversations
Blueprints
   Creatures · Doors · Encounters · Items · Placeables ·
   Sounds · Stores · Triggers · Waypoints
Scripts
```

**Three concrete corrections:**

- **`characters` is wrong as a top-level.** Aurora has no Characters branch. It
  has **Blueprints**, and creatures are one kind under it. Ours flattened a
  parent away.
- **`conversations` is missing entirely**, and it is a peer of Areas — not a
  sub-thing. Given `TRACE-87` found dialogue carries more attachment points than
  every object hook combined, **that is the wrong branch to have omitted.**
- **`quests` has no Aurora counterpart at this level.** Its journal is edited
  through a `Tools` dialog (`STUDY 14`), not browsed in the tree.

**⚠ And `scripts` survives, which I did not expect.** `R16.05`: Scripts appear
under both "Unused" and "Compile" as a peer of Areas and Conversations. **Our
guess was right for the wrong reason** — it came from a folder, and it happens to
match a real category.

## F16.02 · ⚠ The tree nests area → contents. Inferred, and I will say how strongly

**Four independent signals, none conclusive alone:**

1. **`OnExpanding`** (`R16.01`) — a handler that exists to fill children on
   demand. **A flat list has no use for it.**
2. **One action, two captions** (`R16.02`) — `actGoto` is shown as *"View Area"*
   and as *"Focus on Object"*. **Two node kinds in one tree.**
3. **`actLocationAdjust` "Adjust Location"** — meaningless on anything but a
   placed instance, and `actRescanInstances` is captioned **"Refresh Area"**.
4. **`TdlgFindInstance` filters "In Area"** (`R16.07`) — instances are addressed
   *within* an area.

**So: area nodes that expand to their placed contents. I did not find a
design-time node proving it**, because there are none, and I am not going to
present four consistent hints as a fact.

**⚠ And `R16.08` is why it has to nest.** An Aurora area is **2 to 32 tiles a
side, up to 1,024 tiles**, where a tile is a room-sized chunk. **An area is a
dungeon level, not a room.** A flat module-wide list of every creature in a
twelve-area module is not a thing anyone could use — which is also why
`TdlgFindInstance` exists at all.

**⚠ THE OWNER'S POINT IS CORRECT AND THE EVIDENCE IS THE AREA SIZE.** "An area
is not a room" is not a design preference here; it is what 32×32 tiles means.

## F16.03 · The palette and the tree differ, and the difference is exactly the interesting part

**They are not two views of one thing.**

| | Palette | Tree |
|---|---|---|
| Creatures, Doors, Encounters, Items, Placeables, Sounds, Stores, Triggers, Waypoints | **yes, all nine** | yes, under Blueprints |
| Terrain | **yes, Standard only** | no |
| Areas | **no** | yes |
| Conversations | **no** | yes |
| Scripts | **no** | yes |

**⚠ The palette is exactly the `Blueprints` subtree, plus Terrain** (`R16.06`
against `R16.04` — same nine names, no additions, no omissions). That is not a
coincidence; **it is the same list rendered twice for two jobs.**

**The brief's framing is confirmed by the data: the palette is what you can
MAKE, the tree is what this module HAS** — and the three the tree adds are
precisely the things you do not paint. You do not paint an area, a conversation
or a script.

**⚠ And there is one door between them: `actAddToPalette`** (`R16.02`). The tree
can push into the palette. **One direction only** — nothing in the palette adds
to the tree, because placing is what does that.

## F16.04 · ⚠ Haks belong to properties, and that is our dependency answer

`R16.09` is the cleanest transfer in this study. Aurora's custom content —
**haks and the custom TLK** — lives in **Module Properties → Custom Content**,
as a list with **Add, Remove, Move Up, Move Down** and a conflict checker.

**⚠ Move Up and Move Down. It is an ordered list, hand-ordered, in a properties
dialog.** That is `PACKAGE-FORMAT-01 §4`'s `[requires].packages` — *"One ordered
list. Later entries win. That is `Mod_HakList`, and it is the whole mechanism"* —
and here is its interface, shipped.

**So the answer to "where do tilesets, rules and dependencies sit" is: NOT THE
TREE.** They sit in package properties, and `BUILDER-VISION-01 §6` already ruled
dependencies off the creation path and into properties for an unrelated reason.
**Two roads to the same place is a good sign.**

**⚠ Two of our four have no Aurora counterpart at all.** The **manifest** is a
file Aurora never had — its equivalents are scattered across `Module Properties`
tabs, which is what `PACKAGE-FORMAT-01 §1` corrects by making the manifest
authoritative. And **strings**: Aurora's TLK is a single global table selected in
properties, which `PACKAGE-NAMING-01 §1` explicitly rejects.

## F16.05 · ⚠ Aurora's palette IS the shape you want. Copy it

**The palette question, answered from the data rather than invented.**

`R16.06`: the palette is **two axes crossed** — `Standard | Custom` × nine
categories, each tab holding a tree of entries.

**Map that onto the distinction in the brief:**

| Aurora | Ours |
|---|---|
| the nine category tabs | **TYPE** — floor, wall, water, difficult, hazard |
| the entries inside a tab | **VARIETY** — deck plating, grating, scorched deck |
| `Standard` vs `Custom` | **shipped vs this package's own** |
| *(nothing)* | **VARIANT** — engine-picked, author never sees |

**⚠ So Aurora already solved the organisation and we should not invent one.** A
category holds many entries; you pick an entry; the category is the mechanics
and the entry is the thing. **That is variety-grouped-by-type, built in 2002.**

**Two differences worth naming before copying:**

- **⚠ Aurora's palette entries are BLUEPRINTS — they carry rules.** A creature
  in the palette has statistics. **Ours would carry only art**, because
  `PT-1361` fixes the vocabulary and a tileset "supplies pixels and prefabs
  against a vocabulary that already exists". **Ours is the safer version of the
  same shape**, and it is why a stranger's tileset cannot break a package.
- **Terrain is Standard-only and sits outside the nine** (`R16.06`). Aurora
  separated *the tiles you paint the ground with* from *the objects you place on
  it*, and put custom content on the object side only. **Our tiles are the
  Terrain tab, and our varieties are the thing Aurora did NOT allow to be
  custom.** That is a deliberate departure, not a copy.

**⚠ And the five-looking palette today is correct, not a placeholder.** With no
tileset there is exactly one variety per type — the drawn look from `PT-1364` —
so five types show five entries. **The structure does not change when a tileset
arrives; the lists get longer.**

---

## Judgements about our own design, kept separate

**On the tree, what I would change.** `areas` and `scripts` stay. `characters`
becomes a child of a **blueprints** parent alongside placeables, doors, items
and the rest. `conversations` is added as a peer of areas. `quests` I would
leave out until something needs it, because Aurora's counterpart is a dialog and
ours is a folder that may never be browsed.

**⚠ But the nesting is the bigger change and it is not free.** If areas expand
to their contents, the tree needs the contents to exist — and nothing is placed
until `4d`. **The tree cannot be finished before the thing it lists.** Doing the
categories now and the nesting at `4d` is the order the build rule implies.

**A caution.** Everything in `F16.01` and `F16.02` rests on `R16.04`, and
`R16.04` is the **Verify dialog's** vocabulary, not the tree's. It is the best
evidence in the binary and it is not the same thing as reading the tree's node
list, which does not exist to be read. **If this drives a rebuild of the tree,
somebody should open the toolset once and look at the pane** — the same
ten-minute check `STUDY 14` wanted for a different number.
