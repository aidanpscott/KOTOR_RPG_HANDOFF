# TEST 045 — both stalls, PT-1613 held, and a count that changed the question

**Built against:** the **same two binaries as TEST 043 and 044.** App bundle
`kernel_blob.bin` built **16:11**, from `660134a` → Lodestar `9aa7382`
(`grep -c "PT-1626"` → **0**). Loom bundle built **16:39**, from `908a412`.

⚠ **BOTH TREES HAVE MOVED AND NEITHER BUNDLE HAS.** `KOTOR-RPG-APP` HEAD is
`47789fa`, `Loom` HEAD is `776e42e`. **I did not rebuild either** — that writes into
Coder's tree. `47789fa` / `776e42e` / Lodestar `e1a837c` are untested by me.

**Instrument:** PID-scoped. App `536115`, Looms `535096`/`535369`, all on window
`142606339`. All killed by PID; Coder's `517963`/`517968` survived.

---

## 1. The budget stall — the last unseen sentence in `approach.dart`

TEST 044 could not produce *"out of movement N squares short"* and gave the
arithmetic: it needs `d ≥ budget + 2`, a fight starts at contact, so the largest gap
a player can open is `budget + 1`. **The way out is not a bigger run. It is a slower
enemy** — and one exists, because of an asymmetry nobody had named:

> ⚠⚠ **`combatantFrom` READS SPECIES FOR SPEED AND NOT FOR ABILITIES.**
> `attack.dart:233` — `final own = sp == null ? null : speedSquaresBySpecies[sp];`

`species.toml` gives `snivvian` *"8 metres."* — 4 squares against a player's 5. So I
authored `probe-slug` (snivvian) and `a06-probe-longrun`, a 16×3 open lane with no
wall at all, the opposite shape to the barrier. Bump from 1,1; run five east to 6,1;
`away = 6`; it needs five steps and has four. **Predicted, then observed:**

    probe-slug.probe-longrun.02 closes 4 squares — 6 to 2 ·
    out of movement 2 squares short ·
    probe-slug.probe-longrun.02 cannot reach Barrier Tester — 2 squares, reach 1

⚠ **Both of `approach.dart`'s stalls are now on screen**, and they are different
sentences for different reasons exactly as the source says: TEST 044's
*"nothing it can walk gets it closer"* is the **board**, this is the **budget**.
Both routes into `fight.dart:215` are now exercised.

⚠ **And `closes 4 squares` is the measurement, not an inference.** A Human moves 5
and this creature moved 4, from the species alone. **That sharpens the open Gamorrean
finding rather than repeating it:** `probe-tusk` swinging at `Strength 2` on `str 14`
with `species = "gamorrean"` (+4) is not "species is ignored" — **species reaches the
speed and not the ability scores**, and both come off the same blueprint field.

### Can a fight begin at a distance? No.

The brief asked. `_begin` has exactly two call sites (`play_screen.dart:731`, walking
into something, and `:1150`, `_maybeFight` from a conversation) — **and a conversation
also starts by walking into the creature.** There is no third. That is why I placed
`probe-slug` adjacent to the arrival: a creature placed far from any arrival cannot
start a fight at all, it can only be walked to. Consistent with use across the whole
thread — a03 holds five creatures and none of them ever initiated.

### ⚠ And a second discarded sentence, the same shape as the damage derivation

`attack.dart:250` builds `speedNote` — *"`<sp>` has no speed in the rules, so the
default is used"* / *"this blueprint names no species, so its speed is the …"*.

    grep -rn "speedNote" KOTOR-RPG-APP/lib
    attack.dart:56   declaration
    attack.dart:68   constructor
    attack.dart:250  construction

**Three hits, none of them a read.** TEST 043 found `DamageRoll.line` built and never
called; this is the second field of the same kind. The engine explains itself and the
screen does not ask.

---

## 2. PT-1613 held, and my first fixture aimed at the wrong subject

⚠ **`a05-probe-barrier` cannot test the ruling** — nothing in it is unreachable; rows
0 and 4 join both sides of the wall. Loom confirms: a05 and a06 draw unflagged, and
the package stayed at **10 problems**. Correct, but it answers nothing.

So I built `a07-probe-pinch`, 4×4, two halves touching **only** at `1,1`/`2,2` — a
diagonal, which `approach` walks and a player cannot.

⚠ **My first draft put a CREATURE in the far half and expected a fault. It is not one.**
`_position` (`package_validate.dart:406`) checks `areaHasNoStandableSquare`,
`landingNotStandable`, `connectionUnreachable` and `areaHasNoWayOut` — **arrivals and
connections, never contents.** A creature nobody can reach is a locked room, not a
defect. I read the validator before filing instead of after, and rebuilt the fixture
to put a **door** in the far half, with a second reachable door in the arrival half so
a player is never trapped.

**Expected exactly one new fault. Got exactly one — 10 problems → 11:**

    door.probe-pinch.03   3, 3
    "door.probe-pinch.03" is at 3,3 in "a07-probe-pinch", and no walkable route
    joins it to anywhere a character can arrive. The square is floor and it is
    cut off.

⚠ **`PT-1613`'s guarantee held on the first board that could test it.** The narrow
four-offset set caught a door that is reachable only diagonally — *"it may report a
way out that exists and must never miss one that does not."* And `areaHasNoWayOut`
correctly stayed **quiet**, because the other door is reachable. Both halves of the
ruling, on one board.

---

## 3. The count — and it changes the question rather than answering it

⚠⚠ **THE FIRST THING THE COUNT FOUND IS THAT MOST SAVES CANNOT BE ASKED.**

    KRSV \x01  →  a 19-byte header with NO fields at all
    KRSV \x02  →  package · character · class · area

**15 of the 20 saves on the shelf are format 1.** They carry no header area, so the
comparison does not exist for them. `save_listing.dart:69` says so on purpose —
*"a `format = 1` save does not carry them and must still be readable… Null means this
save is older than the field."*

Of the **five** version-2 saves on the owner's shelf: **five agree, zero disagree.**

| shelf | saves | format 1 | format 2 | agree | disagree |
|---|---|---|---|---|---|
| the owner's shelf | 20 | 15 | 5 | **5** | **0** |
| end of TEST 043 | 21 | 14 | 7 | 5 | **2** |
| end of TEST 044 | 21 | 14 | 7 | 6 | **1** |

The three that ever disagreed — `probe-walker`, `reach-tester`, `barrier-tester` —
are **all three saves my own runs left mid-session**, and every save that came to rest
agrees.

⚠ **So the answer is: not normal, and not quite racy either.** It is **positional**.
The header names **the area you last left**; the ledger names **the area you last
arrived in**. `barrier-tester` ends with header `a05-probe-barrier` and ledger
`a01-probe-room 3,1` — the transit out of a05 and into a01. **Those are two different
true facts, and they only look like a bug when something reads one for the other.**

## 4. ⚠ Correction to TEST 044 §1 — I pointed at the wrong line

TEST 044 said *"the list names one area and the button opens another"* and quoted the
line *"in your campaign, a02-probe-hall left you at 1"*. **That line is not the
header.** `play_state.dart:209` builds it from the ledger's `encounter.ended` rows —
`e.payload['encounter']` — and it is a truthful statement about an encounter, not a
claim about where you will resume. **The claim was right and the evidence was wrong.**

Aimed properly, it holds, and here is the real one. `save_listing.dart:67` — *"area —
the row: where"* — the header's area is **the Load Game row's third field**:

    LOAD GAME
    Barrier Tester    level 1 soldier · a05-probe-barrier · 14…
    …
    → clicked it, and it opened a01-probe-room.

⚠ **The Load Game row says `a05-probe-barrier` and loading it puts you in
`a01-probe-room`.** Confirmed by `main.dart:298` — `_entry = resume?.area ?? …`,
where `resume` is `projectPlayState(file.log).position`, **the ledger**. The row is
the header; the load is the ledger; they are different facts and the row is the one a
player reads before choosing.

⚠ **And the format split has a second visible consequence in the same list.** The
sixth row read **`probe-walker.sav` · "when not recorded"** — a raw filename where the
other five show a name, a class and an area, because a format-1 save has none of them
to show.

---

## What I did not check

- `47789fa` / `776e42e` / Lodestar `e1a837c`. Not in either bundle. Untested.
- Whether the Load Game row's **level** and **time** fields are also stale. I only
  followed the area.
- Whether `speedNote` is read anywhere outside `KOTOR-RPG-APP/lib` (Loom, tests).
- **`a06` and `a07` were not played beyond the one fight and the one validation.**
  `a07`'s far half is unreachable by design and I never stood in it.
- I did not test whether the header ever advances *without* a transit.

## State

- **`tester-probe` has changed again and I am keeping it**, declared: new
  `areas/a06-probe-longrun.toml`, `areas/a07-probe-pinch.toml`,
  `blueprints/characters/probe-slug.toml`; `a05-probe-barrier.toml` gains
  `door.probe-barrier.03` (11,4 → a06) and `.04` (0,4 → a07) plus two arrivals,
  `tag_seq` 3 → 5; `package.toml` `[order].areas` gains both. Snapshots `PKG-T043/`,
  `PKG-T044/`, `PKG-T045/`.
  ⚠ **`a07-probe-pinch` is a deliberately faulted fixture** — it is *supposed* to
  raise `connectionUnreachable`, and the package's problem count is now **11 rather
  than 10 because of me**. Anyone counting problems on this package should subtract it.
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination at
  `SV-T045-after/`.
- `base-rules` **unchanged** — `diff -rq` clean against `BK19`.
- The NWN install was not read or written.
