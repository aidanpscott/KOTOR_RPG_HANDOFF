# STUDY 05 — BEHAVIOUR LAYER

Scripts and conversation in KOTOR 1 and KOTOR 2 — NSS, NCS, DLG, LIP.

| file | what it is |
|---|---|
| `RECORDS.md` | four records — DLG, NSS, NCS, LIP |
| `README.md` | this file — the seven questions |
| `FLAWS.md` | F43–F50 |
| `NAMING.md` | batch-5 vocabulary |

**Method.** Every DLG in both games — 1,167 K1 and 1,159 K2, comprising 48,776
speaker nodes, 55,974 player nodes and **150,344 links**. Every NSS and NCS in
the BIF layer, every LIP in `lips/`, both `nwscript.nss` files, and every script
hook on every object type. `.mod` files excluded (batch 4: runtime artifacts).

**Sits on:** batch 2 (globalcat, two string globals), batch 3 (blueprint hooks),
batch 4 (IFO/ARE/GIT bindings, the journal), `LIVE-STATE.md` (the persisted
`ActionList`).

---

## 1 · What a conversation is

Full record in `RECORDS.md`. Three pools and an entry point:

```
StartingList[]  →  which speaker node opens, chosen by gate
EntryList[]        speaker nodes,  each with RepliesList[] → player nodes
ReplyList[]        player nodes,   each with EntriesList[] → speaker nodes
```

**The pools are flat and position-indexed.** A link holds an `Index` into the
other pool; no node is ever nested inside another. So a conversation is a
bipartite graph stored as two arrays and a list of edges, and **the graph
topology is entirely positional** — inserting a node in the middle renumbers
every edge that points past it.

**A node carries six kinds of thing, on every node in both games:** text
(StrRef), voice (resref), a script, an animation list, a camera setup, a screen
fade — plus a quest update. The conversation layer is not a text format with
extras bolted on; presentation and state change are first-class on every line.

**Where a branch condition is evaluated:** on the **link**, not the node. Both
`StartingList` entries and reply/entry links carry the gate. So the same
mechanism decides which line opens a conversation and which replies are offered.

---

## 2 · ⚠ Conditions and actions — the gate mechanism

**There is one mechanism: a call to a compiled script whose return value is the
gate.** No data expressions, no named conditions, no comparison operators in the
file. A gate is `Active`, a resref, and the script's `StartingConditional()`
returns non-zero to open the link.

**But K1 and K2 use that one mechanism in completely different ways**, and the
difference is the most useful finding in this batch.

### K1 — one bespoke script per situation

```
72,337 links   12,424 gated (17.2%)   2,345 DISTINCT gate scripts
top: k_con_carthpm 271 · k_con_bastpm 262 · k_con_talkedto 230 · k_con_fperslow 226
```

**Roughly one hand-written condition script for every five gates.** The names
are situational — `k_con_carthpm` gates on Carth being present, `k_con_comver45`
on a specific conversation version. The logic is inside the compiled script and
invisible to the file.

### K2 — a parameterised primitive library

```
78,007 links   12,303 gated (15.8%)   509 distinct gate scripts (+94 in Active2)
top: c_local_notset 1454 · c_global_eq 1293 · c_local_set 1252
     c_800_globl_true 387 · c_global_gt 370 · c_quest_status 303 · c_ismale 240
```

**A fifth as many scripts for the same number of gates**, and the top ones are
generic. K2 added the engine support that makes this possible:

```
GetScriptParameter(int n)      K1: absent   K2: present
GetScriptStringParameter()     K1: absent   K2: present
```

Reading the shipped source confirms the pattern. `c_local_set` calls
`GetObjectByTag(GetScriptStringParameter())` then
`GetLocalBoolean(obj, GetScriptParameter(1))`. `c_global_eq` calls
`GetGlobalNumber(GetScriptStringParameter())` and compares it against
`GetScriptParameter(1)`. `a_local_set` is the mirror with `SetLocalBoolean`.

**The parameters come from the DLG link.** So the condition is `c_global_eq`
plus `ParamStrA = "some_global_name"` plus `Param1 = 3`, all stored in the
conversation file.

### And K2 added a boolean expression around it

```
Active   Active2   Not   Not2   Logic
```

Two gate slots, each independently negatable, combined by `Logic`. Usage across
78,007 links:

```
Logic = 0 (AND)  77,846      Logic = 1 (OR)   161
Not set           635        Not2 set         308      both  38
Active2 used    1,447 links
Param1 used     8,204        string params  3,239
```

**So the expression language exists and is barely used.** OR appears on 161 of
78,007 links — 0.2%. The second condition slot on under 2%. K2 built a two-term
boolean gate and in practice authored one-term gates with parameters.

### The enumeration the brief asked for

| mechanism | K1 | K2 |
|---|---|---|
| script call returning int | ✅ the only mechanism | ✅ still the only mechanism |
| parameters passed to that script | ❌ | ✅ 5 int + 5 int + 2 string |
| second condition | ❌ | ✅ `Active2` |
| negation | ❌ | ✅ `Not`, `Not2` |
| AND / OR | ❌ | ✅ `Logic` |
| data expression, no script | ❌ | ❌ |
| named reusable condition | ❌ | ⚠ by convention only — `c_*` naming |

**For ENGINE-SPEC-03:** KOTOR never has a declarative gate. Even K2's version is
a function call with arguments, and the *meaning* of the condition lives in
compiled code the file cannot see. The thing K2 got right is that **the
parameters — including the name of what is being tested — live in the content
file, not the code.** That is what took 2,345 scripts down to 509.

**Actions work identically.** `Script` (+ K2's `Script2`) with the same
parameter block. K1 has 3,025 distinct node scripts; K2 has 1,289, and its top
entries are `a_local_set` (1,046), `a_global_set` (810), `a_local_reset`,
`a_influence_inc`/`_dec`, `a_givedark` — the same generic-primitive shift.

---

## 3 · NSS and NCS

**Source ships.** K1: **1,774 NSS** beside 1,784 NCS in the BIF. K2: 638 beside
612. **Module scripts do not** — all 10,861 K1 and 4,508 K2 module scripts are
NCS only, confirmed by searching every `_s.rim` in both games.

**Two entry points, and they are the type system:**

```
void main()                  an action — runs for effect
int  StartingConditional()   a condition — returns non-zero to open a gate
```

**The compiled form** is `NCS V1.0` plus a **big-endian** uint32 length — the
only big-endian field in any format in this study — then an instruction stream
calling engine functions by opcode. Names are compiled away; the binding is
`nwscript.nss`'s declaration order.

**The boundary between engine and author is stark.** K2's `nwscript.nss`
declares **877 functions** and the author writes *only* glue between them.
Grouped by what they touch:

| group | count | note |
|---|---|---|
| creature/object state — read | 251 | `Get*` |
| creature/object state — write | 77 | `Set*` |
| effects | 89 | `Effect*` constructors + application |
| world queries | 58 | `GetFirst/Next/Nearest/IsObjectValid` |
| action queue | 46 | `Action*` |
| sound / music / movie | 38 | |
| combat | 21 | |
| party | 16 | |
| talents | 10 | |
| events / delayed execution | 9 | |
| journal / quest | 7 | |
| dialogue / cutscene | 7 | |
| force / spells | 6 | |
| camera | 3 | |
| **global & local variables** | **2** | ⚠ see §4 |
| unclassified | 223 | maths, strings, item properties, misc |

**Two functions for all persistent state**, against 89 for effects and 251 for
reading object state. That ratio *is* the design.

---

## 4 · ⚠ What a script can actually remember

The constraint, from batch 2: **no named local variables** — `SetLocalBoolean`
takes an integer slot — and **two string globals in the entire game**, with all
globals predeclared in `globalcat.2da`.

**The workaround is that the content file carries the name.**

```
DLG link:   Active = "c_global_eq"   ParamStrA = "Tar_GortonAl"   Param1 = 3
script:     GetGlobalNumber( GetScriptStringParameter() ) == GetScriptParameter(1)
```

The global's *name* is a string in the conversation file. The script is generic.
The engine's two string globals are never involved, because the string is not
runtime state at all — it is **authored data passed as an argument**.

The same trick addresses objects: `c_local_set` does
`GetObjectByTag(GetScriptStringParameter())` and then indexes a local boolean
**slot number** on it. So "does this specific NPC have flag 12 set" becomes a
tag string plus an integer, both stored in the DLG.

**What actually persists, per `LIVE-STATE.md` and batch 2:**

| store | capacity | addressed by |
|---|---|---|
| global booleans | 819 (bit-packed, 103 bytes) | name, predeclared |
| global numbers | 376, **one byte each (0–255)** | name, predeclared |
| global locations | 5 | name |
| **global strings** | **2** | name |
| per-object booleans | integer slots, `SWVarTable.BitArray` | slot number |
| per-object numbers | integer slots, `SWVarTable.ByteArray` | slot number |
| quest state | one stage id per quest | quest tag |

**So a K2 campaign's entire memory is: 819 bits, 376 bytes, 2 strings, plus a
few slots per object and a cursor per quest.** Everything else must be inferred
from the world's current arrangement.

That is why `c_local_notset` is the single most common gate in K2 (1,454 uses) —
"has this specific thing not happened yet" is the only question the storage can
cheaply answer.

**And the workaround has a hard edge.** Because the global name is a *string in
the DLG* and globals must be *predeclared in a game-wide 2DA*, adding one
campaign variable means editing a shared table (batch 2 F19). The K2 design
makes the script generic and leaves the coupling exactly where it was.

### What makes a script suspendable

`LIVE-STATE.md` found a 106 KB script persisted with an instruction pointer.
Following it:

**Only three functions take an `action` parameter** — in both games:

```
DelayCommand(float, action)
AssignCommand(object, action)
ActionDoCommand(action)
```

An `action` argument is a **captured closure** — a fragment of the calling
script, compiled in, handed to the engine to run later or elsewhere. That
closure is what gets stored in `ActionList` with its bytecode and program
counter.

**So scripts do not yield.** A script runs to completion. What survives a save is
a *deferred fragment* that was explicitly handed over, plus queued `Action*`
commands. The three functions above are the entire yield surface, and
`ActionWait`, `ActionPauseConversation` and `ActionResumeConversation` are the
places a queued sequence stalls.

---

## 5 · Event binding — the complete hook table

Every script-bearing field on every object type, both games. **This is the
vocabulary `ATTACHMENT-01` is missing.**

| object | hooks | the events |
|---|---|---|
| **module** (IFO) | **14** | ModLoad, ModStart, ClientEnter, ClientLeave, Heartbeat, PlayerDeath, PlayerDying, PlayerLevelUp, PlayerRest, SpawnButtonDown, AcquireItem, UnacquireItem, ActivateItem, UserDefined |
| **creature** (UTC) | **14** | Spawn, Death, Attacked, Damaged, Disturbed, Dialogue, EndDialogue, EndCombatRound, Heartbeat, Notice, Blocked, Rested, SpellCastAt, UserDefined |
| **door** (UTD) | **14** | Open, Closed, Click, Lock, Unlock, FailToOpen, Damaged, Death, MeleeAttacked, SpellCastAt, Disarm, TrapTriggered, Heartbeat, UserDefined |
| **placeable** (UTP) | **15** K1 / **16** K2 | as door, plus Used, InventoryDisturbed, EndDialogue; K2 adds FailToOpen |
| **trigger** (UTT) | **7** | Enter, Exit, Click, Disarm, TrapTriggered, Heartbeat, UserDefined |
| **encounter** (UTE) | **5** | Entered, Exit, Exhausted, Heartbeat, UserDefined |
| **area** (ARE) | **4** | Enter, Exit, Heartbeat, UserDefined |
| **store** (UTM) | **1** | OpenStore |
| **item** (UTI) | **0** | — |
| **waypoint** (UTW) | **0** | — |
| **sound** (UTS) | **0** | — |

**Identical in both games** except placeable's extra K2 hook.

Four patterns worth naming:

**`UserDefined` is on every type that has hooks at all** — a general-purpose
event a script raises on itself with an integer code. It is the escape hatch,
and it is how one script talks to another without a shared variable.

**`Heartbeat` is on every type that has hooks** — a periodic tick. In a
real-time engine this is how anything polls. `LIVE-STATE.md` §5 flagged the
poll-driven design as a real-time artifact; the hook table is where it enters.

**Items, waypoints and sounds have no behaviour at all.** An item's effects are
pure data (batch 3 §5); a waypoint is a marker; a sound is a config. Three of the
nine blueprint types are inert.

**Conversation is a fourth binding surface**, separate from all of these: 150,344
links each able to carry a gate, and 48,776+55,974 nodes each able to carry an
action. **The conversation layer has more script attachment points than every
object hook in the game combined.**

---

## 6 · ⚠ Voice and lip sync — where K2 moved it

Batch 2 left this open: K2's TLK sound resrefs collapsed from 66.6% of entries
to 1.2%. **They moved to the dialogue node, and K1 had them in both places.**

```
K1 BIF dialogue nodes:  VO_ResRef only 5,346 · Sound only 41 · both 77 · neither 905
K2 BIF dialogue nodes:  VO_ResRef only 4,332 · Sound only    0 · both  0 · neither 5,325
```

**K2 uses the `Sound` field zero times.** K1 populated `Sound` on 118 nodes and
`VO_ResRef` on 5,423; K2 abandoned `Sound` entirely and made `VO_ResRef`
universal.

So the sequence is: K1 carried voice association **redundantly** — in the TLK
entry *and* on the dialogue node. K2 **removed the TLK copy** and kept the node
one. That is a normalisation, and it is the right direction: the TLK is
game-global (batch 2 F23) and the node is where the line actually lives.

**One resref, three assets.** `VO_ResRef` names a string that locates the audio
**and** the lip animation. Confirmed: dialogue node resrefs match a shipped LIP
name 15,126 times in K1 and 15,377 in K2. The text comes separately, by StrRef.

**A `.lip` file is a mouth-shape timeline.** `LIP V1.0`, a float duration, an
entry count, then fixed 5-byte entries — verified arithmetically across
differently-sized files. 18,209 in K1, 26,218 in K2, packaged one archive per
module in `lips/`, the archive name derived from the module name by format
string (`LIPS:%s_loc`).

Batch 1 noted `lips/*.mod` dated 2003 — that is now explained: they are shipped
content, built at release, unlike the `modules/*.mod` files batch 4 showed are
runtime-written. **The extension collides; the provenance does not.**

**K2 also added a whole VO production pipeline into the shipped data:**
`RecordVO`, `RecordNoVO`, `RecordNoVOOverri`, `VOTextChanged`, `DeletedVOFiles`,
`AlienRaceNode`, `AlienRaceOwner`, `PostProcNode`, `PostProcOwner` — recording
status, alien-language processing and post-production flags, on every node of
every conversation.

---

## 7 · K1 vs K2

| area | difference |
|---|---|
| **gates** | the headline: 2,345 bespoke scripts → **509 parameterised primitives**, enabled by `GetScriptParameter` / `GetScriptStringParameter`, which K1 lacks entirely |
| **gate expression** | K2 adds `Active2`, `Not`, `Not2`, `Logic` — a two-term boolean. Used on <2% of links; OR on 0.2% |
| **node actions** | K2 adds `Script2` and the same 12-parameter block |
| **script API** | 877 functions in K2; **+3 effect types** (`DROIDSCRAMBLE`, `DROID_CONFUSED`, `MINDTRICK`), `AdjustCreatureSkills`, `GetSkillRankBase`, `IncrementGlobalNumber`/`DecrementGlobalNumber` |
| **performance** | K2 adds `Emotion` and `FacialAnim` per node, indexing two K2-only 2DAs |
| **voice** | K2 drops `Sound` entirely and the TLK copy with it |
| **VO pipeline** | K2 ships nine production-tracking fields on every node |
| **volume** | K1: 1,774 NSS, 12,645 NCS. K2: 638 NSS, 5,120 NCS — **K2 ships 60% fewer scripts for the same amount of dialogue**, which is the primitive library paying off |
| **hooks** | identical, except placeable 15 → 16 |

---

## 8 · Scope — what was and was not checked

**Read in full:** all 1,167 K1 and 1,159 K2 DLG files from BIF and `.rim`/`.erf`
module archives — every node, every link, every gate and action resref; both
`nwscript.nss` files; the shipped NSS source of K2's condition and action
primitives; NCS headers across both games; every LIP archive.

**Searched, negative:** every `_s.rim` in both games for NSS source (none —
modules ship compiled only); both games' script APIs for `GetScriptParameter`
(K1 absent); every object type for script-bearing fields (items, waypoints and
sounds have none).

**Not checked:**
- **NCS opcode semantics.** The container, header and calling convention are
  established; the instruction set is not decoded. Every statement about what a
  script *does* comes from shipped NSS source or from function names.
- **Any running process.** Gate evaluation order, what happens when a gate
  script errors, and whether `Logic` is AND at 0 — the AND/OR reading is
  **inferred from the 99.8%/0.2% distribution**, not from the engine.
- **The LIP entry field split.** The 5-byte stride is arithmetic; the
  time/shape decomposition is inference.
- **`IsChild`, `OldHitCheck`, `ConversationType`, `AnimList` contents** — present
  on every node, not decoded.
- Whether shipped NSS recompiles to the shipped NCS.
- NWN's scripting layer — batch 7.
