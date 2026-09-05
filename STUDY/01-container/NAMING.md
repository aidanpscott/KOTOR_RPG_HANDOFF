# STUDY 01 — CONTAINER LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-scoped; intended to merge into a study-wide vocabulary table.

Only terms this batch actually read are listed. Where the clearer name is a
judgement rather than a translation, the note says why.

---

## Archive types

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **KEY** (`chitin.key`) | The one index for the read-only bulk layer. Maps `(name, kind)` to an archive and a slot within it. Not an index of the game — only of the BIFs. | **bulk index** |
| **BIF** | A nameless bag of bytes with an offset table. Cannot be read without the KEY. | **anonymous pack** |
| **ERF** | A self-describing named archive with a (dead) localisation header. | **named archive** |
| **RIM** | The same thing as an ERF, simpler header, read-only by intent. | **read-only archive** |
| **MOD** | Byte-identical to ERF. The signature is the only difference. | **archive** — it needs no separate name; see `FLAWS.md` F06 |
| **SAV** | As a *file*: the whole save, mislabelled `MOD`. As a *type id* (2057): one module's saved state nested inside that file. Two different meanings for one word. | file → **save tree**; type → **module snapshot** |

## Identifiers

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **ResRef** | A ≤16-character name. Half of the only lookup key the engine has. | **resource name** |
| **ResType** | A numeric kind (2017 = a rules table, 2029 = a conversation…). The other half of the key. | **resource kind** |
| **ResID** | Not an identity — a packed *address*: `(bifIndex << 20) \| slot`. | **pack address** — calling it an id is the mistake; see `FLAWS.md` F01 |
| **`HD0:` / `OVERRIDE:` / `MODULES:`** | Namespace prefixes forming a virtual path scheme over the layers. | **layer prefix** |

## Locations

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`Override/`** | A flat, game-global folder of loose files that outrank the packed layers. The supported extension point, with no namespacing or ownership. | **loose override layer** |
| **`patch.erf`** | K1 only. A shipped archive that outranks the BIFs, carrying post-release fixes to rules tables, GUI panels and models. | **patch layer** |
| **`rims/`** | K1 only. Phase-associated preloads (`global`, `chargen`, `mainmenu`), addressed by name from the engine. Wholly duplicates BIF content. | **phase preload set** |
| **`modules/<name>.rim`** | The area triple only — area properties, placed instances, module info. | **module core** |
| **`modules/<name>_s.rim`** | Everything the module needs that is not the triple: blueprints, compiled scripts, and (K1 only) conversations. | **module content** |
| **`modules/<name>_dlg.erf`** | K2 only. That module's conversations, split out of the content archive. | **module dialogue** |
| **`lips/<name>_loc.mod`** | That module's lip-sync data. Name derived from the module name by format string, never stored. | **module lip-sync** |
| **`currentgame/`** | A working copy of the module currently being played, as a single archive. | **active module scratch** |
| **`gameinprogress/`** | Live session state as loose files — companion records, inventory, reputation. | **live session state** |
| **`texturepacks/tpa\|tpb\|tpc`** | Three complete copies of the texture library at three quality levels. Selected between, never stacked. | **texture quality tier** |

## Record names seen inside the save

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`AVAILNPC<n>`** | A companion's saved record, identified only by slot number. | **companion slot** — see `FLAWS.md` F10 |
| **`INVENTORY`** | The party's shared inventory. Type id 0, with its own `INV ` magic. | **party inventory** |
| **`REPUTE`** | Faction standing table. | **faction standing** |
| **`GLOBALVARS.res`** | The predeclared global variable values for this save. | **global variable state** |
| **`PARTYTABLE.res`** | Party roster and party-level flags. | **party state** |
| **`savenfo.res`** | The metadata the load screen reads — the only file present in some save directories. | **save header** |

## Engine internals named in the binaries

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`CExoKeyTable`** | The one flat registry of `(name, kind) → bytes`, into which every layer registers. Where precedence is actually decided. | **resource registry** |
| **`AddKey`** | Registration of one resource into that table. Emits `Duplicate Resource` on collision. | **register resource** |

---

## Terms worth *not* carrying forward

**"Key file."** `chitin.key` indexes one layer, not the game. Calling it *the*
key implies an authority it does not have — four other layers outrank it.

**"Override."** It names the mechanism from the modder's side, not the engine's.
The engine has no override concept; it has a registration order across layers,
and the folder is simply one layer. Naming our own equivalent for what it *is*
(a layer, with a declared rank) rather than what it *does to* something else
would remove most of `FLAWS.md` F02 by construction.

**"RIM" / "MOD" / "ERF" as three things.** They are one thing with three
spellings. Any vocabulary we build should have one word.
