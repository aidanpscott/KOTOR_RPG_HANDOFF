# BUILD 71 — `PT-1505`/`PT-1506` and `TEST 017`: declared, not discovered

**742 green** — Lodestar 334 · Lens 5 · Loom 123 · app 280.

---

## ⚠⚠ `PT-1505` — AND `§1` ALREADY REQUIRED IT

The ruling is the owner's and it is recorded in `PACKAGE-FORMAT-01 §4`. **What
the build found is what kind of fix it was**, and it is not "a new rule":

> **`§1`, the format's one sentence:** *"A package is a folder. The manifest
> says what is in it and what it needs. **Nothing is discovered by scanning**."*

`[order].areas` is the only field that says which areas a package has, so
**membership was always the manifest's job.** `validateConnections` reads areas
that way and always has; `Loom` refuses to author past it. **The play client was
not disagreeing with a new rule — it was the one program that never implemented
`§1`.**

`play_screen` was `openArea(_pathOf(id))`: an id turned into a path. It is
`openAreaIn(package, id)` now — **in `Lodestar`, so there is one roster and not
two agreeing and one not.**

⚠ **THE REFUSAL IS ITS OWN PROBLEM, NOT `noSuchFile`.** *"There is no area file
here"* would be a lie about a file that exists and reads perfectly, and **a
wrong reason sends the next person to look in the wrong place.** The test opens
the same file by path to prove the file is not the fault.

### ⚠⚠ AND THE OPEN MOVED AHEAD OF THE THING THAT COSTS THE PLAYER

Walking out of an area **writes the fight outcome** — that is what a player
loses by leaving, `PT-1448` — and it was running **before** anything checked
whether the destination could be reached. **A refused door would have cost a
round and moved nobody.** The open is first now.

⚠ **And a refused travel leaves you where you are.** Tearing down a working room
to display an error is how `F4` happens.

---

## ⚠ `PT-1506` — A NULL TEST, AND THE APP ALREADY OWNED THE SENTENCE

`_canEnterPlay` was `entryArea != null`. It asked whether `[entry]` **names**
something, never whether the something is **there** — so `a09-nowhere` enabled
all three rows and said nothing, while `base-rules`, which is behaving
correctly, greys them **and explains why.**

⚠ **`PT-1380`'s own comment sat two lines below the guard:** *"a disabled row
with no reason is a bug a player cannot distinguish from one."* **The inverse
was there and unguarded: an enabled row that cannot work.**

⚠ **TRI-STATE, BECAUSE REACHING THE ENTRY TOUCHES THE DISK.** Before that answer
arrives the rows must be **neither enabled nor explained** — enabling them
optimistically is the defect itself, and greying them silently is the one
`PT-1380` named.

⚠ **AND THE RIGHT REASON, NOT ONE REASON.** *"names no starting area"* is true
of a rules-only package and false of one whose entry is named and unreachable.
**Saying it of both sends an author to add a line that is already there.**

---

## ⚠⚠ THE THIRD INSTANCE WAS ASKED FOR AND IT WAS `016`'s F3, STILL LIVE

The owner asked for a look while the pattern was in front of me. **The third is
the first: `TEST 016 F3` was never fixed.**

    areas[c.to] == null   →  "which this package does not list"

`areas` holds what **opened**, so `null` meant two different things — *not
listed* and *listed and unreadable* — and **the sentence asserted the first**,
with `didYouMean` printing the area on the very next line. New
`targetAreaUnreadable` member; **a fault rather than a skip**, because the
connection genuinely cannot be checked and silence would make one broken file
look like it had one consequence.

### `017`'s F3 — and the duplicate went with it

The at-rest reason said *"It is authored and has never been placed"*
**unconditionally**, and in `tester-probe` the fault directly above it was that
blueprint's placement. **It is checked now**, and that removed the second defect
Tester noted in the same breath: **the same dead reference was reported once per
path.** At rest is for **what nothing places** — which is what the function's own
docstring always said it was for — and the placement walk is the one that can
name *where*.

    tester-probe   4 faults → 3, and none of them asserts an unchecked clause

⚠ **Placements are gathered from manifest-listed areas only** — `PT-1505`, and
the two rules agreeing rather than each having its own idea of the package.

> **The shape, named: A HELPFUL CLAUSE ASSERTED RATHER THAN CHECKED.** Three
> instances now. Each was added to make a message kinder, and each is the part
> of the message that is false.

---

## ⚠ `F4` — A FAILURE TO ENTER IS A REFUSAL, NOT A SESSION

All three entry failures landed **inside the play screen**: no board, the
message in alert colour, **vitality along the bottom**, and *"arrows to move ·
esc to leave"*. **Tester pressed the arrows. They did nothing and said nothing.**

The refusal screen offers **one key and it is the one that leaves**, and other
keys are **ignored rather than swallowed** — a key that does nothing must not
look like a key that did something. Asserted, so that *does nothing* cannot
quietly become *throws*.

⚠ **`F5` fell out of it**, since the screen had to be written anyway: the
parser's sentence is **kept** and marked *"for the author:"*, below the sentence
a player needs. **Tester asked for exactly that** — the information stays, the
voice around it changes.

---

## ⚠ `PT-1367`'s PREFABS ARE IN `STATE.md` NOW

Not a fix — a tracking entry, and the owner's reason for it is the whole point:
**a ruled feature that is neither built nor tracked is the one that gets
forgotten.** One occurrence of the word in four repos, and it is a note saying
there are none. It is also what `PT-1371`'s single-area decision leaned on.

---

## ⚠⚠ MY CITATIONS COLLIDED TWICE, AND THAT IS THE LESSON

I filed last slice's findings as `PT-1503`/`PT-1504`; the index had spent them.
I renumbered to `PT-1505`/`PT-1506`; **the owner then spent those on `TEST
017`.** They now cite **`PT-1501`**, whose *build* they are — the dead check,
`unlink`, the unrecorded roll and `§9`'s retry are consequences of one ruling,
not rulings.

⚠ **Two records still say `PT-1503` meaning the dead-check rule:** `Lodestar`
commit `0913ce0`'s message, and `TEST 017`, which is Tester's. Recorded, not
rewritten.

**Numbers are the owner's to assign. I stop minting them.**

## Still open

- ⚠ **`PT-1500` — the palette.** Ruled and unstarted.
- ⚠ **`tester-probe/sentinel-challenge`** still needs a **failure node**, which
  is content, and the package is Tester's.
- ⚠ The conversation editor has **no button for `unlink`**.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` is still forked 814 / 1553. The docs mirror is
  otherwise **0 stale** — `PLAYTEST-RULINGS-01` had drifted to 109 lines and was
  copied.
