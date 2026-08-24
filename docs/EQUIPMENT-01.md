# EQUIPMENT-01 — Weapon Damage and the Defence Formula

**Source: StrategyWiki's KOTOR weapon tables and the Neoseeker ranged reference.** `source_system: kotor_game`, secondary. **Range values cross-checked against `baseitems.2da` and identical.**

---

## 1. Two findings that matter more than the numbers

> **Melee adds Strength to both attack and damage. Ranged adds nothing to damage.**

*"Strength modifier is added to both Attack and Damage."* *"Ranged weapons do not get a bonus to damage from STR or DEX, so they can easily be outpaced by melee weapons."*

**That single asymmetry is why melee dominates late in both games**, and it is the reason our ranged Power chain — Charged Shot → Power Shot → **Blast**, +5/+8/+10 — **is doing more work than its melee mirror.** **A blaster's damage comes almost entirely from the attack you declare.**

> **Defence = 10 + armour bonus + Dexterity modifier, and the Dexterity contribution is capped by the armour.**

*"A character under attack will compare your attack roll to their defense, which is calculated as 10 + armor bonus + DEX. The DEX bonus to defense may be capped by your armor."*

**Heavier armour gives more Defence and a lower Dexterity cap.** **⚠ The specific values per armour class are still absent — see §5.**

---

## 2. Melee — base weapons

| Weapon | Damage | Type | Threat | Balanced | Attacks |
|---|---|---|---|---|---|
| **Stun Baton** | **1** | bludgeoning | 20 / ×2 | — | 1 |
| **Short Sword** | **1d6** | piercing | 20 / ×2 | **yes** | 1 |
| **Quarterstaff** | **1d6** | bludgeoning | 20 / ×2 | **yes** | **2** |
| **Gaffi Stick** | **1d8** | piercing | 20 / ×2 | **yes** | **2** |
| **Vibroblade** | **1d10** | piercing | **19–20 / ×2** | **yes** | 1 |
| **Wookiee Warblade** | **1d10** | slashing | 20 / ×2 | **yes** | **2** |
| **Long Sword** | **1d12** | slashing | 20 / ×2 | no | 1 |
| **Gamorrean Battleaxe** | **1d12** | slashing | 20 / ×2 | — | 1 |
| **Vibrosword** | **2d6** | slashing | **19–20 / ×2** | no | 1 |
| **Double-Bladed Sword** | **2d6** | slashing | 20 / ×2 | **yes** | **2** |
| **Vibro Double-Blade** | **2d8** | slashing | 20 / ×2 | **yes** | **2** |

> **The "Attacks" column confirms our double-blade ruling.** **Quarterstaff, Gaffi Stick, Wookiee Warblade, and both double-bladed types are marked 2.** **Every one is also *Balanced*, which is exactly the reduced penalty `ACTION-ECONOMY-01 §7.6` gives them.**

**And the trade is visible in the threat range.** **A vibrosword threatens on 19–20; a double-bladed sword of identical damage threatens only on 20.** *"Capable of inflicting more damage — but also less precise — than the single-bladed variant."*

**Balanced weapons give +2/+0 against the two-weapon penalty when used off-hand.**

---

## 3. Melee — the progression

**Three points on the curve, all vibroswords, to see how far upgrades move the number.**

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibrosword** *(120 credits)* | **2d6** | 19–20 | — |
| **The One's Vibrosword** *(mid)* | **2d6 +5** | 19–20 | **+5** |
| **Bacca's Ceremonial Blade** *(2,480)* | **2d6 +4**, +4 energy, **+2d6 vs droid** | 19–20 | **+4** |
| **Baragwin Assault Blade** *(9,000)* | **2d6 + 2d6 energy + 2d6 sonic** | **17–20** | **+5** |

**And the best double weapon:**

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibro Double-Blade** *(180)* | **2d8** | 20 | — |
| **Yusanis' Brand** *(8,000)* | **2d8 +2**, +3 fire, **+6–9 ion vs droid** | **19–20** | **+3**, on-hit stun |

> **Base to best is roughly 7 average damage to 24**, plus an attack bonus of +5 and a threat range doubled from 10% to 20%. **A factor of three on damage across a campaign.**

---

## 4. Ranged

| Weapon | Damage | Type | Range | Threat |
|---|---|---|---|---|
| **Hold-Out Blaster** | **1d4** | energy | 24 m | **19–20** · on-hit stun |
| **Disruptor Pistol** | **1d4** | physical | 24 m | 20 |
| **Ion Blaster** | **1d4** + **1d10 vs droid** | ion | **16 m** | 20 |
| **Sonic Pistol** | **1d4** | sonic | **16 m** | 20 · Dex damage |
| **Blaster Pistol** | **1d6** | energy | 24 m | 20 |
| **Disruptor Rifle** | **1d6** | physical | 28 m | 20 |
| **Ion Rifle** | **1d6** | ion | 28 m | — |
| **Sonic Rifle** | **1d6** | sonic | 28 m | 20 · Dex damage |
| **Blaster Carbine** | **1d8** | energy | **24 m** | **19–20** |
| **Blaster Rifle** | **1d8** | energy | 28 m | **19–20** |
| **Bowcaster** | **1d10** | energy | 28 m | **19–20** |

**All pistols are *Balanced*.**

**The best pistol in either game:** **Cassus Fett's Heavy Pistol — 6–19 damage, +5 attack, 25% chance to stun.** *"On top of its rifle-like damage."*

> **Note the ceiling.** **A base blaster pistol averages 3.5 damage. A base vibrosword averages 7 and adds Strength.** **A Soldier at Strength 16 swings for 10 average with a weapon costing 120 credits, where a blaster does 3.5 at any Strength.**

---

## 4b. Lightsabers

**Confirmed from `baseitems.2da`. The games differ — K2 bumped every lightsaber one die step.**

| Weapon | **K1** | K2 | Threat | Wield | Size |
|---|---|---|---|---|---|
| **Short Lightsaber** | **2d6** | 2d8 | **19–20 / ×2** | **2 — one-handed** | Small |
| **Lightsaber** | **2d8** | 2d10 | **19–20 / ×2** | **2 — one-handed** | Medium |
| **Double-Bladed Lightsaber** | **2d10** | 2d12 | **20 only / ×2** | **3 — two-handed staff** | Large |

> **Use K1's. Our campaign is 3956 BBY and K1 is the era.**
>
> **And K1's numbers make a cleaner system.** **A vibrosword is 2d6, so a K1 lightsaber sits exactly one die step above it.** **K2's 2d10 is two steps, which widens the gap between a Jedi and everyone else for no reason our port needs.**

**⚠ Correction: an earlier draft cited 2d6 for the standard lightsaber. That is wrong for both games.** *It is the Short Lightsaber's K1 value; the secondary source appears to have confused them.*

**`critthreat` 2 means 19–20; `critthreat` 1 means 20 only.** **Both as we had them.**

**Short Lightsaber is one-handed and Small** — **`weaponwield` 2, the same class as a standard lightsaber.** **So it may be paired, and its Small size makes it the natural off-hand.**

> **The threat ranges are confirmed and they are the whole trade.** ***"Single lightsaber: 19-20 critical threat ⇒ 10% critical chance. Double-bladed lightsaber: 20-20 critical threat ⇒ 5% critical chance."***

**Same shape as the vibrosword against the double-bladed sword** — **more attacks, less precision.** **And the double-bladed lightsaber is Balanced**, so it takes our reduced dual-wield penalty.

**⚠ The base damage die is not confirmed by a primary source in this sweep.** **2d6 energy is the widely cited KOTOR 1 value and is used below**, but **StrategyWiki's lightsaber page states the threat ranges and the upgrade rules without restating the base dice.** **Confirm before the numbers matter.**

**Lightsabers inflict energy damage**, which matters: ***"disruptors aren't the only ranged weapons that don't"*** — **energy is absorbed by shields where physical is not.** *A vibrosword cuts through an energy shield; a lightsaber does not.*

**And a note that affects our roster:** ***"Lightsabers are not melee weapons, and a critical hit doubles bonus damage."*** **Two rules in one sentence** — **the lightsaber is its own weapon category, and its criticals multiply bonus damage where other weapons' do not.**

---

## 5. Armour

**Defence = 10 + armour bonus + Dexterity modifier, and the Dexterity contribution is capped by the armour.**

### 5.1 One rule generates the whole table — confirmed from the data

> ***"The sum of armor and Max Dexterity Bonus is always 9."***

**Confirmed for all organic armour in both games. `baseitems.2da` rows 38–43, identical values.**

| Row | Label | `baseac` | `dexbonus` | Sum | `armortype` |
|---|---|---|---|---|---|
| 38 | Armor_Class_4 | **4** | **+5** | 9 | **leather** |
| 39 | Armor_Class_5 | **5** | **+4** | 9 | **leather** |
| 40 | Armor_Class_6 | **6** | **+3** | 9 | armor |
| 41 | Armor_Class_7 | **7** | **+2** | 9 | armor |
| 42 | Armor_Class_8 | **8** | **+1** | 9 | armor |
| 43 | Armor_Class_9 | **9** | **+0** | 9 | armor |

> **There is no three-way light/medium/heavy flag.** **`armortype` splits leather from armor — Light from everything else — and the medium/heavy boundary is `baseac`-driven, not column-driven.**

**Two exceptions, both K2.** **The Armoured Flight Suit** *(row 98, 5/+4)* **obeys the rule.** **The Zeison Sha** *(row 102, 3/+4 = 7)* **breaks it** — the only organic armour in either game that does.

**So a Defence of 19 is the ceiling from body armour alone**, whatever you wear — **and the choice is only ever *where the 9 comes from*.**

> **A Smuggler at Dexterity 20 in light armour reaches 4 + 5 = 9. A Soldier at Dexterity 10 in heavy reaches 9 + 0 = 9.** **The armour classes are not better and worse. They are the same total, sorted by which ability you invested in.**

**K2 shifts the heavy band down one** — **armour 8 / Max Dex +1** where K1 tops out at **9 / +0** — **but adds upgrade slots that recover it.** *Heavy Bonded Plates up to +4 Defence, Flexible Underlay up to +3 Max Dex.*

### 5.2 Robes are the exception, and it is a bug that became a feature

**Jedi Robe Defence 1 · Knight Robe 2 · Master Robe 3 · Revan Robes 5.**

> ***"Robes display in game a Max Dexterity Bonus of +8, but actually act as if possessing an infinite Max Dexterity Bonus."***

**So a robe's Defence has no cap on Dexterity at all.** **A Jedi at Dexterity 28 in a Master Robe gets 3 + 9 = 12, beating every suit of armour in the game.**

**That is why Jedi wear robes**, and it compounds with the restriction: ***"many Force powers are restricted when using armor."***

### 5.3 Droid plating is a separate class and does not follow the rule

> **Droids cannot wear organic armour. They have plating, which is its own item class and was never bound by the sum of 9.**

**K1 droid plating sums to 9, 7, and 10 across its three grades.** **K2 changed Light and Medium plating to `dexbonus` = −1**, **which the engine reads as *uncapped*.**

> **So a K2-plated droid keeps its full Dexterity bonus on top of its plating.** **A droid in Light plating is the only body-armour case in either game with no Dexterity ceiling** — **the same property that makes Jedi robes worth wearing.**

**⚠ An earlier draft gave the Astromech pregen Defence 10 + 0 + 2 = 12 on the grounds that droids cannot wear armour.** **Corrected — they wear plating.**

### 5.4 Two restrictions worth porting

**Organic armour is not usable by droids or Wookiees.** *"Armor Proficiency is required to use armor, which is not usable by Droids and Wookiees."* **⚠ The Wookiee exclusion is new to our corpus** — the species chapter does not carry it.

**And armour blocks Force powers**, which `ACTION-ECONOMY-01 §12` already depends on to make the Heavy-Armour and Soresu gates on `Well Guarded` genuinely alternative paths. **Confirmed.**

---

## 6. Ability score generation — the blocker is closed

> ***"At character generation each of the six physical attributes is at 8, with 30 points to invest in them. Any attribute can be increased to a maximum of 18 at this time, but beyond 14 there are increased point costs."***

**And: *"Characters are granted an additional attribute point every fourth level, at levels 4, 8, 12, 16 and 20."*** *"These aren't subject to the increased point costs which apply at character generation, so any attribute can be increased to a maximum of 23 by investing points."*

**Point buy. Every ability starts at 8. Thirty points. Maximum 18 at creation, costs rising above 14. One point at levels 4, 8, 12, 16, and 20.**

> **This is the answer for a playtest specifically.** **It is repeatable — two runs of the same encounter are not confounded by one character having rolled an 18** — and it is the source's own method rather than RCR's 4d6-drop-lowest.

**⚠ The exact cost curve above 14 is not in the extract.** **Needed before a character can be built precisely; a flat 2-points-per-step above 14 is the usual d20 shape and would do for a first test.**

---

## 7. ⚠ On a complete equipment catalogue

**You asked for every item in both games with effects, bonuses, penalties, and restrictions.**

> **That is several hundred items across armour, robes, weapons, upgrades, implants, belts, gloves, headgear, masks, shields, and consumables — and it is a data-extraction job, not a research job.**

**The 2DA holder has the files that answer it properly:** **`baseitems.2da` for the categories, and the item instance files for the individual entries with their property lists.** **A wiki sweep would take dozens of fetches and still be secondary.**

**What this document holds instead: the structural rules, every base weapon, three points on the melee upgrade curve, and the complete armour arithmetic.** **That is enough to build a character and run a fight.**

---

## 8. ⚠ Droid plating — named placeholder values

**`baseitems.2da`'s droid plating rows are not in holdings.** **The values below are authored stand-ins so characters can be built, and they are marked as such wherever they appear.**

| Plating | Defence | Max Dex |
|---|---|---|
| **Light** | **+4** | **uncapped** |
| **Medium** | **+6** | **uncapped** |
| **Heavy** | **+8** | **+1** |

**Light and Medium are uncapped because K2 sets their `dexbonus` to −1, which the engine reads as no limit.** **That much is attested.** **The `baseac` figures are not.**

> **Replace when the rows are extracted. Until then every droid Defence in `PREGENS-01` carries this note.**
