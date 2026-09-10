# 036 · The door is not defended and the save is — the soft-lock, constructed

**From `Tester`. Unrequested number.** `PT-1512` followed: packages to `BK12/`,
saves to `SV-T035/`, before anything was opened.

**⚠⚠ BUILT AND MEASURED AGAINST — and I applied my own new step to this line:**

    app 919b55d · Lodestar fc32da0 (from the PUB CACHE) · Lens 5534554

**The binary is the 12:54:56 bundle**, built when `KOTOR-RPG-APP` was clean at
`919b55d`. **⚠ `Lodestar` is written as the pub-cache ref the binary compiled,
NOT the local checkout** — the local `Lodestar/` is now `661405c`, three commits
past it, and **that difference is exactly what `035 §6` caught me on.**

**⚠ I did not rebuild.** The app is 3 dirty, Loom 4 dirty, `MAIN_WORK` 1 dirty as
I write — Coder is mid-flight on `PT-1600`/`PT-1601`. **Nothing here is against
any of that.**

**⚠ CONTAMINATION.** `probe-walker.sav` rewritten; restored from `SV-T035/`. **All
20 saves byte-identical, and `diff -rq` against `BK12/` reports NO package
differences** — the trap was painted, used, and unpainted, and its reproduction
is documented in `a02-probe-hall.toml`'s own comment.

**⚠ AND THE STEP IS NOW IN MY NOTES**, as you asked — *read the copy the binary
was built from*. Three artifacts, not two: local `git HEAD`, `pubspec.lock`'s
`resolved-ref`, and `~/.pub-cache/git/Lodestar-<sha>/`. **The cheapest check on a
compiled artifact skips all three:** `strings …/kernel_blob.bin | grep -c "<a
literal from the new code>"`.

---

# ⚠⚠ 1 · THE SOFT-LOCK IS BUILT, AND IT SURVIVES A SAVE AND A RESUME

**`026` called *"an area you can enter and cannot leave"* a hazard in a
stranger's package and could not construct one. It takes ONE DRAG.**

`a02-probe-hall` is 4×4. Its arrival `from-probe-room` is at `0,0` and its only
connection `door.probe-hall.01` is at `1,0`. **Painting a wall over both, and a
wall band across row 1, leaves this:**

    ##..        ⚠ the arrival AND the only exit
    ####        ⚠ a band that cuts the area in half — and probe-feeble is INSIDE it
    ..#~
    ..:!

**Walked in from `a01` through `door.probe-room.05`:**

    Probe Hall — arrived at from-probe-room     ⚠ standing IN the wall at 0,0
    press Right, toward the door:
    the wall blocks the way

**Then I quit, and the save recorded the wall square — twice:**

    character.moved   Probe Walker   a02-probe-hall   0,0
    character.moved   Probe Walker   a02-probe-hall   0,0

## ⚠⚠ AND THEN `Continue` DID SOMETHING THE DOOR DOES NOT: IT REFUSED TO PUT ME THERE

    resumed at   a02-probe-hall · 3, 0        ⚠ NOT the 0,0 the save records

**It fell back to `2,0` — the first passable square — exactly as `PT-1526`
promises:** *"a resumed square that is now a wall FALLS BACK rather than
refusing, because `PT-1367` makes repainting one gesture and a save must not
become unopenable because a wall moved."*

> **⚠⚠ SO THE TWO PATHS DISAGREE, AND THE RULING IS ON THE WRONG ONE.**
>
> | reaching a walled square | what happens |
> |---|---|
> | **resuming a save** | ✅ **falls back to the nearest passable square** — `PT-1526` |
> | **arriving through a door** | ⚠⚠ **deposits you inside the wall, silently** |
>
> **`PT-1526`'s own reason transfers word for word: *a save must not become
> unopenable because a wall moved* — and neither must a DOOR.** The defended
> path is the one an author cannot reach by painting; the undefended one is the
> one they reach with a brush.

## ⚠ And the prison survives the fallback

**From `2,0`, every direction:**

    Left  → the wall blocks the way        Down → the wall blocks the way
    Up    → out of bounds, silent          Right → a02-probe-hall · 3, 0

> **⚠⚠ THE REACHABLE SET IS TWO SQUARES OF A SIXTEEN-SQUARE AREA, WITH NO
> CONNECTION IN IT. The fallback saved the SAVE and not the PLAYER.**

**⚠ And the fallback is silent about having moved you.** The door path prints
`Probe Hall — arrived at from-probe-room`; the resume path prints `Probe Hall`
and nothing about having relocated you two squares. **That is defensible —
there is no honest sentence about a wall that moved between sessions — but it
is worth knowing that the one defence in this area never says it fired.**

## ⚠⚠ AND THIS IS THE MISSING CATEGORY, NAMED

**`Verify` reported the same 8 problems throughout — before the paint, after
the paint, on a fresh `Verify again`.** The thirteen `PackageProblem` members in
this build:

    blueprintMissing · blueprintUnreadable · equipmentMissing · referenceMissing
    areaFileMissing · areaUnreadable · targetAreaUnknown · targetAreaUnreadable
    landingPointUndeclared · duplicateArrivalName · entryUndeclared
    entryAreaUnknown · requiredFieldMissing

> **⚠⚠ EVERY ONE ASKS WHETHER A NAME RESOLVES. NONE ASKS WHETHER A POSITION IS
> USABLE.** `landingPointUndeclared` checks a door's landing is **declared** and
> not that it is **standable** — the same field, one step short.

**⚠ Shape it wants:** one rule covers all three faults — *a square that a
placement, an arrival or a connection names must be passable.* **The engine
already has both halves**: `openArea` knows the tile and the validator knows the
position. **And `PT-1526` shows the project has already decided what to do when
they conflict — fall back rather than refuse — so the door needs no new ruling,
only the same one.**

---

# ⚠⚠ 2 · THE CONVERSATION LOG GAP IS A MISSING RECORD, NOT A BROKEN PROJECTION

**You asked what `PLAY-STATE-01` folds when every fight ends and none begins.
⚠ Nothing is broken, and the reason is worse than a bug.**

## The projection is intact, measured on screen

**`probe-walker.sav` carries `encounter.ended` for two creatures and ZERO
`encounter.began`. Loaded:**

    probe-sentinel.probe-room.04: 3 of 33 — in your campaign,
                                  a01-probe-room left you at 3
    Probe Walker: 1 of 11 — in your campaign,
                  a03-probe-yard left you at 0 · revived at 1

**Both match the log exactly.** ✅ **The world remembers.**

**⚠ And the sentence names its own source: *"left you at"*.** The projection is
phrased from the **ending**, which is the only half it has.

## Because nothing ever asked about beginnings

    play_state.dart folds exactly five kinds:
        died · encounterEnded · factionChanged · moved · revived

    ⚠ encounterBegan  — NOT folded. One consumer in the whole product:
      dialogue_run.dart:165  events.any((e) => e.kind == encounterBegan)
      …and it reads the IN-MEMORY BEAT, never the log.

    ⚠⚠ dialogueChoiceMade — NOT folded, and outside the ledger constant it has
      exactly ONE occurrence in any lib/: THE LINE THAT WRITES IT.

> **⚠⚠ SO `dialogue.choice-made` IS WRITTEN, DECLARED `campaign`, FOLDED BY
> NOTHING, PERSISTED BY NOTHING, AND READ BY NOTHING. It is emitted on every
> reply a player has ever picked and thrown away twice over.**

**⚠ I must narrow `035 §2`.** I wrote that *"a gate reading 'have I already
asked this' has nothing to read after a reload."* **That is true as a capability
statement and I should have said what I now can: nothing reads it today, so
nothing is currently broken.** The defect is that the **only** record a
conversation happened is discarded — `§5` forbids an author naming that event,
so there is no second channel to fall back on.

**⚠ And the two losses are not the same size.** `encounter.began` is a signal
consumed inside one frame and would cost nothing if it were never persisted —
**its `campaign` lifetime is the part that is wrong.** `dialogue.choice-made` is
a record with no other source, and **its lifetime is right and its plumbing is
missing.**

---

# ⚠ 3 · AND THE ITEM DIALOG'S COUNTER-EXAMPLE, STATED AS THE ARGUMENT

**Five reports of a defect is weaker than one pane three inches away doing it
right, so this is the version worth carrying:**

| | `NEW ITEM` | `ARRIVAL POINT` · `DOORWAY` |
|---|---|---|
| **body** | ~40 base types **and** a `description` field | one field · two short lists |
| **the vocabulary** | `path` is **free text** | ⚠ **a closed list, computed per area** |
| **a dependent field** | — | ⚠ *"pick an area first"* — **explains its own emptiness** |
| **the refusal** | red sentence **30 scroll-steps below** the button | ⚠ **a greyed `Place`, at the button** |

> **⚠⚠ THE SAME PROGRAM, THE SAME SESSION, MINUTES APART. The fix is not a
> design question — it is a pattern already implemented, twice, in the pane
> beside it.**

---

# 4 · Scoped negatives

- **⚠ The trap was HAND-EDITED this time**, not painted. `035 §4` proved Loom
  paints it; here the map content is what the app reads, and re-driving the
  brush would have measured the same bytes. **Said plainly rather than implied.**
- **⚠ The fallback square** — I observed `2,0` and did **not** determine the
  rule that chose it (first passable in reading order, nearest to the saved
  square, or the area's own default). **Three readings fit one observation.**
- **⚠ Whether the fallback fires for a walled square that is NOT the arrival** —
  untested; my saved square and the arrival were the same square.
- **⚠ An area with NO passable square at all** — not built. What the fallback
  does when there is nowhere to fall back to is unknown, and it is the case that
  turns a soft-lock into a crash.
- **`§2` is a save read plus a source census**, plus the two on-screen values. I
  did not instrument the fold.
- **`encounter.began` from a fight started by WALKING IN** rather than from a
  conversation — still untested; both paths lose it here for the same reason.
- **The item dialog and doors/waypoints** — **not re-opened this run.** `§3` is
  the argument, not a fresh measurement; last measured `0dd361b`, `034 §4`.
- **Loom** — not opened at all this run.

## What I left behind — nothing

    diff -rq packages BK12/   →   no differences
    all 20 saves              →   byte-identical to SV-T035/

**The trap is not left in place**, because `a02` is the package's only round
trip and `034 §3` needs it. **Its reproduction is one line of the file's own
comment:** paint `0,0` and `1,0`. **The wall band on row 1, with `probe-feeble`
standing inside it, is still there from `035` and is still invisible to
`Verify`.**

**Backups: `BK3/`–`BK12/`, `SV-T031/`–`SV-T035/`.**
