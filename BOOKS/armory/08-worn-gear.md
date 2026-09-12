# Chapter Eight — Worn Gear

**Everything a character wears that is neither armour nor a weapon** — belts, forearm
mounts, gauntlets, implants and masks. **The largest category in the book after weapons**,
and mechanically its own thing: passive gear occupying a body slot.

**These figures came straight from the games' own item files**, on the same footing as
Chapters Five through Seven.

---

## The five categories

**248 items**, none appearing in both games — every entry here is specific to one game or
the other, or original to this project.

| Category | Count | Slot |
|---|---|---|
| **Belt** | 47 | Waist |
| **Forearm** | 33 | Forearm — mostly timed absorption shields, the same shape as the droid shields in Chapter Seven |
| **Gauntlets** | 42 | Hands |
| **Implant** | 67 | Internal — the largest single category here |
| **Mask** | 59 | Head |

**That is a genuinely split chapter:** **143 items from KOTOR 2, 98 from KOTOR 1, and seven
written for this book.** Nothing here appears in both games, which is why the
price-reconciliation rule that governs Chapter Five's armour never has to fire here.

## ⚠ Seven items in this chapter do not exist in either game

| Item | Category | Cost | Effect |
|---|---|---|---|
| **Sparring Gloves** | Gauntlets | 90 | `Damage (Bludgeoning) 1` |
| **Echani Sparring Gloves** | Gauntlets | 950 | `Damage (Bludgeoning) 2` · `AttackBonus 1` |
| **Clarity Package** | Implant | 1,000 | `Ability (Wisdom) 1` |
| **Motor Package** | Implant | 1,000 | `Ability (Strength) 1` |
| **Presence Package** | Implant | 1,000 | `Ability (Charisma) 1` |
| **Fortitude Package** | Implant | 50 | A saving-throw bonus, gated behind `Constitution 12` |
| **Will Package** | Implant | 50 | A saving-throw bonus, gated behind `Constitution 12` |

**The gauntlet pair fills a slot that otherwise mostly carries skill bonuses** — an
unarmed-adjacent option where the games offered none. **The five implants complete an
obvious ladder**: one package for each of three ability scores at a matched price, and two
cheap saving-throw packages with an attribute prerequisite.

**Every such item in this book is marked**, and that is deliberate: **an invented item
should never sit beside an extracted one as though the two came from the same place.**
Where you see the authored mark, the item is this game's own work rather than BioWare's or
Obsidian's.

## Representative entries

| Name | Category | Provenance | Cost | Effect |
|---|---|---|---|---|
| **Safety Harness** | Belt | K2 | 100 | Skill bonus, skill unresolved — see below |
| **Peragus Mining Shield** | Forearm | K2 | 100 | Absorbs 20 heat, 200-second duration or until exhausted — a Peragus-specific item, tied to that world's mining hazards rather than general combat |
| **Sparring Gloves** | Gauntlets | ⚠ authored | 90 | `Damage (Bludgeoning) 1` |
| **Clarity Package** | Implant | ⚠ authored | 1,000 | `Ability (Wisdom) 1` |
| **Survey Gear** | Mask | K2 | 60 | Sonic resistance plus a skill bonus, **restricted from Wookiees** — the same worn-gear-restriction shape Chapter One already established for organic armour |

## ⚠ Some skill bonuses do not say which skill

**A number of items in this category grant a skill bonus whose target is unreadable in the
game data.** The entry records that a skill is improved and by how much, **but the code
identifying *which* skill does not resolve to a name.**

**It is a known problem with a known cause**, and it is being worked on separately — the
same broken reference that leaves items in Chapters Five, Six and Seven with a bonus and no
label.

**Until it is resolved, treat such an item as granting a bonus a Gamemaster assigns** to
whichever skill the item's description and slot most plausibly support. **`Safety Harness`
in the table above is the clearest example.**

## ⚠ And four rows have a corrupted name

**Four entries below carry a name lifted from somewhere else in the game's string table** —
*"Deflect"*, *"Inner Strength I"*, *"Inner Strength III"* and *"Craft Description"*, none of
which has anything to do with a gauntlet, an implant or a mask. **The items themselves are
real and their properties are their own.**

**They are catalogued by resref and marked. No name has been invented for any of them**, and
they are the same family of damage found in the armour, upgrade and droid chapters.

**⚠ Five more were on that list and are now named.** `g1_i_belt001` is the **Baragwin Stealth
Unit**, `g1_i_implant303` the **Advanced Combat Implant**, `g1_i_implant304` the **Advanced
Alacrity Impant** *(the misspelling is the game's own)*, `g1_i_mask02` the **Medical Interface
Visor**, and `g1_i_mask03` the **Advanced Agent Interface**. **Their names were always
recoverable** and had simply been read against the wrong game's string table. **All five are
catalogued below under their real names.**

---

# The catalogue

**All 248 items, by category**, with resref, which game each comes from, tier, price,
properties and the item's own description.

---

## Belt — 47

**Safety Harness** · `100_belt01` · K2 · Tier 1 · 100 credits · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 1)* — *“This Peragus mining safety harness is designed to aid a miner in setting and removing demolition charges within asteroid mining claims.”*

**Adrenaline Amplifier** · `a_belt_01` · K2 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 2)* — *“This device improves the wearer's reflexes by triggering prolonged bursts of adrenaline. It is thought to be perfectly safe, with only a few instances of uncontrolled muscle spasms.”*

**Cardio-Regulator** · `a_belt_02` · K2 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 1)* — *“This belt monitors heartbeat and breathing and releases chemicals into the body should either of these become irregular. This gives the wearer a higher fortitude than most.”*

**Stealth Field Generator** · `a_belt_03` · K2 · Tier 1 · 100 credits — *“This device enables Stealth Mode, a camouflage field that hides the user. Opponents must make an Awareness check versus the Stealth skill of the user or remain unaware of them. The user must have paid points into the Stealth skill to use Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Czerka Utility Belt** · `a_belt_04` · K2 · Tier 1 · 100 credits · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 7)* — *“This utility belt comes with a variety of tools to assist the wearer with many tasks. It was originally developed by Czerka corporation for their own maintenance staff and quickly found use throughout the Republic. The user must have paid points into the Demolitions and Security skills to gain the respective benefits from this belt.”*

**Advanced Adrenaline Amplifier** · `a_belt_05` · K2 · Tier 1 · 200 credits · Saving throw +3 ⚠ *(which save is unresolved — subtype 2)* — *“This device is an improved version of the basic model, increasing effectiveness with fewer occurrences of side effects. It improves reflexes by triggering prolonged bursts of adrenaline.”*

**Aratech SD Belt** · `a_belt_06` · K2 · Tier 1 · 300 credits · DamageImmunity (Sonic) ⚠ **DR 5** *(25%)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 2)* — *“This Aratech Sound Dampening Belt reduces all sound that the user might make. Opponents must make an Awareness check versus user Stealth skill +2 or remain unaware of them. The belt additionally helps shield the user from sonic attacks. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Strength Enhancer** · `a_belt_07` · K2 · Tier 1 · 500 credits · Ability (Strength) 1 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* — *“This belt injects a steady but slow stream of stimulants into the wearer's bloodstream.”*

**Systech Cardio-Regulator** · `a_belt_08` · K2 · Tier 2 · 700 credits · Ability (Constitution) 1 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* — *“Systech improved upon the standard Cardio-Regulator design by including an intelligent computer system that customizes its parameters based upon its wearer.”*

**Hyper Adrenaline Amplifier** · `a_belt_09` · K2 · Tier 2 · 900 credits · Ability (Dexterity) 1 · Saving throw +3 ⚠ *(which save is unresolved — subtype 2)* — *“This ingenuously designed belt monitors adrenaline in the wearers' blood stream. When elevated, the device injects a massive dose of additional adrenaline, greatly enhancing reaction time.”*

**Exchange Shadow Caster** · `a_belt_10` · K2 · Tier 2 · 1,100 credits · Ability (Dexterity) 1 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* — *“This unit was developed by the Exchange as an escape tool for their members on worlds where the authorities outnumber the Exchange population. It refines the Stealth Mode field to better camouflage the user. Opponents must make an Awareness check versus user Stealth skill +4 or remain unaware of them. The user must have paid points into the Stealth skill to use Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Inertial Inhibitor** · `a_belt_11` · K2 · Tier 2 · 1,300 credits · Ability (Dexterity) 1 · Armor 1 — *“This belt's advanced technology suggests an Arkanian design. It eases the wearer's movement, improving reaction time in combat.”*

**Electrical Capacitance Shield** · `a_belt_12` · K2 · Tier 2 · 8,500 credits · DamageImmunity (Electrical) ⚠ **DR 15** *(75%)* — *“This shielding device, worn around the waist, absorbs and stores electrical energy directed at the user, which is then released slowly over a period of time, dissipating harmlessly. The manner of release generates vibrations along the inside edge of the shield, giving it the less than complimentary nickname, 'The Tingler'.”*

**Thermal Shield Generator** · `a_belt_13` · K2 · Tier 2 · 8,000 credits · DamageImmunity (Fire) ⚠ **DR 15** *(75%)* — *“This generator forms a magnetic shield around the wearer which, while ineffective against most modern weaponry, does allow for the ablation of directed heat attacks, generally in the form of fire.”*

**Eriadu Stealth Unit** · `a_belt_14` · K2 · Tier 2 · 1,250 credits · Ability (Dexterity) 2 · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 2)* — *“This sophisticated Eriadu Stealth Mode unit expertly camouflages the user. Opponents must make an Awareness check versus user Stealth skill +6 or remain unaware of them. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**CNS Strength Enhancer** · `a_belt_15` · K2 · Tier 2 · 8,500 credits · Ability (Strength) 2 · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* — *“An experimental system that amplifies power signals along the length of the central nervous system, this generator, attached to a belt, provides greater impulses to all muscles, as well as a resistance to all sorts of perturbations of the user's system.”*

**Exchange Utility Belt** · `a_belt_16` · K2 · Tier 2 · 4,700 credits · Ability (Dexterity) 1 · Ability (Strength) 1 · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 6)* — *“Ostensibly used by mechanics, this belt's variety of equipment can aid in many more nefarious tasks as well. The user must have paid points into the Demolitions and Security skills to gain the respective benefits from this belt.”*

**Immunity Belt** · `a_belt_17` · K2 · Tier 3 · 6,100 credits · AttackPenalty Penalty_-1 · Ability (Constitution) 1 · DamageResist (Bludgeoning) Resist_5/- · DamageResist (Energy) Resist_5/- · DamageResist (Piercing) Resist_5/- · DamageResist (Slashing) Resist_5/- — *“This awkward and thick belt protects the wearer from attacks, but hinders movement slightly. It is most often utilized by experienced combatants who are not meaningfully hindered by the belt's clumsiness.”*

**Adrenaline Stimulator** · `a_belt_18` · K2 · Tier 3 · 12,000 credits · Ability (Dexterity) 2 · Saving throw +4 ⚠ *(which save is unresolved — subtype 0)* — *“This belt endows the wearer with hyper-sensitivity to their surroundings and dynamically improves reflexes and reaction time.”*

**Nerve Amplifier Belt** · `a_belt_19` · K2 · Tier 3 · 1,000 credits · Ability (Wisdom) 1 · Immunity (MindSpells) 0 — *“This belt monitors the brain, emitting energy waves to reinforce established patterns and block any outside influence. It's extremely effective, if mildly uncomfortable.”*

**Jal Shey Belt** · `a_belt_20` · K2 · Tier 3 · 11,000 credits · Ability (Wisdom) 1 · ImprovedMagicResist Bonus_14 — *“This belt is an improvement upon the earlier efforts by the Jal Shey to protect their minds from the Dark Side. The Jal Shey concentrate on intellectual study of the Force, seeking to understand it at a mental level, rather than a spiritual one. Jal Shey are typically exceptional diplomats, but are less successful in physical pursuits.”*

**Multishield Generator** · `a_belt_21` · K2 · Tier 3 · 12,800 credits · DamageImmunity (Electrical) ⚠ **DR 10** *(50%)* · DamageImmunity (Fire) ⚠ **DR 10** *(50%)* · DamageImmunity (Ion) ⚠ **DR 3** *(15%)* — *“This belt combines the functions of the Electrical Capacitance Shield and the Thermal Shield Generator, providing versatile protection.”*

**Defel Mimicker** · `a_belt_22` · K2 · Tier 3 · 14,600 credits · Ability (Dexterity) 3 · Skill bonus +8 ⚠ *(which skill is unresolved — subtype 2)* — *“The Defel are a small bipedal species of mammals who hail from the planet Af'El. Because of the bizarre conditions on their homeworld, the Defel naturally appear as vague shadows. This device seeks to duplicate that effect. Opponents must make an Awareness check versus user Stealth skill +8 or remain unaware of them. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Frozian Scout Belt** · `a_belt_23` · K2 · Tier 3 · 16,400 credits · Ability (Dexterity) 3 · Armor 1 · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 2)* — *“The Frozian are a species of large, gangly mammalian bipeds from the lush paradise of Froz. They employ the belts to help compensate for their typical clumsiness. Opponents must make an Awareness check versus user Stealth skill +3 or remain unaware of them. The user must have paid points into the Stealth skill to use Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Tech Specialist Belt** · `a_belt_24` · K2 · Tier 3 · 18,200 credits · Ability (Dexterity) 2 · Ability (Strength) 1 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +5 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 7)* — *“This practical and unassuming belt is prized by both scoundrel-types and those desiring to create more potent upgrades. The user must have paid points into the Demolitions and Security skills to gain the respective benefits from this belt.”*

**Aratech Cardio-Regulator** · `a_belt_25` · K2 · Tier 3 · 20,000 credits · Ability (Constitution) 3 · Ability (Strength) 1 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* — *“With its improved performance and lack of negative side-effects, the Aratech Cardio-Regular is a favorite with more experienced mercenaries.”*

**GNS Strength Enhancer** · `a_belt_26` · K2 · Tier 4 · 21,800 credits · Ability (Strength) 4 — *“This generator is a high-powered version of the experimental CNS Strength Enhancer. It emphasizes the increase in muscle performance and lacks the protective capabilities of the earlier model.”*

**Qel-Droma Belt** · `a_belt_27` · K2 · Tier 4 · 23,600 credits · Ability (Charisma) 1 · Ability (Wisdom) 1 · DamageImmunity (Dark Side) ⚠ **DR 4** *(20%)* · DamageImmunity (Light Side) ⚠ **DR 4** *(20%)* — *“The Qel-Droma family has produced many powerful Force sensitives. Some, such as Cay Qel-Droma, have been shining examples of the strength of the Force. Others, like Cay's brother Ulic, have fallen prey to the temptations of the Dark Side.”*

**Immortality Belt** · `a_belt_28` · K2 · Tier 4 · 25,400 credits · AttackPenalty Penalty_-2 · Ability (Constitution) 1 · DamageResist (Bludgeoning) Resist_10/- · DamageResist (Energy) Resist_10/- · DamageResist (Piercing) Resist_10/- · DamageResist (Slashing) Resist_10/- — *“This device is an enhanced version of the Immunity Belt. Though not actually granting immortality, this belt provides impressive protection from many types of attacks.”*

**Aratech Echo Belt** · `a_belt_29` · K2 · Tier 4 · 27,200 credits · Ability (Dexterity) 4 · Skill bonus +10 ⚠ *(which skill is unresolved — subtype 2)* — *“The Echo Belt is a top-of-the-line stealth device used by the wealthiest and the deadliest. Opponents must make an Awareness check versus user Stealth skill +10 or remain unaware of them. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Jal Shey Mentor Belt** · `a_belt_30` · K2 · Tier 4 · 29,000 credits · Ability (Wisdom) 2 · ImprovedMagicResist Bonus_20 — *“This belt is an improvement upon the earlier efforts by the Jal Shey to protect their minds from the Dark Side. The Jal Shey concentrate on intellectual study of the Force, seeking to understand it at a mental level, rather than a spiritual one. Jal Shey are typically exceptional diplomats, but are less successful in physical pursuits.”*

**Baragwin Stealth Unit** · `g1_i_belt001` · K1 · Tier 3 · 10,000 credits · Ability (Dexterity) 3 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +10 ⚠ *(which skill is unresolved — subtype 2)* — *“Similar in concept to the Baragwin Shadow Armor, the Baragwin Stealth Unit is a quantum leap in advancement over standard stealth units. It provides much greater camouflage, as well as enhancing the mobility and situatio”* ⚠ *(description truncated in source)*

**Cardio-Regulator** · `g_i_belt001` · K1 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 1)* — *“This belt monitors heartbeat and breathing and releases chemicals into the body should either of these become irregular. This gives the wearer a higher fortitude than most.”*

**Verpine Cardio-Regulator** · `g_i_belt002` · K1 · Tier 1 · 200 credits · Saving throw +3 ⚠ *(which save is unresolved — subtype 1)* — *“This device regulates the body in distress with emergency fortitude support for the wearer. It functions so well that some wonder how many "bodies in distress" the Verpine tested.”*

**Adrenaline Amplifier** · `g_i_belt003` · K1 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 2)* — *“This device improves the wearer's reflexes by triggering prolonged bursts of adrenaline. It is thought to be perfectly safe, with only a few instances of uncontrolled muscle spasms.”*

**Advanced Adrenaline Amplifier** · `g_i_belt004` · K1 · Tier 1 · 200 credits · Saving throw +3 ⚠ *(which save is unresolved — subtype 2)* — *“This device is an improved version of the basic model, increasing effectiveness with fewer occurrences of side effects. It improves reflexes by triggering prolonged bursts of adrenaline.”*

**Nerve Amplifier Belt** · `g_i_belt005` · K1 · Tier 2 · 1,000 credits · Immunity (MindSpells) 0 — *“This belt monitors the brain, emitting energy waves to reinforce established patterns and block any outside influence. It's extremely effective, if mildly uncomfortable.”*

**Sound Dampening Stealth Unit** · `g_i_belt006` · K1 · Tier 1 · 200 credits · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 2)* — *“This Republic unit improves on the basic Stealth Mode field by dampening all sound that the user might make. Opponents must make an Awareness check versus user Stealth skill +2 or remain unaware of them. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Advanced Stealth Unit** · `g_i_belt007` · K1 · Tier 1 · 500 credits · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* — *“Costly to produce, this unit refines the Stealth Mode field to better camouflage the user. Opponents must make an Awareness check versus user Stealth skill +4 or remain unaware of them. The user must have paid points into the Stealth skill to use Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Eriadu Stealth Unit** · `g_i_belt008` · K1 · Tier 2 · 1,250 credits · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 2)* — *“This sophisticated Eriadu Stealth Mode unit expertly camouflages the user. Opponents must make an Awareness check versus user Stealth skill +6 or remain unaware of them. The user must have paid points into the Stealth skill to gain the use of Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Calrissian's Utility Belt** ⚠ **UNIQUE** · `g_i_belt009` · K1 · Tier 2 · 3,000 credits · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 6)* — *“Galduran Calrissian's name was something of a liability after he became infamous for running an unsanctioned smuggling ring within Hutt space. Eventually cornered, he had to pawn even his personal items to avoid being the last Calrissian. The user must have paid points into the Demolitions and Security skills to gain the respective benefits from this belt.”*

**Stealth Field Generator** · `g_i_belt010` · K1 · Tier 1 · 100 credits — *“This device enables Stealth Mode, a camouflage field that hides the user. Opponents must make an Awareness check versus the Stealth skill of the user or remain unaware of them. The user must have paid points into the Stealth skill to use Stealth Mode. Combat disrupts the field, but mundane tasks do not.”*

**Adrenaline Stimulator** · `g_i_belt011` · K1 · Tier 3 · 12,000 credits · Ability (Dexterity) 2 · Saving throw +4 ⚠ *(which save is unresolved — subtype 0)* — *“This belt endows the wearer with hyper-sensitivity to their surroundings and dynamically improves reflexes and reaction time.”*

**CNS Strength Enhancer** · `g_i_belt012` · K1 · Tier 3 · 8,500 credits · Ability (Strength) 2 · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* — *“An experimental system that amplifies power signals along the length of the central nervous system, this generator, attached to a belt, provides greater impulses to all muscles, as well as a resistance to all sorts of perturbations of the user's system.”*

**Electrical Capacitance Shield** · `g_i_belt013` · K1 · Tier 3 · 8,500 credits · DamageImmunity (Electrical) ⚠ **IMMUNE** *(100%)* — *“This shielding device, worn around the waist, absorbs and stores electrical energy directed at the user, which is then released slowly over a period of time, dissipating harmlessly. The manner of release generates vibrations along the inside edge of the shield, giving it the less than complimentary nickname, 'The Tingler'.”*

**Thermal Shield Generator** · `g_i_belt014` · K1 · Tier 3 · 8,000 credits · DamageImmunity (Fire) ⚠ **IMMUNE** *(100%)* — *“This generator forms a magnetic shield around the wearer which, while ineffective against most modern weaponry, does allow for the ablation of directed heat attacks, generally in the form of fire.”*

**GenoHaradan Stealth Unit** · `geno_stealth` · K1 · Tier 2 · 1,250 credits · Skill bonus +8 ⚠ *(which skill is unresolved — subtype 2)* — *“The assassins of the GenoHaradan work in absolute secrecy, thanks to items such as this highly advanced stealth unit.”*

## Forearm — 33

**Peragus Mining Shield** · `100_fore01` · K2 · Tier 1 · 100 credits · Duration: 200 seconds — *“Absorbs: Heat 20pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. When equipped and activated, these safety energy shields project a safety shield around Peragus miners, protecting them from temperature extremes, accidental thermal detonations, and laser and plasma burns. The small power source can burn out when repeatedly stressed, requiring replacement of the entire unit.”*

**<FullName>'s Armband** ⚠ **UNIQUE** · `a_band_c01` · K2 · Tier 1 · 500 credits · Ability (Constitution) 1 — *“This band belonged to the Jedi <FullName>, who was exiled from the Jedi Order following the Mandalorian Wars.”*

**Nomi's Armband** ⚠ **UNIQUE** · `a_band_x01` · K2 · Tier 2 · 2,500 credits · ArmorAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 1 — *“Nomi displayed incredible affinity for the Force, but only reluctantly pursued Jedi training following the death of her husband, Andur. She became one of the greatest Jedi of the time, training under Master Thon.”*

**Vao Armband** · `a_band_x02` · K2 · Tier 2 · 1,500 credits · Ability (Dexterity) 1 — *“Crudely engraved upon this armband are the words: "For M Vao. - Z"”*

**Ludo Kressh's Armband** ⚠ **UNIQUE** · `a_band_x03` · K2 · Tier 2 · 5,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 1 · Armor 1 — *“Ludo Kressh was a powerful Sith who opposed fellow Sith Lord Naga Sadow in the Great Hyperspace War. This protective armband bears traces of the Dark Lord's once great power.”*

**Energy Shield** · `a_shield_01` · K2 · Tier 1 · 140 credits · Duration: 200 seconds — *“Absorbs: Energy, Electrical 40pts Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. When equipped and activated, these items project an energy shield around the wearer. The small power source can burn out when repeatedly stressed, requiring replacement of the entire unit.”*

**Mandalorian Melee Shield** · `a_shield_02` · K2 · Tier 1 · 1,120 credits · Duration: 200 seconds — *“Absorbs: Bludgeoning, Piercing, Slashing, 50pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Mandalorians don't fear melee combat, but anything that absorbs physical damage brings them a step closer to victory, and these forearm shields are a favorite. The units are discarded once their maximum activations have been expended.”*

**Arkanian Energy Shield** · `a_shield_03` · K2 · Tier 1 · 700 credits · Duration: 200 seconds — *“Absorbs: Energy, Sonic, Cold, Heat, Electrical 80pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Even 2000 years after the designs were pioneered, Arkanian technology remains desirable. When equipped and activated, this forearm shield protects against a variety of combat conditions, though it must be replaced often due to burnout.”*

**Echani Shield** · `a_shield_04` · K2 · Tier 1 · 980 credits · Duration: 200 seconds — *“Absorbs: Energy, Electrical 100pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The Echani put much effort into developing a forearm shield that, once activated, would allow a mercenary to close on a blaster-wielding enemy relatively unscathed. This unit is discarded once its energy cells are depleted.”*

**Mandalorian Power Shield** · `a_shield_05` · K2 · Tier 1 · 1,400 credits · Duration: 200 seconds — *“Absorbs: Energy, Bludgeoning, Piercing, Slashing 70pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. An improvement by the Mandalorians on their basic forearm shield, this variant proved decisive in several battles with the Republic. The units are discarded once their maximum number of activations have been expended.”*

**Echani Dueling Shield** · `a_shield_06` · K2 · Tier 1 · 1,680 credits · Duration: 200 seconds — *“Absorbs: Energy, Electrical 130pts Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Far more powerful than most forearm shields, when activated this unit absorbs some of the incoming energy to provide good protection without the need for bulky generators. The unit must still be replaced after repeated use, however.”*

**Verpine Prototype Shield** · `a_shield_07` · K2 · Tier 2 · 2,240 credits · Duration: 200 seconds — *“Absorbs: Energy, Sonic, Cold, Heat, Electrical 170pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Though manufactured by the Verpine, these forearm shields are based on highly modified Arkanian designs. They are must-have items for the professional soldier, though they have to be replaced when the maximum number of activations are expended.”*

**Energy Shield** · `g_i_frarmbnds01` · K1 · Tier 1 · 140 credits · Duration: 200 seconds — *“Deflection: Energy, Electrical 20pts Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. When equipped and activated, these items project an energy shield around the wearer. The small power source can burn out when repeatedly stressed, requiring replacement of the entire unit.”*

**Sith Energy Shield** · `g_i_frarmbnds02` · K1 · Tier 1 · 350 credits · Duration: 200 seconds — *“Deflection: Energy, Sonic, Electrical 30pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The Sith have made many improvements to personal forearm shielding, much to the dismay of the Jedi. Though efficient, the unit must be replaced often as it burns out when repeatedly activated.”*

**Arkanian Energy Shield** · `g_i_frarmbnds03` · K1 · Tier 2 · 700 credits · Duration: 200 seconds — *“Deflection: Energy, Sonic, Cold, Heat, Electrical 40pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Even 2000 years after the designs were pioneered, Arkanian technology remains desirable. When equipped and activated, this forearm shield protects against a variety of combat conditions, though it must be replaced often due to burnout.”*

**Echani Shield** · `g_i_frarmbnds04` · K1 · Tier 2 · 980 credits · Duration: 200 seconds — *“Deflection: Energy,Sonic, Electrical 50pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The Echani put much effort into developing a forearm shield that, once activated, would allow a mercenary to close on a blaster-wielding enemy relatively unscathed. This unit is discarded once its energy cells are depleted.”*

**Mandalorian Melee Shield** · `g_i_frarmbnds05` · K1 · Tier 2 · 1,120 credits · Duration: 200 seconds — *“Deflection: Bludgeoning, Piercing, Slashing, 20pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Mandalorians don't fear melee combat, but anything that absorbs physical damage brings them a step closer to victory, and these forearm shields are a favorite. The units are discarded once their maximum activations have been expended.”*

**Mandalorian Power Shield** · `g_i_frarmbnds06` · K1 · Tier 2 · 1,400 credits · Duration: 200 seconds — *“Deflection: Energy, Bludgeoning, Piercing, Slashing, Electrical 30pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. An improvement by the Mandalorians on their basic forearm shield, this variant proved decisive in several battles with the Republic. The units are discarded once their maximum number of activations have been expended.”*

**Echani Dueling Shield** · `g_i_frarmbnds07` · K1 · Tier 2 · 1,680 credits · Duration: 200 seconds — *“Deflection: Energy, Electrical 60pts Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Far more powerful than most forearm shields, when activated this unit absorbs some of the incoming energy to provide good protection without the need for bulky generators. The unit must still be replaced after repeated use, however.”*

**Yusanis' Dueling Shield** · `g_i_frarmbnds08` · K1 · Tier 2 · 1,960 credits · Duration: 200 seconds — *“Deflection: Energy, Electrical 100pts Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Yusanis sponsored many of the advances the Echani people are known for. Produced in his honor, these forearm shields are unmatched on the battlefield. The unit must be replaced when the maximum number of activations is depleted.”*

**Verpine Prototype Shield** · `g_i_frarmbnds09` · K1 · Tier 2 · 2,240 credits · Duration: 200 seconds — *“Deflection: Energy, Sonic, Cold, Heat, Electrical 70pts total Duration: 200 seconds, or max damage taken Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Though manufactured by the Verpine, these forearm shields are based on highly modified Arkanian designs. They are must-have items for the professional soldier, though they have to be replaced when the maximum number of activations are expended.”*

**Lower Saves, All 2** · `g_i_frarmbnds10` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 0)* Penalty_-2

**Lower Saves, All 4** · `g_i_frarmbnds11` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 0)* Penalty_-4

**Lower Saves, All 5** · `g_i_frarmbnds12` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 0)* Penalty_-5

**Lower Saves, Fortitude 2** · `g_i_frarmbnds13` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 1)* Penalty_-2

**Lower Saves, Fortitude 4** · `g_i_frarmbnds14` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 1)* Penalty_-4

**Lower Saves, Fortitude 5** · `g_i_frarmbnds15` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 1)* Penalty_-5

**Lower Saves, Reflex 2** · `g_i_frarmbnds16` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 3)* Penalty_-2

**Lower Saves, Reflex 4** · `g_i_frarmbnds17` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 3)* Penalty_-4

**Lower Saves, Reflex 5** · `g_i_frarmbnds18` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 3)* Penalty_-5

**Lower Saves, Will 2** · `g_i_frarmbnds19` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 2)* Penalty_-2

**Lower Saves, Will 4** · `g_i_frarmbnds20` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 2)* Penalty_-4

**Lower Saves, Will 5** · `g_i_frarmbnds21` · K1 · Tier 1 · no sale value · ReducedSpecificSavingThrow ⚠ *(unresolved — `iprp_savingthrow` subtype 2)* Penalty_-5

## Gauntlets — 42

**⚠ Sparring Gloves** · `a_gloves_00` · ⚠ AUTHORED · Tier 1 · 90 credits · **Damage (Bludgeoning) 1** — *“Cured hide over the knuckles and a strap across the palm. Sold at the door of every pit in the galaxy, to anyone who has broken a hand once.”*

**⚠ Echani Sparring Gloves** · `a_gloves_00b` · ⚠ AUTHORED · Tier 2 · 950 credits · **Damage (Bludgeoning) 2 · AttackBonus 1** — *“Layered and weighted to the gram. The Echani treat combat as a form of communication, and these are what they say it in — a training glove made by a people for whom training never stops.”*

**Insulated Gloves** · `a_gloves_01` · K2 · Tier 1 · 25 credits · DamageImmunity (Cold) ⚠ **DR 6** *(30%)* · DamageImmunity (Fire) ⚠ **DR 4** *(20%)* — *“These thick gloves are typically used by workers at metal processing plants.”*

**Exchange Casual Gloves** · `a_gloves_02` · K2 · Tier 1 · 55 credits · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* — *“Common attire for Exchange operatives, these gloves assist with a number of surreptitious activities.”*

**Taris Survival Gloves** · `a_gloves_04` · K2 · Tier 1 · 150 credits · Saving throw +1 ⚠ *(which save is unresolved — subtype 0)* — *“These gloves' name is a marketing tactic to remind people that a little extra protection is a good investment. Developed by Czerka following the bombardment of Taris by Darth Malak, these all-purpose gloves became quite popular.”*

**Accuracy Gloves** · `a_gloves_05` · K2 · Tier 1 · 200 credits · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) — *“These gloves are flexible, but very stiff. Though a bit awkward when first put on, they effectively steady one's hands, improving accuracy with ranged weapons.”*

**Gamorrean Gauntlets** · `a_gloves_06` · K2 · Tier 1 · 275 credits · AttackPenalty Penalty_-1 · Damage (Bludgeoning) 4 — *“These brutish gloves are heavy and clumsy. When used in unarmed combat, they allow for powerful, but less accurate blows. They have no practical effect when wielding a weapon.”*

**Exchange Work Gloves** · `a_gloves_07` · K2 · Tier 2 · 650 credits · Ability (Dexterity) 1 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 6)* — *“These gloves are typical attire for experienced Exchange members.”*

**Czerka Defensive Gauntlets** · `a_gloves_08` · K2 · Tier 2 · 699 credits · Armor 1 · Use Limitation Feat (Armour Prof Medium) — *“Czerka developed these very practical items for those who recognize the original purpose of gauntlets.”*

**Detonator Gloves** · `a_gloves_09` · K2 · Tier 2 · 900 credits · DamageImmunity (Fire) ⚠ **DR 5** *(25%)* · DamageImmunity (Slashing) ⚠ **DR 2** *(10%)* · Saving throw +2 ⚠ *(which save is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* — *“These gauntlets are specifically designed to protect the wearer from demolitions mishaps. Their protective capabilities also tend to increase the wearer's confidence when dealing with mines, improving their performance.”*

**Unarmed Accuracy Gloves** · `a_gloves_10` · K2 · Tier 2 · 1,100 credits · AttackBonus 1 · Damage (Bludgeoning) 2 · **Reflex save +2** ⚠ *(the game’s own file records +1; this game sets it at +2)* — *“These supple gloves add to impact and are suitable for parrying blades, effectively improving unarmed combat skills.”*

**Infiltrator Gloves** · `a_gloves_11` · K2 · Tier 2 · 7,000 credits · Ability (Dexterity) 2 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 6)* — *“These gloves are equipped with an advanced artifical intelligence unit that the wearer can use to tap into nearby computer systems through cables or wireless transmission. The system also stabilizes the wearer's hands for fine detail work.”*

**Jal Shey Perception Gloves** · `a_gloves_12` · K2 · Tier 2 · 1,850 credits · Ability (Dexterity) 1 · Ability (Wisdom) 1 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 3)* — *“The Jal Shey use these gloves during meditation. How they function is unknown, but they seem effective in increasing one's awareness to their surroundings.”*

**Gamorrean Wargloves** · `a_gloves_13` · K2 · Tier 2 · 2,000 credits · DecreaseAbilityScore (Dexterity) Penalty_-2 · Armor 3 · Use Limitation Feat (Armour Prof Heavy) — *“These monstrous gauntlets provide considerable protection but are quite inflexible.”*

**Eriadu Strength Amplifier** · `a_gloves_14` · K2 · Tier 2 · 2,000 credits · Ability (Strength) 2 — *“This device uses micro-bursts of repulsorlift energy to assist actions in combat, giving the appearance that the user is stronger than normal.”*

**Karakan Gauntlets** · `a_gloves_15` · K2 · Tier 2 · 7,500 credits · Ability (Dexterity) 1 · Saving throw +3 ⚠ *(which save is unresolved — subtype 0)* — *“These heavy gauntlets, created by the isolationist Karakan, are almost a complete medical computer in themselves. They constantly monitor and adjust the nervous impulses, blood pressure, and tension through the wearers hands. The resulting increase in stability and overall system integrity have many benefits.”*

**Bothan Precision Gloves** · `a_gloves_16` · K2 · Tier 2 · 4,750 credits · Ability (Dexterity) 1 · DamageImmunity (Fire) ⚠ **DR 5** *(25%)* · DamageImmunity (Slashing) ⚠ **DR 3** *(15%)* · DamageResist (Fire) Resist_5/- · Saving throw +2 ⚠ *(which save is unresolved — subtype 1)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 1)* — *“For obvious reasons, these multi-purpose gloves are highly sought after by demolitions experts.”*

**Sith Power Gauntlets** · `a_gloves_17` · K2 · Tier 3 · 3,000 credits · Ability (Strength) 3 — *“Based on stolen Eriadu designs, items of this type utilize almost uncomfortable bursts of repulsorlift energy to assist movement. They are rarely seen outside of Sith possession.”*

**Gamorrean Power Gauntlets** · `a_gloves_18` · K2 · Tier 3 · 7,250 credits · Ability (Strength) 2 · Damage (Bludgeoning) 2 · Armor 1 · Use Limitation Feat (Armour Prof Heavy) · Use Limitation Feat (Master Power Attack) ⚠ attack chain · OnHit (Stun) 14 — *“These heavy gloves are brutally effective in unarmed combat.”*

**Nagai Combat Gloves** · `a_gloves_19` · K2 · Tier 3 · 10,000 credits · DamageResist (Energy) Resist_5/- · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* — *“The Nagai, who favor knife fighting, employ these gloves to foil those who attempt to break their charge with blaster fire.”*

**Kubaz Scoundrel Gloves** · `a_gloves_20` · K2 · Tier 3 · 12,500 credits · Ability (Dexterity) 5 · UseLimitationClass ⚠ *(unresolved — `classes` subtype 2)* 0 · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 6)* — *“The Kubaz species is most renown for their interest in culture, but they also have a penchant for less refined matters, such as smuggling and espionage. As they are not capable of interstellar travel themselves, their items are very rare finds.”*

**Automation Gloves** · `a_gloves_21` · K2 · Tier 3 · 12,800 credits · Ability (Dexterity) 3 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 5)* — *“A sophisticated computer controls the movements of these gloves. While difficult to become accustomed to, they greatly increase the wearer's precision.”*

**Jal Shey Meditation Gloves** · `a_gloves_22` · K2 · Tier 3 · 15,000 credits · Ability (Dexterity) 2 · Ability (Wisdom) 2 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* — *“The Jal Shey use these gloves during meditation. How they function is unknown, but they seem effective in increasing one's awareness to their surroundings.”*

**Echani Accuracy Gloves** · `a_gloves_23` · K2 · Tier 3 · 16,500 credits · AttackBonus 1 · Ability (Dexterity) 1 · Damage (Bludgeoning) 5 — *“Unarmed combat is an ancient tradition in the Echani culture. These combat gloves help these old techniques to be competitive against the most advanced melee weapons.”*

**Zeison Sha Gloves** · `a_gloves_24` · K2 · Tier 3 · 18,250 credits · Ability (Constitution) 2 · Regeneration 1 — *“These gloves are named for the Zeison Sha, not by them. This Force sensitive culture developed their powers as a means of surviving the harsh planet. Zeison Sha stress independence and survival as well as assistance to those in need.”*

**Dominator Gauntlets** · `a_gloves_25` · K2 · Tier 3 · 15,000 credits · Ability (Strength) 5 — *“A working proto-type of a huge technological advancement in power gauntlets, the Dominators give the user unparalleled strength and power.”*

**Nikto Soldier Gloves** · `a_gloves_26` · K2 · Tier 4 · 21,900 credits · Ability (Dexterity) 2 · Ability (Strength) 3 · UseLimitationClass ⚠ *(unresolved — `classes` subtype 0)* 0 — *“Nikto, though strong and powerful, are typically subservient to other races, such as the Hutts. Some subspecies of Nikto make especially adept and loyal soldiers.”*

**Ossluk's Gloves** ⚠ **UNIQUE** · `a_gloves_27` · K2 · Tier 4 · 25,000 credits · Ability (Constitution) 1 · Ability (Dexterity) 1 · Ability (Strength) 2 — *“These gloves are believed to have belonged to the great Gand Warrior Ossluk Noslee. Most Gand are not identified by name - that Ossluk earned two is testimony to his accomplishments.”*

**Disruption Gloves** · `a_gloves_28` · K2 · Tier 4 · 26,000 credits · Damage (Unstoppable) 1d10 — *“These gloves, intended to be used while unarmed, are designed to penetrate enemy shields and defenses.”*

**Improved Automation Gloves** · `a_gloves_29` · K2 · Tier 4 · 27,500 credits · Ability (Dexterity) 5 · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 5)* — *“A sophisticated computer controls the movements of these gloves. While difficult to become accustomed to, they greatly increase the wearer's precision.”*

**Lightning Gloves** · `a_gloves_30` · K2 · Tier 4 · 29,600 credits · AttackBonus 1 · Damage (Electrical) 2d6 · DamageResist (Electrical) Resist_10/- — *“High charges of electricity pulse through these gloves when they strike an object, making them powerful in unarmed combat.”*

**⚠ Name corrupted in the source** · `g1_i_gauntlet01` · K1 · Tier 3 · 8,500 credits · Ability (Dexterity) 3 · Blaster Bolt Deflect Increase 5 — ⚠ *Its name field carries unrelated text from elsewhere in the game’s string table; the properties above are the item’s own. Recorded, not renamed.*

**Strength Gauntlets** · `g_i_gauntlet01` · K1 · Tier 2 · 1,000 credits · Ability (Strength) 1 — *“Developed by the Mephilis Corporation, these gauntlets use pulses of energy to stimulate muscles at the key leverage points of combat actions, effectively increasing strength.”*

**Eriadu Strength Amplifier** · `g_i_gauntlet02` · K1 · Tier 2 · 2,000 credits · Ability (Strength) 2 — *“This device uses micro-bursts of repulsorlift energy to assist actions in combat, giving the appearance that the user is stronger than normal.”*

**Sith Power Gauntlets** · `g_i_gauntlet03` · K1 · Tier 2 · 3,000 credits · Ability (Strength) 3 — *“Based on stolen Eriadu designs, items of this type utilize almost uncomfortable bursts of repulsorlift energy to assist movement. They are rarely seen outside of Sith possession.”*

**Stabilizer Gauntlets** · `g_i_gauntlet04` · K1 · Tier 1 · 300 credits · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* — *“These gauntlets are quite stiff, minimizing actions that might interfere with the manipulation of volatile materials. The user must have basic knowledge of Demolitions (paid points into the skill) to benefit from this item.”*

**Bothan "Machinist" Gloves** · `g_i_gauntlet05` · K1 · Tier 2 · 600 credits · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* — *“This item uses microbursts of counter-current energy to calm unsteady nerves, increasing accuracy in the handling of volatile materials. The user must have basic knowledge of Demolitions (paid points into the skill) to benefit from this item.”*

**Verpine Bond Gauntlets** · `g_i_gauntlet06` · K1 · Tier 2 · 1,500 credits · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 1)* — *“Tensor-mesh stiffens the forearm for steady handling of volatile materials. The insect-like Verpine don't personally use these items, claiming they merely mimic their own exoskeletons. The user must have basic knowledge of Demolitions (paid points into the skill) to benefit from this item.”*

**Dominator Gauntlets** · `g_i_gauntlet07` · K1 · Tier 3 · 15,000 credits · Ability (Strength) 5 — *“A working proto-type of a huge technological advancement in power gauntlets, the Dominators give the user unparalleled strength and power.”*

**Karakan Gauntlets** · `g_i_gauntlet08` · K1 · Tier 3 · 7,500 credits · Ability (Dexterity) 1 · Saving throw +3 ⚠ *(which save is unresolved — subtype 0)* — *“These heavy gauntlets, created by the isolationist Karakan, are almost a complete medical computer in themselves. They constantly monitor and adjust the nervous impulses, blood pressure, and tension through the wearers hands. The resulting increase in stability and overall system integrity have many benefits.”*

**Infiltrator Gloves** · `g_i_gauntlet09` · K1 · Tier 3 · 7,000 credits · Ability (Dexterity) 1 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 6)* — *“These gloves are equipped with an advanced artifical intelligence unit that the wearer can use to tap into nearby computer systems through cables or wireless transmission. The system also stabilizes the wearer's hands for fine detail work.”*

**GenoHaradan Power Gloves** · `geno_gloves` · K1 · Tier 3 · 7,000 credits · Ability (Strength) 4 — *“Modeled on the Eriadu designs, these gloves use bursts of repulsor-lift energy to assist movement, effectively giving the wearer tremendous strength.”*

## Implant — 67

**⚠ Clarity Package** · `a_imp1_11` · ⚠ AUTHORED · Tier 2 · 1,000 credits · **Ability (Wisdom) 1** — *“A quieting filter across the limbic feed. It does not make you wiser. It stops the noise that was drowning you out.”*

**⚠ Motor Package** · `a_imp1_12` · ⚠ AUTHORED · Tier 2 · 1,000 credits · **Ability (Strength) 1** — *“Myomer threading down the long muscles. The standard dockworker's implant, and the standard dockworker's back problem.”*

**⚠ Presence Package** · `a_imp1_13` · ⚠ AUTHORED · Tier 2 · 1,000 credits · **Ability (Charisma) 1** — *“A vocal-resonance tuner and a subdermal pheromone reservoir. Everyone can tell. Nobody minds.”*

**⚠ Fortitude Package** · `a_imp1_02` · ⚠ AUTHORED · Tier 1 · 50 credits · **UseLimitationAttribute (Constitution) >=12 · ImprovedSavingThrowsSpecific: Fortitude ⚠ **2**** — *“A filtration mesh threaded through the lymphatic line. It does not make you stronger; it makes you harder to poison.”*

**⚠ Will Package** · `a_imp1_03` · ⚠ AUTHORED · Tier 1 · 50 credits · **UseLimitationAttribute (Constitution) >=12 · ImprovedSavingThrowsSpecific: Will ⚠ **2**** — *“A dampener seated at the base of the skull. Cheap, legal, and deeply unpopular with anyone who has to interrogate you.”*

**Reflex Package** · `e_imp1_01` · K2 · Tier 1 · 50 credits · UseLimitationAttribute (Constitution) >=12 · **Reflex save +2** ⚠ *(the game’s own file records +1; this game sets it at +2)* — *“This implant boosts the regular energy impulses of the nervous system, sharpening the performance of dexterous action. Inactive users may suffer the odd lingering twitch.”*

**Pheromone Package** · `e_imp1_02` · K2 · Tier 1 · 200 credits · Ability (Charisma) 1 · UseLimitationAttribute (Constitution) >=12 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 4)* — *“This implant allows the user to subtly secrete synthetic pheromones that generally stimulate a pleasant behavior response in a wide range of species.”*

**Cardio Package** · `e_imp1_03` · K2 · Tier 2 · 1,000 credits · Ability (Constitution) 1 · UseLimitationAttribute (Constitution) >=12 — *“This implant micromanages the cardiovascular system, effectively increasing the user's constitution faster and further than hard work and exercise might.”*

**Strength Package** · `e_imp1_04` · K2 · Tier 2 · 1,000 credits · Ability (Strength) 1 · UseLimitationAttribute (Constitution) >=12 — *“This implant effectively increases the user's strength without the need for additional muscle mass through a combination of autonomic regulatory center management and small doses of adrenal stimulants.”*

**Response Package** · `e_imp1_05` · K2 · Tier 2 · 1,000 credits · Ability (Dexterity) 1 · UseLimitationAttribute (Constitution) >=12 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 2)* — *“This implant boosts the regular energy impulses of the nervous system, sharpening the performance of dexterous action. Inactive users may suffer the odd lingering twitch.”*

**Fitness Package** · `e_imp1_06` · K2 · Tier 3 · 9,800 credits · Ability (Constitution) 1 · Ability (Strength) 1 · UseLimitationAttribute (Constitution) >=12 — *“This simple but advanced implant combines the functionality of the more common Strength and Cardio Packages.”*

**Skills Package** · `e_imp1_07` · K2 · Tier 3 · 20,000 credits · UseLimitationAttribute (Constitution) >=12 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 4)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 2)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 7)* — *“This ingenious device modifies brain chemistry to improve general problem solving and data processing abilities.”*

**Health Package** · `e_imp1_08` · K2 · Tier 4 · 30,000 credits · Ability (Constitution) 1 · UseLimitationAttribute (Constitution) >=12 · Regeneration 1 — *“This advanced implant package employs nano-technology to speed healing.”*

**Physical Boost Package** · `e_imp1_09` · K2 · Tier 4 · 30,000 credits · Ability (Constitution) 1 · Ability (Dexterity) 1 · Ability (Strength) 1 · UseLimitationAttribute (Constitution) >=12 — *“This device improves all physical attributes, making it one of the most valuable of implants of its type.”*

**Mental Boost Package** · `e_imp1_10` · K2 · Tier 4 · 30,000 credits · Ability (Charisma) 1 · Ability (Intelligence) 1 · Ability (Wisdom) 1 · UseLimitationAttribute (Constitution) >=12 — *“This device improves all mental attributes, making it one of the most valuable of implants of its type.”*

**Retinal Combat Implant** · `e_imp2_01` · K2 · Tier 1 · 750 credits · UseLimitationAttribute (Constitution) >=14 · Immunity (Critical Hits) 0 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 3)* — *“This ocular implant greatly increases visual acuity, allowing the user to better track enemy movement in combat. General awareness will improve as well.”*

**Lornan Implant** · `e_imp2_02` · K2 · Tier 1 · 300 credits · UseLimitationAttribute (Constitution) >=14 · DamageImmunity (Electrical) ⚠ **DR 2** *(10%)* · DamageImmunity (Energy) ⚠ **DR 1** *(5%)* — *“This implant regulates electrical current, protecting the user's brain from energy surges.”*

**Biotech Implant** · `e_imp2_03` · K2 · Tier 2 · 1,200 credits · UseLimitationAttribute (Constitution) >=14 · Regeneration 1 — *“This implant does use relatively experimental nano-technology to speed healing, but relies more on coagulants and solid doses of pain relievers. If you feel better, you are better.”*

**Power Implant** · `e_imp2_04` · K2 · Tier 2 · 2,600 credits · Ability (Strength) 2 · UseLimitationAttribute (Constitution) >=14 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* — *“This improved variant of the Strength Package employs substantially higher doses of stimulants.”*

**Alacrity Implant** · `e_imp2_05` · K2 · Tier 3 · 5,800 credits · Ability (Dexterity) 2 · UseLimitationAttribute (Constitution) >=14 · **Reflex save +2** ⚠ *(the game’s own file records +1; this game sets it at +2)* — *“The Alacrity Implant enhances the user's nervous system, signficantly improving reaction times.”*

**Insight Implant** · `e_imp2_06` · K2 · Tier 3 · 12,300 credits · Ability (Wisdom) 2 · UseLimitationAttribute (Constitution) >=14 · Saving throw +1 ⚠ *(which save is unresolved — subtype 3)* — *“By stimulating less used neural networks in the brain, this implant allows the user to see solutions they may not have otherwise considered.”*

**Skills Implant** · `e_imp2_07` · K2 · Tier 4 · 22,000 credits · UseLimitationAttribute (Constitution) >=14 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 4)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 2)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 7)* — *“This ingenious device modifies brain chemistry to improve general problem solving and data processing abilities.”*

**Durability Implant** · `e_imp2_08` · K2 · Tier 4 · 31,000 credits · Ability (Constitution) 1 · UseLimitationAttribute (Constitution) >=14 · DamageResist (Electrical) Resist_5/- · DamageResist (Energy) Resist_5/- — *“This implant regulates current through the body, both improving stamina and providing resistance to energy-related attacks.”*

**Physical Boost Implant** · `e_imp2_09` · K2 · Tier 4 · 31,000 credits · Ability (Constitution) 1 · Ability (Dexterity) 2 · Ability (Strength) 2 · UseLimitationAttribute (Constitution) >=14 — *“This device improves all physical attributes, making it one of the most valuable of implants of its type.”*

**Mental Boost Implant** · `e_imp2_10` · K2 · Tier 4 · 31,000 credits · Ability (Charisma) 2 · Ability (Intelligence) 1 · Ability (Wisdom) 2 · UseLimitationAttribute (Constitution) >=14 — *“This device improves all mental attributes, making it one of the most valuable of implants of its type.”*

**Bio-Antidote System** · `e_imp3_01` · K2 · Tier 1 · 100 credits · Ability (Constitution) 1 · UseLimitationAttribute (Constitution) >=16 · Immunity (Poison) 0 — *“This implant maintains an ever-circulating stream of antitoxins in the user, increasing relevant antidotes for specific poisons introduced. Side effects include dry mouth.”*

**Nerve Enhancement System** · `e_imp3_02` · K2 · Tier 2 · 600 credits · UseLimitationAttribute (Constitution) >=16 · Immunity (MindSpells) 0 — *“This implant regulates the nervous system, preventing loss of consciousness due to sudden impact or sensory overload.”*

**Reaction System** · `e_imp3_03` · K2 · Tier 2 · 1,600 credits · Ability (Dexterity) 3 · UseLimitationAttribute (Constitution) >=16 — *“This system supplants the user's normal nervous system, enhancing it artificially. It allows the impluses to travel faster and farther along the system, improving reaction time, while also improving fine motor control, increasing accuracy.”*

**Advanced Combat System** · `e_imp3_04` · K2 · Tier 2 · 3,400 credits · AttackBonus 1 · UseLimitationAttribute (Constitution) >=16 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats (Weapon Spec Blaster) · BonusFeats (Weapon Spec Blaster Rifle) — *“This system supplants the user's normal nervous system, enhancing it artificially. It allows the impluses to travel faster and farther along the system, improving reaction time, while also improving fine motor control, increasing accuracy.”*

**Bavakar Strength System** · `e_imp3_05` · K2 · Tier 3 · 7,500 credits · Ability (Strength) 3 · UseLimitationAttribute (Constitution) >=16 — *“This implant stimulates physical performance well beyond the user's norm. The Bavakar Medical Research Labs are at the forefront of developmental cybernetics.”*

**Cardio Power System** · `e_imp3_06` · K2 · Tier 3 · 10,000 credits · Ability (Constitution) 4 · UseLimitationAttribute (Constitution) >=16 — *“This implant increases the cardio-vascular recovery rate and pain tolerance of the wearer, giving them almost supernatural stamina.”*

**Skills System** · `e_imp3_07` · K2 · Tier 3 · 15,000 credits · UseLimitationAttribute (Constitution) >=16 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 4)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 7)* — *“This ingenious device modifies brain chemistry to improve general problem solving and data processing abilities.”*

**Numbness System** · `e_imp3_08` · K2 · Tier 4 · 29,500 credits · Ability (Constitution) 2 · UseLimitationAttribute (Constitution) >=16 · DamageResist (Bludgeoning) Resist_5/- · DamageResist (Piercing) Resist_5/- · DamageResist (Slashing) Resist_5/- — *“By converting all pain into benign brain signals, this implant system greatly increases one's durability. It has no direct negative side effects, as its user is still fully aware of his body's current state of health.”*

**Physical Boost System** · `e_imp3_09` · K2 · Tier 4 · 32,000 credits · Ability (Constitution) 2 · Ability (Dexterity) 3 · Ability (Strength) 2 · UseLimitationAttribute (Constitution) >=16 — *“This device improves all physical attributes, making it one of the most valuable of implants of its type.”*

**Mental Boost System** · `e_imp3_10` · K2 · Tier 4 · 32,000 credits · Ability (Charisma) 2 · Ability (Intelligence) 2 · Ability (Wisdom) 3 · UseLimitationAttribute (Constitution) >=16 — *“This device improves all mental attributes, making it one of the most valuable of implants of its type.”*

**Strength D-Package** · `e_imp4_01` · K2 · Tier 1 · 75 credits · Ability (Constitution) 1 · Ability (Strength) 1 · UseLimitationAttribute (Constitution) >=18 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Immunity D-Package** · `e_imp4_02` · K2 · Tier 1 · 300 credits · UseLimitationAttribute (Constitution) >=18 · Immunity (Critical Hits) 0 · Immunity (Poison) 0 · Immunity (MindSpells) 0 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Perception D-Package** · `e_imp4_03` · K2 · Tier 2 · 900 credits · Ability (Charisma) 1 · Ability (Wisdom) 2 · UseLimitationAttribute (Constitution) >=18 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Enhancement D-Package** · `e_imp4_04` · K2 · Tier 2 · 1,700 credits · UseLimitationAttribute (Constitution) >=18 · BonusFeats (Dueling) · BonusFeats (Advanced Dueling) · BonusFeats (Two Weapon Advanced) · BonusFeats (Master Dueling) · BonusFeats (Two Weapon Mastery) · BonusFeats (Two Weapon Fighting) — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Immortality D-Package** · `e_imp4_05` · K2 · Tier 2 · 3,700 credits · Ability (Constitution) 3 · UseLimitationAttribute (Constitution) >=18 · BonusFeats (Improved Toughness) · BonusFeats (Master Toughness) · BonusFeats (Toughness) — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Quickness D-Package** · `e_imp4_06` · K2 · Tier 3 · 7,600 credits · Ability (Dexterity) 4 · UseLimitationAttribute (Constitution) >=18 · Armor 1 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Skills D-Package** · `e_imp4_07` · K2 · Tier 3 · 12,800 credits · UseLimitationAttribute (Constitution) >=18 · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 4)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 6)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 2)* · Skill bonus +6 ⚠ *(which skill is unresolved — subtype 7)* — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Universal D-Package** · `e_imp4_08` · K2 · Tier 3 · 18,200 credits · Ability (Charisma) 2 · Ability (Constitution) 2 · Ability (Dexterity) 2 · Ability (Intelligence) 2 · Ability (Strength) 2 · Ability (Wisdom) 2 · UseLimitationAttribute (Constitution) >=18 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Physical Boost D-Package** · `e_imp4_09` · K2 · Tier 4 · 23,600 credits · Ability (Constitution) 3 · Ability (Dexterity) 3 · Ability (Strength) 3 · UseLimitationAttribute (Constitution) >=18 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**Mental Boost D-Package** · `e_imp4_10` · K2 · Tier 4 · 29,000 credits · Ability (Charisma) 3 · Ability (Intelligence) 3 · Ability (Wisdom) 3 · UseLimitationAttribute (Constitution) >=18 — *“D-Package implants are larger and more intrusive than other types. They tend to have more impressive effects, but can only be used by very healthy individuals.”*

**⚠ Name corrupted in the source** · `g1_i_implant301` · K1 · Tier 2 · 3,500 credits · Ability (Dexterity) 2 · Skill bonus +10 ⚠ *(which skill is unresolved — subtype 3)* — ⚠ *Its name field carries unrelated text from elsewhere in the game’s string table; the properties above are the item’s own. Recorded, not renamed.*

**⚠ Name corrupted in the source** · `g1_i_implant302` · K1 · Tier 2 · 3,000 credits · Immunity (MindSpells) 0 · Immunity (Poison) 0 — ⚠ *Its name field carries unrelated text from elsewhere in the game’s string table; the properties above are the item’s own. Recorded, not renamed.*

**Advanced Combat Implant** · `g1_i_implant303` · K1 · Tier 3 · 7,000 credits · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats ⚠ cut content · BonusFeats (Weapon Focus Melee Weapons) · BonusFeats (Weapon Prof Blaster) · BonusFeats (Weapon Prof Blaster Rifle) · BonusFeats ⚠ cut content · BonusFeats (Weapon Prof Melee Weapons) · BonusFeats (Weapon Spec Blaster) · BonusFeats (Weapon Spec Blaster Rifle) · BonusFeats ⚠ cut content · BonusFeats (Weapon Spec Melee Weapons) — *“The Advanced Combat Implant is an experimental technology, designed to make computer data available to the user. Naturally, one of the first uses for this technology was combat. This implant contains weapons specificatio”* ⚠ *(description truncated in source)*

**Advanced Alacrity Impant** · `g1_i_implant304` · K1 · Tier 4 · 22,000 credits · Ability (Dexterity) 5 — *“By fine-tuning the user's nervous system, this implant allows vastly improved reaction times and coordination over unmodified individuals. The success of this implant, though not in wide distribution due to its cost, has”* ⚠ *(description truncated in source)*

**Cardio Package** · `g_i_implant101` · K1 · Tier 2 · 1,000 credits · Ability (Constitution) 1 — *“This implant micromanages the cardiovascular system, effectively increasing the user's constitution faster and further than hard work and exercise might.”*

**Response Package** · `g_i_implant102` · K1 · Tier 2 · 1,000 credits · Ability (Dexterity) 1 — *“This implant boosts the regular energy impulses of the nervous system, sharpening the performance of dexterous action. Inactive users may suffer the odd lingering twitch.”*

**Memory Package** · `g_i_implant103` · K1 · Tier 2 · 1,000 credits · Ability (Intelligence) 1 — *“This implant stimulates the brain, effectively increasing the user's capacity for intelligent thought, all at a price cheaper than a trip to the libraries of Coruscant.”*

**—** · `g_i_implant104` · K1 · Tier 1 · no sale value — *“This implant releases synthetic versions of the natural stimulants produced by the body, temporarily boosting the user's stamina.”*

**Biotech Package** · `g_i_implant201` · K1 · Tier 2 · 1,000 credits · Regeneration 1 — *“This implant does use relatively experimental nano-technology to speed healing, but relies more on coagulants and solid doses of pain relievers. If you feel better, you are better.”*

**Retinal Combat Implant** · `g_i_implant202` · K1 · Tier 2 · 750 credits · Immunity (Critical Hits) 0 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 3)* — *“This ocular implant greatly increases visual acuity, allowing the user to better track enemy movement in combat. General awareness will improve as well.”*

**Nerve Enhancement Package** · `g_i_implant203` · K1 · Tier 1 · 500 credits · Immunity (MindSpells) 0 — *“This implant regulates the nervous system, preventing loss of consciousness due to sudden impact or sensory overload.”*

**—** · `g_i_implant204` · K1 · Tier 1 · no sale value — *“This implant bolsters the immune system, prompting it to react immediately aggressively toward any virus or bacterium that might have otherwise resulted in a debilitating sickness.”*

**Bavakar Cardio Package** · `g_i_implant301` · K1 · Tier 2 · 2,000 credits · Ability (Constitution) 2 — *“This implant stimulates cardiovascular performance well beyond the user's norm. The Bavakar Medical Research Labs are at the forefront of developmental cybernetics.”*

**Bavakar Reflex Enhancement** · `g_i_implant302` · K1 · Tier 2 · 2,000 credits · Ability (Dexterity) 2 — *“Stimulants and energy bursts allow this implant to boost a user's reflexes well beyond normal. The Bavakar Medical Research Labs are at the forefront of developmental cybernetics.”*

**Bavakar Memory Chip** · `g_i_implant303` · K1 · Tier 2 · 2,000 credits · Ability (Intelligence) 2 — *“This implant controls a cocktail of synthetic nutrients, encouraging quick thought in the user. The Bavakar Medical Research Labs are at the forefront of developmental cybernetics.”*

**Bio-Antidote Package** · `g_i_implant304` · K1 · Tier 1 · 500 credits · Immunity (Poison) 0 — *“This implant maintains an ever-circulating stream of antitoxins in the user, increasing relevant antidotes for specific poisons introduced. Side effects include dry mouth.”*

**Cardio Power System** · `g_i_implant305` · K1 · Tier 3 · 10,000 credits · Ability (Constitution) 4 — *“This implant increases the cardio-vascular recovery rate and pain tolerance of the wearer, giving them almost supernatural stamina.”*

**Gordulan Reaction System** · `g_i_implant306` · K1 · Tier 3 · 10,000 credits · Ability (Dexterity) 4 — *“This implant hyper-stimulates the nervous system of the wearer, significantly improving both reaction time and hand-eye coordination.”*

**Navardan Regenerator** · `g_i_implant307` · K1 · Tier 3 · 8,500 credits · Regeneration 2 — *“This implant gives incredible healing powers, allowing wounds and injuries to heal in mere seconds instead of days or weeks.”*

**Sith Regenerator** · `g_i_implant308` · K1 · Tier 3 · 8,500 credits · Regeneration 2 — *“Extensively used by Sith intelligence operatives, this implant stimulate cell replication in the user's body, allowing wounds to be healed quickly and easily. It is most frequently used on operatives operating behind enemy lines for extended periods, where medical treatment is not normally available.”*

**Beemon Package** · `g_i_implant309` · K1 · Tier 3 · 7,500 credits · Ability (Constitution) 3 — *“Beemon's top of the line package usurps the body's natural reactions to stress and damage, allowing the user to withstand greater amounts of punishment and exertion than normally possible.”*

**Cyber Reaction System** · `g_i_implant310` · K1 · Tier 3 · 7,500 credits · Ability (Dexterity) 3 — *“This system supplants the user's normal nervous system, enhancing it artificially. It allows the impluses to travel faster and farther along the system, improving reaction time, while also improving fine motor control, increasing accuracy.”*

## Mask — 59

**Survey Gear** · `100_mask01` · K2 · Tier 1 · 60 credits · DamageResist (Sonic) Resist_5/- · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees When surveying new asteroid claims, this headgear is designed to help identify both pockets of Peragian gas and any placed thermal charges in the area. The small sonic generation and receiving gear within the helmet is designed to absorb any high decibel emissions from sonic charges (and sonic grenades).”*

**Neural Band** · `a_helmet_01` · K2 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees Developed after the Exar Kun war, this item bolsters the willpower of the user by electrically reinforcing established mental patterns. Republic troops called it "Little Shocky".”*

**Breath Mask** · `a_helmet_02` · K2 · Tier 1 · 100 credits · Immunity (Poison) 0 — *“Restricted: not useable by Wookiees This is standard issue gear for Republic forces and most professional soldiers, protecting against a variety of gas-based attacks.”*

**Rakatan Band** · `a_helmet_03` · K2 · Tier 1 · 85 credits · Ability (Wisdom) 1 — *“Restricted: not useable by Wookiees This simple device improves the wearer's ability to perceive the reality of their surroundings. The origin behind the item's name is unknown, but rumor has it that these bands were constructed as a defense against an ancient species of alien deceivers, who made absurd claims of dominance concerning their role in the galaxy. It is said this species of lying primitives went so far as to take credit for almost every major event in galactic history since the discovery of the hyperdrive.”*

**Stealth Field Enhancer** · `a_helmet_04` · K2 · Tier 1 · 400 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* — *“Restricted: not useable by Wookiees A specialized espionage unit designed to get the most out of a stealth field generator by improving the user's perception of the field while in Stealth Mode.”*

**Bothan Perception Visor** · `a_helmet_05` · K2 · Tier 1 · 1,000 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees Bothans treat information like any other resource, and invest a great deal in devices that help collect it. These Bothan visors are considered to be among the best in the galaxy.”*

**Sonic Nullifiers** · `a_helmet_06` · K2 · Tier 1 · 100 credits · DamageResist (Sonic) Resist_10/- · Use Limitation Feat (Armour Prof Light) — *“Restricted: not useable by Wookiees Replacing bulky ear protection, these items make use of newly developed counterwave-nullifiers, an innovation pioneered by shipyard workers, not the military.”*

**Interface Band** · `a_helmet_07` · K2 · Tier 2 · 1,000 credits · DamageResist (Sonic) Resist_5/- · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees This item provides a mental interface to a store of information on electronic systems common to security, demolitions, and general computing functions.”*

**Targeting Visor** · `a_helmet_08` · K2 · Tier 2 · 1,000 credits · AttackBonus 1 · **Reflex save +2** ⚠ *(the game’s own file records +1; this game sets it at +2)* — *“Restricted: not useable by Wookiees Through assorted heads-up displays and sharpened vision, this device increases one's accuracy in combat.”*

**Shielding Visor** · `a_helmet_09` · K2 · Tier 2 · 1,500 credits · DamageImmunity (Electrical) ⚠ **DR 1** *(5%)* · DamageImmunity (Energy) ⚠ **DR 1** *(5%)* · DamageImmunity (Ion) ⚠ **DR 1** *(5%)* · Armor 1 · Use Limitation Feat (Armour Prof Medium) — *“Restricted: not useable by Wookiees Intersystem travel is commonplace, but the inherent dangers should not be forgotten, especially in times of war. Many consider these to be essential equipment for spacefarers.”*

**Spacer's Sensor** ⚠ **UNIQUE** · `a_helmet_10` · K2 · Tier 2 · 1,750 credits · Ability (Dexterity) 1 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) — *“Restricted: not useable by Wookiees These visors are often used by smugglers and others who desire better combat skills yet are too focused on other endeavors to learn them normally.”*

**Regal Visor** · `a_helmet_11` · K2 · Tier 2 · 2,500 credits · Ability (Charisma) 1 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 4)* — *“Restricted: not useable by Wookiees This attractive headgear includes a voice enhancement module that regulates tone and volume of the wearer's speech. It is employed in diplomatic situations where the slightest error could offend.”*

**Meditation Band** · `a_helmet_12` · K2 · Tier 2 · 3,250 credits · Ability (Wisdom) 1 · DamageImmunity (Dark Side) ⚠ **DR 4** *(20%)* · Saving throw +1 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees This potent device helps shield one's mind from dark thoughts and influences. It will not protect the user from evil that stems from within, however.”*

**Bothan Sensory Visor** · `a_helmet_13` · K2 · Tier 2 · 150 credits · Use Limitation Feat (Armour Prof Light) · Immunity (Critical Hits) 0 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees Bothans place great importance on the tools of the information trade. They would consider these items to be of average quality, though their standards are exceptionally high.”*

**Arkanian Blinders** · `a_helmet_14` · K2 · Tier 2 · 3,250 credits · DamageImmunity (Fire) ⚠ **DR 2** *(10%)* · Armor 1 · Use Limitation Feat (Armour Prof Medium) · Immunity (MindSpells) 0 — *“Restricted: not useable by Wookiees Due to their high-sensitivity to infrared light, Arkanians developed IR Blinders for when they travel to worlds with suns that are high in such light emissions. This technology was adapted to filter out excessive amounts of any electro-magnetic energies, thus preventing any "ocular-overload".”*

**Combat Sensor** · `a_helmet_15` · K2 · Tier 3 · 6,000 credits · Ability (Dexterity) 2 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) — *“Restricted: not useable by Wookiees This improved version of the Spacer's Sensor is for wealthier travelers who are expecting combat.”*

**Multi-spectral Target Assessor** · `a_helmet_16` · K2 · Tier 3 · 9,500 credits · AttackBonus 3 · BonusFeats (Precise Shot I) ⚠ attack chain · BonusFeats (Precise Shot Ii) ⚠ attack chain · Use Limitation Feat (Weapon Spec Blaster) · Use Limitation Feat (Weapon Spec Blaster Rifle) · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees This advanced device is only of use to those who are already highly skilled with ranged weapons. The plethora of information relayed provides the trained user with enhanced accuracy.”*

**Consciousness Helm** · `a_helmet_17` · K2 · Tier 3 · 11,250 credits · Ability (Constitution) 2 · Armor 1 · Use Limitation Feat (Armour Prof Medium) — *“Restricted: not useable by Wookiees This helmet's name is derived not from any cerebral effect, but on its ability to help keep its wearer conscious.”*

**Rebreather Mask** · `a_helmet_18` · K2 · Tier 3 · 12,500 credits · Ability (Constitution) 1 · Use Limitation Feat (Armour Prof Medium) · Immunity (Poison) 0 · Regeneration 1 — *“Restricted: not useable by Wookiees A solid improvement of the standard Breath Mask, the Rebreather also adds vigor-enhancing airborne stimulants to the regulated oxygen stream.”*

**Das'skar Hunting Mask** · `a_helmet_19` · K2 · Tier 3 · 19,000 credits · AttackBonus 1 · Ability (Dexterity) 1 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 2)* — *“Restricted: not useable by Wookiees Nikto bounty hunters often employ these masks to help them track down prey. Das'skar Hunting Masks were created by Hutts to improve the performance of their minions.”*

**Force Mask** · `a_helmet_20` · K2 · Tier 3 · 18,000 credits · DecreaseAbilityScore (Charisma) Penalty_-4 · DecreaseAbilityScore (Wisdom) Penalty_-4 · ImprovedMagicResist Bonus_16 · Saving throw +4 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees For both good and ill, this mask provides the wearer with some protection from the Force.”*

**Sith Mask** · `a_helmet_21` · K2 · Tier 4 · 1,000 credits · BonusFeats (Weapon Focus Lightsaber) · Use Limitation Feat (Armour Prof Heavy) · Immunity (MindSpells) 0 · Regeneration Force Points 1 — *“Restricted: not useable by Wookiees This mask blocks outside mental influence and other sensory noise, allowing the user to focus their abilities inward with no distraction.”*

**Stabilizer Mask** · `a_helmet_22` · K2 · Tier 3 · 5,500 credits · Use Limitation Feat (Armour Prof Medium) · Immunity (MindSpells) 0 · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* — *“Restricted: not useable by Wookiees This mask uses micro-bursts of electricity to regulate the user's mental patterns. It effectively fortifies both mind and body against attack.”*

**Matukai Meditation Band** · `a_helmet_23` · K2 · Tier 4 · 24,000 credits · Ability (Wisdom) 2 · DamageImmunity (Dark Side) ⚠ **DR 6** *(30%)* · Saving throw +2 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees An improved version of the standard meditation band, this item provides unparalleled protection from the ravaging power of the Dark Side.”*

**Target Assessor** · `a_helmet_24` · K2 · Tier 4 · 23,000 credits · AttackBonus 2 · Ability (Dexterity) 2 · BonusFeats (Precise Shot I) ⚠ attack chain · BonusFeats (Targeting 1) — *“Restricted: not useable by Wookiees Though perhaps not as potent as the multi-spectral version, this device requires no training to use.”*

**Circlet of Saresh** · `a_helmet_25` · K2 · Tier 4 · 9,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Ability (Wisdom) 5 — *“Restricted: not useable by Wookiees The wealthy Saresh family of Taris were once known as much for their arrogance and cruelty as for their vast riches and political power. But over the last century many of the family have shown a strong affinity to the Force, and been taken in by the Jedi for training. Foremost among these was Guun Han Saresh, heir to the family fortune. To celebrate Guun Han's acceptance into the Order, his father commissioned the crafting of a powerful headband: the Circlet of Saresh. To prevent this spectacular gift from leading his son down the path of arrogance and pride - an all too real possibility given the Saresh family history - the circlet was fashioned so that only one who is a true servant of the light can use it. The circlet was in Gunn Han's possession when he disappeared shortly after the time of the Great Hunt.”*

**Bindo's Band** ⚠ **UNIQUE** · `a_helmet_26` · K2 · Tier 4 · 22,250 credits · Ability (Charisma) 3 · DamageImmunity (Dark Side) ⚠ **DR 2** *(10%)* · DamageImmunity (Light Side) ⚠ **DR 2** *(10%)* — *“Restricted: not useable by Wookiees It is unknown whether this simple band was ever owned by the reclusive Jedi, but it is likely that Jolee would have appreciated its ability to help one walk the line between the Light and Dark Sides of the Force.”*

**Enhanced Shielding Visor** · `a_helmet_27` · K2 · Tier 4 · 24,750 credits · DamageImmunity (Electrical) ⚠ **DR 3** *(15%)* · DamageImmunity (Energy) ⚠ **DR 3** *(15%)* · DamageImmunity (Ion) ⚠ **DR 3** *(15%)* · Armor 3 · Use Limitation Feat (Armour Prof Medium) — *“Restricted: not useable by Wookiees A vastly improved version of the inexpensive shielding visor, this premium helmet provides physical protection from a variety of sources.”*

**Force Shield** · `a_helmet_28` · K2 · Tier 4 · 30,000 credits · DecreaseAbilityScore (Charisma) Penalty_-6 · DecreaseAbilityScore (Wisdom) Penalty_-6 · DamageResist (Dark Side) Resist_5/- · ImprovedMagicResist Bonus_24 · Saving throw +5 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees This helmet shields the wearer's mind from the Force. It is so potent and successful at its goal that Force sensitives are severely disoriented when they wear it.”*

**Absorption Visor** · `a_helmet_29` · K2 · Tier 4 · 32,000 credits · DamageImmunity (Electrical) ⚠ **DR 3** *(15%)* · DamageImmunity (Energy) ⚠ **DR 3** *(15%)* · DamageImmunity (Ion) ⚠ **DR 15** *(75%)* · DamageImmunity (Sonic) ⚠ **DR 18** *(90%)* · Armor 1 · Use Limitation Feat (Armour Prof Light) — *“Restricted: not useable by Wookiees A high-tech, combat-oriented modification of simple sonic nullifiers, this device provides near immunity to both sonic and ion attacks.”*

**Force Focusing Visor** · `a_helmet_30` · K2 · Tier 4 · 32,000 credits · Ability (Charisma) 1 · Ability (Wisdom) 4 · Regeneration Force Points 2 — *“Restricted: not useable by Wookiees Through means unknown, this visor helps the wearer clear their mind of distractions. It is especially potent when worn by a Force sensitive.”*

**⚠ Name corrupted in the source** · `g1_i_mask01` · K1 · Tier 3 · 6,000 credits · Use Limitation Feat (Armour Prof Light) · Immunity (MindSpells) 0 · Immunity (Poison) 0 · Saving throw +1 ⚠ *(which save is unresolved — subtype 0)* — ⚠ *Its name field carries unrelated text from elsewhere in the game’s string table; the properties above are the item’s own. Recorded, not renamed.*

**Medical Interface Visor** · `g1_i_mask02` · K1 · Tier 2 · 5,000 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +10 ⚠ *(which skill is unresolved — subtype 7)* — *“Similar in functionality to the Bio-Stabilizer series of medical equipment, this visor is designed to assist in the care and treatment of injured individuals. By providing constant data and analysis on the condition of t”* ⚠ *(description truncated in source)*

**Advanced Agent Interface** · `g1_i_mask03` · K1 · Tier 3 · 10,000 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +7 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +7 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +7 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +7 ⚠ *(which skill is unresolved — subtype 5)* · Skill bonus +7 ⚠ *(which skill is unresolved — subtype 6)* — *“A visor with an integrated computer and electronics analysis system, the Advanced Agent Interface uses a superior artificial intelligence routine to assist the wearer in all manner of covert and computer-oriented tasks.”*

**Light-Scan Visor** · `g_i_mask01` · K1 · Tier 1 · 75 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees These are invaluable tools that increase visual acuity by analyzing light on several frequencies above those of normal sight.”*

**Motion Detection Goggles** · `g_i_mask02` · K1 · Tier 1 · 100 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees A built-in micro tracking processor means a user wearing these goggles can detect almost any movement.”*

**Bothan Perception Visor** · `g_i_mask03` · K1 · Tier 2 · 1,000 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees Bothans treat information like any other resource, and invest a great deal in devices that help collect it. These Bothan visors are considered to be among the best in the galaxy.”*

**Verpine Ocular Enhancer** · `g_i_mask04` · K1 · Tier 2 · 750 credits · Ability (Dexterity) 1 · DamageResist (Sonic) Resist_5/- · Use Limitation Feat (Armour Prof Light) — *“Restricted: not useable by Wookiees The Verpine only manufacture this product for export, having no need of it themselves. They have highly evolved sight, a quality they smugly say the visors mimic but do not exceed.”*

**Bothan Sensory Visor** · `g_i_mask05` · K1 · Tier 1 · 150 credits · Use Limitation Feat (Armour Prof Light) · Immunity (Critical Hits) 0 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +3 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees Bothans place great importance on the tools of the information trade. They would consider these items to be of average quality, though their standards are exceptionally high.”*

**Vacuum Mask** · `g_i_mask06` · K1 · Tier 2 · 5,000 credits · Use Limitation Feat (Armour Prof Medium) · Immunity (MindSpells) 0 · Immunity (Poison) 0 — *“Restricted: not useable by Wookiees Intersystem travel is commonplace, but the inherent dangers should not be forgotten, especially in times of war. Many consider these to be essential equipment for spacefarers.”*

**Sonic Nullifiers** · `g_i_mask07` · K1 · Tier 1 · 100 credits · DamageResist (Sonic) Resist_10/- · Use Limitation Feat (Armour Prof Light) — *“Restricted: not useable by Wookiees Replacing bulky ear protection, these items make use of newly developed counterwave-nullifiers, an innovation pioneered by shipyard workers, not the military.”*

**Aural Amplifier** · `g_i_mask08` · K1 · Tier 1 · 50 credits · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees With this item, Durkish Corporation abandoned visual detection in favor of aural, citing that most creatures breathe, and even camouflage fields can't blend the sound of that away.”*

**Advanced Aural Amplifier** · `g_i_mask09` · K1 · Tier 1 · 400 credits · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees In a fine balancing act, this unit amplifies the faint sounds of moving creatures, while filtering out louder background noise that might otherwise deafen the user.”*

**Neural Band** · `g_i_mask10` · K1 · Tier 1 · 100 credits · Saving throw +2 ⚠ *(which save is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees Developed after the Exar Kun war, this item bolsters the willpower of the user by electrically reinforcing established mental patterns. Republic troops called it "Little Shocky".”*

**Verpine Headband** · `g_i_mask11` · K1 · Tier 1 · 200 credits · Saving throw +3 ⚠ *(which save is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 3)* — *“Restricted: not useable by Wookiees Not subject to Republic regulations, the Verpine increased neural band effectiveness with brute electrical force. The market is there, but long-term effects on users are unknown.”*

**Breath Mask** · `g_i_mask12` · K1 · Tier 1 · 100 credits · Use Limitation Feat (Armour Prof Medium) · Immunity (Poison) 0 — *“Restricted: not useable by Wookiees This is standard issue gear for Republic forces and most professional soldiers, protecting against a variety of gas-based attacks.”*

**Teta's Royal Band** ⚠ **UNIQUE** · `g_i_mask13` · K1 · Tier 2 · 3,000 credits · True Seeing 0 — *“Restricted: not useable by Wookiees This "royal band" is attributed to Empress Teta, a warrior leader of Cinnagar. She was instrumental in defeating the Sith in the Great Hyperspace War over a thousand years ago.”*

**Sith Mask** · `g_i_mask14` · K1 · Tier 2 · 1,000 credits · BonusFeats (Weapon Focus Lightsaber) · Use Limitation Feat (Armour Prof Heavy) · Immunity (MindSpells) 0 · Regeneration Force Points 1 — *“Restricted: not useable by Wookiees This mask blocks outside mental influence and other sensory noise, allowing the user to focus their abilities inward with no distraction.”*

**Stabilizer Mask** · `g_i_mask15` · K1 · Tier 3 · 5,500 credits · Use Limitation Feat (Armour Prof Medium) · Immunity (MindSpells) 0 · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* — *“Restricted: not useable by Wookiees This mask uses micro-bursts of electricity to regulate the user's mental patterns. It effectively fortifies both mind and body against attack.”*

**Interface Band** · `g_i_mask16` · K1 · Tier 2 · 1,000 credits · DamageResist (Sonic) Resist_5/- · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees This item provides a mental interface to a store of information on electronic systems common to security, demolitions, and general computing functions.”*

**Demolitions Sensor** · `g_i_mask17` · K1 · Tier 2 · 800 credits · Skill bonus +8 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* — *“Restricted: not useable by Wookiees This item uses advanced processors to assist the wearer in the visual analysis of microelectronics commonly used in demolitions. The acuity granted also serves to improve general awareness.”*

**Combat Sensor** · `g_i_mask18` · K1 · Tier 3 · 6,000 credits · Ability (Dexterity) 2 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) — *“Restricted: not useable by Wookiees The targeting software inherent in this visor uses predictive algorithms to direct the wearer's gaze, allowing them to function more efficiently in combat.”*

**Stealth Field Enhancer** · `g_i_mask19` · K1 · Tier 1 · 400 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* — *“Restricted: not useable by Wookiees A specialized espionage unit designed to get the most out of a stealth field generator by improving the user's perception of the field while in Stealth Mode.”*

**Stealth Field Reinforcement** · `g_i_mask20` · K1 · Tier 2 · 2,400 credits · Use Limitation Feat (Armour Prof Light) · Skill bonus +8 ⚠ *(which skill is unresolved — subtype 2)* — *“Restricted: not useable by Wookiees A very powerful item designed to both regulate stealth field emissions and improve the user's perception of the field while in Stealth Mode.”*

**Interface Visor** · `g_i_mask21` · K1 · Tier 2 · 1,500 credits · DamageResist (Sonic) Resist_5/- · Use Limitation Feat (Armour Prof Light) · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 0)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 1)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 6)* — *“Restricted: not useable by Wookiees This visor combines mental and visual interfaces to aid in the analysis of electronic systems common to security, demolitions, and general computing functions.”*

**Circlet of Saresh** · `g_i_mask22` · K1 · Tier 3 · 9,000 credits · Ability (Wisdom) 5 · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 — *“Restricted: not useable by Wookiees The wealthy Saresh family of Taris were once known as much for their arrogance and cruelty as for their vast riches and political power. But over the last century many of the family have shown a strong affinity to the Force, and been taken in by the Jedi for training. Foremost among these was Guun Han Saresh, heir to the family fortune. To celebrate Guun Han's acceptance into the Order, his father commissioned the crafting of a powerful headband: the Circlet of Saresh. To prevent this spectacular gift from leading his son down the path of arrogance and pride - an all too real possibility given the Saresh family history - the circlet was fashioned so that only one who is a true servant of the light can use it. The circlet was in Gunn Han's possession when he disappeared shortly after the time of the Great Hunt.”*

**Pistol Targetting Optics** · `g_i_mask23` · K1 · Tier 3 · 8,000 credits · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Spec Blaster) — *“This advanced optics and targetting system, worn as a mask, attaches to a held weapon, in this case pistol, and provides targetting information, distances, and tracking of potential targets within line of sight.”*

**Heavy Targetting Optics** · `g_i_mask24` · K1 · Tier 3 · 9,000 credits · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats ⚠ cut content · BonusFeats (Weapon Spec Blaster Rifle) · BonusFeats ⚠ cut content — *“This advanced optics and targetting system, worn as a mask, attaches to a held weapon, in this case rifles and heavy weapons, and provides targetting information, distances, and tracking of potential targets within line of sight.”*

**GenoHaradan Visor** · `geno_visor` · K1 · Tier 2 · 1,500 credits · Use Limitation Feat (Armour Prof Light) · Saving throw +3 ⚠ *(which save is unresolved — subtype 2)* · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 3)* · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 1)* — *“Restricted: not useable by Wookiees These visors hone a Genoharadan agent's senses, making them virtually impossible to catch unaware. The enhanced awareness also increases the agent's effectiveness in combat and in setting delicate, complex explosives.”*
