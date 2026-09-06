# STUDY 06 — PRESENTATION LAYER — RECORDS

Four records — WAV, BIK, CAMERA, ANIMATION REFERENCE — plus a decode addendum
to batch 5's LIP record.

**Scope, as briefed.** Model internals are out: no geometry, materials, shaders
or rigging. What is in: how audio is addressed and triggered, how music changes,
how a cutscene is authored and fired, and how content names an animation.

Coverage: every audio directory in both games (36,000+ files), every movie, all
2,326 DLG files re-read for presentation fields, every `CameraList` in both
games, 4,002 LIP files, and the audio/camera/animation script API.

---

## WAV — the audio stream

**WHAT IT IS** A recorded sound: a voice line, a music bed, or an effect.

**CONTAINER** Four places, and the split is by role, not by format.

```
K1  streamwaves/   13,860 files   596 MB   81 subdirs, two levels deep
    streammusic/      119 files   191 MB   flat
    streamsounds/     991 files   115 MB   flat
    data/*.bif      1,928 WAV              indexed by chitin.key

K2  streamvoice/   17,098 files   610 MB   72 subdirs, two levels deep
    streammusic/      160 files   148 MB   flat
    streamsounds/     830 files   133 MB   flat
    data/sounds.bif 2,265 WAV              indexed by chitin.key
```

**⚠ Most of these are not WAV.** Read from the bytes:

- **Voice and music** open `RIFF` + a **declared chunk size of 0x32 (50 bytes)**
  followed by `WAVEfmt `. The declared size is far smaller than the file. This is
  an **MP3 payload behind a stub RIFF header** — the header is a fixed 58-byte
  prefix and the audio after it is MPEG.
- **`streamsounds/`** has no RIFF header at all: files begin `FF F3` — a raw MPEG
  frame sync — with a `LAME` encoder tag in the first 16 bytes. **Bare MP3 with a
  `.wav` extension.**

So one extension covers two containers, neither of which is WAV.

**STRUCTURE (directory)** Voice is the only audio organised into
subdirectories, and the two games organise it differently:

```
K1   streamwaves/<module>/<speaker>/<RESREF>.wav
        globe/bast06/NGLOBEBAST06775_.wav
     plus 547 loose files at the root
K2   streamvoice/<module-id>/<topic>/<resref>.wav
        001/journal/001journal001.wav
     no loose files
```

K1 keys the second level on **who is speaking** (`bast06` = Bastila);
K2 keys it on **what the line is for** (`journal`, `target`, `stardoor`).

**REFERENCES OUT** Nothing — audio is a leaf.

**REFERENCED BY**
- Dialogue, **by `VO_ResRef`** — one resref locating the audio *and* the lip
  track (batch 5).
- `UTS.Sounds[].Sound`, **by resref**. Resolution checked: **2,171 of 2,173 K1
  sound emitter references resolve** against the BIF plus the stream
  directories; two do not (`cb_ht_blastleth2`, twice).
- Roughly ten 2DAs, **by resref in a cell** — `ambientmusic`, `ambientsound`,
  `guisounds`, `soundset`, `footstepsounds`, `inventorysnds`,
  `placeableobjsnds`, `grenadesnd`, `defaultacsounds`.
- Scripts, by resref via `PlaySound`, `SoundObjectPlay`, `MusicBackgroundPlay`.

**SCOPE** Game-global. Voice is filed under a module directory but addressed by
bare resref — the path is organisation, not namespace.

**AUTHORED BY** Recorded, then encoded and packed by a tool.

**READ WHEN** Streamed on demand.

**K1 vs K2** K1 `streamwaves` → K2 `streamvoice`, and the second-level key
changes from speaker to topic. K2 has 23% more voice files. K2's
`priorityGroups.2da` splits `volume` into `volume_pc` and `volume_xbox` and drops
`maxvolumedist`.

**SAMPLES**
| # | file | game | why |
|---|---|---|---|
| 1 | `streammusic/01b.wav` | K1 | music — stub RIFF over MP3 |
| 2 | `streamsounds/N_ADMSAULK_ATK1.wav` | K1 | effect — **raw MP3, no RIFF at all** |
| 3 | `streamwaves/globe/bast06/NGLOBEBAST06775_.wav` | K1 | voice — module/speaker nesting |
| 4 | `streamvoice/001/journal/001journal001.wav` | K2 | voice — module/topic nesting |
| 5 | `streamwaves/` 547 root-level files | K1 | oddity — voice outside the subdirectory scheme |

**UNKNOWN** The exact stub-header layout (fields between `RIFF` and the MPEG
payload) — read far enough to identify the container, not to parse it.

---

## BIK — the prerendered movie

**WHAT IT IS** A video file played full-screen, outside the engine.

**CONTAINER** Loose files in `movies/`. K1: **61 files, 607 MB**. K2: **67 files,
1,600 MB.**

**STRUCTURE** Binary, magic **`BIKi`** — RAD Game Tools' Bink. Not parsed
further; it is a third-party codec and out of scope.

Sizes: K1 890 KB (`07_2.bik`) to 42 MB (`01a.bik`). K2 1.75 MB (`legal.bik`) to
**117 MB** (`malmov12.bik`).

**REFERENCES OUT** Nothing.

**REFERENCED BY**
- Scripts, **by name**: `PlayMovie`, `QueueMovie`, `PlayMovieQueue`,
  `IsMoviePlaying`.
- `IFO.Mod_StartMovie` — a module can declare a movie that plays on entry.
- `movies.2da` — but see below.

**⚠ `movies.2da` is not the playback list.** Columns are `strrefname`,
`strrefdesc`, `alwaysshow`, `order` — a title, a description, a visibility flag
and a sort key. It has **107 rows against 61 files in K1** and **61 rows against
67 files in K2**. Neither count matches. Its `alwaysshow`/`order` shape and its
StrRef title identify it as **the movie-gallery / bonus-feature listing**, not
the thing that resolves a playback request. Scripts name the file directly.

**SCOPE** Game-global.

**AUTHORED BY** Rendered externally.

**READ WHEN** On `PlayMovie` or module entry.

**K1 vs K2** Same format, same mechanism. K2 ships 2.6× the video by volume for
10% more files — much longer or higher-bitrate pieces.

**SAMPLES**
| # | file | game | why |
|---|---|---|---|
| 1 | `leclogo.bik` / `biologo.bik` | K1 | publisher logos, the trivial case |
| 2 | `01a.bik` (42 MB) | K1 | the opening set-piece |
| 3 | `malmov12.bik` (117 MB) | K2 | the largest single asset in either game |
| 4 | `obsidianent.bik` | K2 | oddity — a developer logo shipped as a gallery-listed movie |

**UNKNOWN** Bink's internals. Deliberately not opened.

---

## CAMERA — the placed viewpoint

*Batch 4 flagged `CameraList` as the one instance type with no blueprint. This
record explains it.*

**WHAT IT IS** A fixed viewpoint in an area, with an id a conversation can call.

**CONTAINER** `GIT.CameraList`, inside the area's instance file. **K1: 1,137
cameras. K2: 1,209.**

**STRUCTURE** Seven fields, all present on every camera in both games:

```
CameraID      int          the handle a dialogue node calls
Position      Vector       x, y, z
Orientation   Orientation  a quaternion
Pitch         float
Height        float
FieldOfView   float
MicRange      float        audio listening radius from this viewpoint
```

**⚠ This is the only structure in either game that uses GFF's `Vector` and
`Orientation` types.** Batch 3 found both unused by blueprints; batch 4 found
them here. Nine of the ten GIT lists spell position as separate floats
(`XPosition`/`YPosition`/`ZPosition` or `X`/`Y`/`Z`); the camera list uses the
proper composite types the format provides.

**⚠ Why it has no blueprint.** A camera has **nothing to template**. Every field
is either a coordinate or a lens setting — all of them intrinsically per-placement.
A blueprint exists to share authored properties across placements; a viewpoint
has no shareable properties. So the format's one "blueprintless" object is
blueprintless for a principled reason, and it is the counter-example that makes
batch 3's F39 and batch 4's F39 sharper: **the format supports pure-instance
objects perfectly well, and gave that treatment to the one type that needed it
least in authoring terms.**

`MicRange` is the interesting field: the camera defines not just what you see but
**where you hear from**. Present on 1,115 of 1,137 K1 cameras and all 1,209 in K2.

**REFERENCES OUT** Nothing.

**REFERENCED BY** Dialogue nodes, **by `CameraID`** — an integer.
`SetDialogPlaceableCamera` in the script API.

**SCOPE** Area-local. `CameraID` is unique within an area only.

**AUTHORED BY** A human placing viewpoints in the toolset.

**READ WHEN** Area load; selected per dialogue node.

**K1 vs K2** Identical field set. K2 makes `MicRange` universal.

**SAMPLES**
| # | source | why |
|---|---|---|
| 1 | any single-camera area | the trivial case — one static angle |
| 2 | `man26_trial` area | **223 dialogue nodes carry a `CameraID`** — the Manaan trial, the most camera-directed scene in K1 |
| 3 | `101atton` area (K2) | 73 camera-directed nodes — K2's densest |
| 4 | 22 K1 cameras with no `MicRange` | oddity — the field is otherwise universal |

**UNKNOWN** How `Pitch` and `Height` combine with `Orientation` — three
rotation-ish fields with overlapping meaning. Not resolved.

---

## ANIMATION REFERENCE — how content names a motion

*Not a resource type. The mechanism by which dialogue and scripts name an
animation, which batch 5 left undecoded.*

**WHAT IT IS** An integer naming a motion, resolved through a 2DA.

**STRUCTURE** On a dialogue node, `AnimList` is a list of:

```
{ Animation : int , Participant : string }
```

**⚠ `Animation` decodes as `dialoganimations.2da` row index + 10000.** Verified:

```
10040 → row 40  "Talk_Forceful"   954 uses — K1's most common
10042 → row 42  "Talk_Sad"        508 uses
10126 → row 126 "Horror"
10424 → row 424                   K2's most common (K1 has only 227 rows)
```

The two most-used dialogue animations in the game being *talk forcefully* and
*talk sadly* is exactly what a conversation system should show, which is what
makes the mapping safe to assert.

A second numbering appears in the same field — **1202, 1412, 1415, 1428** — in
the 1000s rather than the 10000s. These are **inferred** to index a different
table (`animations.2da`, 394 rows in K1 and 571 in K2, which would accommodate
rows 202 and 412) with a +1000 base. **Not verified** — I did not confirm the
row names.

The script API uses a **third** numbering: 93 `ANIMATION_*` constants in K1 and
111 in K2, all valued 0–999, so `PlayAnimation` does not take the same numbers a
dialogue node does.

`Participant` is a **tag string**, with two reserved values: `OWNER` (the
conversation's owner) and `PLAYER`. K1: 224 distinct participants, `OWNER` 1,378
and `PLAYER` 608. K2: 147 distinct, `OWNER` 623, then named companions —
`Atton` 324, `Kreia` 120.

**Animation is sparse.** `AnimList` is empty on **48,914 of 51,804 K1 nodes
(94.4%)** and **50,918 of 52,946 K2 nodes (96.2%)**. Where present it is usually
one entry; five is the observed maximum.

**REFERENCES OUT** `dialoganimations.2da` **by row index + 10000**; an actor
**by tag**.

**REFERENCED BY** Every dialogue node carries the field.

**SCOPE** `dialoganimations.2da` is game-global (batch 2 F18).

**K1 vs K2** `dialoganimations` grows 227 → 512 rows (31 → 58 named);
`animations` 394 → 571; `combatanimations` 58 → 107. K2 adds
`PlayOverlayAnimation` to the script API, and adds `Emotion` (35 rows) and
`FacialAnim` (17 rows) as separate per-node fields — so K2 splits *body*
animation from *face* and *mood*.

**SAMPLES**
| # | instance | game | why |
|---|---|---|---|
| 1 | `{10040, "OWNER"}` | both | the common case — speaker talks forcefully |
| 2 | `{10042, "PLAYER"}` | K1 | the player character emotes on their own line |
| 3 | a 5-entry `AnimList` | K2 | the maximum — five actors blocked on one line |
| 4 | ids in the 1200/1400 range | both | oddity — a second numbering base in the same field |

**UNKNOWN** The 1000-base mapping, stated above as inference. Also
`dialoganimations`'s unnamed rows — 196 of 227 in K1 and 454 of 512 in K2 have
an empty `name`, so most of the table is padding or reserved.

---

## LIP — decode addendum to batch 5

Batch 5 established the container and left the 5-byte entry undecoded. **It is
decoded.**

```
"LIP V1.0"                       8 bytes
duration          float32        seconds
entryCount        uint32
entries           entryCount x { float32 time , uint8 shape }
```

Verified across **4,002 files (2,001 per game)**:

- **Zero stride mismatches** — `16 + 5n == fileSize` on every file.
- Times are **strictly ascending**, start at 0.0, and the last is ≤ `duration`.
- Shape ids occupy **exactly 0–15 — sixteen distinct values, no more, no fewer,
  in both games.**

So a lip track is a **16-viseme timeline**. Shape 2 dominates in both games
(23,764 K1 / 23,821 K2 occurrences), consistent with a rest or closed-mouth
pose.

**UNKNOWN** Which phoneme each of the sixteen ids represents. That mapping lives
in the model layer, which is out of scope for this batch.
