# STUDY 04 — WORLD LAYER

Modules and areas in KOTOR 1 and KOTOR 2 — IFO, ARE, GIT, JRL, and how they bind.

| file | what it is |
|---|---|
| `RECORDS.md` | four records — IFO, ARE, GIT, JRL — and the F08 resolution |
| `README.md` | this file — the seven questions |
| `FLAWS.md` | F34–F42, opening with a retraction |
| `NAMING.md` | batch-4 vocabulary |

**Method.** Every IFO, ARE and GIT in both games (157 K1 / 82 K2 of each), both
`global.jrl` files, all 21 saved module snapshots, all 40 K1 `.mod` files, and
`PARTYTABLE.res`. Inferences marked; negatives scoped.

---

## 0 · ⚠ F08, settled — and it retracts a premise

Two batches carried F08 open. It is now closed, and not the way either expected.

**The `.mod` files in `modules/` are not shipped content. The running game
writes them.**

| evidence | reading |
|---|---|
| every `.rim` is dated `2026-02-05` (install); all 40 `.mod` are `2026-08-29`–`09-01` | written after installation |
| `.mod` ERF BuildYear is **126**; epoch is 1900, confirmed by `lips/*.mod` at year 103 (2003, release) and `patch.erf` at 104 day 47 (Feb 2004, the 1.03 patch) | written in the last fortnight |
| **K1 played** (4 saves) → 40 `.mod`. **K2 never played** (no save data anywhere) → **0 `.mod`** | presence tracks play, not shipping |
| `modulesave` is a literal in both binaries | the engine names this mechanism |

**They are modules, not saves.** All 40 carry `Mod_IsSaveGame = 0` and
`UseTemplates = 1`. The 21 snapshots inside a save carry `Mod_IsSaveGame = 1`
and no `UseTemplates`.

**What survives:** the 82 out-of-range `Appearance_Type` values batch 3 found are
real, and all are in `.mod` files. They are not a stale BioWare build — they are
creature records **this playthrough** wrote back. Why the engine emitted
appearance indices past the table's end is a new open question, and it is a
better question than the one it replaces.

**What was contaminated:** every earlier count that treated `.mod` as shipped
mixed one player's session into the corpus — `FLAWS.md` F34 lists the affected
figures. All counts in *this* batch are `.rim`-only unless stated.

---

## 1 · MODULE.IFO — what a module declares

Full record in `RECORDS.md`. The answers:

**43 fields, every one present on every module in both games.** No optional
fields at all — the only completely fixed record shape found in the study.
"Required versus optional" has a trivial answer here: everything is required,
and the toolset writes defaults for what the author left alone.

**Entry point:** `Mod_Entry_Area` plus `Mod_Entry_X/Y/Z` and
`Mod_Entry_Dir_X/Y`. Five floats and a resref.

**Area list:** `Mod_Area_list` — **always exactly one entry, in all 239 modules
of both games.** The format supports many areas per module; nothing ships more
than one. So in practice **module and area are 1:1**, and the distinction
between them costs a file and buys nothing.

**Fourteen event scripts**, all module-scoped: load, start, client enter/leave,
heartbeat, player death, dying, level-up, rest, spawn-button, item
acquire/unacquire/activate, user-defined.

**A clock:** start year/month/day/hour, minutes-per-hour, dawn and dusk hours,
and `Mod_XPScale`. Every module declares its own time-of-day and rate.

**Three dead lists:** `Mod_CutSceneList`, `Mod_Expan_List`, `Mod_GVar_List` —
length 0 in all 239.

---

## 2 · AREA.ARE — properties of a place

Full record in `RECORDS.md`. 75 fields; K1 60 always / 15 optional, K2 74 / 1.

**Lighting is doubled.** Seven `Sun*` fields and a complete seven-field `Moon*`
mirror, on every area including interiors that never see either.

**Weather is four probabilities** — rain, snow, lightning, wind power — plus
K2's per-room `DisableWeather`.

**Audio lives on the GIT, not the ARE.** `AreaProperties` — ambient day/night
sounds with separate volumes, `EnvAudio` reverb, day/night/battle music and a
music delay — is a struct inside the *instance* file. The ARE carries only
per-room `EnvAudio` and `AmbientScale`.

**Map data is an affine transform.** The `Map` struct gives two world points and
two map-image points, plus `MapResX`, `MapZoom` and `NorthAxis`. That is the
whole minimap definition: a linear mapping and a rotation.

**⚠ The room list, and the whole geometry coupling — confirmed.**

```
K1   Rooms[] = { RoomName, EnvAudio, AmbientScale }
K2   Rooms[] = { RoomName, EnvAudio, AmbientScale, ForceRating, DisableWeather }
```

**`RoomName` is a string and it is the entire coupling.** I searched all 75 ARE
fields across all 239 areas: nothing else references geometry. The model
(`.mdl`/`.mdx`) and the walkmesh (`.wok`) are separate resources located by that
same name — batch 1 established the name match; this batch confirms the ARE
carries nothing else.

So the answer to the brief's second flagged question is **yes, that is the whole
coupling**, and it is by name.

### What else is coupled by name versus by index

| coupled **by name** | coupled **by index** |
|---|---|
| rooms → model + walkmesh (`RoomName`) | `LoadScreenID` → `loadscreens.2da` |
| area ← module (`Mod_Area_list`, resref) | `CameraStyle` → `camerastyle.2da` |
| every blueprint ← instance (`TemplateResRef`) | `AreaProperties.*` → music and ambient 2DAs |
| scripts (18 hooks across IFO + ARE, resrefs) | waypoint `Appearance` → 2DA row |
| other modules (`LinkedToModule`) | `PlanetID` → a planet table |
| objects (`LinkedTo`, a tag) | creature/placeable/door blueprint internals (batch 3) |
| **quests (`Tag`, `JNL_PlotID`)** | — |

**The world layer is the most name-coupled layer in the game.** Rules (batch 2)
and blueprints (batch 3) are dominated by row indices; here the dominant
mechanism is the resref and the tag. That is why areas can be reused with new
content and rules cannot be scoped.

---

## 3 · ⚠ GIT — the complete instance table

The record carries the full table. Two findings matter most.

**`UseTemplates` is the switch.** Set to 1 in all 239 shipped GITs; **absent
entirely** in all 21 saved ones. With it, an entry is a reference plus a
placement. Without it, an entry is a complete inline record. This is the
mechanism behind the six-versus-112-field split, and it is one flag changing
what the file *means*.

**The override surface, completed:**

```
list              inst K1/K2   fields   may override
Creature List      2234/1700      6     ⚠ NOTHING
SoundList          1493/2846      5     GeneratedType
StoreList            51/  18      6     nothing (and uses ResRef, not TemplateResRef)
Placeable List     4845/3223      7     Bearing (+ TweakColor in K2)
Encounter List       65/  69      6     Geometry, SpawnPointList
CameraList         1652/1209      7     ⚠ everything — no template at all
Door List          1092/ 825     12     Bearing, Tag, LinkedTo*, TransitionDestin
TriggerList        1411/ 804     13     Geometry always; Tag + LinkedTo* on 4%/12%
WaypointList       5715/3494     14     Appearance, Tag, Name, Description, MapNote…
List (unnamed)      100/   0      6     same shape as Creature List
```

**The inversion holds across the whole layer.** A creature — the richest
blueprint at ~70 fields — gets six instance fields and can override nothing. A
waypoint — 11 fields — gets fourteen and can override its own name and
description per placement.

**`CameraList` has no template at all.** A camera is defined entirely on the
instance: `CameraID`, `FieldOfView`, `Height`, `Pitch`, `Position` (a Vector),
`Orientation` (an Orientation), `MicRange`. It is the only purely-instance
object type in the game, and it is the only place `Vector` and `Orientation` are
used — closing batch 3's scoped negative, which said those types were unused
**by blueprints**. They are used here.

---

## 4 · ⚠ Entering and leaving a module

**There are three tiers of module state, and "visited" is a real concept.**

```
1  modules/<m>.rim + <m>_s.rim     SHIPPED. Read-only, pristine, never written.
                                    UseTemplates=1, Mod_IsSaveGame=0

2  modules/<m>.mod                 INSTALLATION state. Written by the engine
                                    when you leave a module. Still template-based
                                    (UseTemplates=1, Mod_IsSaveGame=0), but with
                                    instance lists edited — danm13 gains 4
                                    creatures, danm14ac gains a placeable.

3  <save>/SAVEGAME.sav/<m>.sav     SAVE state. One per VISITED module. Full
                                    inline records, UseTemplates absent,
                                    Mod_IsSaveGame=1, and carries the player
                                    in Mod_PlayerList.
```

**What persists:** everything, at two different scopes. Tier 2 follows the
installation; tier 3 follows the save slot. A module you have visited is
reconstructed from tier 3 on load, never from tier 1.

**What resets:** nothing, once visited. A module you have *not* visited has no
tier-3 entry, so it is created fresh from tier 1 the first time you enter.

**So "loaded" versus "visited" is exactly the tier-3 distinction:** the save
carries a snapshot per visited module, and visiting is what creates one. This is
the other half of the mechanism `LIVE-STATE.md` §1 described from the save side.

**How a transition is expressed.** Doors and triggers carry three fields:
`LinkedToModule` (a module name), `LinkedTo` (a tag within it), and
`LinkedToFlags`. `TransitionDestin` holds the display name. The destination is
therefore **module name + object tag — both strings.**

**And K1 and K2 disagree about which object does it:**

```
K1   Door transitions    114     Trigger transitions   40
K2   Door transitions     39     Trigger transitions   85
```

K1 moves you through doors; K2 moves you through invisible regions. That matches
K2's larger open areas and is a real design shift, not a format change.

`Mod_Entry_Area` plus five floats says where you land. 106 distinct entry areas
across 117 K1 modules and 74 across 82 K2 modules — so a handful of modules
share an entry area name.

---

## 5 · Triggers, waypoints and encounters

**A trigger is a polygon.** `Geometry` is a list of `{PointX, PointY, PointZ}`
vertices, on 100% of trigger instances in both games.

```
vertices   4: 360   5: 347   8: 162   6: 45   9: 25   7: 24   (K1)
           4: 322   8: 272   5: 125   6: 22   9: 19   7: 12   (K2)
```

Mostly quads and pentagons, with a long tail. **Three K1 and seven K2 triggers
have a single vertex** — degenerate, and presumably never fire.

**What fires them:** the blueprint's `ScriptOnEnter` / `ScriptOnExit`, plus
`OnClick`, `OnDisarm`, `OnTrapTriggered`. The trigger blueprint (batch 3, UTT)
carries the trap block and the scripts; the instance carries only the shape and,
in 4%/12% of cases, a transition.

**Encounters use a different vertex spelling.** `Encounter List` geometry is
`{X, Y, Z}` rather than `{PointX, PointY, PointZ}` — the same concept, two field
names, in the same file. Encounters also carry a `SpawnPointList`.

**Waypoints are the most instance-heavy object in the game** — 14 fields,
including `MapNote` and `MapNoteEnabled`, so a waypoint is both a script target
and the map-annotation mechanism. 5,715 in K1, the most numerous instance of any
type.

---

## 6 · ⚠ The journal and quest state

Full record in `RECORDS.md` → JRL. The structure, and what it means for
cross-campaign carry.

**Definition — one game-global file.** `global.jrl`, 101 quests in K1 and 117 in
K2. Reconfirmed: searched both KEY indexes and all 644 module archives; exactly
one JRL per game.

```
quest    { Tag, Name→StrRef, Comment, PlotIndex, PlanetID, Priority 0-4,
           EntryList }
stage    { ID, Text→StrRef, End, XP_Percentage }
```

**State — in the save, keyed by name.**

```
PARTYTABLE.JNL_Entries[] = { JNL_PlotID, JNL_State, JNL_Date, JNL_Time }
                             ↑ the quest Tag   ↑ the stage ID
```

**A quest's entire state is one integer** — which stage it is at — plus when it
got there. There is no per-quest flag set, no sub-objectives, no completion
percentage. Progress is a cursor into an authored list.

**Who writes it:** scripts, via the journal API, naming the quest by tag.
Nothing else writes quest state — searched the save for any other quest-shaped
structure.

**How a module references one:** it does not. **A module has no relationship to
a quest at all.** The link is a script inside the module naming a tag inside a
game-global file. `PlanetID` on the quest is a display grouping, not a binding.

**Four properties that matter for cross-campaign carry:**

**Quests are name-addressed, not index-addressed.** `Tag` is a string, used by
the script, the save and the UI. This is nearly unique in KOTOR — the world
layer aside, almost everything is a row index. **A tag survives renumbering; an
index does not.** Anything we build for carry should follow the tag model.

**Stage IDs are authored, sparse and non-monotonic.** They run 1–150 in K1 and
1–100 in K2 and are not sorted within a quest in either game. Gaps are
deliberate insertion room. So a stage id is a **label**, not an ordinal — you
cannot compare two states to see which is further along.

**A quest can end several ways.** `End` is set on multiple stages in 47 of 101
K1 quests and 63 of 117 K2 quests, up to nine on one K2 quest. So "finished" is
not one state, and a carry mechanism asking "did they complete X?" gets a
yes/no that hides which ending happened. The *stage id* is the answer worth
carrying, not the boolean.

**The text is a StrRef into the game-global TLK.** So a quest's prose is coupled
to the same single string namespace batch 2 flagged (F23). A quest cannot travel
without its strings, and its strings cannot travel without their indices.

---

## 7 · K1 vs K2

| record | difference |
|---|---|
| **IFO** | **none.** 43 fields, identical names, no additions or removals. Only volume differs — 157 modules vs 82. |
| **ARE** | K2 promotes the twelve `Dirty*` decal fields, `Grass_Emissive` and `DisableTransit` from rare-optional to universal (60/15 → 74/1). K2's `Rooms` entry gains `ForceRating` and `DisableWeather`. Nothing removed. |
| **GIT** | Field sets identical. K2 makes `TweakColor`/`UseTweakColor` universal on placeables and doors (1–2% of instances in K1). K2's unnamed `List` is empty in all 82 files. |
| **JRL** | Same structure. K2: 117 quests vs 101, `XP_Percentage` used on 205 of 634 entries vs 93 of 598, more multi-ending quests, and **quest titles contain display tokens** (`Heal <FullName>`). |
| **transitions** | The clearest shift: K1 is door-led (114 door / 40 trigger), K2 is trigger-led (39 door / 85 trigger). |
| **instance mix** | K2 has far more sound emitters (2,846 vs 1,493) and far fewer waypoints (3,494 vs 5,715) and triggers (804 vs 1,411). |

---

## 8 · Scope — what was and was not checked

**Read in full:** all 157 K1 and 82 K2 IFO, ARE and GIT files from `.rim`
containers; all 40 K1 `.mod` files and their world records; all 21 saved module
snapshots; both `global.jrl` files with strings resolved through the TLK;
`PARTYTABLE.res`; ERF build dates on every `.mod` and every `lips/*.mod` and
`patch.erf`; filesystem timestamps across `modules/`.

**Searched, negative:** both KEY indexes and all 644 module archives for a
second JRL (exactly one each); all 75 ARE fields across 239 areas for any
geometry reference beyond `RoomName` (none); the save for any quest structure
beyond `JNL_Entries` (none); both games' 2DA lists for a table matching
`PlotIndex` (none found).

**Not checked:**
- **Any running process.** The three-tier module-state model is read from file
  contents, timestamps and the K2 control — the *write* path is inferred, not
  observed. Whether tier 2 or tier 3 wins on load is **not established**.
- **Why the engine wrote out-of-range `Appearance_Type` values** into `.mod`
  files. New question, replacing the old one.
- **`LinkedToFlags` semantics.** Values 0, 1 and 2 appear; what they select was
  not determined.
- **`PlotIndex`** on quests — no matching table found.
- **`Mod_Hak`**, `ModSpotCheck`, `ModListenCheck` — present, NWN-inherited, not
  tested.
- **The `.wok` walkmesh internals.** Batch 1 established the format and name
  match; the geometry itself is batch 6.
- **`CameraStyle` and `LoadScreenID` target tables** — indices confirmed, the
  tables not read.
- NWN's world layer — batch 7.
