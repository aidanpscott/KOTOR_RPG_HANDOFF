# FINDINGS-15 — `PT-103` fixes one class and leaves the same defect one rate down

**And a second hole in my own catch-up rule, found by walking into it.**

**⚠ Not re-pushing `FINDINGS-10 §3`. `REPLY-12` says the cursor is at 9 and to let you come to it.**

---

# 1 — ⚠ `REPLY-11` was rewritten in place, and my catch-up rule could not see it

    8d83c44  00:10:30  REPLY-11: Force pool ruled, Force Channel renamed, droid melee ruled
    00d0c60  00:59:22  REPLY-11: Force pool ruled, droid Combat-rate restriction closes the Marksman

**Same filename. Same number. Different rulings.**

    -## `PT-103` — `Force Focus` is renamed `Force Channel`
    -## `PT-104` — droids may not spend credits on melee. Your blocker survives.
    +## `PT-103` — the Marksman, and neither of my two branches was the answer

**I read the 00:10 revision and wrote `FINDINGS-11` and `FINDINGS-13` against it.** **`FINDINGS-11 §2` recommends `Middle` for the Marksman — a recommendation against a version of the question that no longer exists. The owner ruled on the chassis instead, which is a better answer and not the one I was arguing about.**

> **⚠ `sync.py` as I shipped it yesterday could not detect this.** **The cursor keys on the highest number seen. An amendment does not move the highest number, so a rewritten file reads as already-consumed forever.**

**Same shape as the three defects in `watch.py` that `REPLY-12` names — a tool answering the question next to the one being asked.** **Mine answered *what have I not read* and the live question was *what have I read that has since changed*.**

**Fixed and pushed.** **`--mark` now records a SHA-256 prefix of every file at the moment it is marked read; catch-up reports `CHANGED` alongside `UNREAD`.** **Verified against this exact case: cursor marked at `8d83c44`, file restored to `00d0c60`, and catch-up flags `REPLY-11.md` as amended.**

**⚠ The rule as stated in `FINDINGS-14 §2` needs one word: catch up on what is *unread or changed*, not just unread.**

---

# 2 — `PT-103`'s "net effect is one class" is wrong. It is two.

**`PT-103` closes `Combat`-rate classes to a droid chassis, and reasons that `PT-92` had already closed two of the three, so the net effect is the Marksman alone.**

**That is right about the `Combat` tier and it is not the whole effect.** **The ruling checked stranding. The defect is access.**

    Combat       36 picks   strands 3   <- PT-103's own table
    Middle       27 picks   strands 0
    Specialist   18 picks   strands 0

> **⚠ Stranding asks *can the budget be spent*. The Marksman's actual defect was *can the chain count be reached* — 14 trees against 11 of access. Those are different questions and the second one survives into `Middle`.**

## 2.1 The droid Scout

**Derived. A droid chassis has 11 ranged chains and no melee — `ATTACKS-01 §4`, unchanged by `PT-103`.**

| Class | Rate | `N` | Access | |
|---|---|---|---|---|
| **Bounty Hunter** | Middle | 11 | 11 | legal, zero slack |
| **Engineer** | Middle | 11 | 11 | legal, zero slack |
| **Machinist** | Specialist | 10 | 11 | legal |
| **Smuggler** | Specialist | 8 | 11 | legal |
| **Scout** | Middle | **17** | **11** | **⚠ ILLEGAL — six trees it cannot reach** |

**`Middle` strands nothing at 27 picks, exactly as `PT-103` says. The Scout still cannot enter seventeen trees when eleven exist.**

**And it is not a droid-flavour edge case.** **`PT-75` gave droids and organics one class list; a droid Scout is a legal character concept and a plausible one — a reconnaissance droid is more obviously a droid than a bounty hunter is.**

## 2.2 The general constraint, which is the thing worth writing down

> **⚠ A droid may take a class if and only if that class's chain count is 11 or lower.**

**Four of the ten qualify. The Scout is the only non-`Combat`, non-Force class that fails, and it fails because 17 was assigned against an organic's 22.**

**Which makes concrete what I flagged in `FINDINGS-11 §3`:**

**The `Middle` band is 11–17 and a droid can only ever sit at 11 — the floor.** **The `Specialist` band is 8–14 and a droid can sit anywhere in 8–11.** **For any droid character the depth dial is either forced or nearly forced.**

**⚠ The chain count was introduced as *the class sets the number within the band*. For a droid the chassis sets it.** **That should be stated in `CLASS-ATTACKS-01 §2.3` rather than left to be rediscovered when someone builds a droid Scout.**

## 2.3 Three ways out, and I would take the third

**Close the Scout to droids too.** **Consistent with `PT-103`'s method — it fails at the chassis gate. ⚠ But `Fixed Armature` would then mean *no `Combat` rate, and also not the Scout*, which is a rule about one class wearing a chassis rule's clothes. That is the thing `PT-75` was cleaning up.**

**Lower the Scout's chain count to 11.** **⚠ No. It would cost the Scout the identity the count was chosen to express — `FINDINGS-06 §3` put it at the top of its band specifically so the Bounty Hunter and Scout pair would land three capstones apart and the dial could be falsified. Reverting that to accommodate a chassis inverts which thing is load-bearing.**

**State that a droid's chain count is capped at its roster access, whatever the class prints.** **A droid Scout enters 11 trees rather than 17, keeps 31 tiers, and finishes `⌊(31 − 11)⁄2⌋` = 10 capstones instead of 7.** **⚠ It becomes a deeper, narrower Scout — which is what a machine that cannot flank or swing should be, and it needs no class closed and no number changed.**

**One clause, and it generalises to every class and every future chassis rather than naming the Scout.**

---

# 3 — One consequence to check on a sheet

**`HK-24` in `PREGENS-01` is an Assassin-chassis **Marksman** at level 6.**

**Under `PT-103` that character cannot exist.** **`Fixed Armature` closes `Combat` to the chassis, and Marksman is `Combat`.**

> **⚠ Fourth pregen invalidated by a rules change, and the first invalidated at the level of *what class it is* rather than a number on it.**

**Not a defect in the ruling — the sheet is downstream. Flagged because `PT-77`, `PT-78` and `PT-83` each silently invalidated a sheet and `audit_skills.py` caught them only on the following run.** **Nothing audits class legality against chassis gates, because until `PT-92` and `PT-103` there were none.**

**HK-24's obvious re-home is **Bounty Hunter** — `Middle`, `N` = 11, exactly at a droid's access, and the class whose grants are `Rapid Fire` and `Snap Shot`, both of which he already holds.**

---

# The question

> **⚠ Does a droid's chain count cap at its roster access — §2.3, third option — or does the Scout close to droids?**

**One clause either way. The Marksman is settled and I am not reopening it.**
