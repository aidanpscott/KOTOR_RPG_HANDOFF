# BUILD 97 — `PT-1589`: a creature moves its own record, in squares

**1,102 green** — Lodestar 415 · Lens 7 · Loom 214 · app 342 · `+20`.

Lodestar `2fec152` · Lens `6b55219` · Loom (pin) · app `5d2ba1a`. Pins level.

---

## ⚠⚠ THE DEFECT, IN ONE LINE

`species.toml` says **`speed = "10 metres."`**. The app parsed the 10 and handed
it to `Budgets.speed`, which `move(1)` spends **one per SQUARE**.

> **Every creature on the board moved at twice its own record.**

**Nothing was written wrong. The conversion was missing** — and 10 metres and 10
squares are the same number, so **no screen, no test and no fixture could show
it.** `PT-1490` added the species lookup and **returned the constant it replaced
for 46 of its 49 inputs.**

---

## ⚠ THE CONVERSION IS IN ONE PLACE, AND SQUARES CROSS THE SEAM

    Lodestar   squaresFromMetres(int)   the ONE place the ratio is arithmetic
    Lodestar   defaultSpeedSquares = 5  attested, not chosen
    app        speedSquaresBySpecies    converts ONCE, where the map is built
    app        combatantsIn(speed:)     defaults to defaultSpeedSquares
    Budgets.speed                       its doc now says SQUARES

**⚠ `_metres()` IS STILL `_metres()` AND IS STILL RIGHT.** It is a parser and it
parses metres out of prose. **The name was never the fix — the caller ignored
it.** A boundary is what stops that, and it is crossed once so **nothing
downstream can hold a metre.**

**⚠ AND THE DEFAULT IS ATTESTED.** 46 of the 49 species that state a speed say
10 metres; `§9` makes that **5 squares**. It replaces a bare `10` that had **no
unit at all**.

**⚠ It truncates, and that is stated rather than discovered**: no attested speed
is odd, and half a square is not a distance this board can hold.

## ⚠ BOTH SITES MOVED, BECAUSE ONE WOULD HAVE BEEN THE DEFECT WEARING A FIX

`play_screen` hardcoded `speed: 10` while `attack.dart`'s own comment admitted
*"how `speed: 10` sat hardcoded through every slice."* **The same number meant
metres in one file and squares in the next.**

The player takes **their species' squares**, and `defaultSpeedSquares` where the
species states none — **and `PT-1490`'s rule holds: absent is not five either.**

---

# ⚠⚠ THE TESTS ARE THE THREE THAT COULD EVER HAVE SHOWN IT

> **A fixture at 10 proves nothing. It is the number the bug and the fix agree
> on.**

    snivvian          8 m  → 4 squares
    droid-astromech   8 m  → 4 squares
    droid-remote     12 m  → 6 squares, HOVERING

**All three placed on a board and read through the seam** — the first fixture in
the project that could ever have seen this. **And the old values are asserted
WRONG**, so a revert is loud rather than quiet, which is precisely the property
this defect did not have.

**⚠ `droid-remote` earns its place twice.** At 12 metres hovering it exercises
**both multipliers on one budget at once** — six squares, and `PT-1513`'s
difficult ground ignored — and that is the case that was **unreadable while
speed was doubled**: at twelve squares a walker crossing six rough squares has
six left, which looks exactly like a hoverer at six.

---

## ⚠ WHAT THE BUDGET STRIP SHOWS AFTERWARDS

    before   move 10 of 10        ← a metre value drawn as squares
    after    move 5 of 5

**Both surfaces moved together, as they had to.** `PT-1519`'s remainder reads
off the same number, so *"stepping onto rough ground would leave 3"* is now
against a budget of five rather than ten — **the doubling it exists to make
visible is now a larger fraction of the budget, which is the point of it.**

**⚠ Three tests asserted the old numbers and all three were RIGHT ABOUT THE
PARSE AND WRONG ABOUT THE UNIT** — `power_target_test`'s `human → 10` and two
walk loops in `turn_waits_test`. Each carries the reason in place.

---

## ⚠ AND NOTHING HALVES A `range` — CHECKED

`PT-1576`'s `range = 10` **was authored in squares and was never a metre
value**, and its field doc says so. **Asserted in the file where the other
direction already happened**: ten squares of range reaches ten squares, and a
halved one would stop at five.

> `PT-1587`'s warning ran backwards once already. **This is the check that it
> does not run forwards.**

---

# ⚠ THE CLEAVE — UNCHANGED, AND THE FIRST MISSING PIECE IS STILL THE DATA

    0 · THE DATA        base-rules ships 320 feats and 122 chain heads and
                        ZERO named Cleave. `data/attacks.json` holds 112 rows,
                        7 mentioning Cleave, as A POSITIONAL ARRAY OF LISTS
                        with no field names — and `gen_base_rules.py` does not
                        mention `attacks` at all. **`PT-1385` named that shape
                        in `equipment.json`; this is the same defect in a file
                        nothing consumes**
    1 · A VERB          nothing on the play screen invokes a chain. The only
                        attack gesture is bumping a square
    2 · A TARGET SET    "two adjacent enemies" · "three" · "every enemy within
                        2 squares" — `_occupant(nx, ny)` returns exactly one,
                        and the app has no way to name more
    3 · THE RESOLUTION  "one declaration" is an Action and `spendAction()`
                        exists — but the −3 / −2 / −1 attack penalties and a
                        multi-target roll have no home in `resolve()` or
                        `strike()`, which take one attacker and one defender

**⚠⚠ AND `2` IS WHY `areAdjacent` IS AT ZERO CALLERS.** The only consumer that
would ever ask *"which creatures are next to me"* **does not exist** — and
*Great Cleave's "within 2 squares" needs `squaresBetween` too*, so **the cleave
is the caller that would make one function shared rather than merely alone.**

---

## ⚠ STILL OPEN

    ⚠  beast speeds       `BEASTS-*` was not read. If a beast record states
                          metres, the same seam doubles them — and beasts do
                          not go through `speedSquaresBySpecies`
    ⚠  ranges in metres   `Force Push`'s *"pushed back 4 metres — 2 squares"*
                          is the one place the corpus writes BOTH, and nothing
                          reads either
    ⚠  eight against four adjacency is ruled and movement is not. `PT-1443`'s
                          click-to-move may dissolve it — a click names a
                          SQUARE rather than a direction
