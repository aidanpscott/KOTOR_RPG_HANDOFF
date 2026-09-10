# TEST 046 — the header never moves while you play, and the clock is right

**Built against:** the **same two binaries as TEST 043, 044 and 045.** App bundle
`kernel_blob.bin` built **16:11**, from `660134a` → Lodestar `9aa7382`
(`grep -c "PT-1626"` → **0**). Loom bundle built **16:39**, from `908a412`.
**Neither rebuilt.** `47789fa` / `776e42e` / Lodestar `e1a837c` remain untested by me.

**Instrument:** PID-scoped. App `543379`, Loom `544799`, window `142606339`. Both
killed by PID; Coder's `517963`/`517968` survived.

---

## 1. `savedAt` is right, and my own restore proved it by accident

`PT-1518` puts the clock in the app, not the engine — `main.dart:183`,
`savedAt: DateTime.now().toUtc()`, with the note *"which save is most recent is a fact
about the PLAY SESSION, so the moment the player saved is what is recorded, **never
the file's mtime**."*

⚠ **That claim had a natural experiment sitting in my scratchpad and I did not notice
until I went looking.** Restoring `SV-T042` over the shelf gave all twenty files an
identical mtime of **18:44:09**. If the header time were the file's time, every row
would read the same age. Decoded out of the five version-2 headers:

| save | header `savedAt` | file mtime | original mtime |
|---|---|---|---|
| `blade-tester` | 2026-09-09 **23:21:24** | 18:44:09 | Sep 9 23:21 |
| `grukk-ironjaw` | 2026-09-10 **08:42:04** | 18:44:09 | Sep 10 08:42 |
| `vekk-nal` | 2026-09-10 **09:09:35** | 18:44:09 | Sep 10 09:09 |
| `yard-tester` | 2026-09-10 **10:48:27** | 18:44:09 | Sep 10 10:48 |
| `grave-digger` | 2026-09-10 **11:12:17** | 18:44:09 | Sep 10 11:12 |

**Five for five, to the minute, against the mtimes I recorded before I destroyed
them.** The header carries the play moment and it survives a copy.

And the rendering agrees. Read off the Load Game list at **18:41**:

    Barrier Tester   level 1 soldier · a05-probe-barrier · 14…     savedAt 18:27  → 14 min ✓
    Grave Digger     level 1 soldier · a03-probe-yard    · 7 ho…   savedAt 11:12  →  7.5h ✓
    Yard Tester      level 1 soldier · a04-probe-slit    · 7 hou…  savedAt 10:48  →  7.9h ✓
    Grukk Ironjaw    level 1 duelist · a03-probe-yard    · 9 ho…   savedAt 08:42  → 10.0h ✓
    Blade Tester     level 1 duelist · a04-probe-slit    · 19 ho…  savedAt 23:21  → 19.3h ✓
    probe-walker.sav when not recorded

⚠ **But look at the right-hand edge. Every age is truncated mid-word** — `7 ho…`,
`19 ho…`, and `14…` loses the unit entirely. The field a player uses to tell one save
from another is clipped on **every row that has one**, and on the shortest value the
number survives while the unit does not: `14…` could be minutes, hours or days. The
value is correct and unreadable, which is a different defect from the one I was
hunting and the only one in this section.

### `level` and `className` cannot go stale, and `level` cannot be exercised

`main.dart:191` takes them from `replay(log)` — **the ledger**. Only `area` is a
caller-supplied parameter (`_saveBytes(log, {String? area})`). So the row's level and
class are projections of the same log Continue reads and cannot drift from it. Checked
anyway: all five rows read `level 1`, and each ledger holds exactly one
`character.class-added` with `levels: 1`, class ids matching the rows
(soldier/soldier/soldier/duelist/duelist).

⚠ **And the level field cannot be tested at all on this build.**
`base-rules/rules/event_kinds.toml:94` declares `character.levelled`, and
`grep -rn "levelled" KOTOR-RPG-APP/lib` returns **nothing**. **Nothing in the app ever
emits it**, so no character can leave level 1 and there is no second value to compare.
That is a scoped negative, not a pass.

---

## 2. The header never moves while you play — it moves only on load

My own last negative. Answered, and ⚠ **it inverts the hypothesis in the brief.**

`main.dart:241` stamps `area: _entry` into every save. `_entry` is assigned in
**exactly three places**, and none of them is during play:

    main.dart:298   _entry = resume?.area ?? _package?.entryArea;   ← opening a save
    main.dart:353   _entry = entry;                                 ← New Game
    main.dart:413   _entry = _package?.entryArea;                   ← Play, from the hub

`PlayScreen` receives `entryArea: _entry!` and then travels **without telling `main`.**

**Predicted, then run as a controlled sequence on one character:**

| step | where I was | ledger's last move | header |
|---|---|---|---|
| staged file | — | `a01-probe-room 3,1` | `a05-probe-barrier` |
| loaded it, before moving | a01 | `a01-probe-room` | **`a01-probe-room`** ← moved, no transit |
| walked through the a01→a05 door | **a05** | `a05-probe-barrier 5,2` | **`a01-probe-room`** ← did not move, on a transit |
| walked through the a05→a06 door | **a06** | `a06-probe-longrun 1,1` | **`a01-probe-room`** ← still |

⚠⚠ **The header names the area the SESSION BEGAN IN, and it is frozen for the life of
the session.** It advances on a load — which is the answer to *"does it ever advance
without a transit"*: **yes, and that is the only time it advances.** It does not
advance on a transit, and it lags by however many areas you travel, not by one.

⚠ **So a player who spends twenty minutes in one room has a header that is CORRECT.**
Time is irrelevant. **Travel is the whole story**, and the disagreement condition is
exact: *the header disagrees with the ledger if and only if the player changed area
since the session began.*

### ⚠ Correction to TEST 045 §3 — my own characterisation was a curve through three points

TEST 045 said *"the header names the area you last left; the ledger names the area you
last arrived in."* **That fitted the three saves I had and it is not the mechanism.**
It happened to hold because each of those sessions was one transit long. A second
transit falsifies it: after a05→a06 the "area I last left" is a05 and the header says
a01. **`_entry` is the session's starting area, full stop.**

The consequence I filed stands and is now exactly located: the Load Game row's third
field is the header (`save_listing.dart:67`, *"area — the row: where"*), Continue and
Load both read the ledger (`main.dart:298`), and **the row is the one a player reads
before choosing.** What I had wrong was why.

---

## 3. `a07-probe-pinch` now carries its own reason

`TEST 037`'s trap carried its reproduction in the file's own comment and this fixture
will outlive the report that explains it. Both files now say so, and I checked the
edits are comments only —
`diff <(grep -v '^\s*#' …) <(grep -v '^\s*#' …)` is empty for both — and that Loom
still reports **exactly 11**, unchanged.

`areas/a07-probe-pinch.toml` opens with:

> ⚠⚠⚠ **THIS AREA IS DELIBERATELY FAULTED AND THE FAULT IS THE POINT.**
> ⚠ IT RAISES THIS PACKAGE FROM 10 PROBLEMS TO 11, ON PURPOSE. If you are counting
> problems on `tester-probe`, subtract exactly one … **DO NOT "FIX" IT: repairing it
> destroys the only board in the corpus that tests `PT-1613`.**

…then what the ruling guarantees, why a diagonal pinch is the only shape that can test
it, why there are two doors (so `areaHasNoWayOut` stays quiet and one fault is
isolated), the observed sentence verbatim, and the note that made it worth keeping:

> ⚠ AND THE FIRST DRAFT AIMED AT THE WRONG SUBJECT. I put a CREATURE in the far half
> and expected a fault. `_position` checks arrivals and connections and NEVER
> contents. **A CREATURE NOBODY CAN REACH IS A LOCKED ROOM, NOT A DEFECT.** probe-slug
> at 2,3 is still here, unreachable and unflagged, as the standing demonstration.

`package.toml` carries the short version at the top, so anyone reading the count sees
it without opening an area file, and it names the one-way rooms as two of the other ten.

⚠ I also re-parsed every file in the package: all ok except `zoo-directory.toml` (a
directory on purpose) and `zoo-unparseable.toml` (unparseable on purpose).

---

## What I did not check

- `47789fa` / `776e42e` / Lodestar `e1a837c`. Not in either bundle. Untested.
- **Whether the Load Game row truncates because of the window width or a fixed
  width.** I ran at 1280×720 throughout and did not resize.
- Whether `savedAt` is correct across a *timezone* change or a clock change — I only
  showed it is not the mtime.
- The `rulesVersion` and `package` header fields. I followed area, level, class and time.
- Whether anything other than the Load Game row reads the header's `area`.
  `main.dart:298` is the only `.area` consumer I found, and it uses the ledger's.

## State

- **`tester-probe` changed — comments only this run**, verified by diff.
  `areas/a07-probe-pinch.toml` and `package.toml` gained the explanations above; no
  key, value, tile or placement moved. Snapshots `PKG-T043/` … `PKG-T046/`.
  ⚠ **The package still reports 11 problems and one of them is mine on purpose.**
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination at
  `SV-T046-after/`.
- `base-rules` **unchanged** — `diff -rq` clean against `BK19`.
- The NWN install was not read or written.
