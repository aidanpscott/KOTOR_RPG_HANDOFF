# ATTACKS-07 — The Unarmed Roster

> **Generated context: `data/attacks.json`. Companion to `ATTACKS-04` (ranged), `ATTACKS-05` (melee), and `ATTACKS-06` (lightsaber).**

**4 chains, 6 entries.** *Derived from `data/attacks.json` by matching the names this document renders. `ATTACKS-07` is hand-written, so no `stats()` call covers it and the figure is stated here rather than generated.*


**Two things live here. A basic attack anyone can make, and one chain almost nobody can.**

---

## 1. The basic attack, under three names

**`Jab`, `Punch`, and `Kick` are the same attack.** **One unarmed strike, no penalty, no rider.**

| Attack | Description | Effects |
|---|---|---|
| **Jab** | A short strike thrown from where your hands already are. | **One unarmed attack.** **Damage is set by `Unarmed Specialist` — 1d4 at level 2, rising to 8d4 at level 30 — plus your Strength modifier.** **Without that feat, 1d3.** |
| **Punch** | The whole shoulder behind it. | **One unarmed attack.** **Identical to `Jab` in every respect.** *The name is yours to choose; the mechanics do not care.* |
| **Kick** | Longer reach, worse balance, and it lands like a hammer. | **One unarmed attack.** **Identical to `Jab` in every respect.** |

**They exist separately so a narrator has words.** > **A Soldier who has lost his sword throws a punch; a Smuggler jabs; a Wookiee kicks.** **Nothing in the engine distinguishes them and nothing should.**

### Damage

**`Unarmed Specialist` sets it, and the feat already existed** — **1d4 at level 2, then 2d4, 3d4 and upward to 8d4 at level 30, granted at levels 2, 6, 10, 14, 18, 22, 26 and 30.**

**Without the feat, unarmed damage is 1d3 plus your Strength modifier.**

**`Increase Melee Damage` and `Dueling` both name unarmed explicitly and apply here.**

---

## 2. `Echani Strike` — the one restricted chain

| Attack | Description | Effects |
|---|---|---|
| **Echani Strike** | Combat as conversation. **The Echani read a fight the way other people read a face.** | **Level 5. Requires Echani Combat Training. Unarmed.** **Strike twice this round instead of once. Attack −2.** **Both strikes on one target knock it prone** unless it saves — Reflex, DC 10 + your level + Dexterity modifier. **Damage uses your Dexterity modifier rather than Strength.** |
| › Echani Flow |  | **Level 9.** **Three strikes. Attack −1.** **Prone on any two hits.** |
| ›› Way of the Six Sisters |  | **Level 14.** **Four strikes. No attack penalty.** **Prone as above.** **And a target you have struck this round takes −2 on attack rolls against you until the start of your next turn** — you have read them. |

### The gate is training, not blood

**`SPECIES-CHAPTER-v2` is explicit and it matters:**

> ***"Echani gain access to the Echani Strike feat chain, with the first step available at character level 5. Other species may learn the chain from an Echani teacher — the tradition is trained, not heritable, and every source says so explicitly."***

**An Echani character has `Echani Combat Training` from creation.** **Anyone else may earn it from a teacher, and such teachers are vanishingly rare — the tradition barely leaves Eshan.**

> **This is the only thing in the corpus a GM grants on a narrative event rather than a level.** **Finding an Echani willing to teach you is a story, not a purchase.**

### What each tier does

| | Strikes | Attack | Rider |
|---|---|---|---|
| **`Echani Strike`** *(5)* | **2** | −2 | **Both strikes on one target knock it prone** — Reflex, DC 10 + level + Dexterity |
| **`Echani Flow`** *(9)* | **3** | −1 | **Prone on any two hits** |
| **`Way of the Six Sisters`** *(14)* | **4** | **0** | **Prone as above, and anyone you struck this round takes −2 attacking you until your next turn** |

**Damage uses Dexterity, not Strength.** **Which is the whole character of it** — **`SPECIES-CHAPTER-v2` gives the Echani +2 Dexterity and −2 Constitution, so the chain runs on the ability they have and spares the one they lack.**

### Why it is weaker than a weapon, and should be

**Three strikes at `3d4 + 4` is about 22 a round at level 8.** **A vibrosword Barrage is 39.**

> **It needs no weapon. It cannot be disarmed. It survives `Disarming Strike` and `Sunder`. And it knocks people down.**

**A Jedi stripped of a lightsaber is not unarmed.**

**⚠ It is also the only chain outside Velocity that scales its attack count**, which is deliberate: **it has no weapon die and no Strength behind it, so the count is where its scaling has to live.**
