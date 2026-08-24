# FINDINGS-24 — the Agent, measured against the Smuggler before proposing it

**⚠ `REPLY-21` asks for Explorer, Doctor, Brawler and Duelist. All four are in `FINDINGS-23`, pushed before it was written. Not repeating them.**

**`REPLY-21` also says nothing blocks me. Two things do, both in `FINDINGS-23`: `PT-123` does not map Intelligence, which is the Explorer's save line, and the Agent had no stated purpose. `§1` below closes the second.**

---

# 1 — The inference was half wrong, and measuring it is what showed that

**`FINDINGS-23 §7` proposed the Agent as *the covert base class the two covert prestige classes feed from*.**

**Derived before building on it — who actually holds the covert skills:**

    Stealth           Bounty Hunter · Jedi Sentinel · Smuggler
    Security          Jedi Sentinel · Smuggler · Engineer
    Slicing           Jedi Sentinel · Scout · Smuggler · Engineer
    Streetwise        Bounty Hunter · Jedi Sentinel · Smuggler

> **⚠ The Smuggler holds all four. So does the Jedi Sentinel. No other class holds more than two.**

**So *covert base class* is already occupied, twice.** **An Agent built as *the stealthy one* is the `Smuggler`/`Scoundrel` problem a third time, and I would have written it.**

## 1.1 What separates them is not the skill list, it is who you work for

**The Smuggler's eleven are the fringe package — `Appraise`, `Pilot`, `Sleight of Hand` and `Demolitions` alongside the covert four.** **Commerce, a ship, and light fingers.**

**The Agent's case is the institutional one: Republic or Sith intelligence rather than the underworld.** **Same rooms entered, different reason and different method — the Smuggler is not supposed to be there and the Agent is supposed to be someone else.**

**Which gives the real split, and it is on the primary ability rather than the skills:**

| | Smuggler | **Agent** |
|---|---|---|
| **Primary** | **Dexterity** | **Charisma** |
| **Method** | not seen | **seen, and taken for someone else** |
| **Strong saves** | Reflex | **Reflex and Will** |

**⚠ `SKILLS-01` puts disguise inside `Streetwise` — *"Gather Information + Disguise + the sourcing half of Forgery"* — and `SKILL-RESOLUTION-01 §3` resolves it: *"Streetwise's disguise use rolls against Alertness."*** **The mechanic exists, it is Charisma-keyed, and no class is built on it.**

## 1.2 The overlap, measured

**Proposed Agent list, 9:** `Stealth` · `Security` · `Slicing` · `Streetwise` · `Persuade` · `Intimidate` · `Xenology` · `Alertness` · `Awareness`

    shared with Smuggler   7    Stealth Security Slicing Streetwise Persuade Alertness Awareness
    Agent only             2    Intimidate · Xenology
    Smuggler only          4    Appraise · Pilot · Sleight of Hand · Demolitions

    shared / smaller list  7/9  = 78%
    Jaccard                7/13 = 54%

**`PT-83` measured the pairs that mattered: Machinist/Engineer 89% and split, Scout/Soldier 86% and kept, Consular/Guardian 83%, Engineer/Smuggler 80%.**

> **78% sits below every pair `PT-83` recorded, including the one it kept.**

**⚠ The metric is not stated in `PT-83` and I cannot reproduce which of the two figures above it used.** **Both of mine are below 86% either way, so the conclusion holds under both — but the number should not be compared to `PT-83`'s as though they were computed the same way.**

**And `PT-83`'s own caveat applies:** *"High overlap alone does not condemn a pair. Scout and Soldier sit at 86% and nobody would merge them — they have different jobs that happen to share skills."*

---

# 2 — Agent

| | | |
|---|---|---|
| **Rate** | **Middle** | 15 feats, Sentinel · Watchman cadence |
| **Hit die** | **d8** | |
| **Primary** | **Charisma** | **§1.1.** *The first Charisma-primary class in the game* |
| **Saves** | **6 / 12 / 12** — Fort Weak · Reflex Strong · Will Strong | `PT-123`. Will from Charisma; Reflex as the second job |
| **Skill base** | **5** | Middle band 2–5, at the top |
| **Class skills** | **9** | §1.2 |
| **Feats at 30** | **15** | |
| **Picks at 30** | **27**, `T` = 31 | |
| **Chains** | **11** → **10 capstones** | **The Middle floor.** It fights seldom and finishes what it starts |

**⚠ The chain count is the deliberate opposite of the Scout's 17.** **Same rate, same budget, six trees apart — which is the pair test `FINDINGS-06 §3` set up and the Bounty Hunter currently holds the other end of.** **Three classes now sit at the Middle floor with 10 capstones: Bounty Hunter, Engineer and Agent. Worth knowing before a fourth is added.**

## 2.1 Feature — `Cover Identity`

**`SKILL-RESOLUTION-01`'s `npccanuse` section already rules the whole permission structure and nothing uses it:** *"a mundane skill may not override the decision of a character under player control… Between NPCs, every skill works in every direction."* **And:** *"a Sith officer intimidates a subordinate into talking… all of it runs."*

> **⚠ Talking an enemy out of a fight is explicitly legal, explicitly bounded away from player characters, and no class can do it.**

| Tier | | Effect |
|---|---|---|
| **`Cover Identity`** | 1 | **Declare it in place of an attack.** Opposed `Persuade` or `Intimidate` against one NPC's `Alertness` or Will save. **On a success it takes no hostile action against your party until the end of its next turn.** You make no attack this round. |
| › **`Deep Cover`** | 4 | On a success it **leaves the encounter** if already below half vitality. |
| ›› **`Handler`** | 8 | On a success it **acts on your initiative under your control for one round.** One NPC at a time. |

**⚠ The capstone is the same effect as `Field Override`'s and that is deliberate rather than an oversight.** **The Engineer turns machines with `Slicing`; the Agent turns people with `Persuade`. Neither works on the other's target and both cost a declaration.** **`SKILL-RESOLUTION-01 §4.1`'s own principle covers it — *two things that fail differently is worth more than one that is simply better*.**

**Not dominant:** **it does nothing to droids, nothing to a player-controlled character by the rule above, and nothing to anything without a mind.** **Against the pregen suite it works on the Sith Trooper and the Dark Jedi and fails on T4-K9 and HK-24.**

**⚠ One thing I have not resolved and it is the same one `Field Override` raised.** **A controlled NPC acting on your initiative gets a declaration; nothing states whether that is its own or its controller's.** **`REPLY-08` escalated it as a Force-economy question and it now has a third instance.**

---

# 3 — Still open from `FINDINGS-23`

**`PT-123` does not map Intelligence.** **Proposed extension: `Wisdom, Charisma or Intelligence → Will`. It blocks the Explorer's save line and nothing else.**

**⚠ And it has just acquired a second dependant: the Agent is the first Charisma-primary class, which `PT-123` does map — but the fact that two of the five new classes are the first of their primary ability suggests the rule was written against the ten and should be checked against the whole ability set rather than extended one class at a time.**

**`Armour Proficiency: Light` on the three Sith remains with the owner.**

---

# The question

> **⚠ `PT-123` → Intelligence. One line, and it is the only thing between here and five of five.**

**The Agent is drafted above. If the institutional-versus-fringe split is not what you wanted from the class, say so before I do anything downstream of it — the overlap number in `§1.2` is the argument and it depends on the list.**
