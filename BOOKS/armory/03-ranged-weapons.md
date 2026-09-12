# Chapter Three — Ranged Weapons

**Every ranged weapon in both games.** Wield classes and critical-hit resolution are
taught in Chapter One and not restated here.

---

## The base weapons

| Weapon | Damage | Type | Range | Threat |
|---|---|---|---|---|
| **Hold Out Blaster** | **1d4** | energy | 24 m | 19–20 · on-hit stun |
| **Sonic Pistol** | **1d4** | sonic | 16 m | 20 · Dex damage |
| **Disruptor Pistol** | **1d6** | physical | 24 m | **18–20** |
| **Ion Blaster** | **1d6** + 1d10 vs droid | ion | 16 m | 20 · **×3** |
| **Blaster Pistol** | **1d8** | energy | 24 m | 20 |
| **Heavy Blaster** | **1d10** | energy | 24 m | 20 |
| **Disruptor Rifle** | **1d10** | physical | 28 m | **18–20** |
| **Ion Rifle** | **1d10** | ion | 28 m | 20 · **×3** |
| **Sonic Rifle** | **1d10** | sonic | 28 m | 20 · Dex damage |
| **Bowcaster** | **1d10** | energy | 28 m | 19–20 |
| **Marksman Rifle** | **1d10** | energy | **40 m** | 19–20 |
| **Blaster Carbine** | **1d12** | energy | 24 m | 20 · ×2 |
| **Blaster Rifle** | **1d12** | energy | 28 m | 19–20 |
| **Sniper Rifle** | **1d12** | energy | **50 m** | 19–20 |

**All pistols are *Balanced*** — they take the reduced off-hand penalty from Chapter
One's wield classes.

**The name is `Hold Out Blaster` — three words, no hyphen.** You will see it hyphenated
elsewhere; **the games spell it unhyphenated**, and `g_w_hldoblstr01` is their own code for
it.

## The two long rifles

**`Marksman Rifle`, 1d10 at 40 metres.** Revised from `1d12`. Blaster Rifle's reach
problem solved the other way round: less damage per shot, considerably more range. It
is not a Blaster Rifle alias — this book already distinguishes four rifles by damage
type, and the Marksman Rifle differs on the columns a marksman actually cares about.

**`Sniper Rifle`, 1d12 at 50 metres.** A separate weapon, not a rename — the longer of
the two by both die and range, and the longest-reaching weapon in the book.

Both are plain. No proficiency gates, no class restrictions, no special ammunition —
the same simple shape `Blaster Rifle` has. What a character does with the extra reach is
the only thing that distinguishes them in play.

### What the perception-extension property actually does

Both rifles carry it. It is **passive** (no action to activate, nothing to maintain),
it **matches the weapon's own range** rather than granting some separate fixed bonus,
and it **respects line of sight** — it extends how far you can perceive, not what you
can perceive through.

**The practical consequence is that these rifles' range is real rather than
theoretical.** A weapon that reaches 50 metres is worth nothing if its wielder cannot
detect anything past 30; the shot exists on paper and never on the table. The
perception extension is what closes that gap: a sniper can engage what shorter weapons
cannot reach *because they can see that far in the first place*. Without it, the extra
range would be a number on a sheet that never changed a fight.

## Where the ceiling sits

**A base blaster pistol averages 4.5 damage (`1d8`). A base vibrosword averages 6.5
(`1d12`) and adds Strength.** A Soldier at Strength 16 (+3) swings for 9.5 average with
a weapon costing 120 credits, where a blaster does 4.5 at any Strength.

**Ranged weapons add Dexterity to damage**, so the gap closes for a character built that
way — but it closes by the shooter's own ability, not by the weapon's.

**The best pistol in either game** is Cassus Fett's Heavy Pistol — 6–19 damage, +5 attack,
25% chance to stun, on top of rifle-like damage.

---

## ⚠ The two rifles this game added

**Neither the Sniper Rifle nor the Marksman Rifle exists in either game.** Both were
written for this book, and they are marked as such wherever they appear.

**Sniper Rifle** · `a_w_snprrfl01` · Tier 2 · **800 credits** · `1d12`, threat 19–20 ×2 —
*"A precision-milled barrel and an integrated scope, built for a shot no other rifle can
guarantee."*

**Marksman Rifle** · `a_w_mrksmnrfl01` · Tier 1 · **400 credits** · `1d10` at 40 metres —
*"A long barrel, a heavy stock and a scope rail. It hits softly and it hits from where
nobody expected."*

**⚠ Do not confuse the Sniper Rifle with the `Sith Sniper Rifle`** (`g_w_blstrrfl002`), a
different and genuine K1 weapon that shares part of the name.

**The 800-credit price is a sensible default rather than a derived figure.** It buys a die
step and ten metres over the Marksman Rifle's 400, **and it is the kind of number a table
should feel free to adjust** if it sits wrong in play.

---

---

# The catalogue

**Every ranged weapon in both games, by family.** Fourteen families, **122 items** —
organised Base versus Advanced by tier, the same shape as Chapter Two's eleven melee
families.

**What is not here, and why.** The games carry 172 pistol and rifle entries between them.
**Fifty are excluded**, because they are things that exist only to make a video game work
rather than items a character could ever own:

- **40 nameless `prop*` rows** — K2 placeholder weapons with no name at all.
- **5 `g_w_null*` rows** — engine null-items, cost 0, literally named *"Blaster Pistol:
  Null"* and so on.
- **4 Bith instruments and a pazaak deck** — `g_i_bithitem001`–`004` and `w_pazaak_01`,
  given the Blaster Pistol base type so a cantina band and a card game could put something
  in a character's hands. **Their `g_i_` prefix marks them as items rather than weapons**,
  and all five carry the generic blaster-pistol description by copy-paste.

**⚠ As in Chapter Two, the item code is not a guide to the family.** `w_brifle_` alone
spans **four different families** here. **Families are determined by a weapon's own damage,
threat range and damage type** — and where those are ambiguous, by what the weapon is
called.

## Hold Out Blaster — base die `1d4`, threat 19–20 / ×2

### Base

**Hold Out Blaster** · `g_w_hldoblstr01` · K1 · Tier 1 · 100 credits · *OnHit (Stun) 10* — *“Sometimes called a "sleeper," the hold out blaster is the preferred method of temporarily incapacitating an enemy.”*

### Advanced

**Field Survival Pistol** · `w_blaste_03` · K2 · Tier 1 · 60 credits · *Massive Criticals 1d4* — *“The Field Survival Pistol is a versatile back-up weapon. Though modest in performance, it is”* ⚠ *(description truncated in source)*

**Scout Enforcer** · `w_blaste_07` · K2 · Tier 1 · 500 credits · *Massive Criticals 1d6 · OnHit (Stun) 10* — *“An advanced survival pistol, the Scout Enforcer is an effective weapon for desperate situations.”*

**Bothan Quick Draw** · `g_w_hldoblstr02` · K1 · Tier 2 · 1,000 credits · *Enhancement 1 · OnHit (Stun) 10* — *“An unconscious opponent is a quiet opponent. This weapon is a Bothan favorite, designed to "create opportunities."”*

**Sith Assassin Pistol** · `g_w_hldoblstr03` · K1 · Tier 2 · 1,700 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10 · Enhancement 2 · OnHit (Stun) 10* — *“These weapons are designed to incapacitate so death may be quick or lingered upon as desired. Droids are simply dispatched, as cruelty is best rationed among the living.”*

**Bothan Needler** · `g_w_hldoblstr04` · K1 · Tier 2 · 1,750 credits · *Enhancement 2 · OnHit (Stun) 10* — *“For serious espionage, this is the weapon of choice. Simple ownership can get you arrested in some systems, or invited to dine with royalty, depending on what it helped you learn.”*

**Watchman Blaster** · `w_blaste_18` · K2 · Tier 3 · 7,600 credits · *Damage (Energy) 1d4 · Massive Criticals 1d8 · OnHit (Stun) 14* — *“When fully upgraded, these survival pistols can match the best heavy blaster in performance. Their stun capabilites make them an excellent off-hand weapon.”*

**Elite Watchman Blaster** · `w_blaste_27` · K2 · Tier 4 · 23,600 credits · *Damage (Energy) 1d10 · Massive Criticals 2d6 · OnHit (Stun) 18* — *“When fully upgraded, these survival pistols can match the best heavy blaster in performance. Their stun capabilites make them an excellent off-hand weapon.”*


## Sonic Pistol — base die `1d4`, threat 20 / ×2

### Base

**Sonic Pistol** · `g_w_sonicpstl01` · K1 · Tier 1 · 200 credits · *OnHit (AbilityDrain) 14* — *“Sometimes referred to as "squealers", these weapons deliver a high-frequency jolt to the senses that can damage and potentially disorient an opponent.”*

**Sonic Pistol** · `w_blaste_04` · K2 · Tier 1 · ⚠⚠ **200** credits · *OnHit (AbilityDrain) 14* — *“Sometimes referred to as "squealers", these weapons deliver a high-frequency jolt to the senses that can damage and potentially disorient an opponent. Sonic weapons can temporarily reduce an opponent's DEX. Additionally,”* ⚠ *(description truncated in source)*

### Advanced

**Systech Aural Blaster** · `w_blaste_08` · K2 · Tier 2 · 699 credits · *Damage (Sonic) 2 · Enhancement 1 · OnHit (AbilityDrain) 18* — *“Though inferior in damage potential to traditional blasters, this sonic blaster's advanced design makes it a viable weapon, especially in long combats when its deafening capabilities can accumulate. Sonic weapons can tem”* ⚠ *(description truncated in source)*

**Bothan Shrieker** · `g_w_sonicpstl02` · K1 · Tier 2 · 1,250 credits · *Enhancement 1 · OnHit (AbilityDrain) 14* — *“This is an improvement over the standard sonic pistol design that must seem doubly shrill to the large ears of the Bothans.”*

**Arkanian Sonic Blaster** · `w_blaste_14` · K2 · Tier 2 · 2,900 credits · *Damage (Sonic) 1 · Damage (Sonic) 1d6 · Enhancement 1 · OnHit (AbilityDrain) 18* — *“This sonic pistol of Arkanian design is as potent as a normal blaster, but with the many benefits of dealing sonic damage. Sonic weapons can temporarily reduce an opponent's DEX. Additionally, many types of shields and d”* ⚠ *(description truncated in source)*

**Heavy Sonic Blaster** · `w_blaste_17` · K2 · Tier 3 · 6,100 credits · *Damage (Sonic) 1d6 · Enhancement 1 · OnHit (AbilityDrain) 22* — *“This incredibly debilitating weapon is of unknown origin. Unlike most lesser models, it can be fitted with a targeting scope. Sonic weapons can temporarily reduce an opponent's DEX. Additionally, many types of shields an”* ⚠ *(description truncated in source)*

**Dashade Sonic Blaster** · `w_blaste_23` · K2 · Tier 3 · 16,400 credits · *Damage (Sonic) 2 · OnHit (AbilityDrain) 18 · OnHit (AbilityDrain) 18* — *“The Dashade are a secretive and vicious species made infamous by their renowned assassins. Their weapons of choice are best known for the extreme pain they inflict. Sonic weapons can temporarily reduce an opponent's DEX.”*

**Dashade Sonic Disruptor** · `w_blaste_29` · K2 · Tier 4 · 27,200 credits · *Damage (Unstoppable) 1d10 · Enhancement 1 · OnHit (AbilityDrain) 18 · OnHit (AbilityDrain) 22* — *“The Dashade are a secretive and vicious species made infamous by their renowned assassins. Their weapons of choice are best known for the extreme pain they inflict. This improved model combines the best features of sonic”* ⚠ *(description truncated in source)*


## Disruptor Pistol — base die `1d6`, threat 18–20 / ×2

### Base

**Disruptor Pistol** · `g_w_dsrptpstl001` · K1 · Tier 1 · 200 credits · *no properties* — *“These pistols are illegal in many planetary systems, being regarded as too powerful a weapon to be owned by civilians. Disruptors reduce solid matter to its constituent molecules. Unlike typical blasters, disruptors igno”* ⚠ *(description truncated in source)*

**Disruptor Pistol** · `w_blaste_05` · K2 · Tier 1 · 200 credits · *no properties* — *“These pistols are illegal in many planetary systems, being regarded as too powerful a weapon to be owned by civilians. Disruptors reduce solid matter to its constituent molecules. Unlike typical blasters, disruptors igno”* ⚠ *(description truncated in source)*

### Advanced

**Luxa's Disruptor** ⚠ *unique* · `w_blaste_x05` · K2 · Tier 1 · 200 credits · *AttackBonus 1* — *“These pistols are illegal in many planetary systems, being regarded as too powerful a weapon to be owned by civilians. Disruptors reduce solid matter to its constituent molecules. Unlike typical blasters, disruptors igno”* ⚠ *(description truncated in source)*

**Mandalorian Ripper** · `g_w_dsrptpstl002` · K1 · Tier 2 · 1,500 credits · *Enhancement 2* — *“A weapon similar to this energy-propelled slug-thrower belonged to Jigger Wraith, a bounty hunter who plagued the Republic years ago. Thirty-seven Mandalorians were executed for being him until sightings declined. As a t”* ⚠ *(description truncated in source)*

**Sith Disruptor** · `w_blaste_15` · K2 · Tier 2 · 4,000 credits · *Damage (Energy) 1* — *“The Sith disruptor design is compatible with most types of blaster upgrades.”*

**Mandalorian Ripper** · `w_blaste_20` · K2 · Tier 3 · ⚠⚠ **1500** credits · *Enhancement 2* — *“A weapon similar to this disruptor belonged to Jigger Wraith, a bounty hunter who plagued the Republic years ago. Thirty-seven Mandalorians were executed for being him until sightings declined. As a type of disruptor, th”* ⚠ *(description truncated in source)*

**Mandalorian Disintegrator** · `w_blaste_28` · K2 · Tier 4 · 26,950 credits · *Damage (Unstoppable) 1d6 · Damage (Unstoppable) 2 · Enhancement 2* — *“Not surprisingly, the most deadly disruptor pistol available is of Mandalorian design. Use of this ruthless weapon is a major violation of Republic code.”*


## Ion Blaster — base die `1d6`, threat 20 / ×2

### Base

**Ion Blaster** · `g_w_ionblstr01` · K1 · Tier 1 · 200 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10* — *“Unlike a typical blaster, this weapon fires a stream of energy very damaging to electrical systems, causing havoc on the internal components of droids.”*

**Ion Blaster** · `w_blaste_02` · K2 · Tier 1 · ⚠⚠ **200** credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d12* — *“This standard Ion Blaster is commonly issued to Republic troops as a secondary weapon. While ion weapons are generally less damaging against organic opponents, they are powerful against droids. Also, ion damage can penet”* ⚠ *(description truncated in source)*

### Advanced

**Aratech Droid Oxidizer** · `w_blaste_10` · K2 · Tier 2 · 1,099 credits · *AttackBonus 1 · Damage (Ion) 2 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10* — *“The Aratech Ion Blaster is designed to be capable against all types of opponents, replacing the need to carry a second anti-droid side arm. While ion weapons are generally less damaging against organic opponents, they ar”* ⚠ *(description truncated in source)*

**Verpine Prototype Ion Blaster** · `g_w_ionblstr02` · K1 · Tier 2 · 1,500 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10 · Enhancement 2* — *“Demonstrating this weapon, the insect-like Verpine destroyed legions of droids, doing nothing to quell the public's suspicions of what testing their stun guns must have been like.”*

**Aratech Ionmaster** · `w_blaste_21` · K2 · Tier 3 · 12,799 credits · *AttackBonus 2 · Damage (Ion) 1d8 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d8* — *“This capable side-arm is at the top of Aratech's ion blaster line. It is designed for multi-purpose use, though obviously is best against droids. While ion weapons are generally less damaging against organic opponents, t”* ⚠ *(description truncated in source)*


## Blaster Pistol — base die `1d8`, threat 20 / ×2

### Base

**Blaster Pistol** · `g_w_blstrpstl001` · K1 · Tier 1 · 100 credits · *no properties* — *“The most common ranged weapon in the galaxy is the basic blaster pistol, firing a bolt of intense coherent light powered by a replaceable power pack.”*

**Blaster Pistol** · `w_blaste_01` · K2 · Tier 1 · ⚠⚠ **100** credits · *no properties* — *“The most common ranged weapon in the galaxy is the basic blaster pistol, firing a bolt of intense coherent light powered by a replaceable power pack.”*

### Advanced

**Drink In Hand** · `w_drink_01` · K2 · Tier 1 · 25 credits · *no properties* — *“The most common ranged weapon in the galaxy is the basic blaster pistol, firing a bolt of intense coherent light powered by a replaceable power pack.”*

**Empty Hand** · `w_emptyhnd_01` · K2 · Tier 1 · 25 credits · *no properties* — *“The most common ranged weapon in the galaxy is the basic blaster pistol, firing a bolt of intense coherent light powered by a replaceable power pack.”*

**KillBlaster** · `killblaster` · K2 · Tier 1 · 100 credits · *⚠ properties come from the fitted crystals, not the weapon — see Chapter Six* — *“The most common ranged weapon in the galaxy is the basic blaster pistol, firing a bolt of intense coherent light powered by a replaceable power pack.”*

**Bendak's Blaster** ⚠ *unique* · `g_w_blstrpstl006` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 2 · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This blaster belonged to Bendak Starkiller, a duelist legendary on Taris. It is a highly adaptable weapon, and is definitely of better quality than any standard issue pistol.”*

**Bendak's Blaster** ⚠ *unique* · `g_w_blstrpstl007` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 4 · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This blaster belonged to Bendak Starkiller, a duelist legendary on Taris. It is a highly adaptable weapon, and is definitely of better quality than any standard issue pistol.”*

**Bendak's Blaster** ⚠ *unique* · `g_w_blstrpstl008` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 5 · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This blaster belonged to Bendak Starkiller, a duelist legendary on Taris. It is a highly adaptable weapon, and is definitely of better quality than any standard issue pistol.”*

**Bendak's Blaster** ⚠ *unique* · `g_w_blstrpstl009` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 5 · Massive Criticals 2d6 · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This blaster belonged to Bendak Starkiller, a duelist legendary on Taris. It is a highly adaptable weapon, and is definitely of better quality than any standard issue pistol.”*

**Insta-kill Pistol** · `g_w_blstrpstl020` · K1 · Tier 1 · found only · *OnHit (Instant Death) 100* — *“The most common weapon of bravados and smugglers, the blaster pistol fires a high-energy particle beam designed for short-range combat.”*

**Mining Laser** · `mininglaser` · K2 · Tier 1 · found only · *no properties* — *“This industrial hand-held laser can double as a makeshift blaster.”*

**Remote's Blaster** ⚠ *unique* · `w_blaste_x20` · K2 · Tier 1 · found only · *AttackBonus 5 · AttackBonus 5* — *“Bao-Dur outfitted the Remote with this customized blaster.”*

**Mandalorian Blaster** · `g_w_blstrpstl002` · K1 · Tier 2 · 750 credits · *Enhancement 1* — *“The Mandalorian Blaster is a slightly more powerful version of the basic pistol common throughout the galaxy.”*

**Republic Blaster** · `w_blaste_09` · K2 · Tier 2 · 850 credits · *no properties* — *“The Republic Blaster can be fully upgraded with firing chamber, targeting scope, and power cell.”*

**Arkanian Pistol** · `g_w_blstrpstl003` · K1 · Tier 2 · 1,000 credits · *Enhancement 2* — *“This is a versatile blaster variant, possibly of ancient Arkanian origin. The Arkanians are very proud that such early efforts continue to be prized among collectors and soldiers.”*

**Carth's Blaster** ⚠ *unique* · `g_w_blstrpstl010` · K1 · Tier 2 · 1,000 credits · *AttackBonus 1 · AttackBonus 1 · Damage (Energy) 1 · Damage (Energy) 1 · Damage (Energy) 1* — *“Special: , Ranged Carth's personal blaster is based on an old Arkanian design, but he has adapted it to incorporate all of the latest modular technology available to the Republic.”*

**Zabrak Blaster Pistol** · `g_w_blstrpstl004` · K1 · Tier 2 · 1,500 credits · *Enhancement 3 · OnHit (Stun) 10* — *“This blaster is the staple of the Zabrak mercenary, known for deadly accuracy and exceptional damage.”*

**Bendak's Blaster** ⚠ *unique* · `g_w_blstrpstl005` · K1 · Tier 2 · 2,000 credits · *AttackBonus 1 · AttackBonus 1 · Damage (Energy) 1 · Damage (Energy) 2 · Enhancement 1* — *“Special: , Ranged This blaster belonged to Bendak Starkiller, a duelist legendary on Taris. It is a highly adaptable weapon, and is definitely of better quality than any standard issue pistol.”*

**GenoHaradan Blaster** · `geno_blaster` · K1 · Tier 2 · 2,000 credits · *AttackBonus 5 · Damage (Energy) 1* — *“The GenoHaradan created this blaster as a tool to strike against well-protected assassination targets. It's remarkable accuracy makes it the perfect weapon for precision, long range strikes.”*

**Systech Static Blaster** · `w_blaste_13` · K2 · Tier 2 · 2,199 credits · *Damage (Electrical) 1d6* — *“This unusual weapon was originally developed for use against veermok, a ferocious primate on Naboo that happens to be resistant to blaster fire. Much of the weapon's damage is electrical in nature, allowing it to bypass”* ⚠ *(description truncated in source)*

**Mandalorian Blaster** · `w_blaste_12` · K2 · Tier 2 · ⚠⚠ **750** credits · *Enhancement 1* — *“The Mandalorian Blaster is a slightly more powerful version of the basic pistol common throughout the galaxy.”*

**Onasi Blaster** · `w_blaste_22` · K2 · Tier 3 · 14,600 credits · *Damage (Energy) 1 · Enhancement 2* — *“This blaster bears the symbol of the Onasi family. It perhaps once belonged to Carth Onasi, a former companion of Revan.”*

**Systech Electric Blaster** · `w_blaste_25` · K2 · Tier 3 · 20,000 credits · *AttackBonus 1 · Damage (Electrical) 2d6* — *“This unusual line of weapons was originally developed for use against veermok, a ferocious primate on Naboo that happens to be resistant to blaster fire. The Electric Blaster is the high-end model. Much of the weapon's d”* ⚠ *(description truncated in source)*

**Zabrak Blaster Pistol** · `w_blaste_19` · K2 · Tier 3 · ⚠⚠ **1500** credits · *Enhancement 3 · OnHit (Stun) 10* — *“This blaster is the staple of the Zabrak mercenary, known for deadly accuracy and exceptional damage.”*

**Micro-Pulse Blaster** · `w_blaste_26` · K2 · Tier 4 · 21,800 credits · *Damage (Energy) 1d8 · Enhancement 2* — *“Built of durable thoranium, this blaster is able to fire more intense pulses of energy than lesser pistols are capable of. The result is the potency of an advanced blaster rifle in a one-handed weapon.”*


## Heavy Blaster — base die `1d10`, threat 20 / ×2

### Base

**Heavy Blaster** · `g_w_hvyblstr01` · K1 · Tier 1 · 200 credits · *no properties* — *“These resemble regular blasters in the same way Quoorian marshsuckers resemble mosquitoes. Sure, they both do damage, but the former definitely has the edge in kill-potential.”*

**Heavy Blaster** · `w_blaste_06` · K2 · Tier 1 · ⚠⚠ **200** credits · *no properties* — *“These resemble regular blasters in the same way Quoorian marshsuckers resemble mosquitoes. Sure, they both do damage, but the former definitely has the edge in kill potential.”*

### Advanced

**Cassus Fett's Heavy Pistol** ⚠ *unique* · `g_w_hvyblstr06` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 3 · Damage (Ion) 4 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Cassus Fett was rarely seen without this adaptable blaster. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Cassus Fett's Heavy Pistol** ⚠ *unique* · `g_w_hvyblstr07` · K1 · Tier 1 · found only · *Damage (Ion) 1d8 · Enhancement 5 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Cassus Fett was rarely seen without this adaptable blaster. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Cassus Fett's Heavy Pistol** ⚠ *unique* · `g_w_hvyblstr08` · K1 · Tier 1 · found only · *Damage (Ion) 1d8 · Enhancement 5 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Cassus Fett was rarely seen without this adaptable blaster. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Cassus Fett's Heavy Pistol** ⚠ *unique* · `g_w_hvyblstr09` · K1 · Tier 1 · found only · *Damage (Ion) 1d8 · Enhancement 5 · Massive Criticals 2d6 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Cassus Fett was rarely seen without this adaptable blaster. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Arkanian Heavy Pistol** · `g_w_hvyblstr02` · K1 · Tier 2 · 1,000 credits · *Enhancement 1* — *“Arkanian designs of this kind predated mass acceptance of heavier pistols, but 2000 years later they are still superior performers.”*

**Zabrak Tystel Mark III** · `g_w_hvyblstr03` · K1 · Tier 2 · 1,500 credits · *Damage (Bludgeoning) 2 · Enhancement 2* — *“The Zabrak killed many pirates who were attempting to seize shipments of these weapons and then sold them on the black market anyway. It's not a matter of where they end up, but of who gets paid.”*

**Mandalorian Heavy Pistol** · `g_w_hvyblstr04` · K1 · Tier 2 · 2,000 credits · *Damage (Bludgeoning) 2 · Enhancement 3* — *“Mandalorians boast that a shot from one of these pistols can take a starship out of commission. It's an obvious exaggeration, but for safety's sake, most listeners just smile and nod.”*

**Mandalorian Heavy Blaster** · `w_blaste_16` · K2 · Tier 2 · 5,000 credits · *Enhancement 1* — *“Mandalorians improved upon the standard heavy blaster design, creating a weapon that is both and superior to the standard design.”*

**Arkanian Heavy Pistol** · `w_blaste_11` · K2 · Tier 2 · ⚠⚠ **1000** credits · *Enhancement 1* — *“Arkanian designs of this kind predated mass acceptance of heavier pistols, but 2000 years later they are still superior performers. Unfortunately, their design is incompatible with modern upgrade technology.”*

**Cassus Fett's Heavy Pistol** ⚠ *unique* · `g_w_hvyblstr05` · K1 · Tier 3 · 10,000 credits · *AttackBonus 1 · AttackBonus 1 · Damage (Energy) 1d4 · Damage (Energy) 1d4 · Enhancement 3 · Keen 0 · OnHit (Stun) 10* — *“Special: , Ranged Cassus Fett was rarely seen without this adaptable blaster. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Zabrak Heavy Blaster** · `w_blaste_24` · K2 · Tier 3 · 18,200 credits · *Damage (Energy) 2 · Enhancement 2 · OnHit (Stun) 18* — *“A more cumbersome, but also more damaging, blaster of Zabrak design.”*

**Freedon Nadd's Blaster** ⚠ *unique* · `w_blaste_30` · K2 · Tier 4 · 29,000 credits · *UseLimitationAlignmentGroup [subtype 3 — iprp_aligngrp unmapped] 0 · UseLimitationClass [subtype 16 — classes unmapped] 0 · UseLimitationClass [subtype 15 — classes unmapped] 0 · UseLimitationClass [subtype 14 — classes unmapped] 0 · Damage (Dark Side) 2d10 · Enhancement 2* — *“A vile weapon that once belonged to Freedon Nadd, this blaster has killed more Jedi then any lightsaber.”*


## Disruptor Rifle — base die `1d10`, threat 18–20 / ×2

### Base

**Disruptor Rifle** · `g_w_dsrptrfl001` · K1 · Tier 1 · 400 credits · *no properties* — *“This disruptor is even more destructive than its pistol counterpart, and is outlawed on just as many worlds. Disruptors reduce solid matter to its constituent molecules. Painfully. Unlike typical blasters, disruptors ign”* ⚠ *(description truncated in source)*

**Disruptor Rifle** · `w_brifle_13` · K2 · Tier 2 · ⚠⚠ **400** credits · *no properties* — *“This disruptor is even more destructive than its pistol counterpart, and is outlawed on just as many worlds. Disruptors reduce solid matter to its constituent molecules. Painfully. Unlike typical blasters, disruptors ign”* ⚠ *(description truncated in source)*

### Advanced

**Disruptor Carbine** · `w_brifle_08` · K2 · Tier 2 · 900 credits · *no properties* — *“This disruptor is even more destructive than its pistol counterpart, and is outlawed on just as many worlds. Disruptors reduce solid matter to its constituent molecules. Painfully. Unlike typical blasters, disruptors ign”* ⚠ *(description truncated in source)*

**Zabrak Disruptor Cannon** · `g_w_dsrptrfl002` · K1 · Tier 2 · 1,500 credits · *Damage (Piercing) 5 · Enhancement 2* — *“Zabrak always command respect, especially with the aid of weapons that are even more damaging than already-outlawed standard disruptors. Unlike typical blasters, disruptors ignore most types of personal energy shields.”*

**Charric** · `w_brifle_23` · K2 · Tier 3 · 16,450 credits · *AttackBonus 4 · OnHit (Knockdown) 14* — *“The Charric is an immensely powerful disruptor rifle. Exceedingly rare, its origin is believed to be somewhere in the Unknown Regions, though what species created it is unknown. The Charric employs maser beams and easily”* ⚠ *(description truncated in source)*


## Ion Rifle — base die `1d10`, threat 20 / ×2

### Base

**Ion Rifle** · `g_w_ionrfl01` · K1 · Tier 1 · 400 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d6* — *“Any well-stocked militia usually has stores of ion rifles in reserve. They aren't much use against the living, but if the enemy has battle droids these weapons become essential.”*

**Ion Rifle** · `w_brifle_07` · K2 · Tier 2 · ⚠⚠ **400** credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10* — *“Unlike the less customizable carbines, rifles can be upgraded. Ion weapons cannot utilize most power pack upgrades, however. While ion weapons are generally less damaging against organic opponents, they are powerful agai”* ⚠ *(description truncated in source)*

### Advanced

**Ion Carbine** · `w_brifle_02` · K2 · Tier 1 · 65 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10* — *“Ion Carbines are versatile, low-end rifles. They are sometimes given to combat droids to provide an edge against other droid armies. While ion weapons are generally less damaging against organic opponents, they are power”* ⚠ *(description truncated in source)*

**Bothan Droid Disruptor** · `g_w_ionrfl02` · K1 · Tier 2 · 750 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d6 · Enhancement 1* — *“Droids can be difficult obstacles for a spy, but these weapons take all the guesswork out of dealing with them.”*

**Verpine Droid Disruptor** · `g_w_ionrfl03` · K1 · Tier 2 · 1,750 credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d6 · Enhancement 2* — *“While they may have borrowed liberally from designs the Bothans initiated, the Verpine say you can't argue with results. These weapons are simply devastating against droids.”*

**Bothan Droid Disruptor** · `w_brifle_15` · K2 · Tier 2 · ⚠⚠ **750** credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d10 · Enhancement 1* — *“Droids can be difficult obstacles for a spy, but these weapons take all the guesswork out of dealing with them. While ion weapons are generally less damaging against organic opponents, they are powerful against droids. A”* ⚠ *(description truncated in source)*

**⚠ *name-field corrupted*** · `g1_w_ionrfl01` · K1 · Tier 3 · 12,000 credits · *AttackBonus 3 · AttackBonus 1 · AttackBonus 1 · AttackBonus 1 · Damage (Ion) 1d6 · Damage (Ion) 1d6 · Damage (Piercing) 1d10 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d6 · Keen 0* — *“Mastercraft: Armor III”* ⚠ *(description truncated in source)* **⚠ This item has no usable name.** Its name field in the game data reads *"Mastercraft: Armor II"* — an armour upgrade's name sitting on an ion rifle's entry. **The weapon is real; the name is not.** It is left unnamed here rather than given an invented one.

**Verpine Droid Disruptor** · `w_brifle_20` · K2 · Tier 3 · ⚠⚠ **1750** credits · *DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d10 · Enhancement 2* — *“While they may have borrowed liberally from designs the Bothans initiated, the Verpine say you can't argue with results. These weapons are simply devastating against droids. While ion weapons are generally less damaging”* ⚠ *(description truncated in source)*

**Verpine Droid Disintegrator** · `w_brifle_29` · K2 · Tier 4 · 28,000 credits · *Damage (Ion) 1d10 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d10 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 2d10 · Enhancement 2* — *“This weapon is simply the most powerful anti-droid rifle available. While ion weapons are generally less damaging against organic opponents, they are powerful against droids. Also, ion damage can penetrate some defenses”* ⚠ *(description truncated in source)*


## Sonic Rifle — base die `1d10`, threat 20 / ×2

### Base

**Sonic Rifle** · `g_w_sonicrfl01` · K1 · Tier 1 · 400 credits · *OnHit (AbilityDrain) 14* — *“More powerful than the pistol, the sonic rifle fires a blast of sound that causes a great deal of sensory overload in addition to damage, disorienting the victim.”*

**Sonic Rifle** · `w_brifle_09` · K2 · Tier 2 · ⚠⚠ **400** credits · *Damage (Sonic) 1d4 · OnHit (AbilityDrain) 14* — *“More powerful than the pistol, the sonic rifle fires a blast of sound that causes a great deal of sensory overload in addition to damage, disorienting the victim.”*

### Advanced

**Sonic Carbine** · `w_brifle_03` · K2 · Tier 1 · 95 credits · *OnHit (AbilityDrain) 14* — *“More powerful than the pistol, the sonic carbine fires a blast of sound that causes a great deal of sensory overload in addition to damage, disorienting the victim.”*

**Bothan Discord Gun** · `g_w_sonicrfl02` · K1 · Tier 2 · 1,000 credits · *Enhancement 1 · OnHit (AbilityDrain) 14* — *“This was conceived as a "last resort" weapon should espionage fail and a quick retreat be called for. It is effective, but the Bothans would prefer that it not be needed.”*

**Arkanian Sonic Rifle** · `g_w_sonicrfl03` · K1 · Tier 2 · 2,000 credits · *Enhancement 2 · OnHit (AbilityDrain) 14* — *“The Arkanians pioneered many non-lethal weapons that could disorient opponents, but most were retrofitted to be superior damage dealers as well because the initial demand for them was so low.”*

**Argazdan Riot Buster** · `w_brifle_14` · K2 · Tier 2 · 2,945 credits · *OnHit (AbilityDrain) 14 · OnHit (Stun) 10* — *“During the Argazdan's subjugation of the Lorrdians, non-lethal technology was a profitable commodity. The Argazdan Riot Buster knocks its target to the ground and stuns them.”*

**Sonic Disruptor** · `w_brifle_27` · K2 · Tier 4 · 24,750 credits · *Damage (Unstoppable) 1d10 · OnHit (AbilityDrain) 22 · OnHit (Stun) 18* — *“Combining both sonic and disruptor attacks, this rifle tears through enemy defenses.”*


## Bowcaster — base die `1d10`, threat 19–20 / ×2

### Base

**Bowcaster** · `g_w_bowcstr001` · K1 · Tier 1 · 400 credits · *Damage (Piercing) 2* — *“The bowcaster is an invention of the Wookiees of Kashyyyk. Also called a laser crossbow, it actually uses a magnetic accelerator to hurl an explosive energy quarrel at its target.”*

**Bowcaster** · `w_brifle_05` · K2 · Tier 1 · ⚠⚠ **400** credits · *Damage (Energy) 1* — *“The bowcaster is an invention of the Wookiees of Kashyyyk. Also called a laser crossbow, it actually uses a magnetic accelerator to hurl an explosive energy quarrel at its target.”*

### Advanced

**Zaalbar's Bowcaster** ⚠ *unique* · `g_w_bowcstr003` · K1 · Tier 1 · 400 credits · *AttackBonus 1 · AttackBonus 2 · Damage (Energy) 1 · Damage (Energy) 1 · Keen 0* — *“Special: , Ranged This is Zaalbar's personal bowcaster. He has made modifications to it over the years, but it still tightly conforms to the traditions of his people.”*

**Chuundar's Bowcaster** ⚠ *unique* · `g_w_bowcstr002` · K1 · Tier 2 · 1,500 credits · *Damage (Piercing) 4 · Enhancement 2* — *“Chuundar's personal weapon is a bowcaster with some unusual Czerka modifications. Most Wookiees would likely not appreciate such outside influence.”*

**War Bowcaster** · `w_brifle_11` · K2 · Tier 2 · 2,000 credits · *Damage (Energy) 1* — *“The bowcaster is an invention of the Wookiees of Kashyyyk. Also called a laser crossbow, it actually uses a magnetic accelerator to hurl an explosive energy quarrel at its target. This more expensive war bowcaster is sui”* ⚠ *(description truncated in source)*

**Ceremonial Bowcaster** · `w_brifle_21` · K2 · Tier 3 · 13,750 credits · *BonusFeats (Improved Rapid Shot) ⚠ attack chain · BonusFeats (Rapid Shot) ⚠ attack chain · Enhancement 3 · Keen 0* — *“This specialized bowcaster was designed for use in ceremonial hunts. It is capable of an impressive rate of fire even in unskilled hands. Though not suitable for upgrading, few of the weapon's targets would argue that fu”* ⚠ *(description truncated in source)*


## Marksman Rifle — base die `1d10`, threat 19–20 / ×2

### Base

**Marksman Rifle** · `a_w_mrksmnrfl01` · AUTHORED · Tier 1 · 400 credits · *no properties*


## Blaster Carbine — base die `1d12`, threat 19–20 / ×2

### Advanced

**Jamoh Hogra's Carbine** ⚠ *unique* · `g_w_blstrcrbn006` · K1 · Tier 1 · found only · *Damage (Piercing) 2 · Enhancement 1 · Keen 0 · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This was the weapon of mercenary Jamoh Hogra, and was supposed to protect him against the many enemies he earned in his lifetime. Hogra's skill didn't match its potential, however.”*

**Jamoh Hogra's Carbine** ⚠ *unique* · `g_w_blstrcrbn007` · K1 · Tier 1 · found only · *Damage (Piercing) 4 · Enhancement 1 · Keen 0 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This was the weapon of mercenary Jamoh Hogra, and was supposed to protect him against the many enemies he earned in his lifetime. Hogra's skill didn't match its potential, however.”*

**Jamoh Hogra's Carbine** ⚠ *unique* · `g_w_blstrcrbn008` · K1 · Tier 1 · found only · *Damage (Piercing) 4 · Enhancement 4 · Keen 0 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This was the weapon of mercenary Jamoh Hogra, and was supposed to protect him against the many enemies he earned in his lifetime. Hogra's skill didn't match its potential, however.”*

**Jamoh Hogra's Carbine** ⚠ *unique* · `g_w_blstrcrbn009` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 4 · Damage (Piercing) 4 · Keen 0 · Massive Criticals 1d8 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged This was the weapon of mercenary Jamoh Hogra, and was supposed to protect him against the many enemies he earned in his lifetime. Hogra's skill didn't match its potential, however.”*

**Sith Assault Gun** · `g_w_blstrcrbn002` · K1 · Tier 2 · 1,750 credits · *Damage (Piercing) 1 · Enhancement 1* — *“This is a modification on the blaster carbine rarely seen outside of Sith-controlled space.”*

**Cinnagaran Carbine** · `g_w_blstrcrbn003` · K1 · Tier 2 · 2,750 credits · *Damage (Piercing) 1 · Enhancement 2* — *“This blaster rifle variant is one of many fine weapons produced by the factories of Cinnagar in their continued militarizing after the Great Hyperspace War a thousand years ago.”*

**Jurgan Kalta's Carbine** ⚠ *unique* · `g_w_blstrcrbn004` · K1 · Tier 2 · 4,500 credits · *Damage (Piercing) 2 · Enhancement 3* — *“The Zabrak mercenary Jurgan Kalta commissioned this rifle, a weapon he liked to think of as "amusingly destructive."”*

**Jamoh Hogra's Carbine** ⚠ *unique* · `g_w_blstrcrbn005` · K1 · Tier 3 · 9,000 credits · *AttackBonus 2 · AttackBonus 1 · Damage (Energy) 1 · Damage (Energy) 1d4 · Damage (Piercing) 1d4 · Damage (Piercing) 1d4 · Enhancement 2* — *“Special: , Ranged This was the weapon of mercenary Jamoh Hogra, and was supposed to protect him against the many enemies he earned in his lifetime. Hogra's skill didn't match its potential, however.”*

**Slavemaster Stun Carbine** · `w_brifle_25` · K2 · Tier 4 · 22,500 credits · *DamageNone 0 · OnHit (AbilityDrain) 14 · OnHit (Stun) 22* — *“Trandoshan bounty hunters will use this weapon to capture their victims alive. As it is a carbine, it cannot be upgraded.”*


## Blaster Rifle — base die `1d12`, threat 19–20 / ×2

### Base

**Blaster Rifle** · `g_w_blstrrfl001` · K1 · Tier 1 · 300 credits · *no properties* — *“More powerful than the commonly available pistol, the blaster rifle is favored by soldiers throughout the galaxy. Civilian ownership of these weapons is not generally encouraged.”*

**Blaster Rifle** · `w_brifle_04` · K2 · Tier 1 · ⚠⚠ **300** credits · *no properties* — *“More powerful than the commonly available pistol, the blaster rifle is favored by soldiers throughout the galaxy. Civilian ownership of these weapons is not generally encouraged. Unlike carbines, most rifles can be fully”* ⚠ *(description truncated in source)*

### Advanced

**Blaster Carbine** · `g_w_blstrcrbn001` · K1 · Tier 1 · 500 credits · *no properties* — *“Created initially by Gungis X Weapons, blaster carbine rifles have become very popular in recent years, helped by falling prices due to competition from other companies.”*

**Jurgan Kalta's Assault Rifle** ⚠ *unique* · `g_w_blstrrfl006` · K1 · Tier 1 · found only · *AttackBonus 3 · Damage (Energy) 4 · Damage (Ion) 1d8 · Keen 0 · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Jurgan Kalta wanted to make a big noise in the galaxy. If it was the screams of his enemies, all the better. This weapon was his favorite because it shared his adaptability.”*

**Jurgan Kalta's Assault Rifle** ⚠ *unique* · `g_w_blstrrfl007` · K1 · Tier 1 · found only · *AttackBonus 4 · Damage (Energy) 1d8 · Damage (Ion) 1d8 · Keen 0 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Jurgan Kalta wanted to make a big noise in the galaxy. If it was the screams of his enemies, all the better. This weapon was his favorite because it shared his adaptability.”*

**Jurgan Kalta's Assault Rifle** ⚠ *unique* · `g_w_blstrrfl008` · K1 · Tier 1 · found only · *AttackBonus 4 · Damage (Energy) 1d8 · Damage (Ion) 1d8 · Keen 0 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Jurgan Kalta wanted to make a big noise in the galaxy. If it was the screams of his enemies, all the better. This weapon was his favorite because it shared his adaptability.”*

**Jurgan Kalta's Assault Rifle** ⚠ *unique* · `g_w_blstrrfl009` · K1 · Tier 1 · found only · *AttackBonus 5 · Damage (Energy) 1d8 · Damage (Ion) 1d8 · Keen 0 · Massive Criticals 1d8 · OnHit (Stun) Bonus_14 · Use Limitation Feat (Power Attack) ⚠ attack chain · Use Limitation Feat (Power Blast) ⚠ attack chain · Use Limitation Feat (Rapid Shot) ⚠ attack chain · Use Limitation Feat (Sniper Shot) ⚠ attack chain* — *“Special: , Ranged Jurgan Kalta wanted to make a big noise in the galaxy. If it was the screams of his enemies, all the better. This weapon was his favorite because it shared his adaptability.”*

**Blaster Carbine** · `w_brifle_01` · K2 · Tier 1 · ⚠⚠ **500** credits · *no properties* — *“Blaster carbine rifles are inelegant, but effective weapons. They are commonly used by unskilled thugs and mercenaries.”*

**Sith Sniper Rifle** · `g_w_blstrrfl002` · K1 · Tier 2 · 1,500 credits · *Enhancement 1* — *“Despite its effectiveness, these modified blaster rifles are not often employed by the Sith. They prefer to engage their enemies up close and personal.”*

**Arkanian Blaster Rifle** · `w_brifle_12` · K2 · Tier 2 · 1,595 credits · *Damage (Energy) 2 · Enhancement 1* — *“The Arkanian Blaster Rifle's ancient design is still quite powerful by modern standards. However, they cannot be outfitted with modern firing chambers and power cells, limiting them to scopes for upgrade options.”*

**Mandalorian Assault Rifle** · `g_w_blstrrfl003` · K1 · Tier 2 · 2,500 credits · *Enhancement 2 · OnHit (Stun) 10* — *“These weapons are almost overpowered for their size, but the Mandalorians prefer them that way. They do not make a habit of being subtle in their war making.”*

**Zabrak Battle Cannon** · `g_w_blstrrfl004` · K1 · Tier 2 · 4,000 credits · *AttackBonus 3 · Damage (Energy) 5* — *“These weapons are almost beginning to cross the line to light artillery. Armor is generally ineffective against such a weapon, unless it is of the highest quality.”*

**Jurgan Kalta's Assault Rifle** ⚠ *unique* · `g_w_blstrrfl005` · K1 · Tier 3 · 8,000 credits · *AttackBonus 3 · AttackBonus 2 · Damage (Energy) 1d4 · Damage (Ion) 1d4 · Damage (Piercing) 1d4 · DamageRacialGroup [subtype 5 — racialtypes unmapped] 1d6* — *“Special: , Ranged Jurgan Kalta wanted to make a big noise in the galaxy. If it was the screams of his enemies, all the better. This weapon was his favorite because it shared his adaptability.”*

**Plasma Projector** · `w_brifle_18` · K2 · Tier 3 · 8,075 credits · *AttackPenalty Penalty_-1 · Damage (Energy) 1d12 · Use Limitation Feat (Weapon Focus Blaster Rifle) · Use Limitation Feat (Weapon Spec Blaster Rifle) · Keen 0* — *“This massive weapon fires a bolt of plasma energy at its target. Difficult to wield except by highly trained marksmen, the plasma projector is also unsuitable for further upgrades.”*

**Zabrak Blaster Carbine** · `w_brifle_24` · K2 · Tier 3 · 18,800 credits · *Damage (Energy) 1d12 · Damage (Energy) 3 · Keen 0* — *“The design of the Zabrak Blaster Carbine is too complicated to allow further upgrading. Fortunately, it has little need for additional enhancement.”*

**Mandalorian Assault Rifle** · `w_brifle_19` · K2 · Tier 3 · ⚠⚠ **2500** credits · *Enhancement 2 · OnHit (Stun) 14* — *“These weapons are almost overpowered for their size, but the Mandalorians prefer them that way. They do not make a habit of being subtle in their war making.”*

**Zersium Rifle** · `w_brifle_30` · K2 · Tier 4 · 30,000 credits · *Damage (Energy) 1d12 · Enhancement 1* — *“This rifle is made in part of Zersium, a rare mineral that aids in energy dissipation. This characteristic allows the rifle to utilize more powerful energy bursts without risking the safety of its wielder.”*


## Sniper Rifle — base die `1d12`, threat 19–20 / ×2

### Base

**Sniper Rifle** · `a_w_snprrfl01` · AUTHORED · Tier 2 · 800 credits · *no properties* — *“A long barrel, a heavy stock and a scope rail. It hits softly and it hits from where nobody expected.”*


---
