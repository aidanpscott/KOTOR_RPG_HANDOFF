# STUDY 07 — TOOLSET AND GAME — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-7 additions, drawn from NWN where it has a concept KOTOR lacks. Merges
with batches 1–6.

---

## Things NWN has a name for and KOTOR has nothing for

| NWN's name | What it actually is | A clearer name |
|---|---|---|
| **hak** | A resource pack a module **declares by name in an ordered list**, overriding the game's own for that module only. Carries anything, including rules tables. | **scoped pack** |
| **`Mod_HakList`** | The module's ordered declaration of which packs apply and in what rank. The thing KOTOR's precedence question needed and never had. | **pack order** |
| **custom TLK** | A second string table a module names in one field. | **module strings** |
| **`Mod_CustomTlk`** | The declaration. One resref. | **strings pack** |
| **`VarTable`** (on a module) | Named, typed, module-scoped variables — `{Name, Type, Value}`. | **module config** |
| **`Mod_CacheNSSList`** | Which scripts to preload. | **preload set** |
| **`Mod_MinGameVer`** | The minimum engine version this content requires. | **requires engine** |
| **GIC** | Author notes on placed objects, in a **parallel file the engine ignores**. | **placement notes** |
| **ITP** | The object browser's folder tree, **per module**. | **palette** |
| **`.nwm`** | A `MOD `-signature file with a different extension because it shipped with the game. | — the distinction is shelving, not format |

## Toolset vocabulary worth borrowing

| Aurora's name | What it actually is | A clearer name |
|---|---|---|
| **Blueprint** | A reusable object template. Aurora and KOTOR agree on this word and it is a good one. | **template** (batch 3's preference) |
| **Blueprint Wizard / Area Wizard** | Guided creation flows that leave **no trace in the file**. Correct: a wizard produces data, it is not a kind of data. | **authoring flow** |
| **Build Module** | Compile scripts and validate, in place. Not an export — the working file is the deliverable. | **build** |
| **Custom palette** (`*palcus.itp`) | The module's own folder tree over the game's standard one. | **module palette** |
| **AutoBackup / `.BackupMod`** | The toolset backing up the module itself, because the module *is* the project. | **working copy** |

## Terms worth *not* carrying forward

**Five names for one container.** `ERF `, `MOD `, `SAV `, `HAK ` are four
signatures on one identical format, and `.nwm` is a fifth extension over the
second of them. Our packages get one name.

**"Export" where there is no export.** Aurora's `Build Module` acts on the file
already being edited. Calling the operation an export invites the assumption
that a separate source form exists — and the important property here is that it
does **not**.

**Precedence by list position with an undocumented direction.** `Mod_HakList` is
ordered and nothing says which end wins; the convention is legible only because
authors name packs `_top` and `_core` (`FLAWS.md` F63). If our packages stack,
the rank is a **declared number**, not an array index.

**Comments aligned by position.** GIC is right to be a separate file and wrong to
match its entries to the instance list by index. Notes should carry the id of
what they annotate.

---

## The one-line vocabulary this batch adds

**A module that carries its own source, notes, palettes and configuration is not
an export — it is the project.** NWN has no word for the distinction because it
never needed one. We will need one, because our Builder writes what our app
reads, and the question "can this be reopened" has to be answerable by looking
at the artifact.
