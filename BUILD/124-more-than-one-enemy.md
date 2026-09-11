# BUILD 124 — more than one enemy, and it was one list literal

`PT-1678`. The smallest change, as asked — and the premise makes it smaller
than the ruling assumes.

---

## 1 · ⚠⚠ THE ENGINE WAS NEVER THE LIMIT

`PT-1678` records *"`Encounter`'s only constructor takes exactly two
combatants."* **The constructor takes a `List<Combatant>` of any length.**

| | |
|---|---|
| `Encounter(combatants:)` | a list, any length |
| `rollInitiative` | sorts the whole list |
| `beginRound` / `endRound` | every combatant |
| `Encounter.standing` | filters |
| `Fight.current` | `combatants[turn]` — an index |
| `Fight.over` | `standing.length <= 1` |
| `Fight.advance` | already skips whoever is not standing |

> **`Encounter(combatants: [me, p.combatant])` in `_begin` was the only 1-vs-1
> thing in the product.** Tester's observation is exactly right and the cause is
> one list literal, not the engine.

## 2 · ⚠⚠ THE RULE IS CONTACT, APPLIED TO THE FIGHT RATHER THAN TO ONE CREATURE

**A creature already standing in contact with the fight is in it.** Adjacent to
you, or to the one you touched. **One hop, computed once, never a flood** — a
transitive walk would drag a corridor into a fight over a rule nobody has made.

**⚠ It invents nothing.** Walking into something is already how a fight starts;
the one you touched is adjacent to you, **so the old behaviour is this rule's
one-enemy case.** No format change, no new field, no perception system.

**⚠⚠ AND IT IS A READING, NOT A RULING.** `STUDY 31 §6` names the real gap —
*"nothing detects at range… KOTOR's default is automatic engagement at 20 m, and
ours is 0 m"* — and calls it **worth a ruling.** That is not what this is.
Detection at range would read `PT-1573`'s `range` and change how every package
plays; this only says a creature already touching the fight is in it.

## 3 · ⚠⚠ IT DELIVERS BOTH CASES TESTER COULD NOT REACH

**A creature pulled in is never TOUCHED**, so `_reveal` does not fire and **it
joins concealed.** That is the row `PT-1672` exists for, and nothing could
construct it.

**And `over` is `standing.length <= 1`**, so killing one of two leaves the fight
running — **the dead row persists on the panel with its own track**, which is
what `TEST 055` captured four frames trying to see and found the panel already
gone in all four.

## 4 · ⚠⚠ TWO CONSEQUENCES, BOTH OF THEM REACHABLE ONLY NOW

**The body stood on its square for the rest of the round.** `PT-1538` moved the
dead-leave-the-board filter from one moment to two — arrival and the end of a
fight — **and both are outside the fight.** In a 1-vs-1 the first death ends the
round, so the end-of-fight filter ran in the same tick and the gap could not be
reached. Multi-enemy opens it: the corpse blocked its square, answered
`_occupant`, and could be struck again. **The same predicate, asked at a third
moment.**

**And the board drew it again.** `character.died` is written by `_writeOutcome`
at FIGHT END, so between a killing blow and the outcome **the log cannot say the
body is gone** — and `_fallen` is log-derived. The fight knows DURING and the log
knows AFTER; they are joined in one place, which is what stopped `PT-1525`'s
regression from becoming two.

## 5 · ⚠⚠ SIDES — AND `allies` HAD BEEN FED NOTHING

`enemyTurn` built its target list as **everyone standing except me.** Exactly
right in a 1-vs-1, and **two enemies shooting each other the moment there are
two of them.**

`Role`, through `isParty` — the same predicate the party-wipe rule turns on, so
there is one answer to *which side is this* and not two.

> **⚠ And `DoctrineView.allies` stops being `const []`.**
> `WhenAlone.shouldBreak` reads `v.allies.isEmpty` and the app fed it an empty
> list unconditionally — **so a doctrine that breaks off when alone always broke
> off.** Declared, read, and fed nothing.

### ⚠⚠ And three beds were relying on the absence — one of them on the wrong rule

`Combatant.role` defaults to `Role.player`, and each of `enemy_moves_test`,
`fight_test` and `one_sentence_reaches_the_screen_test` built its trooper by
hand **without ever saying which side it was on.** Thirteen cases went red.

**The fixtures were what was wrong** — `combatantFrom` has passed
`role: Role.enemy` for every placement since `PT-1515`.

> **⚠⚠ AND ONE OF THEM WAS ASSERTING THE WRONG SUBJECT ENTIRELY.**
> `fight_test`'s dying-countdown cases bent the TROOPER into the negative band
> and watched it tick. **`PT-1524` gives an enemy no dying band at all** — *"an
> enemy dies at 0, and the band is the party's entire"*, on the evidence that
> `dying` and `bleed` appear **zero times** in KOTOR's whole API. So the subject
> was a party member wearing an enemy's name.
>
> The rule was right and the subject was wrong, and **only sides made it
> visible.** `PT-1618` says whose case it really is: *85 of 125 crossings across
> twenty saves are the player bleeding out on Normal.* Corrected, with the
> enemy's no-band half added as the control.

## 6 · A FIXTURE TESTER CAN CLICK

`~/.local/share/kotor-rpg/packages/two-enemies` — **a new package, not an edit
to a shared one.** Two droids at `1,0` and `2,0`, and a third at `1,1` that is
`hidden` with `stealth = 35` — above any passive this character can reach, so
the find on approach does not reveal it. 24 vitality each, so the fight outlasts
a blow and the bars move.

**Walk right into the first droid.** All three join; the lurker's row says
`hidden`; kill one and its row stays with the dead track while its body leaves
the board.

**⚠ A new package rather than a change to `endar-spire`**, because
`whole_loop_test`, `play_walk_test`, `wound_survives_test` and
`free_interaction_test` all walk that bed and a second creature adjacent to its
trooper would have joined their fights. `acceptance_test`'s own comment already
rules this: *"a count of a folder somebody else can write is an assertion about
the environment"* — the shelf asserts by NAME, so adding one is safe.

## 7 · `TEST 055`'s OPEN CASE — REPRODUCED, AND TESTER'S CAUSE WAS INVERTED

`TEST 055` reported that a way-placement tool on an already-placed doorway
*"correctly falls back to selecting rather than attempting a duplicate
placement."*

**It does not.** `_tap` returns unconditionally for **every** armed tool and
never looks at what is on the square. Reproduced in a test before anything was
changed:

    CONNECTIONS NOW: door.deck.01@5,2 | door.deck.10@5,2

**Two doorways on one square.** `TEST 056` reached the same conclusion
independently and self-corrected; this was already fixed by then.

### ⚠⚠ And it is not low stakes once `Place` is pressed

| | |
|---|---|
| `Loom`'s board | selects `hit.last` — **the second** |
| the play screen | `_step` takes the **first** connection on the square |
| `Lens` | draws both, identically, on top of each other |

> **An author can only reach the second and a player only ever uses the first.**
> Delete the one you can see and the one that works is still there.

**And `Verify` said *no problems found*.** `PT-1379` is *the Builder must not be
able to create the fault its own validator detects* — **no validator detected
it**, so a hand-edited file passed too. Both halves are closed:
`PackageProblem.twoWaysOnOneSquare` detects it, and `Loom` refuses it **at the
tap** rather than at `Place` — `PT-1500`, a form built to be thrown away is not
a thing that works.

**⚠ And the refusal nearly could not be read.** `_refusal` rode on the selection
bar, which only renders when something is selected — **and a way-tool tap selects
nothing.** The project's own lesson pointing the other way: *a dead-looking Loom
control is usually a refusal you did not read*; a refusal nobody can read is the
same defect with the blame moved.

## 8 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| nobody else joins *(the 1-vs-1 build)* | all three multi-enemy cases |
| the fight's dead are drawn again | the dead-row case |
| `foes` is everyone except me | an enemy targeting its own side |
| `allies` is `const []` again | `WhenAlone` |
| no occupancy check in `Loom` | the refusal, and the file |
| the refusal is not shown with nothing selected | the refusal |
| leaving does not remove *(Lodestar)* | two-ways detection |

**⚠ AND ONE GUARD HAS NO CASE, SAID RATHER THAN LEFT LOOKING TESTED.**
`_alsoInContact` refuses to enlist anyone not standing. `_here` never holds the
DEAD any more, but it can hold the DOWNED, so the guard's real case is *a downed
enemy left over from an earlier fight, adjacent when a new one starts* — which
needs a fixture that ends a fight with a survivor at exactly zero. **Removing
the guard passes the suite**, which is the honest way to say it is not covered.

## 9 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 542 | **545** |
| `Loom` | 252 | **253** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 420 | **426** |
| | 1,224 | **1,234** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 10 · Not done, named rather than skipped

- **Detection at range is not built** — `STUDY 31 §6`'s gap, and it wants a
  ruling. Ours is still 0 m; this slice only says a creature already touching
  the fight is in it.
- **Nothing decides who is hostile beyond contact and a conversation.** Two
  enemies of different factions adjacent to each other both join and both fight
  you; `FACTIONS-01` is not consulted anywhere in a fight.
- **A hidden combatant that strikes stays hidden.** Nothing reveals on being
  attacked, which is what makes the persistent row demonstrable and is probably
  not what the rules want.
- **Initiative order is still not shown**, and with three in a fight that is a
  sharper absence than it was with two.
