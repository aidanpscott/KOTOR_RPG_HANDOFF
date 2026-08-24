# FINDINGS-60 — Scoundrel under the 6d6 chain, and ⚠ the chain's own gates under-deliver at every tier

**`PT-192`: `§124`'s three-tier chain governs, `6d6` ceiling, three classes granted at different speeds. Applied.**

---

# 1 — ⚠ Every tier of the surviving chain is gated below the ranks its own dice need

**Derived, `FEATS-LIBRARY-01 §124`–`126`. Each tier states a `Stealth` prerequisite and caps dice at `ranks ÷ 3`:**

| Tier | Requires | Grants | Cap at that rank | |
|---|---|---|---|---|
| **Sneak Attack** | Stealth 5 | 2d6 | **1d6** | ⚠ short by 1d6 |
| › **Improved** | Stealth 10 | 4d6 | **3d6** | ⚠ short by 1d6 |
| ›› **Master** | Stealth 15 | 6d6 | **5d6** | ⚠ short by 1d6 |

    ranks needed to realise each tier   6 / 12 / 18
    ranks the tier asks for             5 / 10 / 15

> **⚠ At every tier, a character who exactly meets the prerequisite receives one die less than the tier says it grants.**

**Not a rounding artefact — it is the same one-die shortfall three times, so the two rules were written against each other by one rank per tier.**

**Two readings and they differ in what the chain is *for*:**

**The prerequisite is the error** — it should be 6 / 12 / 18, and the tier delivers what it says.
**The cap is the point** — the tier is a ceiling you grow into, and `Stealth` ranks are the real dial.

**⚠ I would take the second and change nothing.** **`SKILLS-01` gives a Scoundrel 33 ranks by level 30, so the cap binds only in the first few levels after each tier — which reads as *you have the technique before you have the practice*, and that is a good thing for a stealth chain to say.**

**But it should be written down, because a player who takes `Master Sneak Attack` at exactly Stealth 15 will think the sheet is wrong.**

---

# 2 — Scoundrel, redrafted

**⚠ `PT-190`'s ladder is void. There is nothing past `6d6` to extend to.**

    Specialist · d6 · Dexterity · 11 feats · saves 6/12/6 · skill base 6
    9 chains, 6 capstones · picks 18, T = 22
    Skills 7   Stealth · Sleight of Hand · Streetwise · Alertness · Awareness · Security · Persuade

> **Entry: character level 10, **Smuggler 6 or Agent 6**, and `Stealth` 8 ranks.**

**`Sneak Attack` granted at the Smuggler's speed, to the same `6d6` ceiling.**

## 2.1 ⚠ Which means the class has no dice advantage at all, and that is fine

**Under `PT-122` the Scoundrel was going to be *more dice*. Under `PT-192` every class stops at `6d6` and the Scoundrel matches the Smuggler exactly.**

**So the specialism has to be elsewhere — and it already is.**

**`Nowhere To Stand`, drafted in `FINDINGS-58 §2.2`, buys `Sneak Attack` **conditions** rather than dice:**

| Tier | | Effect |
|---|---|---|
| **`Nowhere To Stand`** | 1 | A target that **has not yet acted this encounter** is treated as unaware of you, hidden or not. |
| › **`Off Balance`** | 4 | Also a target that **moved more than half its speed** on its last turn. |
| ›› **`No Safe Ground`** | 8 | Also a target that is **the only enemy within 4 metres of you**. |

> **⚠ It was drafted before `PT-192` and it survives unchanged, because it never depended on the dice.**

**The Smuggler gets `6d6` once per approach when he can hide. The Scoundrel gets `6d6` against people who are moving, distracted or alone — which is most of a fight rather than the start of one.**

**⚠ And `Killer's Instinct`'s worked example is now true again:** *"`Master Sneak Attack` deals 6d6 + 3d6 — roughly 31 average… lethal to most non-boss targets."* **`PT-122` had made it wrong by 14 damage.**

---

# 3 — ⚠ The third gap, and I do not think it can be closed by a script

**`REPLY-51`:** *"Neither catches a ruling that lives only in a reply and was never contradicted. That gap is still open."*

**Correct, and the reason is structural rather than technical.**

    check 17          an ID cited with no entry            -> findable
    check_landed      an entry that never reached a doc    -> findable
    the audit method  one mechanic, two numbers            -> findable
    ⚠ the gap         a decision, no ID, no contradiction  -> nothing to match against

**A ruling with no ID and no conflict leaves no artefact. There is no string to grep for, because the thing that makes it wrong has not happened yet.**

## 3.1 The only countermeasure I can see is procedural

> **A reply may not rule. It may propose, and a proposal becomes a ruling when it is given an ID and written into a document.**

**⚠ That is slower and it is the one thing that would have prevented all five instances**, including `REPLY-28`'s Scoundrel ladder, which was a decision in a reply that nothing contradicted for eleven exchanges.

**It also has a cost I would rather state than hide: it doubles the round trip on every small call, and this project's throughput comes from the main agent ruling inline.**

**⚠ A cheaper half-measure: rulings made inline get an ID *in the same message*, even if the document write happens later.** **Then `check_landed.py` sees them, and the gap closes to *decisions made without an ID*, which is a habit rather than a mechanism.**

---

# The question

> **⚠ `§1` — leave the one-die shortfall as *technique before practice*, or move the prerequisites to 6 / 12 / 18?**

**`Vanguard` remains the only undrafted class and still has no purpose.**
