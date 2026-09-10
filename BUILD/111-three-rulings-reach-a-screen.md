# BUILD 111 — three rulings reach a screen, and a wipe is the party's

`PT-1636`. Four things were named and four were built, plus a correction I owe.

---

## ⚠⚠ FIRST, THE CORRECTION: `BUILD 110`'s SECOND-STATE CONCLUSION IS WITHDRAWN

`BUILD 110` said a second `PlayScreen` `State` was being created and that *"a
real player would lose their position exactly as the test does."* **That is not
supported.** Instrumenting `initState`/`dispose` shows the **unmodified,
passing** build also creates three States, each properly paired, and the failing
sequence is an **ordinary quit-and-reload driven by the test itself**:

    PS-INIT 1039563328
    ESC-B
    LEAVE-SCREEN at=Point(5, 4) area=OpenedArea
    PS-DISPOSE 1039563328
    PS-INIT 839320200

After the reload `_enter` completes correctly — `ENTER-DONE a01-command-deck
at=Point(5, 4) resume=null` — and the test's `here()` still returns null for
all 60 pumps. **So the reload is not the defect and the claim about a real
player is wrong.** The next probe is named rather than run: print `_said` inside
the walk loop and see what is occupying the status readout. All probe edits were
reverted and `whole_loop_test` is green.

---

## 1 · ⚠⚠ ONE FACT HAD TWO VOCABULARIES, AND ONLY THE DUPLICATE COULD PRINT

`strike` refused out of reach in one wording and `Fight.enemyTurn` refused it in
another, for the same rule:

    trooper cannot reach you — 6 squares, reach 1     ← enemyTurn's own
    unarmed reaches 1 square and you is 6 away        ← AttackReport.outOfReach

**The second could never appear**, because `enemyTurn` returned before `strike`
ever ran — and the player's path spent the Action first and let `strike` refuse,
which is `PT-1618`'s defect on the path it was not applied to. `strike` has two
callers and neither could reach the field `PT-1593` built.

⚠ **AND THE DUPLICATION WAS FORCED BY A RULING, NOT BY CARELESSNESS.** `PT-1618`
says out of reach is **not an Action either**, so the fight has to ask before it
spends one. **The ASKING is legitimately in two places; the ANSWER was not.**

⚠ **I built the wrong fix first and took it back out.** My first commit gave both
askers a shared sentence-builder in `Lodestar`. That is still two answerers
agreeing, and it leaves `strike`'s own refusal unreachable — **which is the
defect the ruling names.** Reverted in the next commit with the reason.

⚠ **THE SHAPE IS PEEK, RESOLVE, SPEND.** `canAct` asks whether there is an Action
without taking one, `strike` refuses or swings, and the Action is spent only once
something was resolved. `strike` touches no budget, so nothing between the peek
and the spend can fail. **Both paths now read `strike`'s answer**, and the player
gets the rule it never had.

The ratchet is not a string comparison against a literal: the case asks `strike`
for the sentence and demands `Fight.said` match it, so **a second wording added
anywhere fails**, however carefully worded.

## 2 · ⚠⚠ `DamageOutcome.line` WAS CALLED BY NOTHING IN THE APP

`AttackReport.line` printed `8 damage` — **a total with no derivation**, on the
one side of the line `PT-1326` had not been applied to. `DamageOutcome.line` has
built `damage 8 — 1d8 6 + Str 2` since combat existed and the product never
called it, so `PT-1622`'s floor clause could not appear either: `Tester` watched
vitality hold and saw **no 1d3, no damage-side Strength term and no *"not enough
to hurt"***.

    before  Vibroblade · rolled 17 — d20 13 + attack 4 · needed 14 — hit · 8 damage · 17 left
    after   Vibroblade · rolled 17 — d20 13 + attack 4 · needed 14 — hit · damage 8 — 1d8 6 + Str 2 · 17 left

⚠ **`PT-1625` — *the derivation survives the floor* — was true of `Lodestar` and
false of the screen**, which is the whole of `PT-1636`. `amount` stays as the
fallback for a report built with a total and no outcome; it is no longer the
answer.

## 3 · ⚠⚠ A WIPE IS A FACT ABOUT THE PARTY

> **Owner: with a party of one, the player going down IS a wipe. There is nobody
> left standing, and that is the loss condition. Build it as a fact about the
> party, not about the character — it will be wrong the day a companion exists
> otherwise.**

`partyIsWiped(Iterable<VitalityState>)` takes the party, and `afterAWipe` is what
kills. **`PT-1633` had left a wipe as the only thing that can kill a party member
on Easy or Normal and there was no function anywhere that could answer it** — a
ruling with a consequence and no trigger.

⚠ **The argument is the party because a party of one makes the two
indistinguishable.** A `playerIsDown` flag passes every case the product can
reach today and is wrong **silently** the first time a companion stands over a
downed player. The ratchet asserts the case the product cannot reach:
`partyIsWiped([down, standing])` is false.

⚠ **An empty party is not a wipe.** Nobody standing because nobody is there is
absence, not defeat — and it is the one place this would have handed a loss to a
screen with no fight on it.

⚠ **`PT-559` does not fire into a wipe.** `DEATH-AND-DIFFICULTY-01` carries both
halves in one sentence — *"a downed party member stands up when the fight ends;
the only true loss is a total party defeat"* — and the screen only ever said the
first. Reviving into a wipe made the loss condition unreachable, which is
exactly what it was.

Proved end to end: a Strength 20 soldier with 200 vitality against an 8-vitality
fixture writes `character.dying` then `character.died` for the player, **no
`character.revived`**, the condition reads *"the party fell here"* and the screen
says *"YOU FALL, AND NOBODY IS LEFT STANDING."*

⚠⚠ **AND IT STOPS NOTHING, WHICH IS UNRULED AND IS IN `STATE.md`.** The same test
walks a dead character into the same creature forty more times and starts a fresh
encounter on every press. **What a loss DOES is the owner's.**

## 4 · ⚠⚠ FOUR INERT KINDS WERE ONE PAGE — AND IT IS EIGHT

`Tester` compared `encounters`, `placeables`, `stores` and `triggers`: **zero
differing pixels.** Both sentences those pages print were `const` strings with no
noun in them.

⚠ **It is five, not four** — `sounds` is in the same state and was not compared.
⚠ **And the ratchet found three more.** `creatures`, `doctrines` and `items` all
rendered `none in this package` and nothing else on a fresh package, because the
pane opens on the CUSTOM tab. **Eight of ten kinds rendered one of two pages.**

⚠ **They are not eight situations.** `PACKAGE-FORMAT-01 §3` names ten folders and
defines the contents of three; five invented distinguishing sentences would be
five inventions. **What was missing was which one you are looking at**, so the
sentences carry the noun.

⚠ **I built a heading and took it out.** A `▾ stores` row fixes it and **puts the
kind's name on the pane twice, two inches apart** — the exact defect `PT-1566`
removed from this file when `doors` was both a way and a category. A selector
says which mode is selected in the MODE ROW; the page says which kind it is by
talking about it.

⚠ **THE RATCHET IS THE FIX'S SHAPE, NOT ITS TEXT**: no two kinds may render the
same page, and every page must name its kind **or the thing it paints** — read
from `paintableAsAWay`, so `doors` and `waypoints` are derived rather than
excused. A sixth folderless kind added tomorrow fails it.

⚠ **AND THE FIRST VERSION OF THAT TEST HUNG RATHER THAN FAILED.** Real `File`
futures never complete under `testWidgets`'s `FakeAsync`, and widget work cannot
happen inside `runAsync`, so the read moved to `setUpAll`. **It ate two runs
before saying anything** — worth naming: a test that hangs is worse than one that
fails, because nothing tells you which case it was.

## 5 · ⚠⚠ `species` REACHED THE SPEED AND NEVER THE ABILITIES

⚠ **The species FIELD does reach the app, and I checked before building.** An
end-to-end probe against the shipped package reads `sith-trooper species=human
speed=5 note=null kind=sentient`, so the reader, the lookup and the note are all
working.

**What never arrives is the ability line.** `CHARACTER-RECORD-01`: *"`abilities`
holds the BOUGHT scores; the modifier applies ON READ."* `PT-1533` built that
read for the PLAYER and `PT-1536` wired it into every mechanical use including
vitality — **and `combatantFrom` reads `template.abilities.str` raw.** So a
`Gamorrean` an author placed fights at `str 10` while the same species on the
player's sheet fights at `14`. `PT-1533`'s own sentence, still true one path
over: *"a Gamorrean with a bought `dex 10` fought at 10 while its sheet said 8."*

**Two of `Tester`'s placed creatures are Gamorrean** — `probe-boar` and
`probe-tusk` — which is the second creature confirming it.

⚠ **The delta is its own type because `Abilities` DEFAULTS TO TEN.** Reusing it
would make the empty adjustment `+10` to everything, silently, and a caller could
not tell a score from a delta by looking.

⚠ **Constitution is adjusted BEFORE vitality is derived**, because `PT-1536` says
the species reaches every mechanical read *including vitality*. Adjusting the
modifier afterwards is the half-applied version of this fix and it passes a test
that only looks at `constitution` — so there is a case for the pool.

⚠ **A species with no line is ABSENT from the map, not zero** — `human` states
*"None."* and does not appear. A zero entry would claim a line was read and came
out empty, which is `PT-1500`'s distinction one field over.

⚠ **Three abilities of six, and it is in `STATE.md`.** `snivvian`'s `+2 Wisdom` is
parsed and dropped, because nothing on a `Combatant` reads Wisdom.
Declared-and-read-by-nothing is a named defect here; the other three arrive with
the first thing that reads them, and the condition is watchable.

---

## Tests

`Lodestar` 480 · `Lens` 7 · `Loom` 242 · `KOTOR-RPG-APP` 382 — **1,111, green.**
Pins 4/4 level. Gate: 2 advisory warnings, both pre-existing.
