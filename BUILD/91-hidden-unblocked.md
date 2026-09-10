# BUILD 91 — `hidden` is unblocked: the find, on approach

**1,041 green** — Lodestar 403 · Lens 7 · Loom 202 · app 333 · `+59`.

Lodestar `9ef2fd2` · Lens `6b55219` · Loom `1f9178f` · app `355f370`.

**All four questions had rulings. All four are built.**

---

## ⚠⚠ 1 · THE NUMBER IS `stealth` — `PT-1568`. ALREADY SHIPPED.

Renamed at `BUILD 89`, before anything authored against `dc`. The placement
carries the **hider's total** and the finder rolls **the better of Awareness or
Alertness** against it — **an existing rule, not a new one.**

> **`SKILL-RESOLUTION-01`'s own line named the error before it was made:** *"a
> system that assumed every skill has a DC would have got three of eight
> wrong."*

## ⚠⚠ 2 · THE FIND IS ON APPROACH — `PT-1573`, AND THE DISTANCE IS OURS

**KOTOR's 250 m of player sight is 125 squares — the whole area.** It is a
constraint of a real-time 3D game **where the player owns the camera**, not an
answer about perception. `PT-1496`: **Aurora's ANSWERS transfer; Aurora's
CONSTRAINTS do not.**

    KOTOR's effective distances   10 m · 20 m · 35 m, 97.8% on the 20 m default
    RCR darkvision                20 m, flat
    RCR scent                     10 m
    §9's square                   2 metres — RCR's own unit

**`20 m ÷ 2 m = 10 squares`.** Every attested number converts **exactly** rather
than nearly, and **the default is what 97.8% of 4,397 blueprints already
carried** — the opposite of a number invented to make a rule runnable.

⚠ **AND IT RUNS AFTER ARRIVING AS WELL AS AFTER EVERY STEP**, because you walk
into a room **already standing somewhere** — a creature ten squares from the
door was never approached by a STEP.

## ⚠ 3 · ONE DEFAULT, NOT A TABLE — `PT-1571`

`range` on the placement, in squares. **No per-species table and no
per-chassis table**, ruled on data: *KOTOR had the field, had the two races, had
4,397 chances, and used it to separate droids from organics zero times.*

## ⚠ 4 · THE PRESETS — `PT-1564`. ALREADY SHIPPED, AND EXTENDED.

The seven tiers with their numbers visible, **and the file carries the
number** — nothing stores the word, so *easy* cannot disagree with 10. The
range presets follow the same rule: **`4 squares · 8 m`**, the file carries
squares, **and the metres are computed** so the two cannot drift.

---

# ⚠⚠ WHAT I CHOSE RATHER THAN READ — ONE NUMBER, AND THE CODE SAYS SO

**How a distance is measured across squares.** `§9` gives a square 2 metres and
**nothing in the corpus says whether a diagonal counts as one square or more.**

The runtime counts **the greater of the two axes**, and the reason is narrow:
**our movement has no diagonals at all**, so that is the reading that cannot
disagree with a move that does not exist. **A ruling replaces it in one line.**

# ⚠⚠ AND THE SUITE CAUGHT A FIXTURE BEFORE THE TEST DID

**Every case in `hidden_placement_test` began failing the moment the find
shipped.** The ambusher sits **one square from where the player starts** and
carried **no `stealth`** — so its total was **0 against a passive 10**, and it
was found on the first frame.

> **A fixture that was hidden only because nothing looked was never testing
> `hidden`.**

It carries a stealth total now, and two new cases test the find itself: one
found on arrival at four squares, one **never asked** because its range is one.

---

## ⚠ THE FINDER'S NUMBER IS A RANK, AND THAT IS ONE GAP WITH TWO CALLERS

`_lookAround` reads `record.skills[name]` — **exactly what
`dialogue_run._rank` already reads for a skill check.** `PT-1326`'s form is
*"rank 4 + aptitude 2"* and **the aptitude half is unbuilt in both places.**

**Taking the same route was deliberate**: a second answer to *what is this
character's number in a skill* would be a second thing to fix. **One gap, two
callers, and it closes in one edit when it closes.**

## ⚠ SETTLED ONCE — AND THE SET EXISTS ANYWAY

Passive means taking 10, which is **deterministic**, so re-asking would give the
same answer and cost nothing. `_settled` exists so that it is **not asked
again regardless**: a second evaluation with the same numbers is not a second
chance, and a screen that re-asked as the player walked closer would be **one
buff away from `PT-1501`'s free check**, where a roll retried enough times is
passed always.

**Asserted at every distance from 1 to 10.**

## ⚠ AND `PT-1440` IS SATISFIED — NOTHING ABOUT `hidden` IS EXCUSED

`hidden`, `stealth` and `range` are all in `loom_can_write_test`'s **writable**
list. My own excuse was that Loom never rewrites an entry, **and the editor
slice ended that.**

⚠ **Turning `hidden` off takes both riders with it**, because the reader refuses
a `stealth` or a `range` on something in plain sight and `PT-1379` says the
Builder must not be able to write the pair its own validator detects.

---

# ⚠ RCR'S THREE-STAGE SCENT — A SLICE OF ITS OWN, AND HERE IS WHY

    presence in range     you know something is there
    direction             FOR AN ACTION
    pinpoint within 2 m   exactly one square, the first RCR distance to land
                          on our grid with no remainder

**It is worth taking and it is not this slice.** Three reasons, in order of
weight:

**⚠⚠ 1 · IT IS NOT A FIND, IT IS A THIRD VITALITY-LIKE STATE.** *Found* and *not
found* are what `_revealed` holds. *Present-but-not-located* is a *third* state
with **its own rendering, its own effect on `_occupant`, and its own answer to
"can I attack it"** — which is `PT-1515`'s shape exactly, where a fourth
vitality state needed a ruling before it could be drawn.

**⚠⚠ 2 · `DIRECTION FOR AN ACTION` SPENDS A BUDGET, AND THE BUDGET IS RULED.**
`§1` gives a turn five counters and `PT-1540` made the turn wait for the player.
**An action that converts *presence* into *direction* is a new action**, and
`ACTION-ECONOMY-01` names what an action may be. **That is a rules question
before it is a screen.**

**⚠ 3 · IT NEEDS A SENSE, AND WE HAVE NONE.** Scent belongs to creatures that
have it — `APP-UI-VISION-01` records *"Bith identify by scent at 10 m on a DC 15
Wisdom check"* and flags that **whether all 47 species records carry a senses
line is unestablished.** A three-stage find with no way to say **who can smell**
would apply to everyone, which is not the rule.

> **What it would buy is real: a find that is not binary.** `PT-1573`'s find is
> one bit, and *"you know something is there and not where"* is the tension the
> whole feature is for.

**⚠ AND ONE THING IS CHEAP TODAY AND SITS INSIDE THIS SLICE:** the 2 m stage is
**one square**, which is already `PT-1550`'s **contact**. *Pinpoint within one
square* and *walking into it* are the same event. **The floor is already the
third stage; what is missing is the first two.**
