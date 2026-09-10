# BUILD 96 — the metre census, and what the cleave is missing

**A census, not a build. No product code changed.**

Checked against Lodestar `44dd556` · Lens `6b55219` · Loom `9df9fb9` · app
`3942e39`. All five repos level with `origin/main` before I started.

---

# ⚠⚠ IS THERE ONE FUNCTION THAT CONVERTS METRES TO SQUARES? NO — AND THE PLACE THAT SHOULD CONVERT DOES NOT CONVERT AT ALL.

**The ratio appears in five places. Four are prose. One is arithmetic. NONE of
them is at the seam where a metre value crosses into the engine.**

    Lodestar/area_open.dart:237      a comment  — "§9 makes one square 2 metres"
    Lodestar/area_open.dart:326      a comment  — "20 m ÷ 2 m = 10 squares"
    Lodestar/area_open.dart:676      a refusal  — "§9 makes one square 2 metres"
    Loom/area_tab.dart:541           ARITHMETIC — '$n squares · ${n * 2} m'
    Loom/area_tab.dart:553           ARITHMETIC — defaultPerceptionSquares * 2

**Both real conversions are in Loom, both are DISPLAY, and both go the other
way** — squares to metres, so an author who thinks in metres can read a squares
field. **That direction is right and it is not the direction that matters.**

## ⚠⚠ AND THE FINDING IS A LIVE DEFECT: `Budgets.speed` IS FED METRES AND SPENT IN SQUARES

    species.toml           speed = "10 metres."          ← the source's unit
    records.dart _metres() → 10                          ← still METRES; the
                                                           function is named for
                                                           what it returns
    attack.dart:225        final own = speedBySpecies[sp]
    attack.dart:239        speed: own ?? speed           ← crosses into Budgets
    round.dart             moveLeft = speed              ← now SQUARES
    play_screen.dart:667   budgets.move(1)               ← one per square stepped
    budget_strip.dart:75   total: b.speed                ← drawn as "move 10 of 10"

> **A species whose record says 10 METRES is given 10 SQUARES — twenty metres.
> Every creature on the board moves at twice its own record.**

**⚠ NOTHING IS WRITTEN WRONG. THE CONVERSION IS MISSING**, and the numbers are
the same magnitude, so nothing looks wrong anywhere.

**⚠⚠ AND IT IS INVISIBLE BY CONSTRUCTION: 46 of the 49 species that state a
speed say 10 metres.** `PT-1490` added the species lookup and **changed no
observable number for 46 of 49** — the two at 8 m and the one at 12 m are the
only records that could ever have shown it, and none of them is in the bed.

**⚠ The player's own is worse and already flagged**: `play_screen.dart:1189`
hardcodes `speed: 10` with a comment one file over admitting *"how `speed: 10`
sat hardcoded through every slice."* **It has no unit at all.**

## ⚠ AND `PT-1587`'s OWN WARNING IS THE PROPHECY, RUN BACKWARDS

> *"Without the label somebody later HALVES a number that was never doubled."*

**The reverse has already happened: somebody USED a number that was never
halved.** The label would have stopped both.

**⚠ `PT-1576`'s `range = 10` is the one that is RIGHT**, and it is right because
the field's own doc says *"SQUARES, NOT METRES, because the file is read by a
grid"*. **The rule that a natively-square value must say so is already earning
its keep in the one place it was applied.**

## ⚠ WHY I DID NOT FIX IT

The ask was a census. **And the fix is not one line**: halving speeds changes
`move 10 of 10` to `move 5 of 5`, changes what `PT-1513`'s difficult-ground
doubling costs against, and re-baselines **every walk fixture in the app**. It
is a play-balance change wearing a units bug.

**The seam is one place** — `attack.dart:239`, where `own` crosses into
`Budgets` — **and `speedBySpecies` should return squares, with `_metres` kept as
the parser it is.** That is the shape; the decision is the owner's.

---

# ⚠⚠ THE CLEAVE — AND THE FIRST THING MISSING IS THE DATA

**The framing was *"the chain is in the data"*. It is not.**

    ATTACKS-05:47   Cleave — Level 1, Strength 12, two adjacent enemies, −3
    ATTACKS-05:48   › Wide Cleave — Level 4, three adjacent, −2
    ATTACKS-05:49   ›› Great Cleave — Level 8, every enemy within 2 SQUARES, −1

    base-rules/feats.toml    320 records · 122 chain heads · ZERO named Cleave
    data/attacks.json        112 rows, 7 mentioning Cleave — A POSITIONAL
                             ARRAY OF LISTS, no field names
    gen_base_rules.py        does not mention `attacks` AT ALL

> **The extract exists, has never been given field names, and has never
> shipped.** `PT-1385` named that shape in `equipment.json`: *"a positional
> array whose meaning lives only in a prose column order."* **This is the same
> defect in a file nobody has looked at, because nothing consumes it.**

## So the gap is FOUR things, not three

    0 · THE DATA        the chain is not in `base-rules`. Until it is, there is
                        nothing for a verb to invoke
    1 · A VERB          nothing on the play screen invokes a chain. The only
                        attack gesture is bumping a square
    2 · A TARGET SET    "two adjacent enemies", "three", "every enemy within 2
                        squares" — the app has no way to name more than one
                        target, and `_occupant(nx, ny)` returns exactly one
    3 · THE RESOLUTION  "one declaration" is an Action and `spendAction()`
                        exists — but the −3 / −2 / −1 attack penalties and a
                        multi-target roll have no home in `resolve()` or
                        `strike()`, which take one attacker and one defender

**⚠ AND `2 · A TARGET SET` IS THE ONE THAT NEEDS `areAdjacent`.** `TEST 030`
found it at **zero callers**, and this is why: **the only consumer that would
ever ask *"which creatures are next to me"* does not exist.** *Great Cleave's
"within 2 squares" needs `squaresBetween` too* — so the cleave is the caller
that would make one function shared rather than merely alone.

---

## ⚠ AND `PT-1588` IS RECORDED

`AREA-FORMAT-01 §3c` and `squaresBetween` both cite `PLAYTEST-RULINGS-01:238`
by file and line. **They can cite `PT-1588` now**, and I will change them the
next time either file is open rather than touching them for a citation alone.

**⚠ The flat 1 holds, and the argument for it is the same one that makes the
range a square rather than a circle**: *a player counting squares gets the same
answer as the engine.* **Under alternation that becomes false** — the answer
depends on how many diagonals you already spent this turn, which is a number
only the engine is holding.

---

## ⚠ WHAT THIS CENSUS DID NOT COVER

    ⚠  beasts            `BEASTS-*` speeds were not read. If a beast record
                         states metres too, the same seam doubles them
    ⚠  powers and items  anything with a range in metres — `Force Push`'s
                         *"pushed back 4 metres — 2 squares"* is the one place
                         the corpus writes BOTH, and nothing reads either
    ⚠  the 112 rows      I counted them and read one. Whether the 7 Cleave rows
                         are the chain or mentions of it, I did not establish
