# BUILD 98 — beast speeds, and the corpus that had already written the answer

**1,104 green** — Lodestar 416 · Lens 7 · Loom 214 · app 342 · `+2`.
Lodestar `e7a9fbd` · app + Loom pins level. **No new product behaviour.**

---

# ⚠⚠ THE HEADLINE IS A CORRECTION TO `PT-1589`, AND IT IS TWO CORRECTIONS

## 1 · THE CORPUS STATED THE DEFAULT BEFORE I DERIVED IT

**`ACTION-ECONOMY-01:1012`:**

> ***"Base speed is 10 metres — 5 squares."***

`PT-1589` worked that number out from **46 of 49 species records** and `§9`'s
ratio. **The document had already written it, in those words, and the code had
10.**

> **It was not a missing rule. It was A STATED RULE NOTHING READ.**

## 2 · AND THE ROUNDING IS UNRULED — I WROTE THE OPPOSITE

`PT-1589` said truncation was *"stated rather than discovered."* **Nothing
states it.**

`ACTION-ECONOMY-01 §14` is **an open question with two candidates** — *"round
down… round up… **it should be one of them consistently**"* — and the document's
**own blocker table** lists *"how odd-metre radii round"* as **a ruling still
owed.**

**Truncation is round-DOWN — one of the two, picked by me before I knew §14
existed.**

⚠ **What saves it is that nothing rounds today.** Every attested speed is even
in **both** tables — species give 10, 8, 12; beasts give 10, 12, 16, 4 — so the
open question **does not reach a speed**. `§14` bites on RADII, and its own
preferred fix is *"restate the affected radii in even metres."*

⚠⚠ **AND `:1012` CITES `§14` AS IF IT HAD RULED** — *"rounded up under `§14`"* —
**while `§14` says it has not.** A clause asserted rather than checked, **inside
one document, about itself.**

---

# ⚠⚠ BEAST SPEEDS — THE DEFECT IS NOT LIVE, AND THE REASON IS WORSE

**Checked end to end. A beast cannot reach the seam, because a beast cannot
reach the engine at all.**

    BEASTS-ENTRIES-01     24 entries, each stating `speed 16 m` and the like
    data/extracted/       ⚠ NO beast extract. None.
    base-rules/rules/     ⚠ NO beast table. None.
    every .dart file      ⚠ NOT ONE reads a beast record

**So nothing doubles a beast's speed, because nothing gives a beast a speed.**

## ⚠ AND YOUR PREDICTION ABOUT VISIBILITY WAS EXACTLY RIGHT

    10 m   12 entries
    12 m    8 entries
    16 m    3 entries
    4 m     1 entry

**Half of them are not at the modal value.** Where `PT-1589` was invisible
because 46 of 49 species agreed, **a beast defect would have been loud from the
first fixture** — an Iriaz at 16 metres becoming 16 squares is *32 metres*, more
than twice a cannok.

## ⚠⚠ AND THE SEAM IS ALREADY THE WRONG SHAPE FOR THEM

`speedSquaresBySpecies` is **keyed by species id, and a beast is not a species
record** — checked: no beast name appears in `species.toml`. A beast placed
today would miss the map and take `defaultSpeedSquares`, **five squares,
whatever its entry says.**

> **When beasts arrive they need either to become species records or to get a
> second lookup — and a second lookup is a second place a metre can cross.**
> The boundary exists now; **the thing to guard is that the beast extractor
> emits squares rather than that a second consumer remembers to convert.**

⚠ **I did not build a guard, because there is nothing to guard yet** — no
extractor, no table, no consumer. **A test cannot assert about a path that does
not exist**, and the honest artefact is this paragraph rather than a green check
over nothing.

---

# ⚠ THE BOTH-UNITS CENSUS: IT IS A CONVENTION, NOT AN ACCIDENT

**Fourteen sites state both units, and thirteen are in `ACTION-ECONOMY-01`** —
the document that owns the square.

    §9      "Square size: 2 metres"        the ratio itself
    :250    4 metres — 2.5 squares         ⚠ and it says they DO NOT land clean
    :252    "Corrected to 4 metres — two squares. PT-165."
    :297    48 metres — 24 squares
    :317    24 metres — twelve squares
    :744    "a 3-metre radius is one and a half squares"
    :758    "a reach weapon threatens 2 squares — 4 metres"
    :1012   "Base speed is 10 metres — 5 squares"
    :1021   "Force Push, which pushes 4 metres"
    CHARGEN-DATA-01:214   "pushed back 4 metres — 2 squares"   ← the outlier

**⚠ `PT-1587`'s label was already a convention before the rule existed**, and
`:252` shows it working: *a value was CORRECTED to land on a square, and the
correction carries a ruling number.*

**⚠ AND THE ONE OUTSIDE `ACTION-ECONOMY-01` IS THE ONE YOU FOUND.**
`Force Push` is quoted in `CHARGEN-DATA-01` — a document about EXTRACTION —
which is why it reads as careful rather than conventional. **It is the
convention travelling, and it travelled into the document that decides what
becomes data.**

---

# ⚠ `PT-1592` — AND IT CORRECTS SOMETHING I WROTE

I cited *"`§6a`'s on-kill recursion"* as part of the cleave's reason. **They are
two different mechanics and I had been citing them as one.**

    d20's Cleave     an ON-KILL RECURSION — drop an enemy, get a free swing
    ours             A SWEEP. "One motion, two bodies" — two at once, killing
                     nothing. Level 1, Strength 12; three at 4; every enemy
                     within TWO SQUARES at 8

**⚠ AND IT MAKES ADJACENCY LOAD-BEARING RATHER THAN THEORETICAL.** *Eight versus
four is the difference between a cleave that catches a flanker and one that does
not* — so `PT-1588`'s adjacency clause is not a tidiness rule, **it is the rule
that decides who gets hit.**

**⚠ AND `Great Cleave` IS THE SECOND CALLER `TEST 030` SAID DID NOT EXIST** —
*"every enemy within 2 squares"* needs `squaresBetween` for something other than
the find.

## ⚠ AND IT IS FIVE THINGS, NOT THREE — `Tester` was right

    0 · THE DATA          320 feats, 121 chains, none of the attack chains
    0b · AND THE SHAPE    ⚠ `feats.toml` COULD NOT HOLD CLEAVE ANYWAY — no
                          ability-requirement field for "Strength 12", and
                          `effect` is PROSE for all 320. **The record shape is
                          the blocker, not the rows**
    1 · A VERB            nothing invokes a chain
    2 · A TARGET SET      `_occupant(nx, ny)` returns exactly one
    3 · THE RESOLUTION    −3 / −2 / −1 and a multi-target roll have no home in
                          `resolve()` or `strike()`

**THE DATA COMES FIRST, and `0b` says the data is not merely missing — the place
it would go cannot hold it.**

---

## ⚠ STILL OPEN

    ⚠⚠ §14's rounding    an open question CITED AS RULED by its own document.
                         Nothing rounds today; the day an odd metre value
                         reaches a speed, `squaresFromMetres` picks one of the
                         two by default rather than by ruling
    ⚠  beasts            no extract, no table, no reader. The speeds are in
                         metres and half of them are not modal, so it will be
                         loud when it lands — which is the good case
    ⚠  `feats.toml`      cannot express an ability requirement or a structured
                         effect. Blocks the cleave before any code does
