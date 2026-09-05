# STUDY 01 — CONTAINER LAYER

How files are packaged, found, and prioritised, in KOTOR 1 and KOTOR 2.

**Deliverables in this folder**

| file | what it is |
|---|---|
| `RECORDS.md` | the six type records — KEY, BIF, ERF, RIM, MOD, SAV |
| `README.md` | this file — lookup, precedence, load order, K1/K2 summary |
| `FLAWS.md` | batch-1 design problems, each citing a record |
| `NAMING.md` | batch-1 vocabulary table |

`FLAWS.md` and `NAMING.md` are **batch-scoped** and written to merge upward into
study-wide catalogues once later batches land. They are here rather than at
`STUDY/` level because the brief said to commit this batch's work to
`STUDY/01-container/`.

**Method.** Every structural claim below was read from the shipped files with
parsers written for this pass (`arch2.py`, kept out of the repo). Nothing is
taken from community documentation. Where a claim is inferred rather than read,
it says so inline. Negatives name what was searched.

---

## 1 · The archive types, and why there are five of them

| type | signature | index shape | writable | why it exists separately |
|---|---|---|---|---|
| KEY | `KEY ` | two tables: BIFs, resources | no | one index for the whole read-only layer |
| BIF | `BIFF` | offset table, **no names** | no | bulk storage; names deliberately externalised |
| RIM | `RIM ` | one 32-byte table, ResType **u32** | no | simplest possible named archive |
| ERF | `ERF ` | split key + resource arrays, ResType **u16** | no | named archive with a localisation header |
| MOD | `MOD ` | **identical to ERF** | by convention | a module as one self-contained file |
| SAV | file says `MOD `; entries use type 2057 | identical to ERF | yes | the mutable half of the world |

**Where they overlap, and which wins.**

- **RIM vs ERF** overlap almost entirely in purpose — both are named archives of
  module content. They are **not byte-compatible**: RIM stores ResType as u32,
  ERF as u16, and ERF carries a localisation header RIM lacks. K2 uses both at
  once, for different resource types in the same module
  (`262tel_s.rim` + `262tel_dlg.erf`). Neither "wins"; the split is by content
  kind, not by capability.
- **ERF vs MOD** do not overlap in purpose — they are **the same format**. Only
  the four signature bytes differ. MOD wins wherever a module must be one file.
- **BIF vs everything** — BIF is the only nameless one, and the only one needing
  an external index. Everything else is self-describing.

Full detail, per type, in `RECORDS.md`.

---

## 2 · Lookup — how a ResRef becomes bytes

The engine uses a **namespace-prefixed virtual path scheme**. These literals are
present in both binaries:

```
HD0:chitin  HD0:CHITIN  HD0:TEMP        the KEY/BIF layer
OVERRIDE:   OVERRIDE:textures           the Override folder, incl. a subfolder
MODULES:    modulesave                  the modules folder
RIMS:  RIMS:GLOBAL  RIMS:CHARGEN  RIMS:MAINMENU
LIPS:  LIPS:localization  LIPS:%s_loc
SAVES:  SAVES:%06d - %s
CURRENTGAME:   GAMEINPROGRESS:   GAMEINPROGRESS:INVENTORY / :PC / :REPUTE
MOVIES:  MOVIES:%s     ERRORTEX:   DTEMP:pifo   SERVERVAULT:
RIMSXBOX                            (K1 only)
```

Two things follow from these directly.

**The lookup key is `(ResRef, ResType)`, and nothing else.** No path, no
extension, no archive name. `LIPS:%s_loc` shows a companion archive's name being
*derived* from the module name by format string rather than stored anywhere.

**There is one flat table, not a chain of indexes.** The engine's resource
manager is `CExoKeyTable`, and it carries exactly two diagnostics, both present
in both binaries:

```
CExoKeyTable::AddKey: Duplicate Resource
CExoKeyTable::DestroyTable: Resource %s still in demand during table deletion
```

So archives are **registered into one shared key table**, duplicate keys are
detected at registration time, and resources are reference-counted. The KEY file
sits inside this as *one contributor among several* — it is the index for the
BIF layer only, not the index for the game.

**What I could not establish:** the registration order, and whether `AddKey`
rejects a duplicate or replaces it. Both determine precedence and neither is
readable from the shipped files. This needs a disassembly or the running game.

---

## 3 · ⚠ Override precedence — what is proven, and what is folklore

This is the batch's most important question, so the standard of evidence is
stated explicitly.

**The shipped data cannot show precedence directly.** What it *can* show is
**necessity**: if a layer ships a file that shadows another layer's copy **with
different bytes**, then that layer must win, or the file would be inert and
shipping it pointless. Every relation below rests on that argument.

### Forced by the shipped data

| relation | evidence |
|---|---|
| **`patch.erf` > BIF** (K1) | 11 of its 97 entries shadow BIF resources; **10 of the 11 differ in bytes**. `keymap.2da` grows 79 → 80 rows, `bindablekeys.2da` 85 → 103 rows. A patch that loses to the thing it patches is not a patch. |
| **Override > BIF** | K2 ships 10 override files that shadow BIF copies and **all 10 differ** — `handmaiden.dlg` 1,371,033 → 1,372,903 b; `gui_scroll.wav` 188 → 1,964 b; four GUI panels; three MDLs. K1's install carries a TSLPatcher-installed `spells.2da` differing from the BIF copy. |
| **module > BIF**, for the shadowed set | K1: 354 module resources also exist in the BIF layer and **189 occurrences differ** (163 NCS, 21 DLG, 3 UTC, 2 UTI). K2: **105 differ** (52 NCS, 27 UTP, 20 UTI, 3 DLG, 2 UTT, 1 UTC). Module-local copies that differ are only meaningful if the module copy is used. |
| **Override > `rims/`** (K1) | the installed `spells.2da` shadows a copy in `rims/global.rim` as well as the BIF copy. |

Concrete, from `patch.erf` vs BIF:

```
keymap           2DA   bif=  6555   patch=  6807   rows 79  -> 80
bindablekeys     2DA   bif=  2745   patch=  3258   rows 85  -> 103
skills           2DA   bif=  1218   patch=  1220   rows  8  -> 8    (values only)
abilities        GUI   bif= 14906   patch= 16597
character        GUI   bif= 42691   patch= 44382
equip            GUI   bif= 30331   patch= 32022
inventory        GUI   bif= 13501   patch= 15192
mainmenu         GUI   bif= 11386   patch= 11354
w_Lghtsbr_008    MDL   bif= 52323   patch= 52323   same size, differs at byte 36
weapondischarge  2DA   bif=  2801   patch=  2801   same size, 64 rows both
```

*(Incidental, and it corroborates a separate finding: `patch.erf` retunes
`skills.2da` without changing its row count. Even the official patch did not add
a skill.)*

### NOT established — say so rather than guessing

**The relative order of Override, module, and `patch.erf` is unknown.** All
three beat the BIF layer. Nothing in the shipped data ranks them against each
other, because the necessity argument only works against BIF.

The shipped install *does* contain genuine multi-layer collisions, which proves
the engine must have a rule — but not what the rule is:

```
K1  Override    <-> rims/         1   spells.2da
K1  modules/    <-> rims/        10   g_i_credits002, k_def_ambmob, k_hjuh_com01 …
K1  rims/       <-> patch.erf     2   skills.2da, weapondischarge.2da
K1  patch.erf   <-> texturepacks 75   pfha01, pfha01d, pfha01d1 …
K2  Override    <-> modules/      0
K2  Override    <-> texturepacks  0
```

**Whether precedence is per-file, per-type, or per-location is also unknown.**
The `CExoKeyTable` design points at **per-location, resolved once at
registration** — one flat table keyed on `(ResRef, ResType)`, with a duplicate
check at insert. That is an inference from two diagnostic strings and a class
name, not a reading of the resolution code. I found **no evidence of a per-type
rule**: searched both binaries for per-extension or per-restype exclusion
strings near the namespace literals and near `CExoKeyTable`, and found none.
That negative is weak — absence of a diagnostic is not absence of a branch.

**What would settle it:** a disassembly of the resource-manager startup path, or
controlled experiments against the running game (place the same differing file
in two layers and observe). Neither was in scope here.

### One structure that is *not* precedence

The three texture packs `swpc_tex_tpa/tpb/tpc.erf` carry **identical ResRef
sets** — 3,294 each in K1, 3,286 each in K2, 100% mutual overlap — and are
**disjoint from the BIF layer** (0 overlap). These are quality tiers **selected
between**, not layers stacked. Reading them as a precedence chain would be a
mistake.

---

## 4 · Load order and lifetime

Weaker evidence than the rest of this batch. What the files support:

**Phase-named preloads exist and are addressed by name.** `RIMS:GLOBAL`,
`RIMS:CHARGEN`, `RIMS:MAINMENU` are literals in both binaries, matching K1's
`rims/global.rim`, `chargen.rim`, `mainmenu.rim`. So a set of archives is
associated with game phases rather than discovered by scanning.

**The global set is large and duplicated.** K1's `rims/` holds 1,192 distinct
resources and **every one also exists in the BIF layer** — 1,192 of 1,192. Of
those, 1,910 of 1,936 occurrences are byte-identical to the BIF copy; the 26
that differ resolve to **13 distinct 2DA tables**, and the difference is
**purely the column-header delimiter** — the BIF copies separate headers with
`\t`, the `rims/` copies with `\0`. Same content, two serialiser conventions.

**Module state persists across transitions and is written out.** A save holds
one nested `{ARE, GIT, IFO}` snapshot per *visited* module — 20 of them in the
autosave read. So a module's dynamic layer survives leaving it. `currentgame/`
holds a single `.mod` for the active module and `gameinprogress/` holds loose
live records (`AVAILNPC0.utc`, `AVAILNPC1.utc`), with matching
`CURRENTGAME:` / `GAMEINPROGRESS:` literals in both binaries.

**What I could not determine:** what is held in memory versus discarded at an
area transition. Residency is a runtime property and leaves no trace in the
files. The reference-counting diagnostic
(`Resource %s still in demand during table deletion`) shows resources are
counted and torn down in bulk, which implies a lifetime scope wider than a
single request — but the scope's boundary is not readable here. **Needs the
running game.**

---

## 5 · K1 vs K2 — the container-layer differences found

Recorded per-type in `RECORDS.md`; collected here for reference.

| dimension | K1 | K2 |
|---|---|---|
| BIFs | 26, ~1,255 MB, lightmaps split 13 ways | 11, ~1,186 MB, consolidated; adds `scripts.bif`, `sounds.bif` |
| KEY resources | 25,836 | 18,439 |
| KEY drives mask | `0x0001` | `0x0000` |
| `rims/` | **12 files, 37.2 MB**, with `dx` twins | **absent** |
| `patch.erf` | **present**, 97 entries | **absent** |
| module dialogue | inside `_s.rim` — **113 of 117** contain DLG; **0** `_dlg.erf` | **0 of 82** `_s.rim` contain DLG; **82** `_dlg.erf` |
| `modules/` shapes | `.rim` + `_s.rim` + **40 `.mod`** | `.rim` + `_s.rim` + `_dlg.erf` only |
| `lips/` | 123 `.mod`, **14 empty** | 77 `.mod`, **2 empty** |
| Override (shipped) | 0 files shipped (this install has a user-installed mod) | **60 files**, 10 shadowing BIF content |
| Xbox namespace | `RIMSXBOX` literal present | absent |
| console text files | — | `override/custom.txt`, `override/gamepad.txt`, `override/mobile.txt` |

**Both claims in the brief were checked. One is confirmed, one needs correcting.**

- ✅ *"K1 puts dialogue inside `_s.rim` while K2 uses a separate `_dlg.erf`"* —
  confirmed exhaustively, counts above.
- ⚠ *"40 K1 modules ship as `.mod` rather than paired `.rim`"* — there are 40
  `.mod` files, but **34 of them also have a `.rim` pair**. Only **6** are
  `.mod`-only: `unk_m41ae`, `unk_m41af`, `unk_m41ag`, `unk_m41ah`, `unk_m41ai`,
  `unk_m41aj` — the Rakata endgame set. Of the 34 that coexist, **12 hold the
  same resource set** as the pair, **21 are a strict superset**, 1 is neither.
  So `.mod` in K1 is predominantly a **duplicate** of the pair, not a
  replacement. Which one loads when both exist is unknown and matters.

---

## 6 · Scope — what was and was not checked

**Read and parsed:** `chitin.key` and all 37 BIFs across both games; K1
`patch.erf`; all 8 texture packs; all 12 K1 `rims/` archives; all 398 K1 and 246
K2 `modules/` archives; all 200 `lips/` archives; K1 `Saves/000001 - AUTOSAVE/`
including the nested module snapshots; K1 `currentgame/` and `gameinprogress/`;
both game binaries via string extraction.

**Byte-compared across layers:** every shadowing pair in
patch↔BIF, rims↔BIF, modules↔BIF, Override↔BIF, and all pairwise layer
intersections.

**Not checked:**
- Any running process. No claim here about residency, registration order, or
  which file wins a live collision.
- Disassembly of the resource manager. All engine claims come from string
  literals and class names.
- K2 save files — **none present in this install**. The SAV record is K1-only
  and should not be assumed to hold for K2.
- The internals of `GLOBALVARS.res`, `PARTYTABLE.res`, `savenfo.res`, `pifo.ifo`
  — GFF-family by magic, deferred to batches 2 and 4.
- `streamwaves/`, `streammusic/`, `movies/` — audio and video containers,
  deferred to batch 6.
- NWN's container layer — scoped to batch 7 per the study plan.
