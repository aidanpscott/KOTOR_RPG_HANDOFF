# STUDY 04 — WORLD LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-4 additions. Merges with batches 1–3.

---

## The three world files

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **IFO** ("module info") | A 43-field manifest naming exactly one area, an arrival point, a clock and fourteen event scripts. Always one area, in all 239 modules. | **module manifest** — and it should be merged into the area (`FLAWS.md` F37) |
| **ARE** | The properties of a place: lighting, weather, grass, minimap transform, rules flags, and the room-name list that is the entire coupling to geometry. | **area properties** |
| **GIT** ("game instance file") | Everything placed in the area, as ten lists. Its meaning flips on one flag. | **placements** |
| **JRL** | Every quest in the game and the text of every stage. One file, game-wide. | **quest catalogue** |

## Module state, which needs three words KOTOR does not have

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| `<mod>.rim` + `_s.rim` | The shipped module. Read-only, never written. | **module (shipped)** |
| `<mod>.mod` in `modules/` | Written by the engine on leaving a module. Installation-scoped, still template-based, `Mod_IsSaveGame=0`. | **module state (installation)** |
| `<mod>.sav` inside a save | One per **visited** module. Full inline records, carries the player. `Mod_IsSaveGame=1`. | **module snapshot (save)** |

KOTOR calls the first and second `.mod`-family files and distinguishes them by
nothing a reader can see. That ambiguity cost this study two batches
(`FLAWS.md` retraction).

## Fields worth renaming

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`UseTemplates`** | A flag that changes what every list below it *means* — reference-plus-placement, or full inline record. Written as `1`; omitted rather than set to `0`. | **placements-are-references** — and it should be a file type, not a flag |
| **`Mod_Area_list`** | A list with exactly one entry in all 239 modules. | **area** (singular) |
| **`Mod_Entry_*`** | Where the player materialises: an area resref plus five floats. | **arrival point** |
| **`Mod_IsSaveGame`** | Whether this module record is a save snapshot. The only field distinguishing the three tiers, and it does not separate tier 1 from tier 2. | **is-snapshot** |
| **`Rooms[].RoomName`** | A string that locates a model *and* a walkmesh. The whole geometry coupling. | **room** — and it is a name, deliberately |
| **`Map`** | Two world points, two image points, a resolution and a north angle: an affine transform. | **minimap transform** |
| **`AreaProperties`** | Audio configuration — ambient day/night, reverb, three music slots. Lives on the *instance* file, not the area. | **area audio** |
| **`TemplateResRef`** (on an instance) | Which blueprint this placement instantiates. | **template** |
| **`LinkedToModule` + `LinkedTo`** | Destination: a module name plus an object tag. Both strings. | **destination module / destination marker** |
| **`TransitionDestin`** | The name shown to the player for that destination. | **destination label** |
| **`Geometry`** | A polygon of vertices defining a trigger's footprint. Spelled `{PointX,PointY,PointZ}` for triggers and `{X,Y,Z}` for encounters. | **footprint** |
| **`Bearing`** | A single facing angle, used by placeables and doors where everything else uses two orientation floats. | **facing** |
| **`MapNote` / `MapNoteEnabled`** | A waypoint's annotation on the minimap. | **map label** |
| **`CameraList`** | Fixed camera positions. The only object type with no blueprint — defined entirely per placement. | **camera placements** |
| **`List`** (unnamed, K1 only) | 49 weapon templates with positions, in two dev-module files, empty everywhere else. | **(unidentified — see `RECORDS.md`)** |

## Quest vocabulary

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`Categories`** (in the JRL) | The quests. "Category" describes the file's shape, not the thing. | **quests** |
| **`EntryList` / entry** | The stages a quest can be in. | **stages** |
| **`Tag`** (on a quest) | The quest's identity, a string, used by script, save and UI alike. | **quest id** |
| **`ID`** (on a stage) | An authored, sparse, non-monotonic label — **not** a sequence number. | **stage label** |
| **`End`** | This stage terminates the quest. Set on several stages in half of all quests. | **is-terminal** |
| **`JNL_State`** | Which stage the quest is currently at. The entire live state of a quest. | **current stage** |
| **`JNL_PlotID`** | The quest's `Tag`, in the save. Two names for one identifier. | **quest id** |
| **`PlotIndex`** | Unresolved — `-1` on many quests, a small integer on others, matching no table found. | **(unidentified)** |
| **`XP_Percentage`** | A fraction of an award granted on reaching this stage. | **xp share** |
| **`Priority`** | 0–4, a display ordering. | **sort rank** |

---

## Terms worth *not* carrying forward

**"Module" as distinct from "area."** They are 1:1 in all 239 cases. One word.

**`.mod` for two different things.** A shipped module and a runtime state file
must not share an extension, a signature and a `Mod_IsSaveGame` value. If our
packages have a runtime-written layer, it gets its own name and its own tag.

**"Category" for a quest.** Name things what they are.

**"ID" for a label.** KOTOR's stage `ID` is sparse and unordered; calling it an
id invites the assumption that it sorts. Ours should say `stage_label` and carry
an explicit order if order matters.

**A flag that changes parsing.** `UseTemplates` makes one file format mean two
things. If our placements can be either references or inline records, that is
two file types with two tags, not one field.
