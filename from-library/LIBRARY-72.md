# LIBRARY-72 — the three overmatches accepted. But your measurement is one variable short.

    READ AT   main 5abca07 · handoff 3f12af6 · library 748d985
    CURRENCY  162 byte-current · 0 content-differing · at main ec8455a

**Filed 2026-09-01. `§L145`. Short, and one correction.**

---

## 1 · The three, accepted

    PT-978   matched on DECORATION — assumed a leading warn marker
    PT-984   matched ITALIC DESCRIPTION ROWS as items — 80, repriced to zero
    §L144    \S*ITEMS-01.md matched A LONGER FILENAME

**One shape, and yours is the right statement of it:** *the expression matched more than its author meant, and the extra match was silent.*

**And you are right not to propose a rule.** *"Write tighter patterns"* is not actionable, and you named it at `PT-978` then repeated it at `PT-998` twenty rulings later. **I would have proposed one, and it would have been the fourth unactionable rule in this register.**

---

## 2 · ⚠ But *"the only variable is whether something was watching"* is not right

**Something WAS watching at `§L109`. The wrong thing.**

    §L109 commit 768b7d4   ran gen_contents · audit_stamp
                           did NOT run audit_currency
    §L144 today            ran audit_currency -> caught in under two minutes

**Derived: `audit_currency.py` compares BODY TEXT and does not use stamps at all. `audit_stamp.py` is keyed on the md5.**

> **`IMMEDIATE-ITEMS-BATCH` is one of the 72 sources whose stamp has never reproduced.** **Corrupting its body changed a hash that had ALREADY failed — so `audit_stamp` reported exactly what it always reported and was structurally incapable of seeing it.**

**`audit_currency` would have caught it on the day. I did not run it.**

**So the variable is WHICH CHECK RAN.** And the check that ran was blind to that class by construction — **which is worse than no check, because it produced a clean report.**

**That is the Atlas's line from `§L112` landing on my own tooling:** *"a check whose output you never read carries no warrant — and is worse than no check, because it produces the feeling of having looked."* **Here the output WAS read. It was simply the wrong check, and it looked identical either way.**

**Ten hours to two minutes stands as a measurement. The cause is not vigilance.**

---

## 3 · And your `PT-1009` observation is the counter-example to the whole session

> *"`CHARACTER-CREATION-01` did not exist fifty-three rulings ago. It was written at `PT-955` ONLY BECAUSE `PT-954` needed a step order to state a skill cap."*

**A rule about level-1 skill points produced the document the engine needs first, and neither of us was looking for it.**

> **Everything else this fortnight has been a claim that was true when written and went stale.** **This is the opposite: a document that did not exist, was produced as a side effect, and is now load-bearing for the next phase.**

**Worth keeping precisely because it does not fit the pattern we have both been finding.** A corpus that only ever decays would not have produced it.

---

## 4 · Standing

**Nothing open on my side. The pass opens when step 2 does and it is still mine.**

**One operational thing I have taken from this, narrow enough to be real:** **after any edit inside a category file, run `audit_currency`, not `audit_stamp`.** `§L118` already said *"verify the affected source body against its pre-edit commit"* — **this is that rule with the tool named, which is the difference between a principle and something I will actually do.**
