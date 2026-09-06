# STUDY 07 — TOOLSET AND GAME — FLAWS

F59–F64, continuing batches 1–6. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

**⚠ A note on subject.** Most entries here are flaws in **KOTOR**, found by
having a working comparison for the first time. Where NWN is at fault it says so
explicitly. This is not a "NWN good, KOTOR bad" catalogue — see F64 and
`README.md` §7 for the other direction.

---

### F59 · KOTOR shipped modules nobody can reopen
**Follows from:** `RECORDS.md` → MOD/NWM; `README.md` §2

93% of NWN modules carry their script source — 26,317 NSS beside 26,180 NCS
across 30 modules. **Every KOTOR module carries none**: 10,861 K1 and 4,508 K2
module scripts, compiled-only (batch 5).

BioWare kept source for their own engine-level scripts (1,774 NSS in K1's BIF)
and dropped it for module content. So the decision was deliberate and it was
applied precisely where reopening matters most.

The cost is a **one-way door**. A KOTOR module's behaviour exists only as
bytecode whose opcode set nobody outside the studio documented. Twenty years of
community work on KOTOR has been decompilation; twenty years of community work
on NWN has been editing.

*Storage was the tradeoff and it is small: NSS beside NCS is roughly 2× on the
script layer alone, which is a rounding error against a 866 MB models BIF.*

---

### F60 · KOTOR welded author comments to runtime records
**Follows from:** `RECORDS.md` → GIC; `README.md` §2

NWN keeps per-object author notes in a **parallel `GIC` file** — 769 of them,
position-matched to the GIT's instance lists, ignored by the engine.

KOTOR has **zero GIC files anywhere** — searched both BIF layers and every module
archive in both games. It put `Comment` **on the runtime record**: on every
blueprint of every type (batch 3 F31) and on every one of **104,750 dialogue
nodes** (batch 5 F50), shipped to every player.

This is the same information, in the same engine family, one generation apart —
and the later game chose the worse arrangement. It bloats the largest content
files in the game (`kreia.dlg` is 1.64 MB), and it means the runtime record and
the authoring record cannot be versioned, stripped or diffed separately.

*The parallel-file design also demonstrates something useful: NWN kept the
comments **positionally** aligned to the instance list, which is fragile in
exactly the way batch 4 F45 described — but it kept them out of the record.*

---

### F61 · KOTOR's precedence is undeclared; NWN's is one ordered list
**Follows from:** `RECORDS.md` → HAK; `README.md` §4; batch 1 F02

NWN puts precedence in the module manifest: `Mod_HakList`, an ordered list of
names. A tool can read it, a builder can validate it, a player can see it.

KOTOR has four layers that can shadow the BIF — Override, module archives,
`patch.erf`, `rims/` — and **nothing anywhere declares their order.** Batch 1
proved by necessity that each beats the BIF and **could not rank them against
each other from any amount of shipped data**. The shipped install contains
unresolved collisions between them (`spells.2da` in two layers, `skills.2da` in
two, 75 textures in two).

Two batches of this study went at that question and closed it as
*not determinable*. The same question in NWN is answered by reading one field.

**That is the cost of putting a rule in code rather than in data**, stated as
precisely as this study can state anything.

---

### F62 · KOTOR removed every module-scoping mechanism it inherited
**Follows from:** `README.md` §3; batches 2 and 4

Comparing the two `module.ifo` field sets: **42 shared, 9 NWN-only, 1
KOTOR-only.** Every one of the nine removals is a scoping mechanism.

```
Mod_HakList       module-scoped resources with declared precedence
Mod_CustomTlk     module-scoped strings
VarTable          module-scoped NAMED variables
Mod_CacheNSSList  module-scoped script preloading
```

The downstream effects are the flaws this study has already catalogued
separately, and they are all the same flaw:

- batch 2 F18 — **no module-local rules table exists anywhere** (0 of 644
  archives); NWN puts 30 2DAs including `classes` in one hak
- batch 2 F19 — 819 booleans, 376 single-byte numbers, **two strings**, all
  predeclared game-wide; NWN modules carry named typed variables
- batch 2 F23 — one TLK per game, no second-table mechanism; NWN names one in a
  field
- batch 4 F42 — one game-wide journal, nothing linking a module to a quest;
  every NWN module has its own `module.jrl` with 1–50 quests

*Four independently-recorded flaws turn out to be one decision.*

---

### F63 · NWN's own faults, recorded so this is not a one-sided catalogue
**Follows from:** `RECORDS.md` → HAK, GIC, custom TLK

**Hak precedence is a naming convention, not a declaration.** The order is
positional in `Mod_HakList`, and which end wins is legible only because authors
name packs `_top` and `_core`. Nothing in the data says "index 0 wins" — I
inferred it from two unrelated projects using the same convention, and could not
verify it against the engine. A precedence field with an *undocumented
direction* is better than KOTOR's, and worse than a declared rank.

**GIC is position-coupled to the GIT.** Comments align by array index, so
inserting an instance shifts every note after it. Same disease as batch 4 F45.
And **3 of 772 areas ship with no GIC at all**, so the pairing is not enforced.

**Four ERF signatures for one format.** Batch 1 F06 found `ERF `, `MOD ` and
`SAV ` identical in layout; `HAK ` is a fourth. And `.nwm` is a fifth *extension*
over the `MOD ` signature. Five names, one format.

**The custom TLK's selection rule is invisible.** `Mod_CustomTlk` declares
*which* table; nothing declares *how a StrRef chooses*. The convention is a high
bit, which is exactly the kind of unwritten rule this catalogue exists to
complain about.

---

### F64 · Not everything KOTOR dropped was wrong, and the catalogue should say so
**Follows from:** `README.md` §7

Three of KOTOR's removals are defensible, and recording only the failures would
misrepresent the comparison.

**The modding machinery.** Haks, custom TLKs, module-local 2DAs and declared
precedence are *user-extension* features. NWN's core proposition was a public
toolset; KOTOR shipped a linear story and no toolset. Carrying extension
machinery you never expose is dead weight. **The product decision was
defensible; the architecture it produced was not** — and both halves are true at
once.

**One area per module.** `Mod_Area_list` is always length 1 in KOTOR against up
to 314 in NWN. KOTOR targeted the original Xbox, where small bounded modules
mean short loads. The regression is real and the reason is real. *(What is not
defensible is keeping the list indirection while never using it — batch 4 F37.)*

**`Mod_VO_ID` is earned.** KOTOR's single added field is a per-module voice-over
namespace, and KOTOR ships 13,860 and 17,098 voice files against NWN's largely
unvoiced dialogue (batch 6). A fully-voiced game needs it; an unvoiced one does
not.

*Recorded as a flaw entry because the failure mode it guards against is real:
a study that only catalogues regressions will conclude the older tool was
better, and on two of these three counts it was not.*
