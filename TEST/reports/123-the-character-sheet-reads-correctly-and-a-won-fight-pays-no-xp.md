# TEST 123 — the character sheet reads correctly, and a won fight pays no XP

**Build.** App **`7b6a7b5`** ("the character sheet, restyled to PT-1249 —
PT-2471"), tree clean, built from `git archive` of that sha. The committed
lock resolves Lodestar **`d1fcab69`**, and that is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules
files and 65 standard blueprints.

**Verdict.** **All seven routed items confirmed**, the `Needed` pair
thoroughly. Two defects found beside them, one of which is not the sheet's:
**winning a fight awards no XP at all**, and **Auto Level Up leaves Vitality
and Force stale until the save is reloaded**. One thing I nearly filed as a
defect turned out to be my own fixture, and the control is recorded.

---

## The seven items

### 1. Portrait viewport — confirmed, with a stated limit

A rounded viewport holds a static circular placeholder. **No model, nothing
animated, nothing 3D.**

⚠ My saves carry `portrait: null`, so what I have confirmed is *the viewport
and the absence of a model*, not a rendered portrait image. This bench ships
no portrait asset, so I cannot tell a working portrait from a placeholder
that never loads one. Worth one reading on a package that has one.

### 2. The alignment arc — confirmed, and it is folded rather than constant

Beside the viewport, dark red at the **left** horn and pale at the **right**,
which is `alignmentFrom`'s own direction (low is dark). The caption carries
**both halves**, as `PT-2441` ruled.

The pair that makes it a reading rather than a picture — same fixture, same
level, differing only in the log:

| log | caption | marker |
|---|---|---|
| no casts | `Neutral 50` | at the apex |
| three dark casts | `Neutral 49` | just left of the apex |

A constant would have read the same twice.

### 3. Value and modifier in separate columns — confirmed

```
STR   10    +0
DEX   10    +0
CON   16    +3
INT   10    +0
WIS   18    +4
CHA   18    +4
```

Two genuinely separate columns, both left-aligned on their own edge, holding
down the whole table — the modifier column stays put whether the value is
one digit or two.

### 4. Vitality and Force as current/max — confirmed

`Vitality 86 / 86` and `Force 159 / 159`, in a `pools` block above the
abilities.

### 5. `Needed` — confirmed on all four clauses

**A real number that is left to earn, not a threshold.** `xpToReach(13)` is
78000, and at level 12 with 66000 the sheet reads:

```
Experience   66000
Needed       12000
```

**It moves with XP, level held still.** Two fixtures, same level 12, XP the
only variable:

| XP | Needed |
|---|---|
| 66000 | 12000 |
| 70000 | **8000** |

+4000 XP, −4000 needed, exactly. A fixed threshold would have printed 78000
twice.

**Zero once passed, not negative.** At 80000 with the level unspent:
`Needed 0`.

**Absent at the cap.** Level 30, `Experience 435000`, and **no `Needed` row
at all** — not a zero, not a dash, the row is gone. The level buttons are
gone with it, which is right: there is no level to take.

**And it recomputes on a level change.** After Auto Level Up took level 13,
`Needed` became 11000 — `xpToReach(14)` of 91000 less 80000 — without a
reload.

⚠ **What I could not do is confirm it by EARNING XP**, because no XP can be
earned. See the defect below.

### 6. Auto Level Up — confirmed, it grants the level

Level 12 → **13**, immediately, in the sheet header *and* the party card,
with the sheet staying open.

### 7. Level Up (manual) — confirmed inert, with its reason visible

The button is drawn dim beside the live one, grants nothing when clicked,
and the reason sits directly under the viewport in the alert colour:

```
choosing how to spend a level is not built yet — Auto takes it
```

---

## DEFECT — a won fight awards no XP, and writes no outcome at all

A level-12 character killed the only enemy on the board:

```
Force Scream · 8f — 151 → 143 · at frail.xp.01 · frail.xp.01 — 3d6 17
frail.xp.01: -10 of 20
```

The fight then ended — budget strip gone, verbs back to `arrows to move · m
map · i carrying · esc to leave`. And nothing was paid:

```
before   Experience 66000 · Needed 12000
after    Experience 66000 · Needed 12000
```

Unchanged after three further turns, after walking, and **after a reload**.

**The log says why it is not a display problem.** Decoding the save the app
itself rewrote (738 → 771 bytes, so it was written after the fight), the
tail is:

```
session.started
power.cast {force_scream, … force: 151}
power.cast {force_scream, … force: 143}
```

**No `encounter.ended`. No `character.died`. No `character.xp-awarded`.**
`_writeOutcome` never ran.

**Control — the mechanism exists and works elsewhere.** Six saves from
earlier play carry awards (`both2`, `both-ways`, `cr0-cast`, `level-up`,
`stormer`, `w-kill`), and `cr0-cast` shows the shape this fight should have
produced:

```
encounter.ended {subject: x-cr0.probe.02, vitality: -5}
encounter.ended {subject: CR Zero Cast, …}
character.died  {subject: x-cr0.probe.02}
character.xp-awarded {amount: 100, from: x-cr0.probe.02, cr: 0.0, level: 1}
```

So this is not "the table pays nothing": a level-12 character beating a CR-1
creature is owed **25**, the floor of the level-12 row, and `XpAwards`'s own
note is that K2's table *"has no cell worth zero."*

⚠ **Scope, honestly.** One bench, one enemy, killed by a **power** on the
**player's** turn, with the player holding no weapon. I did not determine
which of `_writeOutcome`'s two call sites (`play_screen.dart:8457` and
`:9733`) should have fired, and I have not isolated which of those
conditions matters. What is measured is that the fight ended and the outcome
was never written.

## DEFECT — Auto Level Up leaves the pools stale until a reload

Immediately after Auto Level Up granted level 13, on the open sheet:

| | before | after Auto | after reload |
|---|---|---|---|
| level | 12 | **13** | 13 |
| Experience / Needed | 80000 / 0 | **80000 / 11000** | 80000 / 11000 |
| Vitality | 86 / 86 | **86 / 86** | **93 / 93** |
| Force | 159 / 159 | **159 / 159** | **172 / 172** |

The level, Experience and Needed all update live; **Vitality and Force do
not**. The reload proves the grant itself is correct and persisted — +7
vitality and +13 Force are really there — so this is a refresh gap on the
live screen, not a missing grant. A player who levels up mid-session is
fighting on last level's pools until they reload.

## A smaller one — the disabled button does not absorb its click

Clicking the dim **Level Up** dismisses the whole sheet. Three readings:

* dim `Level Up` → sheet closes, no level granted
* blank space inside the sheet → sheet closes
* live `Auto Level Up` → **sheet stays open**, level granted

So the sheet is tap-anywhere-to-dismiss and the disabled button lets the tap
through to the barrier, where the live one swallows it. The observable is
that a player probing a greyed control loses the screen. Sibling of
`PT-2464`'s *"a greyed button that still took clicks"*, from the other side.

## Not a defect — and the control is the point

The sheet first showed `Defence —` with a red line beside it:

```
`items/armour/clothing` will not open: There is no item here.
```

I nearly filed that. **It is my fixture:** every save I author names that
body item and this bench does not carry it. With the body item dropped and
nothing else changed, the same sheet reads **`Defence 10`** with no error.

So the sheet declines to print a rating it cannot compute, and names the
path and the reason instead of guessing. That is the behaviour wanted, and
it is worth recording as a pass rather than leaving the screenshot to look
like a fault.

## Fixture

`tester-mind`, with `m06-xp` added — one `frail` (20 vitality) and nothing
else, because it is the only bench creature two Force Screams can finish and
therefore the only one that lets a fight be *won*.

`mk123.py` authors XP exactly rather than playing up to it —
`xpToReach(N) = 1000 × (N−1) × N ÷ 2` — with modes `owed` (66000, Needed
12000), `mid` (70000, Needed 8000), `unspent` (80000, Needed 0, level
available), `cap` (level 30) and `nobody` (no body item, the Defence
control). Three dark `power.cast` events give the arc something to fold;
`plain` has none, and the 50-against-49 pair is what proves it folds.
