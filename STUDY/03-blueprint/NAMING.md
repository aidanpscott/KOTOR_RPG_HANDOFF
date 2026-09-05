# STUDY 03 — BLUEPRINT LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-3 additions. Merges with `01-container/` and `02-definition/NAMING.md`.
This is the batch the brief expected to produce most of the vocabulary, so it is
organised by what we would actually need words for.

---

## The format

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **GFF** | A tree of named, typed fields. "Generic File Format" names the genericness, not the job. | **object record** |
| **Struct** | A set of fields. Carries a `Type` id that is usually a schema tag and sometimes payload. | **record** |
| **List** | An array of records. The only nesting mechanism blueprints use. | **record array** |
| **struct type id** | Two different things: a schema tag in most lists, the equipment slot or inventory position in two others. | **schema tag** — and the payload uses should be separate fields (`FLAWS.md` F24) |
| **`CExoString`** | A length-prefixed string. | **text** |
| **`CExoLocString`** | A string index plus optional inline translations. Carries the string reference that the unused `StrRef` type was for. | **localised text** |
| **`ResRef`** | A ≤16-char resource name. The one reference mechanism that is by name rather than position. | **resource name** |

## The blueprint types

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **UTC** | Everything about a creature independent of where it stands. The richest record in the game. | **creature template** |
| **UTI** | An item: kind, price, and a chain of table indices describing its effects. | **item template** |
| **UTP** | A container, terminal, workbench or interactive prop. The largest field set — 62. | **prop template** |
| **UTD** | A door. UTP's field set minus inventory, plus open/close state. | **door template** |
| **UTT** | An invisible region that fires scripts. Its *shape* lives on the instance. | **region template** |
| **UTS** | A sound emitter with playback rules. Module-only. | **sound emitter template** |
| **UTM** | A store's buy/sell rules and stock. Module-only, 10 fields, and the one type that spells its own name field differently. | **vendor template** |
| **UTW** | A named point in space. No scripts. The most numerous blueprint in K1 (2,836). | **marker template** |
| **UTE** | A spawn rule: what appears, how many, how often. | **spawn rule** |
| **`TemplateResRef`** | The blueprint's own name — the key an instance uses to find it. | **template name** |
| **`Tag`** | A second name, used by scripts to find the object at runtime. Not unique-checked. | **script handle** |

## Fields worth renaming

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`SkillList`** | Eight ranks with no ids. Not a list — a fixed array whose index is the skill. | **skill rank array** — and it should not exist in this shape (`FLAWS.md` F26) |
| **`FeatList`** | A real list: each entry carries a feat id. | **feat ids** |
| **`ClassList`** | Class levels, each carrying its own known-powers list. | **class levels** |
| **`KnownList0`** | Force powers known, per class entry. The trailing `0` implies a `KnownList1` that does not exist. | **powers known** |
| **`SpecAbilityList`** | Innate abilities, stored as spell ids with a caster level. | **innate abilities** |
| **`Equip_ItemList`** | Equipped items, slot carried in the struct type. | **equipped items** |
| **`ItemList`** | Carried inventory, sequence carried in the struct type. | **inventory** |
| **`Appearance_Type`** | A row index into the creature body catalogue. Not a "type" in any sense the word usually carries. | **body index** |
| **`GoodEvil`** | A 0–100 byte. One axis, no band, no direction, no history. | **alignment value** |
| **`LawfulChaotic`** | An NWN axis KOTOR does not use, carried on 100% of blueprints. | **(nothing — inherited dead field)** |
| **`PaletteID`** | Which folder the object browser filed this under. Authoring metadata on a runtime record. | **editor category** |
| **`Comment`** | Author notes, shipped to players on every blueprint in both games. | **author note** |
| **`Plot`** | "Cannot be destroyed or removed because the story needs it." | **story-protected** |
| **`Min1HP`** | "Can be reduced to 1 hit point but not killed." | **cannot be killed** |
| **`Repos_PosX` / `Repos_Posy`** | Inventory grid coordinates. Ships in two spellings. | **inventory slot x / y** |
| **`ChallengeRating`** | Encounter-difficulty number, duplicated onto every spawn rule that references the creature. | **threat rating** |
| **`Conversation`** | The dialogue file this object opens. | **dialogue** |
| **`Script*` (14 fields)** | Event bindings, one field per event. | **on-attacked**, **on-death**, **on-spawn**, … |
| **`ScriptEndDialogu`** | `ScriptEndDialogue`, truncated to fit GFF's 16-byte label. | — the truncation is the finding |

## Instance-layer terms

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **instance** (a `GIT` list entry) | A placement. For creatures, a template name plus five floats and nothing else. | **placement** |
| **`XPosition`/`XOrientation`** vs **`X`/`Bearing`** | Two coordinate conventions for the same job, in the same file. | pick one: **position** + **facing** |
| **`LinkedTo` / `LinkedToModule` / `TransitionDestin`** | Where a door or trigger leads. Correctly on the instance, not the blueprint. | **destination** |
| **`TweakColor` / `UseTweakColor`** | K2's per-placement colour override. The only *new* instance override in either game. | **colour override** |

---

## Terms worth *not* carrying forward

**"Blueprint" versus "instance" as KOTOR uses them.** The words imply
inheritance, and there is none — a creature instance overrides nothing
(`FLAWS.md` F28). **Template** and **placement** describe what actually happens.

**"List" for `SkillList`.** It is an array with positional meaning. Calling it a
list invites the assumption that entries are self-identifying, which is exactly
the assumption that breaks.

**The `UT*` prefix family.** Nine two-to-three-letter codes that share a prefix
and nothing else — UTC has 70 fields and UTM has 10, UTS and UTM cannot appear
outside a module and the rest can. The shared prefix implies a uniformity the
types do not have.

**"Type" for anything that is a row index.** `Appearance_Type`, `TrapType`,
`GenericType`, `BaseItem`, `TrapType` — all are positions in tables. Our format
should say **index** when it means index and reserve **type** for actual
discriminated unions.

**Location-as-scope.** KOTOR decides whether a blueprint is global or
module-local by which file it sits in, with nothing on the record declaring it
(`FLAWS.md` F33). Any template we write should carry its own scope.
