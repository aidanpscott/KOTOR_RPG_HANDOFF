# MULTICLASS-01 — multiclassing, and the banking problem

**Two things. The rules, which are 3.5's, and the exploit, which is ours to fix.**

---

## 1. The diagnosis

> **The exploit is not multiclassing. It is *banking* — and the thing being banked is Force powers.**

**KOTOR let you hold levels.** **You stopped at the XP threshold, went to Dantooine, became a Jedi, and then spent eleven banked levels at once.** **Every player who replayed the game learned this and every one of them was right to.**

**Priced against our own numbers, at character level 12 with the Jedi unlock at 8:**

| Route | Force pool | Vitality | BAB |
|---|---|---|---|
| **Scout 8, then Guardian 4** | **34** | 58 | +10 |
| **Scout 1, bank, Guardian 11** | **94** | 65 | +11 |

> **Nearly three times the Force pool.** **Vitality differs by 7 and BAB by 1 — those are noise.**

**Two things are wrong and the second is bigger.**

**The pool.** **`FORCE-POOL-01-v3` computes it as `(Force die + Wisdom + Charisma) per Jedi level`.** **Every banked level is a whole Force die plus both modifiers.**

**Powers known.** > **`cls_spgn_jedi.2da` gives 2 Force powers at Jedi level 1 and +1 per Jedi level after.** **Every banked level is a whole power.**

**⚠ The source community names the second one directly:** ***"When you become a Jedi on Dantooine the lower level you are the better, because you'll get access to more Force Powers."*** **Not the pool. The powers.**

---

## 2. The fix — one part, and a third that was cut

**Splitting the Force pool. That is the whole fix.**

> **⚠ Two other parts existed and both were cut.** **An entry-credit system — `§5` — and a rule forbidding banking outright.**

**The goal is to make committing to your current class attractive, not to make waiting illegal.**

### 2.1 The Force die is per Jedi level. The ability modifiers are per character level.

> **`Force points = (Force die × Jedi levels) + ((Wisdom + Charisma) × character level)`.**

**Your *capacity* is who you are. Your *training* is what you learned.**

**A Scout who spent eight levels surviving has the same reserve of will as anyone else at level 12. What they lack is eight levels of instruction in using it.**

| Route | Pool now | Pool under the fix |
|---|---|---|
| **Scout 8, then Guardian 4** | 34 | **82** |
| **Scout 1, bank, Guardian 11** | 94 | **100** |
| **Pure Guardian 12** | 102 | **102** |

**The banking advantage drops from 60 points to 18 — a 71% reduction** — **and the honest route lands within 20% of a pure Guardian instead of a third of one.**

**⚠ This is a real change to `FORCE-POOL-01-v3 §2` and needs applying there.**

### 2.2 There is no entry credit

**⚠ Removed. See `§5` for what was tried and why none of it was needed.**

**A character entering a new class gains what one level of that class gives, and nothing else.**

> **The rate they gain at from that point forward is the whole mechanism.**

### 2.2a Powers known is the real gap, and the pool split is what closes it

**`cls_spgn_jedi.2da` gives 2 Force powers at Jedi level 1 and +1 per Jedi level after.**

> **A Scout 8 entering Guardian arrives with 2 powers where a pure Guardian 9 has 10.** **That is the largest single gap multiclassing creates anywhere in the system.**

**⚠ And it is why banking was worth doing in the source.** ***"The lower level you are the better, because you'll get access to more Force Powers."***

**`§2.1`'s pool split is what answers it.** **Under the old formula every banked level was a whole Force die plus both ability modifiers; under the split it is a die only, and the modifiers arrive with character level whatever you spent it on.**

**⚠ Powers known still favours early entry, and that is left standing.** **A Jedi who trains young knows more powers than one who trains late. The mechanic and the fiction agree, and nothing needs correcting.**

### 2.2b Banking is discouraged, not forbidden

**No minimum level to enter a Force class.** **A player who wants to bank may.**

**At character level 12, Scout into Guardian:**

| Split | Powers | Pool | BAB | Vitality | Levels spent at 1 |
|---|---|---|---|---|---|
| **Scout 8 / Guardian 4** | 8 | 82 | +10 | 58 | 7 |
| **Scout 5 / Guardian 7** | 10 | 90 | +11 | 61 | 4 |
| **Scout 1 / Guardian 11** | 13 | 100 | +12 | 65 | 0 |

> **Banking to level 1 buys four powers over the level-8 route.** **It costs seven levels of being a level-1 character in a campaign that is not a video game.**

**That is the trade, and it is now a trade rather than a landslide.** **KOTOR's own community landed on 5/15 and 8/12 as optimal rather than 2/18, because *"extra attack bonus and 3 more feats far outweigh a couple Force powers."*** **Under these numbers that judgement holds at a table too.**

---

## 3. The rules themselves — 3.5, as in the source

**KOTOR's multiclass system is D&D 3.5's, and we keep it.**

**Take a level in any class you qualify for, at any level-up.**
**Base attack bonus and saving throws sum across all classes.**
**Hit die and skill points come from the class taken that level.**
**Every class you hold contributes its class skill list. All of them are class skills.**
**Force die accrues only on Force-class levels** — `§2.2`.

**Entry credit applies on first taking any class you do not already hold** — `§2.2`.

**⚠ 3.5's favoured-class XP penalty is cut.** **It is fiddly, it punishes exactly the character concept this game is about, and KOTOR did not implement it either.**

### 3.1 Attack picks

**Picks accrue at the rate of the class you take that level in, read at your current character level** — `CLASS-ATTACKS-01 §3`.

**A Scout 8 taking Guardian at level 9 gains Middle's level-9 entry.** **Both classes are Middle, so nothing changes.**
**A Soldier 8 taking Consular at level 9 gains Specialist's level-9 entry, not Combat's.**

> **This closes `CLASS-ATTACKS-01 §6`'s open question.** **Neither summing nor taking the higher rate — you gain what the class you are actually training in gives you.**

### 3.2 Grants

**Entering a class grants its 1st-level attack grants, once** — `CLASS-ATTACKS-01 §4`.

**⚠ Duplicates are not doubled.** **A Soldier entering Bounty Hunter already has `Shoot` and gains only `Rapid Fire` and `Snap Shot`.**

### 3.3 Force-Sensitive

**A non-Force-using character must hold `Force-Sensitive` before taking a Force-class level.** **The three Force classes receive it free at 1st level; anyone else pays a feat for it.**

**⚠ Warrant: `FORCE-TRAINING-01`. Owner ruling, and it supersedes two dead citations.**

**The gate was cited to `GAP-002` branch A, which the owner ruled dead.** **The Library then proposed `PARTITION-01` (`D-AK`), which is not one** — *grepped: `Force-Sensitive` 0 hits, `multiclass` 0.* **`PARTITION-01` settles the roster, the partition and the drift tiers, and says nothing about who may take a Force class.**

**`FORCE-TRAINING-01` is the warrant because the gate is about *class access*, and access is training.**

> **`FORCE-AWAKENING-01` answers *what am I*. `FORCE-TRAINING-01` answers *who will teach me*.** **The three Jedi base classes open when someone agrees to teach you, and not before.**

**⚠ Which means `Force-Sensitive` is no longer bought as a feat under normal circumstances.** **It is granted secretly at awakening and revealed at confirmation — `FORCE-AWAKENING-01 §21`.**

**This is the gate, and it is deliberately cheap.** **The campaign decides when a character may take it. The mechanics do not.**

---

## 4. What this costs

**Pure single-class characters are slightly worse off relative to multiclass ones than they were.** **That is the point, and it applies to every class rather than only the Jedi.**

**⚠ And a character who takes one Force level purely for the pool now gets more than before** — **(Wis + Cha) × character level applies from that single level.**

> **Mitigation: the Force die is the smaller half at high level, but the ability half only arrives once you have a Force class at all.** **A one-level dip buys a real pool.**

**If that proves too generous in play, the fix is to scale the ability half by Force-class levels up to a cap, rather than character level flat.** **Flagged rather than pre-solved, because it needs a playtest and not an argument.**

---

## 5. Why nobody needs entry credit

**Earlier drafts of this document carried an entry-credit system: a one-time grant scaled to the level you entered at, printed per class.**

**⚠ Removed. Three versions were built and all three were exploitable or unusable.**

### What was tried

**A flat grant** — *"+1 attack pick per 4 prior levels."* **⚠ A one-level dip at 20th produced more than staying pure, and the advantage grew with level.**

**Grants shaped by target class and tier distance.** **Correct, and it took seven steps at the table to answer *what do I get for switching*.**

**Reading the new class's table at *character* level.** **⚠ Worst of the three.** *A Smuggler 12 taking Soldier 1 gained nine attack picks and six feats in one level, matched a pure Soldier exactly, and kept twelve levels of Smuggler on top.*

**A credit pool spent as acceleration.** **Worked, and cost one number of permanent sheet state per class held.**

### Why none of it was needed

> **The rates already do the work.**

**Picks accrue at the rate of the class you take that level in — `§3.1`.** **Split your career and half of it pays at a slower rate.**

| Build at level 30 | Picks | Feats | **Capstones** |
|---|---|---|---|
| **Pure Soldier** | **36** | **23** | **12** |
| Soldier 20 / Smuggler 10 | 30 | 19 | 10 |
| Soldier 15 / Smuggler 15 | 27 | 18 | 9 |
| Three-way even split | 27 | 17 | 9 |

**⚠ These are *capstones*, not chains.** **A chain entered costs one pick; a capstone costs two more on top.** **`PT-88`.** **A character enters more trees than it finishes, and the number below is the finishing count.**

**⚠ Nobody has to write *"multiclassing costs you."*** **It costs you because half your career was paid at a slower rate, and that is arithmetic rather than a penalty.**

### And it is better than 3.5's answer

**3.5 punishes you at the moment you multiclass** — *a 12th-level character taking a new class gets a 1st-level character's worth of it, and an XP penalty on top.*

> **Ours charges you slowly, forever.** **A splitter is continuously behind rather than falling off a cliff.**

**⚠ Which is why the XP penalty was cut and nothing replaced it.** **The rate is the penalty.**

---

## 6. Open

**Prestige class entry requirements.** **Nothing states what a Weaponmaster needs.**

**Whether a character may return to a class they have left.** **3.5 says yes. Nothing here says otherwise, and nothing says so explicitly.**

**Whether a character who returns to a first class collects credit again.** **No — credit is once per class, and the class is already held.** **Stated here because the wording could be read either way.**

---

# PLAYER-FACING TEXT

**⚠ Draft for the Player's Handbook. The sections above are design record; this is what a player reads.**

## Multiclassing

**You are not locked into the class you started with. A Scout who spends a year among smugglers can take a level of Smuggler. A soldier who survives something inexplicable can, with training, become a Jedi.**

**Taking a level in a new class costs nothing extra. There is no penalty, no experience tax, and no permission required beyond what the class itself demands.**

### How it works

**When you gain a level, you choose which of your classes to advance — including one you have never taken before.**

> **You gain exactly what one level of that class gives. Nothing more, nothing less.**

**A 12th-level Smuggler taking her first Soldier level gains a 1st-level Soldier's worth of Soldier: one level of base attack, a d10 for hit points, the Soldier's skill rate for that level, and whatever the Soldier table grants at 1st.**

**She does not catch up. She starts.**

### Then why would anyone do it?

**Because from that point on, every Soldier level you take pays at a Soldier's rate.**

**Attack picks, feats and skill points all accrue faster in some classes than others.** **A Soldier gains attack options quickly; a Smuggler gains skills quickly.** **The moment you start taking Soldier levels, you start gaining like a Soldier.**

> **You are not behind because you started late. You are behind because you spent part of your career gaining at a different rate.**

### What it costs

**Here is a character who committed, against three who did not.**

| At character level 30 | **Attack capstones reached** |
|---|---|
| **Soldier the whole way** | **12** |
| Soldier 20 / Smuggler 10 | 10 |
| Soldier 15 / Smuggler 15 | 9 |
| An even three-way split | 9 |

**The specialist finishes twelve trees. The others finish nine or ten.**

**Those missing chains are the capstones — the top of each attack tree, which you only reach by buying the two below it first.**

### What it buys

| | Specialist | Multiclass |
|---|---|---|
| **Attack capstones** | **More** | Fewer |
| **Class-skill lists** | One | **Two, permanently** |
| **Saving throws** | One progression | **Two, stacked** |
| **What you can do** | **Deeper** | **Wider** |

> **A specialist is better at their thing. A multiclass character has more things.**

**Neither is a trap. Pick the one you want to play.**

### Three things worth knowing

**Every class you hold contributes its class-skill list, permanently.** *A Scout/Smuggler treats both lists as class skills forever.*

**You may return to an earlier class at any time.** *A Scout 5 / Soldier 3 may take Scout 6 whenever they like.*

**Force classes need `Force-Sensitive` first.** *See **Force Sensitivity**, page TK.*
