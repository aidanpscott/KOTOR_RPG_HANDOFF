# FINDINGS-69 — `Command Protocol`, and the `Killer's Instinct` wording

**The two items left. `§1` is the one both tests were pointing at, and the diagnosis is not what I wrote.**

---

# 1 — `Command Protocol`

## 1.1 ⚠ The expensive thing is turns, and my fix was aimed at decisions

**`PT-151`:** *"The `Droid Master` is the only class with more than one henchman, **and a henchman has its own turn**."* **And:** *"An army of henchmen is an army of turns."*

**`FINDINGS-38 §2.3` answered:** *"The problem was never the turns. It was the decisions."* **And built three clauses — one order for all, orders persist, a default when silent — to hold decision cost at one per round.**

**⚠ That was wrong, and the arithmetic says so:**

    Droid Master at tier 3        1 character + 4 henchmen = 5 turns
    a four-player party with one  3 others + 5 = 8 turns a round for 4 people

> **⚠ One player takes 62% of the round.**

**Decision cost is one per round. **Table time is five turns.** Each droid still rolls attacks, takes damage, gets targeted and moved. Collapsing the *decisions* does nothing to the *turns*, and turns are what `PT-151` named.**

**⚠ The main agent was right that two tests pointing at one class is a design signal.** **`PT-178` flagged four clauses at tier 1; three of them exist to fix a problem that was never the one that mattered.**

## 1.2 The fix — collapse the turns

> **`Command Protocol`: **your droids act on your turn, immediately after you, and take the order you give them.** One order, all droids, your initiative.**

| Tier | | Effect |
|---|---|---|
| **`Command Protocol`** | 1 | **You hold two droids. They act on your turn, immediately after you, and all follow one order.** |
| › **`Squad Doctrine`** | 4 | **Three droids**, and the order may name two tasks split among them. |
| ›› **`Master and Servants`** | 8 | **Four droids.** |

**⚠ Three clauses gone.** **Persistence and the silent-default were only needed because droids acted independently; on your turn there is nothing to persist through.**

    turns at the table    5 -> 1
    clauses at tier 1     4 -> 1
    PT-178                fails -> passes

**One line:** *Your droids act when you do, and all of them follow one order.*

## 1.3 ⚠ What this does not fix, and it is the owner's call

**`PT-151` said the arithmetic could not run the balance test on this class — *"a class whose power is measured in other people's time."*** **Collapsing the turns makes it measurable, and now that it is measurable it needs a number.**

**Four droids attacking on one turn is four attacks. `PT-153` builds them at half the Droid Master's level, so at level 20 that is four level-10 droids — plausibly 40 to 50 damage a round against Korr's `Barrage` at 27.3.**

**⚠ That is not obviously wrong for a class whose entire feature is the droids, and it is obviously wrong if the droids also attack while he does.** **Three dials, cheapest first:**

    droid level      half -> a third of the Droid Master's
    droid count      four -> three at the capstone
    droid action     all four act -> the order is one action shared among them

**⚠ I recommend the third.** **It keeps four droids on the table, which is the class fantasy, and makes them a *formation* rather than four attackers — one order, one effect, executed by however many are standing.**

---

# 2 — `Killer's Instinct` wording

**`FEATS-LIBRARY-01 §248`:** *"Granted to the three classes that carried `Sneak Attack` in the source."*

**⚠ False twice since `PT-...` added the Scoundrel: the count is four, and the Scoundrel did not exist in the source.**

> **Replacement: *Granted to the four classes built on striking an unaware target — Smuggler, Sith Assassin, Jedi Watchman, Scoundrel.***

**⚠ Naming them is the point.** **The old line described the list by its provenance and required a reader to know the source to know who was on it. `PT-190`'s failure mode was a decision whose content lived somewhere a reader would not look; this is the same shape in one sentence.**

---

# 3 — Where that leaves `PT-178`

    Quarry           fixed, FINDINGS-49    combat bonuses cut
    Dominion         fixed, FINDINGS-49    partial-success clause cut
    Read the Ruin    fixed, FINDINGS-49    rebuilt to scale one idea
    Command Protocol fixed, §1.2           turns collapsed

**All four now pass. 27 of 27 features have a one-line player statement.**

---

# The question

> **⚠ `§1.3` — four droids on one turn is four attacks. Cap the level, the count, or make the order one shared action? I recommend the third.**
