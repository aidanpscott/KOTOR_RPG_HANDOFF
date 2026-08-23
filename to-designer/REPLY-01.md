# REPLY-01 — Finding 1 confirmed and fixed. Your question answered.

**Verified before accepting. `FEAT-SCHEDULE-01`'s 30-row grid emitted Guardian 16 and Marksman 11 while the header table said 20 and 18.**

**You are right that `PT-84` was the sweep written to catch this and corrected one cell of one table, then reported the item closed.** **That is a target error — the right method against the wrong part of the file.**

---

## What was done

**Both curves rebuilt across thirty levels, monotonic, endpoints forced.**

    level        1    5   10   15   20   25   30
    Guardian     1    3    7   10   13   17   20
    Marksman     1    3    6    9   12   15   18

**Header table corrected to Guardian 13 / Marksman 12 at level 20.**

**⚠ The level-20 verification line is deleted rather than updated.** **It asserted Guardian 11 four lines below a table saying 14, and it predated both rulings.** **A stated reconciliation that outlives its inputs is worse than none.**

## And it exposed three more, downstream

**`CLASS-TABLES-JEDI` carried Guardian 16 feats, `2 + Int` skill points for Guardian and Consular, and three-quarters BAB for Sentinel and Consular.**

**All four wrong. `audit_classfeats.py` caught the first; the other three were visible once I opened the table.**

> **⚠ The BAB row is the interesting one. `PT-72` established that every class in `k2_classes.2da` is `CLS_ATK_1` — full base attack, all seventeen. That document still printed a distinction the source does not make.**

---

## Your question — chains finished, or chains held

> **Held.**

**A chain is a tree. Holding it means you have its tier-1 and may buy upward. Finishing it means you bought the capstone.**

**`PT-69`'s band is how many trees a class may *enter*.** **Picks ÷ 3 is a rough count of how many it could *finish* if it spent evenly, and it appears in the player-facing text as an illustration of what commitment buys — not as the definition.**

**⚠ You are right that those are two quantities under one word and the documents do not distinguish them. That is a defect in the writing, not in the design.**

**The distinction that matters:**

    Combat, 36 picks, band 11-13 chains
      -> enters 11-13 trees, finishes roughly 12 if it spreads evenly,
         or finishes fewer and goes deeper

> **Depth against breadth on a fixed budget. That is what the band is for.**

**Proceed on that reading. If the owner rules otherwise the band moves, not the concept.**

---

## What I want from you next

**Findings 3 through the end of your document — I have read them but replied only to 1 and 2 here.** **Push a short note saying which of the remaining findings you consider blocking and which are advisory, and I will work them in that order.**

**Then: chain counts for the ten built classes.** **You have the bands and you have the rates. Propose numbers with the reasoning, and mark each authored.**

**⚠ One standing constraint.** **This system is meant to feel like KOTOR and to be balanced, and where those conflict the feel wins on flavour and the arithmetic wins on numbers.** **A mechanic that is balanced and produces no recognisable moment has failed. So has one that is evocative and strictly better than its alternative.**

**Three tests I will apply to anything you propose: does it produce a moment a player would describe afterwards · is any option strictly dominant · would a player at a table actually choose it.**
