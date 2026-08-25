# ATTACKS-01 — The Attack System

**A category separate from feats.**

**Status: SETTLED for structure. Roster lives elsewhere.**

| Document | Holds |
|---|---|
| **ATTACKS-01** *(this)* | **The category, the declaration rule, and what moved out of feats** |
| **ATTACKS-02** | The six inherited trees compared across both games |
| **ATTACKS-04** | **The ranged roster** — 11 chains, 31 entries |
| **ATTACKS-05** | **The melee roster** — 11 chains, 31 entries |
| **ATTACKS-06** | **The lightsaber roster** — 14 chains, 42 entries, two per form |

---

## 1. What an attack is

**Attacks are learned combat manoeuvres.** A character acquires them the way they acquire Force powers — **a roster, chains with prerequisites, and NPCs drawing from the same list.**

> **The parallel to Force powers is deliberate.** Both are things a character *knows how to do* rather than things they *are*. **A feat is a permanent property; an attack is an option in a round.**

**Which is why they were the wrong shape as feats.** Thirty rows of `feat.2da` were attack manoeuvres sitting alongside armour proficiencies and Gear Head — **things that alter what you can do, filed with things that alter what you are.**

---

## 2. The declaration rule

> **On your turn you declare one attack. It applies to every swing or shot you make that round.**

**The declaration is the last thing you do — resolving it ends your turn.**

> **One exception: a self-buff Force power does not end your turn.** **You may move after casting one.** **`ACTION-ECONOMY-01 §6.1`.**

**How many swings you get is separate from what modifier is on them:**

| Declaration | Swings or shots |
|---|---|
| **Strike** or **Shoot** | **1** |
| **A Velocity chain** — Flurry, Rapid Fire, Saber Swarm | **3 / 4 / 5** by tier |
| **Dual Strike** | **2**, or one swing with damage rolled twice |
| **Wielding two weapons** | **You strike with both.** Every attack that round takes the dual-wield penalty — see `ACTION-ECONOMY-01 §7`. |

**A level 8 character declaring Flurry strikes three times, and all three take −4 attack and −2 Defence.** **They cannot also declare Power Attack.**

**Every Velocity chain replaces your attack count rather than adding to it.** **Flurry, Rapid Fire, and Saber Swarm all grant three at tier 1, four at tier 2, five at tier 3** — you do not get a base attack plus the chain's bonus. **The chain *is* how many times you go.**

**Dual Strike is the exception and it is a different mechanic** — two swings with one weapon, or one swing with damage rolled twice.

### 2.1 This is the source's own rule

**Every active entry in both games says so:** *"Attack penalty applies to every attack in a combat round."* **You click Flurry once and the round is a Flurry round.**

**`feat.2da` carries it in the `usetype` column** — **0 for melee actives, 1 for ranged actives, blank for passives.** **StrategyWiki splits its page the same way: Active feats need activating; passive ones do not.**

### 2.2 A Force power is an attack for this purpose

**A Guardian who declares Force Lightning has declared their attack that round.** They do not also swing.

> **That is the opportunity cost that makes attacks not needing a resource pool defensible.** A Force user is not paying points to cast; **they are paying the round.**

### 2.3 What it closes

**Three tier-3 chains stacked would have cost attack −2 and Defence −4** — **less on both axes than Rapid Fire or Precise Shot cost alone at tier 1** — while delivering +1 swing, +10 damage, ×4 critical threat, and +1 critical multiplier together.

**Each chain was priced as though its capstone discount were the reward for eight levels. Nothing priced the sum.** **One declaration per round means there is no sum to price.**

---

### 2.3a ⚠ The declaration does not protect against feats — `PT-176`

**`§2.3` closes chain-on-chain stacking:** *"one declaration per round means there is no sum to price."*

> **⚠ That protection is the declaration, and a feat does not compete for one.** **It applies to whatever you declared.**

**The live case, derived:**

    vibrosword, printed width 2

    Deathstroke ×4  alone         13–20    40%
    Commando ×2     alone         17–20    20%
    both, compounded ×8            5–20    80%

**⚠ A Commando with a vibrosword would threaten a critical on four rolls in five.** **Nineteen of twenty rolls hit at all, and sixteen of those threaten.**

**And `§2.3` is exact about why nothing caught it:** *"Each chain was priced as though its capstone discount were the reward for eight levels. Nothing priced the sum."* **The Commando's capstone is not a chain, so the sentence that closes the hole does not reach it.**

**⚠ It only became live when `PT-175` ruled *"widens by one"* to mean `×2`.** **At `+1` the compound was `13–20`; at `×2` it is `5–20`.**

### The rule

> **Threat multipliers do not compound. Where more than one applies, use the largest.**

**⚠ General rather than a Commando patch, because any future feat that multiplies threat hits the same wall.**

**And the cost is real and worth stating.** **A Commando who declares `Deathstroke` gets nothing from three feats they spent.**

**The capstone still fires on `Power Attack`, `Barrage`, `Flurry`, an aimed shot or a plain strike — every round they do not declare a Precision chain.**

> **⚠ The alternative turns `Deathstroke` into a platform rather than the ceiling it was priced as.**

### ⚠ And the same capstone gives different ranges by weapon

**A weapon family spans printed widths.** **The Commando's `×2` gives `19–20` with a long sword and `17–20` with a vibrosword.**

**That is correct rather than broken** — **the multiplier reads the weapon's own column, so a better weapon benefits more, which is what `§303` says the multiplier is for.**

**Recorded because it will look like an inconsistency to the next reader who checks.**

---

### `Assassin Protocols` multiplies with threat — examined and ACCEPTED

**Swept `FEATS-LIBRARY-01` for anything else that stacks with a chain rather than competing with one. Three touch threat, critical or attack count, and one is a genuine multiplication.**

**`Assassin Protocols` fires *on a critical hit*.** **So anything that widens threat raises how often it fires.**

    threat width        execute chance per attack
    plain vibrosword     10%      2.0%
    Commando ×2          20%      4.0%
    Deathstroke ×4       40%      8.0%

**⚠ Owner ruling: accepted, not a defect. `PT-177`.**

**And the first framing of it was wrong.** **This was described as an *execute chance*. It is not one.**

> **Half of *remaining* life is asymptotic. It never reaches zero.**

    after 1 proc   50.00 remaining
    after 4 procs   6.25
    after 8 procs   0.39

**⚠ A target reduced by this eight times is still standing.** **The effect guarantees a survivor by construction.**

**And it is self-limiting in the direction that matters.** **The first proc is large and every one after is worth half the last** — **devastating against a full-health target and rounding error against a hurt one.**

> **⚠ Strongest when the fight has the most left to go, weakest when it could close one out. The opposite of the shape that breaks a game.**

**It needs `Master Assassin Protocols`, `Deathstroke` at tier 3 and a wide-threat weapon simultaneously — a deliberate late-career build rather than something stumbled into.**

**⚠ Contrast the `Commando` case, which was genuinely different.** **`5–20` threat with critical damage multipliers behind it changes every round of every fight.** **This changes some rounds of some fights and ends none.**

**Recorded so the next reader who derives the 8% figure does not re-raise it.**

**`Increase Melee Damage` and `Increase Combat Damage` are flat adders and do not multiply. Checked.**


### 2.3b ⚠ Flat riders multiply by the strikes in a declaration — `PT-180`

**`ACTION-ECONOMY-01 §421` states it, and every class feature was priced against one attack anyway:**

> *"An earlier draft had the tiers grant three, four, and five attacks. That made Power and Precision unplayable: **both apply their bonus to every attack**, and one enhanced swing cannot compete with five ordinary ones."*

**⚠ `Flurry`, `Whirlwind` and `Barrage` are three strikes.** **A `+6` damage rider is `+18` on a Barrage, not `+6`.**

    Sith Warrior Unrelenting, +6 while below half vitality

    as priced        +6 once per round        27.3 → 33.3    +22%
    as it works      +6 on each of 3 strikes  27.3 → 39.9    ⚠ +46%

**Twice what was reported — a per-attack rider divided by a per-round total.**

#### Which features multiply

| Feature | Class | Multiplies? |
|---|---|---|
| **`Unrelenting`** | Sith Warrior | **yes — `+6` damage each** |
| **`Chosen Weapon`** | Commando | yes — `+2` damage, `+3` attack |
| **`Single Combat`** | Duelist | yes — `+4` attack |
| **`Field Position`** | Agent | yes — `+2` attack |
| **`Nothing In My Hands`** | Brawler | **⚠ see below** |
| `Dominion` · One Shot · `Both Barrels` · `Vanish` · `Plunder` · `Field Surgery` · `Read the Ruin` · `Command Protocol` | seven classes | no |

**⚠ Four of the five are `+2` to `+4` — the range `Weapon Focus` and `Weapon Specialization` already occupy and were priced against.** **`Unrelenting` at `+6` is the outlier because it is the largest flat number written.**

#### ⚠ And the Brawler resolves itself

**`ATTACKS-07` has no Velocity chain.** **The unarmed roster is `Jab`, `Punch`, `Kick` — *"one unarmed attack"* each, explicitly identical — and one restricted chain, `Echani Strike`.**

> **A Brawler cannot multi-strike unarmed at all, so `Nothing In My Hands` cannot multiply.**

**⚠ That is luck rather than design and it should be stated.** **If a Velocity chain is ever added to `ATTACKS-07`, ignoring armour on three strikes becomes the largest rider in the game.**

**One Shot's wording — *"your next **single** rifle attack"* — is the same luck. The word is load-bearing and was not chosen to be.**

---

## 3. A tier replaces the tier below it

> **Same attack, better numbers. Nothing new is introduced mid-chain.**

**This is the source's own model.** **Improved Flurry changes the penalty and nothing else. Improved Power Attack changes the damage and nothing else. Improved Critical Strike changes the threat range and nothing else.**

**And it is a legibility rule, which is the project's stated priority.** **A player who knows what Flurry does knows what Master Flurry does.**

### 3.1 The test

> **A tier is a replacement if a player would never want the tier below it.**
> **A tier is a different attack if a player would want to keep both.**

**Twelve of twenty-eight chains failed that test in an earlier draft.** **Overwatch was the capstone of Covering Fire — suppressing an enemy and holding your fire are different actions a player would want both of.** **Sun Djem was the capstone of a chain whose middle tier damaged everyone adjacent — three attacks in one chain.**

### 3.2 Two patterns that satisfy it

**Scaling numbers.** *+5 → +8 → +10 damage. Critical threat ×2 → ×3 → ×4. Attack −4 → −2 → −1.* **Most chains.**

**Adding an option while keeping the old one.** **The disarm chains do this:** *drop the weapon* → *drop or take it* → *drop, take, or destroy it*. **The tier is strictly better because it contains everything below it.**

### 3.3 What it cost

**Nine chains were rewritten and three split into two.** **Riders that had been added at tier 2 or 3 moved into the root**, and the tiers scale their numbers instead.

> **Where a rider was genuinely a different attack, it became its own chain.** **Overwatch is now a Reaction chain of its own. Form I's disarm and sweep are two chains.**

### 3.4 One ladder, and the exceptions are argued

**1 / 4 / 8 is the base ladder** — the source's own, used for every core tree in both games. **Thirty-four of thirty-eight chains use it.**

**Four do not, and each has a reason:**

| Ladder | Chains | Why |
|---|---|---|
| **1 / 5 / 10** | Stealthy Shot · Sneak Attack | **⚠ Re-gated from 2 / 4 / 10 by owner ruling — `PT-196`.** **The capstone sits at 10 because it is a once-per-encounter alpha strike.** |
| **5 / 8 / 14** | Disarming Shot · Disarming Strike | **The capstone destroys a weapon permanently** — the only attacks that remove equipment from the game. |
| **1 / 6 / 12** | Covering Fire · Guarding Stance · Parry · Snap Shot · Guided Strike | **All act outside your own turn, or permit two declarations in one.** *Categorically stronger than anything the source has.* |
| **6 / 10 / 14** | Overwatch | **Both** — it fires before an enemy acts, and it holds a corridor. |

> **An earlier lightsaber draft used 1/5/10 and 1/6/12 with no stated reason, and neither was the base ladder.** **Thirteen of the fourteen chains are now on 1/4/8; Guided Strike keeps 1/6/12 because it is the one entry permitted two declarations in a round.**

---

## 4. The three rosters, and who can take them

| | Chains | Entries | Who |
|---|---|---|---|
| **Ranged** | 11 | 31 | Organics, **Assassin and Battle droids** |
| **Melee** | 11 | 31 | **Organics only** |
| **Lightsaber** | 14 | 42 | **Force classes, and only the form you hold** |

**Eight axes: Velocity, Spread, Precision, Power, Position, Control, Support, Reaction** — plus **Penetration**, reserved for Form II.

> **Melee is chassis-blocked; ranged is role-blocked.** **No droid frame swings a blade** — but **the Assassin droid takes the entire ranged suite** while the Astromech and Remote take none of it. **That distinction is the source's, not ours.**

**A Jedi has every melee chain plus six lightsaber entries** — two chains of three, from whichever form they hold. **Switching forms is the cost of switching attacks.**

---

## 5. The basic attack

**`Strike` for melee, `Shoot` for ranged.** **Every character has both and neither costs anything to learn.**

**No modifier, no penalty.** **It is the attack you declare when you have not declared another.**

---

## 6. Attacks cost nothing

**Confirmed.** **Force powers cost points and permanently degrade the ceiling; attacks cost nothing and always have.** That is the source's design and it survives.

> **What balances a Force user is not cost but *access* — and now also the round.** A Jedi has powers *and* attacks; a Soldier has only attacks. **The Force user pays for a second system, and pays a round every time they use it.**

---

## 7. Classes start with attacks

**Confirmed.** **A class grants a starting set and gains more on a schedule.**

**In KOTOR, class identity came from what you were *given***: Scouts were granted Rapid Shot and Targeting, Smugglers got Sniper Shot and Sneak Attack, Soldiers got Power Attack. **Selectable lists ran 50 to 69 feats for nearly every class and were almost identical.**

**Which attacks each class starts with, at what level each gains more, and how often: `CLASS-ATTACKS-01`.** **Written once the roster closed and the lightsaber tree existed.**

---

## 8. What this removed from feats

**Thirty-one rows left `feat.2da`'s space and stopped being feats.**

**From the universal non-droid set** — Critical Strike, Precise Shot, Sniper Shot, and the melee chains. **From the universal droid set** — Dual Strike and its tiers.

> **What remains in the universal sets is proficiencies, skill feats, and the droid chassis** — **a cleaner definition of what a universal feat is.**

**Three feats came *back* the other way**, having been miscategorised as attacks: **Dueling** *(the single-weapon counterpart to Two-Weapon Fighting)*, **Close Combat**, and **Squad Tactics** *(formerly the Dual Strike feat, now Soldier-only)*.

---

## 9. Two corrections worth keeping

### 9.1 Precise Shot split in two

**KOTOR's Precise Shot did two things at once:** *+1 damage* and *enemy Blaster Bolt Deflection −2*, across five tiers.

> **Those are different kinds of thing.** The damage is what the attack does when you use it. **The deflection penalty is a property of how you shoot** — it applies whether or not you declared that attack.

**The deflection half became the `Marksman` feat.** **The name `Precise Shot` was later reused for the Precision tree's first tier.**

### 9.2 Two capstones were hiding under different names

**`MASTER_FLURRY` and `MASTER_RAPID_SHOT` do not exist in `feat.2da`** — which read as two chains stopping one rung short.

> **They do not exist because the capstones are named differently.** **`WHIRLWIND_ATTACK` requires Flurry and Improved Flurry. `MULTI_SHOT` requires Rapid Shot and Improved Rapid Shot.**

**Ours uses `Barrage` and `Volley of Bolts` for those tiers.** **Both source names were briefly held as isolated entries and are now cut** — the effects they promised were already delivered by the tiers themselves.

**Close Combat genuinely stopped at two tiers.** **It is now a feat, not an attack.**

---

## 10. The reaction pool

> **One pool. Every reaction chain in every roster draws on it.**

**Uses per encounter = the lower of your highest reaction tier and your ability allowance.**

| Allowance | Uses |
|---|---|
| **Dexterity modifier** | +1 → **1** · +3 → **2** · +5 → **3** |
| **Base attack bonus** | +1 → **1** · +6 → **2** · +11 → **3** |

**Take the better of the two. A character with neither has no reactions at all.**

**Three reaction chains exist** — **Snap Shot** and **Overwatch** in ranged, **Parry** in melee.

> **This is the one place where breadth would otherwise convert into extra actions.** **107 of 110 attack entries cost you your declaration**; the three reaction chains do not. **Without a single pool, a combat class buying all three would gain nine free attacks per encounter where a specialist gains three.**

**With it, holding all three buys *options*** — parry a blade, snap-shoot a runner, hold a corridor — **which is what breadth buys everywhere else in the system.**

---

## 11. How attacks are acquired

**Three currencies, three tracks, no crossover.** **Feats, Force powers, and attacks each run their own schedule.** An attack pick cannot buy a feat and a feat cannot buy an attack.

### 11.1 What every character has free

**`Strike` and `Shoot`.** **Not picked, not granted, not spent.** Every character has both from creation.

### 11.2 Picks

> **One pick buys one tier. A full chain costs three.**

**A pick may be spent on any tier whose level gate and prerequisites you meet, in any roster you can use.** **A Jedi's lightsaber picks and melee picks come from the same pool** — the form gate does the limiting on its own.

**Three rates:**

| Rate | Rule | Picks | Full trees |
|---|---|---|---|
| **Combat** | One per level, **two at 1, 6, 11, and 16** | **24** | **8** |
| **Middle** | One per level, **none at 7 and 14** | **18** | **6** |
| **Specialist** | One every other level, **plus 10 and 20** | **12** | **4** |

### 11.3 The schedule

| Level | Combat | Middle | Specialist |
|---|---|---|---|
| **1** | **+2** (2) | **+1** (1) | **+1** (1) |
| **2** | +1 (3) | +1 (2) | — (1) |
| **3** | +1 (4) | +1 (3) | **+1** (2) |
| **4** | +1 (5) | +1 (4) | — (2) |
| **5** | +1 (6) | +1 (5) | **+1** (3) |
| **6** | **+2** (8) | +1 (6) | — (3) |
| **7** | +1 (9) | **—** (6) | **+1** (4) |
| **8** | +1 (10) | +1 (7) | — (4) |
| **9** | +1 (11) | +1 (8) | **+1** (5) |
| **10** | +1 (12) | +1 (9) | **+1** (6) |
| **11** | **+2** (14) | +1 (10) | **+1** (7) |
| **12** | +1 (15) | +1 (11) | — (7) |
| **13** | +1 (16) | +1 (12) | **+1** (8) |
| **14** | +1 (17) | **—** (12) | — (8) |
| **15** | +1 (18) | +1 (13) | **+1** (9) |
| **16** | **+2** (20) | +1 (14) | — (9) |
| **17** | +1 (21) | +1 (15) | **+1** (10) |
| **18** | +1 (22) | +1 (16) | — (10) |
| **19** | +1 (23) | +1 (17) | **+1** (11) |
| **20** | +1 (24) | +1 (18) | **+1** (12) |

**All three land on a whole number of trees at level 20.**

### 11.4 Why breadth is not power

> **You declare one attack per round. 107 of 110 entries cost you your declaration.**

**A Soldier with eight trees and a Consular with four both attack once.** **Breadth buys the right answer more often; it does not buy more actions.** **Depth is where power lives** — tier 3 beats tier 1 — **and every rate can reach tier 3 on the chains it cares about.**

**The specialist gets four capstones. The Soldier gets eight.** **Nobody is locked out of depth; the difference is how many different questions you have an answer to.**

**And the specialist is not short-changed.** **A Consular has Force powers a Soldier will never touch; a Smuggler has eight skill points per level to the Soldier's three.** **The attack roster is a Soldier's whole combat identity and one of three for everyone else.**

### 11.5 The one exception, and it is closed

**Reaction chains do not consume your declaration**, which is where breadth would convert into extra actions. **`§10`'s single pool closes it.**

### 11.6 Class grants sit on top

**These are the picks a player *chooses*.** **What a class is *given* is separate, and belongs to the class workstream** — see `§7`.

**Which rate each class runs at: `CLASS-ATTACKS-01 §2`.** **Settled and no longer provisional.**

> **⚠ The provisional assignment this section used to carry was wrong in three places.** **Guardian moved from Combat to Middle** — `PT-54.2`, K2's feat schedules put it with the Scout. **Marksman moved to Specialist**, because `featgain.2da` gives it the Smuggler's 11 rather than the Soldier's 23. **And Combat is now a two-class tier**, because the Soldier is genuinely alone in the data.

---

## 12. Resolution rulings

**Five things three independent playtest reports found the corpus does not state.** **All five arise in the first round of ordinary combat.**

### 12.1 Critical threat — what ×2, ×3, and ×4 mean

> **Every Precision entry in three rosters says *critical threat ×2 / ×3 / ×4* and no document defines it.**


### ⚠ `crithitmult` carries no information — `PT-172`

**Derived, `baseitems.2da`, both games.**

    K1    crithitmult = 2 on every weapon without exception
    K2    2 on all but three — Ion Blaster, Ion Rifle, Bowcaster at 3

**⚠ `PT-146` and `EQUIPMENT-01 §105` port K1. So for our source the multiplier is uniform.**

> **The critical multiplier cannot distinguish a weapon. Exactly what `PT-72` found of base attack bonus.**

**Recorded beside it so nobody builds a weapon distinction on a column that has none.**

**⚠ `critthreat` is where the information is** — three values, 1 / 2 / 3, and it is the multiplier on the threat *range* rather than on the damage. **That is the column `§292`'s widening rule reads.**

**And K2's three exceptions are worth knowing rather than porting:** **all three are ion weapons or a bowcaster, and K2 raised them as part of the same pass that bumped every lightsaber a die step** — **the pass `EQUIPMENT-01 §105` declined for widening the Jedi gap.**


**A weapon's printed threat range is its base.** **The multiplier widens it by that factor, counting downward from 20.**

| Weapon base | ×2 | ×3 | ×4 |
|---|---|---|---|
| **20 only** *(1 number)* | **19–20** | **18–20** | **17–20** |
| **19–20** *(2 numbers)* | **17–20** | **15–20** | **13–20** |

**A vibrosword threatens on 19–20. With Deathstroke it threatens on 13–20 — a 40% threat chance.**

**A double-bladed lightsaber threatens on 20 only. With Deathstroke, 17–20.**

> **This is the reading that makes a weapon's own threat range matter.** **The alternative — a flat 17–20 regardless of weapon — would erase the vibrosword-versus-double-blade trade `EQUIPMENT-01 §4b` records.**

**The critical *multiplier* is separate and unchanged.** **`crithitmult` 2 means damage doubles.** **`Power Attack` raises it by 1.**

### 12.2 A declaration is atomic

**When a multi-attack declaration drives a target past 0 wounds partway through, the remaining attacks still resolve.**

> **The target is removed after the whole declaration finishes, not mid-Barrage.**

**Attacks may not be redirected to a second target once declared.** *A Barrage aimed at a trooper who falls on the second strike wastes the third.*

**Spread chains are the exception and always were** — **they name their targets when declared.**

### 12.3 Stun timing

**A stun prevents the target's next full turn.**

**It begins immediately.** **A fresh stun on an already-stunned target refreshes it — the count restarts from the newest hit.**

**A stunned character may still use reactions**, and **does not lose an action already readied.**

> **Refresh is the load-bearing clause.** **Without it a Precision build cannot lock a target, and with it, it can.** **That is precisely what S1 and S4 are measuring.**

### 12.4 Disabled, dying, dead — in play

**`E-2` gives the thresholds. This is what they mean at the table.**

| Wounds | State |
|---|---|
| **0** | **Disabled.** Takes no actions. **Still a legal target.** |
| **−1 to −9** | **Dying. Loses 1 wound per round** and may take no actions. **A Medicine check stabilises.** |
| **−10** | **Dead. Removed.** |

### 12.5 What an attack roll is

**No document assembled the expression. Here it is.**

> **`d20 + base attack bonus + ability modifier + Weapon Focus + declaration modifier + situational`**

**Melee and lightsaber use Strength. Ranged uses Dexterity.**

**Situational covers flanking `+2`, cover on the target, Dodge, Guarding Stance, and anything else that names an attack-roll modifier.**

**And damage:**

> **`weapon dice + ability modifier + Weapon Specialization + declaration modifier`**

**Melee adds Strength. Ranged adds nothing** — `EQUIPMENT-01 §1`. **A two-handed weapon adds 1.5× Strength.**

**⚠ Lightsabers add Strength for this playtest.** **`EQUIPMENT-01 §4b` quotes the source saying *"lightsabers are not melee weapons,"* which is a statement about upgrade rules and critical behaviour rather than a damage rule.** **Provisional and flagged: it is ±3 a hit on every Jedi.**

### 12.6 Ability modifiers apply to saving throws

> **`d20 + base save + ability modifier.`** **Fortitude uses Constitution, Reflex uses Dexterity, Will uses Wisdom.**

**Nothing in the corpus stated it and every pregen omitted it.**

### 12.7 The reaction pool exists without a reaction chain

**`§10`'s *lower of tier and allowance* caps how many times a **chain** may fire. It does not gate the pool itself.**

> **Opportunity attacks are universal — `ACTION-ECONOMY-01 §10`.** **A character with a Dexterity or base-attack allowance has reactions whether or not they own Parry, Snap Shot, or Overwatch.**

**The Consular remains the intended zero case: `+0` in both measures, no reactions at all.**

---

## 13. Stealth damage is a rider, not a declaration

**⚠ SUPERSEDED — `PT-193`.** **This move was reversed and the reversal was never written back.**

**`Sneak Attack` is a melee attack chain in `ATTACKS-05` and `Stealthy Shot` is its ranged equivalent in `ATTACKS-04`, both gated `2 / 4 / 10` by `§223` above.**

**⚠ The feat chain that replaced them was itself replaced by `Killer's Instinct` and never deleted.** **Both sat in `FEATS-LIBRARY-01` 120 lines apart for the whole class workstream.**

> **⚠ STRUCK by owner ruling — `PT-198`.** **`Sneak Attack` and `Stealthy Shot` ARE declarations. You choose one instead of another attack.**

**This sentence said the opposite and it is the framework document, so a reader checking the governing rule got the wrong answer.**

**⚠ `PT-195` reversed.** **I ruled it a rider on the argument that `ATTACKS-01` governs because it is the framework document.**

> **The right principle applied to the wrong instance — the framework document can be the one that is stale, and here it was.**

### Why it moved

**Every source treats stealth damage as a rider.** **In KOTOR it is a passive on the sheet — you never queue it.** **In 3.5 it applies to every qualifying attack of a full attack. In 5e it is added once per turn to an attack you were making anyway.**

**Ours made it a declaration, so it competed with Velocity for the same slot — and one attack cannot beat three.**

**S6 measured the consequence.** **A level-4 chain gated behind ten ranks of Stealth and two attack picks was worth 14.8 a round.** **`Shoot`, the free attack every character owns, was worth 9.** **The specialist paid for a 60% improvement over nothing.**

| | Per round | Rounds to drop a Sith Trooper |
|---|---|---|
| **As a declaration** | 14.8 | **3.0** |
| **As a rider** | **22.0** | **2.0** |
| *Korr's Barrage, unconditional* | 27.3 | 1.6 |

**Still behind the fighter, which is right. Close enough that the investment bought something, which it was not.**

### What it cost

**Two chains left each roster and became one feat chain.** **The melee and ranged versions were duplicates — as a rider, which weapon you hold does not matter.**

**Position keeps `Quick Attack` and `Point Blank Shot`** — **both about where you stand, which is what the axis is named for.** **Stealth was always about whether they can see you, which is a condition.**

**And it sits beside `Killer's Instinct`, which was already a rider.** **A character who invests in stealth now stacks both on whatever declaration they choose** — **which is the shape the feat implied and the roster contradicted.**

---

## 14. The unarmed roster

**`ATTACKS-07`.** **`Jab`, `Punch` and `Kick` are one attack under three names — one unarmed strike, damage set by `Unarmed Specialist`.**

**And `Echani Strike` → `Echani Flow` → `Way of the Six Sisters`**, at 5 / 9 / 14, **two strikes rising to four, damage on Dexterity rather than Strength, prone on two hits.**

> **The gate is `Echani Combat Training`, which `SPECIES-CHAPTER-v2` makes trained rather than heritable.** ***"Other species may learn the chain from an Echani teacher."***

**Which makes it the only thing in the corpus a GM grants on a narrative event rather than a level.**


---

## ⚠ An item may grant an attack chain — `PT-315`

> **A few items grant a chain while equipped. Unequip it and the chain is gone.**

**25 of 994 items do this — 2.5%, and every one is in the corpus's top price decile.**

    Droid CEPB        27,200 cr    POWER_BLAST + Improved + Master
    Tehk'la Blade     23,000 cr    CRITICAL_STRIKE + Improved
    Arg'garok         18,500 cr    POWER_ATTACK + Improved

**⚠ The item grants the ladder as the source gives it — not a single tier.** **The constraint is the equipment slot, not the tier count.**

> **You are not getting free chains. You are committing to a weapon.**

### ⚠ It does not count against chain access

**`PT-173` derived that a chassis-restricted character needs `N ≤ access`** — **an ACCESS limit, not a purchase budget.**

**⚠ A granted chain is not purchased and does not consume access.** **So an item cannot make a legal build illegal, and the four zero-slack classes — Bounty Hunter, Engineer, Agent, Droid Master — are unaffected.**

### If you already hold the chain

**⚠ The grant does nothing and takes nothing away.** **A higher purchased tier is not downgraded by a lower granted one.**

### ⚠ And this is why a weapon has a name

**`Arg'garok` is not a big axe. It is *the Power Attack axe*.**

**Which is worth more than mechanical tidiness, and it is what the source was doing.**
