# STUDY 05 — BEHAVIOUR LAYER — FLAWS

F43–F50, continuing batches 1–4. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

---

### F43 · Every gate is opaque compiled code
**Follows from:** `RECORDS.md` → DLG; `README.md` §2

A dialogue gate is a resref. The condition it tests lives in compiled bytecode
and **appears nowhere in the conversation file**.

So nothing can answer "which lines depend on this variable?" without decompiling
every gate script in the game — 2,345 distinct ones in K1. A writer cannot see
why a line is hidden. A tool cannot validate that a gate's variable exists. A
translator cannot tell which branches are reachable.

K2 improves this substantially without fixing it: `c_global_eq` plus
`ParamStrA = "Tar_GortonAl"` makes *what is tested* visible in the file, while
*how it is tested* stays in code. That is the difference between 2,345 scripts
and 509, and it came from moving the operand — not the operator — into content.

*The lesson for a gate schema is narrow and cheap: the operand belongs in the
content file even if the operator does not.*

---

### F44 · K2 built a boolean expression language and used 0.2% of it
**Follows from:** `README.md` §2

K2 added `Active2`, `Not`, `Not2` and `Logic` to all 78,007 links — a two-term
negatable boolean gate. Usage:

```
Logic = 1 (OR)      161 links      0.2%
Active2 populated  1,447 links      1.9%
Not or Not2 set      981 links      1.3%
```

Every link in the game pays for eighteen gate fields; 98% of them use one.

Two readings, and both are uncomfortable. If the expression language was needed,
it is unclear why authors avoided it — most likely because a second parameterised
condition is harder to reason about than writing a third primitive. If it was
not needed, it is 78,007 × 17 fields of ballast in the largest content files in
the game (`kreia` is 1.64 MB).

Same family as batch 1 F07, batch 2 F21 and batch 3 F30 — **declared capability,
near-zero use** — but distinct in that this one was *added deliberately in the
sequel* rather than inherited.

---

### F45 · Conversation topology is positional
**Follows from:** `RECORDS.md` → DLG

`EntryList` and `ReplyList` are flat arrays and every link holds an `Index` into
one of them. Node identity **is** array position.

Inserting a line in the middle of a conversation renumbers every link that
points past it — across 150,344 links in the two games. There is no node id, no
stable handle, nothing to diff against. K2 ships `NodeID` and `NextNodeID` on
every node, but those are *editor* bookkeeping; the runtime links still use
`Index`.

Same disease as batch 2's positional skills and batch 3's `SkillList` — and here
it lands on the single most-edited content type in the game.

---

### F46 · A campaign's entire memory is 819 bits, 376 bytes and two strings
**Follows from:** `README.md` §4

The complete persistent store available to content:

```
819 global booleans   bit-packed into 103 bytes
376 global numbers    ONE BYTE EACH — range 0-255
  5 global locations
  2 global strings
    per-object booleans and numbers, addressed by integer slot
    one stage id per quest
```

Against **89 functions for constructing effects and 251 for reading object
state, there are two for variables** (`README.md` §3).

The consequences are visible in the content. `c_local_notset` is K2's single
most common gate (1,454 uses) because "has this not happened yet" is the cheapest
question the storage can answer. A number cannot exceed 255. A campaign cannot
remember a name, a list, or anything a player typed.

And the workaround — putting the variable's *name* in the DLG as a string
parameter — does not relieve the underlying limit: the name still has to resolve
to a slot in `globalcat.2da`, a **game-wide predeclared table** (batch 2 F19). So
adding one campaign variable edits a file every other campaign shares.

---

### F47 · Per-object memory is addressed by integer slot
**Follows from:** `README.md` §4; batch 2

`SetLocalBoolean(object, int slot, int value)`. There are no named locals in
either game.

So `c_local_set` with `Param1 = 12` means "flag twelve on this object", and what
flag twelve *means* is a convention held in the author's head and in the
comments. Nothing in the data records it. Two authors working on the same
creature collide silently on slot numbers, and there is no registry to consult —
unlike globals, which at least have `globalcat.2da`.

This is the same positional-identity failure as F45 and batch 3 F26, applied to
state rather than to structure.

---

### F48 · Behaviour attaches by fixed hook name, and three types have none
**Follows from:** `README.md` §5

The hook table is a **closed enumeration**: 14 on a module, 14 on a creature, 14
on a door, 15–16 on a placeable, 7 on a trigger, 5 on an encounter, 4 on an area,
1 on a store. **Zero on items, waypoints and sounds.**

An author cannot add an event. If the thing you need to react to is not one of
the eighty-odd named fields, the only route is `Heartbeat` — a periodic poll —
or `UserDefined`, an integer-coded catch-all that scripts raise on each other.

Both escape hatches are visible in the shipped content, and both are symptoms:
polling because there is no event, and integer-coded messages because there is no
typed one.

*For `ATTACHMENT-01`: the vocabulary is good and worth taking. The closedness is
the part to avoid — a reaction model wants an open event namespace, not eighty
named fields.*

---

### F49 · The only way to defer work is to hand the engine a closure
**Follows from:** `README.md` §4; `LIVE-STATE.md`

Exactly three functions take an `action` parameter — `DelayCommand`,
`AssignCommand`, `ActionDoCommand` — and they are the entire deferral surface.
A script otherwise runs to completion.

The cost is on disk. `LIVE-STATE.md` found a **106 KB script fragment persisted
in a save with its instruction pointer**, because a captured closure has to
carry its own bytecode. Save size scales with how much deferred behaviour is
in flight.

It also means a deferred fragment is **not addressable**: it has no name, cannot
be cancelled selectively, and cannot be inspected. It is a suspended chunk of a
script that no longer exists as a script.

---

### F50 · Author-time bookkeeping ships in the product, at scale
**Follows from:** `RECORDS.md` → DLG

Every one of the 104,750 dialogue nodes in the two games carries a `Comment`
field with author notes. Every link carries `LinkComment` (45,594 populated).

K2 adds a whole VO production pipeline to shipped data — `RecordVO`,
`RecordNoVO`, `RecordNoVOOverri`, `VOTextChanged`, `DeletedVOFiles`,
`AlienRaceNode`, `AlienRaceOwner`, `PostProcNode`, `PostProcOwner`, `Changed`,
`NodeID`, `NextNodeID` — on every node of every conversation, plus `EditorInfo`
on five files.

These are recording-status and post-production flags for a voice pipeline that
finished in 2004. They are in the largest content files the game ships
(`kreia.dlg` is 1.64 MB).

Third instance of the pattern batch 3 F31 named: **there is no separation
between the authoring format and the runtime format.** The file the writer edited
is the file that shipped, so everything the editor needed to track shipped too.
