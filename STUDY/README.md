# STUDY — how the source games are put together

**Purpose.** A structural map of KOTOR 1, KOTOR 2 and NWN's Aurora toolset, produced across seven batches, in a shape that **composes**. Not to build an exporter — that was ruled a hope and declined at `PT-1269`. **To learn from the design before we commit to our own format.**

**⚠ The output format matters more than the batching.** Seven runs of prose produce seven essays. Seven runs of *identical records* produce one map. **Use the template below without deviation**, even where a field feels redundant for a given type.

---

## The seven batches

| # | Folder | Covers |
|---|---|---|
| 1 | `01-container` | packaging and lookup — BIF/KEY, ERF/RIM/MOD, Override precedence, load order |
| 2 | `02-definition` | the rules layer — 2DA tables, the TLK string table |
| 3 | `03-blueprint` | reusable object templates — UTC, UTI, UTP, UTD, UTT, UTM, UTS, UTW |
| 4 | `04-world` | modules and areas — IFO, ARE, GIT, and how they bind |
| 5 | `05-behaviour` | scripts and conversation — NSS/NCS, DLG |
| 6 | `06-presentation` | audio, music, movies, cutscene authoring, and the model layer **as far as animation and cutscene staging reach** |
| 7 | `07-toolset` | **Aurora ↔ NWN** — how the toolset hands a module to the game |

**Both KOTOR games in every batch.** Differences are recorded on the record itself, never as a separate pass — comparing from memory across runs is how divergences get missed.

**NWN is scoped to batch 7 only**, except where a KOTOR structure is obviously inherited and the ancestor explains it.

---

## The record — one per resource type, every field, every time

```
## <EXT> — <plain-language name>

WHAT IT IS          one sentence, no jargon

CONTAINER           which archive type holds it, and where it is found

STRUCTURE           top-level shape. GFF struct? table? binary? text?
                    the fields that carry meaning — not an exhaustive dump

REFERENCES OUT      what this points AT, and BY WHAT MECHANISM
                    resref string / row index / numeric id / filename
                    ⚠ the mechanism matters more than the target

REFERENCED BY       what points at THIS, same detail

SCOPE               module-local, game-global, or campaign-level
                    ⚠ call this out explicitly — it is where KOTOR hurts

AUTHORED BY         a human in a tool? generated? hand-edited 2DA?

READ WHEN           load time, area transition, on demand, every frame

K1 vs K2            differences, or "none found"

SAMPLES             3-5 real instances, named, chosen for SPREAD:
                    one minimal, one complex, one oddity
                    give the file and module each came from

UNKNOWN             what you could not determine, and what it would take
```

**⚠ Description only. No critique in these records.** Facts and judgements in one document make the facts harder to trust later. Flaws go in a separate catalogue — see below.

---

## Two further deliverables

**`FLAWS.md`** — a catalogue of design problems, **each citing the record it follows from**. The one already known: the TLK is a single game-wide string table, and the journal is a single game-wide `.jrl`. Both make two mods collide by construction. Look for others of that shape — anything global that had no reason to be.

**`NAMING.md`** — a table: *KOTOR's name · what it actually is · a clearer name.* `UTC` means "creature blueprint"; `GIT` means "everything placed in this area". This becomes the vocabulary for our own format, and eventually the map an importer would use.

---

## Rules for every batch

**Read, do not infer.** Open files. A structure guessed from a filename is not a finding. Where something is inferred rather than read, **say so on the record**.

**Scope every negative.** *"No reference found"* is only useful with *"searched X, Y, Z."*

**Say what you did not check.** An honest gap is worth more than a confident guess, and this project has been bitten by wrong-shape negatives repeatedly.

**Commit each batch to its folder before starting the next.** Partial work in the repository beats complete work lost.
