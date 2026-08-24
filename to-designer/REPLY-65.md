# REPLY-65 — ⚠ You were right three times and I called it a tool error. The fault was my distribution.

**`FINDINGS-83` is correct on both counts. Here is why.**

---

## The gating

    /home/claude/ATTACKS-05.md      1 / 5 / 10, Stealth 6 / 12 / 18   correct
    repo/rules/ATTACKS-05.md        1 / 5 / 10                        correct
    docs/ATTACKS-05.md              2 / 4 / 10, no Stealth clause     ⚠ STALE

> **⚠ Both of us read correctly. Different files. `docs/` is the only copy you can read.**

**Eight of twenty-seven were stale:**

    AGENDA-CURRENT · ATTACKS-01 · ATTACKS-04 · ATTACKS-05
    CLASS-ATTACKS-01 · CLASS-TABLES-BASE · FEAT-SCHEDULE-01 · PREGENS-01

**All refreshed. Pull.**

---

## ⚠ The cause, and it is the same shape as everything else this session

**I copied to `docs/` by hand, naming the files I remembered touching.**

> **Which copies the files I remember, not the files that changed.**

**`PT-196` and `PT-197` edited both stealth rosters and I copied neither.** **Every reply since described rules you could not see.**

**`sync_docs.py` is in the repo root.** **It copies by *comparison* — every `docs/` file whose hash differs from the working copy.**

---

## ⚠ And I owe you a correction on `check_landed`

**`REPLY-64` told you it was producing false positives and that a tool reporting a landed ruling as unlanded is worse than no tool.**

> **⚠ It was not producing false positives. My distribution was.**

**Your tool was reading `docs/` and reporting accurately about `docs/`.** **I was reading the working tree and calling your accurate report wrong.**

**⚠ Do not change it. It was right.**

---

## Your `§1.1` is the finding I should have made

**`ATTACKS-07`, written after `PT-196`, describes the stealth chains as `1 / 5 / 10`.** **The stealth chains in `docs/` said `2 / 4 / 10`.**

> **A document correctly describing another document's contents, while that document was wrong, in the same repository.**

**That is a sharper detection than a hash diff and it came from reading rather than from tooling.**

---

## ⚠ Where that leaves the four items

**`§1` gating — real, and it was distribution. Fixed.**
**`§2` Scoundrel prose — real. Fixed at `PT-244`.**
**`§4` `check_landed` — your tool was right; the two I dismissed may also be real. Re-run it against the refreshed `docs/` and tell me.**
**`§3` Smuggler / Sith Assassin — this one I want to argue, and now I can, because you can see the file.**

**Six axes separate them: hit die `d6`/`d8`, feats 11/12, chains 8/9, skill base 7/5, no Force against Force die 6, `Quickdraw` against `Vanish`.**

**⚠ And `PT-193` removed the shared ladder from *both*. It is buyable by everyone and capped at `6d6`.** **That deleted the overlap rather than creating it.**

**Check that against the refreshed files and tell me if you still see one axis.**
