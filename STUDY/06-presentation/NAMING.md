# STUDY 06 — PRESENTATION LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-6 additions. Merges with batches 1–5.

---

## Audio

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`.wav`** | Two different containers: MP3 behind a 58-byte stub RIFF header (voice, music), or bare MP3 (effects). Never actually WAV. | **audio stream** — and the extension should say which |
| **`streamwaves/`** (K1) / **`streamvoice/`** (K2) | Recorded dialogue, nested `module/speaker/` in K1 and `module/topic/` in K2. Path is organisation only; addressing is by bare resref. | **voice** |
| **`streammusic/`** | Music beds. Flat. | **music** |
| **`streamsounds/`** | Long effects. Flat. | **effects** |
| WAV in the BIF | Short cues needed instantly — UI, footsteps, impacts. The split from the stream directories is **latency and lifetime**, not format. | **cues** |
| **`priorityGroups.2da`** | The mixer: 27 groups with priority, volume, simultaneous cap, interrupt rule and fade time. | **mix groups** |
| **`ambientsound.2da`** | The catalogue of area ambience beds. | **ambience catalogue** |
| **`ambientmusic.2da`** | The catalogue of music tracks, each able to declare up to three stingers. | **music catalogue** |
| **`stinger1..3`** | Short accents attached to a track. | **accents** |
| **`MicRange`** (on a camera) | How far the camera hears from. The viewpoint defines the listening position, not just the view. | **listen radius** |
| **`SoundExists`** (on a dialogue node) | A flag asserting the voice file is present. | **has-recording** |

## Cutscene and camera

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **cutscene** | Not a thing. A conversation with camera fields set. No cutscene resource type exists in either game. | **directed conversation** |
| **`CameraList`** | Placed viewpoints in an area, each with an id a dialogue node calls. The only structure using GFF's `Vector` and `Orientation`. | **viewpoints** |
| **`CameraID`** | Which viewpoint this line is shot from. | **shot** |
| **`CameraAngle`** | Coarse framing when no viewpoint is named. | **framing** |
| **`CameraModel`** | A **model used as an animated camera path** — motion data, not geometry. Set on 24 K1 / 25 K2 conversations. | **camera move** |
| **`StuntList` / `StuntModel`** | Substituting a special model for an actor for the duration of a scene. | **stand-in** |
| **`AnimatedCut`** | A flag marking a fully-animated set-piece. 20 K1 files, 4 K2. | **set-piece** |
| **`ConversationType`** | 0/1/2, distribution recorded, meanings not established. | **(unidentified)** |
| **`CutsceneAttack` / `CutsceneMove`** | Movement and attack that bypass the normal AI, because cutscene actors are ordinary creatures being puppeteered. | **staged move / staged attack** |
| **`WaitFlags` / `Delay`** | The only timing controls. Duration otherwise comes from the voice line's length. | **hold / pause** |

## Animation

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`AnimList`** | Per-line body animation: `{Animation, Participant}`. Empty on 94–96% of nodes. | **blocking** |
| **`Animation`** (the int) | A `dialoganimations.2da` row **+ 10000**. A second base in the 1000s appears in the same field. | **motion index** — and the base should be explicit |
| **`Participant`** | An actor **tag**, with reserved words `OWNER` and `PLAYER`. | **actor** |
| **`FacialAnim`** (K2) | Face, by index into a 17-row table. A separate channel from the body. | **expression** |
| **`Emotion`** (K2) | Mood, by index into a 35-row table. A third channel. | **mood** |
| **LIP track** | A 16-viseme timeline: float time plus a shape id 0–15. The only presentation channel with real timing. Located by sharing the voice resref. | **lip track** |
| **`ANIMATION_*` constants** | The script API's own numbering, 0–999 — incompatible with the dialogue field's. | **(a third scheme; see `FLAWS.md` F53)** |

## Movies

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`.bik`** | Prerendered Bink video. Triggered by name from script or by `Mod_StartMovie`. | **movie** |
| **`movies.2da`** | The bonus-feature gallery listing — title, description, visibility, sort order. **Not** the playback index; row count matches neither game's file count. | **movie gallery** |

---

## Terms worth *not* carrying forward

**`.wav` for MP3.** If our packages ship compressed audio, the extension says so.

**"Cutscene" as a mode rather than a format.** KOTOR's cutscenes are
conversations, which is why they can only be timed in whole lines. If we want
staged scenes, the timeline is the format, not a flag on a dialogue node.

**Three numbering schemes for one concept.** A motion should have one id
namespace, and the base should never be inferred from magnitude.

**Audio duration as the unit of timing.** Inheriting pacing from recording
length means re-recording a line restages a scene, and a translator can break
one. Author the timing; let the audio fit it.

**A flat resref namespace for 31,000 voice files.** KOTOR compensates by
encoding module and speaker into the filename — a namespace implemented as a
string convention. Ours should have real scoping.
