# 023 · It stays dead, and the marker does not go

**From `Tester`. Unrequested number.** `PT-1512` followed; **all packages
restored IDENTICAL**.

**Built 20:20 from:**

    Lodestar 0035afa · Lens 9ca5982 · Loom fe9c1e4 · app 7552602

**Pins honest.** 1280×720.

---

## ⚠⚠ `PT-1527` HOLDS. THE PAIR IS GONE, AND DEATH STICKS

**I killed `probe-sentinel.probe-yard.01` with Grave Digger. Its whole history
in the log:**

    encounter.ended  -2
    character.died
    encounter.ended   0
    character.died

**No `character.revived` anywhere after a `character.died`.** The pair `022`
found is not reproducible on this build, and **you were right not to blame the
role guard** — `PT-1524` removing the down state for an enemy is what removed
the mechanism.

**And it now says so in words.** The strike line reads:

> `probe-sentinel.probe-yard.01 falls — Blaster Rifle · rolled 17 — d20 16 +
> attack 1 · needed 10 — hit · **10 damage · -2 left · character.died**`

and the working line reads **`probe-sentinel.probe-yard.01: 0 of 8 — killed`**.

**⚠ An enemy dies at zero now, not at −Constitution.** One 10-damage blow on an
8-vitality creature was enough — `022`'s "eighteen damage in one continuous
fight" is no longer the price.

---

## ⚠ YOUR FIVE CLAIMS FROM `022`, ANSWERED

| claim | `022` | now |
|---|---|---|
| `character.died` survives a quit | no | **✅ yes** |
| `_occupant` releases | no | **✅ yes — but only on area load** |
| the marker goes | no | **❌ no** |
| a dead creature leaves nothing | untestable | **❌ it leaves its marker** |
| the vacated square exists | no | **✅ YES — first time in this project** |

**I walked onto both dead creatures' squares** — `a01-probe-room · 4, 3` and
`a03-probe-yard · 7, 2` — and no fight started. **The square is real and it is
walkable.**

---

## ⚠⚠ F1 — THE MARKER OUTLIVES THE CREATURE, AND IT IS THE `014` SEAM AGAIN

**Both dead creatures are still drawn**, as hollow markers, in two different
areas, after a full quit. **I stood on one and its marker was drawn underneath
my own token.**

**Because the drawing does not come from `_here`.** You removed the dead
creature from `_here` **once**, which is right and which is why the square
released — but `Lens/board.dart` draws `area.contents` directly, and the row is
still in the file. **This is `014`'s F1 one step along:** *"there is no bad
`from` the board will not render"* is now *"there is no dead creature the board
will not render."*

**So "a dead creature leaves NOTHING" is true of the fight model and false of
the screen.**

---

## ⚠⚠ F2 — A CORPSE IS STILL AN OCCUPANT UNTIL THE AREA RELOADS, AND IT WRITES A SECOND DEATH

**Immediately after killing it, I stepped into the same square and got:**

> `probe-sentinel.probe-yard.01 falls — **initiative** —
> probe-sentinel.probe-yard.01 10 · Grave Digger 8`

**A fresh fight, rolling initiative against a creature the line above calls
`killed`.** The release happens when the area is loaded, not when the creature
dies — so within the session the corpse fights back.

**⚠ And it has a consequence in the log, which is the second `died` above.**
`PT-1421` is *one crossing, one event*; **`character.died` is written twice for
`probe-sentinel.probe-yard.01`**, and the second one is that re-engagement
ending. **The duplicate death is caused by the corpse still being an occupant.**

---

## ⚠⚠ AND `018`'s WALL QUESTION IS ANSWERED — THREE REPORTS LATE

**With a vacated square I could finally construct it.** I painted a wall on
`a03-probe-yard · 7, 2`, the square the dead creature is on, and walked into it:

> **the wall blocks the way**

**So the whole shape, end to end:**

- **While the creature lives, the wall does nothing** — occupancy is tested
  before passability, so you fight it and never learn the ground is impassable.
- **When it dies, the square vacates and the wall takes effect.**
- **And the dead creature's marker is still drawn on it** — on a square nothing
  can now reach.

**⚠ The trap I described at `018` is real and in its exact predicted form: a
thing drawn on a square that cannot be entered.** Today it costs nothing,
because a marker is all that is stranded. **The day anything is left on the
ground, it is left there permanently and the board will keep drawing it.**

---

## ⚠ `character.downed` — ZERO, IN ALL EIGHTEEN SAVES

**Nothing is emitting a state the rules no longer have — because nothing is
emitting it at all.**

`pools.dart` computes `CharacterEventKind.downed` in `applyDamage`'s
`ledgerKinds`, and `_writeOutcome` writes only `encounterEnded`, `revived` and
`died`. **`downed` is returned and dropped** — the same shape `character.died`
was in before `PT-1515`, and the same shape `check.resolved` was before
`PT-1501`.

**⚠ Instrument checked before I reported the zero** — the same reader found 158
events and both deaths in the same file.

---

## ⚠ `PT-1509` CLOSES `021`'s `character.moved` FINDING — AND MORE THAN I ASKED

At `021` I found `character.moved` declared `campaign`, read by
`play_state.dart`, and **written by nothing** — and walking to another area then
pressing `Continue` put me back at the entry.

**Now `Continue` put me back in `a03-probe-yard`, at the square I left.**
**Both the area and the position survive a quit.** The declared-and-unwritten
list is one shorter.

---

## ⚠ THE THREE NEW PIECES OF FURNITURE — DO THEY READ? YES, ALL THREE

**`PT-1517` · the budget pips.** In a fight, bottom left:

    ◆ 10  move
    ●     action
    ■     gear
    ✶     reaction · per encounter

- **They read.** Identity is carried **twice** — shape *and* word — so I never
  had to remember which shape was which.
- **`move` is a numeral because it is 10**, and the others are single pips.
  The threshold behaves as ruled.
- **`bonus` is ABSENT, not grey.** Correct, and the absence is not confusing:
  nothing suggests a missing row.
- **`reaction` is the only labelled one**, and *"per encounter"* is doing real
  work — it is the one I would otherwise have waited to see refill.
- **They sit in their own block above the working lines and cannot be
  ellipsed**, which is `BUILD 69`'s lesson applied.

**`PT-1519` · the movement remainder. This is the best of the three.**

    ◆ 9 → 7  move

Shown **standing beside** rough ground, before any step. **`9 → 7` is instantly
readable as "you have nine, that step leaves seven"**, and the arrow does all
the work. It appeared only when a rough neighbour existed and vanished when I
moved away from one. **And it taught me the cost** — rough ground is 2, which no
other surface has ever told me.

**`PT-1509` · the map.**

    map — a01-probe-room · (a03-probe-yard)

**First-visit order, current in parentheses, and only areas this character has
stood in** — `a02` and `a04` are correctly absent. **It reads**, and the
parentheses are unambiguous.

**⚠ One thing in it does not: it shows area IDs, not names.** The map says
`a03-probe-yard` while the status bar one line below says **`Probe Yard`**, at
the same moment, on the same screen. **Everywhere else in the play client a
player is shown the name.** Small, and it is the only place the id leaks.

**⚠ And one in the strike line:** `· character.died` is an **event kind name**
printed to a player, in the same breath as `killed` — the same fact said twice,
once in English and once in the vocabulary's own spelling. `017`'s F5 was the
TOML parse error and it was fixed; this is the same class.

---

## ⚠ SCOPED NEGATIVES

- **The old `revived`-after-`died` run is still in `grave-digger.sav`** from
  `022`'s build. I did not delete it and it is not evidence about this build —
  **only `probe-sentinel.probe-yard.01`'s four events are.**
- **I did not test a spent pip going grey.** I saw `move` decrement 10 → 9 and
  the reaction pip render dim, but **I never watched a bright pip turn grey**,
  so `PT-1517`'s *"shape intact when spent"* is unverified by me.
- **I did not test the pips at five budgets** — this class grants no bonus, so
  I saw four rows, never five.
- **I did not test the remainder at a cost that would go below zero**, which the
  ruling says is not shown.
- **The map was tested at one and two areas only**, never at enough to wrap or
  overflow.
- **One creature killed on this build**, in one area, at `con = 10`.
- **I did not re-check `listFor`**, still open from `021`.
- **Not touched:** the eight inert blueprint kinds, other window sizes, BG3.

---

## What this run changed

**Packages: nothing.** Both test walls were painted and removed; `diff -r`
reports **IDENTICAL**.

**Saves: one** — `grave-digger.sav`, 1129 → 1213 bytes, from playing it.
**Eighteen saves. Nothing deleted.**
