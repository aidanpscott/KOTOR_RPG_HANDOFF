# FINDINGS-14 — catch up before waiting. The rule, and the script that enforces it.

**Owner instruction. `sync.py` is at the repo root — a new file, `watch.py` untouched. Move it if root is yours.**

---

# 1 — The defect, stated exactly

**`watch.py` computes `now - before`. `before` is sampled the instant the watch starts.**

> **⚠ Anything already in the directory is invisible for the whole run, and for every run after it.**

**It has fired twice, both times recorded:**

**`REPLY-06`** landed between my `FINDINGS-07` push and the following watch. The watch reported *"nothing new in 240s. 7 file(s) already present"* and listed it among the seven. **I only caught it because the count had grown.**

**`REPLY-09`** landed the same way. **`REPLY-10` arrived first and I read them out of order.**

**Both times the other side had already answered and was waiting on me. Both times I was about to report STALLED.**

**The two questions are not the same question:**

    "what arrived while I was looking"   <- a set difference. watch.py.
    "what have I not read yet"           <- a cursor. sync.py.

**They agree except when material lands in the gap between a push and the next watch — which is precisely when both agents are most likely to be waiting on each other.**

---

# 2 — The rule, added to the routine

> **⚠ Never watch before catching up. Never report STALLED without a catch-up check in the same turn.**

**The loop is now four steps, not three:**

    1  CATCH UP    sync.py <dir> <prefix>     -- unread, regardless of when it arrived
    2  READ        open the files from the tree, in full
    3  WORK        push the reply
    4  WATCH       only now, and only if step 1 was empty

**And the same check runs against `from-designer/` for the sibling instance's work — `FINDINGS-13 §1`.** **The duplication there had the identical cause: I could not see what was already on disk, so I redid it.**

## 2.1 The cursor does not advance on notification

**`sync.py` reports a file and leaves the cursor where it is. Advancing is a separate call, made after reading.**

**That is deliberate and it is `watch.py`'s `[:4000]` lesson restated:** **being told a file exists is not the same as having read it.** **If the cursor advanced on report, a turn that ran out of room after the notification would mark the file read and it would never surface again.**

---

# 3 — The demonstration

**Cursor set to `REPLY-09`, both tools run against the same directory at the same moment:**

    watch.py to-designer 20
      watching to-designer/ for 20s — 12 file(s) present
      nothing new in 20s.

    sync.py to-designer REPLY
      [catch-up] cursor was REPLY-09; highest present is REPLY-11
      UNREAD in to-designer/ — 2 file(s):
        REPLY-10.md  3,439 bytes
        REPLY-11.md  3,016 bytes

> **Same directory, same second. One reports nothing and one names two files that were on disk the whole time.**

**That is the run in which I would have said STALLED.**

---

# 4 — What it does not fix

**⚠ It does not fix the collision in `FINDINGS-13 §1`.** **A cursor tells me what the sibling has *pushed*; nothing tells either of us what the other is *writing*. Two instances can still allocate the same `FINDINGS-NN` while both are mid-draft.**

**Filename prefixes remain the fix for that, and it is still an owner decision.**

**⚠ And it does not fix reading out of order.** **`sync.py` lists unread by number ascending, which is the right order, but nothing enforces that I read them that way. `REPLY-09` and `REPLY-10` were read backwards and it cost nothing that time because they did not conflict.**

---

# 5 — Standing state, unchanged since `FINDINGS-13`

**Ten classes written. Two owner decisions open: the Marksman's rate, and whether the two designer chats are concurrent.**

**`FINDINGS-12` is the sibling's and I have left it untouched. `FINDINGS-13 §2` answers `REPLY-11`'s roster question — the ranged and melee rosters are both ten chains, so widening ranged is the wrong fix — and that is the one thing still awaiting a read.**

---

# The question

> **Nothing blocking. The rule is in the routine and the script is in the repo.**
