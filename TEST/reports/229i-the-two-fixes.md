# TEST 229-I: the stand-up wording and Great Cleave's hover

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are `t229i-*` in `KOTOR_RPG_MAIN_WORK/media/screens/test-229/` (MAIN_WORK `cca4584c`).

## Which build ran what

- **Step I only: app main `a46ca98`**. `gate.py --at a46ca98`: "FOR TESTER — CORE at a46ca98, 5556 tests, 0 failed"; ARCHIVE last green at a46ca98. Lodestar `4199fd7` = lock. Defaults. **Shelf** `4f15356`, synced; check_shelf clean. Saves rewritten with the same tool.
- **A to H: app main `0f8ae8e`**, Shelf `a1f1bab`, as filed in TEST 229 and accepted there.

## Summary: both pass

| # | Check | Result |
|---|---|---|
| I.1 | Sweep Plain | **PASS**. "Sweep Attack · … against 14 — win · … prone · cannot stand". End Turn: the box reads "Brute cannot stand", and Messages > Combat ends "Brute cannot stand". No "still" anywhere in the log |
| I.2 | Cleaver | **PASS**. I set it up rather than waiting on the yard: kill the Weakling, then step Left onto its square, which leaves the Brute exactly 2 squares off along the row. **Control**, nothing declared: hover draws a path, "1 square · 3 left". **Great Cleave** (x three times): hover draws no path and no step count, "95% (needs 2+) / +8 attack · +3 Strength · −1 Great Cleave, against Defense 10". The click strikes with no step and she stays on her square: "Great Cleave · Brute · … hit · damage 6 … 394 left", then "Ironhide · … miss", then "Gunman · … hit · damage 8 … 392 left". The log has no opportunity attack after the click |

Not tried: the two TEST 229 findings on this build, since their fixes come with TEST 230.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
