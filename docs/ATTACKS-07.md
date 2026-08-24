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


## 3. The five unarmed chains — `PT-228`

**⚠ This roster held one chain. `Jab`, `Punch` and `Kick` are the same attack under three names, and `Echani Strike` is restricted and gates at 5.**

> **So the `Brawler` could not take a single unarmed chain as a starting attack.**

**Five axes, mirrored from the melee and ranged rosters where a fist can plausibly carry them.**

**⚠ Four axes are deliberately absent.** **`Spread` — one fist, one target. `Stealth` — `Sneak Attack` is already universal and does not care what you hit with. `Support` and `Reaction` are marginal and `Parry` and `Guarding Stance` already cover them for anyone with hands.**

### Velocity — more strikes

| Tier | Level | Effect |
|---|---|---|
| **Combination** | **1** | **Strike twice unarmed.** The second gains `+2` if the first hit. **Attack −3, Defence −2** |
| › **Chain Punch** | **4** | **Three strikes**, each `+2` if the previous hit. **Attack −2, Defence −1** |
| ›› **Rain of Blows** | **8** | **Three strikes**, each `+2` if the previous hit, and **if all three hit the target is `Slowed`** until the end of its next turn |

**⚠ Adopted at `PT-188` and never written here until now.** **Deliberately not `Flurry` renamed — `Flurry` buys back accuracy across its tiers and keeps volume flat; this escalates *within the round*.**

### Power — everything behind one blow

| Tier | Level | Effect |
|---|---|---|
| **Body Blow** | **1** | **+4 damage. Attack −2.** On a hit the target cannot take a reaction until the end of its next turn |
| › **Hammer Blow** | **4** | **+7 damage. Attack −2**, and **knockback 2 squares** unless the target saves — Fortitude, DC 10 + your level + Strength modifier |
| ›› **Haymaker** | **8** | **+10 damage. Attack −2**, knockback 4 squares, and **the target is knocked prone** on a failed save |

**⚠ The melee mirror is `Power Attack`, which requires Strength 12.** **This does not** — **it is the one Power chain a character with no Strength investment can enter, which is `AGENDA-CURRENT §2.4c`'s whole point.**

### Precision — where it hurts

| Tier | Level | Effect |
|---|---|---|
| **Uppercut** | **1** | **Threat range ×2.** On a critical the target takes **−2 attack** until the end of its next turn |
| › **Nerve Strike** | **4** | **Threat ×3**, and the penalty becomes **−4** and also applies to the target's **Reflex saves** |
| ›› **Blackout** | **8** | **Threat ×4**, and on a critical the target is **`Stunned` for one round** unless it saves — Fortitude, DC 10 + your level + Dexterity modifier |

**⚠ Mirrors `Critical Strike` and `Precise Shot` at the same multipliers — `ATTACKS-01 §292`.** **The rider is a debuff rather than damage, because an unarmed critical is already `8d4` at 30.**

**⚠ The tiers escalate one idea:** **a blow that rattles → a blow that finds a nerve → a blow that ends it.** **`PT-182`'s test — a chain is one line if its tiers scale one idea.**

**And `PT-176` applies: `Uppercut`'s multiplier does not compound with `Deathstroke` or the `Commando` capstone. Where more than one threat multiplier applies, use the largest.**

### Position — inside their reach

| Tier | Level | Effect |
|---|---|---|
| **Inside Reach** | **1** | **Move up to your speed and strike as one declaration.** The movement provokes nothing from the target you strike |
| › **Boxed In** | **4** | As above, and **the target cannot move away from you** until the end of its next turn unless it `Disengage`s |
| ›› **Smother** | **8** | As above, and **the target's `Disengage` against you costs its whole movement** |

**⚠ Mirrors `Quick Attack` and `Point Blank Shot`.**

**⚠ `Smother` reaches `Immovable Object`'s tier 2 by a different route.** **Recorded rather than avoided: one is a Juggernaut class feature, this is a chain anyone may buy, and a Juggernaut holding both gets no benefit from the second.**

### Control — take them off their feet

| Tier | Level | Effect |
|---|---|---|
| **Clinch** | **1** | **Opposed attack roll.** On a success the target is **`Slowed`** and cannot make ranged attacks until the end of its next turn |
| › **Off Balance** | **4** | On a success the target is **knocked prone** instead |
| ›› **Throw Down** | **8** | On a success the target is **knocked prone and moved 2 squares**, and **provokes an opportunity attack from one ally** |

**⚠ Mirrors `Sweep Attack` and `Staggering Shot`.** **`Sweep Attack` requires Strength 12; this does not, for the same reason as Power.**

---


## 4. What the unarmed roster needs that the others do not — `PT-228`

### 4.1 The gating ladder

**All fifteen chains gate at `1 / 4 / 8`.**

**⚠ That is the house pattern — `PT-196` derived it: the melee roster uses level 1 four times, 4 seven times, 8 eight times.** **Nothing here departs from it, unlike the stealth chains at `1 / 5 / 10`.**

### 4.2 ⚠ No chain here has an ability prerequisite, and that is the point

    Power Attack · Cleave · Sweep Attack      require Strength 12
    Body Blow · Clinch                        require nothing

**`AGENDA-CURRENT §2.4c`: six of nine melee tier-1 entries are gated at level 1, three behind Strength.**

> **⚠ `Body Blow` and `Clinch` are the first Power and Control entries a character with no Strength investment can take at level 1.**

**That is why the roster exists at the size it does.**

### 4.3 Damage is `Unarmed Specialist`, not the chain

**⚠ Every chain here modifies an unarmed strike; none sets its damage.** **`§2` governs: `1d4` at level 2 rising to `8d4` at 30, or `1d3` without the feat.**

**So `Body Blow`'s `+4` is `+4` on top of that ladder, not a replacement for it.**

**⚠ And `PT-184` defers the comparison that matters:** **`8d4` averages 20 against a lightsaber's `2d8` at 9.** **The owner ruled that meaningless until weapon upgrades exist, and these chains do not change it — they add riders, not dice.**

### 4.4 Who may take them

**⚠ Universal.** **Every class, every species, droids included.**

**`PT-210`: share what is *training*, withhold what is *instinct* or *anatomy*.** **A fist is training.**

**⚠ One exception, and it is a chassis fact rather than a rule:** **a chassis with no hands cannot take `Clinch` or `Combination`.** **`ATTACKS-01`'s chassis blocks already handle this; nothing new is needed.**

### 4.5 ⚠ Interaction with `Nothing In My Hands`

**`PT-188` made the Brawler capstone fire on *the first unarmed attack each round*, specifically so it would not triple when an unarmed Velocity chain existed.**

> **That chain now exists. The pricing holds without change.**

**⚠ Checked: `Combination` at tier 3 is three strikes, and the capstone applies to one of them.** **Worth `+5`, not `+15` — exactly as `PT-188` computed.**

### 4.6 What is deliberately absent

    Spread      one fist, one target
    Stealth     Sneak Attack is universal and does not care what you hit with
    Support     Guarding Stance covers it for anyone with hands
    Reaction    Parry covers it

**⚠ Four of nine axes. The unarmed roster is smaller than melee or ranged by design, and 15 chains against their 11 tier-1 entries each is close enough for parity.**

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
