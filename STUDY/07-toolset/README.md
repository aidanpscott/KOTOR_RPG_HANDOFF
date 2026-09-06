# STUDY 07 — TOOLSET AND GAME

Neverwinter Nights and the Aurora toolset — studied **only** for the
relationship between a shipped game and its authoring tool sharing one format,
because that is the relationship our Builder will have with our app.

| file | what it is |
|---|---|
| `RECORDS.md` | five records — MOD/NWM, HAK, custom TLK, GIC, ITP — and what I have |
| `README.md` | this file — the seven questions |
| `FLAWS.md` | F59–F64 |
| `NAMING.md` | batch-7 vocabulary |

---

## 0 · ⚠ What I have, and what that limits

**The toolset is installed and I cannot run it.** This is a Linux install of the
Steam Enhanced Edition; `bin/win32/nwtoolset.exe` (12.2 MB), `nwhak.exe` and
`util/win32/GFFEditor.exe` are present as Windows binaries. I read their strings.
I did not launch the toolset, build a module, save one, or export one.

**Every behavioural claim below rests on one of two things:** the artifacts the
toolset produced, or literals in its binary. Where a claim needs the running
tool, it says so.

**What I could read properly:** 16 official campaign modules, 14 community
modules, 18 haks, 4 custom string tables, and a 1,389-file override — 30 modules
opened in full. These are *authored artifacts*, which is a better sample for this
question than shipped game data.

---

## 1 · ⚠ What the toolset writes — save, not export

**The toolset works directly on the `.mod`. There is no separate project
format.** Five independent lines of evidence:

**The module carries source.** 26,317 NSS files across the 30 modules, tracking
NCS counts within a couple of percent. Compiled output does not need source;
a project file does. See §2.

**The module carries comment files.** 769 `GIC` files, one per area, containing
*only* the author's notes on each placed object, position-matched to the GIT's
instance lists. The game has no use for them.

**The module carries the toolset's own furniture.** Nine `ITP` palette files per
module — the object browser's folder tree — in all 30. Plus `Mod_CacheNSSList`,
`Mod_Creator_ID`, `Mod_Version`.

**The toolset's file dialogs know only `.mod`.** Extracting every `*.ext`
pattern from `nwtoolset.exe` gives `*.mod` (4 uses), `*.git`, `*.dlg`, `*.nss`,
`*.sav`, `*.ini`, `*.txt`, `*.bmp`, `*.ico`. **No project extension exists.**

**And it backs up the module itself.** The binary carries `AutoBackup`,
`AutoBackupInterval`, `BackUpFileName`, `.BackupMod`, `Create Backup Modules`
and `\module.ifo`. You back up the thing you are working on.

The binary does contain `Build Module`, `Build Module Advanced`, `Export`,
`Export Area` and `Compile the script` — so build and export **operations**
exist. But they act on a file that is already the deliverable. **This is
save-in-place, and the shipped artifact is the working artifact.**

---

## 2 · ⚠ Compiled versus source — the most important question

**A NWN module carries its own source, and can be reopened losslessly.**

```
30 modules       26,317 NSS       26,180 NCS
93% of modules carry source; the two that do not contain no scripts at all
```

Every official campaign module carries it. `Chapter2.nwm`: 2,836 NSS beside
2,834 NCS. `Aribeth's Redemption III.mod`: 1,203 beside 1,198.

**Nothing is lost on the way out**, because there is no "way out" — see §1. The
file the author edits is the file the player loads, and it contains:

| authoring artifact | in a NWN module | in a KOTOR module |
|---|---|---|
| script source (NSS) | **yes, 93% of modules** | **no** — compiled only |
| per-object comments (GIC) | **yes, 769 files** | **no** — comments are on the runtime record |
| object-browser palettes (ITP) | **yes, 9 per module** | **no** — 16/18 game-global in the BIF |
| creator and version | yes | yes |

**The contrast with KOTOR is exact.** Batch 5 found KOTOR ships 1,774 NSS in
K1's BIF and 638 in K2's — but **every one of the 10,861 K1 and 4,508 K2 module
scripts is compiled-only.** BioWare's own engine-level scripts kept their source;
module content did not.

**For the Builder, the finding is narrow and load-bearing:** the thing that makes
a NWN module reopenable is not a clever format — it is the decision to **put the
source in the artifact**. It costs roughly the size of the compiled output again
(26,317 source files beside 26,180 compiled), and it buys a tool that has no
one-way door.

---

## 3 · The global-versus-local problem — NWN does better, and here is how

Batch 2 F18 found KOTOR has **no module-local rules table anywhere** — zero 2DAs
across 644 module archives. Batch 4 F42 found the journal is one game-wide file
and nothing links a module to a quest. NWN solves all three.

| can a module carry its own… | NWN | KOTOR |
|---|---|---|
| **quests** | ✅ `module.jrl` inside the module — **every one of the 26 script-bearing modules has one**, holding 1–50 quests | ❌ one game-wide `global.jrl` |
| **rules tables** | ✅ via haks — `wc_2da_shared.hak` carries 30 2DAs including `classes` and the per-class feat tables | ❌ none, anywhere |
| **strings** | ✅ `Mod_CustomTlk` names a second table | ❌ one TLK per game, no mechanism |
| **named variables** | ✅ `VarTable` on the module — `{Name, Type, Value}` | ❌ 2 string globals game-wide, all predeclared |
| **areas** | ✅ 1–314 per module | ❌ always exactly 1 |

**`VarTable` deserves calling out.** A real example from *Pirates of the Sword
Coast*:

```
{Name: "VERSION",             Type: 3, Value: "0.0.0.041119"}
{Name: "X2_S_UD_SPELLSCRIPT", Type: 3, Value: "potc_ud_spells"}
{Name: "NPC_CREW1",           Type: 3, Value: "a3_vantab"}
```

Named, typed, module-scoped configuration. Batch 5 F46 established KOTOR's
entire campaign memory is 819 bits, 376 single-byte numbers and **two strings**,
all predeclared in a game-wide table. NWN modules carry their own named strings
as a matter of course.

**The mechanism worth taking is the same one in all four rows: a module declares
what it needs, by name, in its manifest.** Haks by name in an ordered list;
strings by name; variables by name. Nothing is discovered by scanning a folder.

---

## 4 · Haks and overrides — declared, ordered precedence

**`Mod_HakList` is an ordered list of hak names in the module manifest.** Usage
across 30 modules: 20 declare none, 7 declare one, 1 declares two, 1 declares
seven, 1 declares eleven.

```
Aribeth's Redemption III        Wyvern Crown of Cormyr
  [0]  cep2_top_v1                [0]  wc_top
  [1]  cep2_add_phenos2           [1]  wc_2da_shared
  [2]  cep2_add_phenos1           [2]  wc_creatures
  …                               …
  [9]  cep2_core1                 [6]  wc_tilesets
  [10] aribethrev1_cep
```

`_top` at index 0 and `_core` at the bottom, in two unrelated projects.
**Index 0 is highest precedence** — *inferred from the naming convention, not
verified against the engine.*

**Compare batch 1 F02.** In KOTOR, four layers can shadow the BIF — Override,
module archives, `patch.erf`, `rims/` — and **nothing in any shipped file
declares their order.** I could prove by necessity that each beats the BIF, and
could not rank them against each other at all. The shipped install even contains
unresolved collisions between them.

The difference is not that NWN's engine is better documented. It is that
**NWN's precedence is data in the module and KOTOR's is registration order in a
binary.** One is readable by a tool; the other is readable by a disassembler.

**Where the base game and the override folder sit in NWN's order is not
established** — I found no declaration of it, and did not disassemble.

---

## 5 · The custom TLK — confirmed

Batch 2 searched both KOTOR install trees for `*.tlk` (one hit each) and both
binaries for `dialogf`, `customtlk`, `usertlk`, `TalkTable` — and found **no
second-table mechanism at all.**

**NWN has one, and it is a single field.** `Mod_CustomTlk` in `module.ifo` names
one table. The field is present on 27 of 30 modules and populated on three:
`cep2_v1`, `nwn2voicesets`, `dla`. Four custom tables ship in `data/tlk/`:

```
dialog.tlk (base)   112,228 entries
prccep.tlk          192,501 entries    larger than the base game's own
nwn2voicesets.TLK     2.07 MB
dla.tlk               1.19 MB
dla_bio.tlk             251 bytes      a near-empty table
```

**Format identical to the base** — `TLK ` V3.0, same 40-byte entries.

**How a StrRef chooses between the two is not established here.** The community
convention is a high-bit split (≥ 0x01000000 selects custom). Searching
`nwmain.exe` for that constant and for alternate-table literals returned only the
field name itself. **The mechanism is confirmed; the selection rule is not.**

---

## 6 · What Aurora exposes that the format does not — both directions

**Toolset concepts that DO have on-disk form** (so the format was designed for
the tool, not merely used by it):

| concept | on disk |
|---|---|
| per-object author notes | `GIC`, 769 files, position-matched to the GIT |
| object-browser folders | `ITP`, nine per module |
| script preload set | `Mod_CacheNSSList` |
| authorship and versioning | `Mod_Creator_ID`, `Mod_Version`, `Mod_MinGameVer` |
| module configuration | `VarTable` |

**Toolset UI concepts with no obvious on-disk counterpart**, from binary
literals: `Area Wizard`, `Blueprint Wizard`, `Conversation Editor`, `Script
Editor`, `Build Module` / `Build Module Advanced`, `Export Area`, `Compile the
script`, `AutoBackup`. These are **operations and dialogs**, and none of them
leaves a trace in the module — which is the correct outcome. A wizard is a way
of producing data, not a kind of data.

**The reverse direction — file fields the toolset cannot author — I could not
establish.** That requires opening a module in the tool and comparing what it
round-trips. **Not checked.** It is the one question in this batch that genuinely
needs the running toolset, and I am not going to guess at it.

---

## 7 · ⚠ The honest comparison

### The manifest diff is the summary

Comparing every field ever seen on a NWN `module.ifo` against every field on a
KOTOR one:

```
shared        42
NWN-only       9   Mod_HakList · Mod_CustomTlk · VarTable · Mod_CacheNSSList
                   Mod_MinGameVer · Mod_OnPlrChat · Mod_OnPlrEqItm
                   Mod_OnPlrUnEqItm · Mod_OnCutsnAbort
KOTOR-only     1   Mod_VO_ID
```

**KOTOR inherited the format, removed nine capabilities, and added one.**

### What NWN got right that KOTOR abandoned

**Source in the artifact.** 93% of NWN modules carry their NSS. KOTOR's carry
none. This is the difference between a tool with a one-way door and one without,
and it cost roughly double storage on the script layer.

**Comments beside the data, not in it.** NWN's `GIC` keeps author notes in a
parallel file the game ignores. KOTOR moved them onto the runtime record — a
`Comment` on every blueprint and every one of 104,750 dialogue nodes, shipped to
every player (batch 3 F31, batch 5 F50).

**Declared, ordered precedence.** `Mod_HakList` is readable data. KOTOR's
resolution order exists only as registration order in a binary (batch 1 F02) and
I could not establish it from any amount of shipped data.

**Module-local everything** — quests, rules, strings, named variables — against
KOTOR's game-global everything (batch 2 F18/F19/F23, batch 4 F42).

### And what KOTOR abandoned for defensible reasons

**Not everything KOTOR dropped was a mistake, and the study should say so.**

**The modding capabilities.** Haks, custom TLKs, module-local 2DAs and ordered
precedence are all *user-extension* machinery. NWN shipped a toolset to the
public as its core proposition; KOTOR shipped a linear single-player story and
no toolset at all. Carrying a hak-precedence system you never expose is dead
weight. **This is a defensible product decision that produced bad architecture —
both halves of that sentence are true.**

**One area per module.** KOTOR's `Mod_Area_list` is always length 1 against
NWN's up-to-314. That looks like a regression and probably is not: KOTOR
targeted the original Xbox, and small single-area modules give short, bounded
loads. NWN's 314-area module is a PC-only luxury. (The *indirection* KOTOR kept
without using is still waste — batch 4 F37.)

**`Mod_VO_ID`, KOTOR's one addition, is earned.** KOTOR ships 13,860 (K1) and
17,098 (K2) voice files against NWN's much lighter, largely-unvoiced dialogue
(batch 6). A per-module voice-over namespace is exactly what a fully-voiced game
needs and an unvoiced one does not.

### The finding that actually matters for the Builder

Aurora's important property is not any single feature. It is that
**the authoring tool and the game read the same file, and that file carries
everything the tool needs to reconstruct the author's intent.** Source, comments,
palettes, configuration — none of which the engine reads.

KOTOR proves the alternative by counter-example. Its formats are the *same
formats*, minus the authoring layer, and the result is content nobody outside
BioWare could reopen: compiled scripts with no source, comments welded to runtime
records, and a precedence order that two batches of this study could not
determine from any amount of data.

**A Builder that writes what our app reads is only safe if the artifact also
carries what the Builder needs to read it back.** That is the whole lesson, and
NWN paid about 2× on one layer to get it.

---

## 8 · Scope — what was and was not checked

**Read in full:** all 16 official and 14 community modules (30 `module.ifo`,
772 ARE, 769 GIC, 274 ITP, 26,317 NSS counted, 26 module journals); all 18 haks
by resource type and 2DA inventory; all 4 custom TLK headers; the NWN base
`dialog.tlk` header; string extraction from `nwtoolset.exe`, `nwhak.exe` and
`nwmain.exe`.

**Searched, negative:** KOTOR's BIF layers and every module archive in both
games for `GIC` (**zero**) and for module-local `ITP` (**zero**; 16/18 exist
game-global in the BIF); `nwmain.exe` for a custom-TLK StrRef offset constant
(only the field name found).

**Not checked, and some of this is structural:**
- **The toolset was never run.** No build, no save, no export, no round-trip
  test. Everything about its behaviour is inferred from its output and its
  strings.
- **Which file fields the toolset cannot author** — §6's reverse direction. This
  genuinely needs the tool.
- **Hak precedence direction** — inferred from `_top`/`_core` naming in two
  projects, not verified against the engine.
- **Where the base game and override folder rank** against haks.
- **The custom-TLK StrRef selection rule.**
- **Whether the toolset regenerates a missing GIC** or loses those comments (3
  of 772 areas ship without one).
- **NWN's own runtime layers** — save format, live state, effects. Out of scope:
  this batch studied the tool/game relationship, not NWN as a game.
