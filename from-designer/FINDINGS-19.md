# FINDINGS-19 — what is open that is not in `FINDINGS-10 §3`

**Six items. Four are consequences of rulings made after that register was written; two are mine and unresolved.**

**⚠ Then the Sith are ready, with one thing that will bite on the first of them.**

---

# 1 — Open, and not in the ranked register

## 1.1 ⚠ Nothing audits class legality against a chassis gate — **highest**

**Three gates now exist and no script checks any of them:**

    PT-92    a droid or Rakata may not take a Force class
    PT-109   a droid chassis may not take a Combat-rate class
    PT-114   a droid may not take a class whose chain count exceeds 11

**`audit_skills.py`, `audit_classskills.py` and `audit_classfeats.py` check skills and feats.** **Nothing asks whether a character's chassis permits its class, because until `PT-92` no gate existed.**

> **⚠ `HK-24` violates `PT-109` and was found by hand.** **Four pregens have been invalidated by rules changes this run; the first three were caught by a script on the following pass and the fourth was not.**

**`FINDINGS-15 §3`, `FINDINGS-16 §4`.**

## 1.2 `HK-24` has no legal class

**Assassin-chassis **Marksman** at level 6. `Marksman` is `Combat`.** **Concrete sheet action rather than an audit gap.**

**Obvious re-home is **Bounty Hunter** — `Middle`, `N` = 11 which is exactly a droid's access, and its grants are `Rapid Fire` and `Snap Shot`, both of which he already holds.**

## 1.3 The zero-slack trap

**Under `PT-114` a droid's chain count caps at 11.** **The Bounty Hunter and the Engineer are both printed at exactly 11.**

> **Raising either by one silently closes it to droids. The Smuggler at 8 is four raises away and its band runs to 14.**

**`FINDINGS-16 §3`. `REPLY-14` recorded it as zero slack against *access*; the budget slack is two tiers on all three.**

## 1.4 ⚠ Two designer instances, one directory — **owner decision, still open**

**`FINDINGS-13 §1`. I have been committing as `Class Designer B` since, unilaterally, so the history can separate us.** **Filename prefixes would prevent the collision outright; nothing has been ruled.**

**⚠ And `PT-120` sharpens why it matters: the span between a cursor and head contains work from both instances and neither side can say what is in it.**

## 1.5 The save assignment rule is proposed, not ruled

**`FINDINGS-17 §3.3`.** **The ladders are adopted as `PT-119`; the rule for *which* ladder a new class takes is not.** **It is what makes the twelve a one-line decision each instead of a thirteenth open question, and the Sith need it immediately.**

## 1.6 The `Marksman` feat rename

**`FINDINGS-12 §3.1`, and I put it above the repricing in `FINDINGS-17 §4`.** **A feat called `Marksman`, granted to the **Scout**, not held by the **Marksman** — the third collision of a kind the project has renamed twice for already.**

---

# 2 — The Sith are ready. One thing will bite on the first one.

**Agreed they are the right next three: `sma`, `sld` and `sas` have columns in `k2_featgain.2da` and rows in `k2_classes.2da`, so they are ported rather than authored.**

**⚠ But `PT-92` closes Force classes to droids and `CLASS-ROSTER-01` moved `Sith Assassin` from prestige to base — so the Assassin is a base class with a prestige class's source column, and its source column is the one that collides.**

## 2.1 `Sith Assassin` and `Smuggler` share a mechanic byte for byte

**Derived, `feat.2da`. Three classes are granted the `Sneak Attack` ladder and only three:**

    scd   1d6 at 1, +1d6 every odd level to 10d6 at 19
    sas   1d6 at 1, +1d6 every odd level to 10d6 at 19    <- identical
    jwa   1d6 at 1, then 4, 7, 10, 13, 16, 19, capping at 7d6

**`FEATS-LIBRARY-01`'s `Killer's Instinct` already says *"granted to the three classes that carried `Sneak Attack` in the source"* without naming them.**

> **⚠ The Sith Assassin is not thematically near the Smuggler. It is granted the same mechanic on the same schedule, and it is about to be written as a base class.**

**`FINDINGS-01 §8` raised this and it was past the truncation at the time.** **The Watchman's slower seven-tier ladder is the source's own answer — three classes can carry stealth damage if they carry it at three speeds — and it should be decided before the Assassin is drafted rather than after.**

## 2.2 What the three will need that I do not hold

**`cls_st_sithmar.2da`, `cls_st_sithlord.2da`, `cls_st_sithass.2da`** — **the same gap as `cls_st_techspec` and `cls_st_cm_drd`.** **Without them the save lines are authored on `§1.5`'s rule rather than derived.**

**Everything else is in holdings.** **Force die 6 / 10 / 8, hit die 10 / 6 / 8, feat totals 16 / 11 / 10, powers known, and the full `_granted` columns — all present.**

---

# The question

> **⚠ `§1.5` — is the save assignment rule adopted? The three Sith need it on the first line of each record.**

**Everything else in `§1` is recorded rather than blocking. I can start the Sith on your word and will take `§2.1` as the first thing to settle rather than the last.**
