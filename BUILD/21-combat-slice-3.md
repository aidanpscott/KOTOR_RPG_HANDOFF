# 21 · Combat slice 3 — the round

**`Lodestar` `16b5593`.** 161 Lodestar tests, 182 app tests, analyze clean.
**The app still does not call combat.**

---

## ⚠ Three reset boundaries, not one

`§1`'s five budgets, and the spec's own sentence is the design: *"the engine
does not design this. It enforces it. Every budget is a counter that resets on
a known boundary."*

    MOVE · ACTION · BONUS · GEAR · free interaction     every TURN
    REACTION                                            every ENCOUNTER

**⚠ The reaction pool is the one a naive implementation gets wrong.** Refilling
it per round **would delete the decision it exists to create** —
`ACTION-ECONOMY-01 §4`: *"a character who spends reactions on opportunity
attacks has none left to parry."*

**And a reaction does not check whose turn it is.** That is the whole point of
one, so `spendReaction` deliberately ignores `turnOver`.

### Two rules that only bite when they meet

- **⚠ Resolving an Action ends your turn.** Which is *why* move is splittable
  **around** the action rather than after it: four metres, a Strike, and the
  other six are gone. **Asserted by spending the leftover and getting zero.**
- **⚠ A Bonus exists only when something grants it** — not *unspent*, **absent**
  — and the grant does not survive the turn either.

---

## ⚠ Initiative was ruled, so there is no stop

`ACTION-ECONOMY-01 §9`: **d20 + Dexterity modifier, once per encounter, no
re-rolls.** `PT-96` closed class modifiers and `PT-74` refused a flat bonus
because *"every class wants it"* — the Smuggler got `Quickdraw` instead, and
the Scout, which had the better claim, got nothing.

**Surprise came with it and is budget-shaped**, so it belongs to this slice:
*"no move, no Action, no Bonus, no Gear, and no reactions until their first
turn would have ended."*

---

## ⚠ The dying countdown — slice 2's first automatic caller

`§6b`: a dying character **loses 1 per round**. A round exists now.

> **⚠ A CHARACTER CAN DIE WITHOUT ANYONE ATTACKING THEM.** The countdown calls
> `applyDamage`, the crossing writes `character.died` exactly once, and the
> test drives it two rounds from −1 to dead with nothing else happening.

**It does not run on `Easy`**, because dying does not exist there — `PT-559`.

---

## ⚠ The two things carried forward from last report

### The second projection — **this slice does NOT force it**

A round needs to know who is standing. **`§4` makes that transient**, so the
encounter answers from its own combatants and **nothing about a round survives
it.** `PLAY-STATE-01`'s projection is owed for state that outlives a fight, and
nothing here does.

**Not built, and the reason is a rule rather than a schedule.**

### Healing past `max` — **the round did not surface it**

Nothing in a round heals. The countdown only decrements. **It stays unclamped
and stays visible**, as reported.

---

## ⚠ WHAT HAD TO BEHAVE SOMEHOW — the count

**One in slice 1, three in slice 2, and one here. Five.**

| Slice | | |
|---|---|---|
| 1 | a tie in an opposed roll | **ruled at `PT-1420`** — to the defender |
| 1 | critical confirmation | **ruled at `PT-1420`** — none |
| 2 | healing past `max` | open. Unclamped for vitality, deliberately visible |
| 2 | negative damage as healing | open. One operation, simplest reading |
| 2 | `down → dead` in one blow | open. One crossing, one event |
| **3** | **a tie in INITIATIVE** | **open. Holds the order it was given in** |

**⚠ The new one is a tie again, in a different place** — and that is the shape
worth noticing. `PT-1420` ruled the opposed-roll tie; **nothing rules the
initiative tie**, and a stable sort keeping declaration order is a choice made
by whoever wrote the sort rather than by anyone deciding.

**It matters more than the opposed-roll tie did**, because initiative order is
**shown on every player's screen** — `APP-UI-VISION-01`: *"one shared,
objective order, identical on every player's screen, since initiative is a fact
of the fight."* **A tie broken by declaration order is a fact about the array
the caller passed in.**

---

## What was NOT built

**No enemy decisions** — `§6`'s *"real question"*, and the round exists first so
that it can be tested when it comes. **No targeting, no grid, no screen.**

**The app does not call combat and did not start.** `resolve`, pools and the
round are a library nothing in the play screen uses.

**No `Ready`, no opportunity attacks, no reaction chains.** The pool is
counted; **what spends it is `ATTACKS-01`'s and not this slice's.**
