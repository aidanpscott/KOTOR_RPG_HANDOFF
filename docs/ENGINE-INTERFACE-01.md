# ENGINE-INTERFACE-01 — what the engine exposes

**`ENGINE-SPEC-01` through `06` describe what the engine DOES. None says what it OFFERS.** That gap did not matter while there was one consumer. **`TRACE-102` settled that there are two** — the app and the Builder — **and two front-ends against an unspecified interface is how they drift.**

**⚠ This is `PACKAGE-FORMAT-01`'s job in memory rather than on disk.** That document specified what passes between Builder and app as files. This specifies what passes between either of them and the rules.

---

## 1 · The shape

> **The engine is a library, not a service.** `TRACE-102`: a service shape **fails on iOS**, where a background process cannot be spawned.

**One implementation, called by both front-ends.** If each reimplemented the rules they would diverge, and **nobody can grep across two codebases** — which is `PT-1292`'s stale skill count with the tooling removed.

**⚠ And the Builder may call it as a SUBPROCESS instead** — `TRACE-102`'s validator shape, *"how compilers and linters work."* **Same interface, different transport.** That is the named fallback if the stacks ever split, and it costs nothing to preserve now.

---

## 2 · ⚠ Four rules the surface must obey

**These come from findings, not from taste.**

**⚠ NEVER EXPOSE AN ORDINAL.** `ENGINE-SPEC-01` on KOTOR's `nNth` parameter: *"the single API that bakes list position into shipped scripts."* And `TRACE-83` found **position-as-identity** to be the defect that made KOTOR's own tables unextendable. **Every handle in and out is a name.**

**⚠ ASK, DO NOT COMPUTE.** `CHARACTER-RECORD-01 §3` derives rather than stores. So the interface offers **`defenceOf(character)`**, never a `defence` field a caller caches. **A front-end that can read a derived value can store it, and a stored derived value drifts.**

**⚠ EVERY MUTATION IS AN EVENT.** `PLAY-STATE-01`: state is a projection of an append-only log. **There is no `setHitPoints`.** There is `apply(event)`, and the projection changes because the log did. **`PT-1268` binds this absolutely** — nothing the caller does may change state except by writing an event.

**⚠ FAIL LOUDLY, RETURN A REASON.** `F35`: KOTOR's engine wrote an index past the end of its own table and **nothing rejected the write.** An engine call that cannot proceed **says why in a form the caller can show a person** — not a boolean, not an exception with no content.

---

## 3 · The surface, by area

**Grouped by what a caller wants. Names are illustrative; the SHAPE is the specification.**

### Packages
```
open(path)              → package | error naming what failed        §6 of the format
validate(path)          → report                                    the Builder's subprocess call
resolve(dependencies)   → ordered list | the first that did not
```

### Characters
```
create(choices)         → events                    creation writes EVENTS, not a record
project(log)            → character                 the record is what replay produces
levelUp(character, choices) → events
legalityOf(character)   → report                    validate-on-load, PT-1272
```

### Checks and combat
```
resolve(check)          → outcome with its whole derivation
```
**⚠ The outcome carries the arithmetic**, not just the total. `TRACE-85` found KOTOR persisting *"Defense Breakdown: 18 = base 10 + dex mod 4 + class 4"* — and `PT-1326` renders exactly that. **A caller that has to reconstruct the working will get it wrong.**

### Knowledge and dialogue
```
knows(character, topic) → yes | no | gated, with the gate         §3.2, seeded
options(conversation)   → the reply set, with each gate's state
recognise(text, options) → an option | nothing                    PT-1303
```
**⚠ `recognise` is the ONLY call whose result is non-deterministic**, and it is the boundary `TESTING-01`'s layer 1a exists to guard. **It returns an authored option or nothing. It never returns a new one.**

### Generation
```
bind(template, world)   → bindings | the constraint that failed   rejection sampling, PT-1025
```

### Save and load
```
save(log)               → bytes         compressed, .sav, PT-1329
load(bytes)             → log | error
snapshot(log)           → snapshot      a cache; deletable without loss, PT-1327
```

---

## 4 · ⚠ What the engine does NOT expose

**No renderer, no layout, no widget.** The engine says a character has 38 of 47 vitality. **It does not know there is a bar.**

**⚠ THAT RULE STANDS, AND IT CREATED A SECOND PROBLEM — `PT-1381`.** Step 6 found `AREA-FORMAT-01 §2b` governs how an area LOOKS in **both** Loom and the app, **and there was nowhere for one implementation to live.** The engine is barred; neither program can depend on the other without worse coupling. **So it was duplicated, flagged in the file rather than silently.**

> **A fourth package: `Lens`. The shared view layer.**

**It depends on `Lodestar` and both programs depend on it.** The engine stays free of widgets; **the widgets stay in one place.**

**⚠ The alternative was accepting drift, and the drift is predictable rather than hypothetical:** the first time `§2b` is amended, **one implementation gets the change and the other does not — and Loom stops showing authors what players will see.** That is the whole promise of a Builder.

**`Lens` holds what BOTH programs draw the same way** — the area grid, tokens, tiles. **Not the Builder's authoring gestures and not the app's play chrome.**

**No AI.** `PT-1268`: AI output is a product of the ledger, never an input. **The AI layer is server-side** (`TRACE-102`) and reaches the engine only through `recognise`, which selects from a fixed set.

**No file paths beyond `open`.** The engine reads a package; it does not browse a disk.

**⚠ No setters.** Repeated because it is the rule most likely to be added "temporarily" and never removed.

---

## 5 · Open

- **⚠ Error shape.** `§2` requires a reason a caller can show a person. **What that structure is — code, message, offending handle — is unspecified.**
- **Async boundaries.** Which calls may block. `load` on a long log is the obvious candidate.
- **Multiplayer.** `PT-1330` rules the table sees one thing; **whether the engine is per-player or per-table is not decided.**
- **⚠ Whether the Builder's subprocess call shares this interface exactly** or a serialised subset. `§1` assumes exactly; nothing has tested it.
