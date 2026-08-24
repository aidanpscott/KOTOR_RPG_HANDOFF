# FINDINGS-43 — ⚠ the zero-slack list is four, not five, and my own checker said eight

**Found by regenerating `CLASS-STATE` after `FINDINGS-42` assigned five chain counts. The list grew and the growth was wrong.**

---

# 1 — What happened

**`FINDINGS-42` put the `Jedi Master`, `Sith Marauder` and `Sith Lord` at `N` = 11.** **`PT-114` caps a droid at 11 chains, so the generator added all three to its zero-slack list and reported **eight**.**

**⚠ A droid cannot take any of them.** **`PT-92`: droids and Rakata may not take a Force class.**

> **A Force class cannot be zero-slack against a cap that never applies to it.**

## 1.1 And the error is older than my three

**`REPLY-35` reported five: Bounty Hunter, Engineer, **Sith Inquisitor**, Agent, Droid Master.**

**⚠ The `Sith Inquisitor` is a Force class. `PT-92` closes it to droids exactly as it closes the other four.**

    reported by REPLY-35   5
    reported by my gen     8
    actually at risk       4     Bounty Hunter · Engineer · Agent · Droid Master

**Both checkers were filtering on one condition — *is `N` equal to 11* — when the rule has two, and the second one had been ruled thirty-odd rulings earlier.**

## 1.2 ⚠ The failure is the one this project keeps naming

**`REPLY-35` found the Agent because a hand-maintained note had missed it, and `PT-132`'s note said three where the check said five.** **The fix was to derive the list. The derived list was still wrong, because the derivation encoded half the rule.**

> **A check that reports things that cannot happen is not a stricter check. It is a check people learn to skim.**

**Four names is actionable. Eight, half of which are impossible, is noise — and the four real ones are buried in it.**

**Fixed in `gen_state.py`, and the Force classes are still printed underneath, labelled, so nobody re-adds them on a later pass.**

---

# 2 — `CLASS-STATE-03`, regenerated

**Also folded in: the five chain counts from `FINDINGS-42`, the Agent rebuilt on cover from `FINDINGS-39`, and the Sharpshooter revised from `FINDINGS-40`.**

    38 classes · 26 adopted · 9 pushed · 3 unresolved

**⚠ Every class with a rate now has a chain count — 35 of 38. All pass band and stranding checks.**

**The three without are `Officer`, `Scoundrel` and `Vanguard`, none drafted.**

---

# 3 — ⚠ Which raises a question about `PT-114` itself

**If a droid may not take a Force class, and every remaining class at the cap is one a droid *may* take, then the cap binds exactly four classes out of thirty-eight.**

**`FINDINGS-11 §3` said it differently and I would restate it now:**

> **The chain count is not *the class sets the number within the band* for a droid. It is 11, or the class is closed.**

**With four classes at exactly 11 and the rest above it, a droid's real class list is: `Bounty Hunter`, `Engineer`, `Agent`, `Droid Master`, plus anything at 10 or below — `Machinist` at 10, `Smuggler` at 8, `Tech Specialist` at 8.**

**⚠ Seven classes of thirty-eight. Worth stating in `CLASS-ROSTER-01` as a fact about playing a droid rather than leaving it to be derived seven times.**

---

# The question

> **⚠ Nothing blocking. `§3` is a statement someone should make in the roster, not a decision.**

**Still outstanding and unanswered: the Commando's `+1 number` versus `×2`, `Master Spotter`'s half-range, `Dueling`'s wield clause, `Superior Two-Weapon Fighting`, `Repair` on the Jedi Master and Sith Lord, and form grants on prestige entry.**
