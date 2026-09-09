# BUILD 73 — `PT-1513` and the header: a cost never spent, a time never recorded

**766 green** — Lodestar 353 · Lens 5 · Loom 127 · app 286.

---

## ⚠ `PT-1513` — the tile names the ground; the creature prices it

    creature   moveCostMultipliers {'difficult ground': 2}
               ignoresMoveCostMultipliers — ONE flag, every source
    tile       moveCostSource — what KIND of hard it is, no number

**The direction is the whole ruling.** A hover droid, a Force power and a boot
each say *"movement costs me nothing extra"* **once**. On the tile, each would
enumerate every terrain kind, and **every kind added later would silently
escape all of them.**

⚠ **`hazard` stays inert**, as ruled. An undecided effect is a different problem
from a cost that was written and never spent: the first waits for a ruling, the
second was a defect.

### ⚠⚠ AND STACKING CANNOT ARISE — `PT-1366` had already answered it

I was about to record *"highest, not product, and it is unruled"*. `PT-1366`
says: *"a text-map cell is one character and therefore **ONE TYPE**, so a swamp
is composed from `water` tiles and `difficult` tiles"* — and adds that **if
tiles were ever meant to combine, the map notation cannot express it.**

**A square names at most one costed source.** The two readings are
indistinguishable by construction, so `max` is written down as the conservative
one for whoever makes tiles combinable.

### ⚠⚠ THE PRICE EXPOSED AN ORDER BUG THAT WAS INVISIBLE AT PARITY

    was:  spend a point → is it passable? → refuse
    now:  is it passable? → can you afford it? → spend

**Walking into a wall cost a point of movement and then refused.** It could not
be seen while every square cost one; it became visible **the moment one and two
stopped being equal.** Asserted from outside: three pushes into a wall leave the
position untouched.

⚠ **And `canAfford` exists because `move` does not answer the question.** `move`
returns what it managed — right for *"how far did I get"*, wrong for *"may I
stand there"*. With one point left, a step onto difficult ground would have been
**half-paid and taken.**

⚠ `STUDY 19`'s finding is recorded beside the rule rather than buried: **neither
source engine modelled this.** `surfacemat`'s `walk` is a boolean and Swamp
prices like Stone. **Our code matched KOTOR exactly and the document was the
outlier** — and the document still wins, because `Loom` offers the type beside
four that do something.

---

## ⚠⚠ THE HEADER — AND YES, IT IS A FORMAT BUMP

**You asked me to answer rather than assume. The answer is `format = 2`, and
the reason is mechanical rather than ceremonial.**

The header is **positional**, and its length is **derived from the fields a
reader knows**:

    n = 4 + 2 + 2 + len(compressor) + 2 + len(rulesVersion)

New fields sit **before the payload**. So a `format = 1` build reading a
`format = 2` save computes that offset **short**, hands header bytes to gzip,
and says:

> **"Damaged save: the contents could not be unpacked."**

**That is a wrong reason for a perfectly good file** — and it is `PT-1366`'s
motivating case word for word: *a package missing `[tiles]` might be written
before the rule existed or might be corrupt, and the loader cannot distinguish
them.* The machinery to say the true thing **already exists**
(`formatFromTheFuture`, *refused rather than read optimistically*) — **and it
only fires if the number moves.**

⚠⚠ **AND MOVING IT IS WHAT KEEPS OLD SAVES READABLE, NOT WHAT BREAKS THEM.** A
`format = 1` save still parses and still yields its log. It carries none of the
new fields, and **absent means *older than the field*** — never a time invented
from the filesystem. `PT-1366`'s own argument for a version number is that **a
change does not orphan old files**, and this is that argument being cashed.

### The field set, and why each one is there

**Every field has a named consumer. None is there for completeness.**

| field | who needed it | what it was doing instead |
|---|---|---|
| `savedAt` | `Load Game` order **and** `Continue` | guessing from file mtime |
| `package` | `listFor` | **decompressing and replaying every log** |
| `character` | the row | showing a filename |
| `className`, `level` | the row | nothing — *"no level, no class"* |
| `area` | the row | nothing — *"no where"* |

⚠⚠ **`package` is the sharpest.** `save_listing.dart`'s own contract is
*"replaying one to answer 'is there a save?' would be the expensive answer to a
cheap question"* — **and filtering by package was doing exactly that, once per
save, to draw a menu.** With `Tester`'s fifteen that is fifteen decompressions
and fifteen replays. And `save_store.dart`'s comment already said the fix:
*"the right fix is a fifth header field and that is the format's call, not this
screen's."* **The format made the call.**

### ⚠ The two surfaces now sort by the same comparator

`Load Game` and `Continue` share `_newestFirst`, so **the first row a player
sees is the one the button takes.** That agreement is the fix, not the ordering
itself.

⚠ **A save with no recorded time sorts LAST, never first.** *Unknown* is not
*oldest*, and it must not be handed to `Continue` ahead of a save that says when
it was written.

⚠ **`savedAt` is supplied to `writeSave`, not read from `DateTime.now()` inside
it.** The engine does not read a clock for the same reason it does not read a
disk — **and a test that cannot pin the time cannot assert on it.**

---

## ⚠⚠ I COLLIDED ON A NUMBER A THIRD TIME

I minted `PT-1514` for the header ruling. **`PT-1514` is your own note about
colliding on a number**, one entry after `PT-1508` ruled that numbers are
yours. The header ruling has no number of its own, so **the code cites
`PT-1416` — the ruling it overturns** — which is accurate and collides with
nothing. `PT-1513` is correct per the index and is untouched.

## ⚠ One flake, declared

`acceptance_test` failed once on *"Endar Spire"* not found, in a full run that
took 2:13; it passed alone and passed on a 1:24 re-run, and the suite is green
twice since. **Recorded rather than chased**, and worth knowing beside
`PT-1511`/`PT-1512`: it looks like contention, not a defect, and I have not
proved that.

## Still open

- ⚠ `PT-1509` — fog: the map is memory, the board is perception. Ruled, unstarted.
- ⚠ `PT-1515` (nothing dies) and `PT-1516` (a flag cannot be set by anyone, and
  Loom offers a gate that reads one) are ruled and not yet built.
- ⚠ `tester-probe/sentinel-challenge` needs a **failure node** — content, and
  Tester's package.
- ⚠ The conversation editor has **no button for `unlink`**.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` forked 814 / 1553 — **left, as ruled.**
