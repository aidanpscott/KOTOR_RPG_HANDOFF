# STUDY 15 — Daggerfall's blocks: records

**Description only.** Judgement is in `FLAWS.md`.

## ⚠ Evidence classes

- **DATA** — parsed from the shipped files in `DF/DAGGER/ARENA2/`. Where a parse
  is self-validating (an archive whose records end exactly where its directory
  begins) that is stated, because it means the reading is not a guess.
- **CROSS** — read from another shipped game in this project's corpus, named.
- **⚠ COULD NOT DETERMINE** — attempted and not established. **No
  reimplementation source was read.** Daggerfall Unity is not present on this
  machine and nothing below is taken from it; where I could not get a layout out
  of the bytes, it says so rather than borrowing an answer.

---

## R15.01 · The archives, and why the parse can be trusted

**DATA.**

```
BLOCKS.BSA   32,884,997 bytes   1,295 records   name directory (0x0100)
MAPS.BSA     22,129,312 bytes     248 records   name directory (0x0100)
```

A Daggerfall BSA is a 4-byte header, then the records, then a **directory at the
end of the file** — 18 bytes per entry for a name directory (14-byte name, then
a `UInt32` size).

**⚠ Both archives are self-validating.** Walking the record sizes from offset 4
lands **exactly** on the first byte of the directory, with no slack in either
file. A wrong stride or a wrong header size would not do that.

## R15.02 · What ships: 920 exterior blocks, 187 dungeon blocks

**DATA.** `BLOCKS.BSA` holds four kinds:

| Extension | Count | Size range | Median |
|---|---|---|---|
| `.RMB` | **920** | 6,776 – 95,708 | 28,227 |
| `.RDB` | **187** | 10,928 – 52,514 | 22,987 |
| `.RDI` | **187** | **exactly 512, every one** | 512 |
| *(none)* | 1 | 52,350 | — a record named `FOO` |

**⚠ `RDI` is 1:1 with `RDB` and is always exactly 512 bytes.** A fixed-size
companion record per dungeon block. What it holds was not established.

**⚠ RMB and RDB are VARIABLE-SIZE on disk** — a fourteen-fold range for RMB.
Whatever a block's footprint is in the world, its file is not fixed-length.

## R15.03 · The names are a scheme, and the scheme is legible

**DATA.** RMB names run `TTTTVS##.RMB` — four letters of function, a variant
letter, a size letter, a two-digit number.

Function codes observed across the 920:

```
ALCH alchemist   ARMR armourer    BANK bank        BOOK bookseller
CARN carnival?   CAST castle      CLOT clothier    CUST custom?
DARK dark?       DUNG dungeon     FARM farm        FIGH fighters guild
FILL filler      FURN furniture   GEMS gem store   GENR general store
GRVE graveyard   LIBR library     MAGE mages guild MANR manor
MARK market      PALA palace      PAWN pawnbroker  RESI residence
RUIN ruin        SENT sentinel?   SHIP ship        SHRI shrine
TEMP temple      THIE thieves     TVRN tavern      WALL wall
WEAP weaponsmith WITC witch       WYRS wyrd?       WAY  waypoint?
```

**The size letter is real and is confirmed by triples.** `TVRNAS`/`TVRNAM`/
`TVRNAL`, `RESIAS`/`RESIAM`/`RESIAL`, `GENRAS`/`GENRAM`/`GENRAL` — small,
medium, large of the same thing, all present.

**⚠ And the archive ships debris.** Names that are plainly not content:
`FOO`, `FOOBAR`, `FOOBGR`, `SHIT`, `BRUCE`, `LYSAN`, `TEST`, `TEMP`, `TMP`,
`BACKUP`, `AAANEW`, `ZZZZZZZ`, `DIR`, `AVI`, `SI`, `SCO`, `LLU`, `SHE`, `HAL`,
`BLOCK`, `BLOCKHAL`, `NASYLUM`. **Roughly twenty of 1,295 records are somebody's
working files, shipped.**

## R15.04 · An RMB carries objects, not only geometry

**DATA.** Every RMB opens with the same four bytes:

```
UInt8   number of block data records
UInt8   number of misc 3D object records
UInt16  number of misc flat object records
```

`TVRNAS00.RMB`: **12 block data records, 4 misc 3D objects, 21 misc flat
objects.**

**⚠ A block is not a shell.** Two of the three counts in its very first four
bytes are object counts, and one of them counts *flats* — Daggerfall's
billboarded sprites, which is what furniture, clutter and people are.

## R15.05 · ⚠ Rotation is in the format, and it is two bits

**DATA, and this is the strongest single finding in the study.**

After the 4-byte header, every RMB carries a **32-entry table, 4 bytes per
entry**, read as two `UInt16`s. Across **all 920 files — 29,440 entries** — the
second `UInt16` takes these values and no others:

```
0x0000   16,118
0x4000    3,154
0x8000    6,492
0xC000    3,674
0x00FF        2      ← both in the junk records
```

**Four values, in the top two bits. That is a quarter-turn field**: 0°, 90°,
180°, 270°.

The first `UInt16` of each entry has **20 distinct values in the range 0–14**
across the whole archive — a small enumeration, not an offset or a size.

**So a block is composed of placed pieces, each carrying a rotation**, and the
same piece is reused at four orientations rather than authored four times.

## R15.06 · How a place is described

**DATA.** `MAPS.BSA` holds **62 regions × 4 files**:

```
MAPTABLE.nnn   an index of the region's locations
MAPPITEM.nnn   the locations themselves
MAPDITEM.nnn   dungeon layouts
MAPNAMES.nnn   names
```

**`MAPTABLE` is a flat array of 17-byte records**, confirmed by exact division:
region 000 is 5,848 bytes → **344 records**; region 001 is 15,504 → **912**.
No remainder in either.

**⚠ Region `.002` is four empty files.** A region slot with no locations at all.

**`MAPPITEM` opens with a `UInt32` offset table, one entry per location**, whose
values are relative to the end of that table. Region 000: 344 offsets, so the
first location record begins at byte 1,376, which is where offset `0` points.

## R15.07 · ⚠ A location record begins with a DOOR LIST

**DATA.** Every location record starts:

```
UInt32  door count
        door count × 8 bytes
        then the location header, then a 32-byte name buffer
```

Confirmed by arithmetic that only works one way: region 000's first location
declares **23 doors**; at `4 + 23×8` bytes past the start, the header begins and
the name **"Caarcun Manor"** appears at a fixed offset within it. A wrong door
stride moves the name.

**Door counts across region 001's 912 locations:**

```
0 doors    310 locations     ← a third have none at all
1 door     142
2 doors     62
24–33      ~250 combined     ← the towns and cities
maximum    326
```

**⚠ Doors are recorded at the LOCATION, not in the block.** The block is the
shape; the door list belongs to the placed instance of it.

**⚠ COULD NOT DETERMINE:** the eight bytes of a door record do not decompose
cleanly under any field split I tried. The **length** is established; the
**fields** are not. The first `UInt16` behaves like an index into something
per-location, but I could not confirm what.

## R15.08 · The location also carries a per-building list

**DATA, partially.** After the door list, region 001's largest location contains
**305 consecutive fixed-length 26-byte records**, anchored by a `UInt16` that is
constant within that location and varies between locations. Each record carries
a small ascending value in its first field and a byte in the range **5–20** with
16 distinct values across the location.

**⚠ COULD NOT DETERMINE, and I want this stated plainly rather than dressed up:**
the anchor I used is location-specific, so the same scan **did not generalise to
the other 911 locations**, and I could not identify the fields. What is
established is that a location carries a **flat array of fixed-size per-building
records separate from any block file**. What each field means is not.

## R15.09 · ⚠ COULD NOT DETERMINE — how blocks are addressed into a grid

**The central mechanism of question 2, and I did not get it.**

I could not locate, within the location record, the arrays that name which block
sits at which cell. I attempted: a fixed offset after the name buffer, scanning
for 64-byte runs of small values, and reconstructing candidate block names to
test against the 920 known ones. **None validated.**

**So the following are NOT established by this study:** whether a city is an 8×8
grid, whether the grid is fixed or ragged, what selects a block per cell, and
whether that selection is seeded or stored. **`MAPDITEM` — the dungeon side of
the same question — was not parsed at all.**

**What IS established** is that block identity must be *stored per location*
rather than derived at runtime, because the location records are large
(region 001's biggest is 10,919 bytes) and the archive ships 920 named blocks
that something must choose between.

## R15.10 · CROSS — how Aurora's descendant answers the door question

**CROSS, from KOTOR 2's shipped blueprints** (Odyssey, Aurora's descendant;
`STUDY/12` and `STUDY/14` establish the toolset lineage). **104 `UTD` door
blueprints ship in the BIFs.** A sample, `door_dan01` — "Peragus Door 4" —
carries **56 fields**:

```
lock        Lockable · Locked · KeyRequired · KeyName · AutoRemoveKey
            OpenLockDC · CloseLockDC · OpenLockDiff · OpenLockDiffMod
damage      HP · CurrentHP · Hardness · Min1HP · NotBlastable · Plot · Static
trap        TrapFlag · TrapType · TrapOneShot · TrapDetectable · TrapDetectDC
            TrapDisarmable · DisarmDC
saves       Fort · Ref · Will
identity    Tag · TemplateResRef · LocName · Description · Comment · Appearance
            GenericType · PortraitId · Faction · Conversation
state       OpenState · AnimationState · Interruptable · LoadScreenID
scripts     OnOpen · OnClosed · OnClick · OnLock · OnUnlock · OnFailToOpen
            OnDamaged · OnDeath · OnMeleeAttacked · OnSpellCastAt · OnDisarm
            OnTrapTriggered · OnHeartbeat · OnUserDefined
```

**Sixteen script hooks and nine lock fields on one door.** `STUDY/14` found the
Aurora toolset ships a **Door Wizard** (`TdlgDoorWizard`, 4 pages) and a
separate door editor, so a door is an authored blueprint type with its own
creation path.

## R15.11 · CROSS — what our own format has today

**CROSS, `AREA-FORMAT-01 §4`:**

```toml
[[connections]]
tag   = "door.command-deck.aft"
at    = [23, 9]
to    = "a02-taris-hideout"
lands = "arrival.north"
```

**A position, a destination, and a named arrival point. No lock, no key, no
hit points, no scripts, no open state.**

**⚠ And `§5` already anticipates the gap** in its own words: *"This is the rule
most likely to be broken first, because a door has an obvious open/closed and it
is tempting to put it here. The door's authored state is its starting state;
everything after is an event."*

The example's `tag` is literally `door.command-deck.aft` — the format calls the
thing a door while modelling only its connection half.
