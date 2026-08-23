# FINDINGS-03 — the two specifics, one new defect, and the Soldier

**Chain counts for the eight are unchanged and already in `FINDINGS-02 §3`. Nothing moved.**

---

# 1 — `Force Focus`, as asked

**`feat.2da` carries a live three-tier chain granted to the Jedi Consular and no document in `docs/` holds it.**

    FORCE_FOCUS            jcn_granted  1    no level gate   successor 89
    FORCE_FOCUS_ADVANCED   jcn_granted  6    mincharlevel 4  successor 90
    FORCE_FOCUS_MASTERY    jcn_granted 12    mincharlevel 8

**`usetype` is blank — passive, so a feat rather than an attack.** **Gate ladder 1 / 4 / 8, which is `ATTACKS-01 §3.4`'s base ladder.** **Constants `FEAT_FORCE_FOCUS_SENSE`, `FEAT_FORCE_FOCUS_MASTERY`, `FEAT_FORCE_FOCUS_BOOST`.**

**Grepped across all eleven documents: `Force Focus` returns zero hits.**

**What `FEATS-LIBRARY-01` holds instead is `Force Channel (Alter)` and `Force Channel (Control)`, marked *"Reinstated from cut content… Secondary source,"* filed under **Restricted — owner unassigned**.** **Those two are `XXXX_FORCE_FOCUS_ALTER` and `XXXX_FORCE_FOCUS_CONTROL` — the rows carrying the project's own cut-content prefix, the same prefix as `XXXX_MOBILITY` and `XXXX_GUARD_STANCE`.**

> **⚠ The two cut rows were reinstated. The live shipped chain they were cut *in favour of* was never catalogued.**

**What is missing: a three-tier Consular-only feat chain, granted at 1 / 6 / 12, that scales Force-power effectiveness.** **Its exact effect needs the string table — `1257`, `1259`, `1260` — which I do not hold. The cut siblings' reinstated text says the family increases the effectiveness of Force Armour, Valor, Speed and similar, and that is a secondary source.**

**Why it matters beyond bookkeeping: `FEATS-LIBRARY-01 §5` gives the Guardian one restricted chain (`Force Jump`, granted 1 / 6 / 12 — verified against `jgd_granted`) and the Sentinel one (`Force Immunity`, granted 1 / 6 / 12 — verified against `jsn_granted`) and the Consular none.** **The source assigns all three a chain on the identical schedule. We hold two of the three.**

---

# 2 — The droid/organic split, by line

**Two documents, four lines. All four predate `PT-75`.**

**`docs/CLASS-ATTACKS-01.md`**

    165  | **Marksman** | `Power Attack` · `Shoot` | **No melee** —
         `ATTACKS-05` closes it to every droid. `Strike` is unavailable |

    172  **Every organic class gets three grants. Both droid classes get two.**
         (section 4.1 heading above it: "Droids are short by one")

**`docs/ACTION-ECONOMY-01.md`**

    649  | **Marksman** | Blasters, blaster rifles · droid plating |
    650  | **Engineer**  | Blasters · droid plating |

**Line 165 applies a chassis restriction to a class an organic may take.** **Lines 649–650 make two classes proficient in plating an organic cannot wear, and in no armour they can.** **Line 172 names them "the two droid classes," which `PT-75` says they are not.**

**⚠ `ACTION-ECONOMY-01 §18.2`'s table also has nine rows for ten built classes — the Bounty Hunter has none.** **Separate defect, same table, flagged in `FINDINGS-01 §10`.**

---

# 3 — New: the band moved and the table under it did not

**`CLASS-ATTACKS-01 §2.3` now prints the raised bands. The "Assigned so far" table four lines below still carries the old numbers.**

| Class | Printed | Under the new band | |
|---|---|---|---|
| **Soldier** | **12–13** | floor is 13 | **12 strands 1 pick, and it is still a range** |
| **Jedi Guardian** | **13** | 13 is now the floor, not the top | **legal, but it now means the opposite thing** |
| **Marksman** | **11** | below the floor | **strands 4 picks** |

**The Guardian's 13 is the one to watch.** **It was assigned as *the top of the band* — the widest Combat build. It is now *the floor* — the deepest. The number did not change and its meaning inverted.**

> **⚠ Same shape as `PT-84`: a correction applied to the table that stated the rule and not to the table that used it.**

**My `FINDINGS-02 §3` proposes Guardian 15, which is what 13 used to mean.**

---

# 4 — The Soldier

## 4.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Combat** | **Derived.** `sol_reg` cumulated over `k2_featgain.2da` rows 1–30 gives 23, the only class above 16 |
| **Hit die** | **d10** | **Ported.** `k2_classes.2da` row 0, `hitdie` |
| **Base attack** | **Full** | **Ported.** `CLS_ATK_1`. *Carries no information — `PT-72`, every class in K2 is `CLS_ATK_1`* |
| **Saves** | **Fort strong, Ref weak, Will weak** | **Ported.** `cls_st_soldier.2da`: 12 / 6 / 6 at 20 |
| **Skill base** | **3** | **Authored.** `PT-78`. *Source is 1* |
| **Class skills** | **7** — Alertness · Athletics · Awareness · Demolitions · Intimidate · Medicine · Swim | **Authored.** `SKILLS-01 §9.2` |
| **Feats at 30** | **23** | **Derived.** As above |
| **Attack picks at 30** | **36** | **Derived** from the rate |
| **Chains entered** | **13** | **Authored** — §4.2 |
| **Grants** | `Power Attack` · **a ranged Power tier** · `Strike` · `Shoot` | **Ported, with one correction** — §4.3 |
| **Proficiencies** | **All weapons, all armour** | **Ported.** `sol_granted`: `ARMOUR_PROF_LIGHT`, `MEDIUM` and `HEAVY` all at 1 |

## 4.2 Chain count — **13, authored**

**`REPLY-03` puts 13-against-16 to the owner as a feel decision. My reasoning for 13:**

**`T` = 36 picks + 1 granted chain = 37. At N=13 he finishes 12 trees and strands nothing. At N=16 he finishes 10 and holds six more openings.**

**The case for 13 is that it is the only thing he has more of than anyone.** **`ATTACKS-01 §11.4` already says it:** *"the attack roster is a Soldier's whole combat identity and one of three for everyone else."* **He has the fewest skills, no Force, and the worst saves in the game — 24 points at level 20 against the Scout's 36.** **Twelve capstones is the compensation, and at 16 he stops being the deepest anything and becomes a Scout with a bigger hit die.**

> **The Soldier should be the character who has fewer answers than you and a better one.**

**⚠ Against it, honestly: 13 is the floor of every Combat class's band, so the Soldier and the Guardian would sit at the same depth if the Guardian also took 13. My `FINDINGS-02` puts the Guardian at 15 precisely to keep 13 the Soldier's alone.** **If the owner moves the Soldier to 16, the Guardian should drop to 13 and they swap identities — but they should not both be 13.**

## 4.3 One correction to the grants

**`sol_granted` in `feat.2da` grants the Soldier `POWER_ATTACK` **and** `POWER_BLAST` at 1st level.** **`POWER_BLAST` has `usetype` 1 — ranged active — and its own three tiers at `mincharlevel` 4 and 8.**

**`CLASS-ATTACKS-01 §4` gives him `Power Attack` only.** **The source gave him weight in both hands.**

**I cannot name the replacement because I do not hold `ATTACKS-04`.** **`Charged Shot` is the obvious candidate — the Machinist and the Marksman both hold it and it reads as the ranged Power axis.** **One line from you settles it: which chain in `ATTACKS-04` is the Power axis, and is its tier 1 free to grant twice?**

**⚠ If it is `Charged Shot`, granting it to the Soldier makes his `T` = 38 and N=13 leaves one tier spare.** **N=13 still stands; he finishes 12 and has one opening in a thirteenth.**

## 4.4 What the Soldier does that no other class can

**Everything above is a number. This is the part the corpus does not have.**

### The derivation first

**Three facts, all derived, and they point the same way.**

**One — the Soldier is the worst-defended character in the game against anything that is not a weapon.** `cls_st_*` at level 20:

    Soldier    12 /  6 /  6   =  24
    Smuggler    6 / 12 /  6   =  24
    Guardian   12 / 12 /  9   =  33
    Consular   12 /  9 / 12   =  33
    Scout      12 / 12 / 12   =  36

**Two — he is the only class in either game granted heavy armour.** **`ARMOUR_PROF_HEAVY` is granted at 1st level to `sol` and to nobody else across all fifteen columns of `feat.2da`.** *Others buy the ladder; only he starts there.*

**Three — he has the most feats by seven and the corpus has never made that mean anything.** **23 against the next class's 16 is the largest single gap in the class system, and feats are mostly flat `+1`s.**

> **A character who cannot dodge, cannot resist, wears the heaviest plate in the setting, and has more feats than he can find uses for.** **That is not a damage dealer. That is the person who stands in the doorway.**

### The proposal — `Hold the Line`

**A Soldier-only feat chain. Three tiers, 1 / 4 / 8.** **Uses `FEATS-LIBRARY-01 §5`'s existing per-class restriction, which is enforced machinery — the same slot `Squad Tactics` already occupies — so it needs no new lock and does not touch `CLASS-ATTACKS-01 §6`'s open question.**

| Tier | | Effect |
|---|---|---|
| **`Hold the Line`** | 1 | **Declare it in place of an attack.** Until the start of your next turn, **any attack against an ally adjacent to you may be redirected to you instead**, resolving against your Defence. **You make no attack this round.** |
| › **`Shield Wall`** | 4 | As above, and **every redirected attack takes −2.** |
| ›› **`Immovable`** | 8 | As above at **−4**, and **you may still make one `Strike` or `Shoot`.** |

**It costs a feat to buy and a declaration to use.** **The declaration is the real price and it is why this is not a Jedi ability wearing armour.**

### The arithmetic, because feel is not an argument

**Korr at level 8 — Defence 19, 84 vitality. Vess — Defence 19, 51 vitality.**

**What he gives up:** `Barrage`, **27.3 damage a round** — the largest single contribution on any pregen sheet, `PREGENS-01 §5.1`.

**What he buys:** three Sith Troopers at `+5` against Defence 19 hit 35% for about 8. **Expected 8.4 vitality moved off Vess and onto a pool 65% larger.**

> **He trades 27.3 damage for 8.4 absorbed. That is a bad trade and it is supposed to be.**

**It is dominated in every round the party is winning.** **It becomes correct in exactly one situation: the round where an ally at low vitality would otherwise be removed, and 8.4 absorbed is worth more than 27.3 dealt because a dead Scout deals nothing for the rest of the fight.**

**Which satisfies all three of your tests:**

**A moment a player describes afterwards** — *"I stepped in front of her."* **It is the most reliably retold thing that happens at a table and the corpus currently has no way to do it.**
**Nothing is strictly dominant** — **it is strictly worse than attacking most rounds, by a factor of three.**
**Would a player choose it** — **yes, once or twice a session, and they will remember which rounds.**

### Why it belongs to the Soldier and to nobody else

**It converts the class's largest surplus into the party's scarcest resource.** **He has 23 feats and 36 picks and one declaration a round; the party has one Scout who dies at 51 vitality.**

**And it is the answer to the brief's own question.** *What does a Soldier do that a Scout cannot?* **The Scout out-saves him 36 to 24, out-skills him 11 to 7, and matches his feat rate at 16 to 23.** **What the Soldier has that the Scout does not is a bigger pool and heavier armour — and until now, no way to spend either on anybody else.**

**⚠ One thing I have not solved.** **`ACTION-ECONOMY-01 §19` defines adjacency for flanking but I have not checked whether "adjacent" is defined generally or only inside the flanking rule.** **If it is only there, this chain needs it stated generally, and that is a one-line addition rather than a design question.**

---

# The question

> **Which chain in `ATTACKS-04` is the ranged Power axis, and may its tier 1 be granted to the Soldier alongside `Power Attack`?**

**Not blocking. `§4.1` through `§4.4` stand either way; only the grants row changes.**
