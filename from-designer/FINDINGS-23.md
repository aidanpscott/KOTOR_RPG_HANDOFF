# FINDINGS-23 — Inquisitor closed. Four authored classes. And `PT-123` does not cover Intelligence.

**Owner ruled 41. `§1` is a gap that blocks one of the four; `§2` is the frame; `§3`–`§6` are the classes.**

---

# 1 — ⚠ `PT-123` maps four abilities and there are six

**`CLASS-TABLES-BASE`, as written:**

    Strength or Constitution primary  ->  Fortitude
    Dexterity primary                 ->  Reflex
    Wisdom or Charisma primary        ->  Will

> **⚠ Intelligence is not mapped, and neither is a class with no clear primary.**

**It did not surface on the ten because none of them is Intelligence-primary — `k2_classes.2da` gives `INT` as primary to no class in either game.** **The **Explorer** is, and so is any future scholar or slicer.**

**Proposal, authored: `Wisdom, Charisma or Intelligence → Will`.**

**Reasoning: Will is the mental save, and the split between the three mental abilities is about *what you know* versus *what you sense* versus *who you are* — none of which is a different kind of resilience.** **The alternative, Intelligence → Reflex on a *thinking fast* argument, would make the only Intelligence class defensively identical to the Dexterity classes and lose the distinction entirely.**

**⚠ One line, and it should go in before the Explorer rather than after.**

---

# 2 — The frame these four are built on

**Everything is authored — no source column exists for any of them — so the discipline is that every number comes from a published band or rule rather than from feel.**

    rate from feat total    Combat 18-23 · Middle 15-16 · Specialist 10-12   (PT-126 opened Specialist)
    skill base band         Combat 1-4  · Middle 2-5   · Specialist 3-7      (PT-78, opened by REPLY-15)
    chain band              Combat 14-20 · Middle 11-17 · Specialist 8-14    (PT-95)
    T = picks + 4 credits   Combat 40 · Middle 31 · Specialist 22            (PT-89)
    capstones               floor((T - N) / 2)
    saves                   PT-123, extended by section 1

**⚠ And every feat total below reuses an existing cadence rather than authoring a new curve.** **`FINDINGS-01 §1` found two authored totals with no schedule behind them; reusing a published column means the thirty rows already exist and cannot drift.**

| Class | Feats | Cadence borrowed from |
|---|---|---|
| **Brawler** | 18 | the Marksman's rebuilt curve — 1 / 3 / 6 / 9 / 12 / 15 / 18 at 1, 5, 10, 15, 20, 25, 30 |
| **Explorer** | 16 | Scout · Guardian — 1, 2, 3, then every odd |
| **Duelist** | 15 | Sentinel · Watchman |
| **Doctor** | 11 | Smuggler · Machinist — 1, 2, then every third |

---

# 3 — Brawler

**`CLASS-ROSTER-01 §5`:** *"`Brawler` and `Duelist` give melee an owner. `ATTACKS-07`'s unarmed roster had no class built around it."*

## 3.1 ⚠ The class has a hard mechanical reason to exist and nobody has stated it

**Derived. `UNARMED_SPECIALIST_I`–`VIII` and `COMPLEX_UNARMED_ANIMS` are granted to `jcn`, `jgd`, `jsn`, `sas`, `sld`, `sma`, `jwa`, `jma`, `jwm`.**

> **All nine Force columns. No mundane class in either game.**

**`ATTACKS-07 §1`:** *"Damage is set by `Unarmed Specialist` — 1d4 at level 2 rising to 8d4 at 30. **Without that feat, 1d3.**"*

**So today a Soldier who loses his sword punches for `1d3` at level 30, and a Jedi Consular punches for `8d4`.** **A mundane unarmed fighter does not merely lack a specialty — the scaling that makes unarmed viable is closed to them entirely.**

**⚠ The Brawler's first grant is `Unarmed Specialist`, and that alone justifies the class.**

## 3.2 The record

| | | |
|---|---|---|
| **Rate** | **Combat** | 18 feats |
| **Hit die** | **d10** | |
| **Primary** | **Strength** | |
| **Saves** | **12 / 6 / 6** — Fort Strong · Reflex Weak · Will Weak | `PT-123`, one job |
| **Skill base** | **2** | Combat band 1–4 |
| **Class skills** | **6** — Athletics · Acrobatics · Alertness · Awareness · Intimidate · Streetwise | |
| **Chains** | **14** → **13 capstones** | Combat floor. The narrowest useful roster, most completely finished |
| **Grants** | **`Unarmed Specialist` I–VIII** at 2, 6, 10, 14, 18, 22, 26, 30 · `Complex Unarmed Anims` at 1 | §3.1 |

## 3.3 Feature — `Nothing In My Hands`

| Tier | | Effect |
|---|---|---|
| **`Nothing In My Hands`** | 1 | **Your unarmed attacks ignore 2 points of the target's armour bonus to Defence.** |
| › **`Through The Plate`** | 4 | **4 points.** |
| ›› **`Armour Is A Comfort`** | 8 | **The target's armour bonus does not apply against your unarmed attacks at all.** |

**Priced: Korr carries 7 of his 19 Defence in medium battle armour, so the capstone is worth about `+7` to hit against him.** **That is large and it is bought with the game's worst weapon — `8d4` at level 30 with no `Weapon Specialization`, no critical range, and no reach.**

**Not dominant:** **worth nothing against an unarmoured target, nothing against a Jedi in robes (Defence 2, and `ACTION-ECONOMY-01 §18.2` gives Jedi no armour at all), and nothing at range.** **It is a hard counter to exactly one thing — the heavily armoured soldier — which is the fight a brawler is supposed to win.**

---

# 4 — Duelist

## 4.1 The record

| | | |
|---|---|---|
| **Rate** | **Middle** | 15 feats |
| **Hit die** | **d8** | |
| **Primary** | **Dexterity** | |
| **Saves** | **6 / 12 / 12** — Fort Weak · Reflex Strong · Will Strong | `PT-123`. Reflex from Dexterity; Will as the second, because a duel is nerve |
| **Skill base** | **4** | Middle band 2–5 |
| **Class skills** | **7** — Acrobatics · Alertness · Awareness · Athletics · Persuade · Intimidate · Streetwise | |
| **Chains** | **12** → **9 capstones** | One above the Middle floor |

## 4.2 Feature — `Single Combat`

| Tier | | Effect |
|---|---|---|
| **`Single Combat`** | 1 | **While exactly one enemy is within your reach, +2 attack and +2 Defence against that enemy.** |
| › **`Nobody Interrupts`** | 4 | **+4 and +4.** |
| ›› **`Just Us Then`** | 8 | **+4 and +4**, and **that enemy gains no benefit from flanking against you.** |

**It is not `Dueling` and does not overlap it.** **`Dueling` is a condition on *your* hands — one weapon. This is a condition on *the field* — one opponent. A Duelist holding both has met two separate conditions and the corpus already stacks conditions that differ.**

**Not dominant:** **it switches off the moment a second enemy closes, which is most encounters in the pregen suite.** **It is a boss-fight and a first-contact feature, and it rewards a player who deliberately isolates — which is a decision at the table rather than a number on a sheet.**

---

# 5 — Doctor

**`CLASS-ROSTER-01 §5`:** *"`Doctor` gives `Medicine` an owner. It sat on five classes and was central to none."*

## 5.1 The record

| | | |
|---|---|---|
| **Rate** | **Specialist** | 11 feats |
| **Hit die** | **d6** | |
| **Primary** | **Wisdom** | |
| **Saves** | **12 / 6 / 12** — Fort Strong · Reflex Weak · Will Strong | `PT-123`. Will from Wisdom; Fortitude as the second — exposure and steadiness |
| **Skill base** | **6** | Specialist band 3–7 |
| **Class skills** | **9** — Medicine · Science · Botany · Xenology · Alertness · Awareness · Persuade · Appraise · Slicing | |
| **Chains** | **12** → **5 capstones** | Wide and shallow. It has an answer occasionally and masters little |

## 5.2 Feature — `Field Surgery`

**Derived from a gap in the damage tracks.** **`ATTACKS-01 §12.4`: vitality is the fast track, wounds are the slow one — 0 is Disabled, −1 to −9 is dying, −10 is dead.** **`PLAYTEST-RULINGS-01 B4`: wound points equal the Constitution score and recover at **1 per day**.**

> **⚠ Every healing effect in the game restores vitality. Nothing restores wounds.** **Medpacs, `Medicine`'s Effect mode, `Jury Rig`, `Regenerate Vitality Points` — all of them are the fast track.**

| Tier | | Effect |
|---|---|---|
| **`Field Surgery`** | 1 | **Ten minutes and one medpac restores 1 wound point to an adjacent character.** Once per character per day. |
| › **`Triage`** | 4 | **As a Gear action in combat**, and you **automatically stabilise a dying character** with no check. |
| ›› **`Not Today`** | 8 | **2 wound points**, and **once per encounter a character within your reach who would be reduced to 0 wounds is instead left at 1.** |

**Priced: a wound point is worth a day of natural recovery, so tier 1 is small and permanent rather than large and temporary.** **The capstone is the strong tier and it is once per encounter, requires reach, and does not prevent the damage — it moves the threshold by one.**

**Not dominant:** **it does nothing to vitality, which is where almost all damage lands.** **A Doctor cannot out-heal a fight; it can stop a character being removed from the campaign.**

---

# 6 — Explorer

**`CLASS-ROSTER-01 §5`:** *"`Explorer` closes the largest structural hole in the skill table — `Archaeology`, `Xenology` and `Science` were a Jedi monopoly. A non-Force character could not be the party's scholar, in a game whose plot is finding Rakatan Star Maps."*

**⚠ Blocked on `§1` for its save line. Everything else below is written.**

## 6.1 The record

| | | |
|---|---|---|
| **Rate** | **Middle** | 16 feats |
| **Hit die** | **d8** | |
| **Primary** | **Intelligence** | **⚠ the first in the game — see `§1`** |
| **Saves** | **12 / 6 / 12** — Fort Strong · Reflex Weak · Will Strong | **⚠ pending `§1`.** Will from Intelligence under the proposed extension; Fortitude second, for the field half |
| **Skill base** | **5** | Middle band 2–5, at the top |
| **Class skills** | **9** — Archaeology · Xenology · Appraise · Science · Botany · Alertness · Awareness · Pilot · Mysticism | *the first four are owner-set* |
| **Chains** | **15** → **8 capstones** | Broad and shallow, matching the Scout's shape one rate down |

## 6.2 Feature — `Prior Study`

**Derived from a mechanic nothing currently answers.** **`SKILL-RESOLUTION-01 §2.2` reserves a scaling band — *character level + N* — for *"the two or three obstacles an adventure is about,"* and notes KOTOR's hardest run to level + 28.**

> **⚠ Fixed DCs describe the world and a character outgrows them. The scaling band never gets easier, by design. No class has a tool for it.**

| Tier | | Effect |
|---|---|---|
| **`Prior Study`** | 1 | **Once per adventure, declare you have studied this place, species or artifact.** You and each ally gain **+2** on all checks concerning it for the rest of the adventure. |
| › **`I've Read About This`** | 4 | **+4.** |
| ›› **`Someone Wrote It Down`** | 8 | **+4**, and **one scaling-band obstacle per adventure is treated as a fixed Heroic DC of 30** instead of scaling with level. |

**The capstone is the class.** **It converts the one category of obstacle that grows with the party into a fixed number, once, and the party has to decide which obstacle is worth it.**

**Not dominant:** **it is declared in advance, so a wrong guess wastes it, and it does nothing in combat.** **⚠ And it makes the Explorer the only class whose feature is spent at the adventure scale rather than the encounter scale, which is a new axis and should be checked in play.**

---

# 7 — The Agent, and why I have not drafted it

**⚠ `CLASS-ROSTER-01 §5` gives a stated purpose for the Explorer, the Doctor, the Brawler and the Duelist. The Agent has none — its row reads *"NEW — nothing written"* and no section explains what it is for.**

**I can infer one from the roster's own structure and I would rather have it confirmed than assume it:**

**`CLASS-ROSTER-01 §6` records two owner distinctions:** *"`Operative` is ranged covert. `Shadow Hunter` is melee covert."* **Both are prestige classes.**

> **⚠ Two covert prestige classes exist and no covert base class does.** **The Smuggler holds `Stealth` and the Sentinel holds `Stealth`, `Security` and `Slicing`, but neither is built for it — the Smuggler is a pilot and a talker, the Sentinel is a Jedi.**

**So the Agent is almost certainly the covert base class the two prestige classes feed from, and `§7`'s open question in `CLASS-ROSTER-01` — whether `Operative` and `Shadow Hunter` are distinct enough to both exist — is the same question read from the other end.**

**If that is right, the Agent is `Middle` or `Specialist`, Dexterity-primary, and its skill list is `Stealth`, `Security`, `Slicing`, `Streetwise`, `Persuade`, `Alertness`, `Awareness`, and it splits from the Smuggler on **infiltration versus commerce**.**

**I have not written it because a class with an inferred purpose is a class built on my guess, and `FINDINGS-20` is what happens when a premise is not checked first.**

---

# The question

> **⚠ Two, and the first blocks the Explorer's save line: does `PT-123` extend to `Intelligence → Will`?**

**And second: is the Agent the covert base class that `Operative` and `Shadow Hunter` prestige from? One line either way and I will draft it.**

**The Brawler, Duelist and Doctor are complete and nothing waits on them.**
