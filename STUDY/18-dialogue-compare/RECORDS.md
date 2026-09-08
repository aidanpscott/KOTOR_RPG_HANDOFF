# STUDY 18 — the three dialogue systems: records

**Description only. Judgement in `FLAWS.md`.**

**Sources, stated per record.** `shipped` = read out of the installed games.
`ours` = read out of our own documents. `undetermined` = named and not
answered.

**Both games installed and read; neither run.** K1 = `swkotor`,
K2 = `Knights of the Old Republic II/steamassets`. Read with our own
`scripts/gfffull.py`, `scripts/container.py` and a `chitin.key`/BIF reader
written for this study. **No third-party tool was used and none is required.**

**⚠ Deduplicated by resref.** A `.dlg` present in both a module's `.rim` and
its `.mod` is counted once. `TRACE-93`'s totals are larger for this reason;
where a proportion can be compared it matches (`R18.06`).

---

## R18.01 · The corpus  `shipped`

|  | K1 | K2 |
|---|---:|---:|
| `.dlg` resources found | 1,589 | — |
| distinct `.dlg` after dedupe | **1,065** | **973** |
| parse failures | 0 | 0 |
| NPC nodes (`EntryList`) | 22,745 | 20,506 |
| player nodes (`ReplyList`) | 25,461 | 23,918 |
| links, incl. `StartingList` | 67,755 | 66,006 |
| `NumWords` summed | 482,848 | 433,707 |

**Where they live.** K1 keeps `.dlg` inside module `.rim`/`.mod` archives plus
32 in the BIFs. **K2 splits them out into a separate `<module>_dlg.erf`** —
246 module files, one dialogue archive per module.

---

## R18.02 · What a `.dlg` is, structurally  `shipped`

**A GFF V3.2 file** — the same container as `.uti`, `.utc`, `.are`. One
top-level struct.

**Three node lists and nothing else holds a node:**

    StartingList   links only, no text — the entry points into the tree
    EntryList      NPC lines
    ReplyList      PLAYER lines

**⚠ There is no node type field.** A node's type is *which list it is in*.

**A link is a struct, not a pointer.** It carries `Index` — an offset into the
*other* list — plus its condition. **Entries link to replies and replies link
to entries; the alternation is structural and cannot be broken.**

**Two supporting lists:** `AnimList` per node (`Animation`, `Participant`) and
`StuntList` per file (`Participant`, `StuntModel`).

**A condition attaches to the LINK, not the node.** `Active` is a **resref
naming a script**, which the engine runs; the script returns int and the link
is taken if it returns true. **An action attaches to the NODE** — `Script`,
fired when the line plays.

**⚠ Walk order is array order.** No priority, weight or sort field exists at any
level in either game (`TRACE-93`, re-confirmed here by the enumeration in
`R18.03`/`R18.04`: no such field name appears).

---

## R18.03 · K1's complete field enumeration  `shipped`

**55 distinct field names; 83 counting each level separately.**

```
TOP-LEVEL (20)
  EntryList  ReplyList  StartingList  StuntList
  VO_ID  NumWords  ConversationType  ComputerType
  DelayEntry  DelayReply  Skippable  OldHitCheck
  EndConversation  EndConverAbort  AmbientTrack  CameraModel
  AnimatedCut  UnequipItems  UnequipHItem  EditorInfo

ENTRY — NPC line (27)
  Speaker  Text  Listener                        who / what / to whom
  Script                                          action fired on play
  RepliesList                                     outbound links
  VO_ResRef  Sound  SoundExists  Delay  WaitFlags  audio + timing
  AnimList  CameraAngle  CameraID  CameraAnimation
  CamFieldOfView  CamHeightOffset  TarHeightOffset
  CamVidEffect  FadeType  FadeColor  FadeDelay  FadeLength
  Quest  QuestEntry  PlotIndex  PlotXPPercentage   journal + XP
  Comment                                          author's note

REPLY — player line (26)
  identical to ENTRY minus Speaker, plus EntriesList

LINK (4)      Index  Active  IsChild  LinkComment
START (2)     Index  Active
ANIM (2)      Animation  Participant
STUNT (2)     Participant  StuntModel
```

---

## R18.04 · K2's complete field enumeration  `shipped`

**99 distinct field names; 163 counting each level separately.** Everything in
`R18.03` plus:

```
TOP-LEVEL (+5)   AlienRaceOwner  PostProcOwner  RecordNoVO
                 DeletedVOFiles  NextNodeID

NODE (+23)       Script2                       a SECOND action script
                 ActionParam1..5, 1b..5b       parameters for Script
                 ActionParamStrA, ActionParamStrB
                 Emotion  FacialAnim           performance
                 AlienRaceNode  PostProcNode  CamVidEffect
                 NodeID  NodeUnskippable  Changed
                 RecordVO  RecordNoVOOverri  VOTextChanged

LINK (+16)       Active2                       a SECOND condition
                 Not  Not2                     negate either
                 Logic                         AND / OR between them
                 Param1..5, 1b..5b             parameters for Active
                 ParamStrA  ParamStrB
```

**⚠ The link grew from 4 fields to 20, and 17 of those 20 are the condition
apparatus** (`Active`, `Active2`, `Not`, `Not2`, `Logic`, ten numeric params,
two string params). `Index`, `IsChild` and `LinkComment` are the rest.

**Reconciliation with `TRACE-95`.** Per-level sums here are 83 and 163.
Excluding the two sub-structs (`AnimList`, `StuntList`, 4 fields) gives
**79 and 159**. `TRACE-95` reports **78 and 159** — K2 exact, K1 one over.
`EditorInfo` is the likely single difference: it is a toolset artefact present
in only 22 of 1,065 K1 files and 4 of 973 K2 files.

---

## R18.05 · What is actually load-bearing  `shipped`

Percentages are of all nodes (`EntryList` + `ReplyList`).

| field | K1 | K2 | |
|---|---:|---:|---|
| `Text` | 65.7% | 73.5% | |
| `VO_ResRef` | 77.0% | 42.1% | |
| `Script` (action) | 12.5% | 15.7% | |
| `Script2` | — | 2.9% | |
| `CameraAngle` | 12.7% | 8.7% | |
| `CameraID` | 7.3% | 6.2% | |
| `AnimList` non-empty | 5.6% | 4.1% | |
| `Listener` | 6.1% | 2.8% | |
| `Comment` | 6.6% | 0.6% | |
| `Quest` / `QuestEntry` | 1.6% | 1.3% | |
| `PlotIndex` | 0.3% | 0.3% | |
| `FadeType` | 0.9% | 1.4% | |
| `CameraAnimation` | 0.5% | 0.2% | |

**⚠ Three K2 fields are defaults, not authoring, and counting presence would
overstate them:**

    Emotion            value 4 on 42,290 of 44,424 nodes — authored on 4.8%
    FacialAnim         0 or -1 on 44,128 — authored on 0.4%
    PlotXPPercentage   1.0 on 44,312 of 44,424 — authored on 0.3%

---

## R18.06 · The shape of the tree  `shipped`

| | K1 | K2 |
|---|---:|---:|
| replies with **no text at all** | 15,023 / 25,461 = **59.0%** | 11,196 / 23,918 = **46.8%** |
| NPC nodes offering **exactly one** reply | 15,434 / 22,745 = **67.9%** | 12,984 / 20,506 = **63.3%** |
| NPC nodes offering **more than one** | 6,290 = **27.7%** | 6,676 = **32.6%** |
| NPC nodes offering **none** (terminal) | 1,021 | 846 |
| links flagged `IsChild` | 19,523 / 64,355 = 30.3% | 21,582 / 63,403 = 34.0% |
| entries carrying a `Speaker` override | 5,258 / 22,745 = 23.1% | 5,222 / 20,506 = 25.5% |

**`TRACE-93` recorded 16,179 of 27,465 K1 replies with no text = 58.9%.** This
sweep gets 59.0% on a deduplicated denominator. **Same proportion, confirmed by
a second method.**

**`Speaker` overrides another character into the conversation** — in
`bastila.dlg`, three of 26 NPC lines are spoken by Carth.

---

## R18.07 · Where a condition lives and whether it can be read  `shipped`

**Distinct condition scripts named by `Active`/`Active2`:** K1 **2,309**,
K2 **493**. **The K2 collapse is the parameterised conditional** — `c_global_eq`
alone is used 1,708 times with different `Param`/`ParamStr` values.

**Resolvability.** Both games ship script **source** (`.nss`, restype 2009) in
the BIFs — K1 1,774, K2 638 — alongside the compiled `.ncs`.

| by USE SITE | K1 (11,716) | K2 (12,541) |
|---|---:|---:|
| source available | 6,197 = 52.9% | 9,716 = 77.5% |
| **compiled only, no source** | **5,501 = 47.0%** | **2,809 = 22.4%** |
| neither found | 18 = 0.2% | 16 = 0.1% |

**Purity — of the ones whose source exists.** A condition is *impure* if its
body calls a state-changing engine function.

| by USE SITE | K1 | K2 |
|---|---:|---:|
| pure predicate | 5,999 = 51.2% | 9,642 = 76.9% |
| **mutates world state** | **198 = 1.7%** | **74 = 0.6%** |
| unreadable | 5,519 = 47.1% | 2,825 = 22.5% |

**Split by where the gate sits:**

```
                         total    pure    MUTATES   unreadable
K1  StartingList gates    2,341   39.6%      6.8%       53.7%
K1  in-tree link gates    9,375   54.1%      0.4%       45.5%
K2  StartingList gates    1,815   71.6%      2.0%       26.4%
K2  in-tree link gates   10,726   77.8%      0.4%       21.9%
```

**⚠ Method control.** The first classifier matched `Start\w+\(` and therefore
matched `StartingConditional()` — the function *every* one of these scripts
declares — and returned "1 pure of 708". Corrected and re-checked against two
scripts read by hand.

---

## R18.08 · One real conversation, walked  `shipped`

**`bastila.dlg`, from `modules/danm13.mod`** — Dantooine, a main companion.
29,414 bytes.

    26 NPC nodes · 35 player nodes · 11 StartingList entries · 58 links
    20 of the 35 player nodes have NO text  (57%)
    2 of 61 nodes carry an action Script
    1 of 58 links carries a condition
    11 of 11 StartingList entries carry a condition — all different
    speakers: Bastila 23, Carth 3
    IsChild set on 8 of 58 links

**⚠ All eleven opening conditions mutate global state as a side effect of being
evaluated.** Every one calls `GetGlobalNumber` to decide, and then calls
`SetGlobalNumber` and/or `SetGlobalBoolean` before returning. The one read
closely reads a zone number, and **on returning true also sets a "done" boolean
and resets the zone number to 0** — so evaluating the list is what marks the
line as spoken.

**This file is an extreme case, not the average.** Corpus-wide only 6.8% of K1
`StartingList` gates provably mutate (`R18.07`). **It is a real case, in a main
companion, in the shipped game.**

**Where the branching actually is:** 1 condition inside the tree, 11 outside it.
**The conversation's logic is in eleven separate compiled scripts, none of which
is in the same archive as the `.dlg`** — `k_pdan_bastila01` and `k_con_bastpm`
are absent from `danm13.mod`, `danm13.rim`, `danm13_s.rim` and `patch.erf`, and
resolve only through `chitin.key` into `scripts.bif`.

---

## R18.09 · Ours, as our documents have it  `ours`

**`ENGINE-SPEC-03 §2` adopts the BioWare model by name** — *"THE BIOWARE MODEL,
UNCHANGED"*:

    StartingList / EntryList (NPC) / ReplyList (PLAYER)
    a link carries Index + Active
    walk links in order, run each Active, take the first that passes
    no scoring, no weighting

**And `§2` takes K2's addition explicitly:** *"PARAMETERISED CONDITIONALS —
`Param1–Param5` plus a `Not` flag, so one conditional script serves many
nodes."*

**⚠ That is the whole of our stated file structure.** `PACKAGE-FORMAT-01`
reserves a `dialogue/` folder and specifies nothing inside it. **No document in
`design/` or `rules/` defines a dialogue file format**, a node field set, or a
gate serialisation. Searched: every file in `design/` and `rules/` for
`EntryList`/`ReplyList` — one hit, `ENGINE-SPEC-03`.

**What our documents add that has no `.dlg` counterpart:**

| ours | where | |
|---|---|---|
| the **topic space** — a closed taxonomy, filter not tree | `§3` | for generated NPCs |
| the **seeded knowledge gate**, `(who ⊕ what)`, zero bytes stored | `§3.2` | |
| the **fact/gate schema** — `id`, `fact`, `tier`, `gate`, `deflection` | `§4b`, `RULES-02 §3` | |
| `all_of`/`any_of`, **nestable arbitrarily deep** | `§4b.1` | |
| the **absence report**, unconditional | `§4a` | |
| the **AI rephrase**, and off-script answer-and-return | `§4.2`, `§4.3` | |
| typed text firing an authored branch | `§4e`, `PT-1303` | |
| **check tags rendered from the gate field** | `§4c` | |
| escalation — per topic, per conversation, derived not stored | `PT-1316` | |
| the character brain as a **view, not a memory** | `PT-1311` | |
| multiplayer, one shared screen | `§4d`, `PT-1104` | |
| package-local `rules/` | `PACKAGE-FORMAT-01` | `TRACE-82`: theirs has none |

---

## R18.10 · The four differences put to me, checked  `ours`

| put to me | verdict | where |
|---|---|---|
| typed text that means an authored reply **counts as picking it** | **confirmed** | `PT-1303`, `§4e` |
| three colours, amber rolls and grey does not | **confirmed, and it is four in the committed state** — amber passed, **coral failed**, grey manner, teal background. Plus `dim` for an act. | `§4c` |
| ruled at `PT-1305` | **corrected — `PT-1305` is the character brain.** The colours are `PT-1306` (settled) and `PT-1307` (simplified) | |
| **no numbers** on options — `[Persuade]`, and you roll | **confirmed** | `PT-1307` |
| a price shown when the player can act on it | **confirmed** — `[Bribe · 50 credits]`; *"a number appears on an option when the player can act on it, and not otherwise"* | `PT-1315`, `§4c` |
| AI never advances the plot | **confirmed, and refined**: `PT-1303` lets the AI pick **which authored door**, which `§4e` argues is the job a menu does, not a story decision | `§4.3`, `§4e` |

---

## R18.11 · What already exists in converted form  `ours`

**Held raw, not converted:** `data/tlk/k1_dialog.tlk` and `k2_dialog.tlk`, with
a README stating their purpose — **resolving item and creature name strrefs**.
No `.dlg` has been read into any document. `data/extracted/` holds nineteen
JSON files; **none is dialogue.**

**One thing IS converted, and it came out of `dialog.tlk`:** the check-tag
vocabulary at `§4c`. `TRACE-12` surveyed 2,509 bracketed lines across 256
distinct strings expressing ~25 concepts, and that was reduced to **eight real
checks, one manner tag (`LIE`), and one retirement** — `THREATEN` folded into
`INTIMIDATE`, *"which we run as a real check — KOTOR never did… OURS. STATED
PLAINLY, NOT ASSUMED SOURCED."*

---

## R18.12 · Not determined

- **Whether the 47% of K1 gates that ship compiled-only are pure.** Not
  decompiled. The measured mutation rate is therefore **a floor, not a rate**.
- **What the parameterised K2 conditionals mean per call site.** `c_global_eq`
  is used 1,708 times; the global names are in `ParamStrA`, and no sweep of
  those values was run.
- **The topic taxonomy.** `§7` records it as open — *"shape settled, list not."*
- **Whether our dialogue file would be TOML.** `PACKAGE-FORMAT-01 §3c` makes
  TOML the shipping format generally; nothing states it for `dialogue/`.
- **The licence position on the text itself.** Not researched here.
