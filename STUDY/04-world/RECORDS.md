# STUDY 04 — WORLD LAYER — RECORDS

Four records — IFO, ARE, GIT, JRL — on the template from `STUDY/README.md`.

Read with the GFF reader from batch 3. Coverage: **every IFO, ARE and GIT in
both games** (157 K1 / 82 K2 of each), both `global.jrl` files, all 21 saved
module snapshots, and all 40 K1 `.mod` files. Inferences are marked.

**Sits on:** batch 1 (containers, F08), batch 2 (2DA references, the game-wide
journal), batch 3 (blueprints, the six-field creature instance) and
`LIVE-STATE.md` (saved module snapshots).

---

## ⚠ Read this first — F08 is settled, and it retracts a premise

Batch 1 F08 recorded that *"34 K1 modules ship both a `.mod` and a `.rim` pair
with no declared winner"*, and batch 3 F25 built on it, concluding the `.mod`
copies *"were built against a larger `appearance.2da` than shipped."*

**The premise was wrong. The `.mod` files in `modules/` do not ship. The running
game writes them.**

Four independent lines of evidence:

| evidence | reading |
|---|---|
| **Filesystem times.** Every `.rim` is `2026-02-05 20:51` (install). All 40 `.mod` files are `2026-08-29` to `2026-09-01`. | written after installation |
| **ERF build dates.** `.mod` files carry BuildYear **126**, days 241–244. The epoch is 1900 — confirmed by `lips/*.mod` at year **103** (2003, matching release) and `patch.erf` at year **104** day 47 (Feb 2004, matching the 1.03 patch). Year 126 is **2026**. | written in the last fortnight |
| **⚠ The control.** K1 has been played on this install (4 saves) and has **40 `.mod`**. K2 has **never been played** (no save data anywhere) and has **0 `.mod`** — only `.rim` and `_dlg.erf`. | `.mod` presence tracks play, not shipping |
| **The `modulesave` literal** is in both binaries (batch 1). | the engine has a name for this |

**And they are modules, not saves.** All 40 carry `Mod_IsSaveGame = 0` and
`UseTemplates = 1`; the 21 module snapshots inside a save carry
`Mod_IsSaveGame = 1` and no `UseTemplates` at all. So KOTOR keeps **three tiers
of module state** — see the GIT record and `README.md` §4.

**What survives from F25:** the observation is real — 82 creature blueprints do
carry `Appearance_Type` past the end of `appearance.2da`, and all are in `.mod`
files. The explanation changes: these are not a stale BioWare build, they are
**creature records the running game wrote back** during this playthrough. Why the
engine wrote out-of-range appearance values is a new and open question.

**What this means for the study:** every earlier count that treated `.mod` files
as shipped content mixed one player's session artifacts into the corpus. The
affected numbers are flagged in `FLAWS.md` F34.

---

## IFO — the module manifest

**WHAT IT IS**
The file that says what a module is: which area it contains, where you arrive,
and which scripts fire on module-level events.

**CONTAINER** `modules/<name>.rim` (always resref `module`), and inside each
saved module snapshot.

**STRUCTURE** GFF, tag `IFO `, V3.2. **43 fields, and every one is present on
every file in both games** — 157 K1 and 82 K2, no optional fields at all. The
only blueprint-family record in the study with a completely fixed shape.

*Identity:* `Mod_Tag`, `Mod_Name` (LocString), `Mod_Description`, `Mod_ID`,
`Mod_Creator_ID`, `Mod_Version`, `Mod_VO_ID`, `Expansion_Pack`, `Mod_Hak`.

*Contents:* `Mod_Area_list` — a list of area resrefs. **Always exactly one
entry, in all 239 modules of both games.** The format supports many; nothing
ships more.

*Entry point:* `Mod_Entry_Area`, `Mod_Entry_X/Y/Z`, `Mod_Entry_Dir_X/Y`.

*Clock:* `Mod_StartYear`, `Mod_StartMonth`, `Mod_StartDay`, `Mod_StartHour`,
`Mod_MinPerHour`, `Mod_DawnHour`, `Mod_DuskHour`, `Mod_XPScale`.

*Fourteen event scripts:* `Mod_OnModLoad`, `Mod_OnModStart`,
`Mod_OnClientEntr`, `Mod_OnClientLeav`, `Mod_OnHeartbeat`, `Mod_OnPlrDeath`,
`Mod_OnPlrDying`, `Mod_OnPlrLvlUp`, `Mod_OnPlrRest`, `Mod_OnSpawnBtnDn`,
`Mod_OnAcquirItem`, `Mod_OnUnAqreItem`, `Mod_OnActvtItem`, `Mod_OnUsrDefined`.

*State flags:* `Mod_IsSaveGame`, `Mod_StartMovie`.

*Dead:* `Mod_CutSceneList`, `Mod_Expan_List`, `Mod_GVar_List` — **all three are
length 0 in all 239 modules of both games.**

**In a save snapshot the IFO grows.** It gains `Mod_PlayerList` (the player —
see `LIVE-STATE.md` §1), `Creature List`, `EventQueue`, `Mod_Effect_NxtId`,
`Mod_NextObjId0/1`, `Mod_NextCharId0/1` — 57 fields rather than 43.

**REFERENCES OUT** Area **by resref** (`Mod_Area_list`, `Mod_Entry_Area`);
scripts **by resref** ×14; a movie by resref.

**REFERENCED BY** The engine, by module name. Nothing in the data references an
IFO — searched every 2DA and every world file in both games.

**SCOPE** Module-local.

**AUTHORED BY** The toolset. `Mod_Creator_ID` and `Mod_Version` are its
fingerprints.

**READ WHEN** Module load.

**K1 vs K2** **Field set identical — 43 fields, same names, no additions or
removals.** The only difference is volume: 157 modules vs 82.

**SAMPLES**
| # | file | why |
|---|---|---|
| 1 | `danm13.rim` / `module.ifo` | plain — Dantooine, one area, all 14 scripts bound |
| 2 | `262tel.rim` / `module.ifo` | K2 equivalent, same 43 fields |
| 3 | `tar_m02aa.sav` / `Module.IFO` | the save form — 57 fields, carries the player |
| 4 | any module | oddity — three declared lists that are empty in all 239 files |

**UNKNOWN** What `Mod_Hak` would do — it is NWN's hakpak field and is present on
every KOTOR module. Not tested; there is no hak mechanism visible elsewhere.

---

## ARE — the area

**WHAT IT IS**
The properties of a place: what it looks like, how it is lit, what the map shows,
and which rooms it is made of.

**CONTAINER** `modules/<name>.rim`, and each saved module snapshot.

**STRUCTURE** GFF, tag `ARE `, V3.2. **75 distinct fields.** K1: 60 always
present, 15 optional. K2: **74 always present**, 1 optional.

*Lighting and sky:* `SunAmbientColor`, `SunDiffuseColor`, `SunFogColor`,
`SunFogOn`, `SunFogNear`, `SunFogFar`, `SunShadows`, and a complete `Moon*`
mirror of all seven, plus `DynAmbientColor`, `LightingScheme`, `ShadowOpacity`,
`IsNight`, `DayNightCycle`, `AlphaTest`, `DefaultEnvMap`.

*Weather:* `ChanceRain`, `ChanceSnow`, `ChanceLightning`, `WindPower`.

*Grass:* nine fields — `Grass_TexName`, `Grass_Density`, `Grass_QuadSize`,
`Grass_Ambient`, `Grass_Diffuse`, `Grass_Emissive`, and four corner
probabilities `Grass_Prob_LL/LR/UL/UR`.

*Map:* the `Map` struct — `MapPt1X/Y`, `MapPt2X/Y`, `WorldPt1X/Y`,
`WorldPt2X/Y`, `MapResX`, `MapZoom`, `NorthAxis`. **Two point-pairs defining an
affine transform from world coordinates to map-image coordinates**, plus a north
rotation. Identical field set in both games.

*Rules flags:* `NoRest`, `Unescapable`, `PlayerOnly`, `PlayerVsPlayer`,
`NoHangBack`, `DisableTransit`, `ModSpotCheck`, `ModListenCheck`,
`StealthXPEnabled`, `StealthXPLoss`, `StealthXPMax`.

*Scripts:* four — `OnEnter`, `OnExit`, `OnHeartbeat`, `OnUserDefined`.

*Decals:* twelve `Dirty*` fields in three groups of four (`ARGB`, `Size`,
`Formula`, `Func`) — optional in K1 (1%), universal in K2.

*Dead:* `Expansion_List` — length 0 in all 239 areas of both games.

**⚠ The room list, and the whole of the geometry coupling.**

```
Rooms : LIST
   K1 entry   { RoomName, EnvAudio, AmbientScale }
   K2 entry   { RoomName, EnvAudio, AmbientScale, ForceRating, DisableWeather }
```

**`RoomName` is a string, and it is the entire coupling to geometry.** The area
names its rooms; the model (`.mdl`/`.mdx`) and the walkmesh (`.wok`) are
separate resources found by that same name. Nothing about geometry, layout or
walkability appears in the ARE.

Confirmed: batch 1 established the WOK/MDL name match; this batch confirms
`RoomName` is the only geometry-bearing field in the whole record — searched all
75 fields across all 239 areas.

Room counts run 1–8+ per area.

**REFERENCES OUT** Rooms **by name**; scripts **by resref**; `Grass_TexName` by
name; `LoadScreenID` and `CameraStyle` **by 2DA row index**;
`Name` **by StrRef**.

**REFERENCED BY** `IFO.Mod_Area_list` **by resref**.

**SCOPE** Module-local.

**AUTHORED BY** The toolset.

**READ WHEN** Area load.

**K1 vs K2** K2 promotes the twelve `Dirty*` decal fields and `Grass_Emissive`
and `DisableTransit` from rare optional to universal. K2's `Rooms` entry gains
`ForceRating` and `DisableWeather`. `MiniGame` is optional in both (3% K1, 7%
K2). No field is removed.

**SAMPLES**
| # | file | why |
|---|---|---|
| 1 | `danm13.rim` / `danm13.are` | plain outdoor area with grass and sun/moon set |
| 2 | `262tel.rim` / `262tel.are` | large — 22 rooms |
| 3 | any K1 area with `MiniGame` | oddity — a swoop/turret area, 3% of K1 |
| 4 | any area | oddity — a full `Moon*` lighting mirror on interior areas that never see a moon |

**UNKNOWN** Whether `ModSpotCheck` / `ModListenCheck` are live. They are NWN
perception modifiers and KOTOR's perception is a list, not a check
(`LIVE-STATE.md` §2). Not tested.

---

## GIT — the instance file

*The most important record in this batch.*

**WHAT IT IS** Everything placed in an area, and where.

**CONTAINER** `modules/<name>.rim`, `modules/<name>.mod` (runtime-written), and
each saved module snapshot.

**STRUCTURE** GFF, tag `GIT `, V3.2. **Only 12 top-level fields**, all present
on all 239 shipped files:

```
AreaProperties   struct — audio configuration
UseTemplates     ⚠ the switch, see below
Creature List · Placeable List · Door List · TriggerList · WaypointList
SoundList · StoreList · Encounter List · CameraList · List
```

`AreaProperties`: `AmbientSndDay`, `AmbientSndNight`, `AmbientSndDayVol`,
`AmbientSndNitVol`, `EnvAudio`, `MusicDay`, `MusicNight`, `MusicBattle`,
`MusicDelay` — all 2DA row indices. Identical in both games.

### ⚠ `UseTemplates` — the switch that explains the six-versus-112 field split

```
K1 shipped GITs (157)   UseTemplates = 1
K2 shipped GITs  (82)   UseTemplates = 1
K1 saved GITs    (21)   field ABSENT
```

With `UseTemplates = 1`, an instance entry is a **reference plus placement**.
Without the field, an entry is a **complete inline record** — the 112-field
creature `LIVE-STATE.md` §1 found. One flag, two entirely different file
meanings.

### ⚠ The complete instance table — every list, both games

Field sets are identical across K1 and K2 except where noted.

| list | instances K1 / K2 | fields | what an instance may override |
|---|---|---|---|
| **Creature List** | 2,234 / 1,700 | **6** | **nothing** — `TemplateResRef` + `XPosition` `YPosition` `ZPosition` `XOrientation` `YOrientation` |
| **SoundList** | 1,493 / 2,846 | 5 | `GeneratedType` only, + `XPosition/Y/Z` |
| **StoreList** | 51 / 18 | 6 | nothing — but uses **`ResRef`**, not `TemplateResRef` |
| **Placeable List** | 4,845 / 3,223 | 7 | `Bearing`; **K2 adds `TweakColor` + `UseTweakColor`** (1% of K1 instances, 100% of K2) |
| **Encounter List** | 65 / 69 | 6 | `Geometry`, `SpawnPointList` |
| **CameraList** | 1,652 / 1,209 | 7 | `CameraID`, `FieldOfView`, `Height`, `Pitch`, `Position`, `Orientation`, `MicRange` — no template at all |
| **Door List** | 1,092 / 825 | 12 | `Bearing`, `Tag`, `LinkedTo`, `LinkedToModule`, `LinkedToFlags`, `TransitionDestin`, + K2 tweak colour |
| **TriggerList** | 1,411 / 804 | 13 | `Geometry` always; `Tag`, `TransitionDestin`, `LinkedTo*` on **4% of K1 / 12% of K2** |
| **WaypointList** | 5,715 / 3,494 | **14** | `Appearance`, `Tag`, `LocalizedName`, `Description`, `HasMapNote`, `MapNote`, `MapNoteEnabled`, `LinkedTo` |
| **List** (unnamed) | 100 / 0 | 6 | same shape as Creature List |

**The inversion batch 3 found holds across the whole layer.** Creatures — the
70-field blueprint — get six instance fields and can override nothing.
Waypoints — the 11-field blueprint — get fourteen and can override their own
name, description and map note per placement.

**`CameraList` is the exception to everything:** it has no `TemplateResRef` at
all. A camera is defined entirely on the instance, with no blueprint type behind
it. It is the only purely-instance object in the world layer.

**Two coordinate conventions, in the same file.** Creatures, triggers,
waypoints, sounds, stores and encounters use `XPosition`/`YPosition`/`ZPosition`
with `XOrientation`/`YOrientation`; placeables and doors use `X`/`Y`/`Z` with a
single `Bearing` float. Cameras use a `Position` **Vector** and an `Orientation`
**Orientation** — the two GFF types batch 3 found unused by blueprints. That
scoped negative is now closed: **GIT uses `Vector`, `Orientation` and `Struct`;
blueprints do not.**

**REFERENCES OUT** Blueprints **by resref** (nine of the ten lists); other
modules **by module name** (`LinkedToModule`); objects **by tag**
(`LinkedTo`); 2DA rows **by index** (`AreaProperties`, waypoint `Appearance`).

**REFERENCED BY** Nothing — the GIT is a leaf. Found by name alongside its ARE.

**SCOPE** Module-local.

**AUTHORED BY** The toolset for the shipped form; **the engine for the
runtime-written and saved forms.**

**READ WHEN** Area load; rewritten on module exit and on save.

**K1 vs K2** Field sets identical. K2 promotes placeable/door `TweakColor` to
universal; K2's `List` is empty in all 82 files; K2 shifts transitions from
doors toward triggers (see `README.md` §4).

**SAMPLES**
| # | file | why |
|---|---|---|
| 1 | `262tel.rim` / `262tel.git` | large — 68,508 b, 22 rooms' worth of instances |
| 2 | `danm13.rim` / `danm13.git` | plain — the shipped form, `UseTemplates = 1` |
| 3 | `danm13.mod` / `danm13.git` | **oddity** — the runtime-written form: 26 creatures where the `.rim` has 22 |
| 4 | `tar_m02aa.sav` / `m02aa.GIT` | the saved form — `UseTemplates` absent, 112-field creature records |
| 5 | `liv_m99aa` / `m50aa.git` | **oddity** — the unnamed `List` with 49 entries, all weapon resrefs (`g_w_sonicrfl03`), in a dev/test module |

**UNKNOWN** What the unnamed `List` is for. It has the Creature List shape but
holds weapon templates, appears in exactly two K1 files (both `liv_m99aa`), and
is empty everywhere else including all of K2.

---

## JRL — the journal

**WHAT IT IS** Every quest in the game, and the text of every stage each quest
can be in.

**CONTAINER** BIF. **One file per game, named `global`.** Confirmed in batch 1
and reconfirmed here: searched both KEY indexes and all 644 module archives —
**exactly one JRL resource exists in each game.**

**STRUCTURE** GFF, tag `JRL `, V3.2. One top-level field, `Categories`.

```
Categories : LIST            a quest
   Tag             string    ⚠ the key scripts use
   Name            StrRef    the quest title
   Comment         string    author notes, shipped
   PlotIndex       int       -1 when unused
   PlanetID        int       -1 = not planet-bound
   Priority        int       0-4
   EntryList : LIST          the quest's stages
       ID             int    ⚠ the state number
       Text           StrRef the stage description
       End            bool   this stage ends the quest
       XP_Percentage  float  fraction of an XP award granted here
```

K1: **101 quests**, 598 entries. K2: **117 quests**, 634 entries.

**Entry IDs are authored, not sequential.** They run 1–150 in K1 and 1–100 in
K2, and are **not monotonic within a quest** in either game. The ID is a label
the author chose, and gaps are deliberate — they leave room to insert stages.

**A quest can end in more than one way.** `End` is set on multiple entries in
**47 of 101 K1 quests and 63 of 117 K2 quests**. Up to 9 terminal stages on one
K2 quest.

**`XP_Percentage` is a K2 idea in practice.** Both games have the field; K1 uses
a non-zero value on 93 of 598 entries, K2 on 205 of 634 — and K2's values are
finer-grained (0.05, 0.1, 0.25, 0.5, 1.0).

**⚠ State lives elsewhere, and the link is by name.** The JRL is definition
only. Live state is in `PARTYTABLE.res`:

```
JNL_Entries : LIST
   JNL_PlotID   string   ⚠ the quest's Tag — a NAME, not an index
   JNL_State    int      the entry ID the quest is currently at
   JNL_Date     int      game day when it reached this state
   JNL_Time     int      game time when it reached this state
```

Twenty-one active entries in the save read. Example: `{PlotID: 'tar_diabounty',
State: 99, Date: 0, Time: 200676}`.

**So a quest is referenced by tag string throughout** — the script sets it, the
save stores it, the UI resolves it. This is one of very few things in KOTOR
addressed by name rather than by row index, and the only one in the world layer.

**REFERENCES OUT** TLK **by StrRef** (`Name`, `Text`); a planet **by 2DA row
index** (`PlanetID`).

**REFERENCED BY** Scripts **by `Tag` string**; `PARTYTABLE.JNL_Entries` by the
same tag; the journal UI.

**SCOPE** **Game-global.** One file, one namespace, for every quest in the game.

**AUTHORED BY** A human. The `Comment` field carries author notes into the
shipped product.

**READ WHEN** Journal open, and whenever a script updates a quest.

**K1 vs K2** Same structure, same field names. K2 has 16 more quests, uses
`XP_Percentage` twice as often, more multi-ending quests, and **K2 quest names
contain display tokens** — `(Prologue) Heal <FullName>: Bonus Mission` — so the
title is templated at display time.

**SAMPLES**
| # | quest | game | why |
|---|---|---|---|
| 1 | `tat18ac_dragonhunt` "A Desert Hunt" | K1 | plain — 7 entries, one ending, Priority 1, PlanetID 4 |
| 2 | `k_starforge` "A Quest for the Star Forge" | K1 | the spine — Priority 0, PlanetID -1, many entries |
| 3 | `kor25_doubtsith` "A Doubting Sith" | K1 | oddity — two entries (20 and 25) both flagged `End`, differing only in outcome |
| 4 | `tutorial_heal_pc` | K2 | oddity — quest title contains `<FullName>`, resolved at display |
| 5 | `tutorial_garage` | K2 | XP_Percentage in use: 0.0 → 0.05 → 0.10 across three stages |

**UNKNOWN** What `PlotIndex` selects — it is -1 on many quests and a small
integer on others, and does not correspond to any 2DA I found. Searched both
games' table lists for a plot-shaped table; none found.
