# FEATS-LIBRARY-01 — Every Feat, by Availability

> **⚠⚠ DO NOT REGENERATE. `PT-618`, `PT-627`.**
>
> **⚠ THIS FILE IS HAND-MAINTAINED despite the header it used to carry.** **`scripts/gen_feats.py` writes to the REPO ROOT, not to `rules/` — running it creates a SECOND, DIFFERENT file: 258 entries against this one's 221.**
>
> **⚠ Every feat edit — `PT-559`, `PT-568`, `PT-590`, `PT-615`, `PT-620`, `PT-621` — went in BY HAND and survived only because the generator has never written here.**

**221 entries across 90 chains.**

> **Feats and attacks are separate systems.** **A feat is a permanent property; an attack is an option in a round.**
>
> **No attack appears in this document.** **The rosters are `ATTACKS-04` (ranged, 11 chains), `ATTACKS-05` (melee, 14 chains), and `ATTACKS-06` (lightsaber, 14 chains)** — **107 entries on their own acquisition schedule.** *See `ATTACKS-01 §1` and `§11`.*

**Naming convention: the adjective always precedes the name.**

---

## Summary

**⚠ THE TABLE BELOW DOES NOT MATCH THE DOCUMENT — `TRACE-100`.** It states **90 chains and 221 entries**. A direct extraction counts **74 chains and 192 entries**, excluding `§5a` (a class-to-ladder table) and `§5b` (prose definitions), neither of which contains feats.

**⚠ And `CHARGEN-DATA-01` carries a third figure, 156.** **None of the three agree, and none is asserted here** — the library needs a recount, and this is the fourth count in this corpus found unreliable today.

| Group | Chains | Entries |
|---|---|---|
| **1. Everyone** — organics and all droids | 6 | 16 |
| **2. Organics and combat droids** | 3 | 9 |
| **3. Organics only** | 26 | 68 |
| **4. All droids** — the chassis | 16 | 36 |
| **5. Restricted** — class or chassis | 39 | 92 |

---

# 1. Everyone — organics and all droids

| Feat | Description | Effects |
|---|---|---|
| **Cautious** | Careful, deliberate handling of dangerous devices and quiet movement. | +1 Demolitions and Stealth. |
| › Improved Cautious |  | +2 Demolitions and Stealth. |
| ›› Master Cautious |  | +3 Demolitions and Stealth. |
| **Gear Head** | An instinct for machinery — what it does, how it opens, and how to make it do something else. | +1 Repair, Security, and Slicing. |
| › Adept Gear Head |  | +2 Repair, Security, and Slicing. |
| ›› Master Gear Head |  | +3 Repair, Security, and Slicing. |
| **Skill Focus** | **Renamed from Class Skill. One feat exists per skill — 23 in total.** The fourth of five aptitude sources. | **Grants aptitude in that skill: 1 point per rank instead of 2**, and raises the rank cap to character level + 3. |
| **Toughness** | Raw physical resilience — the ability to keep standing. | +1 vitality per level. **Retroactive** for levels already gained. |
| › Improved Toughness |  | +2 vitality per level, and **−2 damage** from any hit under 20. |
| ›› Master Toughness |  | +2 vitality per level *(overrides, not cumulative)*, −2 damage under 20, and ⚠ **a further `−2` on hits of 20 or more** — `PT-629`. *(source: −10%)* |
| **Two-Weapon Fighting** | Training in fighting with a weapon in each hand, or with a double-bladed weapon. **⚠ Pairable weapons are wield classes 1, 2 and 4 — `PT-169`. A rifle or a heavy weapon cannot be paired with anything.** | Dual-wield penalty reduced from −6/−10 to **−6 main / −6 off** |
| › Advanced Two-Weapon Fighting |  | **−4 main / −4 off.** |
| ›› Master Two-Weapon Fighting |  | **−2 main / −2 off.** A balanced off-hand weapon reduces this further to 0 / −2. |
| **Weapon Proficiency: Blaster** | Basic training with blaster pistols and hold-outs. | Allows the weapon to be equipped. **Without proficiency it cannot be used at all.** |
| › Weapon Focus: Blaster |  | +1 attack. |
| ›› Weapon Specialization: Blaster |  | +2 damage. **Critical hits multiply it.** |

---

# 2. Organics and combat droids

| Feat | Description | Effects |
|---|---|---|
| **Close Combat** | Training for ranged fighters caught at knife distance. **Astromechs cannot take these.** **⚠ Universal — granted to the Scout at 1, purchasable by anyone. `PT-208`.** | **+1 attack within one range increment** — `PT-163`. **⚠ And an adjacent enemy's `+2` against you drops to `+1`.** Level 4 |
| › Improved Close Combat |  | **+2**, and the adjacent enemy's bonus drops to **0**. Level 8 |
| ›› Master Close Combat | **Authored — the source chain stops at Improved.** | **+3**, and **your own `−4` for firing while adjacent drops to `−1`** |

> **⚠ Repriced by `PT-164`.** **The chain reduced *"the usual +6"* and that `+6` was written nowhere.** **A feat that reduced a bonus nobody had stated.**
| **Dueling** | Single-weapon combat discipline — **the counterpart to Two-Weapon Fighting.** | **+1 attack and defence** when unarmed or wielding a single weapon of **wield class 1, 2 or 4** — `PT-169`. **⚠ A class-3 staff does not qualify: it is already two weapons** |
| › Advanced Dueling | Single-weapon combat discipline — **the counterpart to Two-Weapon Fighting.** A character focused on one weapon fights more efficiently than one splitting attention. | **+2 attack and defence.** Level 4. |
| ›› Master Dueling | Single-weapon combat discipline — **the counterpart to Two-Weapon Fighting.** A character focused on one weapon fights more efficiently than one splitting attention. | **+3 attack and defence.** Level 8. |
| **Weapon Proficiency: Blaster Rifle** | Rifles, carbines, and repeaters. | Allows the weapon to be equipped. |
| › Weapon Focus: Blaster Rifle |  | +1 attack. |
| ›› Weapon Specialization: Blaster Rifle |  | +2 damage. |

---

> **⚠ `PT-1462` — TWO ROWS IN THIS DOCUMENT ARE WRONG, AND THE NOTE IS HERE RATHER THAN IN A CELL.**
>
> **`Plating Proficiency: Light`** sits under **§3 Organics only** and its own text says **DROID ONLY**. **The extraction is faithful; the source row is misfiled.** It belongs in `§4`.
>
> **`Environmental Sealing`** carries `availability = selectable` while its text says *granted at 1st level to every droid* — and **`granted` already exists and is used by 188 feats.** **A wrong value, not a missing field.**
>
> **⚠ AND WHY THIS IS NOT IN THE ROWS:** I first appended both marks **to the Effects cell**, which extracts into `effect` — **the field the Feats screen shows a player.** A re-extraction would have shipped *"⚠ PT-1462 — IN THE WRONG SECTION"* **into player-facing text.** A defect annotation must never live in a data cell.

# 3. Organics only

| Feat | Description | Effects |
|---|---|---|
| **Plating Proficiency: Light** | ⚠ ⚠ **DROID ONLY — `PT-615`.** A chassis rated to carry plating. **⚠ EARNED BY LEVEL, not granted by class.** | **Allows LIGHT plating — `g_i_drdltplat001–003`.** ⚠ Character level 1. |
| › **Plating Proficiency: Medium** |  | **MEDIUM plating.** ⚠ Character level 7. |
| ›› **Plating Proficiency: Heavy** |  | **HEAVY plating.** ⚠ Character level 13. ⚠ **CLOSED to `Astromech` and `Remote`** — `PT-577`. |
| **Armour Proficiency: Light** | Basic training in wearing light armour. Without it, the armour cannot be equipped at all. | Allows light armour on body, head, and hands. |
| › Armour Proficiency: Medium | Training in heavier plating that trades mobility for protection. | Allows medium armour. |
| ›› Armour Proficiency: Heavy | The heaviest personal protection available. | Allows heavy armour. |
| **Blindside** | An instinct for the moment an opponent cannot watch you. | **Flanking grants +3 instead of +2.** |
| › Improved Blindside |  | **+4.** |
| ›› Master Blindside |  | **+5.** |
| **Conditioning** | Physical hardening against everything the galaxy can throw at you. | +1 to all saving throws. |
| › Improved Conditioning |  | +2 to all saving throws. |
| ›› Master Conditioning |  | +3 to all saving throws. |
| **Cybernetic Implantation** | **Reinstated from cut content.** Surgical grounding for cybernetic hardware. Without it, implants cannot be installed. | Allows level 1 implants. |
| › Advanced Cybernetic Implantation |  | Allows level 1–2 implants. |
| ›› Master Cybernetic Implantation |  | Allows level 1–3 implants. |
| **Elusive** | Never quite where the blow lands. | **+1 Defence.** Always active. |
| › Improved Elusive |  | **+2 Defence.** |
| ›› Master Elusive |  | **+3 Defence.** |
| **Evasion** | Training so complete that an area attack can be avoided entirely rather than merely survived. **⚠ Granted to the Scout at 6th level — `sct_granted`, `feat.2da`. Purchasable by anyone else.** | On a successful Reflex save, take **no** damage instead of half. |
| **Freetrader** | Life between worlds — flying, trading, and knowing who to ask. | +1 Appraise and Pilot. |
| › Improved Freetrader |  | +2 Appraise and Pilot. |
| ›› Master Freetrader |  | +3 Appraise and Pilot. |
| **Guarded** | You do not give anyone your back. | **Enemies gain no flanking bonus against you.** |
| › Well Guarded | The more of them there are, the less any one of them matters. | **+1 Defence for each enemy adjacent to you beyond the first**, to a maximum of **+3.** *Live only while the gate is met — a Jedi who switches out of Resilience loses it until they switch back.* |
| ›› Circle of Blades | Nobody gets behind you, and nobody gets behind the person you are standing in front of. | **Maximum rises to +5**, and **enemies adjacent to you do not grant flanking to each other against your allies.** *Live only while you hold Resilience.* |
| **Guarded Step** | They cannot get around you without paying for it. | **An enemy that moves into a flanking position against you provokes an opportunity attack.** **If it hits, their movement ends immediately** — they do not reach the flank. **Costs a reaction from the pool.** Single tier. |
| **Hardiness** | Carrying on when the body wants to stop. | +1 Athletics, Scavenging and **Survival**. |
| › Improved Hardiness |  | +2 Athletics, Scavenging and **Survival**. |
| ›› Master Hardiness |  | +3 Athletics, Scavenging and **Survival**. |
| **Hustler** | Quick hands and hard leverage — the two ways to take something that is not offered. | +1 Intimidate, Sleight of Hand, and Streetwise. |
| › Improved Hustler |  | +2 Intimidate, Sleight of Hand, and Streetwise. |
| ›› Master Hustler |  | +3 Intimidate, Sleight of Hand, and Streetwise. |
| **Improvisation** | Making do with what you have and what you know. | **Once per encounter, attempt a check you otherwise could not** — either a **trained-only skill with no ranks**, or **a different skill in place of the one called for**, if you can describe how. **Resolves at half your ranks in the skill used.** |
| › Improved Improvisation |  | **Twice per encounter.** |
| ›› Master Improvisation |  | **Twice per encounter, at full ranks.** The half-ranks penalty is removed. |
| **Linguist** | A trained ear for how languages are built. | **+1 language**, spoken and read/write. |
| › Improved Linguist |  | **+2 languages** total. |
| ›› Master Linguist |  | **+3 languages** total, and **basic comprehension of any tongue related to one already known** — no check required. |
| **Loremaster** | Deep knowledge of the dead, the living, and the Force. | +1 Archaeology, Mysticism, and Xenology. |
| › Advanced Loremaster |  | +2 Archaeology, Mysticism, and Xenology. |
| ›› Grand Loremaster | **The name already contains *master*, so the chain uses Advanced and Grand.** | +3 Archaeology, Mysticism, and Xenology. |
| **Boresight** | Shots placed where they are hardest to turn aside. **⚠ Universal — granted to the Scout at 4 / 8 / 12, purchasable by anyone. `PT-208`.** **⚠ Renamed from `Marksman`, which collided with the class of that name — `PT-206`.** | **Enemy Blaster Bolt Deflection −2** against your ranged attacks. **Always active.** *(The passive half of KOTOR's Precise Shot. The damage half is an attack — see `ATTACKS-01`.)* |
| › Improved Boresight |  | **Enemy BBD −4.** Level 6 |
| ›› Master Boresight |  | **The target's Blaster Bolt Deflection does not apply to the first ranged attack you make each round.** Level 12 |

> **⚠ Repriced from five tiers to three at `1 / 6 / 12` — `PT-209`.** **The source ran `PRECISE_SHOT_I–V` at 4 / 8 / 12 / 16 / 20 and `PT-101` cut `Targeting` from eight tiers to three for the same reason.**

**⚠ And the capstone went categorical because the arithmetic demanded it.** **`Deflecting Slash` reaches `+15` deflection; a `−6` against that is noise.**

> **This is the one thing that makes a blaster user relevant against a lightsaber** — **and it is the KOTOR moment: watching your bolts come back until they stop coming back.**

**⚠ *First attack each round* is `PT-188`'s pricing.** **Without it the capstone triples on a `Barrage`.**
| **Mobility** | **Reinstated from cut content.** Restored and verified functional by TSLRCM. | **+10% movement rate.** *Source: TSLRCM changelog. Whether 10% is BioWare's value or the modders' is unstated.* |
| **Naturalist** | The study of living things in the field rather than the archive. | +1 Beast Handling, Botany, and Science. |
| › Improved Naturalist |  | +2 Beast Handling, Botany, and Science. |
| ›› Master Naturalist |  | +3 Beast Handling, Botany, and Science. |
| **Nimble** | Moving the body cleanly — over obstacles, through water, out of the way. | +1 Acrobatics and Swim. |
| › Improved Nimble |  | +2 Acrobatics and Swim. |
| ›› Master Nimble |  | +3 Acrobatics and Swim. |
| **Perceptive** | Noticing what is there, and noticing when someone is watching. | +1 Alertness and Awareness. |
| › Improved Perceptive |  | +2 Alertness and Awareness. |
| ›› Master Perceptive |  | +3 Alertness and Awareness. |
| **Regenerate Vitality Points** | Accelerated natural healing. | **0.5 vitality every 6 seconds**, in and out of combat. Doubled under Battle Meditation. |
> **⚠ The `Sneak Attack` FEAT chain was here and is DELETED — `PT-193`.**
>
> **Owner: *"the `Sneak Attack` feat chain was replaced with `Killer's Instinct`, since `Sneak Attack` is now an attack tree. Same for `Stealthy Shot`, the ranged equivalent."***
>
> **⚠ The replacement happened and the replaced chain was never removed.** **Both sat in this file 120 lines apart for the whole class workstream, and four rulings were built on the one that should not exist.**

| **Spotter** | You make the opening; someone else takes it. | **One ally adjacent to your target counts as flanking with you, regardless of position.** |
| › Improved Spotter |  | **All allies adjacent to your target.** |
| ›› Master Spotter |  | **Allies attacking your target at range also count**, within **half one range increment** — 12 m with a pistol, 14 m with a rifle. **⚠ Resolved by `PT-163`; it previously read *"half their weapon's maximum range"* against no range system** |
| **Tenacity** | Refusing to stop when the body has run out of reasons to continue. | **+2 to your death threshold.** ⚠ You die at `−(Constitution + 2)` — `PT-559`. |
| › Improved Tenacity |  | **+4 to your death threshold.** |
| ›› Master Tenacity |  | **+6 to your death threshold**, and **Constitution damage is halved.** *⚠ Constitution drain shrinks the death threshold directly — this protects the band it widens.* |
| **Underworld Connections** | You know people. Not how the fringe works — **specific people in it.** | **Black-market vendors will deal with you**, opening restricted goods that are otherwise unpurchasable. **Once per world, you know someone here.** Single tier. *Distinct from Streetwise, which reduces what you pay; this changes what you can buy at all.* |
| **Weapon Proficiency: Assault Cannons** | **Reinstated from cut content.** Heavy repeating weapons and mounted cannons. | Allows the weapon to be equipped. |
| › Weapon Focus: Assault Cannons |  | +1 attack. |
| ›› Weapon Specialization: Assault Cannons |  | +2 damage. |
| **Weapon Proficiency: Melee Weapons** | Vibroblades, vibroswords, quarterstaffs, and Mandalorian melee weapons. | Allows the weapon to be equipped. **Droids cannot take this.** |
| › Weapon Focus: Melee Weapons |  | +1 attack. **Does not affect lightsabers** — they have their own. |
| ›› Weapon Specialization: Melee Weapons |  | +2 damage. |

---

# 4. All droids — the chassis

| Feat | Description | Effects |
|---|---|---|
| **Blaster Integration** | Special universal ports allow internal placement of most blaster pistol models, tapping the energy pack and emitters as though factory installed. | **Integrates a blaster into the frame as a self-contained weapon system.** **Granted at 1st level to Astromech and Remote droids** — the two chassis with no hands to hold one. |
| **Droid Interface** | Lets a droid speak with other droids that use no sentient language. | Unlocks droid-to-droid dialogue and machine interrogation. |
| **Droid Upgrade 1** | As a droid gains experience its programming becomes more adaptable, accommodating more sophisticated hardware. ⚠ **THE DROID'S OWN CAPACITY TO RECEIVE — `PT-583`. An organic cannot hold it. `Installation` is the MASTER'S counterpart.** | Allows level 1 droid upgrades. Granted at level 1. |
| › Droid Upgrade 2 |  | Allows level 1–2 upgrades. Granted at level 7. |
| ›› Droid Upgrade 3 |  | Allows level 1–3 upgrades. Granted at level 13. |
| **Installation 1** | ⚠ **Authored — `PT-583`. Droid Master only, granted by the class.** Skill at fitting hardware into a droid that is not you. | **Allows you to INSTALL level-1 upgrades into any droid you own.** ⚠ Granted at Droid Master 1. |
| › Installation 2 |  | **Level 1–2.** ⚠ Droid Master 3. |
| ›› Installation 3 |  | **Level 1–3.** ⚠ Droid Master 7. |
| **Droid Upgrade 4** | **Authored.** The chassis accepts a fourth hardpoint. | **Allows level 4 droid upgrades.** *Extends the source's three-slot ladder, which stops at level 13 — the only chassis chain that ends before level 20.* |
| **Emergency Reboot** | When the frame takes a killing blow, the core drops to minimum power and waits. | **Once per day, when reduced to 0, go inert instead of being destroyed.** You reactivate after the encounter at **10% vitality.** *A droid does not die. It stops working.* |
| › Improved Emergency Reboot |  | **Reactivate at 25% vitality**, and **within the encounter** if an ally is still standing. |
| ›› Master Emergency Reboot |  | **Reactivate at 50% vitality**, and **twice per day.** |
| **Environmental Sealing** | **Racial. Granted at 1st level to every droid.** A sealed frame does not breathe, and does not care what it is standing in. | **Immune to vacuum, pressure, radiation, atmospheric hazards, and airborne toxins.** *Nothing in the corpus stated this and it is true of all four chassis.* |
| **Hardened Chassis** | Reinforced plating and shock mounting. | **+2 to your death threshold.** *⚠ The droid equivalent of Tenacity — organics cannot take that chain, droids cannot take this one.* |
| › Improved Hardened Chassis |  | **+4 to your death threshold.** |
| ›› Master Hardened Chassis |  | **+6 to your death threshold**, and **immunity to ion damage's Constitution drain.** |
| **Integrated Toolkit** | Tools built into the frame rather than carried. | **Computer, security, and repair consumables cost one fewer** — minimum one. *Stacks with the `SKILL-RESOLUTION-01 §5.1` reduction curve.* |
| **Ion Shielding** | Grounding and surge protection against the weapons built to kill droids. | **Damage reduction 2 against ion weapons.** *Ion blasters, ion rifles, and ion grenades all exist in `baseitems.2da` and specifically target droids.* |
| › Improved Ion Shielding |  | **DR 5 against ion.** |
| ›› Master Ion Shielding |  | **DR 10 against ion**, and ion effects cannot disable you. |
| **Kill Box** | Converging fire on a target that cannot cover both angles. | **Flanking grants +3 instead of +2.** |
| › Improved Kill Box |  | **+4.** |
| ›› Master Kill Box |  | **+5.** |
| **Logic Upgrade: Combat** | Having witnessed combat first-hand, the droid self-upgrades its defensive algorithms. | Defence +2, rising +2 every six levels. **+2 at 1, +4 at 5, +6 at 11, +8 at 17.** |
| › Logic Upgrade: Tactician | Advanced combat processing — the chassis begins reading the fight rather than only surviving it. | **+2 attack against a target an ally or allied droid is also attacking**, and Defence as tier 1. Level 5 |
| ›› Logic Upgrade: Battle Droid | Full military combat processing. | **+4 attack** under the same condition, and Defence as tier 1. Level 11 |

> **⚠ Tiers 2 and 3 were empty and we ported the emptiness — `PT-210`.** **`FEATS-LIBRARY-01` recorded it as *"in KOTOR 2 this grants no defence bonus despite its description. A known defect."***

**Filled with what their own names promise.** **This is the droid `Squad Tactics`, and the source named the tiers for us.**

> **A Soldier coordinates by training. A droid coordinates by being on the same network.**

**⚠ Which is why `Squad Tactics` is NOT shared with droids.** **They have their own, it was already in the corpus, and two of its three tiers were doing nothing.**
| **Networked** | A live link to any droid within range. | **Share sensor data with one allied droid within 20 metres** — you each use the higher of your two Awareness and Alertness scores. |
| › Improved Networked |  | **Two allied droids, 40 metres**, and **+1 attack against any target another linked droid is attacking.** |
| ›› Master Networked |  | **Any number of allied droids on the same field**, and **+2 attack.** *G0-T0's droid army is the precedent.* |
| **Self-Diagnostic** | Continuous internal fault-checking. | **Repair kits restore +25% more vitality** when used on you. *(Droids have no Medicine; this is the equivalent.)* |
| › Improved Self-Diagnostic |  | **+50%.** |
| ›› Master Self-Diagnostic |  | **+100%, and you may repair yourself in combat** without a kit, once per encounter. |
| **Sensor Package** | Optical, motion, and sonic sensors as standard. | **+2 Awareness and Alertness**, and **a stealth field imposes no penalty on your Awareness.** *The droid answer to `SKILL-RESOLUTION-01 §4` — sensors do not see, so a field that defeats eyes does nothing.* |
| › Improved Sensor Package |  | **+4 Awareness and Alertness.** |
| ›› Master Sensor Package |  | **+6 Awareness and Alertness**, and **you detect droids and powered devices through walls** within 20 metres. |
| **Synthesised Voice** | A speech synthesiser, either fitted or learned. **A droid that ships mute is not designed to talk; one that ends up talking has usually been rebuilt for it.** | **Level 1. Astromech and Remote chassis only** — corrected at `PT-1189`, removing Battle. Both Assassin and Battle ship with a vocabulator already and cannot take this; `SPECIES-CHAPTER-v2`'s own primary Battle entry states it speaks both Basic and Binary by default, no feat required.

**Grants the ability to speak aloud** in any language the droid already understands.

**⚠ Installable.** **The part is a **speech synthesiser**, and a droid may be fitted with one instead of spending a pick** — `DROID-INSTALLATION-01`. |
| **Upgraded Storage** | Perfect recall of anything recorded — a face, a route, a conversation. | **Once per session, automatically recall any detail you witnessed.** No check. |
| › Improved Upgraded Storage |  | **Twice per session**, and **+2 to Archaeology, Xenology, and Appraise** — you are consulting an index, not remembering. |
| ›› Master Upgraded Storage |  | **Unlimited recall of witnessed detail**, and **+4 to those three skills.** |

---

# 5. Restricted — by class or chassis


## Jedi Guardian

**1 chain.**

| Feat | Description | Effects |
|---|---|---|
| **Force Jump** | If diplomacy fails, combat must be swift and decisive. The Jedi crosses the distance in a series of jumps and rolls, almost instantly. | **Closes to a target more than 10 metres away** on a standard lightsaber melee attack. Requires clear line of sight. **Counts as an ambush** against an unengaged opponent — the `Sneak Attack` dice apply if you hold them. |
| › Force Jump Advanced |  | **+2 attack and damage** on every attack in the round. Level 6 Guardian. |
| ›› Force Jump Mastery |  | **+4 attack and damage.** Level 12 Guardian. |


## Jedi Sentinel

**1 chain.**

| Feat | Description | Effects |
|---|---|---|
| **Force Immunity: Fear** | The Sentinel's mind is closed to terror. | **Immune to fear effects — cannot be `shaken` or `panicked`. `PT-446`.** *Covers `Fear`, `Horror`, `Insanity`, `On-Hit: Fear` items, and **plasma grenades** — anything that applies `shaken`, `panicked` or `cowering`. ⚠ The category does the work; the list is illustration, not definition. `k1_feat.2da` row 98 has an empty `spellid` and names no mechanic, because the engine flags a TYPE.* |
| › Force Immunity: Stun |  | **Immune to Force Push, Force Wave, Stun, Critical Strike and Sniper Shot stuns, Concussion Grenades, Flash mines, On-Hit: Stun.** Level 6. |
| ›› Force Immunity: Paralysis |  | **Immune to Stasis and Stasis Field, CryoBan Grenades, On-Hit: Paralyze.** Level 12. A Sentinel past level 11 can only be debilitated by Force Whirlwind, Wound, Choke, or Kill. |


## Soldier

**1 chain.**

| Feat | Description | Effects |
|---|---|---|
| **Squad Tactics** | Trained to fight as part of a unit rather than as an individual. **Soldiers only.** | **+2 attack** against a target another party member is attacking. |
| › Improved Squad Tactics |  | **+4 attack.** Level 4. |
| ›› Master Squad Tactics |  | **+6 attack.** Level 8. |


## Scout

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Targeting 1** | Effective with any weapon fired rather than swung. **⚠ Universal — granted to the Scout at 1, purchasable by anyone. `PT-208`.** | **+1 attack with any ranged weapon — wield classes 4, 5 and 6. `PT-209`.** *Previously read "with blasters", which excluded the bowcaster.* Granted at level 1. |
| › **Targeting 2** |  | **+2 attack**, granted at level 6. **⚠ Repriced — `PT-101`** |
| ›› **Targeting 3** |  | **+3 attack**, granted at level 12. **⚠ The ladder ends here.** The source ran to eight |
| **Uncanny Dodge 1** | The character keeps their footing even when taken by surprise. **⚠ Scout only — `PT-208`. Granted at 4.** | **Retains Dexterity bonus to defence when surprised.** Grenade DC −2. Level 4 Scout. |
| › Uncanny Dodge 2 |  | **Grenade DC −4.** **Granted at 7.** |


## Smuggler

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Killer's Instinct** | An instinct for the moment before someone knows they are in a fight. **Granted to the four classes built on striking an unaware target — Smuggler, Sith Assassin, Jedi Watchman, Scoundrel. `PT-199`.** *⚠ Previously read "the three classes that carried Sneak Attack in the source" — false twice, since the count is four and the fourth did not exist in the source.* | **+1d6 damage on any attack against a target unaware of you.** *Unaware is defined in `ACTION-ECONOMY-01 §19.5` — you are Hidden from them, they are Stunned, or they cannot see.* **A target that has not yet acted but can see you is not unaware; that is Quick Attack's condition.** **Stacks with the `Sneak Attack` chain.** |
| › Improved Killer's Instinct |  | **+2d6 against an unaware target.** |
| ›› Master Killer's Instinct |  | **+3d6 against an unaware target.** *⚠ The `Master Sneak Attack` stacking note that was here is void — `PT-193` deleted that chain. `Killer's Instinct` is the whole feat, and `Sneak Attack` is an attack tree that competes for the declaration. Wound points equal Constitution, so that is lethal to most non-boss targets. Deliberate: it is what an assassin does to someone who has not seen them.* |
| **Smuggler's Luck** | Smugglers have a knack for getting into trouble and an incredible instinct for surviving it. **Granted at 1st — `scd_granted`.** | **Defence +2 + (2 × [(level+1)/6])** in combat |
| › **Improved Smuggler's Luck** | **⚠ Tier restored.** `IMPROVED_SCOUNDRELS_LUCK`, prereq 104 | **Authored effect pending** — the source row exists and its string is not in holdings |
| ›› **Master Smuggler's Luck** | **⚠ Tier restored.** `MASTER_SCOUNDRELS_LUCK`, prereq 104 | **Authored effect pending** |

> **⚠ The source has three tiers and this document carried one.** **Same family as the Consular's chain: the ladder exists in `feat.2da` and only its first rung was catalogued.**

### Quickdraw — Smuggler only

**⚠ Ruled at `PT-74` and ⚠⚠ WRITTEN IN SINCE — ⚠ `PT-909`. ⚠ `Quickdraw — Smuggler only` IS BELOW, WITH A TABLE ROW.** **Grepped: `Quickdraw` appeared in `PLAYTEST-RULINGS-01` and nowhere else.**

> **When someone you can see turns hostile, you may attack them immediately, before anyone else acts.**

**One attack. Once per encounter.**

**⚠ *Turns* hostile is the whole condition.** **Someone already fighting you does not qualify; someone drawing a weapon mid-conversation does.**

**The cost is social, not mechanical.** **You attacked someone who had not yet attacked you, and witnesses saw it.**

**⚠ Perception needs no rule of its own.** **`ACTION-ECONOMY-01 §9`: a surprised character takes no action in round 1. Quickdraw is an action.** **A surprised character cannot use it, by a rule that already exists.**

**In the 1977 film Han shoots Greedo while Greedo is still talking.** **The point is not that Han is fast — it is that he did not wait.**


## Bounty Hunter

**1 chain.**

> **Deferred to the class workstream.**

| Feat | Description | Effects |
|---|---|---|
| **Weapon Proficiency: Wrist-Mounted** | **Bounty Hunter only.** Wrist launchers and integrated arm weapons — the Mandalorian hunter's signature. | Allows the weapon to be equipped. |
| › Weapon Focus: Wrist-Mounted | **Authored — the source has no Focus tier for this family.** | +1 attack. |
| ›› Weapon Specialization: Wrist-Mounted | **Authored.** | +2 damage. |


## Astromech droid

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Nav Computer** | *"A backup or replacement for a nav computer."* The astromech's actual job. | **+2 Pilot**, and **you may plot a hyperspace jump without a ship's navicomputer.** |
| › Improved Nav Computer |  | **+4 Pilot**, and **jumps through poorly charted space carry no penalty.** |
| ›› Master Nav Computer |  | **+6 Pilot**, and **you may plot a route no chart has** — an unmapped jump, once per session. |
| **Slicing Suite** | Dedicated intrusion hardware, not a general processor running a program. | **+2 Slicing and Security**, and **computer spikes cost one fewer** — minimum one. |
| › Improved Slicing Suite |  | **+4**, and **two fewer spikes.** |
| ›› Master Slicing Suite |  | **+6**, and **you may slice a terminal you have no physical access to** within 10 metres, once per encounter. |


## Assassin droid

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Assassin Protocols** | **Learnable, not HK-47's alone.** Targeting routines written to kill organics efficiently. | ⚠ **On a critical hit, roll again: on `17+` you deal `4d6` unstoppable damage** — `PT-630`. **Fortitude at `DC 10 + your level` negates.** *(source: 20% chance, ¼ of the target's remaining life)* |
| › Advanced Assassin Protocols |  | **1/3 of remaining life.** |
| ›› Master Assassin Protocols |  | **1/2 of remaining life.** |
| **Target Analysis** | Study a subject, then act on what the study returns. | **Spend one round observing a target. Gain +2 attack and damage against that individual** for the rest of the encounter. |
| › Improved Target Analysis |  | **+4**, and the bonus applies to **all targets of the same species or model.** |
| ›› Master Target Analysis |  | **+6**, and **no observation round is required** — analysis is instant. |


## Battle droid

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Combat Protocols** | Mass-produced infantry does not improvise. It moves and fires as one. | **+1 attack for each allied droid within 4 metres**, to a maximum of +3. |
| › Advanced Combat Protocols |  | **+2 per allied droid**, maximum +6, and **allied droids in range share your Defence bonus from Logic Upgrade.** |
| ›› Master Combat Protocols |  | **+3 per allied droid**, maximum +9, and **you may act on an ally's initiative** to coordinate a joint attack. |
| **Standardised Parts** | Nothing about you is bespoke. Any droid's components fit. | **Repair parts cost one fewer** — minimum one — and **you may salvage parts from any destroyed droid** without a check. |
| › Improved Standardised Parts |  | **Two fewer parts**, and **repairs may be performed in combat** without a bench. |
| ›› Master Standardised Parts |  | **One part for any repair**, and **a destroyed allied droid may be rebuilt** between encounters at half cost. |


## Remote droid

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Personal Cloaking Shield** | **G0-T0's, made learnable.** A cloaking field built into the frame. | **Use Stealth without a stealth field generator.** *Remote droids are the one chassis the source permits Stealth to.* |
| › Improved Personal Cloaking Shield |  | **+4 Stealth**, and the field **holds through one attack** before dropping. |
| ›› Master Personal Cloaking Shield |  | **+8 Stealth**, and **you may cloak one adjacent ally** while the field is up. |
| **Repulsor Agility** | No legs, no wheels, no ground contact. | **Ignore difficult terrain**, and **cross gaps up to 4 metres** without a check. |
| › Improved Repulsor Agility |  | **+2 Acrobatics**, and **10-metre gaps.** You may hover over hazards. |
| ›› Master Repulsor Agility |  | **+4 Acrobatics**, **20-metre gaps**, and **you may move vertically at full speed.** |


## Any prestige class

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Superior Two-Weapon Fighting** | Dual-wielding beyond ordinary training. | **−2 main / −2 off.** |
| › Advanced Superior Two-Weapon Fighting |  | **0 main / −2 off.** |
| ›› Master Superior Two-Weapon Fighting |  | **0 main / −1 off.** With a balanced off-hand weapon: **+2 main / −1 off.** |
| **Superior Two-Weapon Fighting** | **⚠ Holders: `Jedi Weaponmaster`, `Sith Marauder`, `Gunslinger` — `PT-183`.** A penalty reduction, not an attack bonus — `PT-158` | **Reduces the two-weapon penalty further, to zero at the top.** ⚠ Three classes now reach zero, so `ACTION-ECONOMY-01 §7.2`'s *never zero* needs its exception clause |
| **Superior Weapon Focus** *(any family)* | The character's skill with one weapon family is almost unmatched. **⚠ Opened from lightsaber-only by `PT-150`.** | **+1 attack**, above the Specialization tier |
| › Advanced Superior Weapon Focus |  | **+2 attack** |
| ›› Master Superior Weapon Focus |  | **+3 attack** |

> **⚠ The superior tier existed for one of six weapon families, and it was the Jedi weapon.** **A prestige Jedi could reach `+3` beyond Specialization; a prestige Soldier could reach it with nothing.**

**Six families carry the full `Proficiency → Focus → Specialization` ladder:** **Blaster · Blaster Rifle · Melee Weapons · Lightsaber · Assault Cannons · Wrist-Mounted.** **All six now carry the superior tier above it.**

**⚠ Chosen once, at entry, and locked.** **The `Commando` is the class built on it — one weapon family, taken further than anyone.**


## Jedi Weaponmaster

**3 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Deflect** | A Weaponmaster with a lightsaber has incredible skill deflecting blaster bolts. | **Blaster Bolt Deflection +[(class level + 1) / 2].** +1 at level 1 rising to +18 at 35. Main-hand lightsaber only. |
| **Increase Melee Damage** | Weaponmasters focus their strength to deliver powerful strikes. | **+2 damage** unarmed, melee, or lightsaber. Critical hits multiply it. |
| › Advanced Increase Melee Damage |  | **+4 damage.** Level 8. |
| ›› Master Increase Melee Damage |  | **+6 damage.** Level 15. |
| **Inner Strength** | Weaponmasters use the light side to shield themselves from pain. | ⚠ **`DR 1` against every source — `PT-629`.** *(source: −5% damage taken)* |
| › Advanced Inner Strength |  | ⚠ **`DR 2`.** Level 7. *(source: −10%)* |
| ›› Master Inner Strength |  | ⚠ **`DR 3`.** Level 11. *(source: −15%)* |


## Sith Marauder

**2 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Ignore Pain** | Prolonged channelling of dark side energy has accustomed the Marauder to pain. | ⚠ **`DR 1` against every source — `PT-629`.** Applied after Damage Immunity and Shields, before Toughness. |
| › Advanced Ignore Pain |  | ⚠ **`DR 2`.** Level 7. *(source: −10%)* |
| ›› Master Ignore Pain |  | ⚠ **`DR 3`.** Level 11. *(source: −15%)* |
| **Increase Combat Damage** | Sith Marauders call upon hatred and strength to deliver powerful blows. | **+2 damage** on unarmed, melee, or ranged. Critical hits multiply it. |
| › Advanced Increase Combat Damage |  | **+4 damage.** Level 8. |
| ›› Master Increase Combat Damage |  | **+6 damage.** Level 15. |


## Jedi Master

**1 chain.**

| Feat | Description | Effects |
|---|---|---|
| **Light Side Enlightenment** | Jedi Masters are greatly attuned to the light. Their presence inspires; close companions grow more in touch with the light side by example, while others rebel and fall further. | Shifts companion alignment. **Matures as the Master learns more about the Force.** |


## Sith Lord

**1 chain.**

| Feat | Description | Effects |
|---|---|---|
| **Dark Side Corruption** | A Sith Lord's command of the dark side is so great that it influences his companions. Some grow more corrupt; others find new resolve and align further with the light. | Shifts companion alignment. **Strengthens as the Sith Lord grows in power.** |


## Restricted — owner unassigned

**14 chains.**

| Feat | Description | Effects |
|---|---|---|
| **Empathy** | An instinct for reaching people, and for keeping them alive. | +1 Persuade and Medicine. |
| › Improved Empathy |  | +2 Persuade and Medicine. |
| ›› Master Empathy |  | +3 Persuade and Medicine. |
| **Finesse: Lightsabers** | As above, for lightsabers specifically. | Use Dexterity or Strength for lightsaber attack rolls. **Redundant if Finesse: Melee Weapons is held.** |
| **Finesse: Melee Weapons** | Grace and speed in place of raw power. | Use Dexterity **or** Strength for melee attack rolls, whichever is higher. Affects melee weapons and lightsabers. Does not affect unarmed. |
> **⚠ Force Channel (Alter) and Force Channel (Control) are RETIRED. `PT-103`.**

**They were `XXXX_FORCE_FOCUS_ALTER` and `XXXX_FORCE_FOCUS_CONTROL` — the two cut-content rows, reinstated while the live shipped chain they were cut in favour of was never catalogued.**

**The owner renamed the live chain to Force Channel, which is their name.** **Keeping both would put three entries called Force Channel in one document, two of them cut content and one of them real.**

**⚠ Their described effect survives in the live chain, which is what it was cut in favour of.** **The Alter/Control split does not — `PARTITION-01` governs discipline, not a feat.**

| **Force Rapport** | The pool runs deeper than the training accounts for. **Some Force users simply hold more.** | **Requires `Force-Sensitive`.** **+1 Force point per character level.** |
| › Knight Force Rapport |  | **Level 8.** **+2 Force points per character level**, replacing the tier below. |
| ›› Master Force Rapport |  | **Level 14.** **+3 Force points per character level**, and **your working maximum degrades at half the normal rate** — `FORCE-POOL-01-v3 §4.2`. |
| **Force Sensitive** | A heightened connection to the Force, previously unseen in a newly trained Jedi. | **+40 Force points** to base total. |
| **Guard Stance** | **Reinstated from cut content. ⚠ AUTHORED at `PT-620`.** A defensive posture traded against offence. | **−2 attack, +2 Defence, +2 on all saving throws.** ⚠ **A STANCE: it lasts until you ATTACK or MOVE more than half your speed.** ⚠ *The only accounts report a bonus to attributes or saving throws. `hybrid_authored`. |
| › Advanced Guard Stance |  | **−2 attack, +4 Defence, +4 on saves.** Level 4. |
| ›› Master Guard Stance |  | **−2 attack, +6 Defence, +6 on saves.** ⚠ **And you may move your FULL SPEED without ending it.** Level 8. |
| **Jedi Defense** | With a lightsaber in hand, a Jedi can turn blaster fire aside at any time. | **Opposed roll against incoming blaster attacks.** Beat the attack and the bolt is deflected; beat it by 6 or more and the bolt returns to the attacker. Only within the 180° front arc. |
| › Advanced Jedi Defense |  | **+3 Blaster Bolt Deflection.** Level 4. |
| ›› Master Jedi Defense |  | **+6 Blaster Bolt Deflection.** Level 8. |
| **Jedi Sense** | Awareness of danger before it arrives. | **Defence +2 + (2 × [level/6]).** Always active. |
| › Knight Sense |  | **Defence +2 + (2 × [level/8])** for Jedi Master and Sith Lord. |
| ›› Master Sense |  | **Defence +2 + (2 × [level/5])** for other prestige classes — the fastest progression of the three. |
| **Regenerate Force Points** | The body renews its connection to the Force faster than training alone allows. | Force regeneration **+25% out of combat, +250% in combat.** Stacks additively with the Consular's Force Channel chain. |
| **Stealth Run** | Training in stealth so extensive that speed no longer costs concealment. | **Run instead of walk while in Stealth mode.** Requires level 4. |
| **Unarmed Specialist I** | Extra experience in hand-to-hand combat. | **Unarmed damage 1–4.** Granted at level 2. |
| › Unarmed Specialist II–VIII |  | **2–8 through 8–32 damage**, granted at levels 6, 10, 14, 18, 22, 26, and 30. |
| **Weapon Proficiency: Lightsaber** | **Force classes only.** Droids can never take it. | Allows lightsabers to be equipped. |
| › Weapon Focus: Lightsaber |  | +1 attack. |
| ›› Weapon Specialization: Lightsaber |  | +2 damage. |

### ⚠ Force Channel — the live chain, and it was never catalogued

**`feat.2da`, read directly:**

    FORCE_FOCUS            jcn_granted  1    successor 89
    FORCE_CHANNEL_ADVANCED   jcn_granted  6    mincharlevel 4   successor 90
    FORCE_CHANNEL_MASTERY    jcn_granted 12    mincharlevel 8

**Three tiers, Consular-only, granted at 1 / 6 / 12 — `ATTACKS-01 §3.4`'s base ladder.** **`usetype` blank, so passive: a feat, not an attack.**

> **⚠ This document held Force Channel (Alter) and Force Channel (Control) instead — `XXXX_FORCE_FOCUS_ALTER` and `XXXX_FORCE_FOCUS_CONTROL`, which carry the cut-content prefix.**

**The two cut rows were reinstated. The live shipped chain they were cut in favour of was not.**

**And it is not bookkeeping.** **`§5` gives the Guardian `Force Jump` at 1 / 6 / 12 and the Sentinel `Force Immunity` at 1 / 6 / 12, both verified against their grant columns.** **The source assigns all three Jedi a chain on the identical schedule. We held two of three.**

**⚠ Effect pending.** **The string table rows — `1257`, `1259`, `1260` — are not in holdings.** **The reinstated cut siblings describe the family as increasing the effectiveness of Force Armour, Valor, Speed and similar; that is a secondary source and is marked as one.**

**⚠ RULED. `PT-103`. Force Channel is the Consular's restricted chain and the two cut-content reinstatements are retired.**

**The rename settled it: three entries of one name, two of them cut content, was not a state the document could hold.**

---


### Quarry — Bounty Hunter only. Authored.

**⚠ `CLASS-ATTACKS-01 §4` states the Bounty Hunter *"takes targets alive and moving."* Nothing implemented it.**

**Grepped the corpus: no rule for non-lethal damage, subdual or capture exists anywhere.** **`ATTACKS-01 §12.4` gives the window — 0 is Disabled and a legal target, −1 to −9 dying, −10 dead — and nothing lets a player aim for it.**

> **Every bounty in KOTOR is *alive if possible*. The class named after it should own the mechanic.**

| Tier | Level | Effect |
|---|---|---|
| **Quarry** | **1** | **Name one target you can see. Free action, once per encounter.** You know its exact current wounds and vitality. **Your attacks against it may be declared non-lethal at no penalty** — a quarry reduced to 0 is **Disabled and stable** rather than dying |
| › **Run to Ground** | **4** | As above, and **+2 attack against your quarry**, which gains no benefit from cover against you |
| ›› **No Escape** | **8** | As above at **+4**, and **once per encounter spend a reaction to move your full speed toward your quarry** when it moves away from you |

**⚠ Priced against `Squad Tactics`, the only comparand in the corpus.** **`Squad Tactics` is Soldier-only and reaches `+6` against any target an ally is also attacking.** **Quarry reaches `+4` against one named target and costs a naming action.**

**Strictly weaker on the attack axis, deliberately. The attack bonus is not what the chain is for.**


---


### ⚠ The Scout is the most heavily granted class in the source and we carry a third of it

**Derived, `sct_granted` in `feat.2da`, everything above proficiencies — nineteen rows:**

    FLURRY             1       UNCANNY_DODGE_1    4      EVASION    6
    RAPID_SHOT         1       UNCANNY_DODGE_2    7
    CLOSE_COMBAT       1       TARGETING_1..8     1, 5, 9, 13, 17, 21, 25, 29
                               PRECISE_SHOT_I..V  4, 8, 12, 16, 20

**Eight distinct grants and two long ladders.** **No other class in either game is close — the Soldier has three proficiency groups and two attack chains.**

**This document held `Targeting` and `Uncanny Dodge` and recorded none of the rest.**

**`Evasion` at 6th is now stated above.** **⚠ It matters because `SKILLS-01 §12.4` calls it *"the Scout's damage-avoidance feat"* while this document neither granted nor restricted it.** **A grant is not a lock — the source grants it and leaves it purchasable, and so do we.**

**⚠ `Close Combat` and `Flurry` at 1st are recorded and NOT granted.** **Both are attack chains rather than feats in our system, and granting two more would put the Scout at four granted chains and `T` = 31 — breaking the band arithmetic its chain count was assigned under.**

**Recorded so it is not rediscovered as an omission.**


---


### Terrain Sense — Scout only. Authored.

**⚠ Replaces `Terrain Sense` — `PT-207`.** **That feature shared an ally's Reflex save against area effects, and once the Scout is granted `Evasion` at 6 and `Uncanny Dodge` at 4 and 7, it was the *third* thing on one axis.**

> **All three were *do not get hit by the thing*.**

**The class is called Scout and nothing in it was about going in first.**

| Tier | Level | Effect |
|---|---|---|
| **Terrain Sense** | **1** | **On entering an area, name one feature of it before anyone acts** — a cover position, a chokepoint, a hazard, a second exit. **The GM answers truthfully.** Once per encounter |
| › **Ground Read** | **4** | **Two features**, and one ally who acts before you may use one of them — moving to a cover square you named as part of their own move |
| ›› **Forewarned** | **8** | **Two features**, and **the party is never surprised in an area you entered first** |

**⚠ It does not touch initiative.** **`PT-96` closed that deliberately — *"a flat initiative bonus is a different feat and every class wants it."*** **This changes what the party *knows*, not the order they act in.**

**And the capstone is a hard counter rather than a bonus:** **surprise is `ACTION-ECONOMY-01 §9` — a surprised character takes no action in round one.** **Negating it for the party is decisive when it fires and worth nothing when nobody was ambushing you.**

**⚠ Its whole value is a property of the encounter, like `Field Position`.** **A GM who never ambushes and never varies terrain cuts this class, which is `PT-170`'s dial reaching a third class.**

#### The Scout's defensive identity now comes from grants, not the feature

    Uncanny Dodge 1     level 4    Scout only — PT-208
    Evasion             level 6    granted to the Scout, purchasable by anyone
    Uncanny Dodge 2     level 7    Scout only

**⚠ Which is what the source does.** **24 grants, the most of any class in either game, and `PT-94` found we carried two.**

---


### Field Override — Engineer only. Authored.

**⚠ The corpus granted the Engineer the interface, the skill, and the ruling that it works. It never gave anyone a way to do it.**

**Three derived facts, all pointing one way:**

**`DROID_INTERFACE` is granted at 1st level to `drx` and to no other class column.**
**`Slicing`, `Security` and `Science` are the Engineer's own three under `PT-83`, and `Slicing` is its alone among non-Jedi.**
**⚠ `SKILL-RESOLUTION-01` already rules the case:** *"a slicer takes control of an enemy droid mid-fight. All of it runs."* **Permitted between NPCs, forbidden against a player-controlled character** — **a complete permission structure for an ability that did not exist.**

| Tier | Level | Effect |
|---|---|---|
| **Field Override** | **1** | **Declare in place of an attack.** Opposed `Slicing` against an enemy droid's **Will save**, within 20 m and in line of sight. **On a success it loses its next turn.** You make no attack this round |
| › **Subverted** | **4** | On a success it instead **takes one action of your choosing on your initiative**, that turn only |
| ›› **Turned** | **8** | As above, and it **remains under your control** until it takes damage from your party, you use the chain again, or the encounter ends. **⚠ One droid at a time** |

**Uses only machinery that exists.** **The declaration economy — `ATTACKS-01 §2`. Opposed rolls against a save — `SKILL-RESOLUTION-01 §6`, which already pairs `Intimidate` with Will. Player protection — the same section.**

**⚠ Priced.** **The Engineer gives up the least of any class when it gives up its attack.** **The class that cannot fight gets something to do instead of fighting badly.**

**Not dominant: it does nothing against organics, which is most of the game.**

> **⚠ The capstone needs a ceiling and has one.** **Without *one droid at a time*, an Engineer in a droid-heavy encounter accumulates a second party.** **With it, the strongest case is turning the single most dangerous machine on the field — which is the moment, and it is HK-47 on Tatooine.**

**⚠ OPEN.** **A turned droid acting on the Engineer's initiative gets a declaration of its own, and `ATTACKS-01 §2` gives each character one per round.** **Nothing states whether a controlled character's declaration is separate from the controller's.** **The same question `Battle Meditation` and the domination powers will raise — settle it once.**


---


### Jury Rig — Machinist only. Authored.

**⚠ `SKILL-RESOLUTION-01 §5.3` defines a droid-repair mode and gives nobody a way to use it on anyone else:** *"more vitality restored when a droid uses a repair kit **on itself**."*

> **No character in the game could repair a droid other than themselves.**

**A **Gear** action, one per round — `ACTION-ECONOMY-01 §3` — so it costs no declaration. The same price `Medicine` pays.**

| Tier | Level | Effect |
|---|---|---|
| **Jury Rig** | **1** | **Spend one repair part to restore `2d8 + half your Repair total` vitality to an adjacent droid.** Any droid, not only yourself |
| › **Percussive Maintenance** | **4** | As above, **or instead clear one ion effect, stun, or disabled state** on an adjacent droid |
| ›› **Back in the Fight** | **8** | As above, and **once per encounter restore a droid at 0 to a quarter of its vitality.** It acts on your initiative that round |

**⚠ Parity, derived.** **`Medicine` on a medpac is `2d8 + Medicine ÷ 2`.** **This is the same expression on the same action for the other half of the party.**

**Not a new power level — the missing operator for a mode the corpus already defined.**

**Not dominant: it does nothing in a party without droids.**

**⚠ The capstone overlaps `Emergency Reboot`, a chassis feat firing once per day at 0.** **Alternatives, not a stack: Reboot is automatic and self-only; this is someone else spending their action on you, and it works after Reboot is spent.**


---


### Still Standing — Marksman only. Authored.

**Derived from three ported numbers that say one thing.** **`d12`, the only one in either game. `primaryabil CON`, the only Constitution-primary class. And the spread `14 / 14 / 16 / 8 / 8 / 8` — three mental stats at the floor.**

> **A machine built to keep working after it should have stopped.**

| Tier | Level | Effect |
|---|---|---|
| **Still Standing** | **1** | **The first time each encounter you are reduced to 0 or below, take one more full turn before you become Disabled or begin dying.** Resolved immediately after the attack that dropped you |
| › **Not Finished** | **4** | **Two turns**, taken on your own initiative |
| ›› **Last Word** | **8** | Two turns, and **during them damage cannot take you below −9.** You cannot die until they are spent |

**⚠ Priced.** **One extra turn for a Combat-rate character is one extra declaration — about 27 damage at level 8.** **Once per encounter, across a three-feat investment, on the Combat class with the fewest feats at 18.**

**Not dominant: it does not prevent death and it does not heal.** **You arrive at 0 either way; the chain buys the order of events, not the outcome.**

**⚠ Interaction with `Emergency Reboot`, stated:** **a droid Marksman holding both takes the extra turns first and Reboot fires afterwards** — **Reboot triggers on being destroyed and this postpones that.**

> **The shot that should have ended him lands, and he fires back before he goes down.** **That is Canderous on the Leviathan.**

---

### ⚠ The seven class features, and a pattern worth watching

| Feature | Class | Fires on | |
|---|---|---|---|
| **Hold the Line** | **Juggernaut** — `PT-211` | any round an ally is adjacent | **broad** |
| **Quarry** | Bounty Hunter | any encounter with a named target | **broad** |
| **Still Standing** | Marksman | any encounter you are dropped in | **broad** |
| **Quickdraw** | Smuggler | a conversation becoming a fight | narrow |
| **Terrain Sense** | Scout | area effects only | narrow |
| **Field Override** | Engineer | enemy droids only | narrow |
| **Jury Rig** | Machinist | allied droids only | narrow |

**Four of seven are hard counters to a narrow category.**

**⚠ Derived: the split tracks rate exactly.** **Both Combat classes are broad. Every Specialist is narrow. Middle is split.**

> **Which is arguably what a Specialist *is* — decisive in one place rather than useful everywhere.**

**⚠ The real risk is narrower than the pattern.** **Two of the four narrow features are both about droids, and a party may contain none.** **An Engineer and a Machinist in a droid-free campaign both hold a class feature that never fires.**

**Recorded, not resolved.** **The fix if it is one: a second mode on each that applies to machinery rather than to droids — doors, turrets, security systems.** **Not proposed.**


---


## 5a. ⚠ Restricted chains are GRANTED, not bought — and `Targeting` is repriced

**The corpus never stated which. `feat.2da` carries a level in the `_granted` column for every class-restricted chain; this document files them under *restricted*, which is the section for feats a class *may take*; `ACTION-ECONOMY-01 §18.1` says grants cost nothing.**

> **Ruled: granted. The source says so and this document's own wording says so** — *"Granted at level 1"*, *"granted at levels 5, 9, 13…"*

### Why the reading mattered

**If bought:** **the Scout would spend 8 of its 16 lifetime feats on the `Targeting` ladder. Half a career, which is not a choice.**

**If granted, as ruled:** **`Targeting 8` is `+8` attack with blasters, free, by level 29.**

    Weapon Focus   +1 attack   costs 1 feat
    Targeting 8    +8 attack   costs 0

**⚠ Worth eight feats and costing none, on the class that also holds the best saves in the game.**

### `Targeting` is repriced. `PT-101`.

**Three tiers, not eight. `+1 / +2 / +3` at levels 1 / 6 / 12.**

> **`Targeting` was the outlier, not the principle.** **Force Jump, Force Immunity, Force Channel and `Uncanny Dodge` are all three-tier chains on the 1 / 6 / 12 ladder, and giving those free is what makes a class feel like itself from 1st level.**

**An eight-tier ladder reaching `+8` is a different kind of object, and the source's own Jedi equivalents stop at three.**

**⚠ `Precise Shot I–V` on the same column is under the same reading and needs the same look.**

### And one pregen was already wrong

**`PREGENS-01`, Vess, Scout 8:** *"`+6` BAB, `+4` Dex, `+1` Weapon Focus, `−1` Volley = `+10`."*

**`TARGETING_2` is granted at Scout 5 and she carries a blaster rifle.** **Her attack was `+12` under the old ladder.**

    stated   +10      hit rate 60%     8.10 dmg/round
    actual   +12      hit rate 70%     9.45 dmg/round
    melee-versus-ranged gap:  3.4x  ->  2.9x

**⚠ Three scenarios are reported against the 3.4× figure.** **The finding is not overturned — the number it is stated in moves.**

**Under the repriced ladder Vess holds `Targeting 1` only at level 8, so her attack is `+11` and the gap is roughly 3.1×.**

---


### ⚠ `Sneak Attack` — three classes, and the source gives them three speeds

**Derived from `feat.2da`, granted levels:**

    tier          1d6  2d6  3d6  4d6  5d6  6d6  7d6  8d6  9d6  10d6
    Smuggler        1    3    5    7    9   11   13   15   17    19
    Sith Assassin   1    3    5    7    9   11   13   15   17    19    ⚠ identical
    Jedi Watchman   1    4    7   10   13   16   19    —    —     —

> **⚠ The Smuggler and the Sith Assassin are granted the same mechanic on the same schedule, byte for byte.**

**And the Sith Assassin is a *base* class now — `CLASS-ROSTER-01` moved it from prestige — so two base classes would share their defining mechanic identically.**

### Ruled: three classes, three speeds. `PT-122`.

**The Watchman's ladder is the source's own answer and it generalises.**

| Class | Ladder | Caps at |
|---|---|---|
| **Smuggler** | every odd level from 1 | **10d6 at 19** |
| **Jedi Watchman** | 1, then every third | **7d6 at 19** |
| **Sith Assassin** | **1, then every second from 5** | **9d6 at 20** |
| **Scoundrel** *(prestige)* | **⚠ VOID — `PT-244`.** `PT-193` deleted the ladder | — |

> **⚠ SUPERSEDED by `PT-192`. This ten-step ladder and the three-tier chain at `§124` are the same mechanic with different numbers, 568 lines apart, and neither referenced the other.**

**`PT-101` had already decided the general case and this violated it.** **That ruling repriced `Targeting` from eight granted tiers to three, saying:** *"An eight-tier ladder reaching `+8` is a different kind of object, and the source's own Jedi equivalents stop at three."*

**⚠ A ten-step granted ladder reaching `10d6` is the same object `PT-101` rejected, written by me four rulings after I ruled it.**

#### The resolution

**`§124`'s three-tier chain governs. It is the one that fits every other chain in the corpus** — three tiers, bought, gated, capped.

**What survives from `PT-122` is the *speed distinction*, which was the finding:**

    Smuggler        reaches each tier fastest
    Sith Assassin   one level slower per tier
    Jedi Watchman   slowest
    Scoundrel       the Smuggler's speed, and it is the only class that
                    can hold Master Sneak Attack at its Stealth cap

**⚠ The three classes are granted the chain rather than buying it — `PT-101` — and reach its three tiers at different rates.** **`6d6` is the ceiling for everyone.**

**And `PT-191` still holds: one tree, the higher governs, dice never sum.**

> **⚠ The Scoundrel's ladder was ruled in `REPLY-28` and never written here. `PT-190`.**

**⚠ VOID — `PT-244`.** **This read *"a prestige class that continues a base class continues its progression"* and *"the Scoundrel is what a Smuggler becomes when `Sneak Attack` is the only thing left."***

**`PT-193` made `Sneak Attack` an attack chain anyone may buy, capped at `6d6`.**

> **⚠ The Scoundrel has no dice advantage at all. Its case is `Nowhere To Stand`, which buys openings rather than dice.**

**⚠ VOID.** **This argued about a fourth *speed* on a ladder that no longer exists.**

**⚠ Same shape as `PT-240`: the correction reached the table and stopped at the prose beneath it.** **The row above carried a supersession note; three paragraphs under it did not.**

**⚠ The Assassin's is authored.** **It sits between the other two: faster than the Watchman, one tier short of the Smuggler at the ceiling.**

**⚠ CORRECTED. `PT-127`.** **The ladder first printed as *"every second from 4"*, which reaches 10d6 at 20 — the Smuggler's own cap, one level earlier.** **It was not slower at all.**

    1, then every second from 4:   1, 4, 6, 8, 10, 12, 14, 16, 18, 20  -> 10d6
    1, then every second from 5:   1, 5, 7, 9, 11, 13, 15, 17, 19      ->  9d6

**Found by the designer computing the stated cap rather than accepting it.**

**The reasoning is the classes' own cases.** **The Smuggler's whole identity is the opening — `PT-73` gave it the Scoundrel's kit and the Scoundrel was *"`Sneak Attack` and one good opening."*** **The Assassin has a Force pool and a lightsaber as well, so it should not also hold the fastest stealth ladder in the game.**

**⚠ `Killer's Instinct` says *"granted to the three classes that carried `Sneak Attack` in the source"* without naming them.** **They are the Smuggler, the Sith Assassin and the Jedi Watchman. Now named.**


---


### Cover Identity — Agent only. Authored.

**⚠ `SKILL-RESOLUTION-01 §207–211` already rules the whole permission structure and nothing used it:** *"a mundane skill may not override the decision of a character under player control… Between NPCs, every skill works in every direction."*

> **Talking an enemy out of a fight is explicitly legal, explicitly bounded away from player characters, and no class could do it.**

| Tier | Level | Effect |
|---|---|---|
| **Cover Identity** | **1** | **Declare in place of an attack.** Opposed `Persuade` or `Intimidate` against one NPC's `Alertness` or Will save. **On a success it takes no hostile action against your party until the end of its next turn.** You make no attack this round |
| › **Deep Cover** | **4** | On a success it **leaves the encounter** if already below half vitality |
| ›› **Handler** | **8** | On a success it **acts on your initiative under your control for one round.** One NPC at a time |

**⚠ The capstone mirrors Field Override's deliberately.** **The Engineer turns machines with `Slicing`; the Agent turns people with `Persuade`.** **Neither works on the other's target and both cost a declaration.**

**Not dominant: nothing to droids, nothing to a player-controlled character by the rule above, nothing to anything without a mind.** **Against the pregen suite it works on the Sith Trooper and the Dark Jedi and fails on T4-K9 and HK-24.**

**⚠ OPEN, third instance:** **a controlled NPC acting on your initiative gets a declaration and nothing states whether it is its own or its controller's.** **Field Override, Battle Meditation and now this.**


---


### ⚠ Salvage Charge — Saboteur only. ⚠ Authored, `PT-784`.

**⚠ `SKILL-RESOLUTION-01` ALREADY PRICES RECOVERY AND NOTHING USED IT:** *"Setting a mine uses the tier DC. Disabling adds `+2`. ⚠ **RECOVERING ADDS `+5`.**"*

> **⚠⚠ NOBODY WOULD EVER ATTEMPT IT. ⚠ FAILING MEANS STANDING OVER A LIVE MINE.**

| Tier | Level | Effect |
|---|---|---|
| **Salvage Charge** | **1** | ⚠ **After an encounter ends, recover any mine you placed** with a `Demolitions` check at its tier DC `+5`. ⚠ On a failure it detonates; you take its damage. |
| › **Live Placement** | **7** | ⚠⚠ **Place a mine as a Bonus action, in combat**, in a square adjacent to you. ⚠ It arms at the end of your turn. |
| › **Nothing Wasted** | **13** | ⚠ **A thrown grenade that deals no damage may be recovered** — same check, same failure. ⚠ And `Salvage Charge` no longer requires the encounter to have ended. |

**⚠ THE CLASS IS ⚠ RENEWABLE, WHICH NOTHING ELSE IN THE GAME IS.**

> **⚠⚠ A GRENADE COSTS 100cr AND IS GONE. ⚠ THAT IS WHY PLAYERS HOARD THEM. ⚠ A `Saboteur` THROWS ITS ORDNANCE BECAUSE TOMORROW IT GOES AND COLLECTS IT.**

**⚠ `Live Placement` AT TIER 2 IS WHAT MAKES IT A **COMBAT** CLASS RATHER THAN A **PREP** ONE — ⚠ PRE-PLACEMENT ONLY FIRES WHEN A GM TELEGRAPHS A FIGHT.**

### Nothing In My Hands — Brawler only. Authored.

**⚠ `ATTACKS-07`'s unarmed roster has never had a class built on it.**

| Tier | Level | Effect |
|---|---|---|
| **Nothing In My Hands** | **1** | **Your unarmed attacks ignore 2 points of the target's armour bonus to Defence** |
| › **Through The Plate** | **4** | **4 points** |
| ›› **Unburdened** | **8** | **The first unarmed attack you make each round ignores the target's armour bonus to Defence entirely** |

> **⚠ *The first each round* — `PT-188`.** **Without it the capstone triples the moment an unarmed Velocity chain exists.**

    on all strikes, with Combination     57.0   capstone worth +15.0
    first strike only                    47.0   capstone worth  +5.0
    today, single strike                 19.0   capstone worth  +5.0

**⚠ Worth the same whether or not an unarmed Velocity chain exists.** **`FINDINGS-23` priced this class against a world with no such chain; this makes that pricing stay true.**

**And repricing the tier does not work — `ACTION-ECONOMY-01`'s 95% hit ceiling means `−6` and *all* both reach it.** **The multiplication is in the strike count, not the tier value.**

**⚠ Priced.** **`KORR` carries 7 of his 19 Defence in medium battle armour, so the capstone is worth about `+7` to hit against him.**

**That is large and it is bought with the game's worst weapon** — **`8d4` at level 30, no `Weapon Specialization`, no critical range, no reach.**

**Not dominant: worth nothing against an unarmoured target, nothing against a Jedi in robes — `ACTION-ECONOMY-01 §18.2` gives Jedi no armour at all — and nothing at range.**

> **A hard counter to exactly one thing: the heavily armoured soldier.** **Which is the fight a brawler is supposed to win.**


---


## 5b. ⚠ COMPANIONS and HENCHMEN are different things — `PT-145`, amended by `PT-571`

**`PT-145` ruled that everything a character controls is a HENCHMAN — *"its own turn, its own initiative, its own declarations."*** **⚠ IT WAS RULED TO ANSWER *"WHOSE DECLARATION IS IT"* BEFORE **Command Protocol**, BEFORE MOUNTED COMBAT, AND BEFORE BEAST OBEDIENCE EXISTED.**

> **⚠ EVERY SYSTEM BUILT SINCE HAS ANSWERED *"THE MASTER'S"*.** **`PT-201`, `PT-560` and `PT-566` all have the controlled thing act ON THE CONTROLLER'S TURN, and `PT-201` REBUILT A CLASS to make that true.**

**⚠ SPLIT. The two categories are real and the corpus needed both words.**

| | ⚠ COMPANION | ⚠ HENCHMAN |
|---|---|---|
| **What** | A Beast Master's beast · a Droid Master's droid · a mount | ⚠ A hired NPC, a converted enemy, a temporarily overridden droid |
| **⚠ Owned by** | ⚠ **The player.** | ⚠ **Nobody.** Hired, turned, or temporary. |
| **⚠ Decided by** | ⚠ **THE PLAYER.** | ⚠ **THE GM, or the AI.** |
| **Initiative** | ⚠ **Its own** — `PT-573` | Its own |
| **On death, `Normal`** | ⚠ **Dies** — `PT-558` | ⚠ The `Easy` rule: down at 0, up after combat |

> **⚠ THE CATEGORY IS ABOUT OWNERSHIP AND WHO DECIDES. IT IS NOT ABOUT HOW CAPABLE THE CREATURE IS.**

**⚠ `PT-571` WROTE *"a short fixed menu"* INTO THE COMPANION ROW AND THAT WAS WRONG — `PT-573`.** **That menu is `PT-566`'s DROID rule, and putting it in the category would have stripped the beast of its chains, its skills and its nature.**

### ⚠ BREADTH belongs to the CREATURE, not the category

| | What it can do |
|---|---|
| **⚠ A BEAST** | ⚠ **Everything.** Its own Action, its chains, its skills, its levels, a nature it can refuse from. **⚠ IT IS A SECOND CHARACTER SHEET AND THAT IS THE POINT** — `PT-153`: *"the Beast Master has one companion and it matters."* |
| **⚠ A DROID** | ⚠ **Three options** — move, one attack, one chassis action, `PT-566`. No chains, no levels, no obedience. **⚠ Deliberately LESS than a sheet, which is what lets a Droid Master field four.** |
| **⚠ A MOUNT** | ⚠ **Shares the rider's turn while ridden** — `MOUNTED-COMBAT-01`. It has no initiative of its own until it is dismounted. |



> **⚠ THAT IS THE WHOLE OF THE TABLE-TIME PROBLEM `PT-201` FOUND — one player at 62% of the round — AND IT IS WHY THE COMPANION CATEGORY HAD TO EXIST.**

### ⚠ What KEEPS the henchman rule

**`Field Override`'s capstone — a turned droid.** **`Cover Identity`.** **Any hired or converted NPC.**

**⚠ Those genuinely ARE temporary control of something that was its own creature, and giving it its own turn is correct.** **`PT-145`'s mechanism survives intact for exactly the cases it was written for.**

### ⚠ What BECOMES a companion

**A Beast Master's beast. A Droid Master's droids. A mount — `MOUNTED-COMBAT-01`.**

**⚠ `PT-145`'s own line — *"a droid an Engineer or Droid Master controls becomes a henchman. A beast a Beast Master controls becomes a henchman"* — IS REVERSED FOR BOTH CLASSES.**

**⚠ AN `Engineer`'s controlled droid stays a HENCHMAN.** **The Engineer takes control of something that was not his; the Droid Master owns his.**

**`Field Override`'s capstone — the turned droid becomes a henchman for the duration.** **⚠ Control is capped at one droid at a time — `PT-203`.**

**⚠ And a **Machinist** may *build* droids — `PT-225`. Construction is downtime work, not a class-chain tier.** *`PT-203` said Engineer; the owner has corrected it.* **The mechanism is deferred to after the classes; it depends on `EQUIPMENT-01`'s unwritten item extraction and touches the Astromech's `Portable Workbench`, which already removes the facility requirement.**
**The Droid Master — its whole premise, and it now has a mechanism before it is written.**
**The Beast Master — same.**

### ⚠ What it does not cover

**`Cover Identity`'s capstone lets an Agent control a *person* for one round.**

**That was authored with no precedent in either game, and the owner has questioned it.** **⚠ Flagged for revision rather than left.** **The tier below it — a wounded enemy leaves the encounter — is the version that fits.**

---

### Command Protocol — Droid Master only. ⚠ NOT A FEAT YOU TAKE — `PT-582`, `PT-584`.

**⚠ REBUILT THREE TIMES — `PT-201`, `PT-566`, `PT-582`.** **`PT-201`'s first version bounded *decision* cost when the expensive thing was *turns*.**

> **⚠ IT IS GRANTED BY THE CLASS at the levels below. It costs no feat slot and cannot be chosen.**

| Tier | ⚠ Granted at | Effect |
|---|---|---|
| **Command Protocol** | ⚠ **Droid Master 1** | ⚠ **You CONTROL two droids** — at character level 7, the earliest entry. **Each acts on ITS OWN INITIATIVE from a menu of three — `PT-566`, `PT-573`.** |
| › **Squad Protocol** | ⚠ **Droid Master 4** | ⚠ **THREE droids** — at character level 15 or higher. ⚠ **THIS IS THE CAP.** |
| ›› **Master Protocol** | ⚠ **Droid Master 8** | ⚠ **Still three.** **Once per encounter, as a BONUS action, every controlled droid takes its turn IMMEDIATELY AFTER YOURS instead of on its own initiative.** |

> **⚠ THREE IS THE CAP — `PT-582`. It was four.** **THE THIRD TIER IS NOT MORE DROIDS. IT IS BETTER CONTROL.**

**⚠ `Squad Doctrine` and `Master and Servants` are WITHDRAWN — the old ladder was `2 / 3 / 4` and every tier only ever added a body.**

**⚠ **Master Protocol** IS THE OLD `PT-201` SHAPE, legal ONCE PER ENCOUNTER — what `PT-573` removed as a default returns as a burst.**

**⚠ BOTH GATES MUST BE MET: the TIER from Droid Master level, the DROID COUNT from CHARACTER level — `PT-581`.**

#### ⚠ Why the first version failed both tests

    Droid Master at tier 3        1 character + 4 henchmen = 5 turns
    in a four-player party        8 turns a round for 4 people

> **⚠ One player took 62% of the round.**

**`FINDINGS-38` answered *"the problem was never the turns, it was the decisions"* and built three clauses to hold decision cost at one per round.** **Decision cost was one. Table time was five turns.**

**Each droid still rolled attacks, took damage, got targeted and moved.** **Collapsing the decisions did nothing to the turns, and turns were what `PT-151` named.**

    turns at the table    5 → 1
    clauses at tier 1     4 → 1
    PT-178                fails → passes

**⚠ Persistence and the silent-default are gone.** **They existed only because droids acted independently; on your turn there is nothing to persist through.**

**⚠ Two tests pointing at one class was a design signal and the design was wrong, not the wording.**

#### The droids themselves need no authoring

**Owner: familiars rather than fighters — specialists that reach, fly, slice and hack. Weaker is fine.**

**⚠ `SPECIES-CHAPTER-v2` already carries all four chassis as full species records:**

| Chassis | Already written |
|---|---|
| **Astromech** | **`Portable Workbench`** — item construction or upgrade work anywhere, no facility. **+2 Slicing, +2 Repair** |
| **Remote** | **`Repulsorlift Frame`** — hovers, ignores difficult terrain, no footfalls, **+4 Stealth**, 12 m speed. Tiny or Medium |
| **Assassin** | **The entire ranged suite** — `ATTACKS-01 §242` |
| **Battle** | **`Mass-Produced`** — repair at half time and cost |

> **⚠ *Flies* is the Remote. *Slices and hacks* is the Astromech. *Reaches hard places* is the Remote at Tiny. *Upgrades* is `Portable Workbench`, verbatim.**

**`AGENDA-CURRENT §215` had already said so.**

---


### ⚠⚠ Hold the Deck — Pirate only. Authored. `PT-991`

**⚠ THE `Pirate` HAD ⚠⚠ **NO CLASS FEATURE**. ⚠ `CLASSES-STANDARD-PHB §999` READ ⚠⚠ *"NOT YET WRITTEN."***

| Tier | Level | Effect |
|---|---|---|
| ⚠⚠ **Hold the Deck** | **1** | ⚠ **WHILE YOU ARE ABOARD A SHIP YOU HAVE BOARDED OR SEIZED, ⚠⚠ ALLIES WITHIN 10 SQUARES TAKE `+1` ON ATTACK ROLLS AND SAVES AGAINST FEAR** |
| ⚠ **Take the Bridge** | **4** | ⚠⚠ THE BONUS RISES TO `+2`, ⚠ AND YOU MAY **REROLL ONE FAILED `Persuade` OR `Intimidate` CHECK PER BOARDING** |
| ⚠⚠ **Nothing Is Nailed Down** | **8** | ⚠ ONCE PER BOARDING, ⚠⚠ **NAME ONE ITEM ABOARD** — ⚠ IT IS IN THE HAUL IF THE SHIP IS TAKEN |

> **⚠ IT KEYS ON ⚠⚠ **BOARDING**, WHICH `SPACE-COMBAT-01` ALREADY HAS AS A MECHANIC — ⚠ AND `PT-828` GAVE THE `Pirate` A **DOCTRINE** IN `SPACE-AI-01 §7`. ⚠⚠ THE CLASS HAD A DOCTRINE AND A SHIP AND **NOTHING TO DO ONCE IT ARRIVED**.**

**⚠ AND IT IS ⚠⚠ NOT A COMBAT BONUS IN GENERAL — ⚠ IT IS **DEAD ON FOOT**. ⚠⚠ `Hondo Ohnaka` IS THE ARCHETYPE `CLASS-ROSTER-01 §390` CHECKED IT AGAINST, ⚠ AND HE IS ONLY DANGEROUS ON HIS OWN DECK.**

---

### ⚠⚠ Triage — Medic only. Authored. `PT-991`

**⚠ THE `Medic` HAD ⚠⚠ **NO CLASS FEATURE**. ⚠ `CLASSES-STANDARD-PHB §1261` READ ⚠⚠ *"NOT YET WRITTEN."***

| Tier | Level | Effect |
|---|---|---|
| ⚠⚠ **Triage** | **1** | ⚠ **WHEN YOU STABILISE A DYING ALLY, THEY RETURN AT `1` VITALITY INSTEAD OF `0`, ⚠⚠ AND MAY ACT ON THEIR NEXT TURN** |
| ⚠ **Field Surgery** | **4** | ⚠⚠ ONCE PER ENCOUNTER, ⚠ A `Treat Injury` CHECK **RESTORES VITALITY EQUAL TO YOUR CLASS LEVEL** |
| ⚠⚠ **No One Left** | **8** | ⚠ YOU MAY STABILISE ⚠⚠ **AT RANGE**, 6 SQUARES, ⚠ WITHOUT TOUCHING THE PATIENT |

> **⚠ IT KEYS ON ⚠⚠ `DEATH-AND-DIFFICULTY-01`'s **THREE MODES**, ⚠ WHICH IS WHY TIER 1 IS WRITTEN AS *"stabilise"* RATHER THAN *"heal"*: ⚠⚠ ON `Easy` NOBODY DIES AND THE TIER **STILL DOES SOMETHING** — ⚠ IT GETS A DOWNED ALLY **BACK ON HIS FEET A TURN EARLIER**.**

**⚠ AND ⚠⚠ NEITHER FEATURE DUPLICATES A SKILL. ⚠ `Treat Injury` ALREADY HEALS; ⚠⚠ `Triage` CHANGES **WHAT HAPPENS AT ZERO**.**

---

### Read the Ruin — Treasure Hunter only. Authored.

**⚠ Adopted at `PT-147` and ⚠⚠ WRITTEN IN SINCE — ⚠ `PT-909`. Same defect as `Quickdraw` at `PT-96`.**

> **⚠ Tiers 2 and 3 CUT — `REPLY-45`, applied at `PT-233`.** **`PT-182` found the chain carried three ideas: the first is the class; the other two are competence in general and belong in the skill rules if anywhere.**

**⚠ The Treasure Hunter now has a one-tier feature and needs tiers 2 and 3 that scale *knowing why you failed* rather than adding new verbs.** **Open.**

**Replaced `Prior Study`, which was declared in advance and spent once per adventure** — **a resource, not a competence, and the class is a competence.**

| Tier | Level | Effect |
|---|---|---|
| **Read the Ruin** | **1** | **When you fail a knowledge, `Security` or `Awareness` check to understand, open or navigate something, you learn *why* it failed** |
| › **Second Look** | **4** | It also tells you **what would succeed** — a tool, a skill, or a piece of knowledge you lack |
| ›› **Nothing Is Sealed** | **8** | It tells you **whether anything would**, so the party knows to stop trying |

> **⚠ Tiers restored — `PT-240`.** **`PT-233` cut the old tiers 2 and 3 and left both of their ideas inside tier 1.**

**Tier 1 read: *"you learn why — one concrete fact about what would work. You may retry once that condition is met."*** **⚠ *One concrete fact about what would work* is tier 2. *You may retry* is the retry clause `PT-182` cut.**

**The cut removed the tiers and not the content.**

**And the replacements were written in `FINDINGS-49 §4`, forty-eight documents before `PT-233` called them missing.**

> **Each tier is more of *knowing why*, not a new verb — which is what `PT-182` asked for.**

**⚠ Tier 2 is `SKILL-RESOLUTION-01 §2`'s own sentence turned into a class ability.** **That section says the number that matters is *"auto-succeeds at"* because *"most skill use is not under pressure."*** **The Treasure Hunter is never not taking 10.**

**Not dominant: it does nothing in combat, and it cannot make an impossible check succeed — it tells you what would.**

**⚠ Tier 3 needs `SKILL-RESOLUTION-01 §7`'s knowledge-skill DC ladder, which is listed as unset.** **The class works at tiers 1 and 2 without it.**

---

### Single Combat — Duelist only. Authored.

**⚠ Adopted at `PT-134`/`FINDINGS-27` and never written here.**

**Wielding condition, on owner instruction: a single weapon of wield class 1, 2 or 4 and an empty off hand — `PT-169`.**

| Tier | Level | Effect |
|---|---|---|
| **Single Combat** | **1** | **Name one enemy as a free action. +1 attack and +1 Defence against it**, and **−1 Defence against everyone else** |
| › **Measured** | **4** | **+2 / +2**, and **−1 against everyone else** |
| ›› **Nothing Else Matters** | **8** | **+3 / +3**, and **−2 against everyone else** |

> **⚠ It gets sharply better against exactly one enemy and no better at all in a crowd.**

**And the cost is real and derived:** **a class-3 double-blade is barred, so the Duelist gives up the largest melee damage multiplier** — **and `ACTION-ECONOMY-01 §7.4`'s `1.5×` Strength needs a two-handed weapon, which is also barred.**


---


### Field Position — Agent only. Authored.

**⚠ Cover is a fully specified positional system and exactly one thing in the game references it — `Run to Ground`, which lets a Bounty Hunter *ignore* it.** **Nothing uses it.**

**Fifth class feature in a row that operates a rule the corpus already had.**

| Tier | Level | Effect |
|---|---|---|
| **Field Position** | **1** | **While you are in cover, your attacks gain `+2`** — the same bonus the cover gives your Defence |
| › **Shift** | **4** | **Once per round, move from one cover square to another within your speed as a free action.** Provokes nothing |
| ›› **Never In The Open** | **8** | **Once per encounter, when targeted by an attack you can see, move to any cover square within your speed before it resolves** |

**Cover as offence, then mobility, then escape. All three read `PT-3`'s existing rule and add no geometry.**

**⚠ The constraint is unusually hard: it does nothing in the open.** **Cover is terrain, so the class's whole feature is a property of the encounter rather than of the character.**

> **Which is the sharpest *would a player actually choose it* test in the set, and the answer is that they choose their position instead.**

**⚠ And it does not overlap the `Operative`.** **`No Firing Position` is concealment — nobody knows where the shot came from. This is terrain — they know exactly where you are and cannot reach you.**

**⚠ It also makes `PT-170`'s map-size dial matter a second time.** **A GM who builds bare rooms cuts this class the way they cut the Sharpshooter.**


---


### Combination — unarmed Velocity, `ATTACKS-07`. Authored.

**Gated on `Unarmed Specialist IV`, which in practice means the Brawler and the Force classes.**

| Tier | Level | Effect |
|---|---|---|
| **Combination** | **1** | **Strike twice unarmed.** The second gains `+2` if the first hit. **Attack −3, Defence −2** |
| › **Chain Punch** | **4** | **Three strikes**, each `+2` if the previous hit. **Attack −2, Defence −1** |
| ›› **Rain of Blows** | **8** | **Three strikes**, each `+2` if the previous hit, and **if all three hit the target is `Slowed`** until the end of its next turn |

**⚠ Deliberately not `Flurry` renamed.** **`Flurry` buys back accuracy across its tiers and keeps volume flat.** **This starts at two strikes and escalates *within the round* — a hit makes the next easier.**

> **Which is what a boxer does and what a swordsman does not.**

**⚠ It closes `PT-180`'s luck.** **`ATTACKS-07` had no Velocity chain, so `Nothing In My Hands` could not multiply. It can now, and the capstone is reworded rather than repriced to keep that from mattering.**


---


### Unrepeatable — Sith Battlemaster only. Authored.

**Owner-approved. Granted at class levels 1, 4 and 8.**

| Tier | | Effect |
|---|---|---|
| **Unrepeatable** | **1** | **If the attack you declare comes from a different chain than the one you declared last round, `+2` attack** |
| › **Unreadable** | **4** | **`+4`**, same condition |
| ›› **Unpredictable** | **8** | **`+4`**, and the target gains **no Defence bonus from any Defensive chain it has declared** against you |

> **He never attacks the same way twice, and you cannot get set for it.**

**⚠ Built on the one stat that is already his.** **The Battlemaster has the widest chain count in the game — 18, against the Weaponmaster's 15 and the Commando's 14.** **The feature rewards breadth directly.**

**⚠ It is conditional, which is the Jedi shape under `PT-129` rather than the Sith one.** **That is correct here: `PT-129` describes *base* classes, and the prestige tier already departs — `Regenerate Force Points` and both alignment chains are unconditional on Jedi prestige classes.**

**Priced against `Deflect`, which is a whole defensive system.** **⚠ It costs him nothing to satisfy — a class with 18 trees always has something else to declare.**


---


### ⚠ One `Sneak Attack` tree per character — `PT-191`

**Owner ruling.**

> **A character holds **one** `Sneak Attack` tree. Where two classes grant it, the higher governs and the lower is subsumed. Dice never sum.**

**⚠ Third quantity settled on the same principle as `PT-159`** — highest rate held, highest chain count held, highest `Sneak Attack` held. **A pattern rather than three exceptions.**

#### ⚠ *Higher* is measured at your level, not at the cap

**The three ladders differ in speed *and* cap, and the caps are not the test.**

    level 12      Smuggler 6d6      Watchman 4d6
    level 30      Smuggler 10d6     Watchman 7d6

**And a split character reads each ladder from its *own class level*, so the comparison shifts as you advance.**

> **⚠ A player's governing tree can change mid-career.** **When the newer tree overtakes the frozen one, the old is subsumed from then on.**

**That is the ruling working as intended — one tree, and which one resolves to whichever is higher when you check.** **⚠ It needs stating because *"the higher"* reads as a fixed answer and is not one.**


---


### ⚠ The stealth trees are open to every class — `PT-200`

**Owner ruling.** **`Sneak Attack` and `Stealthy Shot` may be taken by anyone who meets the `Stealth` requirement.**

> **`Killer's Instinct` is what makes them worth taking, and that is granted to four classes.**

**Priced, and it is why the openness costs nothing:**

    Barrage, 3 strikes, unconditional            27.3 a round
    Sneak Attack, 1 strike + 6d6                 23.8
    Sneak Attack + Killer's Instinct (+3d6)      31.1

**⚠ On its own the declaration loses to a Barrage.** **A class without the rider can buy the tree and will rarely declare it.**

**Which is the cleanest kind of class distinction: the mechanic is universal and the reason to use it is not.**

### ⚠ And two things the trees do NOT do

**They do not stun.** **The stun belongs to `Critical Strike` and `Precise Shot` — *"a first-attack hit stuns the target for one round unless it saves."***

**⚠ And *surprise* is not a bonus of the chain — it is the *condition* that lets it fire.** **`ACTION-ECONOMY-01 §19.5`: unaware means Hidden from, Stunned, or unable to see.**

> **You need surprise to use `Sneak Attack`. You do not get surprise from it.**


---


## 5c. What droids and organics share — `PT-210`

**Derived from `feat.2da`. Every granted feat, organic columns against droid columns:**

    organic-granted   84
    droid-granted     11
    BOTH               5   ⚠ and all five are proficiencies

**Shared in the source:** **Armour Light · Armour Medium · Weapon Blaster · Blaster Rifle · Melee Weapons.**

**Droid-only:** **Blaster Integration · Droid Interface · Droid Upgrade 1–3 · Logic Upgrade: Combat.**

> **⚠ The games share nothing but what you can hold and what you can wear.**

### That is too restrictive and `PT-75` already said so

**`PT-75` dropped the droid/organic class split: they draw from one class list.** **Keeping the feat split at five would undo it.**

**Shared, because nothing in them is biological:**

| | |
|---|---|
| **`Targeting`** | pointing a gun — a droid does this better than anyone |
| **`Boresight`** | the same, against deflection |
| **`Close Combat`** | a chassis caught at knife distance has the same problem. **⚠ Astromechs excepted, as stated** |
| **`Weapon Focus` · `Weapon Specialization`** | practice with a weapon family |

**⚠ NOT shared: `Squad Tactics`.** **Droids have their own — `Logic Upgrade`, above — and two of its three tiers were empty until now.**

**⚠ NOT shared: `Evasion` and `Uncanny Dodge`.** **Both are *keeps their footing when surprised*, and a repulsorlift frame has no footing.**

### The line, stated so a reader can apply it without a table

> **Share what is *training*. Withhold what is *instinct* or *anatomy*.**

**⚠ And where a droid should have the effect, give it its own chain rather than access to the organic one.** **`Logic Upgrade` is that done; `Droid Upgrade 1–3` is the same opportunity unused.**

---

### Hold the Line — Juggernaut only. Authored.

**⚠ Moved from the Soldier — `PT-211`.** **The KOTOR Soldier has eight grants — three armour, three weapon, `Power Attack` and its ranged twin — and no ally-protection mechanic of any kind.**

> **We invented it and gave it to the class the games made simplest.**

| Tier | Level | Effect |
|---|---|---|
| **Hold the Line** | **1** | **When an enemy in your reach attacks an ally other than you, you may take the hit instead.** Once per round, no action |
| › **Shield Wall** | **4** | **Twice per round**, and an ally adjacent to you **gains your armour bonus against ranged attacks** while they stay adjacent |
| ›› **None Get Past** | **8** | As above, and **once per encounter, when you take a hit for an ally you may immediately make one attack against the enemy that dealt it** |

**⚠ It pairs with `Immovable Object` rather than duplicating it.** **That chain is *you cannot get past me*; this is *and it costs you to try*.**

**Tier 2 is what makes the class a tank rather than a wall** — **standing next to a Juggernaut is safer than not, which no other class offers.**

#### ⚠ Why the absorb is per round and the counterattack is per encounter

**Absorbing is a *transfer*, not a gain. You spend your own vitality to save an ally's.**

    Juggernaut, d10, CON 16, level 10        ~85 vitality
    absorbing 2 hits a round for 5 rounds    ~120 damage — he dies

> **⚠ The hit points are already the cap.** **A frequency cap on top does nothing except stop it in the case where it was already stopping.**

**The tier-3 counterattack *is* a gain, so it carries a per-encounter cap.**

> **Cap the thing that gives you something. Do not cap the thing that costs you something.**

---

### Both Hands — Soldier only. Authored.

**⚠ Replaces `Hold the Line`, which was never written as a chain and has moved. `PT-211`.**

**Derived from the one thing the source gives this class and no other:** **POWER_ATTACK *and* POWER_BLAST — the `Charged Shot` ladder — both granted at 1st.**

> **The only class in either game given weight in both hands.**

| Tier | Level | Effect |
|---|---|---|
| **Both Hands** | **1** | **Your Power-axis chains do not distinguish melee from ranged.** A tier bought in one applies at the same tier in the other |
| › **Improvised** | **4** | **Switching between a melee and a ranged weapon is free once per round**, and provokes nothing |
| ›› **No Wrong Weapon** | **8** | As above, and **you take no penalty for firing a ranged weapon while adjacent** — `ACTION-ECONOMY-01 §6.2a`'s `−4` does not apply to you |

**⚠ Tier 3 is the one that makes the class:** **the `−4` for firing while adjacent is the point-blank rule, and the Soldier is the one character it never touches.**

**Not dominant: it grants no attack, no damage and no defence.** **It removes the reasons to have chosen wrong.**


---


### Two Fronts — Tech Specialist only. Authored.

**⚠ The class had no feature at all, on a faithfulness argument that does not survive.** **`PT-174` justified it as *"the only class in either game with no granted class feature — a way for it to be something without inventing a chain the source never gave it."***

> **⚠ The source's Tech Specialist was widely considered the worst class in the game.** **Faithfulness to a class that did not work is the `Logic Upgrade` mistake — `PT-210` — in the same file, two chains apart.**

**Owner's vision:** ***"What a Machinist or Engineer picks to fill the other's gap without going into that class — and to deal with both sides at once rather than splitting their time."***

**The skill list already does the first half.** **This is the second. `PT-212`.**

| Tier | Level | Effect |
|---|---|---|
| **Two Fronts** | **1** | **Use `Jury Rig` on an allied droid and `Field Override` on an enemy droid in the same round** — one is a Gear action, the other your declaration |
| › **Nothing Is Scrap** | **4** | **Your `Field Override` target counts as an allied droid for `Jury Rig` while you hold it.** You can repair what you stole |
| ›› **Salvage And Command** | **8** | **Once per encounter, repair and seize in one action** — an enemy droid at or below half vitality is restored to half and turned |

**⚠ Not a bundle.** **Holding both features is what multiclassing already buys.**

> **The point is not having both tools. It is using them on the same object, which neither parent can do and neither could reach by multiclassing.**

**⚠ It requires holding both parents' features, which the entry already guarantees** — **`Engineer 6` or `Machinist 6`, plus the skill list of whichever you are missing.**

**Not dominant: it does nothing in a fight without droids on both sides.** **⚠ Third feature keyed to droids, after `Field Override` and `Jury Rig` — `PT-100`'s narrow-counter pattern reaching a third class.**


---


### Vigil — Jedi Watchman only. Authored.

**⚠ The Watchman was the one class `PT-193` left with nothing. `PT-219`.**

**Grepped: its entire record was a rate, a feat total, a cadence and one granted chain — *`Sneak Attack` 1d6–7d6*.** **That grant was its only distinguishing content, and `PT-193` deleted the ladder it was written in.**

**And it was never *stripped*. `feat.2da`, distinctive grants with proficiencies and the universal Force package removed:**

    jwa   (nothing)
    sma   Ignore Pain I–III · Increase Combat Damage I–III
    jsn   Force Immunity: Fear · Stun · Paralysis

> **⚠ Zero. Its entire distinctive content in KOTOR 2 *was* `Sneak Attack`, and when that became an attack tree anyone could buy, the class became an empty column.**

| Tier | Level | Effect |
|---|---|---|
| **Vigil** | **1** | **You may `Scan` as a free action once per round**, and you use the better of `Awareness` or `Alertness` for it |
| › **Unhidden** | **4** | **Anything you find with a `Scan` is found by your whole party** until the end of your next turn |
| ›› **Standing Watch** | **8** | **An enemy Hidden from you when combat begins is not**, and **you may not be made unaware by anything short of losing consciousness** |

**⚠ The capstone is the class's own parent chain finished.** **`Force Immunity` runs Fear → Stun → Paralysis, and two of those three are ways to be made *unaware* under `ACTION-ECONOMY-01 §19.5`.**

> **The Sentinel becomes immune to the conditions. The Watchman becomes immune to their consequence.**

**⚠ Named `Vigil` by the owner, checked against check 21 before proposing — clear in all seven documents, where `The Watch` collided in four.**


---


### Rally — Officer only. `PT-221`, renamed by `PT-224`.

**⚠ The repair for `PT-215`.** **`Inspire Followers I–V` were five ported Force powers gated on `Jedi Master`, which `PT-215` cut.**

**They are now an Officer class feature and no longer Force powers at all.**

| Tier | Level | Effect |
|---|---|---|
| **Rally** | **1** | **Spend your declaration.** Every ally who can hear you gains **`+1` attack, `+1` damage and `+1` Will** |
| › **On My Mark** | **4** | **`+2`**, and **one ally may immediately make one attack** |
| ›› **Command Presence** | **8** | **`+3`**, and the immediate attack applies to **two** allies |

> **It lasts while you are conscious and able to speak. It ends the moment you are not.**

**⚠ No Force power can cancel it.** **`Force Suppression` and `Force Breach` strip *Force* effects, and an order is not one.** **Both have lost their `Inspire Followers` clause.**

#### ⚠ Why that counter is better than a dispel

    a dispel      costs an enemy caster one power, at range, from safety
    an order      costs the enemy an attack that must reach and drop the Officer

**The counter exists, it is expensive, and it is physical.**

#### ⚠ And it costs the declaration, which is what prices it

**An Officer who gives the order does not attack that round.** **`ATTACKS-01 §2` — one declaration — is doing the balancing, exactly as it does for `Field Override` and `Cover Identity`.**

**⚠ Named `Rally` by the owner — `PT-224`.** **Checked against check 21 first: `Command`, `Orders`, `Authority`, `Bearing`, `Cadence` and `Signal` all already appear in the corpus. `Rally` is free.**

**⚠ *"Not droids"* does NOT survive. `PT-222`.**

**`REPLY-59` said it did. The designer's `PT-210` warrant settles it the other way:**

> **Share what is *training*. Withhold what is *instinct* or *anatomy*.** **An order is training. A droid follows orders better than anyone.**

**⚠ The source clause is a *Force-morale* artefact.** **`Inspire Followers` was a Light-side power raising **morale**, and a droid has none.** **An Officer's version is not morale; it is instruction.**

**⚠ And the consequence I named was the argument against my own reading: a Droid Master fielding four henchmen was five turns.** **⚠ `PT-571` made them COMPANIONS — five bodies, ONE turn, and each acting from a menu of three.**

**And it is the only leadership mechanic in the roster** — **`Squad Tactics` and `Logic Upgrade: Tactician` are *fight better beside someone*, which is not leading.**


---


### Field Surgery — Medic only. Authored.

**⚠ Adopted with the class and never written here — `PT-233`.** **Third instance of the `Quickdraw` shape, after `Combination` and `Read the Ruin`'s uncut tiers.**

**`SKILL-RESOLUTION-01` gives `Medicine` a medpac mode restoring vitality to someone still standing.** **⚠ NOTHING IN THE GAME TOUCHES A CHARACTER WHO HAS GONE PAST 0 — `PT-559`. That is the Medic's.**

| Tier | Level | Effect |
|---|---|---|
| **Field Surgery** | **1** | **A Gear action.** Spend a medpac to restore **`1d8` vitality** to an adjacent character ⚠ **at or below 0**. They stop dying |
| › **Stabilise** | **4** | **`2d8`**, ⚠ **the character is no longer `dying`**, and it is no longer `Disabled` |
| ›› **Back Up** | **8** | **`3` wounds**, and **once per encounter you may do this at range 4 metres** without touching them |

> **⚠ YOU CAN BRING BACK SOMEONE WHO IS ALREADY DYING, WHICH NOTHING ELSE IN THE GAME CAN — `PT-559`.**

**⚠ Priced against `DEATH-AND-DIFFICULTY-01`.** **On `Easy` a downed character recovers anyway and this is convenience. On `Hard` it is the difference between a character and a memory.**

**⚠ Which makes it the one class feature whose value is set by the campaign mode rather than by the table** — **worth stating, and it is the right kind of dependency.**

**A Gear action, so it costs no declaration — the same price `Jury Rig` pays.**


---


### Dark Rage — Force-sensitive. ⚠ Ported, `PT-474`.

**Requires Strength 12, Force-sensitive, Character Level 9.**

**All damage-dealing Force powers add your Strength modifier to their damage.**

> **⚠ THIS INVERTS THE FORCE STAT MODEL AND THAT IS THE POINT.** **Every Force save DC in the corpus runs on Wisdom and Charisma. A Consular has neither reason nor room for Strength.** **`Dark Rage` makes a Strength build cast harder without casting more ACCURATELY — the DC is untouched.**

**⚠ Recorded as a deliberate class-distinction change.** **A Sith Marauder with `Force Lightning` now out-damages a Consular with the same power, and the Consular still lands it more often.** **If that is wrong the feat is the thing to cut, not the DCs.**

---

### Sadism → Sated — Force-sensitive. ⚠ Ported, `PT-474`.

| Tier | Level | Effect |
|---|---|---|
| **Sadism** | **9** | **Damaging Force powers deal `+50%` against a target that is `stunned`, `paralysed`, `shaken`, `panicked` or `cowering`.** |
| › **Sated** | **12** | As above, and **reducing such a target to 0 restores `1d8` vitality to you.** |

**⚠ Renamed from `Sweet Release` — the source name does not belong in this game.**

**⚠ The alignment scaling is KEPT: *half as effective for a light-side aligned character*.**

**Nothing in the corpus rewarded setting a target up and then hitting it.** **`Force Stun` → strike was a sequence with no mechanical payoff.**

**⚠ The condition list is OURS.** **The source says *"Stun, Paralysis or Fear"*; `PT-447` split fear into three conditions and `PT-445` cut `frightened`, so the list is restated against the real condition set.**

---

### Constancy → Respite — Force-sensitive. ⚠ Ported, `PT-474`.

| Tier | Level | Effect |
|---|---|---|
| **Constancy** | **9** | **Beneficial Force powers you cast on a friendly target last `50%` longer.** |
| › **Respite** | **12** | As above, and **each such power also restores `1d8` vitality to its target.** |

**⚠ The alignment scaling is KEPT and INVERTED against `Sadism`: half as effective for a DARK-side character.**

> **⚠ TOGETHER THESE TWO ARE A MECHANIC WE DID NOT HAVE.** **`ALIGNMENT-01` scales the COST of a power by alignment band — 0.50x to 1.75x. Nothing scaled an EFFECT.** **`Sadism` and `Constancy` are the first, and they are mirrored: cruelty works for the dark, patience for the light.**

**⚠ *"Half as effective"* needs a rule where a doubling does not divide cleanly.** **Ruled: halve the numeric result and round down; a `+50%` becomes `+25%`, a `1d8` becomes `1d4`.**

---

### Anti-Shield Protocol — Assassin and Battle chassis. ⚠ Retargeted, `PT-474`/`PT-475`.

**Requires Character Level 8 and a disruptor-type weapon.**

**A successful hit with a disruptor SUPPRESSES every `DamageImmunity` effect on the target for 4 rounds and prevents reactivation for that time.**

**⚠ The source's prerequisite is literally `HK-47` — a named character.** **Retargeted to the two COMBAT chassis: `Assassin` and `Battle` — `DROID-SKILLS-01 §2.3`.** **HK-47 is the Assassin chassis' own exemplar.**

**⚠ And the mechanic ports cleanly because shields in this corpus ARE percentage damage immunity:** **`Energy Shielding Mark I–IV` at 10/15/20/30%, `Thermal Shield Generator` at 75% Fire, `Multishield Generator` at 50% Electrical.**

---

### Auto-Shield Protocol — Astromech and Remote chassis. ⚠ Retargeted, `PT-474`/`PT-475`.

**Requires Character Level 8 and an equipped shield generator.**

**When you fall below half vitality, your equipped shield generator activates automatically. This costs no action and does not consume your turn.**

**⚠ The source's prerequisite is `Expert Droid` — a KOTOR 2 class name. `PT-76` renamed it `Engineer`.**

**⚠ Retargeted again at `PT-475` to the two SUPPORT chassis: `Astromech` and `Remote`.** **The split mirrors `Anti-Shield Protocol`: the combat chassis STRIP shields, the support chassis RAISE them.** **`DROID-SKILLS-01 §2.3` already draws the same line — the support chassis get `Treat Injury`, the combat chassis keep the exclusion.**

---

### Shield Boost — ⚠ ANY droid chassis. Authored, `PT-475`/`PT-476`.

| Tier | Level | Effect |
|---|---|---|
| **Shield Boost** | **1** | **A shield generator you equip absorbs `10` more points of damage before it fails.** |
| › **Reinforced Emitters** | **4** | **`20` more points**, and the generator may be reactivated once per encounter without an action. |
| ›› **Overcharge** | **8** | **`30` more points**, and while a shield is active you take **no damage from the first attack each round** that the shield would have absorbed. |

**⚠ ANY droid, any chassis — owner ruling, `PT-476`.** **Unlike the two Protocol feats, this is not a role: every droid carries a power supply and every droid can reinforce a shield.** **`DROID-SKILLS-01 §2.1` already has a nine-skill universal set; this is the same shape.**

**⚠ FLAT POINTS, NOT PERCENTAGES — deliberately.** **The source reads `+20% / +40% / +60%`.**

> **⚠ See `AGENDA-CURRENT`'s percentage-mechanics item.** **Percentages are everywhere in `ITEMS-03` and `ITEMS-05` and they are the wrong shape for a table.** **This feat is written the way the replacement should look.**

---

### Last Stand — ⚠ Ported and retranslated, `PT-477`.

**No prerequisite.**

| Tier | Level | Effect |
|---|---|---|
| **Last Stand** | **1** | **While you are the last conscious member of your party, you regain **`1d4` + your Constitution modifier** vitality at the start of each of your turns.** |
| › **Improved Last Stand** | **4** | **`2d4` + Constitution modifier**, and **you gain `+4` on saves against `fear effects` — you are past being afraid.** |
| ›› **Master Last Stand** | **8** | **`3d4` + Constitution modifier**, and **you cannot be reduced below 1 vitality by a single attack** while the condition holds. |

**⚠ *Party* means every allied character under player or GM control — players, companions, a Beast Master's beast, a Droid Master's droids.** **You are the last when every one of them is at 0 vitality or below, or otherwise out of the fight.**

**⚠ The source reads *"while both of your COMPANIONS are incapacitated"* and *"5% of maximum VP every round."*** **Both are KOTOR's three-slot party hard-coded into a feat.** **Rewritten to scale to any party size, and to flat dice — `PT-475`'s percentage ruling.**

> **⚠ It is strongest in a small party and weakest in a large one, which is the inverse of most feats.** **Deliberate: a solo survivor is the point.** **Recorded so it is not read as a scaling error.**

**⚠ The dice were `1d8` / `2d8` / `3d8` in the first draft — lowered at `PT-478`, then set to `1d4` / `2d4` / `3d4` + Constitution at `PT-479`.** **Nothing else in the corpus regenerates near the original: the beast `Regeneration 2` is `2` flat and `Regenerate Vitality Points` is half a point every six seconds.**

**⚠ COUNT-SCALING, and it is the owner's ruling.** **`PT-456` ruled that POISON ladders grow the die; `ATTACKS-05`'s player chains grow the count at `1d6`/`2d6`/`3d6`. This follows the CHAIN convention, which is what it is — a three-tier feat chain, not a poison.**

**⚠ The Constitution modifier is what makes it a SURVIVOR'S feat rather than a generic one.** **It scales with the stat that already governs vitality, so a tough character holds out longer and a fragile one gains little — and a low-Constitution character may regain nothing at all.**

**⚠ `Master Last Stand`'s floor is NOT immunity.** **Repeated attacks still kill you; one attack cannot.**

---

### Payday — Pirate only. ⚠ Ported from the mod block, `PT-474`.

| Tier | Level | Effect |
|---|---|---|
| **Payday** | **1** | **Every enemy you reduce to 0 or below leaves credits.** Roll `1d10 × the enemy's level` in credits, taken as a free action when you drop it. |
| › **Good Hunting** | **4** | **`2d10 ×` level**, and **you may claim credits from an enemy an ally dropped**, if you are adjacent to it. |
| ›› **Clean Sweep** | **8** | **`3d10 ×` level**, and **credits are claimed automatically from every enemy that falls within 4 metres of you** — no action, no adjacency. |

**⚠ The source is a party-slot economy feat — *"while a character with this feat is in your active party you can claim an amount of credits for every kill."*** **Rewritten as a per-body drop, which is what the owner asked for and what a table can actually run.**

**⚠ It pairs with `Plunder` rather than duplicating it: `Plunder` takes an ITEM, `Payday` takes CREDITS.** **A Pirate with both strips a corpse completely.**

---

### Momentum — Authored from the mod block, `PT-474`.

| Tier | Level | Effect |
|---|---|---|
| **Momentum** | **1** | **When you reduce an enemy to 0 or below, `+1` to attack rolls for 10 rounds.** ⚠ Stacks with itself, to a maximum of `+1`. |
| › **Gathering Pace** | **4** | **`+2` per kill, maximum `+2`.** |
| ›› **Killing Pace** | **8** | **`+3` per kill, maximum `+3`.** |

**⚠ Renamed from the source's *Killer Instinct* — owner ruling. The old name is deliberately NOT a definition.**

**⚠ THE CAP IS OURS AND IT IS THE WHOLE FIX.** **The source stacks without limit — *"this bonus stacks with itself in the case of multiple kills"* — so a room of weak enemies hands you an unbounded attack bonus.** **Capped at the tier value, the feat rewards finishing without rewarding farming.**

**Nothing else in the corpus rewards reducing a target to 0.** *`Plunder` and `Payday` trigger on it; neither improves your attacks.*

---

### Plunder — Pirate only. Authored.

| Tier | Level | Effect |
|---|---|---|
| **Plunder** | **1** | **When you reduce an enemy to 0 or below, take one carried item as a free action** — a weapon, medpac, grenade, spike or mine. **It is immediately usable** |
| › **Quick Hands** | **4** | **Also on a critical hit, without dropping them** |
| ›› **Everything Is Cargo** | **8** | As above, and **once per encounter the item you took costs no Gear action to use** |

**⚠ Requires dropping someone first, which is why it unlocks at class level 1 — `PT-239`.**

---

### Unrelenting — Sith Warrior only. Authored.

| Tier | Level | Effect |
|---|---|---|
| **Unrelenting** | **1** | **While your vitality is below half, `+2` damage on every attack you make.** No declaration, no action, no limit per encounter |
| › **Past Caring** | **4** | **`+4` below half** |
| ›› **Last Stand** | **8** | **`+6` below half**, and **`+2` attack while below a quarter** |

**⚠ It multiplies — `PT-180`.** **`+6` on a three-strike `Barrage` is `+18`, which took the realised increase from a reported `+22%` to `+46%`.**

**`PT-183` kept the numbers.** **The `+46%` is a peak rather than an average — it fires only below half, so a realised fight is nearer `+20%`.**

> **⚠ The thing to watch is the incentive, not the damage.** **A capstone that pays for being hurt rewards a player for not disengaging, and `DEATH-AND-DIFFICULTY-01` governs what happens when that goes wrong.**

---

### Vanish — Sith Assassin only. Authored.

| Tier | Level | Effect |
|---|---|---|
| **Vanish** | **1** | **Once per encounter, immediately after an attack of yours deals `Sneak Attack` damage, make a `Stealth` check as a free action** against the better of each enemy's `Awareness` or `Alertness` |
| › **Displaced** | **4** | **Twice per encounter** |
| ›› **Absent** | **8** | Twice, and **you may move up to half your speed as part of it**, before the check resolves |

**⚠ It is conditional, which is the Jedi shape under `PT-129` rather than the Sith one.** **`PT-131` records that as a departure caused by `PT-126` — the owner ruled the Assassin off the mirror onto `Specialist`, which made it the one Sith built around a tool rather than a number.**

**⚠ And `PT-193` narrowed it.** **`Sneak Attack` is now an attack chain anyone may buy, capped at `6d6`, so the trigger still fires but the distinction it rested on is gone.**

---

### Dominion — Sith Inquisitor only. Authored.

| Tier | Level | Effect |
|---|---|---|
| **Dominion** | **1** | **`+1` to the saving throw DC of every Force power you cast** |
| › **Advanced Dominion** | **4** | **`+2`** |
| ›› **Master Dominion** | **8** | **`+3`** |

**⚠ `PT-182` flagged the capstone: converting a failure into a partial success is a different mechanic, borrowed from an existing stun clause.** **`REPLY-45` ruled it cut and the cut was never applied.**

**⚠ Applied here — `PT-242`.** **Tier 3 is `+3` and nothing else. *Harder to resist* is already the class.**


---



---

# ⚠ How a feat reaches a character — `PT-353`

**Three routes. They are not interchangeable and the difference is load-bearing.**

| | How | Lasts | ⚠ Counts as yours? |
|---|---|---|---|
| **Purchased** | you spent a feat slot | permanently | **yes** |
| **Class grant** | a class feature gave it | while you hold that class | **yes** |
| **⚠ Item** | an item grants it | ⚠ **only while equipped** | **NO** |
| **⚠ Droid bay** | installed in a bay | ⚠ **permanently, cannot be removed** | **yes** |

---

## ⚠ The hard rule

> **⚠ A feat held from an ITEM is a property of the ITEM, not of the character.**

**It cannot satisfy a prerequisite. Not for a prestige class, not for a higher tier of its own chain, not for anything.**

**⚠ Because a prerequisite is a statement about what you have LEARNED.** **An item you can take off has taught you nothing.**

### What follows

**⚠ It does not consume chain access.** **`PT-173`'s `N ≤ access` test counts what you bought. An item cannot make a legal build illegal — `PT-315`.**

**⚠ It does not stack with the same feat held permanently.** **If you already have it, the grant does nothing and takes nothing away.**

**⚠ It does not survive unequipping.** **Including mid-combat.**

---

## ⚠ A droid bay is the exception, and deliberately

**`PT-318` installs a feat into a bay permanently, and `PT-321` says why:**

> ***"The permanent are as if you levelled up and got it to that level."***

**⚠ So a bay-installed feat IS yours.** **It satisfies prerequisites, it counts, and it cannot be removed.**

**Which is exactly what distinguishes a bay from a socket** — **`PT-350`.**

---

## ⚠ Why this needed writing down

**`PT-351` established item-granted feats are temporary. `PT-318` established bay feats are permanent.**

**⚠ Both were true and neither said what that MEANT for prerequisites**, **which is where the two would first collide at a table.**
