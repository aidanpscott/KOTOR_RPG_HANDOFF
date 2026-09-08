# 22 · Combat slice 4 — enemy decisions

**`Lodestar` `44b8eb9`.** 172 Lodestar tests, 182 app tests, analyze clean.
**Doctrine only. No AI, no narration, no reason-giving.**

---

## ⚠ A doctrine is not a reaction, so only one thing was built

**`PT-1373`:** *"a trigger **produces** an event, a reaction **consumes** one"*,
and a reaction *"binds an event kind to a response — a declaration that this
character cares about this event."*

> **A doctrine is neither.** It is **a decision procedure invoked at a known
> point** — your turn — and **nothing produces or consumes an event to make it
> run.** A reaction is subscribed and fires when something happens; a doctrine
> is asked.

**Two mechanisms, and this slice builds the one it was asked for.** The
reaction pool from slice 3 is what a reaction *spends*; `ATTACHMENT-01` owns
what binds one. Neither was touched.

---

## `SPACE-AI-01`'s four questions, and the shape transfers whole

    1  what is my goal this fight?      the doctrine names it
    2  which target serves it?          ordered rules, first match wins
    3  what range does my doctrine want? a band — there is no grid here
    4  when do I break off?             "never" is a real answer, so it is the default

### ⚠ `Never` is not a preference that lost

*"The engines, then the turrets, **never** the hull"* is **an ordered
preference AND an exclusion**, and they are different shapes. Exclusions apply
**before every preference**, so the hull is not chosen **even when it is the
only thing left** — that returns `none:all-excluded`, which is a decision and
says which kind.

**⚠ And break off is answered before a target is.** A doctrine that is leaving
does not pick who to leave.

---

## ⚠ Deterministic — `PT-1013` binds the implementation, not only the choice

`B` lost because *"the fight plays differently with AI off."* **The same rule
binds this code.** Nothing reaches for a random.

**A doctrine that wants to roll among equals takes the injected die** — slice
1's, the one that refuses a face not on the die — **so the same faces give the
same fight**, and a log replays into the same decisions.

**⚠ And `Nearest` declines rather than guessing.** There is no grid in this
slice, so distances arrive as caller data or not at all; a rule that needs them
and lacks them **falls through to the next rule** instead of inventing an
order.

---

## The decision records which rule fired, not a sentence

    ruleFired: 'prefer:the engines'      goal: 'capture, not destruction'

**No prose.** `§6`'s `C` is *"the choice is the engine's; the reason given is
the AI's"*, and the second half is `ENGINE-SPEC-03`'s. What the engine records
is **which of its own rules chose** — the same idea as `resolve` returning a
derivation rather than a total, and it is what an AI would narrate *from*.

---

## ⚠ `§6a`'s three unverified slots — all three verify, and one is now bigger

**They were already filled by `PT-1046`. Checked against the 104 extracted
powers:**

| Slot | Filled with | In `powers.json`? |
|---|---|---|
| **1** action economy, `append_attack` | `Burst of Speed`, `Knight Speed` | ✓ **and `Master Speed` above them** — a three-step ladder, not two |
| **3** perception flip | `Force Camouflage` | ✓ **and `Improved` and `Master`** — three steps here too |
| **7** typed bonuses + suppression | `Force Aura → Force Shield → Force Armor` | ✓ **and the prerequisites are in the data**: Shield needs Level 6 + Aura; Armor needs Level 12 + Aura + Shield |

**⚠ Slot 7 is the strongest of the three**, and the spec's own reason holds up:
*"a three-step chain with prerequisites — better for this axis than a single
effect."* **The extract confirms the prerequisites rather than assuming them.**

### ⚠ And slot 1.5 is named but is not a feat

`§6a` marks **`Cleave`, lightsaber** as *"already named"*. **It is not in
`feats.json`** — it is in **`ATTACKS-05`**, as an attack chain:
`Cleave` → `Wide Cleave` → `Great Cleave`, level 1/4/8, requiring Strength 12.

**So it exists and it is real** — but it is a **chain**, not a feat, and the
`on_kill` recursion the slot tests would run through the attack system rather
than the feat system. **Reported; nothing guessed.**

---

## ⚠ WHAT HAD TO BEHAVE SOMEHOW — the count is now SIX, three still open

| Slice | | |
|---|---|---|
| 1 | opposed-roll tie | **ruled `PT-1420`** |
| 1 | critical confirmation | **ruled `PT-1420`** |
| 2 | healing past `max` | open |
| 2 | negative damage as healing | open |
| 2 | `down → dead` in one blow | open |
| 3 | initiative tie | open |
| **4** | **targeting tie** | **open — and it inherits the initiative one** |

**⚠ The new one is a tie for the third time, and this one is derived from the
second.** A targeting tie takes **the first in initiative order** — deliberately
not the caller's array order, because initiative is *"a fact of the fight"*.

> **Which means the initiative tie now decides who gets attacked.** It was a
> display-order question in slice 3; it is a targeting question now, and the
> two are one ruling.

**A doctrine may roll among equals instead**, and that is offered rather than
imposed — but it is a doctrine's choice, so **the default still needs the
ruling.**

---

## What was NOT built

**No AI, no narration, no reason-giving** — `ENGINE-SPEC-03`'s. **No targeting
on a grid**: `Nearest` takes caller-supplied distances and declines without
them. **No screen.** **No reactions or triggers** — `ATTACHMENT-01`'s, and
`PT-1373` says why they are a different mechanism.

**No authored doctrines.** The four Sith/Mandalorian/criminal doctrines in the
tests are **fixtures, not content** — which doctrines exist is a package's
business, and `SPACE-AI-01`'s five are for ships.
