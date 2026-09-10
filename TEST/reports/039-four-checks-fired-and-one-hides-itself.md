# 039 · All four position checks fired — and one of them hides itself

**From `Tester`. Unrequested number.** `PT-1512` followed, **and `PT-1617`
applied**: `BK15/` and `SV-T038/` taken first, and **a diff showing somebody
else's change would have been reported, not reversed.** Nothing of anyone's
moved this run.

**⚠⚠ BUILT AND MEASURED AGAINST — pin read from the commit I BUILT:**

    Loom 7d04511  →  Lodestar 5031aed      built 14:42

**⚠ Verified in `~/.pub-cache/git/Lodestar-5031aed…/` AND in the binary** —
`"can be stood on"` ×2, `"nobody can stand on it"` ×2, `"no walkable route"` ×2.

**⚠⚠ AND MY FIRST GREP OF THAT BINARY RETURNED THREE ZEROS.** I had guessed the
wording. **The strings were mine, not the build's** — I read the reasons out of
the pub-cache source and grepped again. *Ask whether the instrument is
measuring, and the instrument here was my own guess.*

**⚠ THE APP WAS NOT BUILT AND NOT OPENED.** Everything in `§3` is a source read
of `d11b724`/`5031aed` plus a measurement of save files. **No app finding here
was observed on a screen** — said plainly because the rest of this thread was.

**As I write: `Loom 7d04511` is 9 dirty — the palette rebuild has started.**

---

# ✅ 1 · ALL FOUR FIRE, AND THE WORDING IS WORTH KEEPING

**Four fixtures on `a02-probe-hall`, `Verify again` between each — ⚠ and it
re-reads from disk, so the package need not be reopened.**

## `landingNotStandable` — fixture `#...`

    a02-probe-hall   from-probe-room
    "a02-probe-hall" declares the arrival "from-probe-room" at 0,0, and that
    square is wall — nobody can stand on it. A door landing there puts a
    character inside it.

✅ **Names the area, the arrival, the coordinates, THE TILE KIND, and the
consequence.**

## `connectionUnreachable` — fixture `#.#.` / `.#..` plus a standable arrival

    a02-probe-hall   door.probe-hall.01
    "door.probe-hall.01" is at 1,0 in "a02-probe-hall", and no walkable route
    joins it to anywhere a character can arrive. The square is floor and it is
    cut off.

✅ **And it took the FLOOR branch of its own conditional** — *"the square is
floor and it is cut off"* rather than *"the square is wall"*. **A door that
exists and cannot be walked to, which is the case `areaHasNoWayOut` explicitly
does not cover.**

## `areaHasNoWayOut`, SECOND BRANCH — same fixture

    a02-probe-hall
    "a02-probe-hall" has 1 connection and none of them can be walked to, so a
    character who arrives is stuck.

✅ **The branch `038` could not reach. Singular/plural handled.**

## `areaHasNoStandableSquare` — fixture: every square walled

    a02-probe-hall
    No square in "a02-probe-hall" can be stood on, so nothing can be placed
    there and nobody can arrive. The fallback that rescues a player from a
    walled-in arrival has nowhere to fall back to.

> **⚠ ITS LAST SENTENCE IS `037 §1`, IN THE FAULT TEXT.**

**✅ AND IT SUPPRESSES THE OTHER THREE.** With the area fully walled the count
was **11, not 13**: the check `return`s, so `landingNotStandable`,
`connectionUnreachable` and `areaHasNoWayOut` do not also fire for that area.
**The worst fault wins rather than drowning the author in three descriptions of
one wall.** That is a choice and it is the right one.

---

# ⚠⚠ 2 · AND ONE OF THEM HIDES ITSELF. MEASURED ON ONE VARIABLE

**My first attempt at `connectionUnreachable` FAILED to fire** — door at `1,0`
walled in on all three sides, and `Verify` said 11. **I did not accept that.**

**Two runs, walls byte-identical, one line different:**

    walls #.#. / .#.. , arrivals: from-probe-room 0,0 (WALL) + far-corner 3,3   →  13 problems
    walls #.#. / .#.. , arrivals: from-probe-room 0,0 (WALL)                    →  11 problems

**Removing the one STANDABLE arrival silenced BOTH `connectionUnreachable` AND
`areaHasNoWayOut`.**

> **⚠⚠ AN AREA WHOSE ONLY ARRIVAL IS UNSTANDABLE HIDES ITS OWN CUT-OFF DOOR.**
>
> The reachability seed is *"anywhere a character can arrive"*, and with no
> standable arrival it falls back to the **first standable square** — which in
> this fixture **is the isolated door itself.** The door trivially reaches a
> place a character can arrive, because it *is* that place.

**⚠ And that pairing is not exotic — it is the obvious one.** Walling an arrival
is exactly what an author does by accident with a brush, and it is the case
`landingNotStandable` exists for. **The moment it fires, the two faults that say
*this area is a trap* go quiet.**

**✅ The package is not silent** — `landingNotStandable` still fires, so the
author is told the arrival is walled. **But the severity collapses**: *"your
arrival is in a wall"* reads as a placement slip; *"there is no way out"* reads
as a soft-lock, and it is the second one that is true.

**⚠ Shape it wants:** the fallback seed exists so the runtime can put a player
somewhere — `PT-1605`. **The VALIDATOR does not need it**: an area with no
standable arrival should seed from nothing and report every connection as
unreachable, which is exactly what the player will experience.

---

# ⚠⚠ 3 · `VitalityState.down` IS REACHED ONLY AT EXACTLY ZERO — AND THAT CORRECTS `PT-1616` AND ME

**You said to settle whether the state is ever entered. ⚠ It is, and far more
rarely than either of us assumed.**

    pools.dart:74   partyStandsAtOne(mode, role)
                      enemy            -> false
                      Difficulty.easy  -> true
                      normal + henchman-> true
                      ⚠⚠ normal + PLAYER -> FALSE

**And `play_screen`'s own comment: *"the app has no setting for it — every fight
so far has been Normal."*** So the player takes the last branch:

    current > 0            -> standing
    current == 0           -> down        ⚠⚠ EXACTLY ZERO, AND ONLY THERE
    current <= -constitution -> dead
    otherwise              -> DYING

## ⚠ So `revived` and `downed` do not describe the same set

`play_screen.dart:1888` writes `revived` for
**`c.vitality.current <= 0 && c.role != Role.enemy && !_hasDied(...)`** — **the
whole band.** `down` is one point of it.

**Counted across all twenty saves, every `encounter.ended` at or below zero:**

    at or below zero        125
      exactly 0  (DOWN)      40
      negative   (DYING)     85

> **⚠⚠ SO A WRITER PLACED BESIDE `revived`'s WOULD EMIT ~92 `character.downed`
> EVENTS FOR A POPULATION THAT IS AT MOST ~40 DOWN. The log would stop being
> silent and start being WRONG, which is worse.**

**⚠ I must correct my own `038`.** I wrote *"92 revivals and not one down"* as
though the 92 were 92 missing downs. **They are not.** At most 40 could be, and
I did not check which of the 125 belonged to the player rather than a henchman.

## ⚠⚠ AND THE STATE THE PLAYER ACTUALLY ENDS IN HAS NO EVENT AT ALL

    grep "dying" Lodestar/lib/src/ledger.dart        -> nothing
    grep "character.dying" base-rules event_kinds    -> 0

**`VitalityState.dying` is the player's ordinary failure state on Normal — 85 of
125 records — and there is no kind for it, in the ledger or in the shipped
rules.** `downed` is declared and unwritten; **`dying` is not even declared.**

## ⚠ And a third thing, which is a design question rather than a gap

**`died` and `revived` are written in `_writeOutcome`, at fight END** — the
comment says so itself: *"`PT-1421` is ONE CROSSING ONE EVENT and this wrote one
per FIGHT."* `PT-1538` closed the duplicate half; **the events are still emitted
from the outcome and not from the crossing.**

> **⚠ So `downed` beside `revived` gives ONE PER FIGHT, and `PT-1421` asks for
> ONE PER CROSSING. The honest site is `applyDamage`, where `before` and `after`
> are both known — and there it would fire rarely, and correctly.**

---

# ⚠⚠ 4 · WHAT THE TREE MARKS — AND IT IS A GROUPING ARTIFACT, NOT A FAULT SURFACE

**Ten faults on `tester-probe`. ⚠ The tree marks THREE, and they are the three
it could not FILE.**

    ▼ ⚠ unknown kind          ⚠ red, and the only alert in the whole tree
        probe-sentinel.pro…  3,2      from = "blueprints/characters/…"
        probe-warden.pro…    1,2      from = "blueprints/characters/…"
        mystery.probe-roo…   0,0      from = "widgets/probe-thing"

**Everything else renders in plain text, including four real faults:**

    zoo-empty.probe-…    2,4    ⚠ blueprintUnreadable — plain
    probe-warden.pro…    4,1    ⚠ equipmentMissing    — plain
    probe-warden.pro…    3,4    ⚠ equipmentMissing    — plain
    a03-probe-yard              ⚠ areaHasNoWayOut     — plain teal, like any area

> **⚠⚠ THE GROUP EXISTS BECAUSE THE TREE HAD NOWHERE TO PUT THOSE THREE. The
> mark is a side effect of not being able to classify a path — it marks what it
> CANNOT FILE and nothing it CAN file, however broken.**

## ⚠ AND EVERY POSITION FAULT NAMES A ROW THE TREE ALREADY DRAWS

**This is the list, and it is why the gap is cheap to close:**

| fault | it names | the tree draws that row today |
|---|---|---|
| `landingNotStandable` | an **arrival** | ✅ `▼ arrival points` → `from-probe-hall 4,2` |
| `connectionUnreachable` | a **connection** | ✅ `▼ doorways` → `door.probe-room.05 5,2` |
| `areaHasNoWayOut` | an **area** | ✅ the area row itself |
| `areaHasNoStandableSquare` | an **area** | ✅ the area row itself |
| `blueprintUnreadable` · `blueprintMissing` · `equipmentMissing` | a **placement** | ✅ the placement row, with coordinates |
| `duplicateArrivalName` · `landingPointUndeclared` | an arrival / a connection | ✅ both drawn |
| `entryUndeclared` · `entryAreaUnknown` | the **package** | ✅ the `Tester Probe` row, which already carries the count |

**⚠ Not one of them needs a new row. Every fault has a place to land.**

**⚠ And there are TWO alert surfaces already, split by subject:** the **palette**
marks BLUEPRINTS in red with the reader's own refusal — *"⚠ zoo-comment-only —
The file has no [character] section"* — and the **tree** marks unclassifiable
PLACEMENTS. **Neither marks an area, an arrival or a connection**, which is
exactly where the four new faults live.

**⚠ Shape it wants:** the count is already on the package row (`10 problems`).
**A fault carries `areaId` and `tag` — which is the row it belongs to** — so the
tree has the key it needs without a new lookup.

---

# ⚠ 5 · Seventh sighting, and it is on its way out

**`doors` still carries both lines on `7d04511`** — *"painted as `doorway`
above"* **and** *"⚠ cannot list — no folder is specified for this kind **yet**"*.
Sixth report, seventh sighting. **Loom is 9 dirty as I write and the palette
rebuild is where this dies; I am not filing it again, only marking the date.**

---

# 6 · Scoped negatives

- **⚠⚠ THE APP WAS NEVER OPENED.** `§3` is a source read plus a count of save
  files. **I did not watch a character go down, and I did not construct a fight
  that lands a player on exactly 0.** That is the observation that would close it.
- **⚠ I did not separate PLAYER from HENCHMAN in the 125.** `revived`'s guard is
  `role != Role.enemy`, which includes henchmen, and `partyStandsAtOne` is TRUE
  for a henchman on Normal — **so some of the 85 negatives may be henchmen who
  were genuinely `down`.** The 40/85 split is a ceiling on the error, not a
  measurement of it.
- **⚠ `connectionUnreachable`'s WALL branch** — *"the square is `wall`"* — not
  exercised; I only produced the floor-cut-off form.
- **⚠ `referenceMissing`, `targetAreaUnknown`, `targetAreaUnreadable`,
  `duplicateArrivalName`, `entryUndeclared`, `entryAreaUnknown`,
  `requiredFieldMissing`** — still never seen to fire by me. **Seven of nineteen
  members remain unwitnessed**, and `§4`'s table lists where they would land
  from their `areaId`/`tag`, not from having watched them.
- **⚠ The suppression in `§1`** is inferred from the count (11 not 13) and from
  the `return` in the source. **I did not confirm which three were suppressed by
  reading them individually.**
- **`PT-1607`'s fourth placement** — `probe-warden.probe-room.10` — still not
  walked into.
- **Painting tiles** — three sessions now, **still never with a TILESET.**

## What I left behind — nothing

    diff -rq packages BK15/  →  IDENTICAL
    all 20 saves             →  IDENTICAL, and the app was never opened

**`a02-probe-hall` was rewritten four times and restored from `BK15/` byte for
byte.**

**Backups: `BK3/`–`BK15/`, `SV-T031/`–`SV-T038/`.**
