# STUDY 03 — BLUEPRINT LAYER

The reusable object templates of KOTOR 1 and KOTOR 2 — UTC, UTI, UTP, UTD, UTT,
UTM, UTS, UTW, UTE — and the GFF format they are all written in.

| file | what it is |
|---|---|
| `RECORDS.md` | GFF + nine blueprint records |
| `README.md` | this file — GFF answers, **§3 the UTC vs CHARACTER-RECORD-01 comparison**, template/instance, items, positional sweep |
| `FLAWS.md` | **Part one** F24–F33 (KOTOR). **Part two** OF01–OF07 (observations on *our* format, kept separate) |
| `NAMING.md` | batch-3 vocabulary |

**Method.** Every blueprint in both games was read with a GFF reader written for
this pass — 2,656 K1 and 1,741 K2 creature blueprints, 13,000+ blueprints in
total across BIF and every module archive. "Every" means every. Inferences are
marked; negatives name what was searched.

**Sits on:** batch 1 (containers, the duplicate `.mod` question F08, precedence
F02) and batch 2 (2DA reference mechanisms, positional identity, F18).

---

## 1 · GFF, and the question that matters

Full record in `RECORDS.md`. The headline answer to *"is it self-describing?"*:

**Structurally yes. Semantically no. And the gap is the whole problem.**

A reader with no schema can walk any blueprint and print every field name, type
and value correctly — the labels and type tags are in the file. What it cannot
know is that `Appearance_Type = 452` is a **row index into `appearance.2da`**,
while `Str = 14` beside it is a **quantity**. Both are integers of the same
width in the same shape. Nothing in the file names a target table, and nothing
marks a field as a reference at all.

So the format carries **shape** but not **meaning**, and the entire reference
graph lives only in code. This is batch 2's F13 (untyped 2DA cells) one layer
up, and the two compound: an integer in a blueprint points at a row in a table
whose columns are also untyped.

**Nineteen field types are defined; blueprints use eleven.** Never used by any
blueprint: `DOUBLE`, `DWORD64`, `INT64`, `Orientation`, `Vector`, `VOID`,
**`StrRef`**, **`Struct`**.

The last two are worth stating plainly. There is a dedicated `StrRef` type and
**no blueprint uses it** — string references travel inside `CExoLocString`
instead. And there is a `Struct` type and **no blueprint nests one** — all
nesting is through lists. A blueprint is always a flat record plus arrays.

**⚠ The struct type id is doing two different jobs.** In most lists it is a
constant schema tag (`SkillList` 0, `FeatList` 1, `ClassList` 2,
`SpecAbilityList` 4). But `Equip_ItemList` uses it as the **equipment slot
bitmask** — 13 distinct values matching `baseitems.equipableslots` — and
`ItemList` uses it as the **inventory sequence number**. A format-level field
that identifies a struct's schema is carrying payload. See `FLAWS.md` F24.

---

## 2 · The nine types, and where the boundary sits

| type | what it is | K1 BIF / modules | K2 BIF / modules | fields |
|---|---|---|---|---|
| **UTC** | creature | 205 / 1,589 | 284 / 932 | ~70 |
| **UTI** | item | 557 / 302 | 994 / 127 | 20 |
| **UTP** | placeable | 317 / 884 | 383 / 463 | **62** |
| **UTD** | door | 50 / 434 | 104 / 256 | 58 |
| **UTT** | trigger | 21 / 812 | 34 / 312 | 31 |
| **UTS** | sound | **0** / 395 | **0** / 417 | 25 |
| **UTM** | merchant | **0** / 38 | **0** / 17 | **10** |
| **UTW** | waypoint | 9 / 1,738 | 9 / 400 | **11** |
| **UTE** | encounter | 65 / 60 | 65 / 40 | 22 |

Module counts are distinct resrefs. **UTS and UTM never appear in the BIF layer
of either game** — they are structurally module-only. Searched both KEY indexes.

**No other blueprint type exists.** Searched both KEY indexes and all 644 module
archives for every GFF-family resource type; the nine above are the complete set
of `UT*` types. `GIT`, `ARE`, `IFO`, `DLG`, `JRL`, `FAC` are GFF but are not
blueprints — they belong to batches 4 and 5.

**Where the boundary sits — what is ON the blueprint versus looked up:**

*On the blueprint:* everything instance-independent. Attributes, hit points,
flags, script hooks, inventory contents, list membership.

*Looked up from a 2DA by row index:* everything catalogued — appearance,
portrait, race, gender, faction, body bag, palette, trap type, door type,
placeable model, and the entire item-property chain.

*Resolved at spawn by ResRef:* scripts, conversations, equipped and carried
items, sound files.

*Deferred to the instance:* position and orientation, always. Plus, per type,
a small and inconsistent set of overrides — see §4.

The consistent rule is that **a blueprint holds values and names; it never holds
geometry**. The inconsistent part is which type gets to override what.

---

## 3 · ⚠ UTC against CHARACTER-RECORD-01

**Source note.** This section was rewritten against the real specification, read
from `STUDY/_reference/CHARACTER-RECORD-01.md`. The first version of this
section inferred our side from `docs/`; that version is gone, not appended to.
The reference copy is read-only — nothing below edits it, and where it looks
wrong the observation is reported rather than corrected.

**A correction I should carry.** In the batch-3 report I flagged `SKILLS-01`
line 15 reading "twenty-two skills" against a brief saying 24, and asked which
was stale. Neither. That line is the **quoted text of a historical error** —
`PT-865` records the header once reading that and being corrected. The live
count is **24**, and every count below uses 24. The failure mode is worth
naming because a corpus that records its corrections in place will produce it
again: **a claim carries the warrant of its reading, not of its relay.** Raising
it was right; concluding from it was not.

The full UTC field pass is in `RECORDS.md` → UTC. This section compares.

---

### 3.1 Field by field

**Both store the concept.**

| concept | UTC | CHARACTER-RECORD-01 |
|---|---|---|
| name | `FirstName` + `LastName` (CExoLocString) | `identity.name` |
| portrait | `PortraitId` (row index) | `identity.portrait{kind, ref}` |
| species | `Race` + `Subrace` + `SubraceIndex` | `species{id, subrace, chassis, model}` |
| gender | `Gender` (row index) | `gender` |
| classes | `ClassList[{Class, ClassLevel, KnownList0}]` | `classes[{id, levels}]`, max 3 |
| abilities | `Str Dex Con Int Wis Cha` | `abilities{str…cha}` |
| skills | `SkillList[8]{Rank}` | `skills{name: rank}` |
| feats | `FeatList[{Feat}]` | `feats[{id, source, at_level}]` |
| powers | `ClassList[].KnownList0[{Spell, …}]` | `powers[{id, at_level}]` |
| equipment | `Equip_ItemList` + `ItemList` | `equipment{route, items, credits}` |
| level | `ClassList[].ClassLevel` | `progress{level, xp}` |

**Only KOTOR has it** — grouped, because the grouping is the finding.

*Current state:* `CurrentHitPoints`, `MaxHitPoints`, `HitPoints`, `CurrentForce`,
`ForcePoints`.
*Derived-but-frozen:* `NaturalAC`, `fortbonus`, `refbonus`, `willbonus`,
`ChallengeRating`.
*World identity:* `Tag`, `TemplateResRef`, `FactionID`, `IsPC`, `PaletteID`.
*Narrative protection:* `Plot`, `Min1HP`, `NoPermDeath`, `Disarmable`,
`Interruptable`, `PartyInteract`.
*Embodiment:* `Appearance_Type`, `BodyVariation`, `TextureVar`, `Phenotype`,
`SoundSetFile`, `BodyBag`.
*Behaviour:* fourteen `Script*` hooks, `Conversation`, `PerceptionRange`,
`WalkRate`, `BlindSpot`, `IgnoreCrePath`, `MultiplierSet`, `NotReorienting`.
*Alignment:* `GoodEvil`.
*Other:* `SpecAbilityList`, `Comment`.

**Only ours has it.** `schema`, `id`, `package`; `identity.story` and
`story_origin`; the whole `origin` block (`world`, `world_open`,
`aptitude_skill`, `upbringing`); the whole `backstory` block (`profession`,
`programming`, `lifestyle`, `grant_taken`); `species.chassis` and
`species.model`; `feats[].source` and `at_level`; `powers[].at_level`;
`equipment.route` and `credits`; `progress.xp`.

---

### ⚠ Same concept, stored differently — the interesting category

**Skills.** UTC: a fixed 8-slot array of bare ranks, position implying which
skill. Ours: a sparse map keyed by skill name, with absent meaning rank 0. This
is the divergence batch 3 spent most of its effort on, and it is the one place
where the two designs are not on a spectrum — they are opposites. Ours can hold
24 skills and grow; KOTOR's cannot hold 9.

**Feats.** UTC stores `{Feat}` — the id and nothing else. Ours stores
`{id, source, at_level}`. KOTOR records **that** you have a feat; ours records
**how and when** you got it. Note the direction: KOTOR can *derive*
granted-versus-chosen from `feat.2da`'s `<cls>_granted` column, which holds the
level a class grants a feat at. We store what KOTOR computes. See §3.4.

**Powers.** UTC nests them **inside the class entry** — `ClassList[].KnownList0`
— so the record knows which class granted which power, and carries
`SpellMetaMagic` and `SpellFlags` per power. Ours holds a flat top-level
`powers[]` with only `id` and `at_level`. Given that `MULTICLASS-01` §2.2a
identifies powers-known as the real multiclass gap and closes it with a pool
split, KOTOR's nesting stores exactly the association that rule needs and ours
discards it.

**Name.** UTC uses `CExoLocString` — a string index into the game-wide table
plus optional inline translations. Ours uses a plain string. KOTOR's is built
for localisation and inherits batch 2's F23 with it; ours is not localisable at
all.

**Portrait.** UTC: a bare integer into `portraits.2da`. Ours:
`{kind: "preset", ref: "bith_04"}` — a tagged union with a named referent, so a
non-preset kind can be added without renumbering anything.

**Species.** UTC spends three fields — `Race` (index), `Subrace` (string),
`SubraceIndex` (index) — two of them redundant with each other and with no
stated relationship. Ours uses one nested object with an explicit
mutual-exclusion rule (`subrace` XOR `chassis`, `model` only with `chassis`).

**Equipment.** UTC has two lists: `Equip_ItemList` with the **slot in the GFF
struct type id** (F24), and `ItemList` with grid coordinates. Ours has one flat
`items[]` array with no slot concept at all. See §3.5.

**Level and XP.** UTC has per-class `ClassLevel` and **no XP field anywhere on
the creature record** — experience lives in the save's party table. Ours has
`progress{level, xp}` plus per-class `levels`, with a validation rule that they
sum. Ours is the more complete record; KOTOR's split is a consequence of the
blueprint being shared by 1,589 NPCs who never gain XP.

**Absence.** Ours states "absent, not zeroed" as a principle — a droid has no
`upbringing` key. UTC is the exact opposite: **every field present on every
file**, zeroed when meaningless. Batch 2 F14 showed KOTOR loses the same
distinction one layer down, where `****` collapses to empty string in compiled
2DAs. KOTOR cannot express "not applicable" anywhere in either layer.

---

### 3.2 ⚠ The storage model

Ours: the record is a **projection of an append-only event log**. Creation
writes events; the record is what replaying them produces; the log persists.
KOTOR's: the blueprint **is** the store, and a save holds a replacement copy —
batch 1 found `SAVEGAME.sav` embedding full `UTC` records for companions
(`AVAILNPC0…8`) alongside a per-module `{ARE, GIT, IFO}` snapshot.

**What the event log buys.** Corrections do not destroy prior state. The "store
the choice, derive the consequence" principle only works if the choice is what
persisted — a rules change to `SKILLS-01`'s aptitude stacking then reaches every
existing character, which is stated as the goal. History is answerable without
being separately stored. And multiplayer sync falls out of visibility sets over
the log rather than needing its own design.

**What it costs, honestly.** Every read requires a replay, so nothing can just
open the file. The log's own schema must stay replayable forever — an event type
written today must be interpretable in five years, which is a stronger
compatibility commitment than a record format's. Replay must be deterministic,
which means every derivation is pure and every table lookup is version-pinned,
or the same log yields different characters on different days. And the headline
benefit has a matching hazard: **if a rules change reaches every existing
character, then a live campaign's characters change under its players between
sessions.** "Should change every character, not none of them" is right for a
spec under development and dangerous for a saved game in progress. Nothing in
`CHARACTER-RECORD-01` §4 addresses that — `validate on load` catches a record
that became *illegal*, not one that quietly became *different*.

**What KOTOR's model buys, argued in its own favour.**

*Load is O(1).* Open the file, you have the creature. With 2,656 K1 creature
blueprints and 1,619 placements in one area set, no replay budget would survive.

*Authoring is direct.* A designer edits a UTC in a tool and sees the result.
There is no "author an event stream" problem, and no need for the toolset to
model creation as history.

*The record is a portable artifact.* A blueprint can be handed to another
module, another tool, another team and read standalone. An event log needs the
replay engine **and** the rules tables at the right version to mean anything —
so the log is not an interchange format, and something UTC-shaped has to be
generated whenever content crosses a boundary.

*Save/restore is trivially correct.* Batch 1 showed the save just embeds copies.
There is no class of bug where the reloaded character differs from the one on
screen, because nothing is recomputed.

*Immunity to drift is a feature for authored content.* A shipped creature is
exactly what shipped, and a later patch cannot silently restat it. (KOTOR broke
this itself — F25's 82 blueprints with dangling appearance indices — but the
breakage is a data error, not a model failure.)

**The honest reconciliation, and it is the section's main conclusion.** These two
models are not competing answers to one question. They serve different
populations. An event log is right for a **player-owned character that evolves
and whose history matters**. A frozen record is right for **authored content
that is placed, not played** — the 1,589 NPCs a package ships. `CHARACTER-
RECORD-01` covers only the first, and its opening line says so: it is the
contract the creation screens write into.

So the model choice is not ours-versus-KOTOR's. **We will need both**, and the
missing half is unspecified — see §3.3 and §3.5.

---

### 3.3 ⚠ Against §4 — does our model collapse the same way?

§4 established that a KOTOR creature instance can override nothing: six fields,
and in practice 1,589 distinct blueprints for 1,619 placements — roughly one
template per instance. The template layer is barely functioning as one.

**Ours has the same collapse, and in a stronger form.**

`CHARACTER-RECORD-01` has **no template/instance split at all.** Every character
is a complete record with its own `uuid`. Two characters differing in one choice
are two complete records. KOTOR at least *has* the split, even though the
instance side is nearly empty; ours does not have the concept.

**The event log makes templating harder, not easier.** Because the record is
replay output, one record cannot inherit from another — inheritance would have
to be a shared log prefix, which means either copying the events (the same
collapse, one layer down) or a fork/branch model that nothing specifies.

**Two things genuinely mitigate it.** Because we store choices rather than
consequences, two near-identical characters diverge in a handful of *events*
rather than in forty derived values — the authored difference is small even
though the record count is not. And `package` scoping means records need not be
globally unique in the way KOTOR's flat resref namespace demands (batch 3 F33).

**But the real gap is not mitigation, it is absence.** A package ships hundreds
of NPCs. `CHARACTER-RECORD-01` does not describe them, and nothing else does
either. If NPCs are `CHARACTER-RECORD-01` records we inherit KOTOR's one-record-
per-instance problem **plus** a replay cost per NPC that KOTOR never paid. If
they are something else, that something else is unspecified. This is the largest
structural hole the comparison found and it is recorded in `FLAWS.md` under the
our-format heading.

---

### 3.4 Derived versus stored

Ours derives, per `CHARACTER-RECORD-01` §3: ability adjustments, species
bonuses and traits, the aptitude set, skill rank caps, vitality, defence, saves,
attack bonus, Force points, languages, credits remaining.

**KOTOR freezes every one of those into the blueprint.** `HitPoints`,
`MaxHitPoints`, `CurrentHitPoints`, `ForcePoints`, `CurrentForce`, `NaturalAC`,
`fortbonus`, `refbonus`, `willbonus`, `ChallengeRating` — all stored values on
the record, not lookups.

**And KOTOR ships our mechanism, disabled.** `racialtypes.2da` carries
`stradjust`, `dexadjust`, `intadjust`, `chaadjust`, `wisadjust`, `conadjust` —
exactly the derive-on-read species modifier `CHARACTER-RECORD-01` §5 closes at
`PT-1260`. **Every one of those columns is `0`**, in both games, for both
labelled rows; five of the seven rows have no label at all. KOTOR has two
species, Human and Droid, and neither adjusts an ability. So the question of
whether UTC stores bought or final scores is moot in KOTOR — with all
adjustments zero they are the same number — and the mechanism is another
instance of F30's dead-capability pattern.

**Where KOTOR froze and freezing was the better call.**

*Hit points, clearly.* A designer can give one particular guard 40 HP without
touching a rule. Our model derives vitality from classes, abilities and feats,
so **there is no way to author a one-off tougher enemy** short of inventing a
class or a feat for it. A derived-only model has no escape hatch, and authored
content needs one. If NPCs use our record shape, this becomes a daily problem.

*`ChallengeRating`, probably.* It lets an author say "this fight is harder than
the arithmetic suggests". We have no equivalent field. (F32's complaint stands —
UTE duplicates it with nothing keeping the copies in step — but that is a
denormalisation defect, not an argument against having the field.)

*`CurrentHitPoints` as distinct from `MaxHitPoints`, decisively.* See §3.5.

**Where we freeze and KOTOR derives — and we are on the wrong side of our own
principle.** `feats[].source` distinguishes `granted` from `chosen`. That is a
**consequence of the class feat schedule**, not a choice the player made — and
KOTOR derives exactly this from `feat.2da`'s `<cls>_granted` column, which holds
the level at which each class grants each feat. Storing it means
`FEAT-SCHEDULE-01` changing leaves stored `source` values stale, which is the
precise failure "store the choice, derive the consequence" exists to prevent.

The mitigation is real but narrow: in a pure projection a denormalised field is
harmless because it is regenerated. It becomes a hazard the moment anything
persists the projection — a cache, a save file, an export, a package handed to
another player. Recorded in `FLAWS.md`.

---

### 3.5 ⚠ What we are missing

Bluntly, and in order of how much it will hurt. Twenty years of shipped content
knows things a specification does not.

**1 · There is no current state anywhere in the record.** No current hit points,
no current Force, no conditions, no position. `CHARACTER-RECORD-01` is a
creation-time contract — its own purpose line says so — and nothing else
specifies what a character *in play* is. KOTOR carries `CurrentHitPoints` and
`CurrentForce` on the record and position on the instance. A wounded character
has nowhere to be wounded. This is the largest gap and it is not a rules
difference; it is a missing half of the model.

**2 · No alignment field.** `ALIGNMENT-01-v2` defines seven bands with
hysteresis, drift, atonement routes and passive recovery. The record has no key
for any of it. KOTOR has `GoodEvil`, one byte — crude, but present.

**3 · No equipment slots.** Ours has a flat `items[]`. There is no way to
express "wielding this, wearing that, carrying two of the other". KOTOR has
`Equip_ItemList` keyed by slot plus `ItemList` for carried, with `StackSize` on
the item. `EQUIPMENT-01` defines wield classes and armour categories that the
record cannot represent.

**4 · No faction or relationship handle.** KOTOR has `FactionID` into a
relationship matrix (batch 2's `repute.2da`). Any NPC needs one, and so does any
party member who can be turned hostile.

**5 · No narrative-protection flags.** `Plot`, `Min1HP`, `NoPermDeath`. Three
booleans that solve the story-NPC-must-not-die problem, cheaply, and we have
none of them.

**6 · No embodiment beyond a portrait.** An organic character has no body model
reference at all. KOTOR has `Appearance_Type`, `BodyVariation`, `TextureVar`,
`Phenotype` and `SoundSetFile`. Our `species.model` exists only for droid
chassis.

**7 · No script handle.** Ours has a `uuid`, which is identity but not a name
anything can author against. KOTOR's `Tag` is how a script says "the guard in
the cantina" without knowing which uuid that is.

**8 · No behaviour attachment.** KOTOR has fourteen event hooks and a
`Conversation`. For a tabletop-first app that may be correct — but a package has
to attach *something* to a character, and nothing specifies what.

**9 · No stacking or inventory position.** Two medpacs are two array entries.
KOTOR has `StackSize` on the item and grid coordinates on the inventory entry.

**10 · No `IsPC` equivalent.** Once packages ship NPCs, something has to say
which records are player-owned.

---

### 3.6 What we carry that KOTOR structurally cannot

Only structural differences — rules differences are not the point.

**A sparse, named, extensible skill map.** 24 skills with room to grow, absent
meaning zero. KOTOR has eight positional slots with no identifier and cannot
reach nine.

**Provenance on progression entries.** `source` and `at_level` on feats,
`at_level` on powers. KOTOR's `FeatList` carries an id and nothing else, so a
KOTOR record cannot answer "when did this happen" at all.

**A declared content schema.** `schema: "CHARACTER-RECORD-01"` versions the
*content*. KOTOR blueprints carry a *format* version (`V3.2`, on every one of
3,097 files) and nothing about the shape of what is inside.

**Declared scope.** `package` is on the record. Batch 3 F33 found KOTOR decides
a blueprint's reach by which file it happens to sit in, with nothing on the
record saying so.

**Absent-as-meaningful.** A droid has no `upbringing` key. KOTOR ships every
field on every file and cannot distinguish inapplicable from zero — at either
layer, per batch 2 F14.

**Player-authored free text with a recorded provenance.** `identity.story` plus
`story_origin`, and `origin.world_open`. Earlier work established KOTOR consumes
exactly one piece of typed text, the character's name, and nothing else in
either game.

**Stated invariants.** `subrace` XOR `chassis`; `origin` absent iff droid;
`gender` absent iff Astromech or Remote; classes ≤ 3 and levels summing to
`progress.level`. KOTOR has three overlapping species fields with no stated
relationship between them and no validation anywhere.

---

## 4 · ⚠ Template versus instance

**A creature instance can override nothing.**

Every `Creature List` entry in every `GIT` in both games carries **exactly six
fields**:

```
TemplateResRef  XPosition  YPosition  ZPosition  XOrientation  YOrientation
```

100% of 1,619 K1 and 1,700 K2 creature instances. No exceptions, no optional
fields, no partial overrides. **There is no inheritance and no copy-on-write —
an instance is a placement, not a variant.** To vary a creature you author
another blueprint.

**But the override surface is wildly inconsistent across types:**

| type | instance carries beyond position |
|---|---|
| **Creature** | **nothing** |
| Sound | `GeneratedType` |
| Store | `ResRef` *(not `TemplateResRef`)* |
| Placeable | `Bearing`, and in K2 `TweakColor` + `UseTweakColor` |
| Encounter | `Geometry`, `SpawnPointList` |
| Trigger | `Geometry`, `Tag`, `TransitionDestin`, `LinkedTo`, `LinkedToModule`, `LinkedToFlags` |
| Door | `Tag`, `LinkedTo`, `LinkedToModule`, `LinkedToFlags`, `TransitionDestin`, `Bearing`, K2 `TweakColor` |
| **Waypoint** | **`Appearance`, `Tag`, `LocalizedName`, `Description`, `HasMapNote`, `MapNote`, `MapNoteEnabled`** |

So the **richest blueprint gets the poorest instance**, and the poorest
blueprint — an 11-field waypoint — gets the richest. A waypoint instance can
override its own name and description; a creature instance cannot override
anything at all.

Two structural consequences worth carrying into our package design:

**Geometry is the only universal instance property**, and even that varies —
creatures and triggers use `XPosition`/`XOrientation`, placeables and doors use
`X`/`Y`/`Z`/`Bearing`. Two coordinate conventions in the same file.

**Area links live on the instance, not the blueprint** (`LinkedTo`,
`LinkedToModule`, `TransitionDestin` on doors and triggers). That is the right
call — a door blueprint reused in two places must lead to different rooms — and
it is the one place the split is clearly principled.

---

## 5 · Items — data or code?

**Entirely data. No script is involved anywhere in an item's mechanical effect.**

A `UTI.PropertiesList` entry is a chain of integer row indices:

```
UTI.PropertiesList[n]
  PropertyName  ──► itempropdef.2da row          (60 K1 / 70 K2 rows)
                      ├── subtyperesref   NAMES another 2DA (20 K1 / 23 K2 targets)
                      │       └── Subtype     ──► row in that table
                      ├── costtableresref ──► iprp_costtable.2da row (26 / 27)
                      │       └── CostValue   ──► row in the table it names
                      └── param1resref    ──► iprp_paramtable.2da row (12 / 12)
                              └── Param1Value ──► row in the table it names
  ChanceAppear
  UpgradeType   (K2 only, on upgradeable items)
```

Five levels of indirection, all by row index, terminating in 2DA cells. The
subtype targets include `appearance`, `classes`, `feat`, `gender` and the whole
`iprp_*` family — so an item property can be scoped to a class or gated on a
feat purely by table reference.

`BaseItem` → `baseitems.2da` supplies the kind: damage dice, equippable slots
(as the hex bitmask that reappears as the GFF struct type — §1), model, icon.

**Property counts:** 573 of 1,170 K1 items and 350 of 1,198 K2 items have **no
properties at all** — they are pure `baseitems` instances with a name and a
price. The most-used properties are `Damage`, `AttackBonus`, `Enhancement`,
`OnHit`, `Armor`, `DamageRacialGroup`, and in K2 `Ability` and `Skill`.

**Upgrades are data too, and they are K2's addition.** K2 adds `UpgradeLevel` to
UTI and `UpgradeType` to property entries; `upgradetypes.2da` grows 10 → 12 rows
and `upcrystals.2da` 7 → 14. The upgrade system is a property filter plus a
crystal table — no code.

*Defect worth noting:* `itempropdef.2da`'s `costtableresref` and `param1resref`
columns hold **decimal strings**, not ResRefs — they are row indices despite the
name. Only `subtyperesref` holds an actual table name. `FLAWS.md` F27.

---

## 6 · Position-is-identity sweep, continued from batch 2

Batch 2 catalogued five positional families in the rules layer. This layer adds
four more.

| # | where | mechanism |
|---|---|---|
| 1 | **`UTC.SkillList`** | 8 entries, `{Rank}` only. Position is the skill. Batch 2 established it; this batch confirms it on all 4,397 creature blueprints and finds the three 20-entry violations |
| 2 | **`UTC.Equip_ItemList` struct type** | the equipment slot, as a bitmask in the GFF struct-type field |
| 3 | **`UTC.ItemList` struct type** | the inventory sequence number, in the same field |
| 4 | **every 2DA index field on every blueprint** | `Appearance_Type`, `Race`, `Gender`, `FactionID`, `PortraitId`, `SubraceIndex`, `BodyBag`, `PaletteID`, `Phenotype`, `Appearance`, `GenericType`, `TrapType`, `BaseItem` — all bare integers into tables whose rows have no stable id |

On (4), range-checking the indices against their target tables found **two live
overflows in K1**:

```
Appearance_Type   1..546  vs appearance.2da  509 rows   ⚠ 82 occurrences overflow
Race              2..8    vs racialtypes.2da   7 rows   ⚠
SoundSetFile      1..65535                              65535 is a "none" sentinel, not a bug
```

**All 82 appearance overflows are in `.mod` files. Zero in `.rim`, zero in
BIF.** 36 of the 78 distinct resrefs also exist in a `_s.rim` with a valid
value. See §7 — this bears directly on batch 1's F08.

Fixed-length lists found: `UTC.SkillList` (8) and `UTC.TemplateList` (always 0,
in all 4,397 files — a list field that is never non-empty).

---

## 7 · A cross-batch finding: evidence on batch 1's F08

Batch 1 recorded that **34 K1 modules ship both a `.mod` and a `.rim` pair**,
that 21 of the `.mod` files are strict supersets, and that **nothing declares
which loads** — flagged as the batch's most consequential open question.

This batch turned up evidence bearing on it, from a different direction.

**Every one of the 82 blueprints with an out-of-range `Appearance_Type` lives in
a `.mod` file.** None in any `.rim`. None in the BIF layer. And the specific
extra blueprints batch 1 identified in `danm13.mod` — `dp_danjedifc2`,
`dp_danjediftw`, `dp_danjedimb2`, `dp_danjedimtw` — are among them, carrying
appearance ids 541–544 against a 509-row table.

**Reading:** the `.mod` copies were built against a **different, larger
`appearance.2da`** than the one that shipped. They are not a repackaging of the
same content; they are from a different data set.

**What this does and does not establish.** It does *not* prove which file the
engine loads. It does establish that the `.mod` duplicates are **not
equivalent** to the `.rim` pairs and contain references that cannot resolve
against shipped data. If the engine prefers `.mod`, 82 creatures have a dangling
appearance index. If it prefers `.rim`, the `.mod` files are dead weight.

Either way F08 is now sharper: **the two copies disagree in a way that shipped
data cannot reconcile.** Recorded as `FLAWS.md` F25.

---

## 8 · K1 vs K2

Per-type detail is on each record. The pattern across the layer:

**K2 standardised and cleaned.** Field presence goes from K1's long tail of
stragglers to near-uniform 100%. Five fields present on exactly **one** K1 file
each — `BlindSpot`, `Hologram`, `MultiplierSet`, `IgnoreCrePath`,
`WillNotRender` — become 66–89% standard in K2. The three 20-entry `SkillList`
files are gone. The case-variant fields (`FortBonus` vs `fortbonus`, `SubRace`
vs `Subrace`) are gone.

**K2 removed toolset metadata from shipped data.** `KTGameVerIndex`,
`KTInfoDate`, `KTInfoVersion` appear on K1 UTC, UTD, UTI, UTP and UTW files.
Absent from K2 entirely.

**K2 narrowed blueprint scope in favour of the instance.** `LinkedToModule` is
dropped from UTT and UTW blueprints — K2 carries area links only on instances.

**K2 added one system: item upgrades.** `UpgradeLevel` on UTI, `UpgradeType` on
property entries, and K1's `ModelPart1/2/3` replaced by `ModelVariation`.

**K2 added instance-level colour.** `TweakColor` / `UseTweakColor` on placeable
and door instances — the only *new* instance override in either game.

**Counts moved in both directions.** K2 has more items (994 vs 557 in BIF) and
more sound emitters (1,366 vs 840), but far fewer waypoints (400 vs 1,738
distinct) and fewer triggers (312 vs 812).

---

## 9 · Scope — what was and was not checked

**Read and parsed in full:** every blueprint of all nine types in both games,
from the BIF layer and every module archive — 2,656 K1 and 1,741 K2 UTC files,
1,170 K1 and 1,198 K2 UTI, 2,494 K1 and 1,300 K2 UTP, and the rest as tabulated
in §2. Every `GIT` file in both games (117 K1, 82 K2) for the template/instance
comparison. `itempropdef`, `iprp_costtable`, `iprp_paramtable`, `baseitems`,
`upgradetypes`, `upcrystals` in both games.

**Searched, negative:** both KEY indexes and all 644 module archives for any
`UT*` type beyond the nine (none found); the whole repository for
`CHARACTER-RECORD-01` (not present).

**Not checked:**
- Any running process. No claim about which blueprint copy loads, whether the
  engine truncates a 20-entry `SkillList`, or whether UTE's duplicated
  `Appearance`/`CR` or the creature's own value wins.
- GFF-family non-blueprints — `GIT` was read only for its instance lists;
  `ARE`, `IFO`, `DLG`, `JRL`, `FAC` are batches 4 and 5. **The claim that
  `StrRef` and `Struct` field types are unused is scoped to blueprints only.**
- Whether `PitchVariation` / `VolumeVrtn` on UTS are ever non-zero.
- Whether `ChanceAppear` on item properties is ever non-100.
- Save-game blueprint copies — batch 1 noted saves carry UTC records; their
  field sets were not compared against the shipped blueprints here.
- NWN's blueprint layer — batch 7.
