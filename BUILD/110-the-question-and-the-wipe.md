# BUILD 110 — the question answered, and only a wipe kills

Lodestar `e1a837c` · app `47789fa` · Loom `776e42e`.
Lodestar 470 · Lens 7 · Loom 239 · app 374 — **1,090 green.** Pins level.

---

# ⚠⚠ THE QUESTION, ANSWERED WITH EVIDENCE AND NOT A THIRD ATTEMPT

**Why does extending `main._log` before its own `await` break travel?**

## It is not a stall. The player never reaches the door.

    ENTER a01-command-deck   OPENED   RENDERED
    ENTER a01-command-deck   OPENED   RENDERED
    (no ENTER for a02-starboard-hold, ever)

`_enter` is never called for the hold. **Travel is not slow or hung — the walk
stops.**

## And it stops because keys arrive at a `PlayScreen` that has just been born

    STEP -> 5,4
    KEY state=273802314  area=OpenedArea  at=Point(5, 4)
    INIT state=1022988577
    KEY state=1022988577  area=Null  at=null
    KEY state=1022988577  area=OpenedArea  at=Point(5, 4)

**A SECOND `PlayScreen` State is constructed mid-fight** — `initState` runs, it
re-enters the ENTRY area from scratch, and the keys the test is sending go to
it. `_step` early-returns on `at == null` **with no sentence**, which is
`PT-1610`'s finding one screen over.

## ⚠⚠ SO IT IS THE PRODUCT, NOT THE HARNESS — and that is the answer asked for

The queue's failure looked like fake-async because every append still completed;
**this one has a print of `initState` running twice.** A widget test cannot
manufacture a second `State`; the tree does. **An extra `setState` on
`_HomeState` during play can destroy and rebuild the play screen**, and a real
player would lose their position exactly as the test does.

**⚠ WHAT I HAVE NOT ESTABLISHED is why the widget loses identity** — `_where`
does not change and `PlayScreen` sits at one position in a `switch` inside
`WidgetsApp`'s `builder`. That is a Flutter-tree question and it is the next
thing, **not something to guess at while touching the save path.**

> **`PT-1265` guarantees CONTENT and says nothing about two writers. A save
> rewritten WHOLE means every append is a read-modify-write** — and the narrow
> fix closed the one pair that exists, not the class. **Every future writer
> inherits it.**

---

# ⚠⚠ `PT-1633` — ONLY A WIPE KILLS

    Easy     0 and below → down          no band, no death
    Normal   0 → down, below → dying     the band, and no death
    Hard     −Constitution → dead        untouched
    enemy    0 → dead, always            PT-1524 untouched

## ⚠ AND I REMOVED IT FOR ALL THREE ON THE FIRST PASS

The ruling says *"there is no individual death threshold on EITHER
difficulty"* — **Easy and Normal.** `Hard` is a third difficulty the ruling
never mentions, and its own section is that **no ROLE is distinguished** —
nothing there says nobody dies. Caught by the suite; restored, with a case.

## ⚠⚠ AND `partyStandsAtOne` HAD TO BE RENAMED, WHICH IS THE INTERESTING PART

It had **one caller**, and that caller is `PT-559`'s *"on Easy, damage below 0
is not tracked at all"* — a statement about the FLOOR, not about standing up.

> **The two came apart the moment the wipe rule landed.** Standing back up is
> something every party member now does on both difficulties; flooring at zero
> is Easy's alone. **A predicate meaning both would have been true in one place
> and wrong in the other** — and it would have floored a Normal character at
> zero, deleting the band `PT-559` keeps.

`zeroIsTheFloor(mode, role)`, named for what it does.

## ⚠ AND THE ASYMMETRY THE AMENDMENT COMPLAINED OF IS GONE

`PT-571` gave a henchman the Easy rule on Normal, and the amendment removed it
because it made *"the two companion classes the only ones playing without a
stake."* **Nobody has an individual stake now; the party has one and it is the
whole of it.** A case asserts player and henchman land in the same state.

## ⚠⚠ AND THE DYING COUNTDOWN ON NORMAL IS NOW A CLOCK WITH NO TERMINUS

It ticks, it never kills, **and what ends it is the fight resolving.** *"It can
die untouched mid-fight"* is `Hard`'s case now, and both halves are asserted.

---

# ⚠⚠ TWO THINGS I AM ASKING RATHER THAN CHOOSING

**1 · Can an ally help a downed character up mid-fight, and what does it cost?**
`PT-559` says they can on Easy, `§1` gives a turn five counters, and **there are
no allies in the product.** `−Constitution` is recorded as that boundary and
**nothing reads it** — a number kept doing nothing is better than a number
quietly repurposed, which is how `crithitmult` came to be read as a threat
range.

**2 · With a party of ONE, is the player going down a wipe?** *"If the entire
party dies then everybody dies"* — and today the entire party is one person. **A
wipe is a fact about the party that `stateOf` cannot see**; it takes one
character and its own numbers. **I have not implemented it**, and the case says
so rather than guessing.

---

# ⚠ AND WHAT THE DROPPED BLEED-OUT COSTS — asked, and measured

`Fight.advance()` returns the round-end kinds and **both call sites drop the
return value**; one of them already says so in a comment.

    Easy, Normal   nothing at all after PT-1633 — the countdown produces no
                   deaths there, so the dropped value carries none
    Hard           the MOMENT, not the FACT

**`_writeOutcome` still catches it**: it emits `died` for anyone `_isDead` at
fight end, guarded by `_hasDied` against duplicates — **and `_leaveScreen` calls
the same thing, so a quit mid-fight is covered too.**

> **`PT-1611`'s test passes: every effect has its cause.** What the log cannot
> say is that *nobody struck the blow* — the death is recorded per FIGHT rather
> than per CROSSING, which is `PT-1421`'s shape and is the same reason `died`'s
> site is still wrong and still not mine to move.

---

# ⚠ AND I HAVE BEEN KILLING `Tester`'s PROGRAMS TOO

`pkill -f bundle/loom` is what I have used to restart Loom all week, and it
matches every Loom on the machine. **`Tester` found it and fixed its own half; I
had not looked at mine.** The display and the process table are shared.

**Stopped.** Keep the PID from `nohup`, kill that PID, never `pkill`. If a Loom
of yours vanished this week, some of those were mine.

---

# STILL OPEN

**Why a second `PlayScreen` State is constructed** — the next thing, and what
the general `_append` fix waits on · the `_append` race for every pair that is
not a fight-ending blow · `died`'s writer at the outcome · whether an ally can
help, and whether one person going down is a wipe · `PT-1634`'s
what-you-keep-between-fights · the drawn icon set · the two deferrals in
`STATE.md`.
