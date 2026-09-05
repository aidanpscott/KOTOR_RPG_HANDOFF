# STUDY 04 — WORLD LAYER — FLAWS

F34–F42, continuing batches 1–3. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

**Opens with a retraction**, because this batch invalidated the premise of a
finding carried across two earlier ones.

---

### ⚠ RETRACTION · F08 is withdrawn, and F25's explanation with it
**Follows from:** `RECORDS.md` → preamble; `README.md` §0

**F08 (batch 1)** recorded: *"34 K1 modules ship both a `.mod` and a `.rim` pair
with no declared winner"*, and called it the most consequential open question in
that batch. **F25 (batch 3)** built on it, concluding the `.mod` copies *"were
built against a larger `appearance.2da` than shipped"* and that *"the 34
duplicated modules are not equivalent copies."*

**The premise was wrong. The `.mod` files do not ship.** The running game writes
them — `modulesave` in both binaries, timestamps a week old against a February
install, ERF BuildYear 126 (2026) against `lips/*.mod` at 103 (2003) and
`patch.erf` at 104 (2004), and a clean control in K2: never played, zero `.mod`
files.

**What was actually wrong, and why:** I treated "present in `modules/`" as "part
of the product". Neither batch checked a filesystem timestamp or an ERF build
date, both of which were one command away and would have settled it immediately.
The lesson is narrow and worth stating: **in a game directory, shipped and
runtime-written files sit side by side, and the format does not distinguish
them.** Nothing in a `.mod` says "the engine wrote me" except `Mod_IsSaveGame`,
which is `0` — the same value the shipped `.rim` files carry.

**What survives.** The 82 out-of-range `Appearance_Type` values are real and are
all in `.mod` files. They are not a stale build; they are records **this
playthrough** wrote back. That is a better question, and it is open — see F35.

**Figures contaminated by the old premise**, all of which counted `.mod` files
as shipped content:

- batch 1: K1 `modules/` "40 `.mod`, 27.1 MB" as shipped volume; the
  `.mod`-versus-`.rim`-pair comparison entirely
- batch 3: the K1 blueprint census (2,656 UTC files included 698 `.mod`
  occurrences); the three 20-entry `SkillList` files are **BIF**, so that
  finding is unaffected
- this batch's own counts are `.rim`-only unless stated

---

### F35 · The engine writes references it cannot resolve
**Follows from:** `RECORDS.md` → preamble; batch 3 F25

82 creature records written back into `.mod` files carry `Appearance_Type`
values of 515–546 against a 509-row `appearance.2da`. Every one was produced by
the running game, not by an author.

So the engine **emitted a row index past the end of the table it indexes**, and
then persisted it. Nothing rejected the write, and on reload nothing will reject
the read.

This is batch 2's F13 (untyped cells, no declared target) and batch 3's GFF
semantics gap reaching their conclusion: when a reference is a bare integer with
no declared range, **the write path has nothing to validate against either**. A
format that cannot check a reference on read cannot check it on write.

*Why the engine produced these values is unknown and would need the running
game. That it produced them is on disk.*

---

### F36 · One flag changes what the file means
**Follows from:** `RECORDS.md` → GIT

`UseTemplates` is a single field in the GIT. Set to 1 — as in all 239 shipped
files — an instance entry is six fields: a template name and a position. Absent
— as in all 21 saved files — an entry is a **112-field inline record**.

The same list, in the same field, in the same file format, holds two entirely
different structures depending on one flag that **is not even present in the
second case**. A reader must test for a field's *absence* to know how to parse
everything below it.

And the two producers disagree about how to express it: the toolset writes
`UseTemplates = 1`; the engine omits the field rather than writing `0`. So
"templates off" and "field missing" are the same state, which means a truncated
or partially-written file parses as a save.

---

### F37 · Module and area are 1:1, and the format pretends otherwise
**Follows from:** `RECORDS.md` → IFO

`Mod_Area_list` is a list. **It has exactly one entry in all 239 modules of both
games.**

So every module is one area, the indirection buys nothing, and the cost is
real: two files, two tags, two name spaces, and every consumer writing
`Mod_Area_list[0]` forever. The `IFO`'s other 42 fields would sit on the `ARE`
perfectly well.

Same shape as the dead lists beside it — `Mod_CutSceneList`, `Mod_Expan_List`
and `Mod_GVar_List` are length 0 in all 239 files. **Four list fields on the
module manifest; one always has one entry and three always have none.**

---

### F38 · Two coordinate conventions and two vertex spellings, in one file
**Follows from:** `RECORDS.md` → GIT; `README.md` §5

Within a single GIT:

```
creatures, triggers, waypoints,   XPosition YPosition ZPosition
sounds, stores, encounters        XOrientation YOrientation
placeables, doors                 X Y Z  +  Bearing
cameras                           Position (Vector)  Orientation (Orientation)
```

Three conventions for "where is it and which way is it facing", chosen
apparently by object type. A tool that moves objects between lists has to
convert.

And the same split appears in geometry: **trigger vertices are
`{PointX, PointY, PointZ}`; encounter vertices are `{X, Y, Z}`** — the same
polygon concept, two field-name sets, both in the GIT.

*Cameras are the only place `Vector` and `Orientation` are used at all — the
format has proper types for this and nine of the ten lists do not use them.*

---

### F39 · The override surface is inverted, and the world layer confirms it
**Follows from:** `RECORDS.md` → GIT; batch 3 F29

Batch 3 found the inversion on a partial sample. The complete table confirms it
across every instance in both games:

```
Creature   ~70-field blueprint  →   6 instance fields, overrides NOTHING
Waypoint    11-field blueprint  →  14 instance fields, overrides its own
                                    name, description and map note
```

2,234 K1 creature placements against 1,589 distinct creature blueprints — **the
template layer is running at roughly one template per placement.**

The counter-example makes it worse rather than better: `CameraList` has **no
template at all** and works fine. So the format supports pure-instance objects,
and chose to give that treatment to cameras rather than to the object type that
would most benefit from a per-placement tweak.

---

### F40 · A quest's identity is a name; everything else's is a number
**Follows from:** `RECORDS.md` → JRL; `README.md` §6

Quests are addressed by `Tag`, a string, throughout — script, save
(`JNL_PlotID`), and UI. This is **good**, and it is nearly unique in the game:
rules are row indices (batch 2), blueprint references are row indices (batch 3),
and only the world layer uses names.

The flaw is the inconsistency, not the choice. The same save file that stores a
quest by name stores a skill by array position, a feat by table row, a faction
by matrix index and an appearance by row number. A reader has to know, per
field, which of two philosophies applies — and nothing in the data says which.

*Recorded here rather than as praise because the lesson for our format is "pick
one", and KOTOR demonstrates the cost of not.*

---

### F41 · Quest state is one integer, and completion is ambiguous
**Follows from:** `RECORDS.md` → JRL; `README.md` §6

A quest's entire state is `JNL_State` — one stage id — plus a timestamp. No
sub-objectives, no flag set, no partial progress.

Two consequences:

**Stage ids are labels, not ordinals.** They run 1–150 in K1 and 1–100 in K2 and
are **not monotonic within a quest** in either game. So two states cannot be
compared to see which is further along. "Where is this quest up to" is
answerable only by looking the id up in the authored list.

**"Complete" is not a state.** `End` is set on multiple stages in **47 of 101 K1
quests and 63 of 117 K2 quests** — up to nine on one K2 quest. So a quest that
has ended does not have a canonical end state, and any consumer asking "did they
finish it?" gets a boolean that hides *which* ending occurred.

For a cross-campaign carry mechanism this is the crux: **the stage id is the
thing worth carrying, and the completion flag is not.**

---

### F42 · Nothing connects a module to the quests it advances
**Follows from:** `RECORDS.md` → JRL; `README.md` §6

A module has no quest reference of any kind. The only link is a script inside
the module naming a tag inside a game-global file, and the tag appears nowhere
in the IFO, ARE or GIT.

So there is no way to ask "which quests does this module touch?" without
decompiling every script it contains, and no way to ask "which modules does this
quest span?" at all. `PlanetID` on the quest is a display grouping, not a
binding.

Combined with batch 2's F18 (no module-local rules) and F23 (one global string
table), the pattern completes: **content is packaged per module; everything that
gives content meaning is game-global and unlinked.** A module is portable in the
sense that its files move together, and not portable in any sense that matters.
