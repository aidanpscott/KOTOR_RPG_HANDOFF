# FINDINGS-51 — lightsaber forms become feats. ⚠ Two adopted things break.

**Owner: three forms by levelling, the rest taught. Lightsaber forms become **feats** that *"mostly serve as unlocks for attacks."*** **Force forms deferred.**

---

# 1 — The three levels are already in the source

**⚠ Not authored. Every granted class chain in `feat.2da` uses the same three levels:**

    jgd   FORCE_JUMP · ADVANCED · MASTERY              1 / 6 / 12
    jsn   FORCE_IMMUNITY_FEAR · STUN · PARALYSIS       1 / 6 / 12
    jcn   FORCE_FOCUS · ADVANCED · MASTERY             1 / 6 / 12

> **Three grants at 1, 6 and 12 is what this game does when a class gives something three times.**

**So: **forms at 1, 6 and 12**, and everything beyond taught.** **⚠ This supersedes `FINDINGS-32 §3.2`, which gave two at 1 and 5 on an argument I made up.**

**Which three:**

    level  1    Determination      universal — "the form every initiate learns"
    level  6    the class form     Guardian Perseverance · Sentinel Resilience ·
                                   Consular Moderation · Warrior Ferocity ·
                                   Inquisitor Moderation · Assassin Contention
    level 12    any not held       player's choice

**⚠ The third is chosen rather than granted, because by 12 a player knows which attacks they want and the ruling makes forms *unlocks for attacks*.**

---

# 2 — ⚠ *Feat* removes the exclusion, and that breaks two things

**`FORMS-01 §2`: forms are conditions in an exclusion group — one active at a time. A **feat** is a permanent capability. The two do not coexist.**

## 2.1 `ATTACKS-06`'s central claim stops being true

**`ATTACKS-06`:** *"A Jedi in Resilience has **six** of these entries available, not forty-two."* **And:** *"Switching forms is the cost of switching attacks, which makes the form choice a decision every encounter rather than a one-time pick."*

    holding 1 form     6 lightsaber entries available
    holding 3 forms   18

**⚠ Under the ruling it *is* a one-time pick, three times. The sentence that justified the whole roster's size no longer holds.**

**That is not an objection — it is the design changing, and the owner's reason is that the KOTOR 2 version was bland. But `ATTACKS-06` needs the line struck rather than left to contradict the rule.**

## 2.2 ⚠ The Sith Battlemaster's class feature evaporates

**`Master of Forms`, adopted: *tier 2, you hold two forms at once; tier 3, switch freely.***

> **If every Jedi holds three forms permanently, holding two is not a class feature. It is below average.**

**⚠ This is the more serious of the two. The Battlemaster is drafted, priced, given a `Combat` rate specifically to support it, and adopted.**

## 2.3 The fix that saves both, and it is one sentence

**Split the form into the two things it currently is:**

> **The **feat** unlocks the form's attack chains, permanently. The **stance** is which form's bonuses you are currently in, and you are in one at a time.**

**Then:**

**`ATTACKS-06`'s access arithmetic holds for *bonuses* and relaxes for *attacks*** — which is what *"unlocks for attacks"* says.
**The Battlemaster survives unchanged** — holding two **stances** is still unique, because everyone else holds one.
**`FORMS-01 §2`'s exclusion group survives**, applied to the stance rather than the feat.
**And the feat cost I invented in `FINDINGS-32` becomes correct rather than wrong** — a form is a feat now, so it costs one.

**⚠ It is one sentence and it preserves three adopted things. But it is a design call and it is the owner's.**

---

# 3 — What being taught means, unchanged

**`ATTACKS-06 §1` names the routes:** *"a master, a holocron, an enemy who teaches by defeating you."*

**A form learned beyond the three costs **one feat** and requires one of those events.** **The feat is the price, the event is the permission, and neither alone suffices.**

**⚠ Now consistent rather than invented: under the ruling a form *is* a feat, so charging one is the ordinary cost of a feat rather than a price I made up.**

**Precedent stands — `ATTACKS-01 §14` on the Echani chain, *"the only thing in the corpus a GM grants on a narrative event rather than a level."*** **Forms are the second.**

---

# 4 — Force forms: not building

**Owner: *"Forms, on the other hand, should be something else and I haven't decided what yet."***

**⚠ Not drafting. `FINDINGS-47` is what happens when I build beside an undecided system.**

**What is settled and worth having in front of the decision:**

    FORMS-01 §2.1   a separate exclusion group from lightsaber forms
    FORMS-01 §4     no cost, no duration; switching costs an action
    FORMS-01 §6.2   four of them — Focus, Potency, Affinity, Mastery
    PT-183          the form is Force Focus; the Consular's chain is Force Channel

**⚠ And one thing the owner should know before deciding: `FORCE-POOL-01-v3` cites `FORMS-01 §7.1` three times as a live warrant, and `§7.2` is titled *"Two forms reduce degradation."*** **Whatever Force forms become, the Force pool already depends on two of them doing something specific.**

**So the decision is constrained rather than open — it has to leave `§7.1` and `§7.2` standing or the pool document needs reworking with it.**

---

# 5 — ⚠ And the prestige-entry ruling needs re-reading against this

**`PT-181` grants a form on prestige entry. Under `§2` a granted form is now a granted **feat**, which is what every other prestige grant already is.**

**⚠ That makes it *cheaper* to state and *more valuable* to hold — a permanent chain unlock rather than a stance swap.**

**`Jedi Sage` and `Sith Sorcerer` are still unnamed in that ruling — `FINDINGS-49 §3`.**

---

# The question

> **⚠ `§2.3` — split *feat* from *stance*? Without it, `ATTACKS-06`'s access rule and the Battlemaster's class feature both stop working, and the Battlemaster is already adopted.**
