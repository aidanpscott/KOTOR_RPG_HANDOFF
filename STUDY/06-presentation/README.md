# STUDY 06 — PRESENTATION LAYER

Audio, music, movies, cutscenes and animation reference in KOTOR 1 and KOTOR 2.

| file | what it is |
|---|---|
| `RECORDS.md` | WAV, BIK, CAMERA, ANIMATION REFERENCE + the LIP decode |
| `README.md` | this file — the seven questions |
| `FLAWS.md` | F51–F58 |
| `NAMING.md` | batch-6 vocabulary |

**Scope, as briefed.** Model internals are out — no geometry, materials,
shaders or rigging. In: audio addressing and triggering, music state, cutscene
authoring and firing, animation reference.

**Method.** Every audio directory in both games (36,000+ files), every movie,
all 2,326 DLG files re-read for presentation fields, every `CameraList`, 4,002
LIP files, and the audio/camera/animation script API.

---

## 1 · Audio formats and layout

Full record in `RECORDS.md` → WAV.

**Four locations, split by role:**

| | K1 | K2 |
|---|---|---|
| voice | `streamwaves/` 13,860 files, 596 MB | `streamvoice/` 17,098 files, 610 MB |
| music | `streammusic/` 119, 191 MB | `streammusic/` 160, 148 MB |
| effects | `streamsounds/` 991, 115 MB | `streamsounds/` 830, 133 MB |
| short cues | BIF, 1,928 WAV | BIF, 2,265 WAV |

**Why several, and it is a coherent scheme.** The BIF holds short cues that are
needed instantly and often — UI clicks, footsteps, impacts — indexed by
`chitin.key` alongside everything else. The three stream directories hold long
audio that is played once and discarded, kept out of the archive layer so it can
be streamed from disk rather than resolved through the KEY. The split is
**latency and lifetime**, not format.

**⚠ Most of it is not WAV.** Voice and music are **MP3 behind a 58-byte stub
`RIFF` header** — the declared RIFF chunk size is 0x32 while the file runs to
megabytes. `streamsounds/` skips the pretence entirely and begins with a raw
MPEG frame sync and a `LAME` tag. One extension, two containers, neither of them
WAV.

**Addressing is by bare resref in all four cases.** The directory nesting under
voice is organisation for humans, not a namespace — nothing in the data ever
names a path. K1 nests `module/speaker/`, K2 nests `module/topic/`.

---

## 2 · ⚠ How a sound is triggered

Five mechanisms, and the data/script split differs for each.

| sound | fired by | data or script |
|---|---|---|
| **area ambience** | `GIT.AreaProperties` — `AmbientSndDay`, `AmbientSndNight`, and separate day/night volumes, all row indices into `ambientsound.2da` | **pure data**, on area load |
| **positional sound** | a `UTS` blueprint placed via `GIT.SoundList` | **pure data** — the blueprint carries `Active`, `Continuous`, `Looping`, `Random`, `Interval`, `IntervalVrtn`, `Hours`, `MaxDistance`, `MinDistance`, `Volume`, `Priority` and a `Sounds[]` list |
| **background music** | `GIT.AreaProperties.MusicDay` / `MusicNight`, indices into `ambientmusic.2da` | **data**, overridable by script |
| **combat music** | `GIT.AreaProperties.MusicBattle` | **data**, engine-switched — see §3 |
| **voice line** | `DLG` node `VO_ResRef` | **data**, on node play |
| **one-shot effect** | `PlaySound`, `SoundObjectPlay`, or a 2DA lookup (`guisounds`, `footstepsounds`, `placeableobjsnds`, `inventorysnds`, `grenadesnd`) | **both** |

**UTS is the interesting one, and it connects to batch 3.** A sound emitter is a
blueprint with **25 fields, all always present** — the only blueprint type in the
game with no optional fields — and its behaviour is entirely declarative. It can
loop, fire at random intervals with variance, restrict itself to certain hours,
pick randomly from a list of up to ten sounds, and position itself randomly
within a rectangle. **No script is involved.** 2,171 of 2,173 K1 sound
references resolve; two do not.

That is a genuinely good design and worth naming: **ambience is data all the way
down**, and the only scripted audio is the deliberate one-shot.

**And there is a mixer.** `priorityGroups.2da` (27 rows in both games) carries
`priority`, `volume`, `maxplaying`, `interrupt` and `fadetime` — so sounds are
grouped, capped in simultaneous count, allowed to interrupt each other by
priority, and cross-faded. K2 splits `volume` into `volume_pc` / `volume_xbox`
and drops `maxvolumedist`.

---

## 3 · Music and state

**There is no state machine, and there are exactly three slots.**

An area declares three music tracks in `GIT.AreaProperties`:

```
MusicDay      index into ambientmusic.2da
MusicNight    index into ambientmusic.2da
MusicBattle   index into ambientmusic.2da
MusicDelay    a delay before (re)starting
```

The engine picks day or night from the world clock (`IFO.Mod_DawnHour` /
`Mod_DuskHour`) and swaps to battle when combat begins. **That is the entire
automatic behaviour** — a three-way selection driven by two conditions.

Everything else is explicit script:

```
MusicBackgroundPlay / Stop / ChangeDay / ChangeNight / SetDelay
MusicBackgroundGetDayTrack / GetNightTrack / GetBattleTrack
MusicBattlePlay / Stop / Change
SetMusicVolume
```

So a story beat changes music by a script calling `MusicBackgroundChangeDay` and
then `MusicBackgroundPlay`. There is no cue system, no transition graph, no
layering — **the composer's structure lives in the audio file, not in the
engine.**

**`ambientmusic.2da` carries stingers** — `stinger1`, `stinger2`, `stinger3`
alongside `resource`. So a track can declare up to three short accents. In both
games' shipped tables the stinger columns are largely empty on the rows sampled;
I did not tabulate their fill rate.

**Where music state lives across a save:** nowhere on its own. The area's three
indices are in the GIT, which the save snapshots wholesale (batch 4). Whatever a
script changed is captured because the GIT is captured.

---

## 4 · ⚠ Cutscenes

**The answer to the brief's question is: a cutscene is a conversation with
cameras attached, and KOTOR has no separate cutscene format at all.**

Searched both games for a distinct cutscene resource type: **none exists.**
`IFO.Mod_CutSceneList` is a declared list that is **length 0 in all 239 modules**
(batch 4). Every in-engine cutscene in both games is a `DLG`.

### What makes a conversation cinematic

Five mechanisms, all fields on the DLG:

**`CameraID` on a node** — selects one of the area's placed viewpoints
(`RECORDS.md` → CAMERA). This is the workhorse. Density measures how directed a
scene is:

```
K1  man26_trial     223 nodes carry a CameraID   the Manaan trial
    man26_pcexile   183
    man26_selarb    155
    tat17_04celis   148
K2  101atton         73
    003atton         66
```

**`CameraAngle`** — on every node, a coarse framing choice when no `CameraID` is
given. Plus optional `CamHeightOffset`, `TarHeightOffset`, `CamFieldOfView`,
`CameraAnimation`, `CamVidEffect`.

**`CameraModel`** — a **model file used as an animated camera path**, set on 24
K1 files (22 distinct, e.g. `m12aa_c02_cam`) and 25 K2 files (19 distinct, e.g.
`102percam`). This is the only place the model layer enters the cutscene system,
and it enters as *motion data*, not geometry.

**`StuntList`** — `{Participant, StuntModel}`, substituting a special model for
an actor for the duration. Non-empty on **24 K1 files and 4 K2 files.** This is
how a scene shows something the normal character models cannot do.

**`AnimatedCut`** — a flag, set on **20 K1 files and 4 K2 files.** So the
fully-animated set-piece is rare: under 2% of conversations in either game.

**`ConversationType`** — 0, 1 or 2. K1: 737 / 114 / 139. K2: 958 / 124 / 77.
The values are not decoded; the distribution suggests normal / computer /
cinematic but that is **inference, not established.**

### The unit of authoring is the dialogue node

Everything a cutscene does is attached to a line: which camera, which framing,
which fade, which animations on which actors, which script fires, which quest
advances. **Timing comes from the voice line** — the node plays until its audio
ends, with `Delay` and `WaitFlags` as adjustments.

That is the whole system, and it explains three things at once:

- **why `CameraList` has no blueprint** — a viewpoint has nothing shareable to
  template (`RECORDS.md` → CAMERA);
- **why animation is sparse** — 94–96% of nodes carry none, because most
  conversation is two people standing still;
- **why the script API has `CutsceneAttack` and `CutsceneMove`** — special
  variants that move and fight *without* the normal AI interfering, because the
  actors are ordinary creatures being puppeteered by dialogue.

### What it cannot do

There is no timeline, no track, no keyframe list, and no way to sequence two
things at once except by putting them on the same node. A cutscene's granularity
is **one line of dialogue**, and anything shorter than a line has nowhere to go.

---

## 5 · Movies

Full record in `RECORDS.md` → BIK.

**Prerendered Bink video** (`BIKi`), in `movies/`. K1: 61 files, 607 MB. K2: 67
files, **1,600 MB** — 2.6× the volume for 10% more files.

**Triggered by name, from script:** `PlayMovie`, `QueueMovie`,
`PlayMovieQueue`, `IsMoviePlaying`. Also `IFO.Mod_StartMovie`, so a module can
declare one that plays on entry.

**`movies.2da` is not the playback table.** Its columns — `strrefname`,
`strrefdesc`, `alwaysshow`, `order` — are a title, a description, a visibility
flag and a sort key, and its row count matches neither game's file count (107
rows / 61 files in K1; 61 rows / 67 files in K2). It is the **bonus-feature
gallery listing**. Playback names the file directly.

**How it differs from an in-engine cutscene:**

| | in-engine cutscene | movie |
|---|---|---|
| authored as | a DLG with cameras | rendered externally |
| reflects player state | yes — appearance, party, gear | **no** |
| branches | yes, via gates | no |
| skippable | per `Skippable` / `NodeUnskippable` | engine-level |
| cost | authoring time | 117 MB for one file |
| localisation | StrRef + per-language voice | re-render or subtitle |

The trade is visible in the numbers: K2 shipped 2.6× the video and **one fifth
as many animated cutscenes** (4 files with `AnimatedCut` versus K1's 20).

---

## 6 · Animation

Full record in `RECORDS.md` → ANIMATION REFERENCE. The decode batch 5 deferred:

**`AnimList` on a dialogue node is `[{Animation: int, Participant: string}]`, and
`Animation` is a `dialoganimations.2da` row index plus 10000.**

```
10040 → row 40  "Talk_Forceful"   954 uses, K1's most common
10042 → row 42  "Talk_Sad"        508 uses
10126 → row 126 "Horror"
```

`Participant` is an actor **tag**, with two reserved words — `OWNER` and
`PLAYER`. K1 has 224 distinct participants, K2 147.

**Three numbering schemes coexist.** The 10000-base above is verified. A second
family appears in the same field in the 1000s (1202, 1412, 1415) and is
**inferred** to index `animations.2da` with a +1000 base — not confirmed. And the
script API's 93/111 `ANIMATION_*` constants are all valued 0–999, a third
scheme, so `PlayAnimation` does not take the numbers a dialogue node does.

**Animation is sparse:** absent on 94.4% of K1 nodes and 96.2% of K2 nodes.

**K2 separates body, face and mood.** K1 has one channel (`AnimList`); K2 adds
`FacialAnim` (17 rows) and `Emotion` (35 rows) as their own per-node fields, and
`PlayOverlayAnimation` to the script API. Lip movement is a fourth channel
entirely — the LIP track, driven by the voice resref.

So a K2 line can carry: a body animation per actor, a facial animation, an
emotion, and an independent 16-viseme lip track. **Four channels, four
mechanisms, no shared timeline.**

---

## 7 · K1 vs K2

| area | difference |
|---|---|
| **voice directory** | `streamwaves/` → `streamvoice/`; second level changes from **speaker** to **topic**; K1 has 547 loose root files, K2 none |
| **voice volume** | 13,860 → 17,098 files |
| **movies** | 61 → 67 files, but **607 MB → 1,600 MB** |
| **animated cutscenes** | **20 → 4 files** with `AnimatedCut` |
| **stunt models** | 24 → 4 files with a non-empty `StuntList` |
| **animation tables** | `dialoganimations` 227 → 512, `animations` 394 → 571, `combatanimations` 58 → 107 |
| **animation channels** | K2 adds `FacialAnim` and `Emotion` per node, and `PlayOverlayAnimation` |
| **music/sound tables** | `ambientmusic` 49 → 59, `ambientsound` 48 → 73, `placeableobjsnds` 70 → 88; `soundset` **90 → 66** (the only shrink) |
| **mixer** | `priorityGroups` gains per-platform volume, loses `maxvolumedist` |
| **script API** | 53 → 54 audio/camera/animation functions; the addition is `PlayOverlayAnimation` |

**The pattern:** K2 spent its presentation budget on **prerendered video and
per-line facial performance**, and spent much less on hand-directed in-engine
set-pieces than K1 did.

---

## 8 · Scope — what was and was not checked

**Read in full:** every file in `streamwaves`/`streamvoice`, `streammusic`,
`streamsounds` and `movies` in both games (headers and directory structure);
2,001 LIP files per game, fully decoded; all 2,326 DLG files for `AnimList`,
`CameraID`, `CameraModel`, `StuntList`, `AnimatedCut`, `ConversationType`; every
`CameraList` in both games; ten audio 2DAs; the audio/camera/animation script
API in both games.

**Searched, negative:** both games for a distinct cutscene resource type (none);
`IFO.Mod_CutSceneList` across all 239 modules (empty in every one);
`ANIMATION_*` constants for values matching dialogue animation ids (none — three
separate numbering schemes).

**Not checked:**
- **Model internals** — out of scope by the brief. `CameraModel` and `StuntModel`
  are identified as model references; their contents are not opened.
- **The MP3 stub-header layout** — identified as a container, not parsed.
- **Bink internals** — third-party codec, deliberately untouched.
- **The 1000-base animation mapping** — stated as inference in `RECORDS.md`.
- **The 16 viseme meanings** — the ids are decoded, the phoneme mapping is in the
  model layer.
- **`ConversationType` values** — distribution recorded, meanings not established.
- **Stinger fill rate** in `ambientmusic.2da` — columns identified, not tabulated.
- **Any running process.** Nothing about mixing behaviour, streaming, or how the
  engine chooses between day and battle music is observed — all of it is read
  from data and the script API.
- NWN's presentation layer — batch 7.
