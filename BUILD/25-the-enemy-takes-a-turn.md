# 25 · The enemy takes a turn

**`KOTOR-RPG-APP` `e8fba9b`.** 197 app tests, 186 Lodestar, 101 Loom. Analyze
clean everywhere.

**Four slices of engine, and the app called `resolve` and nothing else. It
calls all of it now** — initiative, the five budgets, doctrine, the round
boundary and the dying countdown.

---

## The smallest fight

**Walking into it starts an encounter** rather than resolving one blow. The
affordance is unchanged; what it triggers is not.

A real run, from the play screen:

    initiative — you 14 · sith-trooper.command-deck.07 18
    sith-trooper.command-deck.07: rolled 18 — d20 16 + attack 2 · needed 10 — hit · 4 left

**⚠ The doctrine is scaffolding and it says so.** `plainAggression` —
`AnyEnemy`, never break off. *"Which doctrines exist is a package's business"*,
and no package authors one.

**⚠ Resolving an Action ends the turn, and the budget enforces it.** A second
attack in the same turn is **refused, not ignored**. Moving in a fight spends
**Move**, and running out says so.

**⚠ The player's vitality is derived, not invented** — `PT-648`'s formula, with
the hit die from the **class**, because `CHARACTER-RECORD-01` deliberately does
not store one and `§3` lists vitality as derived.

---

## ⚠ 1 · THE SECOND PROJECTION — a multi-round fight does NOT force it

**Ruled not forced a fourth time, and the reason is the same one:**

> `§4`: *"a round is transient state, not canon. Not written — hit/miss,
> **current vitality**, position, **whose turn it is**."*

**Everything a multi-round fight needs is on that list.** The `Encounter`
holds who is standing across turns, and it lives exactly as long as the
screen's area does. **Nothing it knows is meant to persist**, so there is
nothing to project.

**⚠ AND THE THING THAT WOULD FORCE IT IS STILL THE SAME ONE: a fight that
survives being left.** This one does not — see below.

---

## ⚠ 2 · ESCAPE — you can always leave, and there is nothing to resume

**Leaving the area discards the fight.** `Fight.abandon()` is that, named.

**`§4` wrote nothing, so nothing is lost that was meant to persist.** Quitting
the app is the same case.

**⚠ Two consequences, and both are readings:**

- **A fight can always be left**, by walking to the door. **Fleeing is not
  built** — this is what falls out of a round being transient, not a mechanic.
- **A fight can never be lost by leaving.** Walk out mid-fight, walk back, and
  the trooper is whole and the encounter is new.

**Nothing rules either.** They are stated here rather than presented as
settled — and **the second is the same wound-does-not-survive choice from slice
24, seen from the other side.**

---

## ⚠ 3 · The dying countdown works — and not the way I expected

Slice 3 built it and only a test drove it. **It has a second caller now**, and
the surprise is which direction the risk lay in.

> **I expected the round might never reach a downed combatant. The opposite is
> true: a dying combatant is NOT STANDING, so the advance skips it and wraps —
> which makes the round boundary fire SOONER, not never.**

It bleeds without anyone touching it, and **it can die mid-fight untouched** —
tested at Con 12 from −11, one advance, `character.died`.

**⚠ And a combatant who is not standing does not get a turn — the app's
reading.** `beginRound` resets **every** budget including a downed combatant's,
and `Encounter.standing` is what says who is in the fight. **The engine does
not skip; the caller does.**

---

## ⚠ THE TWO COUNTS, SEPARATELY

### Had to behave somehow — **one, unchanged**

| | |
|---|---|
| `down → dead` in one blow writes only `character.died` | **still open**, and this slice gave no new reason to change it |

**Five ruled across slices 1–3. This slice added none** — every choice it made
had a document behind it.

### Readings — **four now, two of them new**

| | |
|---|---|
| walking into something is the attack affordance | slice 24 |
| a wound does not survive leaving the area | slice 24 |
| **a fight can always be left, and never lost by leaving** | **new** |
| **a combatant who is not standing does not get a turn** | **new** |

**⚠ The distinction is holding up.** A *behaviour* is something the code had to
do and no document says which; a *reading* is a choice with a reason written
down. **This slice produced two readings and zero behaviours**, which is the
shape of a slice built on ground that has already been ruled.

---

## What was NOT built

**No targeting UI, no multiple enemies, no fleeing, no equipment resolution.**
One trooper, one player, alternating turns. **Nothing writes to the ledger** —
the kinds a crossing owes are carried on the report and dropped, because the
play screen is not a campaign.

**And the weapon is still a fist.** `CHARACTER-RECORD-01` carries equipment;
nothing resolves it.
