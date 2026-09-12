# Chapter Seven — Droid Equipment

**Everything a droid can be fitted with.** Like the armour and upgrade chapters before it,
these figures came straight from the games' own item files rather than through any summary.

**Droids do not wear armour and cannot use most of what Chapters Two through Six
catalogue.** This chapter is what they get instead.

---

## The eight categories

**129 items**, three appearing in both games.

| Category | Count | What it is |
|---|---|---|
| **Device** | 29 | Charge-limited combat items — stun, slow, flame, poison, ion effects, each consumed on use |
| **Interface** | 15 | Skill bonuses for computer-terminal interaction |
| **Named** | 10 | Unique droid-specific items, the equivalent of the unique weapons named throughout this book |
| **Plating** | 25 | Droid armour — the item-level equivalent of Chapter One's droid-plating formula |
| **Sensor** | 12 | Detection bonuses, including against Stealth |
| **Shield** | 13 | Timed energy absorption — a duration and a damage cap, not a passive bonus |
| **Spike-mount** | 7 | Computer and security bypass modules — see the note below |
| **Tool** | 18 | Combat-utility bonuses |

**Every device-category item, and most plating, carries a `Use Limitation Feat (Droid
Upgrade N)` property — the "bay gate", and it is a deliberate exception to how a feat
normally reaches a character.** A droid doesn't learn these the way an organic character
learns a feat; **the gate is the item requirement itself, not a separate feat purchase.**

## ⚠ One spike-mount item has a broken name in the game data

**The best item in the Spike-mount category is hard to find, because its name field is
corrupted.** It is the **Advanced Droid Interface** — `g1_i_drdcomspk01`, Tier 3, **9,000
credits**, and it requires `Droid Upgrade 3`.

**It grants skill 7 in Awareness, Computer Use, Demolitions and Security** — four bonuses
at once, which is why it costs what it does. Its own description calls it *"a
self-contained artificial intelligence system… to provide them with additional resources
useful in the bypassing of computer and conventional"* security.

> **If you are searching the game files for this item by name, you will not find it.
> Search the code instead.** **It is catalogued below under its real name.**

---

# The catalogue

**All 129 items, by category**, with resref, which game each comes from, tier, price,
properties and the item's own description.

## ⚠⚠ Two things to know before using it

**⚠ 1 — Forty-nine of these 129 rows had a property the data did not fully resolve, and the
skills among them are now named.** The commonest shape was a skill bonus whose *size* was
known and whose *skill* was not: **`Skill bonus +4`, and no name attached to it.** The games
store the skill as a numeric index, and that index had never been mapped back to a name.

**⚠ IT IS MAPPED NOW, FROM THE GAMES' OWN TABLE.** `skills.2da` is eight rows —
ComputerUse, Demolitions, Stealth, Awareness, Persuade, Repair, Security, TreatInjury — and
**both games ship it row for row identical**, so one mapping serves the whole chapter.
**Thirty-nine properties across thirty-three rows now carry a name.**

> **Nothing was resolved from the page.** Each index was read back off the item's own
> `.uti` and matched on **both** the subtype and the magnitude, so a margin that disagreed
> with its blueprint would have been reported rather than rewritten. None disagreed.

**⚠⚠ AND THE OTHER TWENTY-TWO ROWS RESOLVED TOO, FROM THE TABLE THE DATA ITSELF NAMES.**
`itempropdef` carries a `subtyperesref` column saying which 2DA each property's subtype
indexes — so nothing here was matched to a vocabulary by hand. Eight saving throws, ten
character-locks, four racial subtypes and one Defence type: **every marker in this chapter
is now a name.**

> **⚠ A SUBTYPE COLLIDES ACROSS VOCABULARIES, AND THE MARGIN IS WHAT SEPARATES THEM.**
> `Droid Energized Armor Mark II` carries `DamageResist` *and*
> `ImprovedSavingThrowsSpecific` both at subtype 1, so *"whatever this item calls 1"* is two
> answers. The margin names `iprp_savingthrow`, and the blueprint must actually carry a
> property indexing that table — **so the margin is checked rather than believed.**

**⚠ AND THE CHARACTER-LOCKS NAME THE DROIDS YOU WOULD EXPECT** — `G0-T0`, `HK-47`, `T3-M4`
— on a page of droid equipment, from `iprp_pc`, which nothing told the resolver to look
for.

**⚠ And one row proved the mapping was recoverable.** The `Advanced Droid Interface` carried
its four skills by name — **Awareness, Computer Use, Demolitions, Security** — where its
six neighbours in the same category carried bare indices. **The resolution existed. It had
simply not been applied to the rest.** It has been now, and that row was the check: its own
four indices — 3, 0, 1, 6 — resolve to exactly the four names it was already printing.

**⚠ 2 — This chapter's item total was wrong, and the catalogue is what corrected it.** The
count had stood at **135**. Counting the rows gives **129**, and every one of the eight
category figures above was already right and already summed to 129. **The total was the only
wrong number, and it disagreed with the table printed directly beneath it.**

---

## Device — 29

**⚠ Effects are the games' own and are not converted** — damage as flat points, durations in seconds, saves on the games' DC scale.

**Droid Neural Pacifier** · `d_device_01` · K2 · Tier 1 · 100 credits · Damage: None · On Hit: Stun, 100% for 9sec · Save: DC 15 to negate stun · Range: Medium · Charges: Using this item consumes one charge. This item is a · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: None On Hit: Stun, 100% for 9sec Save: DC 15 to negate stun Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This device fires a beam that is disruptive to the neural pathways of biological creatures.”*

**Droid Repulsor** · `d_device_02` · K2 · Tier 1 · 200 credits · Damage: None · On Hit: Slowed, 75% for 9sec · Save: DC15 to negate slow · Charges: Using this item consumes one charge. This item is automatically dis · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: None On Hit: Slowed, 75% for 9sec Save: DC15 to negate slow Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This technology is borrowed from the units that power repulsor-lifts and creates an artificial gravity wake around the droid, essentially randomizing the axis of the gravity surrounding its enemies and slowing them to a crawl.”*

**Droid Flame Thrower** · `d_device_03` · K2 · Tier 1 · 300 credits · Damage: Heat, 30pts · On Hit: Horror, 100% for 3sec · Special: Targets 7th level and up ignore horror effect · Save: DC15 for half damage · Range: Sho · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Heat, 30pts On Hit: Horror, 100% for 3sec Special: Targets 7th level and up ignore horror effect Save: DC15 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Designed for extermination and pest control, these devices can also be used on larger beings.”*

**Droid Neural Scrambler** · `d_device_05` · K2 · Tier 1 · 500 credits · Damage: None · On Hit: Stun, 100% for 9sec · Save: DC20 to negate stun · Range: Medium · Charges: Using this item consumes one charge. This item is au · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: None On Hit: Stun, 100% for 9sec Save: DC20 to negate stun Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. More powerful than the Pacifier, the Neural Scrambler is used to overload the victim's neural pathways to the point of loss of conciousness.”*

**Droid Ion Striker** · `d_device_06` · K2 · Tier 2 · 850 credits · Damage: Ion, 20pts · Range: Medium · Charges: Using this item consumes one charge. This item is automatically discarded after all available charges ar · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Ion, 20pts Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The Ion Striker is used by security droids to disable and destroy other droids, whether they be assassins or simply malfunctioning.”*

**Droid Molten Cannon** · `d_device_07` · K2 · Tier 2 · 800 credits · Damage: Fire, 60pts · On Hit: Horror, 100% for 3sec · Special: Targets 7th level and up ignore horror effect · Save: DC20 for half damage · Range: Sho · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Fire, 60pts On Hit: Horror, 100% for 3sec Special: Targets 7th level and up ignore horror effect Save: DC20 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. An upgrade of the standard flame thrower, this device actually shoots wide streams of liquid fire. There are few practical applications requiring such devices but they are sought after by military powers for their devastating effect on morale.”*

**Droid Carbonite Projector** · `d_device_08` · K2 · Tier 2 · 900 credits · Damage: Cold, 20pts · On Hit: Paralyze, 100% for 9sec · Save: DC15 for half damage, · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Cold, 20pts On Hit: Paralyze, 100% for 9sec Save: DC15 for half damage, paralyze reduced to 3sec Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Typically used for long-term storage of perishable goods, these tools can be turned on human targets with reasonable certainty of the outcome.”*

**Droid Plasma Thrower** · `d_device_09` · K2 · Tier 2 · 1,500 credits · Damage: Fire, Ion 60pts · Save: DC20 for half damage · Range: Short · Charges: Using this item consumes one charge. This item is automatically discard · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: Fire, Ion 60pts Save: DC20 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Ionized gas is pumped through this upgrade and burns through most known metals in seconds. Designed for rescue droids who sometimes need to make holes in starships' heavily armored hulls.”*

**Droid Bio-Assault Spray** · `d_device_10` · K2 · Tier 2 · 1,700 credits · Damage: None · On Hit: · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: None On Hit: Poisoned, Virulent Save: DC22 to negate slow Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Illegal in most civilized societies, the Bio-Assault Spray upgrade essentially breaks the target down at the molecular level, often leaving behind nothing more then a grey ooze.”*

**Droid Ion Blast Mark I** · `d_device_12` · K2 · Tier 2 · 1,975 credits · Damage: Ion, 15pts · On Hit: Stun, 100% for 12sec · Save: DC10 to ignore stun · Range: Short · Charges: Using this item consumes one charge. This item · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Ion, 15pts On Hit: Stun, 100% for 12sec Save: DC10 to ignore stun Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The "Scrambler" was developed by Aratech and marketed towards customers who were faced with massive droid armies. Sending a pulse of highly-charged ions, this weapon destroys the electronics of enemy droids.”*

**Droid Ion Blast Mark II** · `d_device_13` · K2 · Tier 2 · 2,150 credits · Damage: Ion, 15pts · On Hit: Stun, 100% for 12sec · Save: DC14 to ignore stun · Range: Short · Charges: Using this item consumes one charge. This item · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Ion, 15pts On Hit: Stun, 100% for 12sec Save: DC14 to ignore stun Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This version is equipped with a beam-splitter to allow the beam to be directed at multiple targets simultaneously.”*

**Droid Ion Blast Mark III** · `d_device_14` · K2 · Tier 2 · 2,500 credits · Damage: Ion, 30pts · On Hit: Stun, 100% for 12sec · Save: DC18 to ignore stun · Range: Medium · Charges: Using this item consumes two charges. This it · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: Ion, 30pts On Hit: Stun, 100% for 12sec Save: DC18 to ignore stun Range: Medium Charges: Using this item consumes two charges. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The Mark III is the most feared weapon by droid army commanders. There is a drawback in the unit's power consumption. The interal circuitry can only withstand a few shots before it destroys itself. This version is also equipped with a beam-splitter to allow the beam to be directed at multiple targets simultaneously.”*

**Mastercraft: Armor I Description** · `g1_i_drdutldev01` · K1 · Tier 2 · 3,000 credits · CastSpell ⚠ subtype dropped · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Mastercraft: Armor II Description”* ⚠ *(description truncated in source)*

**Mastercraft: Armor III Description** · `g1_i_drdutldev02` · K1 · Tier 2 · 3,000 credits · While not the most powerful of weapons, the Baragwin have modified a normal Stun Ray to run at such efficiency that it can tap into the power supply of the droid mounting · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“is not knocked down”* ⚠ *(description truncated in source)*

**is knocked down** · `g1_i_drdutldev03` · K1 · Tier 2 · 3,000 credits · CastSpell ⚠ subtype dropped · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate

**Blowtorch** · `g_d_blowtrch01` · K2 · Tier 1 · 100 credits · Damage: Heat, 6pts · Save: DC15 for half damage · Range: Short · Charges: Using this item consumes one charge. This item is automatically discarded af · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Heat, 6pts Save: DC15 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This droid-mounted acetylene blowtorch can be used as an improvised weapon, inflicting minor heat damage over an area.”*

**Advanced Blowtorch** · `g_d_blowtrch02` · K2 · Tier 1 · 200 credits · Damage: Heat, 12pts · Save: DC15 for half damage · Range: Short · Charges: Using this item consumes one charge. This item is automatically discarded a · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Heat, 12pts Save: DC15 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This droid-mounted advanced blowtorch can be used as an improvised weapon, inflicting heat damage over an area. While an industrial tool, its advanced hydrocarbon fuel is closer to military-grade incendiaries than the more common acetylene.”*

**Fire Suppression System** · `g_d_firesupres01` · K2 · Tier 1 · 150 credits · Damage: Cold, 10pts · On Hit: Paralyze, 25% for 6sec · Save: DC15 for half damage and ignore paralyze effect · Range: Short · Charges: Using this item · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Fire Suppression System Damage: Cold, 10pts On Hit: Paralyze, 25% for 6sec Save: DC15 for half damage and ignore paralyze effect Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This item uses a high-pressure agent to douse flames and cool critically overheating systems. The agent is comprised of two naturally occurring gasses and a synthetic compound similar to those used in carbonite freezing, producing a chemical stream cold enough to be used as an improvised weapon.”*

**Stun Ray** · `g_i_drdutldev001` · K1 · Tier 1 · 300 credits · Damage: None · On Hit: Stun, 100% for 9sec · Save: DC15 to negate stun · Range: Medium · Charges: Using this item consumes one charge. This item is au · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: None On Hit: Stun, 100% for 9sec Save: DC15 to negate stun Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Quellegh Industrial is becoming the standard in publicly traded non-lethal droid-mounted weapons. Company officials credit aggressive marketing towards any despot with credits.”*

**Advanced Stun Ray** · `g_i_drdutldev002` · K1 · Tier 2 · 900 credits · Damage: None · On Hit: Stun, 100% for 9sec · Save: DC20 to negate stun · Range: Medium · Charges: Using this item consumes one charge. This item is au · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: None On Hit: Stun, 100% for 9sec Save: DC20 to negate stun Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This product is a special order aftermarket modification of a Quellegh Industrial stun ray. Very expensive to produce, most are in the hands of government-sponsored elite troops.”*

**Shield Disruptor** · `g_i_drdutldev003` · K1 · Tier 1 · 300 credits · Damage: Ion, 20pts · Range: Medium · Charges: Using this item consumes one charge. This item is automatically discarded after all available charges ar · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Damage: Ion, 20pts Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Designed for Republic forces, these devices allow a droid to potentially devastate opponent droids or the personal shielding of an enemy, though the energy drain is quite large.”*

**Advanced Shield Disruptor** · `g_i_drdutldev004` · K1 · Tier 2 · 900 credits · Damage: Ion, 40pts · Range: Medium · Charges: Using this item consumes one charge. This item is automatically discarded after all available charges ar · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Ion, 40pts Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Prototyped by Czerka Corporation, these extremely devastating droid and shield nullifiers have found their way to forces on both sides of the Sith/Republic conflict.”*

**Oil Slick** · `g_i_drdutldev005` · K1 · Tier 2 · 1,500 credits · A thin film of oil across the path of the enemy can slow their progress, allowing allies to retreat or engage them at range. · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“This is a simple, yet effective, upgrade for any droid. A thin film of oil across the path of the enemy can slow their progress, allowing allies to retreat or engage them at range.”*

**Flame Thrower** · `g_i_drdutldev006` · K1 · Tier 1 · 300 credits · Damage: Heat, 30pts · On Hit: Horror, 100% for 3sec · Special: Targets 7th level and up ignore horror effect · Save: DC15 for half damage · Range: Sho · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Heat, 30pts On Hit: Horror, 100% for 3sec Special: Targets 7th level and up ignore horror effect Save: DC15 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This droid-mounted weapon can inflict damage over a broad area. The incendiary compounds within border on military quality, though the unit was initially designed for industrial purposes.”*

**Advanced Flame Thrower** · `g_i_drdutldev007` · K1 · Tier 2 · 900 credits · Damage: Heat, 60pts · On Hit: Horror, 100% for 3sec · Special: Targets 7th level and up ignore horror effect · Save: DC20 for half damage · Range: Sho · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: Heat, 60pts On Hit: Horror, 100% for 3sec Special: Targets 7th level and up ignore horror effect Save: DC20 for half damage Range: Short Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Intended as a combat upgrade and not generally avaliable to the public, this droid-mounted weapon can inflict a great deal of damage over a broad area. It is widely used by Republic forces.”*

**Carbonite Projector** · `g_i_drdutldev008` · K1 · Tier 1 · 300 credits · Damage: Cold, 20pts · On Hit: Paralyze, 100% for 9sec · Save: DC15 for half damage, · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: Cold, 20pts On Hit: Paralyze, 100% for 9sec Save: DC15 for half damage, paralyze reduced to 3sec Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. The inverse of a flamethrower, this weapon uses a carbonite freezing technique to super-cool synthetic compounds hurled at a target. This unconventional weapon has not yet seen widespread use.”*

**Carbonite Projector Mark II** · `g_i_drdutldev009` · K1 · Tier 2 · 900 credits · Damage: Cold, 40pts · On Hit: Paralyze, 100% for 15sec · Save: DC20 for half damage, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: Cold, 40pts On Hit: Paralyze, 100% for 15sec Save: DC20 for half damage, paralyze reduced to 9sec Range: Medium Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. Like the basic model, this weapon uses a carbonite freezing technique to super-cool synthetic compounds hurled at a target, though more efficient projectors make it far more effective.”*

**Gravity Generator** · `g_i_drdutldev010` · K1 · Tier 1 · 500 credits · Damage: None · On Hit: Slowed, 75% for 9sec · Save: DC15 to negate slow · Charges: Using this item consumes one charge. This item is automatically dis · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Damage: None On Hit: Slowed, 75% for 9sec Save: DC15 to negate slow Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. These devices allow a droid to create localized gravity swells, the reverse effect of a repulsorlift engine. This can seemingly increase the weight of an enemy, slowing their movement.”*

**Adv. Gravity Generator** · `g_i_drdutldev011` · K1 · Tier 2 · 1,100 credits · Damage: None · On Hit: Slowed, 100% for 9sec · Save: DC20 to negate slow · Charges: Using this item consumes one charge. This item is automatically di · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Damage: None On Hit: Slowed, 100% for 9sec Save: DC20 to negate slow Charges: Using this item consumes one charge. This item is automatically discarded after all available charges are consumed. Items that have charges do not stack in inventory. This device creates a more powerful gravity swell than the basic unit due to an unregulated energy governor. The use of such items is discouraged because of concern over environmental effects.”*

## Interface — 15

**Droid Optimized Interface** · `d_interface_01` · K2 · Tier 1 · 50 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Computer Use) 2 — *“This interface is streamlined for more efficient, and thus more effective, interactions with computer terminals.”*

**Droid Stabilization Subroutine** · `d_interface_02` · K2 · Tier 1 · 100 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Demolitions) 4 — *“This module provides extra computing power for the droid's motivators and actuators, allowing it to make smoother and more subtle movements... two very handy things to have when disarming a mine.”*

**Droid Machine Interface** · `d_interface_03` · K2 · Tier 1 · 300 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Repair) 4 — *“This interface is designed to interact with most standard types of droids, machines, and equipment, allowing complex and detailed analysis of problems to be sent to the droid for reference.”*

**Droid Lockout Bypass** · `d_interface_04` · K2 · Tier 2 · 850 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Computer Use) 3 · Skill (Security) 3 — *“This interface is designed to bypass most standard lock-out and security measures common for mass-produced terminals and locks.”*

**Droid Parabolic Guides** · `d_interface_05` · K2 · Tier 2 · 1,100 credits · Ability (Dexterity) 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · ImprovedSavingThrowsSpecific (953) 2 — *“These modifications tie directly into the droid's sensors and provides multiple trajectory possibilities and solutions for munitions fired at the droid.”*

**Droid Motivator Booster** · `d_interface_06` · K2 · Tier 2 · 1,700 credits · Ability (Dexterity) 1 · Armor 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“This module ties directly in with a droid's motivators, increasing their output drastically. Even the most sluggish droids will show a marked improvement.”*

**Droid Durability Upgrade** · `d_interface_07` · K2 · Tier 2 · 2,900 credits · Ability (Constitution) 1 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · ImprovedSavingThrowsSpecific (951) 2 — *“This module increases the droid's survivability by creating redundant programs and upgrading the self-repair software.”*

**Droid Agility Upgrade** · `d_interface_08` · K2 · Tier 2 · 4,700 credits · Ability (Dexterity) 3 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · ImprovedSavingThrowsSpecific (953) 2 — *“This module increases the droid's agility by creating new programs to run its motivators and increase their reaction time.”*

**Droid Wisdom Upgrade** · `d_interface_09` · K2 · Tier 3 · 7,600 credits · Ability (Wisdom) 2 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · ImprovedSavingThrowsSpecific (952) 2 — *“This module increases the droid's reasoning and self-identity by removing most of the factory-installed safety restrictions put in place during its manufacture.”*

**Droid Exchange Interface** · `d_interface_10` · K2 · Tier 3 · 12,000 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Computer Use) 3 · Skill (Security) 6 — *“This interface solves the problem of unknown access codes - if you can find it on the black market.”*

**Droid Remote Interface** · `d_interface_11` · K2 · Tier 3 · 14,800 credits · DecreasedSkill (Awareness) Penalty_-3 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Security) 10 — *“This interface uses a wire-free signal to completely bypass security hardware and countermeasures. This signal takes much of the droid's power to maintain, however, and a loss of cognitive awareness is the result.”*

**Droid Anatomy Library** · `d_interface_12` · K2 · Tier 3 · 18,000 credits · AttackBonusRacialGroup (Human) 3 · DamageRacialGroup (Human) 1d10 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“This upgrade provides the droid with numerous files and other reference material relating to the anatomy of humanoid creatures, giving the droid an intimate knowledge of their strengths and weaknesses.”*

**Droid Scavenger Upgrade** · `d_interface_13` · K2 · Tier 3 · 20,000 credits · Ability (Constitution) 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Immunity (Critical Hits) 0 · ImprovedSavingThrowsSpecific (951) 3 · Skill (Repair) 5 — *“This upgrade enhances your droid's self-diagnostics and self-repair capability, allowing it to sustain itself by scavenging parts from the environment as well as its own non-critical systems.”*

**Droid Source Ripper** · `d_interface_14` · K2 · Tier 4 · 25,000 credits · ArmorRacialGroup (Droid) 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Computer Use) 10 — *“This interface allows the droid to see the original coding used to create a computer system, thus allowing unprecedented access to sub-systems that even the programmer might not have known to exist.”*

**Droid Systems Upgrade** · `d_interface_15` · K2 · Tier 4 · 28,880 credits · Ability (Constitution) 2 · Ability (Dexterity) 4 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Using higher mathematics and an advanced binary languages, this upgrade completely re-writes the droid's system software to be more efficient, more powerful, and much faster.”*

## Named — 10

**⚠ These are character-locked in the source.** Chapter Fourteen treats them as a template for unique droid gear rather than as three specific characters, since a KOTOR-era campaign has no `HK-47`.

**Droid Stealth Booster** · `d_g0t0_01` · K2 · Tier 3 · 6,000 credits · (G0-T0) · Skill (Stealth) 5 — *“This unit coaxes more power out of existing stealth unit circuitry, improving its effect notably.”*

**Droid Omniscience Unit** · `d_g0t0_02` · K2 · Tier 3 · 6,000 credits · AttackBonus 3 · Immunity (Critical Hits) 0 · (G0-T0) · Skill (Awareness) 10 · Skill (Demolitions) 5 — *“This sensor array has unique technology that allows the droid to basically know what is going on around it at all times.”*

**Droid Singulararity Projector** · `d_g0t0_03` · K2 · Tier 3 · 6,000 credits · BonusFeats (Cautious) · BonusFeats (Improved Caution) · BonusFeats (Master Caution) · (G0-T0) · Skill (Stealth) 10 — *“While it is unknown where the technology came from to create such a device on such a small scale, the outcome is well worth any possible compatability dangers. This unit actually folds space around the droid, making it not only appear to be gone, but actually ripping it out of normal space... the droid *is* gone.”*

**Goto Targeting Module** · `d_g0t0_04` · K2 · Tier 2 · 4,000 credits · BonusFeats (Improved Power Blast) ⚠ attack chain · BonusFeats (Improved Rapid Shot) ⚠ attack chain · BonusFeats (Improved Sniper Shot) ⚠ attack chain · BonusFeats (Power Blast) ⚠ attack chain · BonusFeats (Rapid Shot) ⚠ attack chain · BonusFeats (Sniper Shot) ⚠ attack chain · (G0-T0) — *“This droid auxiliary processor provides exceptional ranged combat abilities.”*

**Droid Assassin's Rifle** ⚠ **UNIQUE** · `d_hk47_01` · K2 · Tier 1 · 500 credits · 1d10, 18–20 ×2 · AttackBonus 5 · BonusFeats (Improved Sniper Shot) ⚠ attack chain · BonusFeats (Master Sniper Shot) ⚠ attack chain · BonusFeats (Sniper Shot) ⚠ attack chain · Massive Criticals 2d10 · (HK-47) — *“This disruptor has all the modifications an assassin droid needs: improved optics, reduced recoil, extended range, and several open ports for even more modular upgrades.”*

**Droid Capacitor Armor** · `d_hk47_02` · K2 · Tier 3 · 6,000 credits · DamageImmunity (Electrical) ⚠ **DR 15** *(75%)* · DamageImmunity (Energy) ⚠ **DR 15** *(75%)* · DamageImmunity (Ion) ⚠ **DR 15** *(75%)* · Armor 4 · (HK-47) — *“Based on an inverse architecture of Energized Armor, Capacitor Armor actually absorbs incoming energy and converts it into usable power for the droid's internal power source. The rest of the energy is dissipated harmlessly into the environment around the droid.”*

**Droid Assassination Module** · `d_hk47_03` · K2 · Tier 3 · 6,000 credits · AttackBonus 3 · BonusFeats ⚠ cut content · BonusFeats ⚠ cut content · BonusFeats ⚠ cut content · BonusFeats (Targeting 1) · BonusFeats (Targeting 2) · BonusFeats (Targeting 3) · (HK-47) — *“Not much is known about the inner-workings of these modules, but one thing is for certain: they work.”*

**Droid Shock Arm** ⚠ **UNIQUE** · `d_t3m4_01` · K2 · Tier 1 · 1 credits · Damage: Special, Electricity. · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · (T3-M4) — *“Damage: Special, Electricity. This unit is a popular upgrade for utility droids in that it is well hidden among the droid's other tools and delivers quite a jolt to the unsuspecting victim. The victim suffers 1-6 points of damage for each of the attacking droid's levels, to a maximum of 10 levels (10-60 points). A successful Fortitude save by the target at a DC of 5 + the attacking character's level reduces damage by half.”*

**Droid Self-Sustaining Unit** · `d_t3m4_02` · K2 · Tier 3 · 6,000 credits · BonusFeats (Regenerate Vitality Points) · (T3-M4) · Regeneration 3 — *“By reprogramming its internal systems, this upgrade takes the droid's built-in diagnostic routines to the next step: self-repair. Through several, closely-guarded processes, the droid can actually sustain and repair itself, regardless of availability of repair kits.”*

**Droid Renewable Shield** · `d_t3m4_03` · K2 · Tier 1 · 200 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · (T3-M4) — *“Absorbs: Energy, Sonic, Cold, Heat, Ion 80pts total Duration: 200 seconds, or max damage taken Through a complex ambient-energy collection system, these shields can be maintained and renewed without the replacement of the unit, allowing for this shield to be raised and lowered a near infinite amount of times.”*

## Plating — 25

**Droid Impact Armor Mark I** · `d_armor_01` · K2 · Tier 1 · 80 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Impact armor is designed to help absorb some of the wear-and-tear droids can take in an active workplace and save the chassis from major damage. Little more than a dust cover for the internal components of droids, Mark I is still a considerable improvement over nothing.”*

**Droid Modular Plating Mark I** · `d_armor_02` · K2 · Tier 1 · 130 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Modular Plating was designed as a light-weight yet durable substitute for heavier, more cumbersome armor. The Mark I series is used primarily in droids in diplomatic situations where discretion is more important than defense.”*

**Droid Impact Armor Mark II** · `d_armor_03` · K2 · Tier 1 · 400 credits · Armor 1 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Impact armor is designed to help absorb some of the wear-and-tear droids can take in an active workplace and save the chassis from major damage. The first in the series to be seriously considered armor, the Mark II provides a decent, uniform covering.”*

**Droid Desh Plating** · `d_armor_04` · K2 · Tier 2 · 770 credits · Ability (Dexterity) 1 · Defence penalty -3 (armour) · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Desh is a very flexible, but less sturdy metal. When combined with another metal, it provides cost-effective way to protect droids. This armor uses a desh and maranium alloy that cuts the weight and expense, but at a cost to the durability.”*

**Droid Impact Armor Mark III** · `d_armor_05` · K2 · Tier 2 · 1,250 credits · Armor 3 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Impact armor is designed to help absorb some of the wear-and-tear droids can take in an active workplace and save the chassis from major damage. Mark III is the best protection available for non-combat droids and increases their survivability in hostile situations.”*

**Droid Modular Plating Mark II** · `d_armor_06` · K2 · Tier 2 · 1,950 credits · Armor 2 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Modular Plating was designed as a light-weight yet durable substitute for heavier, more cumbersome armor. The Mark II has become the standard given its high protection versus weight ratio and is used in almost every droid army.”*

**Droid Modular Plating Mark III** · `d_armor_07` · K2 · Tier 2 · 3,000 credits · Armor 3 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Modular Plating was designed as a light-weight yet durable substitute for heavier, more cumbersome armor. The Mark III is the pinnacle of light-weight, high-impact protection using exotic materials and highly-detailed manufacturing techniques.”*

**Droid Agrinium Armor** · `d_armor_08` · K2 · Tier 2 · 4,775 credits · DamageImmunity (Electrical) ⚠ **DR 10** *(50%)* · DamageImmunity (Energy) ⚠ **DR 10** *(50%)* · DamageImmunity (Fire) ⚠ **DR 10** *(50%)* · Armor 2 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Agrinium is used to create solar sails and is highly resilient to all forms of radiation. Applied to droid armor, it creates a highly effective barrier against many forms of damage. This armor is used on light-weight repair droids that maintain the sails on deep space sail ships.”*

**Droid Dura Plating Mark I** · `d_armor_09` · K2 · Tier 3 · 7,750 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Originally used on starship hulls, durasteel is the most cost-effective way to prevent the destruction of your droids. Mark I is the standard heavy armor used in large military droids and vehicles.”*

**Droid Quadranium Armor** · `d_armor_10` · K2 · Tier 3 · 12,500 credits · DamageImmunity (Electrical) ⚠ **DR 5** *(25%)* · DamageImmunity (Energy) ⚠ **DR 5** *(25%)* · DamageImmunity (Fire) ⚠ **IMMUNE** *(100%)* · DamageImmunity (Sonic) ⚠ **DR 5** *(25%)* · Armor 3 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Quadranium is an incredibly strong element used in the manufacture of starship fuel tanks. It was first applied to droid armor by Aratech during the development of droids that could be sent to clean starship engines and fuel tanks without sustaining any damage.”*

**Droid Dura Plating Mark II** · `d_armor_11` · K2 · Tier 3 · 14,850 credits · Armor 1 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Originally used on starship hulls, durasteel is the most cost-effective way to prevent the destruction of your droids. Mark II is the heaviest mass-production armor available on the open market.”*

**Droid Diatium Plating** · `d_armor_12` · K2 · Tier 3 · 18,550 credits · DecreaseAbilityScore (Dexterity) Penalty_-2 · DamageImmunity (Bludgeoning) ⚠ **DR 15** *(75%)* · DamageImmunity (Piercing) ⚠ **DR 15** *(75%)* · DamageImmunity (Slashing) ⚠ **DR 15** *(75%)* · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Diatium is used in the construction of armor sheets that protect vital military installations and structures that are in close proximity to asteroid fields. Prohibatively heavy and expensive to shape on such a small scale, Diatium droid armor is very rarely made.”*

**Droid Energized Armor Mark I** · `d_armor_13` · K2 · Tier 4 · 22,250 credits · Armor 3 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · ImprovedSavingThrowsSpecific (951) 5 — *“Energized armor draws on the droid's power source and applies a current through a specially designed matrix on this armor. This energy matrix binds the molecules of the armor together to create a nearly inpenetrable physical barrier. Extremely difficult to manufacture, energized armor takes years to produce, thus making this the most expensive droid armor on the open market.”*

**Droid Energized Armor Mark II** · `d_armor_14` · K2 · Tier 4 · 26,650 credits · DamageResist (Bludgeoning) Resist_5/- · DamageResist (Piercing) Resist_5/- · DamageResist (Slashing) Resist_5/- · Armor 4 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · ImprovedSavingThrowsSpecific (951) 5 — *“Energized armor draws on the droid's power source and applies a current through a specially designed matrix on this armor. This energy matrix binds the molecules of the armor together to create a nearly inpenetrable physical barrier. Extremely difficult to manufacture, energized armor takes years to produce, thus making this the most expensive droid armor on the open market.”*

**Droid Energized Armor Mark III** · `d_armor_15` · K2 · Tier 4 · 29,905 credits · DamageResist (Bludgeoning) Resist_10/- · DamageResist (Piercing) Resist_10/- · DamageResist (Slashing) Resist_10/- · Armor 5 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · ImprovedSavingThrowsSpecific (951) 5 — *“Energized armor draws on the droid's power source and applies a current through a specially designed matrix on this armor. This energy matrix binds the molecules of the armor together to create a nearly inpenetrable physical barrier. Extremely difficult to manufacture, energized armor takes years to produce, thus making this the most expensive droid armor on the open market.”*

**Lock** · `g1_i_drdhvplat01` · K1 · Tier 2 · 3,000 credits · Armor 4 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate

**Droid Heavy Plating Type 1** · `g_i_drdhvplat001` · K1 · Tier 2 · 1,250 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Originally used on starship hulls, durasteel is the best protection available for droids. This particular variant of the alloy is the standard for mass-production heavy combat droids.”*

**Droid Heavy Plating Type 2** · `g_i_drdhvplat002` · K1 · Tier 2 · 1,500 credits · Armor 1 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“A specialized variant of heavy plating, this type of durasteel alloy is not sold in mass quantities. More often, it is used to equip elite troops where the initial cost of the battle droid warrants the investment.”*

**Droid Heavy Plating Type 3** · `g_i_drdhvplat003` · K1 · Tier 2 · 2,000 credits · Armor 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“The heaviest protection available, this type of plating is uncommon due to the cost involved in production. It is best suited to specialized assassin or assault droids, though such units are highly regulated.”*

**Droid Light Plating Type 1** · `g_i_drdltplat001` · K1 · Tier 1 · 75 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“A thin sheet of alloy plating is a relatively inexpensive way to improve a droid's chance of surviving combat. This model is an excellent option for light-duty droids.”*

**Droid Light Plating Type 2** · `g_i_drdltplat002` · K1 · Tier 1 · 150 credits · Armor 1 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Though more for the factory floor, plating of this type is seeing more general use. Light but effective, this upgrade can mean the difference between repair and replacement if a droid comes to harm.”*

**Droid Light Plating Type 3** · `g_i_drdltplat003` · K1 · Tier 1 · 250 credits · Armor 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“The strongest of the light-grade plating, this is the best protection most individuals consider purchasing for droids not actively in a class intended for combat.”*

**Droid Medium Plating Type 1** · `g_i_drdmdplat001` · K1 · Tier 1 · 500 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Developed by engineer Hoot Calin, this plating relies more on deflecting angles than exotic alloys. Cost can be prohibitive, though this is the most affordable model of the type.”*

**Droid Medium Plating Type 2** · `g_i_drdmdplat002` · K1 · Tier 2 · 750 credits · Armor 1 · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“This version of the Calin Industries plating system signaled a company shift in production from construction droids to military models. It now sees use on many different worlds.”*

**Droid Medium Plating Type 3** · `g_i_drdmdplat003` · K1 · Tier 2 · 1,000 credits · Armor 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“To solidify its place in the market, Calin Industries introduced this specialty variant of their medium plating system. Only heavy plating protects better, though the cost is prohibitive for some.”*

## Sensor — 12

**Droid Motion Sensors Type 1** · `g_i_drdmtnsen001` · K1 · Tier 1 · 50 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Awareness) 2 — *“These devices allow a droid to better detect creatures hidden by stealth fields. This basic model is the most inexpensive of the type, and is commonly available on many worlds.”*

**Droid Motion Sensors Type 2** · `g_i_drdmtnsen002` · K1 · Tier 1 · 100 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Awareness) 4 — *“This sensor package greatly enhances droid vision, increasing the likelihood of detecting creatures hidden by stealth fields. This model is marketed mainly to manufacturers of sentry and combat droids.”*

**Droid Motion Sensors Type 3** · `g_i_drdmtnsen003` · K1 · Tier 1 · 200 credits · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Awareness) 6 — *“Incorporating the most sophisticated sensors available, this model of upgrade is usually purchased for special-duty droids guarding sensitive materials or galactic heads of state.”*

**Droid Sonic Sensors Type 1** · `g_i_drdsncsen001` · K1 · Tier 1 · no sale value · Skill (Awareness) 2 — *“These devices allow detection of hidden or visually camouflaged intruders. Better quality sensors provide more sensitive background noise filtering to improve performance.”*

**Droid Sonic Sensors Type 2** · `g_i_drdsncsen002` · K1 · Tier 1 · no sale value · Skill (Awareness) 3 — *“These devices allow detection of hidden or visually camouflaged intruders. Better quality sensors provide more sensitive background noise filtering to improve performance.”*

**Droid Sonic Sensors Type 3** · `g_i_drdsncsen003` · K1 · Tier 1 · no sale value · Skill (Awareness) 4 — *“These devices allow detection of hidden or visually camouflaged intruders. Better quality sensors provide more sensitive background noise filtering to improve performance.”*

**Basic Targeting Computer** · `g_i_drdtrgcom001` · K1 · Tier 1 · 500 credits · BonusFeats (Weapon Focus Blaster) · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Battle droids come factory-ready for combat, but it is still wise to invest in targeting computer upgrades to optimize performance at range. Cost rises with quality, as always.”*

**Advanced Targeting Computer** · `g_i_drdtrgcom002` · K1 · Tier 2 · 1,500 credits · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Meant for droids that see regular combat, this targeting unit improves on the basic model and greatly increases battlefield performance.”*

**Superior Targeting Computer** · `g_i_drdtrgcom003` · K1 · Tier 2 · 2,000 credits · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats (Weapon Spec Blaster) · BonusFeats (Weapon Spec Blaster Rifle) · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Reserved for the highest quality battle droids, targeting units of this type are rarely seen outside of military operations.”*

**Sensor Probe** · `g_i_drdtrgcom004` · K1 · Tier 1 · 500 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Demolitions) 2 — *“This basic probe improves a droid's demolitions capabilities, allowing for more sensitive adjustments of volatile substances. A droid must have basic Demolitions software (paid points into the skill) to benefit from this item.”*

**Verpine Demolitions Probe** · `g_i_drdtrgcom005` · K1 · Tier 2 · 1,000 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Demolitions) 4 — *“Wartime contracts over the last forty years saw a great deal of money poured into Verpine droid modifications, particularly in the area of demolitions. A droid must have basic Demolitions software (paid points into the skill) to benefit from this item.”*

**Bothan Demolitions Probe** · `g_i_drdtrgcom006` · K1 · Tier 2 · 1,500 credits · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Demolitions) 6 — *“Concerning demolitions, the Bothans prefer well-equipped droids for the task of explosives management, and invest research accordingly. A droid must have basic Demolitions software (paid points into the skill) to benefit from this item.”*

## Shield — 13

**⚠ A duration and a damage cap, not a passive bonus** — and both figures are the games' own.

**Droid Deflector Mark I** · `d_shield_01` · K2 · Tier 1 · 200 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Absorbs: Energy, Electric, Ion 50pts Duration: 200 seconds, or max damage taken Deflectors provide limited protection against all types of energy. Mark I shields are used primarily by astromech droids to protect their chassis from the particulate radiation they come into contact with when exposed to open space.”*

**Droid Deflector Mark II** · `d_shield_02` · K2 · Tier 1 · 400 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Absorbs: Energy, Electric, Ion 70pts Duration: 200 seconds, or max damage taken Deflectors provide limited protection against all types of energy. Mark II are more robust than the Mark I, allowing a droid to stay exposed to space, even when passing close to stars.”*

**Droid Defense Barrier** · `d_shield_03` · K2 · Tier 2 · 600 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Absorbs: Energy, Sonic, Cold, Heat, Ion 60pts total Duration: 200 seconds, or max damage taken The Droid Defense Barrier is the standard for units in droid armies, providing decent protection at a reasonable cost to the buyer.”*

**Droid Energy Collector** · `d_shield_04` · K2 · Tier 2 · 800 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Absorbs: Energy, Sonic, Cold, Heat, Ion 80pts total Duration: 200 seconds, or max damage taken Initially designed to resist the harsh conditions of factory floors, these shields provide a droid with basic protection against a broad array of effects. The power drain is significant, however, and they must be replaced regularly.”*

**Droid Deflector Mark III** · `d_shield_05` · K2 · Tier 2 · 975 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Absorbs: Energy, Electric, Ion 100pts Duration: 200 seconds, or max damage taken Deflectors provide limited protection against all types of energy. The Mark III is the most cost-effective of the heavy droid shielding systems, providing decent protection from focused energy.”*

**Droid Unity Grid** · `d_shield_06` · K2 · Tier 2 · 1,350 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Absorbs: Energy, Sonic, Cold, Heat, Ion 110pts total Duration: 200 seconds, or max damage taken This shielding module creates overlapping shield vectors and then unifies them into a single shield, greatly increasing its absorption capacity as a result.”*

**Search** · `g1_i_drdshld001` · K1 · Tier 2 · 4,000 credits · CastSpell ⚠ subtype dropped · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Droid Interface”* ⚠ *(description truncated in source)*

**Energy Shield Level 1** · `g_i_drdshld001` · K1 · Tier 1 · 300 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Deflection: Energy, 20pts Duration: 200 seconds, or max damage taken This is a basic model energy shield universally applicable to most droids. The power drain is significant, however, and units like this must be replaced regularly.”*

**Energy Shield Level 2** · `g_i_drdshld002` · K1 · Tier 1 · 450 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Deflection: Energy, 30pts Duration: 200 seconds, or max damage taken Upgraded from the basic portable energy shield, these units are marketed to companies and governments that keep large standing forces of combat droids. The power drain is significant, however, and they must be replaced regularly.”*

**Energy Shield Level 3** · `g_i_drdshld003` · K1 · Tier 2 · 700 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Deflection: Energy, 50pts Duration: 200 seconds, or max damage taken This sophisticated item is designed for top quality combat droids, and produces superior protection for any droid with the necessary software to install it. The power drain is significant, however, and it must be replaced regularly.”*

**Environment Shield Level 1** · `g_i_drdshld005` · K1 · Tier 1 · 350 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“Deflection: Energy, Sonic, Cold, Heat, 20pts total Duration: 200 seconds, or max damage taken Initially designed to resist the harsh conditions of factory floors, these shields provide a droid with basic protection against a broad array of effects. The power drain is significant, however, and they must be replaced regularly.”*

**Environment Shield Level 2** · `g_i_drdshld006` · K1 · Tier 1 · 500 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“Deflection: Energy, Sonic, Cold, Heat, 30pts total Duration: 200 seconds, or max damage taken This unit is an aftermarket modification of the shielding typically found on deep-core mining droids. It provides broad protection against many effects, but the power drain is significant and it must be replaced regularly.”*

**Environment Shield Level 3** · `g_i_drdshld007` · K1 · Tier 2 · 900 credits · Duration: 200 seconds, · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“Deflection: Energy, Sonic, Cold, Heat, 50pts total Duration: 200 seconds, or max damage taken This variant of environmental shielding is designed for frontline combat droids. It provides broad protection against many effects, but the power drain is significant and it must be replaced regularly.”*

## Spike-mount — 7

**Advanced Droid Interface** · `g1_i_drdcomspk01` · K1 · Tier 3 · 9,000 credits · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Awareness) 7 · Skill (Computer Use) 7 · Skill (Demolitions) 7 · Skill (Security) 7 — *“A self-contained artificial intelligence system, this module can be equipped on droids to provide them with additional resources useful in the bypassing of computer and conventional security systems. This AI extends the current capabilities of the mounting droid to a level typically only seen on military espionage droids.”*

**Computer Probe** · `g_i_drdcomspk001` · K1 · Tier 1 · 500 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Computer Use) 2 — *“This retractable probe allows droid access to the higher programming functions of any computer terminal. Better quality probes provide cleaner access, increasing functionality.”*

**Universal Computer Interface** · `g_i_drdcomspk002` · K1 · Tier 2 · 1,500 credits · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Computer Use) 6 — *“The best and most expensive of its type available, this retractable probe allows droid access to the higher programming functions of any computer terminal.”*

**Advanced Computer Tool** · `g_i_drdcomspk003` · K1 · Tier 2 · 1,000 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Computer Use) 4 — *“Like the basic unit, this retractable probe allows droid access to the higher programming functions of any computer terminal, though better interface adapters make it more effective.”*

**Security Interface Tool** · `g_i_drdsecspk001` · K1 · Tier 1 · 500 credits · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Security) 2 — *“Pioneered by Toshan Gant, this is the basic droid security breaker in use across the galaxy. Gant did most of his research for the Republic military after private efforts led to his imprisonment. A droid must have basic Security software (paid points into the skill) to benefit from this item.”*

**Security Domination Interface** · `g_i_drdsecspk002` · K1 · Tier 2 · 1,500 credits · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Security) 6 — *“Modified on the aftermarket, this Toshan Gant security breaker is the best available. A droid must have basic Security software (paid points into the skill) to benefit from this item.”*

**Security Decryption Interface** · `g_i_drdsecspk003` · K1 · Tier 1 · 100 credits · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate · Skill (Security) 4 — *“This model of security breaker is no longer in production. It was an effective option before the factories of Toshan Gant took over the market. A droid must have basic Security software (paid points into the skill) to benefit from this item.”*

## Tool — 18

**Droid Motion Tracker** · `d_tool_01` · K2 · Tier 1 · 75 credits · AttackBonus 1 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Awareness) 2 — *“A droid enhancement that increases the perception and tracking of targets in combat.”*

**Droid Upgrade Slot** · `d_tool_02` · K2 · Tier 1 · 200 credits · BonusFeats (Droid Upgrade 2) ⚠ bay gate · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate — *“This module reprograms a droid's systems to allow upgrades that normally would be too advanced for that droid to handle.”*

**Droid Surveillance Upgrade** · `d_tool_03` · K2 · Tier 2 · 600 credits · Ability (Dexterity) 1 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Awareness) 3 · Skill (Demolitions) 1 — *“An upgrade designed for light scout droids and other listening models.”*

**Droid Advanced Upgrade Slot** · `d_tool_04` · K2 · Tier 2 · 900 credits · BonusFeats (Droid Upgrade 3) ⚠ bay gate · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“This module reprograms a droid's systems to allow upgrades that normally would be too advanced for that droid to handle.”*

**Droid Reference Database** · `d_tool_05` · K2 · Tier 2 · 1,300 credits · AttackBonusRacialGroup (Droid) 2 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Repair) 4 — *“This unit provides your droid with a library of schematics that it can draw upon when repairing or dismantling technology.”*

**Droid System Fortification** · `d_tool_06` · K2 · Tier 2 · 2,200 credits · DamageResist (Ion) Resist_10/- · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“This module carefully monitors and regulates the circuitry of the droid, preventing minor spikes and fluctuations from causing disruptions.”*

**Droid Fighting Upgrade** · `d_tool_07` · K2 · Tier 2 · 3,700 credits · AttackBonus 3 · Armor 2 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Awareness) 2 — *“This module is designed to give your droid a tactical advantage in combat by increasing its sensor range, reflexes, and logic systems.”*

**Droid Perception Sensors** · `d_tool_08` · K2 · Tier 3 · 6,100 credits · AttackBonus 2 · Armor 1 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Awareness) 8 · Skill (Demolitions) 2 — *“This sensor cluster scans the entire light spectrum and audio frequencies well beyond the range of most organic beings. It is nearly impossible for something to occur within the droid's perceptive range without its knowing about it.”*

**Droid Memory Upgrade** · `d_tool_09` · K2 · Tier 3 · 9,200 credits · Ability (Intelligence) 2 · Use Limitation Feat (Droid Upgrade 1) ⚠ bay gate · Skill (Computer Use) 5 — *“This upgrade provides extra memory banks and computing power that can be integrated seamlessly with its existing programming.”*

**Droid Warfare Upgrade** · `d_tool_10` · K2 · Tier 3 · 12,800 credits · AttackBonus 2 · Ability (Constitution) 2 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats (Weapon Prof Blaster) · BonusFeats (Weapon Prof Blaster Rifle) · BonusFeats (Weapon Spec Blaster) · BonusFeats (Weapon Spec Blaster Rifle) · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“A highly complex module with near unlimited learning capacity and highly modifiable software. Designed to be a costly alternative to training, these modules were designed to create master generals, tacticians, and assassins after only a short install time.”*

**Droid Battle Upgrade** · `d_tool_11` · K2 · Tier 3 · 16,400 credits · AttackBonus 3 · Ability (Constitution) 2 · Ability (Dexterity) 2 · BonusFeats (Weapon Focus Blaster) · BonusFeats (Weapon Focus Blaster Rifle) · BonusFeats (Weapon Prof Blaster) · BonusFeats (Weapon Prof Blaster Rifle) · BonusFeats (Weapon Spec Blaster) · BonusFeats (Weapon Spec Blaster Rifle) · Armor 2 · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate — *“This module is a step up from the Droid Fighting Upgrade and provides your droid with a library of countless tatical engagements to draw upon for reference.”*

**Droid CERS** · `d_tool_12` · K2 · Tier 3 · 20,000 credits · AttackBonus 1 · BonusFeats (Improved Rapid Shot) ⚠ attack chain · BonusFeats (Multi Shot) ⚠ attack chain · BonusFeats (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“These upgrades offer powerful new tactics to be hard-wired directly into your droid's combat algorithms. The Droid Combat Enhancement: Rapid Shot adds all the information necessary to your droid's databanks for it to fire multiple times without sacrificing accuracy.”*

**Droid CESS** · `d_tool_13` · K2 · Tier 4 · 23,600 credits · AttackBonus 1 · BonusFeats (Improved Sniper Shot) ⚠ attack chain · BonusFeats (Master Sniper Shot) ⚠ attack chain · BonusFeats (Sniper Shot) ⚠ attack chain · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“These upgrades offer powerful new tactics to be hard-wired directly into your droid's combat algorithms. The Droid Combat Enhancement: Sniper Shot adds all the information necessary to your droid's databanks for it to focus on a single, highly-accurate shot.”*

**Droid CEPB** · `d_tool_14` · K2 · Tier 4 · 27,200 credits · AttackBonus 1 · BonusFeats (Improved Power Blast) ⚠ attack chain · BonusFeats (Master Power Blast) ⚠ attack chain · BonusFeats (Power Blast) ⚠ attack chain · Use Limitation Feat (Droid Upgrade 2) ⚠ bay gate — *“These upgrades offer powerful new tactics to be hard-wired directly into your droid's combat algorithms. The Droid Combat Enhancement: Power Blast adds all the information necessary to your droid's databanks for it to store up energy to release in a single, powerful shot.”*

**Droid Micro-Optics** · `d_tool_15` · K2 · Tier 4 · 30,000 credits · Ability (Dexterity) 5 · BonusFeats (Cautious) · BonusFeats (Improved Caution) · BonusFeats (Master Caution) · Use Limitation Feat (Droid Upgrade 3) ⚠ bay gate · Skill (Demolitions) 10 — *“This sensor array includes several optical sensors that can see changes in substances at the molecular level, allowing the droid to more accurately identify hazardous materials.”*

**Repair Kit** · `g_i_drdrepeqp001` · K2+K1 · Tier 1 · 25 credits · Included are the basic tools needed for a droid to repair itself after being damaged in combat. — *“Included are the basic tools needed to repair a droid that has been damaged in combat. Basic kits repair 15 vitality points + INT modifier + user's skill in Repair.”*

**Advanced Repair Kit** · `g_i_drdrepeqp002` · K2+K1 · Tier 1 · 50 credits · Included are an improved assortment of tools and parts needed for a droid to repair itself after being damaged in combat. — *“Included are an improved assortment of tools and parts needed to repair a droid that has been damaged in combat. Advanced kits repair 25 vitality points + INT modifier + (2 x user's skill in Repair).”*

**Construction Kit** · `g_i_drdrepeqp003` · K2+K1 · Tier 1 · 100 credits · This kit contains all the necessary parts for a droid to repair itself after being damaged in combat, including electrical regulators designed to isolate malfunctions. — *“Included are electrical regulators designed to isolate malfunctions and all the parts needed to repair a damaged droid. Construction kits repair 35 vitality points + INT modifier + (3 x user's skill in Repair).”*
