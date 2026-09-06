# STUDY 05 — BEHAVIOUR LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-5 additions. Merges with batches 1–4.

---

## The formats

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **DLG** | A bipartite graph of speaker lines and player lines, joined by gated links. Also carries camera, animation, voice, fades and quest updates. | **conversation** |
| **NSS** | C-like source. Ships for BIF scripts, never for module scripts. | **script source** |
| **NCS** | Compiled bytecode. The most numerous resource in the game. | **compiled script** |
| **LIP** | A mouth-shape timeline: a duration and fixed-stride entries. | **lip-sync track** |

## Conversation vocabulary

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`EntryList`** | Lines a character speaks. "Entry" describes the file, not the thing. | **speaker lines** |
| **`ReplyList`** | Lines the player may choose. | **player lines** |
| **`StartingList`** | Gated candidates for which line opens the conversation. First match wins. | **openings** |
| **`RepliesList` / `EntriesList`** | The outgoing links from a node — each with a gate. | **branches** |
| **`Index`** (on a link) | Array position of the target node. Node identity is position. | **target position** — and it should be an id (`FLAWS.md` F45) |
| **`Active`** | A script resref whose return value opens or closes this branch. | **gate script** |
| **`Active2` / `Not` / `Not2` / `Logic`** | A second gate, two negations and an AND/OR — used on under 2% of links. | **second gate / negate / combine** |
| **`Param1..5`, `Param1b..5b`, `ParamStrA/B`** | Arguments to the gate script, read with `GetScriptParameter`. **The operand lives here; the operator lives in code.** | **gate arguments** |
| **`Script` / `Script2`** | Action scripts run when the node plays. | **on-play** |
| **`ActionParam*`** | Arguments to those. | **action arguments** |
| **`Speaker` / `Listener`** | Tags naming who says it and who it is aimed at. | **speaker / addressee** |
| **`VO_ResRef`** | One name locating **both** the voice audio and the lip track. | **voice id** |
| **`Sound`** | K1's other voice field. K2 uses it zero times. | **(retired)** |
| **`Emotion` / `FacialAnim`** | K2-only row indices into `emotion.2da` (35) and `facialanim.2da` (17). | **mood / face** |
| **`Quest` + `QuestEntry`** | The quest tag and stage this line advances. | **advances quest / to stage** |
| **`IsChild`** | Present on all 150,344 links; unresolved. | **(unidentified)** |

## Script vocabulary

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`void main()`** | An action — runs for effect. | **action script** |
| **`int StartingConditional()`** | A condition — non-zero opens a gate. The name describes where it was first used, not what it does. | **condition script** |
| **`c_*` / `a_*`** (K2) | The primitive library: generic, parameterised conditions and actions. 509 + 1,289 of them replace K1's 2,345 + 3,025 bespoke scripts. | **condition primitive / action primitive** |
| **`k_con_*` / `k_act_*`** (K1) | One-off scripts per situation. | **bespoke gate / bespoke action** |
| **`GetScriptParameter(n)`** | Reads an integer argument the content file supplied. K2-only. | **gate argument** |
| **`GetScriptStringParameter()`** | Reads the string argument — usually a global's *name* or an object *tag*. K2-only. This is the whole workaround for having no named locals. | **gate name argument** |
| **`SetLocalBoolean(obj, slot, v)`** | Per-object flag, addressed by integer slot. No names anywhere. | **object flag [slot]** |
| **`SWVarTable`** | The per-object flag store: a `BitArray` and a `ByteArray`. | **object memory** |
| **`UserDefined`** | An integer-coded event scripts raise on each other. The only open extension point. | **custom event** |
| **`Heartbeat`** | A periodic tick. How anything polls, because there is no event for it. | **tick** — and needing it is a smell |
| **`action`** (the NWScript type) | A captured closure — a compiled fragment handed to the engine to run later. Persisted with its instruction pointer. | **deferred fragment** |
| **`DelayCommand` / `AssignCommand` / `ActionDoCommand`** | The entire deferral surface. Three functions. | **defer / run-as / enqueue** |

---

## Terms worth *not* carrying forward

**"Entry" and "Reply."** They name positions in a file. **Speaker line** and
**player line** name the thing, and stay correct when a conversation has 28
speaker lines and no player lines (`man26_swoop1`).

**"StartingConditional."** It describes the first place BioWare used it. A
condition is a condition wherever it runs.

**Index-as-identity.** A branch target should be an id, not an array position.
KOTOR's largest content file has 1,365 nodes and no stable handle for any of
them.

**Integer slots for memory.** `SetLocalBoolean(obj, 12, TRUE)` is unreadable and
uncheckable. If our attachments carry state, it is named.

**A closed hook list.** Eighty-odd fixed field names, and three object types with
none at all. The *names* are worth taking (`ATTACHMENT-01` needs exactly this
vocabulary); the closedness is not.
