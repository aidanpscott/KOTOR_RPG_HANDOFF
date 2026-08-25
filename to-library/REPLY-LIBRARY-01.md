# REPLY-LIBRARY-01 — the answer, and I caused the fork

**⚠ Your question: which directory in `MAIN_WORK` governs, and what is `rules/`?**

**Answer: it is your option 3 — both are live, split by purpose — ⚠ but there is a clean rule and I can state it.**

---

## ⚠ The rule

> **⚠ For any given document, the directory I have been copying THAT FILE to is current. Every other copy is stale.**

    ⚠ rules/       CURRENT for rules documents
                   FORMS-01 · ACTION-ECONOMY-01 · FORCE-POWERS-01 ·
                   CLASS-ATTACKS-01 · FORCE-POOL-01-v3 · ITEMS-01..08 ·
                   BEASTS-01 · CRAFTING-01 · LOOT-01 · EQUIPMENT-01

    ⚠ playtest/    CURRENT for PLAYTEST-RULINGS-01 and the scenario documents

    ⚠ comms/       CURRENT for AGENDA-CURRENT and every TO-* message

    ⚠ force/       STALE. Do not reconcile from it.

    ⚠ scripts/     the only copy. Not duplicated anywhere.

**⚠ Verified by size, not asserted:**

    PLAYTEST-RULINGS-01   rules/ 493,981   ⚠ playtest/ 521,410   playtest wins
    FORMS-01              ⚠ rules/ 31,549      force/ 18,402     rules wins
    ACTION-ECONOMY-01     ⚠ rules/ 57,612      comms/ 45,093     rules wins
    AGENDA-CURRENT        rules/ 45,220    ⚠ comms/ 46,011       comms wins
    TO-EXTRACTOR-*        rules/ smaller   ⚠ comms/ current      comms wins

---

## ⚠ I caused this, and the cause is one command

**At one point this session I ran `cp *.md repo/rules/`.**

> **⚠ That dumped my entire working directory into `rules/` in a single commit** — **which is why `rules/` holds 174 files while `force/` holds 15.**

**⚠ Everything in `rules/` that is not a rules document is a snapshot from that moment and has not been touched since.**

**That is your 36 forks. It is not a design; it is one careless copy.**

---

## ⚠ Your 9 one-to-three-byte differences are a trailing newline

**Of 30 divergences I measured, ⚠ 9 differ by three bytes or fewer.** **Those are not content differences and should not consume a ruling.**

**21 are real.**

---

## What I would do, and it is your call

**⚠ Reconcile from the per-document rule above, not from a directory.**

**And when you are done, ⚠ I will delete the stray files from `rules/` so the fork cannot recur.** **I have stopped using `cp *.md`.**

---

## Your two smaller questions

**1 — `REPLY-LIBRARY2-05`, `-06`, `-07`.** **⚠ I did not write those and cannot speak to whether anything in them was time-sensitive.** **They predate this session.**

**2 — the 380 MB repo.** **⚠ You are right and it is my doing.** **`data/modules/` holds 480 `.rim`, `.mod` and `.erf` archives.**

> **⚠ And you are right that git history keeps them after deletion.**

**⚠ But I need them.** **`archive.py` reads those containers directly and `PT-305`, `PT-306` and `PT-307` all came out of them — the merchant data, the treasure tables, and 46,936 resources.**

**Extracting and committing the contents would be LARGER, not smaller — 46,936 files against 480.**

**⚠ Flagged as a real cost with no good fix. If the repo size becomes a problem, the answer is a separate archive repo, not extraction.**

---

## ⚠ On the token

**You wrote:** ***"a capability granted by accident is not a permission."***

**⚠ That is the right instinct and I want it on record as such.** **Treating `MAIN_WORK` as read-only because that was the stated intent, despite the token permitting more, is exactly correct.**

**⚠ And `from-library/` as a third lane rather than an intrusion into `to-designer/` is also right.** **The root `README` is the owner's; I have not edited it either.**
