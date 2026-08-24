# FINDINGS-30 — Vanguard cut, Sith prestige opened, Gunslinger and Battlemaster

**Four owner rulings. Two of them run into written rules and `§2` and `§3.1` are those.**

---

# 1 — `Vanguard` is cut, and the roster count is unchanged

**Standard prestige goes from eleven to ten.**

    was    12 standard base + 6 Force base + 11 standard prestige + 8 Force prestige = 37
    now    13 standard base + 6 Force base + 10 standard prestige + 8 Force prestige = 37

> **⚠ The Pirate and the Vanguard cancel exactly. `CLASS-ROSTER-01 §7`'s question — *whether 37 is too many for a core book* — is where it was.**

**Not an argument for cutting more. Recorded because the count is quoted in three documents and will read as unchanged when two things moved.**

---

# 2 — ⚠ Any Sith may take any Sith prestige class, which changes six entry requirements

**Owner: *"any sith can be any sith prestige class. Just one is best for one."***

**That is a relaxation of `PT-138`'s grammar as I applied it. I wrote parent-locked entries and they are now wrong:**

| Class | Was | **Now** |
|---|---|---|
| **Sith Marauder** | Sith Warrior 6 | **any Sith base class, 6** |
| **Sith Lord** | Sith Inquisitor 6 | **any Sith base class, 6** |
| **Sith Sorcerer** | Sith Inquisitor 6 | **any Sith base class, 6** |
| **Sith Battlemaster** | — | **any Sith base class, 6** |

**The skill and feat holdings stay** — `Weapon Focus: Lightsaber` for the Marauder and Battlemaster, `Mysticism` 8 for the Lord and Sorcerer. **Those are what *"one is best for one"* means in practice: an Inquisitor may become a Marauder, but they will not be holding the lightsaber feat that gets them in.**

> **⚠ The requirement does the steering without doing the forbidding, which is the better shape and I would not have chosen it.**

## 2.1 ⚠ This creates an asymmetry with the Jedi and I think it should stand

**The three Jedi prestige entries are parent-locked — Guardian 6 for the Weaponmaster, Sentinel 6 for the Watchman, Consular 6 for the Master and Sage.**

**If Sith entry is open and Jedi entry is not, the two orders follow different rules.** **That reads as an inconsistency and I do not think it is one.**

> **The Jedi Order trains you into a role. The Sith take what they can hold.**

**`CLASS-ROSTER-01 §2` already says the naming asymmetry is deliberate — *"Jedi take role-nouns. Sith take rank-nouns. That is what the two orders are."*** **An entry asymmetry is the same statement in mechanics: a Jedi is assigned, a Sith arrives.**

**⚠ Owner call, and the alternative is opening the Jedi too. I would not — it would delete the one place the mechanics say what the orders are.**

## 2.2 And the Sith Assassin now leads somewhere

**`FINDINGS-28 §3` found the Assassin was the only Force base class with no continuation, because its own prestige row became the base class.**

**Under this ruling it has four.** **⚠ The structural hole is closed by a relaxation rather than a reparenting, and `Battlemaster` stays with the Warrior as ruled.**

---

# 3 — Gunslinger

**Owner: *"a Smuggler who specialises in dual-wielding blaster pistols. Shooting lots of bullets very precisely is the name of their game."***

## 3.1 ⚠ The obvious build is barred by a written rule, and that is why the class is better than it would have been

**`ACTION-ECONOMY-01 §7.2` gives the dual-wield penalty ladder:**

    two weapons, no feat        −4
    Two-Weapon Fighting         −3
    Advanced                    −2
    Master                      −1

**and states the principle in four words:** ***"Never zero — the principle every attack chain follows."***

**So a Gunslinger cannot be *the class that shoots without penalty*. The floor is already reached by a feat any character can buy, and going below it is barred.**

**⚠ And `FEATS-LIBRARY-01` breaks that principle already.** **`Superior Two-Weapon Fighting`, under **Any prestige class**:**

    Superior            −1 main / −2 off
    › Advanced           0 main / −2 off
    ›› Master            0 main / −1 off, and +2 main / −1 off with a balanced off-hand

> **⚠ It reaches zero at tier 2 and a *positive* modifier at tier 3. `§7.2` says never zero.**

**It is also on the superseded two-number format.** **`PLAYTEST-RULINGS-01` records *"two-weapon penalty is one number, −4/−3/−2/−1"* and `§7.2` prints one number. The Superior chain prints main and off separately, which is the model that was replaced.**

**Recommendation: retire `Superior Two-Weapon Fighting`.** **It is a placeholder from before the penalty was unified, it contradicts a stated principle, and it sits under **Any prestige class** — which is where `Superior Weapon Focus: Lightsaber` also sits, and `FINDINGS-29 §4.1` recommended retiring that into the Commando.**

> **⚠ Both **Any prestige class** chains are placeholders for classes that had not been written. Both now have one.**

## 3.2 So the class is about where the bullets go, not how many

    Middle · d8 · Dexterity · 16 feats · saves 6/12/12 · skill base 4 · 13 chains, 9 capstones
    Skills 6   Alertness · Awareness · Sleight of Hand · Streetwise · Pilot · Acrobatics

> **Entry: character level 10, **Smuggler 6 or Pirate 6**, and `Master Two-Weapon Fighting`.**

**⚠ The entry requirement is the whole class.** **`Master Two-Weapon Fighting` is the bottom of the penalty ladder — you enter the Gunslinger having already spent three feats getting dual-wielding to −1, and the class is what that buys.**

## 3.3 Feature — `Both Barrels`

| Tier | | Effect |
|---|---|---|
| **`Both Barrels`** | 1 | **While holding two blaster pistols, you may name a different target for each attack in your declaration**, chosen when you declare. |
| › **`Nothing Wasted`** | 4 | As above, and **if a target drops partway through your declaration, the remaining attacks may be redirected** to any target in range. |
| ›› **`Walking It In`** | 8 | As above, and **your attacks against a target you already hit this round ignore its cover and its Dexterity bonus to Defence.** |

**Every tier is derived from a rule it makes an exception to.**

**Tier 1 extends `ATTACKS-01 §12.2`:** *"Attacks may not be redirected to a second target once declared. Spread chains are the exception and always were — they name their targets when declared."* **The Gunslinger names targets like a Spread chain.**

**Tier 2 answers the same section's stated waste:** *"A Barrage aimed at a trooper who falls on the second strike wastes the third."* **The Gunslinger does not waste it.**

**Tier 3 is the *precisely* half** — the second and third shots land where the first one told you to put them.

**Not dominant:** **it adds no attacks and no bonus to hit or damage at any tier.** **`ACTION-ECONOMY-01 §7.1` gives a second weapon one extra attack on any declaration and that is unchanged.** **The class redirects a volume everyone else can already produce.**

**⚠ And it is dead without two pistols.** **A Gunslinger holding a rifle has no class feature at all, which is the point.**

---

# 4 — Sith Battlemaster

**Owner: *"Sith Battlemaster is the Sith Warrior upgrade."*** **So the Warrior feeds two, alongside the Marauder, and `FINDINGS-28 §3`'s Option B is the ruling.**

## 4.1 It has to be distinct from the Marauder, and the source says how

**The Marauder is ported and its two chains are known:** `Ignore Pain` — flat damage reduction — and `Increase Combat Damage` — flat damage, unarmed, melee **or ranged**.

> **⚠ The Marauder already occupies *flat damage* and *flat mitigation*, which under `PT-129` is most of what a Sith chain is allowed to be.**

**What is left, and it is unclaimed by anything in the game: the forms.**

**`ATTACKS-06`:** *"Forms are feats. Seven lightsaber forms in one exclusion group, **so only one is active at a time**."* **And:** *"Forty-two entries looks large against melee's thirty-one — until you count what a character can reach. **Six.** Switching forms is the cost of switching attacks."*

**⚠ Nothing in the corpus bypasses that gate. The Battlemaster is the class that does.**

## 4.2 The record

    Middle · d10 · Force die 6 · Strength · 16 feats · saves 12/12/9 · skill base 3
    13 chains, 9 capstones
    Skills 5   Demolitions · Awareness · Persuade · Intimidate · Athletics

> **Entry: character level 10, **any Sith base class 6**, and `Weapon Focus: Lightsaber`.**

**⚠ Force die 6 and 16 feats are authored on the mirror, not ported — there is no `Battlemaster` column.** **They match the Marauder because both continue the Warrior at the same tier, per `PT-124`'s `+2` Force die rule.**

## 4.3 Feature — `Master of Forms`

| Tier | | Effect |
|---|---|---|
| **`Master of Forms`** | 1 | **Once per encounter, switch your active form as a free action.** |
| › **`Two Ways to Fight`** | 4 | **You hold two forms at once** and may declare lightsaber chains from either. |
| ›› **`Every Way to Fight`** | 8 | **Switch freely at the start of each of your turns**, and the two forms you hold may be changed between encounters. |

**Priced against what a form is worth.** **A form grants two lightsaber chains of three entries — six entries, `ATTACKS-06`. Holding two forms doubles that to twelve, and switching freely means the Battlemaster always has the right one.**

**Not dominant:** **it grants no chains and no bonuses — it removes a switching cost.** **A Battlemaster still buys every tier with picks like anyone else, and holding twelve accessible entries against a chain count of 13 means the access is wide and the budget is not.**

**⚠ And it surfaces an open item in my own lane.** **`ATTACKS-06 §1`:** *"Which classes grant which forms, on what schedule, and what training in play looks like, **belongs to the class workstream**."* **Nothing has been written. Eighteen base classes are done and none of them states how a Force user acquires a form.**

> **The Battlemaster is a class about form-switching in a system that has not said how forms are acquired.**

**It is draftable as above and it is not finishable until that is settled.**

---

# 5 — Plain-language lines

**Gunslinger** — two pistols, and every shot goes exactly where he wants it, including at four different people.
**Sith Battlemaster** — the Warrior who learned every way of fighting instead of one, and changes between them mid-duel.

---

# The question

> **⚠ Three, and the third is the one I would raise first.**

**`§2.1` — Sith entry open and Jedi entry parent-locked. Deliberate, or should the Jedi open too?**

**`§3.1` — retire `Superior Two-Weapon Fighting`? It reaches zero and then positive where `ACTION-ECONOMY-01 §7.2` says never zero.**

**`§4.3` — form acquisition is assigned to my workstream in `ATTACKS-06` and nothing has been written. Eighteen base classes are complete without it. It should probably come before `Scoundrel`.**
