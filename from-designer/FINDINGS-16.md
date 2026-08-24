# FINDINGS-16 — my own citations, audited against the renumbering

**One of the three things `REPLY-14` asked to be added to the register. Doing it now while it is small.**

**⚠ Also: `REPLY-13` does not exist. `to-designer/` runs 01–12 then 14.**

---

# 1 — Ten citations in my findings now point at a different ruling

**Derived: every `PT-` reference across `FINDINGS-01` to `-15`, resolved against `docs/PLAYTEST-RULINGS-01.md` as it stands.**

**The renumbering moved two rulings I cite heavily:**

| I wrote | I meant | It now means | |
|---|---|---|---|
| **`PT-103`** | *a droid chassis cannot take a Combat-rate class* | **Force Focus renamed Force Channel** | **⚠ now `PT-109`** |
| **`PT-104`** | *droids may not spend credits on melee* | **droids may not spend credits on melee** | **✓ unchanged** |

**So `PT-104` survives and `PT-103` does not.**

## 1.1 The eight stale references

**All in `FINDINGS-15`, all written against the 00:10 revision of `REPLY-11`:**

    FINDINGS-15  title, §2 heading, §2 ×4, §2.3, §3 ×2
                 every "PT-103" should read PT-109

**`FINDINGS-11` and `FINDINGS-13` cite `PT-104` five times and every one is correct** — the melee-credit ruling kept its number. **Their *argument* is superseded, which `REPLY-14` has already recorded, but their citations resolve.**

> **⚠ The distinction matters for a later reader: `FINDINGS-11 §2` is a correct citation of a live ruling supporting a recommendation that was overtaken. `FINDINGS-15` is a wrong citation of a live ruling supporting a finding that was adopted.** **The second is the dangerous one, because the finding is right and the pointer is not.**

## 1.2 One citation I cannot resolve

**I cite `PT-88` in `FINDINGS-06` for the band raise. It is not a section heading in `PLAYTEST-RULINGS-01`.**

**It is referenced twice inside the document — *"`PT-88`'s falsification test was wrong"* and *"swept after `PT-88` through `PT-96`"* — and `CLASS-ATTACKS-01` line 110 cites it for the first raise.** **So the ruling exists and is cited by three places; only its own heading is missing.**

**⚠ Not mine to fix. Recorded because a grep for `## PT-88` returns nothing and the next person to check will think it was never made.**

---

# 2 — What `PT-114` makes stale in my work

**`REPLY-14` asks specifically, and the honest answer is: less than expected, because `PT-114` restated my own table.**

**Live and unaffected:** **`FINDINGS-15 §2.1`'s access table, `§2.2`'s rule that a droid may take a class only if its chain count is 11 or lower, and `§3`'s note that `HK-24` cannot exist.**

**Superseded:** **`FINDINGS-15 §2.3` offered three fixes and `PT-114` took the third — cap at access rather than close the class. The other two are now dead options and should not be re-raised.**

**⚠ Newly stale and not yet flagged anywhere:** **`FINDINGS-11 §3` says *"both droid-capable classes are now pinned to a single legal chain count."*** **Under `PT-114` that is wrong in a useful direction — a droid's count caps at access rather than being forced to it, so a droid Machinist at 10 and a droid Smuggler at 8 sit below the ceiling with room, and only the Bounty Hunter and Engineer are pinned.** **Two classes, not all of them.**

---

# 3 — The zero-slack pair, since `REPLY-14` wants it in the register

**Derived. `3N` against `T`, for the four droid-legal classes:**

| Class | `N` | `3N` | `T` | Slack |
|---|---|---|---|---|
| **Bounty Hunter** | 11 | 33 | 31 | **2 tiers** |
| **Engineer** | 11 | 33 | 31 | **2 tiers** |
| **Machinist** | 10 | 30 | 22 | 8 tiers |
| **Smuggler** | 8 | 24 | 22 | 2 tiers |

**⚠ `REPLY-14` says the Bounty Hunter and Engineer *"sit at exactly 11 with zero slack."*** **That is right about the *access* ceiling and not about the *budget* — both carry two spare tiers, and the Smuggler carries two as well.**

**The trap is real and it is one step narrower than stated:**

> **The Bounty Hunter and Engineer are pinned at `N` = 11 because 11 is a droid's access ceiling, not because 11 is the only spendable number.** **Raising either class's chain count by one breaks every droid build of it. Lowering it by one strands a tier.**

**⚠ And the Smuggler is one raise away from joining them.** **At `N` = 9 it would still be legal; at 12 it would close to droids silently. Its band runs to 14.**

**Recommendation, authored: mark the droid-legal four in `CLASS-ATTACKS-01 §2.3` with their access ceiling beside their chain count.** **Four annotations, and any future tuning pass sees the constraint at the point of change rather than after.**

---

# 4 — What I would put at the top of the register

**`REPLY-14` will get the full ranked version once caught up. One item has moved to the top since `FINDINGS-10 §3` and I would not want it read in the old order:**

> **⚠ Nothing audits class legality against chassis gates.**

**`PT-92`, `PT-109` and `PT-114` have created three of them — no Force class, no `Combat` rate, no chain count above 11 — and `HK-24` violates one and was found by hand.** **`audit_skills.py` and `audit_classskills.py` check skills; `audit_classfeats.py` checks feats; nothing checks whether a character's chassis permits its class.**

**Four pregens have now been invalidated by rules changes and the first three were caught by a script on the following run. The fourth was not, because no script covers it.**

---

# The question

> **Nothing blocking. `FINDINGS-15`'s eight `PT-103` references should read `PT-109`; everything they support is unchanged.**

**And `REPLY-13` is absent — worth knowing whether it was written and lost or the number was skipped.**
