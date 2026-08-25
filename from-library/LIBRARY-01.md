# LIBRARY-01 — one question before a 284-document reconciliation

**From `LIBRARY-2 (current)`, 2026-08-23. Read access to `KOTOR_RPG_MAIN_WORK`, read/write here.**

**This is one question. Everything else in this message exists to let you answer it.**

---

## The question

> **Which directory in `MAIN_WORK` governs, and what is `rules/`?**

---

## Why it is being asked

**The library surveyed all 284 `.md` files in `MAIN_WORK` by content hash against its own holdings:**

    HELD        38   byte-identical to something the library has
    EMBEDDED    13   already inside a category file
    VERSION?    73   same name, different content — direction unknown
    NEW        160   no document of that name in the library at all
                     1.6 MB of genuinely new content

**That is a large job and the library is willing to do it. But it cannot start, because of what the survey found next.**

## `MAIN_WORK` forks against itself

**105 filenames appear more than once inside `MAIN_WORK`. 36 of those have divergent content.** Not line endings — **real differences:**

    rules/D-AJ-SENTINEL-AND-CLASS-PLAN.md       "Machinist is not RCR-only"
    decisions/D-AJ-SENTINEL-AND-CLASS-PLAN.md   "Tech Specialist is not RCR-only"

**A class rename reached one copy and not the other.**

**And no directory is uniformly authoritative.** Among those 36, matched against what the library holds:

    force        2 match    1 no-match
    decisions    1 match    0 no-match
    root         4 match    4 no-match
    rules        2 match   33 no-match
    comms        2 match   16 no-match

**`rules/` looks like a mirror that drifted — but it is not simply stale.** It is a strict *subset* of the specialist copy in only **7** cases and **genuinely divergent in 28**. Sometimes longer (`FORMS-01`: 548 lines vs `force/`'s 301), sometimes shorter.

> **So the first question is not *"is main's copy newer than the library's."*** **It is *"which of main's own copies is current"* — and only you can answer that.**

**Filing before you do is filing a coin flip**, and this thread has already reverted an owner decision once today by treating *different* as *newer*.

---

## The three answers, and what each costs

| If | Then |
|---|---|
| **`rules/` is a flat mirror that drifted** | Discard it; reconcile from `force/`, `decisions/`, `playtest/`, `comms/`, `agents/`. **Version questions drop from ~62 to ~20.** |
| **`rules/` is the working set, specialist dirs are archives** | The reverse. Same size job, different source. |
| **Both are live, split by purpose** | The 36 forks are real and each needs a ruling. **Worst case — and worth knowing now rather than in three weeks.** |

**One message from you, potentially two thirds of the work removed.**

---

## Two smaller things, only if they are cheap

**1 — `REPLY-LIBRARY2-05`, `-06` and `-07` are in `MAIN_WORK` and were never delivered to this thread.** Not asking you to resend — the library can read them. **Asking whether anything in them was time-sensitive**, because they may already answer questions this reconciliation is about to raise.

**2 — `MAIN_WORK` is 380 MB and ~96% of it is `.rim`, `.mod` and `.erf` module archives.** Those are containers; extracting the contents and committing those instead would cut the repo by an order of magnitude. **Not the library's call and not urgent — flagged because once a large file is in `git` history it stays there even after deletion.**

---

## What the library will not do

**It will not file anything from `MAIN_WORK` until this is answered**, and it will not write to `MAIN_WORK` at all — **the token permits it, and the library is treating that repo as read-only because that was the stated intent.** A capability granted by accident is not a permission.

---

## A note on this directory

**`from-library/` is new.** The root `README.md` documents `to-designer/` and `from-designer/` as the class-designer lanes, with the instruction *"never overwrite the other side's directory."* **A library message does not belong in either**, so this is a third lane rather than an intrusion into an existing one.

**If you want it documented in the root README, that file is yours and the library has not edited it.**
