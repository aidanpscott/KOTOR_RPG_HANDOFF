# STUDY 07 — TOOLSET AND GAME — RECORDS

Five records — MOD/NWM, HAK, custom TLK, GIC, ITP — on the template from
`STUDY/README.md`.

---

## ⚠ What I actually have, stated first

**The toolset is installed but not runnable here.** This is a Linux install of
the Steam NWN Enhanced Edition. The Windows binaries are present and readable:

```
bin/win32/nwtoolset.exe      12.2 MB   the Aurora toolset
bin/win32/nwhak.exe           3.3 MB   the hak packer
util/win32/GFFEditor.exe      0.8 MB   a raw GFF editor
bin/linux-x86/nwmain-linux             the game (runnable, not run)
```

**So everything below about the toolset's *behaviour* comes from two sources:
the files it produced, and string extraction from its binary.** I did not launch
it, did not build a module, and did not observe a save or an export. Where a
claim depends on running it, the record says so.

**What I could read properly, and it is a lot:**

```
data/nwm/   16 official campaign modules   322 MB
data/mod/   14 community modules            73 MB
data/hk/    18 haks                        525 MB
data/tlk/    4 custom string tables         14 MB
data/ovr/ + ovr/   1,389-file override, including a KOTOR conversion
```

30 modules opened in full. That is a better sample than the shipped game gives
for KOTOR, because these are *authored artifacts*, not just runtime data.

---

## MOD / NWM — the module

**WHAT IT IS** A complete adventure in one file: areas, blueprints, dialogue,
scripts, quests — **and the source those scripts were compiled from.**

**CONTAINER** Loose file. `data/mod/*.mod` for community work, `data/nwm/*.nwm`
for BioWare's campaigns. Both carry the signature `MOD ` — the `.nwm` extension
is a shelf label, not a format.

**STRUCTURE** ERF-family (batch 1). Contents of a real one, `Chapter2.nwm`:

```
7,229 resources   NSS 2,836 · NCS 2,834 · UTC 384 · DLG 278 · UTI 146
                  UTE 128 · UTS 124 · UTW 121 · ARE 79 · GIC 79 · GIT 79
                  IFO 1 · JRL 1 · ITP 9 · FAC 1
```

**⚠ The module carries its own source.** Across all 30 modules:
**26,317 NSS against 26,180 NCS.** 93% of modules ship source; the only two that
do not contain **no scripts at all**. Every official campaign module carries it.
NSS counts track NCS counts within a percent or two throughout.

**⚠ It also carries authoring data the game does not need:** a `GIC` per area
(comments), nine `ITP` palettes, `Mod_CacheNSSList`, `Mod_Creator_ID`,
`Mod_Version`.

**`module.ifo` — 51 distinct fields, 41 always present.** Shares 42 with KOTOR's
IFO. **Nine are NWN-only:**

```
Mod_HakList        ordered list of haks    Mod_CustomTlk    module's own strings
VarTable           NAMED module variables  Mod_CacheNSSList scripts to preload
Mod_MinGameVer     minimum engine version  Mod_OnPlrChat    player-chat hook
Mod_OnPlrEqItm     equip hook              Mod_OnPlrUnEqItm unequip hook
Mod_OnCutsnAbort   cutscene-abort hook
```

**One is KOTOR-only:** `Mod_VO_ID`.

`Mod_Area_list` holds **1 to 314 areas** — against KOTOR's always-exactly-1
(batch 4 F37).

**REFERENCES OUT** Haks **by name, in order**; a custom TLK **by name**; areas
**by resref**; 18 event scripts **by resref**.

**REFERENCED BY** The game's module selector; the toolset's file dialogs.

**SCOPE** **Self-contained.** This is the batch's point: a NWN module is a
portable unit that carries its content, its rules extensions (via haks), its
strings (via a custom TLK), its quests and its source.

**AUTHORED BY** A human in the Aurora toolset, working **directly on this file**
— see `README.md` §1.

**READ WHEN** Module load. Source is never read by the engine.

**SAMPLES**
| # | file | shape | why |
|---|---|---|---|
| 1 | `DEMO - KotOR Heads.mod` | 19 resources, 0 scripts, 2 areas | minimal — a content demo, no logic at all |
| 2 | `Chapter2.nwm` | 7,229 resources, 2,836 NSS | the large official one |
| 3 | `Aribeth_s Redemption III.mod` | 3,177 resources, **11 haks**, 110 areas | the large community one, deepest hak stack |
| 4 | `Neverwinter Nights - Pirates of the Sword Coast.nwm` | `VarTable[12]` with named string variables | oddity — module-scoped named config, which KOTOR cannot express at all |
| 5 | `DEMO-NWN2_voicesets.mod` | 14 resources, custom TLK `nwn2voicesets` | oddity — a module that exists only to carry a string table |

**UNKNOWN** Whether the toolset writes the `.mod` in place or via a temp file.
Would need to run it.

---

## HAK — the scoped content pack

**WHAT IT IS** A bundle of resources a module declares, which override the
game's own for that module only.

**CONTAINER** Loose file in `data/hk/`. Signature **`HAK `** — a **fourth**
signature on the ERF format, after `ERF `, `MOD ` and `SAV ` (batch 1 F06).

**STRUCTURE** Identical to ERF. 18 present, 547 KB to 193 MB.

**⚠ Haks carry 2DAs — this is the mechanism KOTOR lacks.**

```
wc_2da_shared.hak    30 2DAs   ambientmusic, ambientsound, baseitems,
                               classes, cls_feat_barb, cls_feat_bard,
                               cls_feat_cler, cls_feat_divcha …
potsc_top.hak        17 2DAs   appearance, baseitems, bodybag, doortypes,
                               IPRP_SPELLS, itempropdef, loadscreens …
prcc2.hak             8 2DAs   racialtypes, phenotype, traps, itemprops …
id_resources.hak     72 2DAs   SubTypeAzer, SubTypeDrow, SubTypeElf …
AribethRev1_CEP.hak  12 2DAs   appearance, parts_chest, parts_legs …
```

`classes.2da` and the per-class feat tables in a hak means **a NWN module can
redefine the class system for itself**. Batch 2 F18 found KOTOR has **zero**
module-local 2DAs anywhere.

Haks also carry every other resource type: `id_resources.hak` has 514 UTC, 396
UTI, 379 UTP, 314 ARE; `potsc_resources.hak` has 1,018 MDL and 669 WOK.

**⚠ Precedence is declared, ordered, and per-module.** `Mod_HakList` is a
**list** of `{Mod_Hak}`, and list order is the ranking. Observed usage across 30
modules: 20 declare none, 7 declare one, 1 declares two, 1 declares seven, 1
declares eleven.

The naming makes the intended order legible:

```
Aribeth_s Redemption III      Wyvern Crown of Cormyr
  [0]  cep2_top_v1              [0]  wc_top
  [1]  cep2_add_phenos2         [1]  wc_2da_shared
  …                             …
  [9]  cep2_core1               [6]  wc_tilesets
  [10] aribethrev1_cep
```

`_top` at index 0 and `_core` at the bottom in both. **Index 0 is highest
precedence.** That reading is **inference from the naming convention**, not from
the engine — I did not verify it against `nwmain`.

**REFERENCES OUT** Nothing. A hak is a bag.

**REFERENCED BY** `module.ifo`'s `Mod_HakList`, **by name and by position**.

**SCOPE** **Exactly the modules that name it.** This is the whole point.

**AUTHORED BY** `nwhak.exe`, shipped alongside the toolset.

**READ WHEN** Module load, in declared order.

**SAMPLES**
| # | file | shape | why |
|---|---|---|---|
| 1 | `aribeth_head.hak` | 2 resources — 1 MDL, 1 PLT | minimal — one head |
| 2 | `id_resources.hak` | 2,705 resources, 193 MB, 72 2DAs | the large one |
| 3 | `wc_2da_shared.hak` | 30 2DAs including `classes` | **the rules-override case** |
| 4 | `kotor_heads.hak` | 243 resources, 162 MDL | oddity — a KOTOR conversion living inside NWN |
| 5 | `potsc_top.hak` / `potsc_resources.hak` | 1,290 + 2,829 | oddity — one pack split by precedence layer, `_top` and `_resources` |

**UNKNOWN** Whether hak precedence outranks the override folder, and where the
base game sits in the order. Not established; needs the engine.

---

## Custom TLK — a module's own strings

**WHAT IT IS** A second string table, declared by a module, holding text the
base game does not have.

**CONTAINER** Loose file in `data/tlk/`.

**STRUCTURE** **Identical to the base TLK** — `TLK ` V3.0, language id, string
count, offset, then fixed 40-byte entries (batch 2). No format difference at
all.

```
dialog.tlk (base)     112,228 entries
prccep.tlk            192,501 entries   10.5 MB — larger than the base table
nwn2voicesets.TLK      2.07 MB
dla.tlk                1.19 MB
dla_bio.tlk              251 bytes      oddity — a near-empty table
```

**REFERENCED BY** `module.ifo`'s **`Mod_CustomTlk`** — a single resref naming
one table. Present as a field on 27 of 30 modules; **populated on 3**:
`cep2_v1`, `nwn2voicesets`, `dla`.

**How a StrRef selects base versus custom is not established here.** The
community convention is that a high bit (StrRef ≥ 0x01000000) selects the custom
table. Searching `nwmain.exe` for that constant and for alternate-TLK literals
returned only the field name `Mod_CustomTlk` itself. **So: the mechanism exists
and is declared per module; the selection rule is unverified in this study.**

**SCOPE** Per module, by declaration. Contrast batch 2 F23: KOTOR has **exactly
one** TLK per game and **no second-table mechanism** — a negative I scoped by
searching both install trees and both binaries.

**AUTHORED BY** A TLK editor, not shipped in this install.

**SAMPLES**
| # | file | why |
|---|---|---|
| 1 | `dla_bio.tlk` (251 b) | minimal — a table with almost nothing in it |
| 2 | `prccep.tlk` (192,501 entries) | larger than the base game's own table |
| 3 | `nwn2voicesets.TLK` | oddity — uppercase extension, and paired with a 14-resource module that exists only to declare it |

**UNKNOWN** The StrRef split rule, stated above.

---

## GIC — the area comment file

**WHAT IT IS** The author's notes about the things placed in an area, kept
**beside** the runtime data rather than inside it.

**CONTAINER** Inside the module, one per area.

**STRUCTURE** GFF. Its top-level fields **mirror the GIT's instance lists
exactly** — `Creature List`, `Door List`, `Placeable List`, `TriggerList`,
`WaypointList`, `SoundList`, `StoreList`, `Encounter List`, `List` — and each
entry contains **only** `Comment`.

So it is a parallel array: instance *n* in the GIT has its note at position *n*
in the GIC.

**769 GIC files against 772 ARE** across the 30 modules — near 1:1, three areas
lacking one.

**⚠ KOTOR has no GIC. Zero, anywhere** — searched both BIF layers and every
module archive in both games. KOTOR put `Comment` **on the runtime record
itself**: on every blueprint (batch 3 F31) and every one of 104,750 dialogue
nodes (batch 5 F50).

**REFERENCES OUT** Nothing — position-coupled to the GIT.

**REFERENCED BY** The toolset only. The game does not need it.

**SCOPE** Area-local.

**AUTHORED BY** The toolset, automatically.

**READ WHEN** Never by the engine. **Inferred** — nothing in the game binary
suggests a use, but I did not disassemble to confirm.

**SAMPLES**
| # | instance | why |
|---|---|---|
| 1 | `area.gic` from *Aribeth's Redemption II* | 31 waypoint comments, 14 door comments |
| 2 | the 3 areas with no GIC | oddity — the pairing is not enforced |
| 3 | any `Encounter List` entry with **no keys at all** | oddity — an empty comment record still occupies its slot, to keep positions aligned |

**UNKNOWN** Whether the toolset regenerates a missing GIC or silently loses the
comments. Needs the tool.

---

## ITP — the palette

**WHAT IT IS** How the toolset's object browser groups blueprints into folders.

**CONTAINER** Inside the module — **nine per module, in all 30 examined.**

**STRUCTURE** GFF. One top-level field `MAIN`, a list whose entries carry
`LIST` (nested children) and `STRREF` (the folder's display name). A tree of
named folders.

Nine files per module, one per blueprint type — `creaturepalcus.itp`,
`itempalcus.itp` and so on. `cus` = custom: these are the **module's own**
palette, over the game's standard one.

**⚠ KOTOR ships 16 ITP files in K1's BIF and 18 in K2's — and zero in any
module.** So KOTOR has a game-global palette and no way for content to extend
it, which is why every KOTOR blueprint carries a `PaletteID` integer instead
(batch 3).

**REFERENCES OUT** Blueprints by resref; the TLK by StrRef for folder names.

**REFERENCED BY** The toolset only.

**SCOPE** Module-local in NWN; game-global in KOTOR.

**AUTHORED BY** The toolset.

**READ WHEN** Never by the engine.

**SAMPLES**
| # | instance | why |
|---|---|---|
| 1 | `creaturepalcus.itp` | the typical case — a 4-entry folder tree |
| 2 | the nine-file set, identical in count across all 30 modules | the convention is rigid |
| 3 | K1's 16 BIF ITPs | the contrast — palettes that content cannot extend |

**UNKNOWN** Nothing outstanding at this scope.
