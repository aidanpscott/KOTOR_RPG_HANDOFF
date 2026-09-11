# BUILD 126 — a wipe ends the fight, and the detection was already right

`PT-1683`, owner ruling. `TEST 057`.

---

## 1 · ⚠⚠ THE WHOLE BUG IN ONE LINE

```dart
bool get over => encounter.standing.length <= 1;
```

**That is a LAST-ONE-STANDING rule, not a loss condition.** With a party of one
down and **two** enemies alive it is `2`, so nothing was over — and `TEST 057`
watched the consequence: *"a dead player kept moving. The encounter never
resolved."*

```dart
bool get over => partyWiped || encounter.standing.length <= 1;
```

## 2 · ⚠⚠ AND THE DETECTION HAD BEEN RIGHT THE WHOLE TIME

`partyIsWiped` has been **party-shaped since `PT-1636`** and returns true for a
lone downed player. `_partyWiped` reads `isParty`, not the player's handle. The
owner's own sentence was **already quoted in its doc comment**:

> *"With a party of one, the player going down IS a wipe. There is nobody left
> standing, and that is the loss condition. Build it as a fact about the party,
> not about the character."*

**It was consulted by exactly one caller — `_writeOutcome` — which runs when the
fight is already over.**

> **The wipe decided what a loss LOOKED like and never decided that one had
> happened.**

⚠ This is not the ruling arriving late to unbuilt code. It is a **correct
derivation wired to the wrong question**: the outcome writer asked *how did this
end*, and nothing asked *has this ended*.

## 3 · ⚠ ASKED OF THE PARTY, AND ASKED ONCE

The ruling is explicit about why the subject matters:

> *"It must read party-size, not 'is this specific combatant the player', or it
> will be wrong the day a companion exists and the player alone going down is no
> longer the whole party."*

`Fight.partyWiped` folds `isParty(c.role)` — the project's one answer to *which
side is this*, the same predicate `PT-1678`'s targeting uses.

**⚠ And the screen's copy is gone.** `_partyWiped(f)` was a second fold over the
same list; the moment `Fight.over` needed the answer they would have become
**two answers to one question** — the fight deciding it was not over while the
outcome writer decided the party had been wiped. It now reads `f.partyWiped`.

**⚠ An empty party is not a wipe** — `partyIsWiped`'s own guard, `PT-1636`.
Without it a fight built entirely of enemies would be born over.

## 4 · ⚠⚠ THE OTHER HALF OF `TEST 057` — MOVEMENT OUTSIDE YOUR TURN WAS FREE

> *"Position updated on arrow-key presses with no attack and no move-counter
> decrement… an input path with no combat gate rather than intentional
> behaviour."*

```dart
if (f != null && f.playersTurn) {
  if (!f.player.budgets.canAfford(1, ground)) { … return; }
  f.player.budgets.move(1, crossing: ground);
}
```

**Everything else fell through to the free move below it.** So while it was an
enemy's turn the player walked the board at no cost.

> **⚠⚠ THE GATE WAS WRITTEN AS A PRICE AND READ AS A PERMISSION.** It answered
> *what does this cost* and nothing ever answered *may this happen* — the same
> shape `PT-1596`'s toll had one program over, where a door spent an interaction
> it had not checked for.

`ACTION-ECONOMY-01 §1` gives a **turn** five counters, so a step outside one is
not a cheap step — **it is a step the economy has no price for.** Refused, with
a reason, rather than priced at zero.

### ⚠ How the dead player got a turn that never came back

`advance` returns when `standing.contains(current)` — **a downed combatant is
skipped forever.** `_enemyTurns` loops while it is not the player's turn, caps
at eight, and exited with the fight permanently on an enemy's. That is the state
`TEST 057` was standing in, and the wipe fix is what makes it unreachable.

## 5 · ⚠ AND THE SYMPTOM IS CLOSED AT THE INPUT TOO

`PT-1642` already gives the game-over panel the keyboard — *"a key that still
walked you around behind it would be offering one"*. So once the wipe resolves
the fight, the panel opens, the board goes inert, and *"a dead player kept
moving"* is closed at the outcome **and** at the input. Both are asserted.

## 6 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| a wipe does not end the fight *(the bug, restored)* | both fight cases and the end-to-end |
| the wipe asks about the CHARACTER, not the party | `IT IS THE PARTY, NOT THE CHARACTER` |
| movement outside your turn is free again | **nothing — §7** |

**⚠ AND ONE OF MY OWN CASES WAS A CONDITIONAL THAT ASSERTED NOTHING ON THE
BRANCH IT TOOK.** I wrote a play-level test for the movement refusal that
branched on whose turn it was and, on the branch it actually reached, asserted
`mine.current` is true — which is the condition it had just tested. **Removed,
not weakened**: a conditional case that asserts nothing on the branch it takes
is worse than no case.

## 7 · ⚠ The movement guard has no case, and here is why

With the wipe fixed, **the keyboard cannot reach an enemy's turn.**
`_enemyTurns` runs synchronously from `_begin`, `_endTurn` and `_playerStrikes`
and loops until it is the player's turn, so no frame that accepts input sits on
somebody else's. `TEST 057` reached it only because the fight never ended.

**The one path that could still reach it is `_enemyTurns`' eight-iteration cap**,
which exits mid-round in a fight with nine or more enemies — and `PT-1678`'s
adjacency rule cannot assemble that many from this bed's corner. Named in the
test file beside the case it replaces.

## 8 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 545 | **545** |
| `Loom` | 253 | **253** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 436 | **441** |
| | 1,244 | **1,249** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 9 · Not done, named rather than skipped

- **`_enemyTurns`' eight-iteration cap is still there**, and it is now the only
  way to leave a fight on somebody else's turn. It exists to stop a runaway
  loop; with nine or more combatants it silently truncates a round. **Named, not
  changed** — what it should do instead is a rules question.
- **A down-but-not-dead party member has no case**, because a party of one that
  goes down is a wipe and a wipe kills. It arrives with the first companion.
- **Nothing tests a fight that ends while the player is DOWN rather than DEAD.**
  `afterAWipe` makes that impossible today; `PT-559`'s revive is the path that
  would exercise it.
