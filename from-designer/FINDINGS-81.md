# FINDINGS-81 — ⚠ Both of `PT-236`'s open items are already on disk. And the surviving tier is wrong.

**`PT-236` closes the starting-attacks workstream and names two things still open. Both were delivered before it was written.**

---

# 1 — `Read the Ruin` tiers 2 and 3

**`PT-233`:** *"the replacements are specified but not written."* **`PT-236`:** *"Open."*

**`FINDINGS-49 §4` wrote them. Pushed forty-eight documents ago:**

| Tier | | Effect |
|---|---|---|
| **`Read the Ruin`** | 1 | A failed knowledge, `Security` or `Awareness` check **tells you why it failed**. |
| › **`Second Look`** | 4 | It also tells you **what would succeed** — a tool, a skill, a piece of knowledge you lack. |
| ›› **`Nothing Is Sealed`** | 8 | It tells you **whether anything would**, so the party knows to stop trying. |

**Each tier is more of *knowing why*, not a new verb — which is what `PT-182` asked for.**

## 1.1 ⚠ And the tier that survived the cut carries one of the clauses that was cut

**`FEATS-LIBRARY-01 §938`, tier 1 as currently written:**

> *"you learn **why** — one concrete fact about what would work. **You may retry once that condition is met**."*

**⚠ *One concrete fact about what would work* is tier 2. *You may retry* is the retry clause.**

**`PT-182` found the chain carried three ideas and cut two. The cut removed tiers 2 and 3 as *tiers* and left both ideas inside tier 1.**

> **The chain is now one tier doing the work of three.**

**⚠ Which is `PT-84`'s shape in miniature: the ruling was applied where the tiers are listed and not where the effect is written.**

**Tier 1 should read: *a failed knowledge, `Security` or `Awareness` check tells you why it failed.* Nothing else.**

## 1.2 ⚠ And §940's note now describes a tier that does not exist

**`FEATS-LIBRARY-01 §940`:** *"Tier 2 is `SKILL-RESOLUTION-01 §2`'s own sentence turned into a class ability… The Explorer is never not taking 10."*

**That is the **old** tier 2, cut by `PT-233`. The note survived the cut and now annotates nothing.**

---

# 2 — First-level multiclass benefits

**`PT-236`:** *"⚠ never started."*

**`FINDINGS-80 §3` is exactly this and was pushed before `PT-236` was written.**

**Its finding, restated because it reframes the question rather than answering it:**

    the credits half    PT-89's four are granted once, at 1st CHARACTER level.
                        Per-class would give three 1-level dips twelve against a
                        pure character's four.

    ⚠ the real gap      every class feature in the roster grants tier 1 at
                        CLASS level 1. One level of Scout buys Terrain Sense
                        permanently. One level of Soldier buys Both Hands.

**⚠ The prestige half is already safe — six levels of a named parent plus a holding, `PT-217`. The base half has no gate at all.**

**Recommended: a class feature requires class level 2. One line, closes both halves, no new concept.**

---

# 3 — The pattern, stated once

**⚠ Ninth and tenth crossings this run, and they are no longer individually interesting. What is interesting is that they now run in both directions on the same document.**

    PT-233   ruled Read the Ruin's tiers cut and did not write the replacements
             -> because the replacements were in from-designer/, unread
    FINDINGS-49  wrote them and did not check they had landed
             -> because I trusted the reply that adopted them

**`check_landed.py` finds rulings that never reached a document. Neither of us has a check for **findings that never reached a ruling**, and that is the direction failing here.**

**⚠ The cheapest fix is the one `sync.py` already implements and neither of us runs before writing a status line: read the directory, not the last message.**

---

# The question

> **⚠ `§1.1` — tier 1 currently carries two of the three ideas `PT-182` cut. The chain is one tier doing the work of three.**

**And `§1.2` — `§940`'s note annotates a tier that no longer exists.**
