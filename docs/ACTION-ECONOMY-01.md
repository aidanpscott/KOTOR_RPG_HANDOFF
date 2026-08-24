# ACTION-ECONOMY-01

**What a character can do in a round, and which budget it comes from.**

**Settled.** **Items marked ⚠ are noted for playtest or belong to another workstream; none of them blocks play.**

**Round length: 6 seconds.** *RCR is d20 and uses the same. KOTOR's real-time rounds are 3 seconds, which is why a 6-second stun there is one round here.*

**Square size: 2 metres.** *RCR's own unit — d20's 5-foot square converted to metric, which is why every species record reads Speed 10 metres. Every distance in the corpus is already in metres and lands on a clean square count without conversion.*

| | Metres | Squares |
|---|---|---|
| **Movement** | 10 | **5** |
| **Melee reach** | 2 | **1** |
| **Point-blank band** | 5 | **2–3** |

---

## The five budgets

| Budget | Frequency |
|---|---|
| **Move** | Every round, up to your speed, splittable around your Action |
| **Action** | **One per round** |
| **Bonus** | **One per round, only when something grants it** |
| **Gear** | **One per round** |
| **Reaction** | **From the pool — 1 to 3 per encounter** |

**Plus one free interaction per turn.**

---

# 1. Action

**The main thing you do. One per round, and resolving it ends your turn.**

| Action | What it does |
|---|---|
| **Attack** | **Declare one attack.** It applies to every swing or shot this round. `Strike` and `Shoot` are the defaults. |
| **Use the Force** | **A power targeting an enemy or an ally.** Counts as your declared attack. |
| **Dash** | **Double your movement this round.** |
| **Disengage** | **Your movement provokes no opportunity attacks.** |
| **Dodge** | **Attacks against you take −4 until the start of your next turn**, and you gain +4 on Reflex saves. |
| **Aid** | **An ally's next attack roll or skill check gains +2**, if you can plausibly help. |
| **Hide** | **A Stealth check** against the better of enemy Awareness or Alertness. |
| **Ready** | **Name a trigger and an action.** When it fires, spend a reaction to take it. **Your turn ends.** |
| **Scan** | **An Awareness or Alertness check** to find what you have missed — a hidden enemy, a trap, a way out. |
| **Slice** | **A Slicing check** against a terminal, droid, or system. |
| **Treat** | **A Medicine check** on a wounded ally within reach. |
| **Repair** | **A Repair check** on a droid within reach. |
| **Improvise** | **Anything else the GM allows.** Kick a console, cut a cable, shove someone off a ledge. |

> **⚠ Throwing a grenade is an Attack, not Gear.** **It is a ranged attack roll with an area effect** — treating it as Gear would let a character grenade *and* declare an attack in the same round.

---

# 2. Bonus

**Only when a feature, power, or piece of equipment grants one. You do not have a Bonus by default.**

| Bonus | Granted by |
|---|---|
| **Self-directed Force power** | **A power that targets only you** — Speed, Valor, Battle Meditation on yourself. |
| **Class features** | **Whatever the class chapter grants.** Deferred. |

> **⚠ The Bonus list is short and that is deliberate.** **In 5e a character without a granting feature simply has no Bonus** — and most of what fills it here belongs to the class workstream.

---

# 3. Gear

**One per round. Using a consumable or activating a worn device, on yourself or an ally within reach.**

| Gear use | Examples from `baseitems.2da` |
|---|---|
| **Medical** | Medpac · Advanced Medpac · Life Support Pack · Antidote Kit |
| **Combat chemical** | Adrenal Strength · Adrenal Alacrity · Adrenal Stamina · Battle Stimulant |
| **Device** | Energy Shield · Echani Shield · Droid Shield · Stealth Field Generator |
| **Droid** | Repair Kit · Computer Spike · Security Spike *(applied, not used in a check)* |

> **This is the setting's category.** **Blaster-era combat runs on consumables, and `baseitems.2da` carries dozens.** **If each cost an Action nobody would use them; if free they would be spammed.**

**And it gives a character with nothing good to declare something useful to do** — which matters most for the classes with the fewest attack picks.

**⚠ Not Gear:** **throwing a grenade** *(Attack)*, **placing a mine** *(Action — a Demolitions check)*, **using a spike in a Slicing or Security check** *(Action — the check is the action)*.

---

# 4. Reaction

**From the pool. `ATTACKS-01 §10`: 1 to 3 per encounter, by Dexterity modifier or base attack bonus, whichever serves better.**

| Reaction | Trigger |
|---|---|
| **Opportunity attack** | **An enemy leaves your melee reach on foot** while you can see it. **One `Strike` at no penalty** — no chain applies. Prevented by Disengage. **⚠ Not available to droids** — see below. |
| **Parry** *(chain)* | A melee attack against you. |
| **Snap Shot** *(chain)* | An enemy enters your line of sight or leaves cover. |
| **Overwatch** *(chain)* | Declared on your turn; fires when an enemy moves or attacks. |
| **Readied action** | Your named trigger fires. **This is how a ranged character reacts to someone approaching** — see below. |

> **All of these draw on the same pool.** **A character who spends reactions on opportunity attacks has none left to parry** — which is the decision the single pool exists to create.

### `Ready` is the ranged answer, and nobody has used it

**Opportunity attacks trigger on an enemy *leaving* melee reach. Nothing triggers on an enemy *closing*.**

> **That is deliberate and it is D&D's own line.** **Entering reach provokes nothing without a specific feat** — 5e's Polearm Master, and 2024 removed even that. **Ranged characters do not get opportunity attacks; melee gets zone control and ranged gets range.**

**A character who wants to shoot an approaching enemy uses `Ready`.** **Name the trigger, spend the reaction when it fires.** **`§1`.**

**And `Guarded Step` is our Polearm Master** — a feat that grants an opportunity attack when an enemy moves to flank you.

**⚠ `Ready` has been available in six scenarios and no character has used it once.** **That is a discoverability problem, not a rules gap.**

### Droids cannot make opportunity attacks

**An opportunity attack is one `Strike`. `Strike` is melee. Melee is closed to every droid chassis.**

> **So a droid with a reaction allowance and no reaction chain has no legal way to spend it.**

**A droid that should be able to react must hold `Snap Shot` or `Overwatch`.** **Those are the only two reaction chains open to any chassis.**

**⚠ Found in play, not in review.** **A scenario printed five reaction uses across four enemy droids and not one was spendable under any circumstance.**

**⚠ A character with Dexterity +0 and base attack bonus +0 has no reactions at all**, including opportunity attacks. **That is a Consular, and it reads correctly.**

---

# 5. Free interaction

**One per turn, and it costs nothing.**

**Draw or stow a weapon, or switch to a second loadout** · **Open or close an unlocked door** · **Drop something you are holding** · **Pick up one item within reach** · **Hand an item to an adjacent ally** · **Speak** — a sentence or two, not a speech

**A second interaction in the same turn costs your Action.**

---

# 6. Rulings that needed argument

## 6.1 Force powers cost the Action

**Every Force power costs your Action. There is no exception.**

> **Including self-buffs.** **An earlier ruling made them a Bonus because none was ever cast in sixty rounds of testing — but the cause was a bad duration conversion, not the cost.** **See `PLAYTEST-RULINGS-01 §C24`.**

**Durations convert by rounds, not seconds.** **KOTOR runs 3-second rounds; divide printed seconds by 3.** **Force Valor is 7 rounds, Burst of Speed 12, the Energy Resistance chain 40.**

**At those durations a buff pays for itself across a long fight and does not across a short one** — **which is the decision the power is meant to pose.**

### A self-buff does not end your turn

**`ATTACKS-01 §2` ends your turn when you resolve your declaration. A self-buff is the exception.**

> **You may move after casting one.** **Everything else — an attack, an offensive power, a heal, a power on an ally — still ends the turn.**

**It costs your Action, so you do not also attack.** **What you keep is the movement.**

**Which is the KOTOR image exactly: a Jedi raises a barrier at the door and then walks through it.** **Without this you must move first and cast second, and a character who buffs is rooted for a round in a game where position decides flanking, cover, and reach.**

## 6.2 Cover

**Nothing in the corpus mentions cover, and blaster combat is built on it.**

**Cover is a property of position, gained by moving. It is not an action.**

| Cover | Defence | Reflex saves |
|---|---|---|
| **Half** — a low wall, a console, a corner | **+2** | **+1** |
| **Three-quarters** — a doorway, a pillar, a crouching position behind a barricade | **+5** | **+2** |
| **Total** | **cannot be targeted** by attacks that need line of sight | — |

**Aligns with `SKILL-RESOLUTION-01`'s ±2 / ±5 / ±10 modifier ladder.**

> **Blaster combat is built on cover and nothing in the corpus mentioned it.** **Making it positional rather than an action means it costs movement, which is the correct price** — and it gives the GM something concrete to describe about a room.

**⚠ Two things cover interacts with and neither is settled.** **Whether `Covering Fire` should let an ally move without losing cover**, and **whether a lightsaber's Form II barrier-cutting removes cover** — *`Stabbing Strike` cuts through a bulkhead, and a bulkhead is cover.*

## 6.2a Range — `PT-163`

**⚠ `PT-160` recorded that no range rules existed and that two written feats already depended on them.** **This is the system, ported from the games and expanded where a straight port would do nothing.**

### The source model

**KOTOR gives every ranged weapon a maximum: **pistols 24 m, rifles 28 m**.** **Verified against `EQUIPMENT-01` — eight ranged weapons, two distinct values, no others.**

**And KOTOR 2 applies penalties in two places:** *shooting past your weapon's range, and shooting an enemy who is in melee at point blank.*

**⚠ A straight port does nothing.** **A KOTOR corridor is about 4 metres and a room about 15.** **Every indoor encounter sits inside both weapons' maximum, so the number never fires.**

### The expansion: the printed range is an *increment*, not a ceiling

| Distance | | |
|---|---|---|
| **Within one increment** | **24 m** pistol · **28 m** rifle · **16 m** sidearm | **no penalty** |
| **Each further increment** | to 48 / 56 / 32, then 72 / 84 / 48 | **cumulative −2 attack** |
| **Beyond three increments** | past 72 / 84 / 48 m | **cannot be attempted** |

**⚠ `SKILL-RESOLUTION-01`'s ±2 / ±5 / ±10 ladder is the warrant for −2 per step**, and three increments is the RCR shape compressed — **the source's ten-increment ceiling is meaningless at a table where a long room is 20 metres.**

> **Which makes the printed number do work at every distance instead of at one.**

### Point blank — the rule the source has and we did not

**⚠ In KOTOR a melee attacker gets `+10` against a ranged attacker at point blank, and the ranged attacker gets a `+10` close-proximity bonus back.** **Players noticed those cancel and asked why the rule exists.**

**Ours does not cancel:**

> **Firing a ranged weapon while adjacent to an enemy is at **−4**.** **The Reaction axis is the answer — `Snap Shot` fires as they close, before they are adjacent.**

**⚠ And `Close Combat` now has a definition.** **It read *"+1 attack at short range"* with short range undefined.** **Short range is within one increment. The feat is a specialist's answer to the `−4`, and it stacks against it rather than against nothing.**


### ⚠ And the melee-against-ranged bonus did not exist either

**`FEATS-LIBRARY-01`'s `Close Combat` reduces *"the usual +6"* an enemy gets for engaging a ranged fighter in melee.** **Grepped: that `+6` is written nowhere.**

> **A feat that reduces a bonus, and the bonus was never stated.** **Same defect as the range gap and found in the same pass.**

**Stated now, and it is the other half of the point-blank rule:**

    firing a ranged weapon while adjacent to an enemy      −4 attack
    attacking an adjacent enemy who holds a ranged weapon  +2 attack

**⚠ Not `+6`.** **The source's `+10` was cancelled by a `+10` and did nothing; a `+6` on top of the `−4` is a `10`-point swing on one axis, which is outside `SKILL-RESOLUTION-01`'s whole modifier ladder.**

**`+2` and `−4` is a 6-point swing and it is decisive without being absurd.**

**⚠ `Close Combat` is repriced against the real number.** **Its tiers reduce the enemy's bonus from `+2` to `+1` to `0`, rather than from a `+6` that never existed.**


### ⚠ Point blank is 4 metres, not 5, and the increments in squares

**`§9` sets a square at 2 metres and `§587` records that every distance in the corpus lands cleanly on one.**

**⚠ `ATTACKS-04`'s `Point Blank Shot` and three `Spray` tiers use **4 metres** — 2.5 squares.** **They do not land cleanly and they are the only distances in the corpus that do not.**

**Corrected to 4 metres — two squares.** **`PT-165`.**

**Which also settles what *point blank* means, because two rules used two definitions:**

    adjacent            1 square    2 m    the −4 firing penalty
    point blank         2 squares   4 m    Point Blank Shot, Spray

> **⚠ Adjacent and point blank are different distances and both were in the corpus unstated.** **Adjacent is *in melee with you*. Point blank is *close enough that they cannot react*.**

**The increments, in squares:**

    pistol   11 squares   no penalty   |  to 23   −2  |  to 34   −4
    rifle    14 squares   no penalty   |  to 28   −2  |  to 42   −4

**⚠ 11 and 14 squares against a map that `§551` says is ten to fifteen across.** **One increment covers a typical encounter, which is why the penalty tiers only fire outdoors or across a hangar — and that is correct.**


### ⚠ Three of the four source ranges do not land on our grid

**Found by check 20 immediately after `PT-165` claimed every distance did.**

    source   squares   snapped   
    16 m      8.5       16 m      ion blaster, sonic pistol
    24 m     11.5       24 m      blaster pistol, hold-out, disruptor pistol
    24 m     12.5       24 m      blaster carbine
    28 m     14.0       28 m      all rifles, bowcaster — already clean

**⚠ Snapped to the grid. `PT-166`.**

**23 and 25 both land on 24 — twelve squares.** **That is not a loss: the carbine's 2-metre edge over a pistol was one square in a game that has no squares, and it did nothing.**

> **⚠ The alternative was changing the square, and `§9` records that 2 metres is RCR's own unit — a 5-foot square converted — and that every species speed is 10 metres because of it.**

**Moving the square to make four weapon ranges tidy would move every speed, every reach and every area effect in the corpus.**

**Four ranges move by at most 2 metre. That is the cheaper end.**

### What this unblocks

**`Master Spotter` — *"within half their weapon's maximum range"* — now resolves: half of one increment.**
**⚠ The `Sharpshooter` can be revisited.** **`PT-160` built it on *one shot, lined up* because outranging was not a thing that happened. It is now.**

**⚠ Still blocked: the `Pirate`'s dogfighting. That is ship rules, not range.**

---

## ⚠ SUPERSEDED — the gap `PT-160` recorded, kept for the record

**`PT-160`. Grepped `ACTION-ECONOMY-01`, `ATTACKS-01` and `ATTACKS-04` for maximum range, range penalties, short and long range. Nothing.**

**The only ranges in the corpus are two numbers on equipment lines — blaster rifle 28 m, blaster pistol 24 m — and nothing consumes them.**

> **⚠ There is no penalty for shooting at distance, no maximum beyond which you cannot, and no benefit to being far away.** **A rifle's 28 metres is a fact about the weapon that changes nothing.**

**Two written rules assume a system that does not exist:**

**`FEATS-LIBRARY-01`'s `Master Spotter`** — *"within half their weapon's maximum range."*
**`Close Combat`** — *"+1 attack at short range"*, with short range undefined.

### ⚠ It has now blocked two classes

**The `Pirate`'s dogfighting has no ship rules — `FINDINGS-27 §3.5`.**
**The `Sharpshooter` cannot be built on *outranging people* because outranging is not a thing that happens.**

**⚠ Both were built on what the archetype has *instead*, and both should be revisited when range exists.**

**Recorded here rather than in a class document, because it is a combat-system gap and the next class to want it will be the third.**

---

## 6.3 What a dying character can do

**`E-2` gives the thresholds — disabled at 0 wounds, dying from −1 to −9, dead at −10.** **Nothing says what a dying character may do on their turn.**

**Nothing. They lose 1 wound per round until stabilised.** **A Medicine check by an ally stops the bleed.**

---

# 7. Two weapons

> **There is no off-hand swing in this game, and dual-wielding does not add attacks to a chain.**

## 7.1 What holding two weapons does

**Your attacks alternate hands, starting with the primary.**

| Declaration | One weapon | Two weapons *or a double-blade* |
|---|---|---|
| **`Strike`** · **`Shoot`** | 1 | **2** — P O |
| **Flurry · Rapid Fire** *(all tiers)* | **3** | **4** — P O P O |
| **Saber Swarm** *(Ataru, all tiers)* | **4** | **5** — P O P O P |
| **Dual Strike** | 2 | 2 — **P O** |
| **Everything else** — Power, Precision, Position, Control, Support | 1 | **2** — P O |

> **A second weapon adds one attack to any declaration.** **What it does not do is change a Velocity chain's own count** — **Flurry is three swings whether you hold one blade or two; the second weapon adds a fourth.**

**⚠ `PT-9` previously ruled the opposite — that only `Strike` and `Shoot` gained an attack — and said this table would be corrected to match. It was revised the other way instead.**

> **`PT-42` settles it in favour of this table, because it is KOTOR's** — **a second weapon there grants one extra attack whatever you queued, and Power Attack's bonus applies to all of them.**

**`§7.5` is rewritten to agree.**

### Velocity does not scale with tier

**Flurry, Rapid Fire, and Saber Swarm grant the same number of attacks at every tier. The tiers reduce the penalty.**

> **This is KOTOR's shape.** **Flurry there gives +1 attack at tier 1, tier 2, and tier 3 alike** — **−4/−2, then −2/−1, then nothing at all.**
>
> **An earlier draft had the tiers grant three, four, and five attacks. That made Power and Precision unplayable**: both apply their bonus to every attack, and one enhanced swing cannot compete with five ordinary ones. **The imbalance was ours, not inherited.**

**And there are no iterative attacks.** **A character with attack bonus +20 still makes one base attack.** **In KOTOR, extra attacks come only from dual-wielding, a Velocity declaration, and Force Speed. Ours matches.**

**Ataru is the exception at four**, and it pays two Force points per use for it.

## 7.2 What it costs

**Every attack that round takes the dual-wield penalty.**

| | Penalty |
|---|---|
| **Two weapons, no feat** | **−4** |
| **Two-Weapon Fighting** | **−3** |
| **Advanced Two-Weapon Fighting** | **−2** |
| **Master Two-Weapon Fighting** | **−1** |

**Never zero** — the principle every attack chain follows.

> **The feat chain is what makes dual-wielding viable.** **At −4 with no feat it is a bad trade; at −1 it is a good one.**

## 7.3 What it buys

**One extra attack on `Strike` and `Shoot`.**

**And two damage profiles.** **Alternating hands means each attack uses that weapon's dice, its upgrades, and its crystal.** *A vibrosword primary and a short-blade offhand deal different damage on alternating strikes; two lightsabers carry two crystals.*

## 7.4 Two-handed weapons

**A two-handed weapon adds **1.5× your Strength modifier** to damage, rounded down.**

> **Without this a two-handed vibrosword is strictly worse than two blades** — fewer attacks, no second damage profile, and no compensating benefit. **The 1.5× is 3.5's own answer and RCR inherits it.**

## 7.5 Which declarations get the second attack

**Every declaration except the ones listed below.** **A second weapon adds one attack, appended to whatever your declaration already gives you.**

**Velocity chains keep their own count and gain the extra on top** — **Flurry is three swings, four with two weapons.**

**These do not involve the offhand at all:**

| | Why |
|---|---|
| **Disarming Strike · Disarming Shot** | **An opposed roll, not a volume of blows.** A dual-wielder does not disarm twice. |
| **Sweep Attack · Staggering Shot** | One knockdown, one stagger. |
| **Covering Fire · Guarding Stance** | Neither deals damage. |
| **Parry · Snap Shot · Overwatch** | **Reactions.** They come from the pool, and the pool is not per hand. |
| **Sneak Attack** *(now a feat)* | **The dice attach to the first attack of your declaration, once.** |
| **The Spread chains** — Cleave · Spray · Sarlacc Sweep | **A sweep is one motion.** **Every attack is made with the primary weapon.** |
| **Rancor's Reach · Sustained and Total Overwatch** | Same — **primary only.** |

> **`Sneak Attack` is the one worth stating explicitly.** **3.5 applies sneak damage to every qualifying attack**, which would double it for a dual-wielder. **Ours does not: the dice are the declaration's, once.**

## 7.6 Double-bladed weapons

> **A double-bladed weapon counts as wielding two weapons.** **Alternating hands, the dual-wield penalty applies, and Two-Weapon Fighting reduces it.**

**The source is explicit.** *"A double bladed lightsaber gives you an off-hand attack — for all intents and purposes it acts like dual wielding two sabers, and should be treated the same."* *"Dual bladed weapons count as two weapons and using them gives a penalty to your attack value."*

### Three differences from carrying two separate weapons

| | Two weapons | Double-bladed |
|---|---|---|
| **Penalty** | −4 / −3 / −2 / −1 | **−3 / −2 / −1 / −1** |
| **Damage** | **Two profiles** — each weapon's own die | **One profile**, both ends |
| **Upgrades** | **Two crystal or upgrade sets** | **One set, applied to every attack** |

**The reduced penalty is the source's own.** **A double-bladed weapon is *balanced*, which in KOTOR lowers the off-hand penalty the way a balanced off-hand weapon does.** **Floored at −1, like everything else.**

> **The trade is breadth against consistency.** *"If you use a double-bladed lightsabre with a particularly good upgrade crystal, its effect applies to all your attacks instead of only to half of them."* **Two sabers give you two crystals and a weaker off-hand; a double gives full damage on both ends and one crystal that always applies.**

### Two knock-on rulings

**No 1.5× Strength.** **§7.4 gives two-handed weapons 1.5× Strength to damage. A double-bladed weapon does not get it** — it is getting a second attack instead. **3.5 rules the same way.**

**Dual Strike uses its one-handed mode.** **Two swings, not one swing with damage rolled twice** — **because a double-blade is two weapons, not one large one.**

### Which weapons

**`weaponwield` 3, excluding polearms.** **Double-bladed sword · double-bladed vibrosword · double lightsaber.** *The Force Pike and quarterstaff are also `weaponwield` 3 and are **reach** weapons, not double weapons — see §15.2.*

---

## 7.7 Riposte

**A riposte is made with the primary weapon.** *The parry was made with it; the counter comes off the same blade.*

## 7.8 One thing worth knowing about Two-Pronged Attack

**Dual-wielding, its two swings are P then O.** **So the automatic critical threat lands on the offhand weapon.**

> **Which means an offhand weapon carrying the better crystal or upgrade is the correct build for that chain.** **Deliberate, and worth stating so nobody discovers it by accident.**

**⚠ And it does not apply to a double-bladed weapon**, since both ends share one upgrade set. **A double-wielder gets the auto-threat on the same weapon they always use** — simpler, and slightly worse.

---

# 8. Flanking

**Flanking exists. It gives +2 to attack rolls. It is melee only.**

**You flank when you and an ally are adjacent to the same enemy on opposite sides.** **Both of you get the bonus.**

### Why +2 and not advantage

**5e's optional rule grants advantage, and the community consensus is that it is too strong.** *"Advantage effectively conveys the equivalent of +4 to the affected roll. That's a hefty bonus, and maybe too much for flanking."*

**The reported failure is specific:** *"It cheapened all of the features that granted sneak attack, made advantage too common, and lessened impact of AC such that it wasn't worth any opportunity costs anymore."*

> **We have no advantage mechanic — we are d20 with modifiers — so the question does not arise in that form.** **+2 is what 3.5 and Pathfinder use, RCR is d20 3.x-derived, and it is what most tables house-rule 5e back down to.**

### What flanking does not do

> **Flanking does not make a target unaware.**

**`Killer's Instinct` fires on an unaware target — one that cannot see you.** **A flanked enemy sees you perfectly well; it simply cannot watch both of you.**

**And flanking does not enable the `Sneak Attack` chain.** **That chain is gated on Stealth 5 / 10 / 15 and triggered by attacking from concealment.**

> **3.5 lets flanking enable a rogue's sneak attack, and that is exactly the coupling the research warns about.** **Our three triggers stay distinct: `from Stealth`, `unaware`, and `has not yet acted`.** **Flanking is a fourth thing and it is worth +2.**

### It does not stack

**Three allies surrounding one enemy still grant +2, not +6.**

### ⚠ Flanking is cheap and that is a known problem

**The research names it:** *"There is no real cost to getting a flank"* — **because moving *around* a target does not provoke an opportunity attack; only moving *away* does.**

**Ours inherits that.** **A character can circle freely once they are in reach.**

**⚠ Worth watching in playtest.** **If flanking turns out to be free +2 every round for every melee character, the fix is to make movement within a threatened area provoke** — which is a real rule change and should not be made pre-emptively.

---

# 9. Initiative and surprise

## Initiative

**d20 + Dexterity modifier, rolled once per encounter. No re-rolls.**

**⚠ CLOSED. No class modifies initiative. `PT-96`.**

> **`PT-74` answered it by refusing.** ***"A flat initiative bonus is a different feat and every class wants it."***

**The Smuggler's slot is filled by `Quickdraw`, which was written specifically to be the conditional version** — **useless in an ambush, useless at range, useless against something that was always going to attack you.**

**⚠ And the Scout had the better claim on a flat bonus, which is the argument for giving it to nobody.** **Its feature is `Read the Ground`, built on the saves that actually distinguish it.**

## Surprise

**A surprised character takes no action in round 1.** **No move, no Action, no Bonus, no Gear, and no reactions until their first turn would have ended.**

**Determined by the ambushing side's Stealth against the better of the other side's Awareness or Alertness**, per `SKILL-RESOLUTION-01 §4`.

> **This is 5e's 2014 rule.** **2024 softened it to disadvantage on initiative; ours uses the older, harsher version.**

**⚠ An earlier version said *acts last in the first round and cannot use reactions*. Both halves were inert in play.**

**S6 ran four ambushes and surprise changed nothing in any of them.** **The Smuggler won initiative on his own roll, so acting last cost the patrol nothing.** **And the troopers held no reaction chain, so `ATTACKS-01 §12.7` left them opportunity attacks only — which a ranged ambusher never provokes.**

> **Four printed reaction uses, none spendable, surprised or not.** **A surprise rule whose two effects are "lose a position you were not going to hold" and "lose a reaction you could not spend" is decorative.**

**The stealth attack chains do not duplicate this.** **An earlier draft had *Silenced Shot* cost the target its first turn; that was cut during the replacement pass, and surprise is now a system rule rather than an attack rider.**

---

# 10. Opportunity attacks

**They exist. They are universal. They draw on the reaction pool.**

**Trigger:** an enemy **leaves your melee reach on foot** while you can see them.
**Effect:** one **`Strike`** at no penalty. **No chain applies.**
**Prevented by:** the **Disengage** action.

> **A character with Dexterity +0 and base attack bonus +0 makes none at all.** **That is a Consular, and it reads correctly.**

**Because they come from the pool they compete with Parry, Snap Shot, and Overwatch.** **A character who spends reactions swatting runners has none left to turn a blade.**

---

# 11. What remains open

**None of these blocks play.**

| Item | Where it belongs |
|---|---|
| **Which Force powers are marked Bonus** | Force workstream — a per-power pass on `PARTITION-01` |
| **Class initiative modifiers** | Class workstream |
| **Whether `Covering Fire` preserves an ally's cover** | Playtest |
| **Whether Form II's barrier-cutting removes cover** | Playtest |
| **Whether flanking is too cheap** | Playtest — the fix, if needed, is making movement within a threatened area provoke |

---

# 12. Flanking feats

**Five, in `FEATS-LIBRARY-01`.**

| Feat | Availability | Effect |
|---|---|---|
| **Blindside** → Improved → Master | **Universal organic** | Flanking grants **+3 / +4 / +5** instead of +2 |
| **Kill Box** → Improved → Master | **Assassin and Battle droids** | Same numbers |
| **Guarded** | **Universal organic** | **Enemies gain no flanking bonus against you** |
| › **Well Guarded** | **Heavy Armour Proficiency *or* the Resilience form** | **+1 Defence per adjacent enemy beyond the first**, max **+3** |
| ›› **Circle of Blades** | **The Resilience form** | Max **+5**, and **enemies adjacent to you do not grant flanking to each other against your allies** |
| **Spotter** → Improved → Master | **Universal organic** | One adjacent ally counts as flanking with you → all adjacent allies → allies at range within their weapon's range |
| **Guarded Step** | **Universal organic, single tier** | An enemy moving into a flanking position provokes an opportunity attack; **if it hits, their movement ends immediately.** Costs a reaction. |

### Why the Guarded chain gates the way it does

> **A Smuggler can stop being flanked. A Soldier in heavy plate can become harder to surround. Only a Jedi holding Resilience can shut down flanking for the whole party.**

**Soresu is the only form whose identity is *not being beaten*.** **Ferocity runs at Defence −4 rising to −6** — a Juyo duellist holding Circle of Blades would be simultaneously the hardest and easiest person in the room to hit.

**And the two gates on Well Guarded are genuinely alternative paths.** **Armour blocks Force powers**, so a Jedi cannot take the heavy-armour route and a Soldier cannot take the Soresu one. **Each gets there their own way.**

**The benefit is live only while the gate is met.** **A Jedi who switches out of Resilience loses it until they switch back** — which makes the form switch a real tactical decision, exactly as `ATTACKS-06` intends.

### Guarded Step patches a known defect

**Flanking is cheap because circling does not provoke** — only moving *away* does. **`Guarded Step` makes it cost something, for one character.**

> **A feat that fixes a systemic weakness for whoever takes it is a good feat.** **If flanking turns out to be too cheap in playtest, this is the model for the general fix.**

---

# 13. Ranged flanking and weapon range

**Source: `baseitems.2da`, K1 and K2.** *Range values are identical across both games on every weapon row.* `source_system: kotor_game`.

## 13.1 The bands

| Band | `maxattackrange` | Squares | Weapons |
|---|---|---|---|
| **Short** | **16 m** | **8** | Ion Blaster · Sonic Pistol |
| **Medium** | **24 m** | **12** | Blaster Pistol · Heavy Blaster · Hold-Out Blaster · Disruptor Pistol |
| | **24 m** | **12** | Blaster Carbine |
| **Long** | **28 m** | **14** | Blaster Rifle · Ion Rifle · Bowcaster · Disruptor Rifle · Sonic Rifle · Repeating Blaster · Heavy Repeating Blaster |

## 13.2 A ranged attacker flanks within **half** their weapon's range

| Band | Flanking reach | Squares *(2 m)* |
|---|---|---|
| **Short** | **8 m** | **4** |
| **Medium** | **12 m** | **6** |
| **Carbine** | **12 m** | **6** |
| **Long** | **14 m** | **7** |

> **Full range does not gate anything.** **28 m is fourteen squares, and a typical encounter map is ten to fifteen across** — a rifle user would flank from almost anywhere, and the rule would be decorative.
>
> **`prefattackdist` is 20 for every direct-fire weapon**, so the source's own preferred engagement distance does not distinguish them either.

**Half range gives four to seven squares.** **A real positioning constraint that still makes a rifle better at it than a hold-out blaster** — and it means a pistol user has to close to within four squares to flank at all.

**You may still shoot at full range. You simply do not flank beyond half.**

## 13.3 Grenades do not flank

**`maxattackrange` 24 m, but `maxrange` — actual projectile travel — is 10 m, and `prefattackdist` is 0.5.**

> **The engine walks the thrower to near-melee before lobbing.** **A grenade is an area weapon with no angle**, and flanking is about angle. **No grenade or thrown explosive grants or benefits from flanking.**

## 13.4 Two findings for other workstreams

**The Wrist Launcher has no `maxattackrange` at all.** **It is a launcher slot, not a fireable weapon** — the Rocket, its ammunition, carries 24 m attack range and 20 m travel. **Relevant when the Bounty Hunter class is built**, since `Weapon Proficiency: Wrist-Mounted` is assigned there.

**`weaponwield` distinguishes one-handed from two-handed at the data level.** **4 = one hand *(all pistols)*, 5 = two hands *(all rifles)*, 6 = special *(repeating blasters)*.** **`weaponsize` 2 = Small, 4 = Large.**

> **This settles which weapons can be dual-wielded without a separate ruling.** **`weaponwield` 1, 2, and 4 are one-handed and may be paired. 3, 5, and 6 are two-handed and may not.** **Two pistols yes; two rifles no; two vibroblades yes; two Force Pikes no.**

**And `weaponwield` 6 is resolved: it is the heavy autofire category, exactly two items in both games.**

> **In K1 it gated `WEAPON_PROF_HEAVY_WEAPONS`, feat row 42. In K2 that feat was cut — `XXXX_WEAPON_PROF_HEAVY_WEAPONS` — and heavy weapons folded under rifle proficiency.**
>
> **We reinstated it.** **`Weapon Proficiency: Assault Cannons` → Focus → Specialization in `FEATS-LIBRARY-01` is K1's heavy-weapon ladder restored**, and **`weaponwield` 6 is what it gates.**

### Double-bladed weapons — see §7.8

**They are `weaponwield` 3, so they cannot be paired with anything — but they function as two weapons.** **Confirmed against the source and ruled.**

---

# 14. Distances already in the corpus

**Every one was written in metres and lands cleanly on a 2-metre square.**

| Rule | Metres | Squares | Where |
|---|---|---|---|
| **Movement, Medium creature** | 10 | **5** | species records |
| **Melee reach** | 2 | **1** | — |
| **Point Blank Shot band** | 5 | **2–3** | `ATTACKS-04` |
| **Guarding Stance radius** | 3 | **1–2** | `ATTACKS-05` |
| **Bulwark radius** | 5 | **2–3** | `ATTACKS-05` |
| **Reflex Fire — ally protected** | 5 | **2–3** | `ATTACKS-04` |
| **Suppressing Fire radius** | 5 | **2–3** | `ATTACKS-04` |
| **Covering Barrage radius** | 10 | **5** | `ATTACKS-04` |
| **Lockdown splash** | 3 | **1–2** | `ATTACKS-04` |
| **Draw Closer pull** | 10 | **5** | `ATTACKS-06` |
| **Pushing Slash push** | 5 | **2–3** | `ATTACKS-06` |
| **Disarmed weapon lands within** | 3 | **1–2** | `ATTACKS-05` |
| **Grenade travel** | 10 | **5** | `baseitems.2da` |

> **⚠ Several land on an odd metre and straddle two squares.** **A 3-metre radius is one and a half squares; a 5-metre radius is two and a half.**

**Two ways to resolve, and it should be one of them consistently:**

**Round down** — 4 m becomes 1 square, 4 m becomes 2. **Tighter, and it makes Guarding Stance adjacent-only.**

**Round up** — 4 m becomes 2 squares, 4 m becomes 3. **More generous, and it keeps Guarding Stance covering a small cluster.**

**⚠ Or restate the affected radii in even metres** — 4 m and 6 m instead of 3 and 5 — **which is cleanest but touches eight entries across three documents.**

---

# 15. Reach weapons

**A reach weapon threatens 2 squares — 4 metres. An ordinary weapon threatens 1.**

> **At 2-metre squares, one square is already a long lunge for a vibroblade.** **A Force pike is a polearm and should reach further than a sword.**

## 15.1 What reach changes

**You may attack a target 2 squares away** without moving.

**You threaten a larger area for opportunity attacks.** **An enemy leaving *either* square provokes** — which is the real value, and it is why reach weapons are a positioning tool rather than a damage one.

**You still do not flank at 2 squares.** **§8 requires adjacency whatever your reach** — a pike user standing back does not make the target turn its head.

**⚠ And nothing covers the classic reach drawback.** **In 3.5 a reach weapon cannot attack an adjacent target**, which is what balances the threatened area. **Ours does not import that** — worth watching in playtest, because without it a pike is strictly better than a sword.

## 15.2 Which weapons have reach — authored, because the data has none

> **`baseitems.2da` carries no reach column in either game.** *Searched all 62 headers: no `reach`, `threat`, `threatrange`, or `meleedist`.* **Every melee weapon has identical geometry — a Stun Baton and a Force Pike have the same engagement values.**

**Reach is not a data-layer concept in KOTOR.** **It is entirely ours to author, and `weaponwield` is the closest proxy the source offers.**

### `weaponwield`, decoded

| Value | Meaning | Members |
|---|---|---|
| *(empty)* | Thrown or deployed | All grenades · Wrist Launcher · Rocket |
| **1** | One-handed, Tiny | **Stun Baton only** |
| **2** | One-handed, standard | Swords · vibroblades · **lightsaber · short lightsaber** |
| **3** | **Two-handed staff or double** | **Quarterstaffs · Force Pike · double-bladed weapons · double lightsaber** |
| **4** | One-handed ranged | All six blaster pistols |
| **5** | Two-handed ranged | All rifles · bowcaster · carbine |
| **6** | **Two-handed ranged, heavy autofire** | **Repeating Blaster · Heavy Repeating Blaster only** |

### The ruling

**Reach belongs to polearms, not to everything in `weaponwield` 3.**

| Reach — threatens 2 squares | No reach |
|---|---|
| **Force Pike** · **Quarterstaff** | Everything else, including **all double-bladed weapons and the double lightsaber** |

> **`weaponwield` 3 conflates two different things.** **A Force Pike is a polearm; a double-bladed lightsaber is two blades on one shaft.** **The first reaches further. The second reaches exactly as far as a normal blade and simply has two of them.**

**No lightsaber has reach, whatever its configuration.** **Giving Jedi a larger threatened area on top of the lightsaber roster would compound.**

---

# 16. Resolution order

**When one declaration produces several attacks, resolve them one at a time.**

> **Roll the attack. If it hits, roll its damage. Then move to the next attack.**

**Do not roll every attack first and then every damage.** **Multi-die damage is rolled together** — 2d6 is two dice at once, not two separate rolls.

### Why the order is a rule and not a preference

**Korr declares Barrage: five strikes, each doing 2d6 + 4 on a hit.**

**Resolving attack-by-attack and resolving in batches produce the same *expected* outcome and different *actual* ones**, because they consume randomness in a different order.

> **At a table with physical dice that does not matter.** **In a seeded engine, in a replay, or when two GMs run the same encounter, it decides the result.**

**`ENGINE-SHAPES-01` makes the engine event-sourced with seeded RNG.** **A replay that resolves in a different order than the original produces a different fight from the same seed.** **This rule is what makes the seed mean something.**

### Order within a round

**Attack rolls, saves, opposed rolls, and skill checks all draw d20.** **They resolve in the order they arise, and initiative order breaks simultaneity.**

**Each die type draws independently.** *A character wielding a vibrosword and a blaster in the same round draws d6 for one and d8 for the other; the two do not interleave.*

---

# 17. What remains open

**None of these blocks a playtest.**

| Item | Where it belongs |
|---|---|
| **How odd-metre radii round** — 4 m and 4 m on a 2 m square | **A ruling. §14.** |
| **Whether reach weapons can attack adjacent targets** | Playtest — 3.5 says no, we did not import it |
| **Whether flanking is too cheap** | Playtest |
| **Which Force powers are marked Bonus** | Force workstream |
| **Class initiative modifiers** | Class workstream |

**And three that block one:**

| Blocker | Needs |
|---|---|
| **Weapon damage dice and type** | **`baseitems.2da`** |
| **Armour Defence bonus and maximum Dexterity** | **`baseitems.2da`** |
| **Ability score generation** | **A ruling.** *RCR uses 4d6-drop-lowest; KOTOR uses point buy.* |

**Everything else is written.** **`CLASS-TABLES-BASE` covers Soldier, Scout, and Smuggler; `CLASS-TABLES-JEDI` covers the three Jedi classes.** **Machinist needs `k2_classes.2da`.**

---

# 18. Two acquisition rulings

**Both surfaced from playtest reports and neither was stated anywhere.**

## 18.1 Grants do not consume picks

**`ATTACKS-01 §11.6` says class grants sit on top of attack picks. The same holds for feats.**

> **⚠ A class no longer grants attacks — `PT-89` replaced them with four credits the player spends.** **What remains free: a racial feat, a class-granted feat, and the four credits themselves.**

> **A racial feat, a class-granted feat, and a class-granted attack are all free. None spends a pick.**

**So `Blaster Integration` and `Environmental Sealing` on an Astromech cost nothing. Neither does `Killer's Instinct` on a Smuggler.**

## 18.2 Weapon and armour proficiency

**Every class is proficient with the weapons and armour its concept requires, granted free at 1st level.**

> **Nothing in the corpus said so, and the consequence was absurd: no pregen carried a proficiency, so Korr could not legally draw his own vibrosword.**

| Class | **Recommended opening** — `PT-89` |
|---|---|
| **Soldier** | All weapons · Light, Medium, and Heavy armour |
| **Scout** | Blasters, blaster rifles, melee weapons · Light and Medium armour |
| **Smuggler** | Blasters, melee weapons · Light armour |
| **Machinist** | Blasters, melee weapons · Light armour |
| **Jedi Guardian · Sith Warrior** | Lightsabers, blasters, melee weapons · **light and medium armour** |
| **Jedi Sentinel · Jedi Consular · Sith Assassin · Sith Inquisitor** | Lightsabers, blasters, melee weapons · **light armour** |
| **Bounty Hunter** | **All weapons · light and medium armour** — **⚠ Row added; the table had nine rows for ten classes. `PT-107`** |
| **Marksman** | Blasters, blaster rifles · light and medium armour |
| **Engineer** | Blasters · light armour |

**A character may still buy proficiency in anything their class does not grant** — that is what the ladders in `FEATS-LIBRARY-01` are for.

> **⚠ REVERSED by owner ruling. `PT-144`.** **Force classes are granted armour: the two `Combat`-rate ones — Jedi Guardian and Sith Warrior — take light and medium; the other four take light.**

**⚠ This touches a stated rule rather than a gap.** **`EQUIPMENT-01 §5.2` records that armour blocks Force powers and that robes have no Dexterity cap.** **That rule is unchanged — what changes is that a Force character is now *proficient* with armour and may make the trade knowingly.**

**Proficiency is permission, not obligation.** **A Guardian in medium plate still cannot use Force powers while wearing it; the difference is that they no longer have to spend a feat to find that out.**

**⚠ And it makes `PT-128`'s unresolved grant moot.** **`sas`, `sma` and `jwa` carried `Armour Proficiency: Light` and `sld`, `jma` and `jwm` did not — a split that stratified by nothing.** **Every Force class now has it.**

---

# 19. Conditions

**Each of these was defined inside whichever entry first needed it, then referenced by four or five others as though it were general.** **This is the general definition. Where an entry scales one of them, it says so in its own text.**

## 19.1 Stunned

> **A stunned character loses their full turn** — no Action, no Bonus, no Gear, no movement.
>
> **They may not use reactions while stunned.**
>
> **And attacks against them ignore their Dexterity bonus to Defence.**

**A fresh stun on an already-stunned target refreshes it. The count restarts from the newest hit.**

**A stunned character does not lose a readied action already declared.**

**Being easier to hit is KOTOR's own behaviour** and it is what makes a stun worth its save DC. **It is also the difference between stunned and surprised.**

### A saved stun becomes Slowed

> **A successful save against a stun does not negate it. The target is Slowed for the same duration instead.**

**This is the source's own rule and it is stated on every stun power it has.** **`Force Stun`: *"A successful Fortitude save… means the target is slowed for the duration instead of stunned."*** **`Force Stasis` and `Force Stasis Field` say the same.**

**It applies to every stun in the system** — **Force powers, `Critical Strike`, `Precise Shot`, and anything added later.**

> **A stun is never wasted. You either lose your turns or you get slow.**

**And the interaction with `§19.3` is the reason to have it.** **A Slowed enemy's `Jedi Hunter` range halves, so an enemy who saves against a stun aimed at protecting your Jedi still stops chasing her.** **The power redirects him either way.**

### Durations

| Source | Seconds | **Rounds** |
|---|---|---|
| **`Critical Strike` · `Precise Shot`** — weapon riders | — | **1** |
| **`Force Push`** | 3 | **1** |
| **`Force Wave`** | 6 | **2** |
| **`Force Stun`** | 9 | **3** |
| **`Force Stasis`** · `Stun Droid` · `Disable Droid` · `Destroy Droid` | 12 | **4** |

**Converted at `PT-24`'s rate — printed seconds divided by 3.**

**The weapon riders stay at one round deliberately.** **A rider on an attack should not match a power that costs an Action and Force points.**

## 19.2 Surprised

> **A surprised character takes no action in the first round at all**, and **may not use reactions until their first turn would have ended.**
>
> **They are not easier to hit.**

**The reactions clause is the point of the condition.** **You were surprised because you failed to react.**

**But surprise is a failure of attention, not of balance.** **A surprised soldier still has his shield up and his feet under him — he simply has not started shooting yet.** **`Sneak Attack` is what rewards attacking someone who cannot see you, and it is a separate condition.**

## 19.3 Slowed

**Source: `FORCE-POWERS-01`, `Force Slow`.** *"The victim suffers a −2 penalty to Defense, Reflex saves, and attack rolls."* **Duration 30 seconds — 10 rounds under `PT-24`.**

> **−2 to Defence, Reflex saves, and attack rolls.**
> **Movement is halved, rounded down.**
> **And because `TARGETING-01`'s middle proximity band is *your own movement*, that band halves with it.**

**The last clause is ours and it is the interesting one.**

**A slowed trooper who cannot close on the Jedi stops trying.** **He deals with whoever is actually in front of him** — **which is what a soldier who has just realised he is too slow to reach the swordsman would do.**

> **No clause and no cross-reference.** **The band is his movement, so halving one halves the other.**

> **So `Force Slow` becomes a targeting tool as well as a debuff.** **Cast on the enemies converging on your Jedi, it sends them back to the rest of the party.**

**And it gives a Consular something to do that is not damage** — **which the playtest found she badly needed.**

## 19.5 Unaware

> **A character is unaware of you if they cannot perceive you.**
>
> **You are Hidden from them** — a successful Stealth check, and you have not revealed yourself.
> **They are Stunned.**
> **They are blinded or otherwise cannot see.**

**Attacking reveals you**, so it fires once per approach unless you hide again.

**Attacks against an unaware character ignore their Dexterity bonus to Defence.**

### What is deliberately not unaware

**Surprised. Prone. Slowed. Flanked. A target that has simply not acted yet.**

> **That last one is `Quick Attack`'s condition and always was.**

**And surprised stays out on purpose.** **`§19.2` says a surprised character is not easier to hit** — **if surprise made you unaware it would strip Dexterity and quietly reverse that.** **A surprised soldier still has his feet under him; he has not started shooting yet.**

**⚠ Facing is not a criterion.** **`PT-2` struck the 180° arc from `Jedi Defense` because the corpus does not model facing.** **An earlier version of `Killer's Instinct` said *"you are in Stealth, behind it, or it is blinded"* and the middle clause was unreachable.**

### The same test runs in reverse

**A character unaware of you cannot see what you are holding or casting.**

> **So a Stunned trooper does not trigger `Jedi Hunter`, and neither does one you are Hidden from.** **`TARGETING-01 §3.1`.**

**One definition serves the stealth feats and the targeting rules, which is the point of defining it centrally.**

## 19.4 Prone

**Five documents referenced it. One defined it, for itself.**

> **A prone character takes +2 damage from melee attacks, and standing costs half their movement.**

**Nothing else.** **No Defence penalty, no attack penalty.** **A prone rifleman shoots from the floor at full effect** — **which is correct, and it is why knockback against a shooter is worth little.**

**`Sweep Attack`'s chain now reads as a scaling of a general condition** rather than a private rule: **its tiers raise the save DC and add its own riders on top of this.**

## Knockback is 3 squares, not 2

**Base speed is 10 metres — 5 squares.** **Standing costs half of that, rounded up under `§14`: 3.**

| Pushed | Movement left after standing | Squares to re-close | Result |
|---|---|---|---|
| **2** | 2 | 2 | **re-closes and attacks** |
| **3** | 2 | 3 | **turn denied** |

> **At 2 squares the knockback denied nothing at all.** **The target stood, walked back the two squares, and attacked exactly as it would have.**

**Three squares also matches `Force Push`, which pushes 4 metres — and which denied the Dark Jedi two full turns in S4.** **It was the only Force power either Jedi cast in twenty rounds, and the movement denial is why.**

**⚠ Applies to melee enemies only, and that is a narrow buff by design** — **thirty-one enemy combatants across seven scenarios and three of them were melee.** **Being pushed three squares does not break a rifleman's line of sight or exceed his range.**

---

---

---

# 20. Who an enemy attacks

> **`TARGETING-01` governs.** **Two gates — reach, sight, and whether they are still standing — then a score.**

**This section previously carried a complete scoring model of its own.** **`TARGETING-01` was later written as a ladder, independently, by someone who did not know this existed.** **The two contradicted each other on the sign of persistence and both were live.**

**They are now one document.** **The scoring table and its load-bearing −3 came from here; `Jedi Hunter`, the duellist preference, and the visibility test came from the ladder and became modifiers.**

**⚠ Recorded rather than quietly deleted.** **`TARGETING-01 §7` holds the full comparison, because the failure mode — building the same system twice and shipping both — is one the gate cannot catch.**

---

# 21. Piloting in bad conditions

**Storms, ash, ion interference, heavy weather, and anything else that makes a vehicle harder to read.**

> **−4 on Pilot checks made in bad conditions.**

**The GM calls when conditions are bad.** **It is one number rather than a scale, because a table does not need a weather system.**

**⚠ `Nikto, Pale` ignore it entirely.** **`Weather Sense` — they read weather the way other species read a room.**
