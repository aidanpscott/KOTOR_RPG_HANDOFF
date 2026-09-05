# STUDY 03 — BLUEPRINT LAYER — FLAWS

F24–F33, continuing batches 1 and 2. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

---

### F24 · The struct type id carries payload, not schema
**Follows from:** `RECORDS.md` → GFF, UTC

GFF gives every struct a `Type` field, whose job is to say **what shape this
struct is**. Most lists use it that way — `SkillList` 0, `FeatList` 1,
`ClassList` 2, `SpecAbilityList` 4, constant across all 4,397 creature
blueprints in both games.

Two lists do not:

- **`Equip_ItemList`** stores the **equipment slot bitmask** there — 13 distinct
  values, matching `baseitems.equipableslots` hex.
- **`ItemList`** stores the **inventory sequence number** there — 34 distinct
  values in K1.

So the same field means "which schema" in three lists and "which slot" or
"which position" in two others, within one file.

The cost is concrete. A generic GFF reader cannot round-trip a UTC: rewriting it
with normalised struct types silently unequips every item. And a validator
cannot check struct types against a schema table, because for two lists there
is no schema to check — the value is data.

*The slot needed one BYTE field inside the struct. It was given a field reserved
for something else instead.*

---

### F25 · 82 blueprints carry an appearance index past the end of the table
**Follows from:** `RECORDS.md` → UTC; `README.md` §6, §7

`Appearance_Type` is a bare row index into `appearance.2da`. In K1 the shipped
values run **1..546** against a **509-row** table. 82 blueprints, 78 distinct
resrefs, index rows that do not exist.

`Race` overflows too: values to 8 against `racialtypes.2da`'s 7 rows.

Nothing detects this. There is no bounds information in the blueprint (F13/GFF
semantics), no declared target table, and no validation pass — so the defect
ships and stays shipped.

**It is also evidence about batch 1's F08.** All 82 are in `.mod` files; zero in
`.rim`; zero in the BIF layer. 36 of the 78 resrefs also exist in a `_s.rim`
with a valid value. The `.mod` copies were built against a larger
`appearance.2da` than the one that shipped — so the 34 duplicated modules are
**not equivalent copies**, and one of the two sets contains unresolvable
references. Which one the engine loads is still unknown; that it matters is now
established.

---

### F26 · `SkillList` is the one progression list with no id, and nothing enforces its length
**Follows from:** `RECORDS.md` → UTC; `README.md` §3

Across the whole blueprint layer, every progression list carries an explicit
identifier — `ClassList.Class`, `FeatList.Feat`, `KnownList0.Spell`,
`SpecAbilityList.Spell`. **`SkillList` alone is `[{Rank}]` with position as
identity.**

The consequence is not theoretical. **Three K1 blueprints ship a 20-entry
`SkillList`** — `c_drdg`, `c_sebulba`, `partymember` — with real ranks in the
extra slots (`partymember` carries rank 4 at index 18). Nothing rejected them,
because with no id there is nothing to reject against: any array length is
syntactically valid and semantically meaningless.

One of those three is `c_sebulba`, a prequel-film character with no role in
either game. It shipped, in the BIF layer, with a skill array of the wrong
length, for twenty-plus years.

*This is the single most transferable finding in the study. Eight skills looked
fixed in 2003 too.*

---

### F27 · Column names lie about what they hold
**Follows from:** `RECORDS.md` → UTI; `README.md` §5

`itempropdef.2da` has three columns named `subtyperesref`, `costtableresref`
and `param1resref`.

- `subtyperesref` holds an actual table name (`iprp_abilities`, `feat`, …).
- **`costtableresref` and `param1resref` hold decimal strings** — `'0'`, `'1'`,
  `'11'`, `'14'` — which are row indices into `iprp_costtable.2da` and
  `iprp_paramtable.2da`.

Two of the three columns are named for a mechanism they do not use. Combined
with batch 2's F13 (cells are untyped), the name is the *only* documentation a
reader has, and here it is wrong.

Same family, elsewhere in this layer: **`UTM` and `UTE` use `ResRef` where every
other blueprint uses `TemplateResRef`** for the identical purpose, and the `GIT`
`StoreList` follows UTM's spelling. And `UTC.ItemList` ships both `Repos_Posy`
and `Repos_PosY` — 1,468 entries with the lowercase spelling, 139 with the
uppercase, in the same games.

---

### F28 · A creature instance can override nothing
**Follows from:** `RECORDS.md` → UTC; `README.md` §4

Every creature instance in every area file of both games carries exactly six
fields: a template name and five position/orientation floats. 100% of 1,619 K1
and 1,700 K2 instances.

There is **no inheritance, no partial override, no copy-on-write.** Two guards
who differ only in hit points require two complete blueprints.

The waste is visible in the counts: 1,589 distinct creature blueprints in K1's
modules for 1,619 placements — **roughly one blueprint per instance**. The
template layer is barely functioning as a template layer.

---

### F29 · The override surface is inconsistent, and inverted
**Follows from:** `README.md` §4

What an instance may override varies per type with no discernible principle:

```
Creature   nothing
Sound      GeneratedType
Store      ResRef
Placeable  Bearing (+ TweakColor in K2)
Encounter  Geometry, SpawnPointList
Trigger    Geometry, Tag, TransitionDestin, LinkedTo*
Door       Tag, LinkedTo*, TransitionDestin, Bearing (+ TweakColor in K2)
Waypoint   Appearance, Tag, LocalizedName, Description, HasMapNote,
           MapNote, MapNoteEnabled
```

**The richest blueprint gets the poorest instance and the poorest blueprint gets
the richest.** A waypoint — 11 fields — can override its own name and
description per placement. A creature — 70 fields — can override nothing.

And even position is not uniform: creatures and triggers use
`XPosition`/`YPosition`/`ZPosition` with `XOrientation`/`YOrientation`, while
placeables and doors use `X`/`Y`/`Z` with a single `Bearing`. **Two coordinate
conventions in the same file.**

---

### F30 · Dead fields, third instance — now a confirmed house pattern
**Follows from:** `RECORDS.md` → GFF, UTC

Batch 1 F07 found dead declared fields in the archive headers
(`LanguageCount`, `FixedResCount`, `DescriptionStrRef`). Batch 2 F21 found three
dead fields in every TLK entry, with a flag bit asserting data that is not there.
This layer adds:

- **`TemplateList`** — a List field on every UTC, **length 0 in all 2,653 K1 and
  all 1,741 K2 files.**
- **`Deity`** — present at 100% in both games, an NWN concept with no KOTOR
  meaning.
- **`LawfulChaotic`** — 100% in both games; KOTOR has one alignment axis.
- **Eight of GFF's nineteen field types** are never used by any blueprint,
  including the dedicated `StrRef` type while every string reference travels
  inside a `CExoLocString` instead.
- K1 only, on 1–3 files each: `Tail`, `Wings`, `Morale`, `MoraleBreakpoint`,
  `MoraleRecovery`, `SaveFortitude`, `SaveReflex`, `SaveWill`,
  `Appearance_Head`, `SoundSet`.

Across three batches the pattern is consistent enough to state as a rule: **these
formats inherited capability they never removed, then shipped it populated with
zeroes.** The cost is that a reader cannot tell inherited-and-dead from
new-and-unused-so-far without checking every file in the game.

---

### F31 · Toolset metadata shipped in the product
**Follows from:** `RECORDS.md` → UTC, UTI, UTP, UTD, UTW

`KTGameVerIndex`, `KTInfoDate` and `KTInfoVersion` appear on 55 K1 creature
blueprints and on K1 door, item, placeable and waypoint blueprints. They are
authoring-tool bookkeeping, present in the shipped game.

`Comment` is worse in kind and universal in reach: **every blueprint of every
type in both games carries an author-notes field**, shipped to every player.

K2 removed the `KT*` triple and kept `Comment`.

*Minor as a defect. Recorded because it shows there was no separation between
authoring format and runtime format — the file the designer edited is the file
that shipped, and that is the same decision that put `PaletteID` (an object-
browser grouping) on every runtime record.*

---

### F32 · Duplicated denormalised data with nothing keeping it in step
**Follows from:** `RECORDS.md` → UTE

A `UTE.CreatureList` entry carries `{ResRef, Appearance, CR, SingleSpawn}`.
`Appearance` and `CR` **already exist on the UTC that `ResRef` names.**

So a creature's appearance and challenge rating are stored in two places, with
no constraint that they agree, and nothing in the data says which wins. Editing
the creature does not update the encounters that spawn it.

I could not determine which the engine uses — it needs the running game — and
that is precisely the problem: neither can a designer.

---

### F33 · Blueprint scope is decided by file location, not by declaration
**Follows from:** `RECORDS.md` → all types; `README.md` §2

The same UTC file is game-global in the BIF layer and module-local in a module
archive. **Nothing on the blueprint says which it is.** Scope is a property of
where the bytes happen to sit.

Two consequences. A blueprint cannot declare its own intent, so moving a file
silently changes its reach. And the collision behaviour is batch 1's F02 all
over again: 139 K1 and 117 K2 blueprint resrefs exist in **both** the BIF layer
and a module, 189 of them with different bytes, with no declared winner.

This is the blueprint-layer instance of the pattern batch 2 named in F18 for the
rules layer: **KOTOR has no scoping mechanism anywhere.** Not for 2DAs, not for
strings, not for blueprints. Reach is always a side effect of file placement.

---
---

# PART TWO — OBSERVATIONS ON **OUR** FORMAT

**⚠ Different subject, different catalogue.** Everything above (F24–F33) is
about KOTOR. Everything below is about `CHARACTER-RECORD-01`, found by comparing
it against UTC in `README.md` §3. These are **not** source-game flaws and must
not be cited as such — hence the separate numbering (`OF`), so a later batch
merging the study-wide flaw catalogue does not blend the two.

These follow from reading `STUDY/_reference/CHARACTER-RECORD-01.md`, which is a
read-only copy. Where something below reads as an error in the spec, it is
reported here rather than corrected there.

---

### OF01 · There is no current-state layer, anywhere
**Follows from:** `README.md` §3.5, item 1

`CHARACTER-RECORD-01` holds no current hit points, no current Force, no
conditions, no position. Its purpose line is honest about this — it is the
contract the eleven creation screens write into — but **nothing else specifies
what a character in play is**, and the record is what "every later system reads
from".

KOTOR carries `CurrentHitPoints` and `CurrentForce` on the creature record and
position on the placement. A wounded character has somewhere to be wounded.

This is the largest structural gap the comparison found. It is not a rules
disagreement; it is a missing half of the model, and every system that touches
combat, healing, rest or death will need it before it can be written.

---

### OF02 · No NPC record exists, and the PC record cannot become one cheaply
**Follows from:** `README.md` §3.3

A package ships hundreds of NPCs. Nothing describes them.

If they are `CHARACTER-RECORD-01` records, we inherit KOTOR's collapse — F28's
one-template-per-instance, 1,589 blueprints for 1,619 placements — **plus** a
replay cost per NPC that KOTOR never paid, because our record is a projection of
an event log and KOTOR's is a file you open.

And the event-log model makes the usual fix harder rather than easier: a record
that is replay output cannot inherit from a template, because inheritance would
have to be a shared log prefix. That is either event-copying (the same collapse
one layer down) or a fork model that nothing specifies.

Two things genuinely soften it — storing choices rather than consequences means
near-identical characters diverge in a few events rather than forty derived
values, and `package` scoping avoids KOTOR's flat global resref namespace
(F33). Neither addresses the absence.

*This is the one to close first, because §3.2's conclusion is that the two
storage models serve different populations and we have specified only one.*

---

### OF03 · `feats[].source` violates the document's own first principle
**Follows from:** `README.md` §3.4

`CHARACTER-RECORD-01` §2 opens with **"store the choice, derive the
consequence"**, and gives the reason: two sources of truth means one goes stale.

`feats[].source` stores whether a feat was `granted` or `chosen`. Granted-ness
is **not a choice** — it is a consequence of the class feat schedule. KOTOR
derives exactly this, from `feat.2da`'s `<cls>_granted` column, which holds the
level at which each class grants each feat.

So a change to `FEAT-SCHEDULE-01` leaves stored `source` values describing a
schedule that no longer exists — the precise failure the principle exists to
prevent, in the same document that states it.

**The mitigation is real but narrower than it looks.** In a pure projection a
denormalised field is harmless, because it is regenerated on every replay. It
becomes a hazard the moment anything persists the projection: a cache, an export,
a save file, a package handed to another player. §3's own table already lists
nine things as "derive, never store"; this is a tenth that was stored.

*Same argument applies more weakly to `feats[].at_level` and
`powers[].at_level`, which the log already knows.*

---

### OF04 · Alignment has a chapter and no field
**Follows from:** `README.md` §3.5, item 2

`ALIGNMENT-01-v2` specifies seven bands, directional hysteresis, dark-power
drift, four atonement routes, meditation, passive recovery below 50, and Wisdom
resistance. **The record has no key for any of it.**

KOTOR has `GoodEvil` — one byte, 0–100, no band, no direction, no history. Crude,
and present.

Whether alignment belongs on the character record or in a separate play-state
record is a real design question — but it currently exists in neither, and
§3.5's OF01 gap means there is no play-state record to put it in.

---

### OF05 · Equipment has no slot model
**Follows from:** `README.md` §3.5, item 3

`equipment.items` is a flat array of item ids. There is no way to express
"wielding the lightsaber, wearing the robe, carrying two medpacs" — and two
medpacs are two array entries, because there is no stacking either.

KOTOR separates `Equip_ItemList` (slot-keyed, though it abuses the GFF struct
type to do it — F24) from `ItemList` (carried, with grid coordinates and
`StackSize` on the item).

`EQUIPMENT-01` defines wield classes and armour categories that the record as
specified cannot represent.

---

### OF06 · Derived-only vitality leaves no authoring escape hatch
**Follows from:** `README.md` §3.4

`CHARACTER-RECORD-01` §3 derives vitality, defence, saves and attack bonus from
classes, abilities and feats. For a player character that is right — it is the
"one source of truth" argument working as intended.

For **authored** content it removes something KOTOR has and uses constantly. A
designer cannot give one particular guard 40 hit points without inventing a
class or a feat to justify it. KOTOR freezes `HitPoints`, `MaxHitPoints`,
`NaturalAC`, the three save bonuses and `ChallengeRating` onto the record
precisely so an author can override the arithmetic for one creature.

This compounds with OF02: the moment NPCs use this record shape, "make this one
tougher" becomes a daily need with no supported answer.

*The fix is not to abandon derivation — it is an explicit override layer, which
is a different thing from a stored value and can be validated as one.*

---

### OF07 · Replay determinism is assumed, and live-campaign drift is unaddressed
**Follows from:** `README.md` §3.2

The event-log model's headline benefit is stated in §2: a rules change to
`SKILLS-01`'s aptitude stacking "should change every character, not none of
them."

That is right for a specification under development and **hazardous for a saved
campaign**. The same property means a group's characters can change between
sessions because a rule was edited, with nothing telling them it happened.

Two requirements follow that the document does not state:

- **Replay must be deterministic.** Every derivation pure, every table lookup
  version-pinned. Otherwise the same log yields different characters on
  different days, which is a correctness bug rather than a feature.
- **The log's schema is a stronger compatibility commitment than a record
  format's.** An event type written today must remain interpretable indefinitely,
  because the log is the only store and cannot be migrated in place — only
  appended to.

§4's `validate on load` catches a record that became **illegal**. It does not
catch one that quietly became **different**, and the second is the more likely
outcome of a rules edit.
