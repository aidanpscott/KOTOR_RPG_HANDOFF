# BUILD 93 — `PT-1581` the diagonal, and `PT-1582` the species

**1,081 green** — Lodestar 410 · Lens 7 · Loom 214 · app 337 · `+22`.

Lodestar `44dd556` · Lens `6b55219` · Loom `9df9fb9` (+pin) · app `2b5374e`.

---

# ⚠⚠ THE HEADLINE IS A CORRECTION, AND IT IS MINE

**`BUILD 91` said the diagonal cost was mine rather than read. IT WAS RULED, AND
HAD BEEN ALL ALONG.**

**`PLAYTEST-RULINGS-01:238`:**

> *"**Grid diagonals** — Ruled here: **diagonal costs 1 square**, diagonally
> touching is adjacent, and diagonal adjacency satisfies both melee reach and
> flanking."*

**One sentence carrying three rulings.** `PT-1581` took the second and third out
of it **while the first was being asked as an open question** — by me, and then
routed to research by the owner.

⚠⚠ **AND THE SEARCH BEHIND MY CLAIM WAS `design/` AND `rules/` AND NOT
`playtest/`.**

> **A scoped negative is only as wide as the shelf it read, and mine did not
> name its scope.** This corpus's own recurring defect, committed by me, **in a
> document** — where `AREA-FORMAT-01:464` asserted *"nothing in the corpus says
> whether a diagonal counts as one square or more."*

**Found by `Scholar`. Verified here rather than taken**: `grep diagonal` over
that file returns **two lines** — 117 (`PT-4`, flanking) and 238 (the ruling) —
and nothing supersedes it. **Corrected in the document and in the code**, both
of which now cite it.

⚠ **AND ONE PREMISE OF MINE WAS WRONG TOO.** I addressed the question to
"the Extractor" via the only KOTOR research session listed. **`Scholar` does not
hold RCR** — `STUDY 25 §6` and `STUDY 26 §6` say so in terms, and it
re-verified across the filesystem. **The Extractor holds it.** Corrected with
them.

---

# ⚠ `PT-1581` — A DIAGONAL IS ADJACENT, AND THERE IS ONE ANSWER

`squaresBetween` and `areAdjacent`, in Lodestar. **All eight surrounding squares
are one away**, and a square is **not** adjacent to itself — something standing
where you stand is not *beside* you, and melee, cleave and opportunity all mean
beside.

**⚠ ONE FUNCTION, BECAUSE THE FIND, THE CLEAVE AND THE STEP ASK THE SAME
QUESTION.** A project with ten instances of *a rule applied to one path and not
the next* should have exactly one answer to **"how far is that"** — so a second
measurement anywhere is now the defect rather than a variation. The app's inline
copy is gone.

**⚠ THE REASON IS CLEAVE AND IT IS OURS.** `STUDY 25` found `Cleave` is **an
attack CHAIN** in `ATTACKS-05` — level 1, 4 and 8, Strength 12 — **not a feat.**
A cleave hits what is next to you, so **what counts as next to you is a COMBAT
rule and not a geometry preference.**

**⚠ AND THE RANGE SHAPE FOLLOWS RATHER THAN BEING CHOSEN**: a range of ten is a
**21×21 square, not a circle** — asserted by counting all 441. *A player counting
squares gets the same answer as the engine*, which is the property a tabletop
projection needs and a 3D game does not.

## ⚠⚠ AND REACH AND COST ARE ONE FUNCTION ONLY BECAUSE THE COST IS ONE

`max(1, 1) = 1`, so a diagonal step costs what any step costs — **which is
exactly what `PLAYTEST-RULINGS-01:238` rules.** Asserted: **four diagonal steps
cost four, never six.**

> **Had the cost alternated — d20's 1, 2, 1, 2 — they would have had to be TWO
> functions**, because an alternating cost depends on **the path taken** and a
> reach does not. **That is in the code**, because the day someone rules an
> alternating cost is the day one function silently becomes wrong.

---

# ⚠⚠ `PT-1582` — A CREATURE HAS A SPECIES

`CharacterWriter` has taken a `species` since `PT-1490` and **no surface ever
supplied one.** Every creature `Loom` has authored is **species-less.**

**⚠ AND IT IS NOT COSMETIC.** `PT-1536` wired the species adjustment into
**every mechanical read, including vitality**, and `PT-1402` makes the SUBRACE
what resolves those values.

> **A species-less creature is an unadjusted one** — every creature `Tester` has
> ever placed.

**⚠ IT IS `PT-1533`'s SHAPE, ONE PROGRAM OVER.** There, the record was right and
**the READ did not exist.** Here, the WRITER takes a field **no surface
supplies** — *a complete path on one side with nothing on the other.*

**57 records, 22 of them subraces — a closed list, in the data, with a reader**,
which is exactly what `PT-1572` said a typed field should have had. **This one
was not typed. It did not exist.**

⚠ **The picker shows PARENTS** — `PT-1391`: *"the picker shows records with no
parent"*, filtering is a display decision and the file's job is to hold the
rules. **And the SUBRACE is what is written**, because `PT-1402` makes it what
resolves the values: writing `Aqualish` for an Aquala loses the **+4 Swim** and
the **−4 on anything built for fingers**. A parent left alone is **called out**
rather than quietly written.

⚠ **And with no `base-rules` it says the creature would be UNADJUSTED** — the
consequence, not the cause, which is what an author needs.

## ⚠⚠ AND ONE FOUND WHILE BUILDING IT: `parent` NAMES A `name`, NOT AN `id`

`aqualish-aquala` carries `parent = "Aqualish"`. **The parent's id is
`aqualish`.**

**`PACKAGE-FORMAT-01`: *"an id is the only identity"***, and `PT-1386`'s
per-record merge turns on that id. **A join on a display name is a value used as
a key** — this corpus's most-repeated defect — **and it holds today only because
all 22 differ from their parent's id by CASE ALONE.**

⚠ **The reader joins on either and does not pretend the file is clean.
Reported, not repaired**: `base-rules` is generated, and the fix belongs in the
extractor rather than in a reader that quietly accepts a name where an id was
meant. **A test exists so the day a name and an id genuinely differ is the day
something says so.**

---

# ⚠ `PlaceWayDialog` — A LESSON, NOT AN INCONSISTENCY. AND I KNOW WHICH.

**It is the lesson, and the six are the ones out of step.**

`STUDY 27` found Aurora's wizards **ask in the domain's language**; `PT-1552`
found ours **ask for the schema**. `PlaceWayDialog` asks *"where does this door
go, and what does it land on?"* — **two questions in the domain's words, with
pick-lists, before anything is written.** That is the shape `PT-1559`'s
conversation wizard was built to copy.

**⚠ And the reason it asks is structural rather than stylistic**: a doorway needs
a **target** and a **landing**, and `AREA-FORMAT-01 §4` makes a connection
landing on an undeclared arrival **a loud load failure**. `PT-1379` says the
Builder must not be able to create the fault its validator detects — **so it
could not write first and ask later.**

> **A creature can be placed without asking because a placement needs nothing
> but a square. A doorway cannot.**

**⚠ SO "place" MEANING TWO GESTURES IS CORRECT, and what is missing is the
label.** The palette offers `arrival point` and `doorway` beside blueprint names
with nothing saying that two of them stop and ask. **That is a one-line fix in
the palette when the palette is next opened — not a change to the dialog.**

## ⚠ AND THE ASSISTANT STAYS AS IT IS

*"not built yet"* is **honest**, and `PT-1341` puts the AI panel outside this
rebuild. **Recorded as settled rather than carried as an open row.**

---

## ⚠ STILL OPEN

    ⚠  what RCR says about diagonals   genuinely unknown and genuinely
                                       unasked — and it was never our open
                                       question. Route to the EXTRACTOR
    ⚠⚠ a ruling with no number         PLAYTEST-RULINGS-01:238 sits in a
                                       summary table under no PT- heading, so
                                       it is quotable by file and line and NOT
                                       BY ID. A ruling nobody can cite is one
                                       that gets re-asked
    ⚠  species `parent`                names a `name`; the extractor's to fix
    ⚠  the palette's two gestures      one line, next time the palette is open
