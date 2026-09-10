# 032 · It hit me from six squares — and the remainder is wrong three times in four

**From `Tester`. Unrequested number.** `PT-1512` followed: packages backed up to
`BK8/` and **saves backed up to `SV-T031/` before the app was opened**.

**⚠⚠ BUILT AND TESTED AGAINST — the only build any of this holds for:**

    app 5d2ba1a · Lodestar 2fec152 · Lens 6b55219 · Loom df15adf

**⚠ I did not build a tree being edited.** At 11:21 the app was **8 dirty** with
`play_screen.dart` at 11:18 and `turn_waits_test.dart` still moving at 11:21 —
Coder was mid-`PT-1589`. **I did every source read in `§2`–`§4` first and built
nothing until 11:27**, when all four were clean and the app's
`resolved-ref: 2fec152…` matched `Lodestar` HEAD exactly.

**⚠ And it moved again while I ran.** As I write: **`Lodestar e7a9fbd`**,
**`Loom 2f0d79f`**, app `5d2ba1a` (1 dirty). **Everything below is against what
I BUILT.**

**⚠ CONTAMINATION, declared not prevented.** Leaving the fight rewrote
`grave-digger.sav` at 11:35. **Restored from `SV-T031/` and verified byte-identical;
all 20 saves and every package file now match pre-run.**

---

# ⚠⚠ 1 · THE THING I WENT LOOKING FOR IS NOT THE DEFECT. THIS IS

**You sent me to prove a diagonal. On the fourth end-turn of that test the anvil
hit me for 3 from the other side of the room.**

`probe-anvil.probe-yard.04` stands at `6,3` and **never moved once in four
turns.** Each of my turns ended at a greater distance. Every line below is read
off the screen, with the app's own coordinate readout in the corner:

| my position | Chebyshev to `6,3` | what the anvil did |
|---|---|---|
| `5,4` | **1, diagonal** | `rolled 17 — d20 16 + attack 1` · **hit · 1 damage** |
| `5,2` | **1, diagonal** | `rolled 10 — d20 9 + attack 1` · needed 13 — miss |
| `3,2` | **3** | `rolled 11 — d20 10 + attack 1` · needed 13 — miss |
| **`0,3`** | **⚠⚠ 6** | `rolled 18 — d20 17 + attack 1` · **hit · 3 damage · 2 left** |

**Four consecutive turns, four different d20 results, so four real
resolutions** — not one line re-rendered. **`needed 13` is my own
`defence base 10 + class 3 = 13`, so each roll was resolved against me.**

> **⚠⚠ AN UNARMED CREATURE HIT ME ACROSS A TEN-SQUARE ROOM. There is no range
> check anywhere in the enemy's turn, at any of the four places one could live.**

## The four places, and each is individually reasonable

    1  fight.dart:114  enemyTurn() builds DoctrineView(self:, enemies:, allies:)
                       ⚠ and does NOT pass `distanceTo`.
    2  doctrine.dart:49  final Map<String,int>? distanceTo;
                       "⚠ CALLER-SUPPLIED, AND OFTEN ABSENT… a rule that needs
                        it and does not have it declines rather than guessing."
    3  fight.dart:210  plainAggression targets AnyEnemy() — which never asks.
    4  attack.dart:429  AttackReport strike({target, weapon, attack, defence,
                        damageModifiers, dice, kind, …})
                       ⚠⚠ NO DISTANCE PARAMETER AT ALL. It cannot refuse.

**⚠⚠ AND THE DOCTRINE DECLARES THE RANGE IT WANTS, IN THE SAME CONST.**
`fight.dart:212` — `wantRange: RangeBand.close`. **`wantRange` is written in two
places and read in none.** The creature says it wants to be close and strikes
from six.

**⚠ `Nearest` is unreachable for the same reason.** `doctrine.dart:257` — *"no
grid, no distances, no answer"* — returns `const []` whenever `distanceTo` is
null, **which is always.** `Weakest` and `AnyEnemy` work; **the one targeting
rule that needs geometry cannot fire in a running game.**

## ⚠⚠ AND THE SCREEN ALREADY MEASURED IT, FOR SOMETHING ELSE

`play_screen.dart:216` —

    final away = squaresBetween(me.x, me.y, t.x, t.y);

**That is inside `_lookAround`. The screen computes the distance from the player
to every placement in order to decide what is noticed, and hands the fight
nothing.** The map the doctrine wants is the same loop with one more line.

> **⚠ This is `030 §2`'s census with the consequence attached. I reported
> `squaresBetween` has ONE caller and called that a smell. It is not a smell:
> the second caller is missing from the enemy's turn, and its absence is a
> creature that hits from six squares.**

**⚠ Shape it wants:** `enemyTurn` already holds the placements it draws.
`distanceTo: {for (final t in _present) t.combatant.handle:
squaresBetween(...)}` fills the declared field, `Nearest` starts working, and
`strike` still cannot refuse — **so the reach check is a second, separate
decision and it has no home yet.** `PT-1581` ruled a diagonal is adjacent and
`ATTACKS-01` gives melee a reach; nothing owns *"is the target within it."*

---

# ⚠⚠ 2 · TASK 1 — I RAN IT, AND IT CORRECTS BOTH OF US

**You told me to run the fixture rather than derive it. I did, and the diagonal
is NOT the failure. A different one is, on the same widget.**

## 2a · ✅ The diagonal: no wrong number. NO NUMBER

`a03-probe-yard`, standing at **`5,4`**. The difficult block is cols 2–4, rows
2–3, so `4,3` is **diagonally adjacent** and **no orthogonal neighbour is
rough** — `4,4` and `6,4` and `5,3` are floor, `5,5` is hazard, which carries no
`moveCostSource`.

    a03-probe-yard · 5, 4        ◆ 2  move        ⚠ NO ARROW

**It did not say `2 → 1`. It said nothing**, which is what
`_afterNextStep`'s four orthogonal offsets predict.

> **⚠ AND THAT IS CONSISTENT, NOT WRONG. `_afterNextStep`'s four offsets are
> the SAME four `_step` accepts** — `030 §2` enumerated them. **A diagonal step
> cannot be taken, so a diagonal remainder would be a prediction of a move the
> keyboard cannot make.**

**⚠⚠ SO I MUST CORRECT MY OWN `031`.** I called this *"the FIRST of the three
that is silently WRONG rather than merely absent."* **It is not.** The two
orthogonal-only sites agree with each other; **this one is latent, and it goes
wrong on the day a diagonal step exists — which is the day click-to-move lands.**

## 2b · ⚠⚠ AND HERE IS THE ONE THAT *IS* SILENTLY WRONG, TODAY

**The remainder does not describe the step you are about to take. It describes
the roughest neighbour you happen to have, and a player cannot tell which.**

Measured, in one turn, with the budget refreshed to a full 5:

    a03-probe-yard · 5, 3        ◆ 4 → 2  move      ⚠ 4,3 is rough, to the WEST
      press Up  →  5,2, which is plain floor
    a03-probe-yard · 5, 2        ◆ 3 → 1  move      ⚠⚠ I HAVE 3. IT SAID 2.

**And the claim is not my reading of an arrow — the widget says it in words.**
`budget_strip.dart:180` builds the accessible name:

    label: after == null ? '$label $left of $total'
                         : '$label $left of $total, $after after the next step'

> **⚠⚠ "2 AFTER THE NEXT STEP." I TOOK THE NEXT STEP AND HAD 3.**

**At `5,3` exactly one of four neighbours is rough, so the number is wrong for
three of the four keys a player can press.** The doc comment defends it —

> *"⚠ THE DIRECTION IS NOT KNOWN AND DOES NOT NEED TO BE. `PT-1513` puts the
> multiplier on the CREATURE and the source on the GROUND KIND, so every
> difficult neighbour costs the same."*

**Every difficult neighbour does cost the same. The neighbours that are not
difficult are the ones it forgot.** The reasoning is sound about *price* and the
gap is about *which square*.

**✅ And it is right where all the passable neighbours are rough.** At `3,2` —
walls north, difficult west, east and south — it read `5 → 3` and the step cost
exactly 2. **That is the case the comment was written against.**

> **⚠ THIS IS `PT-1519`'s OWN STANDARD TURNED ON ITSELF:** *"a remainder that is
> not the square count, or the doubling stays invisible until already paid."*
> **A remainder that is wrong for three of four directions is paid before it is
> visible in the other direction.**

**⚠ Shape it wants:** it has no direction because it is a getter with no input.
Either **four values, one per arrow** — the strip already draws one budget per
row and could tint the rough ones — or **hold the last-pressed direction** and
predict that one. The first needs no new state.

## 2c · ✅ `PT-1513` and `PT-1589` confirmed in passing

**`◆ 5 move`, not 10.** `PT-1589` has landed in play: Grave Digger is human,
`species.toml` says `speed = "10 metres."`, and the strip opens at **5 squares.**
Two difficult steps west from `5,2` took 5 → 1. **Doubling charged, unit halved,
both on screen.**

---

# ⚠⚠ 3 · TASK 2 — IT IS NOT FOUR AND IT IS NOT FIVE. IT IS EIGHT, AND `PT-1554` DOES NOT EXIST

## 3a · ⚠ The citation first, because I could not verify it

**You wrote that `PT-1554` ruled gear has no verb.** I searched every tracked
file in `KOTOR-RPG-APP`, `Lodestar`, `Lens`, `Loom`, `MAIN_WORK` and `HANDOFF`:

    grep -rn "PT-1554" .      →   ZERO occurrences, anywhere

**I am not saying the ruling is wrong — I am saying I could not find it, so I
could not test against it.** `PT-1551`, `PT-1552`, `PT-1553` and `PT-1559` all
resolve in `BUILD/STATE.md`; **`PT-1554` resolves to nothing.**

> **⚠ And `BUILD/94` is titled *"a PT id must resolve to one ruling."* This is
> that check's first live miss, and it is in a brief rather than in code.**

## 3b · ⚠⚠ AND THE GLOW IS NOT HONEST. THE GEAR PIP IS BRIGHT

**Whatever ruled it, the screen does not do what you described.** `budget_strip.dart`:

    if (b.bonusGranted)       _Budget(label: 'bonus', …)      ⚠ GUARDED
    if (b.reactionsLeft > 0)  _Budget(label: 'reaction…', …)  ⚠ GUARDED
                              _Budget(label: 'gear',
                                      left: b.gearSpent ? 0 : 1, …)  ⚠⚠ NO GUARD

**Confirmed on screen for every turn of the fight: `◆ move · ● action · ■ gear`,
and the gear square is drawn BRIGHT.** Bonus and reaction are correctly absent.

> **⚠⚠ `PT-1517`'s rule is *"a grey pip is a promise."* A BRIGHT pip is a
> stronger promise — it says spend me now — and `spendGear` has zero callers in
> any `lib/` in any of the four repos. The pip has been lit in every fight ever
> played and nothing has ever been able to darken it.**

**The reasoning written on the bonus pip is the reasoning gear needs**, three
lines above it: *"an unearned slot drawn as spent is a promise."*

## 3c · ⚠ And the reaction pip is pre-broken for the day it is wired

    left: b.reactionsLeft,  total: b.reactionsLeft,

**`left` and `total` are the same expression.** Spend one and both drop
together: a pool of 2 with 1 spent draws **1 of 1**, never *1 of 2*. It is
invisible today because `highestReactionTier: 0` is hardcoded at
`play_screen.dart:1207`, so the pool is always 0 and the pip never renders.
**Two gates, and the far one is already miswired.**

## 3d · ⚠⚠ THE CENSUS, AND THE DISTINCTION YOU ASKED FOR

**Verified on clean HEADs across all four `lib/` trees. Tests excluded
deliberately** — a spender only tests reach when the product calls it.

| declared | callers in `lib/` | waiting on | what it costs to reach |
|---|---|---|---|
| `spendGear` | **0** | ⚠ **a feature** | `ACTION-ECONOMY-01 §3` names four gear categories off `baseitems.2da`. Needs an **inventory**, a **verb**, and a **target** (self or ally within reach). ⚠ **Nothing in `play/` mentions an inventory at all.** The largest of the four |
| `spendBonus` | **0** | ⚠ **a feature, and a GRANTER first** | `bonusGranted` is set true **only in tests**. Nothing in the product can grant one, so the spender is the *second* missing half. ⚠ **Two features, not one** |
| `spendReaction` | **0** | ⚠ **a feature** | Opportunity attacks. Needs the reach check `§1` shows has no home, plus a **tier source** — `highestReactionTier: 0` is hardcoded, so the pool is 0 before anything else |
| **`spendInteraction`** | **0** | ⚠⚠ **A WIRE. The app already DOES two of them** | see below |
| `areAdjacent` | **0** | ⚠ **a wire, blocked on a consumer** | correct, defined, and every consumer `PT-1581` names is unbuilt — `030 §2` |
| **`DoctrineView.distanceTo`** | **0 in `lib/`** ⚠ **supplied only by `doctrine_test.dart:114`** | ⚠⚠ **A WIRE — and it is `§1`** | the screen already measures it |
| `Nearest` | reachable, **never fires** | ⚠ **the wire above** | declines while `distanceTo` is null |
| `wantRange` | **written twice, read 0 times** | ⚠ **the reach check** | `plainAggression` says `close` and nothing asks |

> **⚠⚠ SO IT IS EIGHT, NOT FIVE — and the split is not four-and-four. THREE
> WAIT ON A FEATURE AND FIVE WAIT ON A WIRE, and the wires are all the same
> wire: THE FIGHT HAS NO GEOMETRY.**

## 3e · ⚠⚠ `spendInteraction` is the sharpest, because the app already performs interactions

**`ACTION-ECONOMY-01 §5` lists six free interactions. The play screen does two
of them, in a fight, for free:**

| `§5` says | the app | charged? |
|---|---|---|
| *"Open or close an unlocked door"* | `play_screen.dart:677` — *"Stepping onto a connection travels"* | **⚠ no** |
| *"Speak — a sentence or two"* | `_startTalk(target)` on a bump | **⚠ no** |

**The word `interaction` does not appear anywhere in `KOTOR-RPG-APP/lib` or in
`Lodestar/lib` outside `round.dart` itself.**

> **⚠⚠ AND `§5`'s SECOND SENTENCE IS UNIMPLEMENTABLE AS A RESULT:** *"A second
> interaction in the same turn costs your Action."* **Nothing counts the first,
> so a player can cross three doors and talk twice in one turn at no cost.**
> This is not a feature waiting to be built — **it is a budget that exists,
> a verb that exists, and no line joining them.**

---

# ⚠⚠ 4 · TASK 3 — THE KEY TABLE, AND THE CONSTRAINT WRITTEN AS A CONSTRAINT

## 4a · ⚠⚠ THE CONSTRAINT. `_talkKey` OWNS IT, AND IT OWNS IT ALONE

> ## ⚠⚠ A DIGIT IS NOT A BINDING WHILE A TEXT BOX HAS CONTENT.
>
> **`play_screen.dart:966`, in `_talkKey` and nowhere else:**
>
>     // ⚠ A DIGIT PICKS ONLY WHILE THE BOX IS EMPTY — otherwise "50 credits"
>     // could not be typed. The box wins once you are in it.
>     if (_typed.isEmpty && ch != null && ch.length == 1) { … _pick(…) }
>
> **Any rebinding surface must treat `1`–`9` as CONDITIONALLY bound, and the
> condition is another widget's state.** A settings screen that lists `1 · pick
> reply one` and lets a player rebind it has already broken the sentence
> *"I have 50 credits"* — and it breaks it **silently**, because the reply will
> simply fire mid-word.
>
> **⚠ THE RULE IS NOT "DIGITS ARE SPECIAL." It is that `_talkKey` claims the
> WHOLE printable range** — `ch.codeUnitAt(0) >= 32` — **and yields the digits
> back only while empty.** A rebinder that knows about digits and not about the
> printable claim will let a player bind `k` and lose the letter `k`.

**⚠ AND THE OWNERSHIP IS THE ANSWER TO YOUR QUESTION, WITH A TRAP IN IT.**
`_talkKey` owns the conditional rule — **but it is not the only handler that
takes digits, and the other one reads a DIFFERENT SOURCE:**

    _talkKey:966   final ch = e.character;              ← the text produced
    _castKey:1848  int.tryParse(e.logicalKey.keyLabel)  ← the key's label

> **⚠⚠ TWO DIGIT PATHS IN ONE SCREEN, FROM TWO DIFFERENT PROPERTIES OF THE SAME
> EVENT.** A rebinding surface that normalises to one of them changes the other's
> behaviour on any layout where they diverge — a shifted digit, a numpad, a
> non-US layout. **Untested behaviourally: Grave Digger and Blade Tester are a
> soldier and a duelist and neither can open the cast menu.** The divergence is
> a source fact; **what it does on a numpad, I did not measure.**

## 4b · The table, as it actually is

**Four handlers, and three of them are total sinks.**

| handler | reached when | keys | falls through? |
|---|---|---|---|
| **board** `:2090` | default | `←→↑↓` `F` `M` `space` `esc` | ✅ **`ignored`** on anything else |
| **`_talkKey`** `:933` | `_beat != null` | `esc` `enter`/`numpadEnter` `backspace` `1`–`9` ⚠ **conditional** · **every printable char** | ⚠ **no — `handled` always** |
| **`_castKey`** `:1839` | `_casting` | `esc` `F` `1`–`9` | ⚠ **no — `handled` always** |
| **`_refusal`** `:2016` | area failed to open | `esc` | ✅ **`ignored`**, and says why: *"a key that does nothing must not look like a key that did something"* |

**Eight named keys plus two whole classes, and the two sinks mean that while a
conversation or a cast menu is open, EVERY other binding is dead.** That is
correct behaviour and it is a hard constraint on a rebinder: **bindings are
modal, and two of the four modes swallow everything.**

**⚠ `esc` at four sites, three outcomes:** board → `_leaveScreen`, refusal →
`_leaveScreen`, talk → `_endTalk`, cast → close the menu. **`F` is a toggle
split across two handlers** — board opens, cast closes. **Neither can be
rebound in one place.**

**⚠ Rebindable without redesign:** the four arrows, `M`. **Not rebindable
without ruling something first:** `esc` (four sites), `F` (split), the digits
(the constraint above), `enter`/`backspace`/printable (a text box, not
bindings), `space` (see below).

## 4c · ⚠ "NO KEY LISTS THE KEYS" — I MUST NARROW MY OWN CLAIM

**`031` said the footer never mentions `space` or `F`. Half of that is wrong and
I should not have said it without looking at a fight.**

    footer, constant string, play_screen.dart:2304:
        arrows to move · m map · esc to leave

    ⚠ above the budget strip, ONLY during a fight, on your turn:
        space to end your turn

**`space` IS named — contextually, exactly when it becomes useful.** That is
good design and I filed it as a defect. **Withdrawn.**

> **⚠⚠ `F` IS NAMED NOWHERE. Confirmed live: I pressed it mid-fight and got
> *"you know no Force powers"* — a correct, honest refusal to a key the screen
> has never mentioned.** `PT-1478`'s own comment records how it was found:
> *"`Tester` tried nine keys before settling it in code."* **A second Tester
> would have to do it again.**

**And `M` is the reverse case — listed in the footer, useful everywhere.** So
the screen has all three behaviours at once: **listed always (`m`, `esc`,
arrows), listed when relevant (`space`), and never listed (`F`).** The middle
one is the pattern; **`F` is the only key that does not follow one.**

> **⚠ It is one line in the same footer, or one more contextual line beside
> `space to end your turn`. It is worth filing alone, and it is smaller than I
> made it sound.**

---

# 5 · Scoped negatives — where I looked and what I did NOT check

- **The range gap is measured against ONE creature with NO authored doctrine.**
  `probe-anvil` names no `doctrine` and `tester-probe` has no `doctrine/`
  folder, so it ran `plainAggression`. **I did not test an authored doctrine**,
  and `endar-spire`'s trooper is untested here.
- **I did not test whether the PLAYER can strike at range.** `030 §2` proved the
  player strikes by stepping into a square, which bounds it at 1 orthogonally —
  **but I did not re-run it on this build.**
- **The eight sentinels/wardens drawn `P`** were placeholders throughout and
  never entered the fight. **A fight with more than one live enemy is untested**,
  so `AnyEnemy`'s tie-breaking is unexercised.
- **`_castKey` behaviourally** — never opened. No character in the bed has a
  Force pool. `§4a`'s `keyLabel`-vs-`character` divergence is **a source read.**
- **Numpad digits** — not pressed, in either handler.
- **The diagonal remainder on a build with diagonal movement** — cannot exist yet.
- **`_lookAround` on approach** was not re-measured this run; `029`/`030` cover it.
- **Loom** — not opened at all. **Doors and waypoints, the item-dialog refusal
  and the free-text conversation `owner` are all UNCHECKED on `2f0d79f`**; my
  last measurement of each is `030 §4` / `028 §3–§4` on `df15adf`.
- **`PT-1582` in play** — a Gamorrean created in Loom hitting at `+4` is **still
  untested**. ⚠ **`grukk-ironjaw.sav` is a level 1 duelist standing in
  `a03-probe-yard`** and is the readiest bed for it; I did not load it.
- **Painting tiles in Loom** — still not done, **eight sessions running.**

---

# 6 · What I left behind

**Nothing. This run added no fixture and changed no file.**

    packages   ⚠ diff -rq against BK8/ → no differences
    saves      ⚠ all 20 byte-identical to SV-T031/ after restoring
               grave-digger.sav, which THIS run rewrote at 11:35

**The `a03-probe-yard` bed needed no change** — `probe-anvil.probe-yard.04` at
`6,3`, placed for `PT-1519` in `031`, turned out to be the fixture for `§1` as
well, because **a creature that never moves is exactly what proves the distance
is never read.**

**Backups: `BK3/`–`BK8/` and `SV-T031/`.**
