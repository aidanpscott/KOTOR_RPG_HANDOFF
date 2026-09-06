# STUDY 06 — PRESENTATION LAYER — FLAWS

F51–F58, continuing batches 1–5. Each cites the record it follows from.
Batch-scoped; intended to merge into a study-wide catalogue.

---

### F51 · One extension, two containers, neither of them the extension
**Follows from:** `RECORDS.md` → WAV

Every audio file in both games ends `.wav`. Read from the bytes:

- **voice and music** begin `RIFF`, declare a chunk size of **0x32 — fifty
  bytes** — against files running to megabytes, then `WAVEfmt `. The payload
  after that stub is MPEG.
- **`streamsounds/`** has no RIFF at all: `FF F3`, a raw MPEG frame sync, with a
  `LAME` tag in the first sixteen bytes.

So the extension is wrong for both, and the two are wrong in *different ways* —
one lies with a header, one does not bother. Any tool walking the audio tree has
to sniff bytes, and a naive WAV reader trusting the declared chunk size reads
fifty bytes and stops.

*This is the fourth format in the study whose declared metadata contradicts its
contents — after batch 1's F07 archive headers, batch 2's F21 TLK flags and
batch 4's `Mod_IsSaveGame`.*

---

### F52 · There is no cutscene format
**Follows from:** `README.md` §4

Searched both games: **no distinct cutscene resource type exists.**
`IFO.Mod_CutSceneList` is declared on every module and is **length 0 in all
239** (batch 4). Every in-engine cutscene in both games is a conversation with
camera fields set.

Consequences that fall out of the choice:

**The unit of time is one line of dialogue.** There is no timeline and no track.
Anything shorter than a line — a beat, an overlap, a reaction landing mid-
sentence — has nowhere to be expressed. Two things happen simultaneously only by
being attached to the same node.

**Direction is scattered across the node.** A single moment's staging lives in
`CameraID`, `CameraAngle`, `CamHeightOffset`, `TarHeightOffset`,
`CamFieldOfView`, `CameraAnimation`, `CamVidEffect`, `FadeType`, `FadeColor`,
`FadeDelay`, `FadeLength`, `AnimList`, `Delay` and `WaitFlags` — fourteen fields
on a record whose primary job is to hold a line of text.

**And the engine needs special verbs to compensate.** `CutsceneAttack` and
`CutsceneMove` exist because the actors are ordinary creatures whose AI would
otherwise interfere with being puppeteered.

*Recorded as a flaw rather than an economy because the cost is visible in the
content: 223 dialogue nodes carry a `CameraID` in `man26_trial`, which is a
timeline written one line at a time.*

---

### F53 · Three animation numbering schemes in one game
**Follows from:** `RECORDS.md` → ANIMATION REFERENCE; `README.md` §6

The same concept — "play this motion" — is numbered three incompatible ways:

```
dialogue AnimList     dialoganimations.2da row + 10000   verified
same field, 1000s     inferred: animations.2da + 1000    NOT verified
script API            93/111 ANIMATION_* constants, all 0-999
```

So a dialogue node and a `PlayAnimation` call cannot share a number, and one
field carries two bases. Nothing in the data declares which base applies — a
reader must infer it from magnitude.

Compounding it: **196 of `dialoganimations`' 227 K1 rows and 454 of its 512 K2
rows have an empty `name`.** Most of the table an author indexes into is
unlabelled, so the number is the only handle and there is no way to check it
means what you think.

---

### F54 · Four animation channels, no shared timeline
**Follows from:** `README.md` §6

A K2 dialogue line can drive four independent things:

```
AnimList     body animation, per actor, by 2DA index
FacialAnim   face, by index into a 17-row table
Emotion      mood, by index into a 35-row table
the LIP file  16-viseme lip track, located by the voice resref
```

Four mechanisms, four numbering schemes, four resolution paths, and **no
structure relating them**. Nothing says the emotion and the facial animation
should agree, nothing synchronises the body animation to the lip track, and the
lip track is not even referenced from the node — it is found by sharing a name
with the audio.

The lip track is the only one with real timing information (float timestamps at
millisecond resolution). The other three are fire-and-forget indices.

---

### F55 · Presentation timing is inherited from audio length
**Follows from:** `README.md` §4

A dialogue node plays until its voice line finishes. `Delay` and `WaitFlags`
adjust; nothing else sets duration.

So **a line with no recorded voice has no natural length**, and a scene's pacing
is a property of the audio files rather than of the authored content. Re-recording
a line changes the timing of everything staged on it. A translator producing a
longer or shorter reading changes the cutscene.

`GetStrRefSoundDuration` exists in the script API, which is the tell: content has
to *ask the engine how long a sound is* in order to time anything against it.

---

### F56 · `movies.2da` describes movies it cannot resolve
**Follows from:** `RECORDS.md` → BIK

`movies.2da` has 107 rows against 61 files in K1, and 61 rows against 67 files in
K2. **Neither count matches, in either direction** — K1 lists 46 movies that do
not exist, K2 ships 6 that are not listed.

The table is the bonus-feature gallery, not the playback index; playback names
the file directly from script. But nothing in the data says that, and the name
`movies.2da` invites exactly the wrong reading. A tool cross-referencing the
table against the directory finds mismatches in both directions and no
explanation.

Same family as batch 3's F27 (column names that lie) and batch 4's `.mod`
ambiguity: **the name is the only documentation, and it is misleading.**

---

### F57 · Audio is addressed by bare resref across a flat global namespace
**Follows from:** `RECORDS.md` → WAV

Voice is filed under `<module>/<speaker>/` in K1 and `<module>/<topic>/` in K2 —
but **nothing in the data ever names a path**. Every reference is a bare resref,
resolved across all four audio locations plus the BIF.

So the directory structure is organisation for humans and buys nothing at
runtime: 31,000 voice files across the two games share one flat name space, and
two modules cannot both have a line called `greeting01`.

The naming conventions compensate by hand — `NGLOBEBAST06775_`,
`001journal001` — encoding module, speaker and index into the resref itself.
That is a namespace implemented in a string, which is where batch 2's F23 (one
global TLK) and batch 4's flat resref space already left us.

---

### F58 · The mixer is data; everything above it is not
**Follows from:** `README.md` §2, §3

`priorityGroups.2da` is genuinely good: 27 groups with `priority`, `volume`,
`maxplaying`, `interrupt` and `fadetime`, so simultaneous sounds are capped,
ranked and cross-faded declaratively.

**Music above it has none of that.** An area declares exactly three tracks —
day, night, battle — and the engine's whole automatic behaviour is picking
between them on two conditions. There is no transition graph, no layering, no
cue system, and no way to express "when this happens, move to that" except a
script calling `MusicBackgroundChangeDay` followed by `MusicBackgroundPlay`.

So the composer's structure has to live inside the audio file, and any musical
state a campaign wants is a global variable in the 819-bit budget batch 5 F46
catalogued.

*The contrast is what makes it worth recording: the engine has a declarative
priority system for footsteps and none for the score.*
