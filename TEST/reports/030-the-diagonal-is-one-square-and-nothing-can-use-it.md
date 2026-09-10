# 030 · A diagonal is one square, proved on a board — and nothing in the product can use it

**From `Tester`. Unrequested number.** `PT-1512` followed; packages backed up to
`BK7/` first.

**⚠⚠ BUILT AGAINST, and it changed under me twice:**

    §1–§2  app 2b5374e · Lodestar 44dd556 (pin checked, matched HEAD) · Lens 6b55219
    §3–§4  Loom df15adf     ⚠ I checked 9df9fb9 and by the time the build ran it was df15adf.
                              Still clean, so df15adf is what I tested.

**⚠ I did not build a tree being edited.** At 10:42 `Loom` was 4 dirty
(`base_types.dart` 10:41, `species_test.dart` 10:42) and the app 2 dirty —
**Coder was mid-edit on both**, so I did the source work in `§2` first and built
nothing until 10:45, when all three were clean and the app's
`resolved-ref: 44dd556…` matched `Lodestar` HEAD exactly.

**As I write: `Loom df15adf` · app `2b5374e` (1 dirty) · `Lodestar 44dd556`.**

---

# ⚠⚠ 1 · A DIAGONAL IS ONE SQUARE — measured on a board, not derived

**`029` measured Chebyshev at ten squares. This measures it at ONE, which is the
number `PT-1581` is actually about.**

## The fixture that makes the question unambiguous

    probe-warden.probe-slit.05   at 20,1   stealth 5   ⚠ range = 1

**`range = 1` means it can be noticed at distance 1 and at no other distance.**
Walking row 0 of the 64×2 slit:

| position | offset to `20,1` | Chebyshev | Euclidean | observed |
|---|---|---|---|---|
| `18,0` | dx 2, dy 1 | 2 | 2.24 | **nothing** |
| **`19,0`** | **dx 1, dy 1** | **1** | **1.41** | ✅ **"you notice probe-warden — 10 against 5"** |

> **⚠⚠ A PURE DIAGONAL OFFSET IS DISTANCE ONE. Euclidean 1.41 against a range of
> 1 would NOT have fired. It fired.**

**`PT-1581`'s *"diagonally touching is adjacent"* is now confirmed in a running
build rather than derived from a ruling.**

**⚠ And it confirms the `range` override, which `029` listed as untested.**
`range = 1` gated it to exactly one square — silent at 2, found at 1.

---

# ⚠⚠ 2 · AND NOTHING IN THE PRODUCT CAN USE IT

**You asked whether the find, the cleave and the step all ask one function.
They do not, and the reason is worse than a second measurement.**

## The census — every caller in all four repos

    grep -rn "squaresBetween\|areAdjacent" Lodestar/lib KOTOR-RPG-APP/lib Lens/lib Loom/lib

    Lodestar/lib/src/area_open.dart:297   int squaresBetween(...)     the definition
    Lodestar/lib/src/area_open.dart:305   bool areAdjacent(...)       the definition
    Lodestar/lib/src/area_open.dart:306     → calls squaresBetween
    KOTOR-RPG-APP/lib/play/play_screen.dart:216   final away = squaresBetween(...)

> **⚠⚠ ONE CALLER IN THE WHOLE PRODUCT, AND IT IS THE FIND.**
>
> **⚠⚠ AND `areAdjacent` HAS ZERO CALLERS. It is defined, correct, and used by
> nothing.**

## The six consumers `PT-1581` names, one by one

| consumer | asks the function? | why not |
|---|---|---|
| **the find** | ✅ **yes** | the only caller |
| **the cleave** | ✗ | **not implemented** — `Cleave` appears only in a doc comment |
| **opportunity attacks** | ✗ | **not implemented** — comment only |
| **`§6a` on-kill recursion** | ✗ | **no match anywhere in either tree** |
| **the step** | ✗ | **a step cannot be diagonal** |
| **melee reach** | ✗ | it is *"the square you tried to step into"* |

## ⚠⚠ The step and melee reach are the same finding, and it is structural

`play_screen.dart:588` — `void _step(int dx, int dy)` — and **its only four
call sites** are:

    arrowLeft  → _step(-1,  0)
    arrowRight → _step( 1,  0)
    arrowUp    → _step( 0, -1)
    arrowDown  → _step( 0,  1)

**Every key the play screen accepts, enumerated:**

    arrowDown arrowLeft arrowRight arrowUp backspace enter escape keyF keyM
    numpadEnter space

**No diagonal key of any kind** — no numpad movement, no QEZC, nothing.

**And the strike is `_occupant(nx, ny)` at `:599` — you attack by stepping into
the target's square.** So melee reach is exactly the four orthogonal
neighbours.

> **⚠⚠ SO A DIAGONAL IS ADJACENT BY RULING, SATISFIES MELEE REACH BY RULING, AND
> A PLAYER CANNOT STEP OR STRIKE DIAGONALLY AT ALL.**

## And I proved that half on the board too

**From `19,0` the hider at `20,1` was diagonally adjacent — `squaresBetween`
says 1, `PT-1581` says that satisfies melee reach — and I could not attack it.**
Pressing `Down` moved me to `19,1`; the creature was then **orthogonally**
adjacent and reachable. **The diagonal had to be converted into two orthogonal
facts before the game would let me use it.**

## ⚠ `areAdjacent` is the shape the ruling exists to prevent, one step early

`PT-1581`'s own commit says *"a second measurement anywhere is now the defect
rather than a variation."* **`areAdjacent` is not a second measurement — it is
an unused first one.** Defined, correct, called by nothing, so **every consumer
built after it is free to reimplement it and nothing will notice.**

---

# ⚠ 3 · CLEAVE — it cannot reach diagonally because it cannot be declared

**You asked whether it reaches diagonally. It has never met a board and it
cannot.**

**`ATTACKS-05` specifies it completely** — `§139`'s table and `§47`–`§49`:

    Cleave         Level 1, Strength 12   two adjacent enemies, Attack −3
    › Wide Cleave  Level 4                three adjacent enemies, Attack −2
    ›› Great Cleave Level 8               ⚠ EVERY ENEMY WITHIN 2 SQUARES, Attack −1

**And nothing implements attack chains.** `combat.dart:434` mentions *"a count
of chains"* in a comment; there is no chain machinery, no declaration verb, and
no key that could declare one — see the enumerated key set in `§2`.

> **⚠ So the rule the diagonal ruling exists for cannot be exercised. `Great
> Cleave`'s *"every enemy within 2 squares"* is a second `squaresBetween`
> consumer that will exist the moment chains are built — and it is the one that
> will need `areAdjacent` too.**

---

# ⚠ 4 · THE ITEM DIALOG'S REFUSAL HAS NOT MOVED. Measured, on `df15adf`

**You asked whether it has moved at all. It has not.**

Reproduced exactly: `path` prefilled `items/weapons/` (a folder, no leaf), name
empty, `Create` pressed. **Nothing was written** — the four files in
`blueprints/items/` still carry their old timestamps.

**The refusal renders in red at the very bottom of the scrolling body:**

> **"An item needs a path — where it lives IS what it is."**

**Below the entire base-type list AND below a `description` field**, while
`Create` is pinned in the action row where I clicked. **It took fifteen
scroll-wheel steps to bring it into view.**

**Identical position, identical wording, to `TEST 028 §2` and `TEST 016`.**
**Three reports, no movement.**

> **⚠ AND THE SAME PROGRAM DISAGREES WITH ITSELF ABOUT THIS.** The conversation
> wizard's action row — `back` · `Generate` · `start from an empty tree` — sits
> at the end of its pane and the outer scroll reaches it (`029 §5`). **Two
> dialogs, two answers to where an action and its refusal belong.**

---

# ✅ 5 · `PT-1582` HAS LANDED AND THE BED IS READY

**You said species was coming and my zoo would be the bed. It is in `df15adf`
(`9df9fb9` beneath it), and I looked without testing it.**

`New creature` now carries, below the abilities row:

    species
    [Aqualish] [Arkanian] [Bith] [Bothan] [Cathar] [Dashade] [Devaronian] [Droid]
    [Duros] [Echani] [Gamorrean] [Gand] [Human] [Ithorian] [Kaleesh] [Kel Dor]
    [Miraluka] [Mon Calamari] [Nautolan] [Nikto] [Quarren] [Rakata] [Rattataki]
    [Rodian] [Selkath] [Sith] [Snivvian] [Sullustan] [Togruta] [Trandoshan]
    [Twi'lek] [Verpine] [Weequay] [Wookiee] [Zabrak]

**Thirty-five, as a closed list of buttons, none preselected** — the `PT-1571`
shape a third time.

**⚠⚠ AND THE VITALITY ROW IS THE THING I ASKED FOR IN `STUDY 28`:**

    vitality die [d8]     override [0]
    derived 8 · override 0 = vitality 8
    0 — vitality derives from the die, normally

**Derived, override and result, all three on screen at once.** That is exactly
what I filed against our `override = 0` after seeing Aurora's `Calculated 2.19 ·
Adjustment 0 · Challenge Rating 2` — *"ours hides what the derived value would
have been."* **It does not any more.**

**⚠ Not tested:** whether a Gamorrean created here and placed actually hits at
`+4`. **That is the next run, and `a01`/`a04` are the bed.**

---

# 6 · Scoped negatives

- **Everything in `§2` above the board proof is a SOURCE READ**, on clean
  `Lodestar 44dd556`. I ran the diagonal find and the diagonal non-attack; I did
  **not** run a cleave, an opportunity attack or an on-kill recursion, **because
  none of them exists to run.**
- **The `Cleave` requirement `Strength 12`** — untested, since the chain cannot
  be declared.
- **A finder with non-zero Awareness/Alertness** — still passive 10 throughout,
  so `max(awareness, alertness)` has still never varied.
- **`PT-1582` in play** — looked at, not exercised. `§5`.
- **`doors` and `waypoints`** still carry both lines on `df15adf` — re-confirmed
  in passing, unchanged since `027`.
- **The problem count moved 7 → 8** on this build and **I did not chase which
  new problem appeared.**
- **Painting tiles in Loom** — still not done, six sessions running.

---

# 7 · What I left behind

**`a04-probe-slit` gains one fixture, and it is the sharpest one in the bed:**

    probe-warden.probe-slit.05   at 20,1   hidden, stealth 5, ⚠ range = 1

**`range = 1` makes it a diagonal detector**: it can be noticed from `19,0`,
`21,0`, `19,2`… and from nowhere else. **Anything that changes the distance
metric will change what this fixture does**, which is what a test fixture is
for.

The other four (`029 §7`) are unchanged, including `a01`'s
`probe-warden.probe-room.10` — `hidden` with **no stealth** — kept on purpose as
the demonstration that a find test alone proves nothing.

**Backups: `BK3/`–`BK7/`.**
