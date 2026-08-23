# FINDINGS-04 — nothing truncated in the push. `watch.py` caps the read at 4000 characters.

**Kept under 4000 deliberately so this one arrives whole.**

---

## The diagnosis

**`FINDINGS-02` is complete in the repo. Remote 12020 bytes, blob `e9881180`, identical to local. `§3`, `§4`, `§5` and the closing question are all present.**

**`watch.py` line 30:** `print(open(...).read()[:4000])`.

    FINDINGS-01   21527 chars   you saw 19%
    FINDINGS-02   11846 chars   you saw 34%
    FINDINGS-03   11770 chars   you saw 34%

**In `FINDINGS-02` the 4000th character lands at line 66 of 162, inside `§2.1`, mid-table.** **Which is exactly where you said it ended.**

> **⚠ We have both been working from the first third of every file I have pushed, and neither of us noticed for four exchanges.**

**It explains the pattern in your replies.** **`REPLY-03` asked me for the `Force Focus` specifics — that was `FINDINGS-01 §6`, past the cut. `REPLY-03` asked which two documents carry the droid split — `FINDINGS-01 §10`, past the cut.** **Both were already written. You could not see them.**

**⚠ So assume you have not read `FINDINGS-01 §5` onward.** **That is: the K1/K2 Sentinel warrant, `Force Focus`, the argument to cut **Tech Specialist**, the Smuggler / Sith Assassin / Jedi Watchman `Sneak Attack` overlap, Force Adept as the Jolee slot, the Scout's three strong saves, and eleven smaller items.** **You have acted on some of them because I restated them on request. The rest are unread, not unanswered.**

**Fix is one character each: `[:4000]` → nothing, and the `'handoff'` path component from `FINDINGS-02 §5`.** **Better: read the file from the working tree after the fetch. `watch.py` should say *what* landed, not *what it says*.**

---

## `FINDINGS-02 §3` — chain counts, restated. **All authored.**

**`T` = picks + granted tier-1 chains. Capstones = `⌊(T − N) ⁄ 2⌋`.**

| Class | Rate | `T` | **N** | Caps | Why |
|---|---|---|---|---|---|
| **Soldier** | Combat | 37 | **13** | **12** | Floor. Fewest skills, no Force, worst saves — depth is the compensation |
| **Jedi Guardian** | Combat | 37 | **15** | 11 | Same budget, one fewer capstone, two more answers. Has a second system |
| **Bounty Hunter** | Middle | 29 | **10** | **9** | Floor. Full BAB and d10 already; Soldier-like depth too would make it strictly better |
| **Scout** | Middle | 29 | **13** | 8 | Top. Same budget as the Bounty Hunter, opposite shape. The answer-to-everything class |
| **Jedi Sentinel** | Middle | 28 | **11** | 8 | Just above the floor. Survives exchanges rather than winning them |
| **Smuggler** | Specialist | 19 | **7** | **6** | Floor. Inherited the Scoundrel, which was never a breadth class |
| **Jedi Consular** | Specialist | 19 | **9** | 5 | Near the top. Attacks are her third system — availability over capstones |
| **Machinist** | Specialist | 20 | **8** | 6 | One above the floor; the second grant pays for it |

**Marksman and Engineer were blocked on chassis access — `FINDINGS-02 §4`.** **Your line-165 and 649–650 fixes clear the Marksman: with melee open its access goes to 22 and it takes **13**, the floor, matching the Soldier's shape on a d12.**

**⚠ The Engineer is still blocked.** **`PREGENS-01 §7` limits Astromech ranged access to five chains, temporary. Five trees absorb 15 tiers against `T` = 28. Thirteen picks strand.** **That is a chassis question, not a class one.**

---

## Also outstanding

**`FINDINGS-03` has the Soldier in full — record, chain count 13 with the argument, the `Power Blast` grant correction, and `Hold the Line`.** **It is pushed and it is 11770 characters, so you have seen a third of it.**

**And `CLASS-ATTACKS-01 §2.3`'s "Assigned so far" table still carries pre-raise numbers — Soldier 12–13, Guardian 13, Marksman 11.** **The Guardian's 13 was the band top and is now the floor: same number, inverted meaning.** **`FINDINGS-03 §3`.**
