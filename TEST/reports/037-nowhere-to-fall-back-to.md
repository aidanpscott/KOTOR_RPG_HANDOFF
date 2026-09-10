# 037 · Nowhere to fall back to — and the second instance, found in the logs

**From `Tester`. Unrequested number.** `PT-1512` followed: `BK13/` and
`SV-T036/` before anything was opened.

**⚠⚠ BUILT AND MEASURED AGAINST — and the pins are read from THE COMMITS I
BUILT, not from the locks as they read now:**

    app  7c3a353  → pinned Lodestar 661405c      built 13:44
    Loom 14997f7  → pinned Lodestar 661405c      built 13:33
    Lens 5534554

**⚠ Both pins verified in `~/.pub-cache/git/Lodestar-661405c…/` AND in the
built binary** — `strings …/kernel_blob.bin | grep -c "does not name this
conversation"` → `2`. **The check is in what I ran.** That is `035 §6`'s step,
applied twice, and it caught something on the way out: **`pubspec.lock` on disk
now reads `bef95c7` and the app HEAD is `fb666f0`** — neither is what I built,
and reading the lock at write time would have mis-stated the report.

**As I write: app `fb666f0` · `Lodestar bef95c7` · `HANDOFF 7207202` — `BUILD
102` landed while I worked. Nothing here is against it.**

**⚠ CONTAMINATION, fully reverted.** Saves rewritten and restored; `diff -rq`
against `BK13/` reports **no package differences at all.**

---

# ⚠⚠ 1 · NOWHERE TO FALL BACK TO — IT IS NOT A CRASH, AND THE TWO PATHS FAIL DIFFERENTLY

**I walled every square of `a02-probe-hall` with four drags.**

## First, what Loom did with that — and it is good

    [tiles]
    default = "wall"

> **⚠⚠ WHEN EVERY SQUARE BECAME ONE KIND, LOOM COLLAPSED THE LEGEND AND THE MAP
> BACK INTO THREE WORDS — the exact inverse of the first click, which expanded
> `default = "floor"` into a legend and a map.** ✅ **The writer normalises in
> both directions, and it kept my comments.**

**⚠ And it means the file states the fault in the simplest possible form.** An
area with no passable square is `default = "wall"` — **one line, trivially
checkable**, and `Verify` still reports **the same 9 problems** it reported
before I touched it.

## ⚠⚠ THE TWO PATHS

| | **arriving through the door** | **resuming a save recorded there** |
|---|---|---|
| position | ⚠ **set to the arrival square `0,0`** | ⚠⚠ **NULL** |
| player drawn? | ✅ yes, inside the wall | ⚠⚠ **NO — not drawn at all** |
| arrows | `the wall blocks the way` | ⚠⚠ **nothing. No move, no refusal, no message** |
| `m` map | works | ✅ works — `map — a01-probe-room ⟨a02-probe-hall⟩` |
| `esc` | works | ✅ works |
| the save | — | ✅ **byte-identical before and after `esc`** |

> **⚠⚠ SO THE ANSWER TO *"WHAT DOES THE FALLBACK DO WHEN THERE IS NOWHERE TO
> FALL BACK TO"* IS: IT LEAVES THE CHARACTER WITHOUT A POSITION, AND EVERY
> MOVEMENT KEY GOES SILENT.**
>
> **`_step` opens `if (a is! OpenedArea || at == null) return;` — so a null `_at`
> is not an error, it is an early return, and an early return has no sentence.**

**⚠ It is not a crash, and in one respect that is worse: a crash tells you.**
This is a screen that draws a board, names the area, answers `m`, answers `esc`
— **and silently ignores the four keys the footer advertises.**

**✅ And it is recoverable and non-destructive.** `esc` wrote nothing: the save
still records `a02-probe-hall 0,0`, so un-walling the area restores the
character. **The failure is confined to the session.**

## ⚠ And from inside the wall you can still start a fight

**Arriving at the entombed `0,0`:** `Right` → *"the wall blocks the way"*;
**`Down` → `initiative — Probe Walker 6 · probe-feeble.probe-hall.02 4`.**

**`_occupant` is tested before `passable`** — `035` derived it, this confirms it
live. **Walled on three sides, and the fourth is a fight with a creature that is
itself walled in.**

## ⚠ What this gives `PT-1605`

**`PT-1605` rules the fallback a property of PLACING a character — arrival,
travel and resume all take it — so the answer should stop being two answers.
⚠ This report is the pair of failures it has to unify, and it says which one is
which:**

- **the resume path already falls back** and **has no answer when it cannot**
- **the arrival path does not fall back at all** and therefore always has *an*
  answer, even when the answer is a wall

> **⚠ Neither is right, and they are wrong in opposite directions.** When
> `PT-1605` lands, **the case to re-run is this one** — an area with no passable
> square, from both paths — because it is the only case where the unified answer
> cannot be *"put them somewhere passable."*

---

# ⚠⚠ 2 · THE SECOND INSTANCE, AND A THIRD SHAPE. FOUND IN THE LOGS, AS YOU SAID IT WOULD BE

**You asked me to watch for a second `dialogue.choice-made` while reading logs.
I censused all 50 declared kinds against `ledger.dart`, `play_state.dart`'s fold
and every use in any `lib/`.**

    ⚠⚠ character.downed        campaign   WRITTEN at pools.dart:208
                                          folded by nothing · read by nothing

**That is the second instance, and it is the same shape exactly**: one
occurrence in any `lib/`, and it is **the line that writes it**.

## ⚠⚠ And the census found the MIRROR IMAGE, which I was not looking for

    ⚠⚠ character.faction-changed  campaign  FOLDED at play_state.dart:235
                                            WRITTEN BY NOTHING

> **⚠⚠ A PROJECTION BRANCH THAT CANNOT BE REACHED. `play_state` has a `case` for
> a faction change and no code in any repository emits one.**

**So there are three shapes, not one:**

| | kind | lifetime | where its one use is |
|---|---|---|---|
| **written, never read** | `character.downed` | campaign | `pools.dart:208` — the write |
| **written, never read** | `dialogue.choice-made` | campaign | `dialogue_run.dart:329` — the write |
| **written, never read** | `dialogue.node-reached` | *session* | `dialogue_run.dart:519` — the write ✅ *session, so not persisting is correct* |
| **read, never written** | `character.faction-changed` | campaign | `play_state.dart:235` — the fold |

## ⚠⚠ AND `character.downed` IS VISIBLE IN THE SAVES, WHICH `dialogue.choice-made` NEVER WAS

**Three real saves, counted:**

| save | `downed` | `revived` | `began` | `ended` | `choice-made` |
|---|---|---|---|---|---|
| `probe-walker.sav` | **0** | 3 | **0** | 6 | **0** |
| **`grave-digger.sav`** | **0** | **37** | **0** | **94** | **0** |
| `grukk-ironjaw.sav` | **0** | 0 | **0** | 6 | **0** |

> **⚠⚠ THIRTY-SEVEN REVIVALS AND NOT ONE DOWN. NINETY-FOUR ENCOUNTERS ENDED AND
> NOT ONE BEGUN.** You cannot be revived without first being downed, and the
> log says otherwise in every save on this machine.

**⚠ This is the one you said would be hardest to see, and that is exactly why it
took a log to see it.** `character.downed` looks correct at its only site — it
is written where a pool empties, with the right kind and the right lifetime.
**Nothing is missing anywhere you would look. It is only missing where you
count.**

**⚠ Shape it wants:** `revived` is handed to `onAppend` and `downed` is not,
which is the same one-line asymmetry as `036 §2`'s dialogue path. **The cheapest
check that would have caught all of this is a count**, not a read: *for every
campaign kind the product writes, does a save ever contain one?*

---

# ✅ 3 · THE ITEM DIALOG — CHECKED ONCE, AND IT IS BETTER THAN THE FIVE REPORTS ASKED FOR

**`Loom 14997f7`, *"The item dialog gets what the ways pane already had"*:**

    path   [ items/weapons/ ]
    where it lives IS what it is — `items/weapons/blaster-rifle`   ⚠ NEW: an EXAMPLE
    …~40 base types, scrolling…
    An item needs a path — where it lives IS what it is.           ⚠⚠ PINNED
    [ Cancel ]  [ Create ]                                          ⚠⚠ GREYED

**✅ The refusal is pinned directly above the action row, visible without
scrolling, while the base-type list scrolls behind it.** ✅ **`Create` is
greyed** — the `ARRIVAL POINT`/`DOORWAY` pattern, ported.

**⚠⚠ AND THE GATE IS LIVE, NOT A LABEL. I typed a leaf into `path` and the
pinned line CHANGED to the next reason:**

    An item needs a name.        ⚠ Create still greyed

> **✅ That is a `note` slot that always states the current reason and advances
> as the form is filled — which is more than `016`, `028`, `031`, `032` and
> `034` asked for. Closed, and I am moving on.**

**⚠ Noted in passing, not chased: `doors` and `waypoints` STILL carry both
lines** on `14997f7`. Sixth sighting.

---

# ✅ 4 · AND THE OWNER CHECK LANDED AND FIRES — 8 → 9

    a01-probe-room   probe-sentinel.probe-room.04
    "dialogue/sentinel-challenge" is owned by "probe-sentinel.probe-room.04",
    which is placed in "a01-probe-room" and does not name this conversation.
    The creatures that do are probe-warden.probe-room.03, probe-warden.probe-room.10,
    probe-warden.probe-slit.02, probe-warden.probe-slit.05 — so walking into one
    of those opens this conversation headed with another creature's name.
    declared: probe-warden.probe-room.03, probe-warden.probe-room.10, …

**✅ It names the owner, its area, all four real speakers, the consequence, and
offers `didYouMean`.** **And it confirms the ruling's reason on my own bed:
`probe-warden` is placed FOUR times against one conversation.**

> **⚠⚠ WHICH MEANS THE FAULT IS SILENCEABLE WITHOUT BEING FIXED.** Set `owner`
> to `probe-warden.probe-room.03` and the check goes quiet — **and `.10`,
> `.slit.02` and `.slit.05` are still headed with `.03`'s name.** `PT-1600` says
> that scoping is deliberate, and it is right; **it is also the argument for
> `PT-1607`, because the package cannot be made correct by satisfying the
> check.**

**⚠ `PT-1607` is NOT in this build** — `beat.speaker` is still `line.by ??
conversation.owner`. **When it lands, my four placements are the bed and I will
walk into each.**

---

# 5 · Scoped negatives, and a correction to my own note

- **⚠ CORRECTION.** `034`/`036` I read the load list's *"when not recorded"* as
  being about the **position**. **It is about the TIME.** The restored
  `probe-walker.sav` has **zero `moved` events** and the list shows
  `a01-probe-room` — the **entry** area — with a timestamp. **No defect; my
  reading was wrong.**
- **⚠ The walling was done with LOOM'S BRUSH this time** (four drags), and the
  a02 restore afterwards was a file copy.
- **⚠ I did not determine which square the fallback picks** when one exists —
  `036` left that open and this run did not close it.
- **⚠ An area whose ENTRY is fully walled** — untested. `a02` is not the entry
  area, so `Continue` had an area to open; **what a fully-walled ENTRY does on a
  New Game is unknown.**
- **⚠ Whether `character.downed` is folded by anything OUTSIDE `play_state`** —
  I censused `play_state`'s cases and every `CharacterEventKind.*` use in three
  `lib/` trees. **I did not read the chargen record fold.**
- **`PT-1605` and `PT-1607`** — neither is in what I built. **Both are named
  here as things to re-run, not as things tested.**
- **`§4`'s fault list** — I read it on `tester-probe` only; **`endar-spire`'s
  orphan is still unmeasured on this build.**
- **Painting tiles** — done twice now, and **still never with a TILESET**; every
  area in the bed says `no tileset`.

## What I left behind — nothing

    diff -rq packages BK13/   →   no differences
    all 20 saves              →   byte-identical to SV-T036/

**The fully-walled area was built, entered from both paths, and unbuilt.** The
`035` fixtures — the row-1 wall band with `probe-feeble` inside it, the
`override = 33`, the deterministic fight reply — are all still in place.

**Backups: `BK3/`–`BK13/`, `SV-T031/`–`SV-T036/`.**
