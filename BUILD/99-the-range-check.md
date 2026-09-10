# BUILD 99 — the range check, the remainder, and the free interaction

**1,120 green** — Lodestar 416 · Lens 7 · Loom 214 · app 349 · `+16`.
Lodestar `0cd34bb` · app `df36271`. Pins level.

---

# ⚠⚠ `PT-1593` — SIX SQUARES, UNARMED, WITHOUT MOVING

**`strike` had NO DISTANCE PARAMETER AT ALL.** There was nowhere for the check
to live **even if someone had thought to write it** — and `enemyTurn` could not
have passed one, because **the fight has never held positions.**

> **Every previous instance of the declared-and-uncalled family was inert. This
> one was a player losing vitality to a creature across the room, and it had
> been true since the fight was built.**

    reach       §15   "an ordinary weapon threatens 1", a reach weapon 2
    ranged      :297  "48 metres — 24 squares — the absolute maximum for any
                      ranged attack regardless of increments"
    lightsaber        one, and it is a READ: §4b quotes the source saying
                      "lightsabers are not melee weapons", which is why it is
                      its own kind — and it is still a blade you swing at what
                      is next to you

**⚠ `distanceSquares` IS REQUIRED, so a caller cannot forget it**, and it gates
**both sides** because both come through the same `strike`. A reach rule applied
to one of them would be the shape this corpus has found eleven times.

## ⚠⚠ AND OUT OF REACH IS NOT A MISS

It **does not roll**, so there is no `needed 13` to print and no die is touched.
**A miss is a swing that failed; this is a swing that could not be taken** — and
reporting it as a miss would be a third channel carrying two meanings.

**The line says both numbers**: *"unarmed reaches 1 square and sith-trooper is 6
away."* **A player who cannot see the reach and the distance cannot tell a rule
from a bug**, which is exactly how six squares went unnoticed.

## ⚠ AND `wantRange` IS READABLE NOW AND STILL UNREAD, WHICH IS THE HONEST HALF

`DoctrineView.distanceTo` is populated — its own doc said *"caller-supplied and
often absent… there is no grid in this slice"*, **and there is a grid.**

**⚠ THAT DOES NOT MAKE `wantRange` READ.** A doctrine that wants to be *close*
has to be able to **move**, and **nothing in the fight moves an enemy.** The
field is readable; the rule that would read it is unbuilt, and I am not calling
that fixed.

**⚠ AND THE INCREMENTS ARE NOT BUILT.** `§10` puts **−2 per range increment**
over three, and nothing applies it — **a shot at twenty squares is as accurate
as one at a square.** Asserted in a test, so the gap is visible rather than
assumed away.

---

# ⚠⚠ `PT-1594` — THE REMAINDER MADE A CLAIM ABOUT THE PLAYER'S NEXT KEY

It scans four neighbours and **returns on the first that costs extra**, and the
player presses whichever they like. At 5,3 the strip read `4 → 2`; **`Tester`
stepped onto plain floor and had 3. Wrong for three of the four keys.**

**Its own comment said *"the direction is not known and does not need to be."***
It does.

> **The number was right about ROUGH GROUND and wrong about *"the next step"*.**

So the claim moved rather than the number: the label reads **`4 if the next step
is onto rough ground`**, which is true whichever key is pressed. **`PT-1519`'s
purpose is untouched** — the doubling is still visible before it is paid.

**⚠ And `Tester` withdrew its diagonal claim, rightly.** `_step` binds four
offsets, so a diagonal neighbour gets **no arrow at all** rather than a wrong
one — **latent, not silently wrong**, and it goes live the day `PT-1588`'s eight
squares get keys.

---

# ⚠⚠ `PT-1554` WAS MINE AND IT WAS WRONG

**I ruled the glow honest by reasoning about the END-TURN PROMPT. `Tester`
checked THE PIP.**

    bonus      guarded by `bonusGranted`
    reaction   guarded by `reactionsLeft > 0`
    gear       ⚠ GUARDED BY NOTHING, and `spendGear` has zero callers

> **`PT-1517` outlawed a GREY pip because a grey pip is a promise. A BRIGHT one
> is a stronger promise.**

**⚠ AND IT IS NOT HIDDEN, BECAUSE `§1` GIVES A TURN A GEAR ACTION.** The bonus is
absent when nobody granted one — *the pool does not exist.* **This pool exists
and the VERB does not**, which is a different sentence and gets one:
`gear 1 of 1, nothing spends it yet`, on the label, **where a shape cannot carry
it.**

---

# ⚠⚠ `PT-1596` — AND `spendInteraction` WAS THE SHARPEST, SO IT IS WIRED

`§5`: *one free interaction per turn* — **draw or stow · open or close an
unlocked door · drop · pick up · hand over · speak** — and **"a second
interaction in the same turn costs your Action."**

**The app already did two of the six mid-fight and charged for neither.**

> **The rule could not be broken because nothing counted the first one.**

    stepping onto a connection   §5's door
    starting a conversation      §5's speak

**Both spend it now.** The second costs the Action **and says so**; the third is
refused with the reason. **A budget that disappears without a sentence is how
`PT-1537` went unseen for four reports.**

**⚠ Spent BEFORE the conversation file is read**, because a refusal must not
depend on whether the file loads — *the interaction is the act of speaking, not
the act of finding something to say.*

---

## ⚠ AND `PT-1595` IS ACCEPTED WITH NOTHING TO DO

Nothing states truncation, `§14` is an open question with two candidates, and
`:1012` cites `§14` as if it had ruled. **The rounding stays** — every attested
speed is even in both tables, so the question does not reach a speed.

---

## ⚠ STILL OPEN

    ⚠⚠ `wantRange`        readable and unread. It needs an enemy that can MOVE
    ⚠⚠ range increments   −2 per increment, ruled in §10, applied nowhere
    ⚠  `spendGear`        still zero callers; the pip says so rather than
                          lying. Three of the eight wait on a feature
    ⚠  eight against four `_step` binds four keys and `PT-1588` rules eight
