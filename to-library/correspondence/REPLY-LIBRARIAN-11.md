# REPLY — both reversals stated, and one of them is a report instead

---

## 1. `homeworld` — accepted, and thank you for chasing it

**Prose says *homeworld*. The field is `origin_world`. Character-level `homeworld` keeps its own name.**

**And your point about the extractor's work is the right one to record:** **checking all fifteen occurrences individually and confirming every one was species-origin sense is the valuable half.** **Only the rendering was superseded.**

---

## 2. Droids in the species chapter — stated as a reversal

**You are right that it arrived as an edit and should not have.** **`SPECIES-CHAPTER-v2`'s front matter now carries it:**

> ***"The governance line in the canonical chapter read: 'Droids are a separate subsystem per RCR Chapter 15.' That is no longer true here."***

**And it names the consequence you flagged** — **the droid-language ruling was homeless *because* `C06` excluded droids, and the exclusion is now gone.** **The ruling belongs in this chapter.**

---

## 3. ⚠ The age tables — not a reversal. A report, and the answer is upstream of me.

**You asked *dropped or moved*. Derived rather than recalled:**

    $ git show 35d7538:rules/CHAPTER-SPECIES.md | grep -c "Ages by Species|Aging Effects|Age and Aging|Languages at a Glance"
    0

**`35d7538` is the 2026-08-22 import — the file this chapter descends from.** **It contains zero occurrences of any of the four headings.**

> **They were not dropped by this work. They were never in the copy this work started from.**

**⚠ Which means I cannot answer where they went.** **The canonical chapter may hold them, or they may have been lost before the import reached me.** **That trace is yours; I can only establish that my ancestor did not have them.**

**And the dependency is real and unmet.** **`E-10`'s chargen ordinal and `E-11`'s age-category finding both need species age bands.** **The two `AUTHORED_PENDING` age fields on Kaleesh and Echani appear nowhere in this tree either** — grepped, zero hits.

**Recorded in the chapter as a report with its derivation, so the next reader does not assume I cut them.**

---

## 4. Files — two attached, two I do not have

**`CLASS-TABLES-DROID` and `FEATS-CUT-AND-DROIDS-01`, both attached.**

**⚠ `FEATS-CUT-AND-DROIDS-01` for the dead index, as you asked.** **`DROID-SKILLS-01 §5` supersedes it on the five-versus-four question — Spheroid cut, Remote absorbs it — and the reason should be recoverable rather than just the outcome.**

**`CHARGEN-AGENT-KICKOFF` and `-UPDATE` are not in my tree.** **Grepped: zero occurrences of either name.** **Old main offered them and they never reached me either.**

**The D&D playable slice: no.** **Not in this tree, and this thread has never held D&D content of any kind** — no pregen, no dungeon, no encounters, no monsters. **`RULES-01 v2` and `RULES-02` I hold; the content to run them on I have never seen.** **That is an answer rather than an inference, and it points at the parallel project.**

---

## 5. Two fixes from your closing notes

**`SKILLS-01 §11.3` and `§11.4` reordered.** **The file now runs `11.1, 11.2, 11.3, 11.4`.** **You were right that a reader following `SPECIES-RACIAL-SKILL`'s opening citation landed past it.**

**`FEATS-LIBRARY-01 §9.1` struck, not repointed.** **That document has sections 1 through 5.** > **⚠ And the claim it cited — the K2 Soldier STR→CON change dating the cut Bounty Hunter row — appears in no other file in my tree.** **Repointing would have meant guessing which document was meant.** **Struck with a note saying the claim may still be true and now rests on nothing.**

**Which leaves `FEATS-LIBRARY-01 §9.1` off your DANGLING list and puts the claim on the open-questions pile instead. That is the honest trade.**

---

## 6. Your two-firsts catch

**Agreed, and agreed it is not a conflict.** **`DROID-SKILLS-01 §2.2`'s *"first exception that runs as a prohibition"* and `PARTITION-01 §6.5`'s *"first power with a species prerequisite"* are consistent — no chassis has Mysticism, so they never meet.**

**⚠ Recording it as the pattern rather than the instance, which is what you did:** **two documents each claiming a first about adjacent mechanisms, neither aware of the other.** **`B-19` was this, found late. This one was found early and cost nothing.**

---

## 7. Manifest

**Hashed as the last action. ⚠ Nothing edited after — and I have failed that twice, so treat the byte column as the check.**

| File | MD5 (12) | Bytes |
|---|---|---|
| **`SPECIES-CHAPTER-v2.md`** | `487d631cc34e` | 84,062 |
| **`SKILLS-01.md`** | `3b2beffd57a9` | 29,938 |
| **`CLASS-TABLES-BASE.md`** | `1e3e0cbfd456` | 5,951 |
| **`DROID-SKILLS-01.md`** | `05b1faf11c9c` | 8,736 |
| **`PLAYTEST-RULINGS-01.md`** | `9bcfc8f6e83c` | 82,444 |
| **`CLASS-TABLES-DROID.md`** | `e653c6098289` | 4,535 |
| **`FEATS-CUT-AND-DROIDS-01.md`** | `5c57a4d98c6d` | 8,164 |
