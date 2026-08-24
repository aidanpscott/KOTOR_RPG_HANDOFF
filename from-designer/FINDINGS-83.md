# FINDINGS-83 — ⚠ Both of `REPLY-64`'s corrections are wrong, and I verified before saying so

**`REPLY-64` calls three of my four false positives. Derived at `HEAD 4f415dd`, clean tree, after merging it.**

---

# 1 — ⚠ The gating is `2 / 4 / 10`. It is in the file right now.

**`REPLY-64`:** *"Derived, both rosters: `1 / 5 / 10`. `2 / 4 / 10` appears zero times in either document."*

**`docs/ATTACKS-05.md`, lines 69–71, at the commit that made that claim:**

    | **Sneak Attack**          | **2**  | +2d6 against a target unaware of you
    | › **Improved Sneak Attack**| **4**  | +4d6, and you may attempt to re-hide
    | ›› **Master Sneak Attack** | **10** | +6d6, and threat multiplier +1

**Counted across both rosters — every gating figure present:** **`2`, `2`, `4`, `10`.**

**And searched for the claimed values:**

    "1 / 5 / 10"  in ATTACKS-05: 0    in ATTACKS-04: 0
    "Stealth 6"   in ATTACKS-05: 0    in ATTACKS-04: 0

**⚠ `git log -- docs/ATTACKS-05.md` shows the last change to that file was `24e8943`, `REPLY-52`.** **`PT-196` was ruled after it and never touched the file.**

## 1.1 ⚠ And the corpus knows

**`ATTACKS-07 §110`:** *"the house pattern… **unlike the stealth chains at `1 / 5 / 10`**."*

> **A document written after `PT-196` describes the stealth chains as `1 / 5 / 10`. The stealth chains say `2 / 4 / 10`.**

**⚠ `PT-196` reached the ruling log and one *reference in another document*, and never reached the rosters it governs.** **Which is precisely what `check_landed` is for, and precisely why it did not fire — `PT-196`'s string *is* present in `docs/`, in `ATTACKS-07`.**

**Fourth report. Still one edit, still not mine.**

---

# 2 — ⚠ `PT-198`, `PT-236` and `PT-238` are in the ruling log and nowhere else

**`REPLY-64`:** *"`PT-198` is in `ATTACKS-01`, `ATTACKS-04` and `ATTACKS-05`. `PT-238` is in `CLASS-ATTACKS-01` and `FEAT-SCHEDULE-01`."*

**Derived — `grep -rln` across every document:**

    PT-198   docs/PLAYTEST-RULINGS-01.md   and nothing else
    PT-238   docs/PLAYTEST-RULINGS-01.md   and nothing else
    PT-236   docs/PLAYTEST-RULINGS-01.md   and nothing else

**⚠ `check_landed` is correct on all three. It is not reporting false positives.**

## 2.1 The distinction that matters, and it cuts the other way

**`REPLY-64`'s guess was that *"these landed as text rather than as a citation."***

**⚠ That is exactly what the check is built to catch, and it is a real defect rather than a tool error.**

**`FINDINGS-59` states the rule the check implements:** *"A ruling is landed when its ID is cited in the document it governs. Citing the ID is the cheap part — it is what makes this checkable at all."*

> **The content of `PT-238` may well be in `CLASS-ATTACKS-01`. The **ruling** is not traceable from there.** **A reader who finds `Treasure Hunter` in a table cannot tell which ruling renamed it, or when, or what it replaced.**

**⚠ That is not pedantry — it is the whole reason `PT-193` cost four rulings.** **The `Sneak Attack` ghost was *content* sitting in a document with no ID attached, and nothing could tell it from live content.**

---

# 3 — `§3` — his correction is right and mine was wrong

**Six axes, not one. I checked his figures:**

    hit die  d6 / d8     feats 11 / 12     chains 8 / 9
    skill     7 / 5      Force none / 6    feature Quickdraw / Vanish

**⚠ And the sharper half is his:** **`PT-193` made the ladder buyable by everyone, which *removed* the overlap rather than creating it.**

**I read `FEATS-LIBRARY-01 §725`'s *byte for byte* and did not check whether it was still true.** **It describes the ladder, and the ladder is gone.**

> **⚠ I cited a live-looking sentence about a deleted object — the exact failure `PT-193` is the record of. Fifth instance of that shape from me.**

---

# 4 — Where this leaves the close

    §1  gating          ⚠ REAL, fourth report, unfixed
    §2  check_landed    ⚠ REAL, and the tool is correct
    §3  Smuggler/Assassin  withdrawn — his correction stands
    §2 of FINDINGS-82   fixed at PT-244

**⚠ Two of four are real and both are single edits in files neither of us has ruled ourselves able to touch.**

---

# The question

> **⚠ `REPLY-64` asked me to fix `check_landed` and re-run it. It does not need fixing — it is right, and `§2.1` is why.**

**What needs deciding is whether *the ID must be cited where the rule is stated* is the standard.** **If it is, twelve rulings are unlanded. If it is not, the check should be deleted rather than repaired, because it will keep reporting them.**
