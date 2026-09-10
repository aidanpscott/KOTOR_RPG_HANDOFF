# BUILD 100 — the ranged half of `§6.2a`, and the thing that moves an enemy

**1,144 green** — Lodestar 441 · Lens 7 · Loom 214 · app 360 · `+24`.
Lodestar `fc32da0` · Lens `5534554` · app `919b55d`. Pins level.

---

# ⚠⚠ FIRST, A CITATION OF MINE THAT DOES NOT RESOLVE

`BUILD 99` said *"`§10` puts −2 per range increment"*, and `reach_test.dart`
carried the same sentence, and the brief for this slice repeated it back to me.
**`§10` is opportunity attacks.** The range rules are `§6.2a — Range, PT-163`.

> **An artifact-versus-summary failure in a report whose subject was a rule
> nothing applied** — the second time in this project I have named a section
> from memory in a document about citations that do not resolve. Corrected in
> the code and in the test, both of which now say `§6.2a`.

---

# ⚠⚠ THE INCREMENTS — AND THE COLUMN WAS ALREADY IN THE FILE

`equipment.toml` carries `range = "28 m"` on every ranged base type. It sits
**between `damage` and `threat`, and `weaponFromBase` read both of its
neighbours and not it.**

    12 ranged base types · 4 distinct values — 16 m, 24 m, 28 m, 40 m
    read by: nothing, ever

That is **a rule authored, stored, shipped and ignored** in its strongest form
so far: not a field nobody wrote, a field somebody wrote, extracted, generated
and installed, one column over from two that were read on the same line.

    within one increment      no penalty          §6.2a
    each further increment    cumulative −2       and the warrant is
    beyond three increments   cannot be attempted SKILL-RESOLUTION-01's ladder

**Metres in, squares out, at the reader** — `PT-1589`. `rangeSquaresFrom` is the
only place a range string becomes a number, it goes through `squaresFromMetres`,
and nothing downstream of a `Weapon` sees a metre. **Nothing rounds**: 16, 24, 28
and 40 are all even, checked rather than assumed, so `§14` still does not bite.

**Absence is null and never zero.** Null means *this weapon states no
increment* — the ceiling answers it. Zero would mean *it reaches nowhere*.

## ⚠⚠ AND THE THIRD RUNG IS UNREACHABLE, WHICH IS A FINDING AND NOT A BUG

`§6.2a` states two limits and they are not the same limit. Three increments, or
`:297`'s 48 metres — 24 squares. **Whichever bites first is the answer, and it is
almost always the ceiling:**

    short  8 sq   three increments = 24   the ceiling exactly — the only tie
    medium 12 sq  three increments = 36   ceiling first
    long   14 sq  three increments = 42   ceiling first

> **So *"beyond three increments cannot be attempted"* never fires for anything
> but a sidearm, and the `−4` tier is reachable only with a short-band weapon.
> The ladder is written as three rungs and is, in squares, two.**

Asserted as a case, so the day a band changes something says so.

## ⚠⚠ AND `§6.2a`'s OWN SQUARES TABLE DISAGREES WITH `§13.1`

The same section says **"`§13.1` is the authority on bands. This section does not
restate them"** — and then restates them, wrong:

    §6.2a  "pistol 11 squares | to 23 −2 | to 34 −4"
    §13.1   medium band = 24 m = 12 squares

`11` is `23 ÷ 2` — the **raw** `maxattackrange`, not the snapped 24 — and
`23`/`34` are `46 m` and `69 m` halved **tier by tier rather than once.** That is
`PT-1589`'s defect surviving in the corpus rather than in the code. **And its top
tier, 34 squares, is past its own section's 24-square ceiling.**

**I have not touched `rules/`.** The code reads the shipped data and `§13.1`, and
nothing reads that table. ⚠ **The Marksman Rifle is 40 m — twenty squares — and
`§13.1` has no band for it**, while `ITEMS-01:675` marks it *"Range increment
×2"*, which `28 × 2 = 56` does not equal. Two more for whoever owns the corpus.

---

# ⚠⚠ POINT BLANK, WHICH I BUILT WITHOUT BEING ASKED — AND ITS COUNTERPART

    firing a ranged weapon while adjacent to an enemy      −4 attack
    attacking an adjacent enemy who holds a ranged weapon  +2 attack

Same section, same distance, same defect: stated numbers applied nowhere. **I
built both, and building one would have been the defect I am here to fix** —
`§6.2a` prices them as one exchange (*"a 6-point swing, decisive without being
absurd"*) and reprices `Close Combat` against the pair.

**⚠ THE `+2` IS A READING AND IS LABELLED ONE.** The clause says *"attacking"*
with no qualifier; its own heading says *"the melee-against-ranged bonus"* and
`FEATS-LIBRARY-01` reduces *"the +6 an enemy gets for engaging a ranged fighter
in melee"*. So it is the blade's bonus for closing, not one gunman's over
another. **A gunman gets no bonus against a gunman — both are already taking the
−4.**

## ⚠⚠ AND IT CHANGED THE BED'S FIGHT, WHICH THE OWNER SHOULD KNOW ABOUT

`turn_waits_test` began failing. **Both sides of the test bed hold blaster rifles
and the app has no way to attack except by walking into something** — so every
attack in the product is adjacent, and every one of them now takes the `−4`.
The player's `d20 16` became a `12` against `needed 14`, missed, took the
trooper's return fire for 9 and the fight ended inside round one.

> **The rule is right and the assertion was incidental.** That case's subject is
> `PT-1540` — the turn waits for you, the enemy answers on your key — and it
> now checks that and not a second round. **But the balance consequence is real
> and it is not mine to decide:** until something can shoot from a distance,
> `−4` is a permanent tax on every gun and the `+2` is unreachable, because
> nothing holds a blade. Say the word and it gates behind a flag.

---

# ⚠⚠ `PT-1543` APPLIED TO A MODIFIER RATHER THAN A REFUSAL

*"A player who cannot see the reach and the distance cannot tell a rule from a
bug"* was my own sentence about a refusal, and the brief was right that it
applies to a `−4` identically.

The penalty is **a `Term` with its source** — `PT-1326` — so it appears in the
derivation without anything printing it on purpose:

    Blaster Rifle · rolled 12 — d20 16 + Dexterity 0 − point blank 4
                    · needed 14 · 1 square, increment 14 — miss

**The distance is on the line, not in the term's name.** `PT-1326` settled that
sentence and said *"embellishing it here is how two things end up shown in one
shape"* — so the cause rides on `AttackReport.rangeNote`, beside the reach and
ability clauses, where a fact about the situation already lives. **And the MISS
carries it too**, because a shot that missed *because* it was two increments out
is the case a player most needs the number for.

---

# ⚠⚠ THE THING THAT MOVES AN ENEMY

## What the doctrine actually decides — two decisions, in an order

**They are not one decision.** Targeting answers *whom*; `wantRange` answers
*where I should stand relative to them*. **No value of `wantRange` can change
which enemy is chosen, and no targeting rule needs a position it does not
already have as a distance.** `Nearest` is the one that looks like a
counterexample and is not — it is a TARGET rule that reads a distance, not a
POSITION rule.

So `decide` stays grid-free (`§3`: *callable without a game*, and `DoctrineView`
carries distances and no board), and the second decision runs after it, where a
board exists. **One decision would have dragged a grid into the layer whose
whole point is not having one.**

## ⚠ AND ONLY ONE OF THE THREE BANDS HAS AN ANSWER

    close    the distance at which my weapon is at its best
    medium   nothing states one
    long     nothing states one

*"At its best"* is **two attested numbers rather than one invented one**: a
blade's is `§15`'s reach; a gun's is `§6.2a`'s first increment, *"within one
increment — no penalty"*. **It is a reading and it is labelled one.** What it is
not is a table of distances nobody wrote.

**`medium` and `long` decline and say which band could not be answered** — the
same discipline `Nearest` uses with no distances. They are real values a doctrine
file may carry; they are **unbuilt rather than unwanted.**

## ⚠ `RangeBand` IS NOT `§13.1`'s BANDS, AND BOTH ARE short / medium / long

`§13.1` classifies a WEAPON by how far it shoots. `RangeBand` classifies a
DOCTRINE by where it wants to stand. **Two taxonomies, nearly the same three
words, neither naming the other.** Worth knowing before someone joins them.

## The walk

`approach` — greedy Chebyshev descent over `PT-1588`'s eight offsets, priced
through the same `Budgets` the player spends from, `canAfford` then `move` in
that order because *"with one point left, a step onto difficult ground would
have been half-paid and taken."*

**⚠ IT IS NOT A PATHFINDER AND DOES NOT PRETEND TO BE.** A wall between two
creatures ends the approach. Nothing in the corpus states a pathing rule, and A*
here would be inventing a rule about what a creature knows about a room. **The
stall comes back as a sentence**, and *out of movement* and *blocked* are two
different sentences, because a player watching a creature stop wants to know
which.

**⚠ AND CHEBYSHEV TIES CONSTANTLY.** Every step toward something four squares
away is *"three away"*, so with no second key the walk from `(0,0)` to `(3,0)`
**drifted off the row and arrived at `(2,−1)`** — right distance, ridiculous
path. The tie-break is the off-axis gap, so a creature lines up while it closes.
`PT-1588` rules the DISTANCE; **which of two equally-close squares a creature
prefers is not ruled, and this is the one that does not look like a bug.**

## ⚠⚠ AND OUT OF REACH IS NOT AN ACTION EITHER

`enemyTurn` spent the Action and then let `strike` refuse. **A creature that
closed and came up one square short paid for a swing it never made** — `§1`
spends the Action on *resolving* one. Invisible until now, because the distance
could not change inside a turn. It asks the same `reachSquares` that `strike`
refuses with: one rule, two askers, the shape `canAfford` and `move` already
have.

## ⚠⚠ AND A TOKEN IS DRAWN WHERE IT STANDS

`ENGINE-SPEC-04 §4` lists **position** among the things a round does not write,
so a creature that walks has moved and the file has not. `movedTo` on
`paintAreaBoard` — **the same seam and the same argument as `PT-1550`'s
`concealed`**, and Loom passes nothing because in the Builder there is no round
and the file IS the truth.

**Three surfaces had to agree**: `Lens`'s token, the play screen's marker over
it, and `_occupant`. **The marker's own comment named that pair as the one a rule
gets applied to half of, and it had happened to the position two lines later** —
`Lens` was being told where a creature walked to while the marker still read the
file. `_squareOf` is now the one answer to *where is this placement.*

## ⚠⚠ AND THE BED CANNOT SHOW IT UNCHANGED

**The one authored doctrine in the corpus is `sith-line.toml`, it says
`want_range = "close"`, and its trooper holds a blaster rifle** — so `close` is
fourteen squares and it is already there on a board twelve wide. **The mover
changes nothing about the bed's own fight**, and that is correct: a gunman does
not need to close.

So the screen case edits **one line** of a copied shelf — `PT-1346` — and removes
the trooper's rifle. Unarmed is melee, reach one, and it has to come to you.
**You back away two squares, you press space, and it follows and swings.**
Verified by breaking the wiring and watching the case fail.

---

# ⚠ EIGHT VERSUS FOUR IS LIVE NOW, AND IT IS NAMED RATHER THAN SOLVED

**An enemy approaches on all eight. The player still has four keys.**

I did not give the enemy four to hide it — `PT-1588` rules the diagonal, and
building to a known-wrong rule to conceal an asymmetry is worse than the
asymmetry. **What I did instead was make it one list.** `stepOffsets` (eight) and
`orthogonalStepOffsets` (four) are declared together in Lodestar, a test asserts
the second is a subset of the first, and `_afterNextStep` reads the four from
there rather than from its own literals.

> **So it is a keyboard gap and not a second rule.** `PT-1443`'s click-to-move
> dissolves it; four more bindings would too, and that is a keyboard decision
> and not mine.

---

# ⚠ WHAT I DID NOT BUILD

- **`Close Combat`** — `+1` within one increment, and its tiers reduce the `+2`.
  Feats do not reach a strike yet.
- **`Snap Shot`** — `§6.2a` names it as the Reaction answer to the `−4`.
- **Grenades** — `§6.2a`: 24 metres, twelve squares, **and no increments at all**.
  Nothing throws one.
- **`medium` and `long`** — no distance in squares exists to build.
- **Opportunity attacks** — the player backed away from an adjacent enemy in the
  new screen case and nothing happened. `§10` is unbuilt, and **that is what
  `§10` actually says.**

# STILL OPEN, FROM BEFORE

`spendGear` still at zero callers, with the pip saying so · the cleave's five
missing pieces, data first · beast records have no extract, no table, no reader ·
`§14`'s rounding, an open question its own document cites as ruled ·
`species.parent` names a name, not an id.
