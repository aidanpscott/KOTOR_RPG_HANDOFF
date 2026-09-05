# STUDY 03 — BLUEPRINT LAYER

The reusable object templates of KOTOR 1 and KOTOR 2 — UTC, UTI, UTP, UTD, UTT,
UTM, UTS, UTW, UTE — and the GFF format they are all written in.

| file | what it is |
|---|---|
| `RECORDS.md` | GFF + nine blueprint records |
| `README.md` | this file — GFF answers, template/instance, items, positional sweep, our-system comparison |
| `FLAWS.md` | F24–F33 |
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

## 3 · ⚠ UTC field-by-field, and the comparison against our system

The full field pass is in `RECORDS.md` → UTC. Ten groups: identity, attributes,
vitals, progression, appearance, alignment, behaviour flags, inventory, scripts,
and vestigial.

### The asymmetry the brief asked to map, now mapped across the whole layer

```
ClassList        [{Class, ClassLevel, KnownList0}]      explicit id
  KnownList0     [{Spell, SpellMetaMagic, SpellFlags}]  explicit id
FeatList         [{Feat}]                               explicit id
SpecAbilityList  [{Spell, SpellCasterLevel, ...}]       explicit id
SkillList        [{Rank}] × 8                           ⚠ POSITION ONLY
```

**`SkillList` is the only progression list in the entire blueprint layer with no
identifier.** Confirmed on all 1,741 K2 files and 2,653 of 2,656 K1 files.

The three K1 exceptions are the tell: `c_drdg`, `c_sebulba` and `partymember`
ship **20-entry** skill lists, with real ranks past the eighth slot
(`partymember` has rank 4 at index 18). Nothing validates the length, and
nothing could — there is no id to validate against.

### ⚠ The comparison — with a scope note first

**`CHARACTER-RECORD-01` does not exist in this repository.** Searched the whole
tree by filename and by content; `WHERE-IS.md` shows the design documents live
in `aidanpscott/KOTOR_RPG_Library`, which I cannot open. So this compares
KOTOR's UTC against the specs that **are** visible in `docs/` — `SKILLS-01`,
`CLASS-ROSTER-01`, `FORCE-POOL-01-v3`, `ALIGNMENT-01-v2`, `MULTICLASS-01`,
`EQUIPMENT-01`, `FORMS-01`, `ACTION-ECONOMY-01`. **Treat the "ours" column as
inferred from those documents, not read from a record spec.**

*(One thing to check on your side: `SKILLS-01` §1 is headed "Twenty-two skills",
while the brief for batch 3 says 24. One of the two is stale.)*

**Where KOTOR stores something we appear not to:**

| KOTOR field | what it does | do we have it? |
|---|---|---|
| `PaletteID` | toolset grouping for the object browser | authoring metadata — we would need an equivalent if we ship a builder |
| `Plot`, `Min1HP`, `NoPermDeath` | narrative-protection flags on the record | not visible in the docs; these are cheap and solve real problems |
| `ChallengeRating` (+ `CRAdjust`) | encounter-balance number on the creature | `SCENARIOS-01` may cover it; not confirmed |
| `PerceptionRange`, `BlindSpot`, `IgnoreCrePath` | AI sensing parameters | our system is tabletop-first; likely N/A |
| 14 `Script*` hooks | per-object event bindings | our equivalent is the package layer, not the character |
| `Faction` | one integer into a relationship matrix | not visible; worth having |
| `SoundSetFile`, `PortraitId`, `Appearance_Type` | presentation, by table index | we would carry these as names, not indices |

**Where we store something KOTOR cannot:**

| ours | KOTOR's position |
|---|---|
| **22+ skills** | **impossible** — 8 positional slots, no id, and the array is the record |
| **Aptitude system** | no home. Nothing on UTC is a general per-character keyed store |
| **Force pool with regeneration, fatigue and degradation** (`FORCE-POOL-01`) | `ForcePoints` + `CurrentForce`. Two integers. No rate, no fatigue, no tier state |
| **7-band alignment with hysteresis and drift** (`ALIGNMENT-01-v2`) | `GoodEvil`, one 0–100 byte. No band, no direction, no history |
| **Five action budgets** (`ACTION-ECONOMY-01`) | nothing — the engine's turn state is not on the record at all |
| **Forms as conditions, two groups** (`FORMS-01`) | no condition/stance store. `SpecAbilityList` is the nearest and it is a spell list |
| **37 classes across four lists** (`CLASS-ROSTER-01`) | `ClassList` handles multiclass fine — but see batch 2 F15: each class needs columns in five 2DAs |
| **Species traits and bonuses** (`SKILLS-01` §5–6) | `Race` + `Subrace` + `SubraceIndex`, three fields, two of them redundant, all indices |

**The single most useful conclusion.** KOTOR's UTC is a **wide flat record of
scalars plus five arrays**, and every extensible thing on it is extensible
*because it carries an id*. The one place BioWare used position instead —
skills — is the one place the record cannot grow, and it is exactly the axis our
system needs most (22+ skills, plus an aptitude layer that has no KOTOR analogue
at all).

**The design lesson is narrow and cheap: every list entry carries its own id,
always, even when the list looks fixed.** Eight skills looked fixed in 2003 too.

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
