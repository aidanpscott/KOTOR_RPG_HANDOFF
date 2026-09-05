# STUDY 01 — CONTAINER LAYER — FLAWS

Design problems found in batch 1. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

The brief asked particularly for **anything global that had no reason to be**.
Entries 1, 2 and 3 are that shape. The rest are recorded because they cost
something real, not because they are untidy.

---

### F01 · Resource identity encodes physical location
**Follows from:** `RECORDS.md` → KEY, BIF

`ResID = (bifIndex << 20) | indexWithinBif`. A resource's identifier *is* its
address — which BIF, and which slot inside it.

The identifier and the location should be independent. Because they are not,
nothing can be added to or removed from the read-only layer without rebuilding
both the archive and the master index in lockstep, and every id downstream of an
insertion point shifts. It also means the KEY cannot express "this resource
lives somewhere else now" — the only way to relocate a resource is to renumber
it.

The cost is visible in the shipped data: this is why every later layer
(`Override`, `patch.erf`, module archives) had to be invented as a *shadowing*
mechanism rather than as an *edit* to the index. You cannot amend the KEY, so
you must outrank it.

---

### F02 · Precedence is undeclared, undiscoverable, and load-bearing
**Follows from:** `README.md` §3, §2

Four layers can shadow the BIF layer — `Override`, module archives, `patch.erf`,
`rims/`. **Nothing in any shipped file declares their order.** There is no
manifest, no priority field, no per-layer rank. The order exists only as
registration sequence inside the resource manager.

Three consequences.

The rule cannot be read by tooling. Any mod installer, and any exporter, has to
encode community-reverse-engineered behaviour rather than read a declaration.

The rule cannot be *checked*. `CExoKeyTable::AddKey: Duplicate Resource` is a
diagnostic, not a policy — it reports a collision after the fact, at a point
where the losing file has already been chosen silently.

And the shipped game itself contains unresolved collisions across those layers
(`README.md` §3 lists them: `spells.2da` in two layers, `skills.2da` in two,
75 textures in two). The game must be resolving them; nothing records how.

*This is the single highest-value thing to do differently. A format that
declares its own layer order costs one field and removes an entire class of
undiagnosable bug.*

---

### F03 · Override is one flat game-global folder
**Follows from:** `README.md` §3; `RECORDS.md` → ERF

Every override is a loose file in one directory, keyed on filename alone. There
is no namespacing, no per-mod subtree, no manifest, no ownership.

Two mods that both improve `spells.2da` do not merge and do not conflict —
**the second one installed silently wins**, and the first is simply gone. The
same is true for any GUI panel, any dialogue, any texture.

This is the same shape as the two problems the study README already names (the
game-wide TLK, the game-wide `global.jrl`), and it has the same root: a shared
mutable namespace with no owner. Here it is worse than those two, because the
Override folder is the *supported extension point* — it is where the design
tells you to put your changes.

The engine does support one level of structure (`OVERRIDE:textures` is a literal
in both binaries, so a `textures` subfolder is recognised), which shows the flat
namespace was a choice rather than a limitation.

---

### F04 · The save file is tagged as a module
**Follows from:** `RECORDS.md` → SAV

`SAVEGAME.sav` opens with `MOD V1.0`. The file's own signature says "module",
and the only thing marking it as a save is its filename and the type id of its
entries.

A container whose magic number lies about what it is defeats the purpose of
having a magic number. Anything reading by signature — a tool, a validator, a
recovery path — will classify a save as a module and try to load it as one.

The related confusion: type id 2057 *is* named SAV and *is* used correctly, but
only for the nested per-module snapshots inside the file. So "SAV" means one
thing as a type id and something else as a file extension.

---

### F05 · Two mutually incompatible formats for one job
**Follows from:** `RECORDS.md` → RIM, ERF

RIM and ERF hold the same thing — named module resources — and cannot share a
parser. RIM stores `ResType` as **u32** in a single 32-byte table; ERF stores it
as **u16** across two parallel arrays. Neither capability difference is used:
ERF's extra localisation header is dead everywhere (see F07).

K2 then uses **both at once for the same module** — `262tel_s.rim` alongside
`262tel_dlg.erf` — splitting one module's content across two formats by resource
kind. Every consumer needs two code paths to read one module.

---

### F06 · MOD and ERF are the same format with different names
**Follows from:** `RECORDS.md` → MOD

`MOD ` and `ERF ` are byte-identical in layout — verified by parsing both with a
single code path, every field landing correctly. The distinction lives entirely
in four signature bytes and carries no structural meaning.

So the format has **two ways to say "identical"** (F05: two incompatible formats
for one job) **and one way to say "different"** that isn't (this entry). The
type system is doing the opposite of its job in both directions.

---

### F07 · Declared-and-dead fields shipped with uninitialised values
**Follows from:** `RECORDS.md` → ERF, BIF

- `LanguageCount` is **0 in every ERF-family file** in both games. The localised
  description block is declared and never used.
- `FixedResCount` is **0 in every BIF** in both games. A whole second resource
  mechanism, declared in the header, unused.
- `DescriptionStrRef` holds implausible values in shipped files — `1159751020`,
  `3452816845`, `1601205100`. These are not StrRefs; they read as uninitialised
  memory written straight to disk.

The first two cost only confusion. The third is worse: a field that *sometimes*
holds a valid-looking number and sometimes holds garbage cannot be trusted or
ignored safely, and a consumer has no way to tell the two cases apart.

---

### F08 · Ambiguity shipped: 34 modules exist twice with no declared winner
**Follows from:** `RECORDS.md` → MOD; `README.md` §5

34 of K1's 40 `.mod` modules **also** ship as a `.rim` + `_s.rim` pair. In 21 of
those the `.mod` is a strict superset of the pair; in 12 the contents match; in
1 neither. `danm13` is the clearest case — the `.mod` carries four UTC
blueprints the pair does not have.

So for 34 modules the game ships two candidate definitions of the same module,
differing in content, with **nothing declaring which one loads**. Under F02
there is no way to find out from the data.

Whatever the answer, 21 modules have a set of blueprints that either always load
or never load, and the shipped files do not say which.

---

### F09 · The global rules tables ship twice, in two serialisations
**Follows from:** `RECORDS.md` → RIM; `README.md` §4

K1's `rims/` holds 1,192 resources and **all 1,192 also exist in the BIF layer**.
It is a wholesale duplicate.

Mostly byte-identical — but **13 tables are not**, and the difference is that
the BIF copies delimit column headers with `\t` while the `rims/` copies use
`\0`. Two serialiser conventions for the same table, both shipped, in
`appearance`, `baseitems`, `placeables`, `portraits`, `heads`, `soundset` and
seven others.

Nothing marks either copy as authoritative. Combined with F02 this means the
effective content of thirteen core rules tables depends on an undeclared
resolution order.

---

### F10 · Companion identity is positional
**Follows from:** `RECORDS.md` → SAV

The save stores companions as `AVAILNPC0`, `AVAILNPC1`, `AVAILNPC2`,
`AVAILNPC6`, `AVAILNPC7`, `AVAILNPC8` — **slot number baked into the resource
name**, with gaps where slots are unfilled.

A companion has no identity beyond its index. Adding one means claiming a free
integer; reordering is impossible; and a save cannot express "this is Mission"
except as "this is slot 1".

This is the same positional-identity pattern found in the creature record's
skill array, and it has the same effect: the container can hold exactly the
number of things it was built for, and membership is an address rather than a
name.

---

### F11 · Empty archives ship, and nothing prunes them
**Follows from:** `RECORDS.md` → RIM, MOD

Valid, well-formed, **zero-entry** archives are shipped: 14 of K1's 123
`lips/*.mod`, 2 of K2's 77, and 4 of K1's 12 `rims/*.rim`
(`legal.rim`, `legaldx.rim`, `subglobal.rim`, `subglobaldx.rim`).

Minor on its own. Worth recording because it says the build produced an archive
per expected name whether or not there was anything to put in it, so the
*presence* of an archive carries no information about whether content exists —
a consumer must open every one to find out.

---

### F12 · Quality tiers stored as full duplicate archives
**Follows from:** `RECORDS.md` → ERF; `README.md` §3

`swpc_tex_tpa/tpb/tpc.erf` carry **identical ResRef sets** — 3,294 each in K1,
3,286 in K2, 100% mutual overlap — as three complete copies of the texture
library at three quality levels. Roughly 640 MB in K1 and 730 MB in K2 for the
texture packs, of which two thirds can never be used in a given session.

The alternative — mip levels inside one asset, or one pack plus deltas — was
available. Recorded here mainly because the structure **looks like a precedence
chain and is not**, which is an easy misreading for anything walking the
directory.
