# BUILD 95 — adjacency is eight and movement is four

**1,082 green** — Lodestar 410 · Lens 7 · Loom 214 · app 338.
app `3942e39` · HANDOFF `0864116`.

---

# ⚠⚠ FIRST — I ASSERTED A CITATION I HAD NOT CHECKED

`BUILD 94` closed with *"`PT-30` is the one I would look at first, **because
`ACTION-ECONOMY-01` cites it**."*

> **It does not. Nothing cites `PT-30` anywhere, bare or backticked.**

**That is the artifact-versus-summary failure, in the one sentence that mattered
most** — the sentence recommending where to look. I named a citation from
memory of what `ACTION-ECONOMY-01` is about, in a report whose whole subject was
citations that do not resolve.

⚠ **The reasoning stands and the fact did not.** *"No action in round 1"* and
*"surprise removes the round"* are different rules rather than different
wordings — **and that is why it would have mattered, not evidence that it did.**

⚠⚠ **AND `PT-1583` ANSWERS THE QUESTION: NO.** `PT-30`, `PT-31`, `PT-32` and
`PT-1085` are cited in **zero** documents. `PT-29` and `PT-484` once each, **both
about the half that is not in dispute.**

> **The six are a hazard, not a bill.** The ratchet stops a seventh.

---

# ⚠⚠ DO THE FIND, THE CLEAVE AND THE STEP SHARE ONE FUNCTION? NO — AND TWO OF THE THREE DO NOT MEASURE AT ALL.

    the find     the ONLY caller of `squaresBetween`
    the step     takes `(dx, dy)` from four arrow keys and CONSTRUCTS a
                 destination. It never measures — and no diagonal key is
                 bound, so a diagonal step CANNOT BE TAKEN
    the cleave   ⚠⚠ DOES NOT EXIST. `ATTACKS-05` has the chain — level 1, 4
                 and 8, Strength 12 — and nothing in Lodestar, Loom or the
                 app implements it. `grep cleave` returns my own comments
    the strike   reached only by bumping `_occupant(nx, ny)`, so melee reach
                 is **"the square you tried to walk into"** — one square,
                 orthogonally, never measured

> **So *"it must be one function"* is satisfied VACUOUSLY: one measurement, one
> caller. That is not three callers agreeing, and I would rather say so than
> report a rule as honoured because nothing contradicts it.**

## ⚠⚠ AND THE CONSEQUENCE IS FINDABLE TODAY

**A creature diagonally beside you can be NOTICED and cannot be REACHED.** Not
walked into, not spoken to, not struck — because `_step` is bound to four keys.

    adjacency   EIGHT, by PT-1581
    movement    FOUR, by the board

**The ruling landed on the one path that measures and not on the three that do
not** — *a rule applied to one path and not the next*, the eleventh instance,
**and this time the rule is newer than the paths.**

⚠ **The test asserts the GAP, not a fix.** Binding diagonal movement is a
play-surface change nobody has asked for, and it touches the move budget, the
difficult-ground doubling and every existing walk fixture. **The day it is
bound, this case fails and says the two were out of step.**

---

## ⚠ AND THE OTHER THREE WERE ALREADY IN — `BUILD 93`

    the diagonal cost   PLAYTEST-RULINGS-01:238, corrected in AREA-FORMAT-01
                        §3c and in `squaresBetween`. My claim of corpus
                        silence had searched design/ and rules/ and NOT
                        playtest/
    species             picked from 57 shipped records; the picker shows
                        PARENTS and writes the SUBRACE, and a parent left
                        alone is called out. ⚠ And `parent` names a NAME
                        rather than an id — a value used as a key, holding
                        only because all 22 differ by CASE ALONE
    PlaceWayDialog      ⚠ THE LESSON, and the six are out of step. It asks in
                        the domain's words because a doorway NEEDS a target
                        and a landing, and §4 makes a bad landing a load
                        failure — PT-1379 means it could not write first and
                        ask later. A creature can be placed without asking
                        because a placement needs nothing but a square

**⚠ `Tester`'s zoo is the bed for the species work** — and a Gamorrean placed in
Loom now carries one, so it will hit like one the moment the fight reads it.

---

## ⚠ STILL OPEN

    ⚠⚠ eight against four   adjacency is ruled and movement is not. Whether
                            the board gains four keys is the owner's, and it
                            costs the move budget, the difficult-ground
                            doubling and every walk fixture
    ⚠  the cleave           ruled in `ATTACKS-05`, implemented nowhere. It is
                            the reason `PT-1581` was decided, and it is the
                            one caller that would prove the function shared
    ⚠  six ambiguous ids    a hazard, not a bill — `PT-1583`. `PT-484` is
                            still where the near miss is
    ⚠  line 238             still has no number
