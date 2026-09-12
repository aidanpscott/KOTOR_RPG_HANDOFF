# Chapter Five — Armour

**The defence formula, the sum-of-nine rule, robes and droid plating are all taught in
Chapter One and not restated here.** This chapter is the catalogue — the same relationship
Chapter Two has to Chapter One's damage rules.

**⚠ One difference worth knowing, because it affects how much to trust these numbers.** The
armour figures in this chapter were converted straight from the games' own item files.
**They did not pass through a summary first**, which is where the errors corrected in
Chapters Two, Three and Four came from.

---

## The six categories

**172 items in total**, nine of them appearing in both games.

| Category | Count | What it is |
|---|---|---|
| **Clothing** | 16 | No armour bonus by default; civilian and party-member wear, some unique (Atton's jacket, Mira's mesh jacket) that quietly matches light-armour protection despite the slot |
| **Disguise** | 2 | Not combat gear at all — grants a `Disguise` property and little else, worn to pass as something you aren't rather than to take a hit |
| **Light** | 37 | The Light armour class from Chapter One's table — armour bonus 4–5, high Dexterity cap |
| **Medium** | 41 | Mid-range of Chapter One's table |
| **Heavy** | 34 | The low-Dexterity-cap end of Chapter One's table |
| **Robes** | 42 | Uncapped Dexterity, per Chapter One's own exception — the largest single category, reflecting how central Force users are to this game's item design |

## Representative entries

| Name | Category | Cost | Note |
|---|---|---|---|
| **Light Combat Suit** | Light | 50 | The cheapest armour that actually protects you, tied with the plain `Combat Suit` |
| **Heavy Combat Suit** | Light | 100 | Same category, better protection, same Dexterity treatment |
| **Padawan Robe** | Robes | 50 | `Armor 1` — the entry-level robe every Jedi pregen starts closest to |
| **Atton's Ribbed Jacket** ⚠ unique | Clothing | 0 (found, not bought) | `Armor 4` — matches Light armour's protection from a Clothing slot |
| **Sith Armor** ⚠ unique | Disguise | 0 (found, not bought) | `Armor 2` plus a disguise property — one of only two items in this category |

## ⚠⚠ Armour prices: where an item is in both games, KOTOR 1's price governs

**This is the single most important thing to know before reading the prices below**, and it
settles thirty-five of them.

**The two games price the same armour differently — every item present in both, at a median
of nearly twice.** This game resolves that one way, and it is not a compromise: **the
KOTOR 1 price is the price.** KOTOR 1 is the more carefully balanced economy, and a single
ladder beats two.

**Thirty-one entries below are marked *reconciled to the KOTOR 1 price*.** Their KOTOR 2
rows are kept so the difference stays visible, but the figure shown is the governing one.

**Four more are marked *the KOTOR 1 price, which governs*, and they are the interesting
ones**, because in each case the two games disagree sharply about what the same armour is
worth:

| Item | KOTOR 1 — **the price** | KOTOR 2 records |
|---|---|---|
| **Dark Jedi Robe** | **100** | 700 |
| **Ulic Qel Droma's Mesh Suit** | **5,000** | 30,000 |
| **Exar Kun's Light Battle Suit** | **6,000** | 15,000 |
| **Jamoh Hogra's Battle Armor** | **10,000** | 30,000 |

**All four are mechanically identical between the two games** — same armour bonus, same
resistances, same restrictions. **Only the price moved, and by as much as six times.**

**One wrinkle worth flagging rather than hiding.** KOTOR 2's `Dark Jedi Robe` carries
`Regeneration Force Points 1` where KOTOR 1's does not. **The price still follows KOTOR 1**,
but a Gamemaster running the KOTOR 2 version is getting the better item at the older price.

### The robes show why the rule exists at all

**The robe ladder runs light and dark in pairs, and the two halves of each pair should cost
the same** — a dark robe does not do more than its light twin. **Six of the seven pairs
already price equal:**

| Pair | Price, light and dark |
|---|---|
| KOTOR 1 base | 100 / 100 |
| Padawan | 50 / 50 |
| KOTOR 1 knight | 150 / 150 |
| Knight | 2,200 / 2,200 |
| KOTOR 1 master | 200 / 200 |
| Master | 6,100 / 6,100 |
| **KOTOR 2 base** | **100 / 700** ⚠ |

> **One mismatched pair out of seven, and the `Dark Jedi Robe` was the odd one.** It is
> mechanically identical to the `Jedi Robe` — same `Armor 1`, same restriction — and it was
> the only robe in the ladder that cost more than its twin.

**Under the rule above it follows KOTOR 1 at 100**, which resolves the ladder to
**100 · 150 · 200, light and dark equal at every tier.** The 700 is recorded and is not what
a Gamemaster charges.

## ⚠ Some armour carries a `DecreaseAC` property, and it means exactly what it says

It is a real penalty, not a display quirk.

**Worked example — the `Light Combat Suit`.** Its base row in the games' own armour table
gives armour 4 and a Dexterity cap of +5, an ordinary Light entry under Chapter One's
sum-of-nine rule. Its `DecreaseAC` property then reduces the armour component
specifically — **not some narrower penalty against melee or ranged attacks.**

**So its true protection is `+3` armour, not the `+4` its category suggests**, while
keeping the full `+5` Dexterity cap. **Genuinely below-average gear, cheaply priced to
match.**

**Any other `DecreaseAC` or `IncreaseAC` entry resolves the same way:** find which part of
Defence the property touches, then find the base value it is modifying in the item's own
armour row.

---

# The catalogue

**All 172 items, by category**, with resref, which game each comes from, tier, price,
properties and the item's own description.

**⚠ Four rows have a corrupted name.** `g1_a_class5001`, `g1_a_class5002`, `g1_a_class6001`
and `g1_a_class8001` are real armour with real properties, **but their name and description
fields both carry unrelated text** — feat descriptions and upgrade labels that belong
somewhere else in the game's string table. **They are catalogued by resref and marked. No
name has been invented for any of them.**

**⚠ Many rows carry a property the data does not resolve** — a species restriction without
the species, a Defence penalty without its type, a skill bonus without its skill. **Each
keeps its index in the margin and none is guessed at.**

---

## Clothing — 16

**Atton's Ribbed Jacket** ⚠ **UNIQUE** · `a_light_x02` · K2 · Tier 1 · no sale value · Armor 4 · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 2)* 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Atton's durable jacket provides protection comparable to light armor.”*

**Mira's Ballistic Mesh Jacket** ⚠ **UNIQUE** · `a_light_x09` · K2 · Tier 1 · no sale value · DamageResist (Bludgeoning) Resist_5/- · DamageResist (Piercing) Resist_5/- · DamageResist (Slashing) Resist_5/- · Armor 5 · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 8)* 0 · ⚠ *Species-restricted (which species is unresolved)* — *“One of the first major purchases of a successful bounty hunter is often exceptional protection. Mira's mesh jacket is as protective as medium armor, but much less restrictive.”*

**Clothing** · `a_robe_01` · K2 · Tier 1 · 25 credits · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing** · `g_a_clothes01` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 09}** · `g_a_clothes010` · K2 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant Czerka}** · `g_a_clothes011` · K2 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 11}** · `g_a_clothes012` · K2 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 02}** · `g_a_clothes02` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 03}** · `g_a_clothes03` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 04}** · `g_a_clothes04` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 05}** · `g_a_clothes05` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 06}** · `g_a_clothes06` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 01}** · `g_a_clothes07` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 07}** · `g_a_clothes08` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Clothing {Variant 08}** · `g_a_clothes09` · K2+K1 · Tier 1 · no sale value · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple garments that protect little more than the modesty of the wearer.”*

**Dancer's Outfit** ⚠ **UNIQUE** · `g_danceroutfit` · K2 · Tier 1 · no sale value · UseLimitationGender ⚠ *(unresolved — `gender` subtype 1)* 0 · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 3)* 0 · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 8)* 0 · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 0)* 0 · Skill bonus +2 ⚠ *(which skill is unresolved — subtype 4)* — *“This dancer's outfit leaves little to the imagination.”*

## Disguise — 2

**Sith Armor** ⚠ **UNIQUE** · `ptar_sitharmor` · K1 · Tier 1 · no sale value · Armor 2 · Disguise ⚠ *(which appearance is unresolved)* — *“This full body armor could be used to fool people into thinking the wearer was one of the Sith.”*

**Sand People Clothing** ⚠ **UNIQUE** · `tat17_sandperdis` · K1 · Tier 1 · no sale value · Disguise ⚠ *(which appearance is unresolved)* — *“These are the intricate robes of a Sand People warrior. They seem to be in good condition, and might allow a wearer to superficially appear to be a member of the Sand People species.”*

## Light — 37

**Light Combat Suit** · `a_light_01` · K2 · Tier 1 · 50 credits · **Defence penalty -1** ⚠ *(which Defence type is unresolved — subtype 2)* · ⚠ *Species-restricted (which species is unresolved)* — *“The lightest form of armor available, the light combat suit is very inexpensive and still notably superior to normal civilian garb.”*

**Combat Suit** · `a_light_02` · K2 · Tier 1 · 50 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“Even the most frugal of mercenaries know they need at least some protection from the rigors of combat, although suits of this type are recommended for light skirmishes only.”*

**Heavy Combat Suit** · `a_light_03` · K2 · Tier 1 · 100 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“This version of the combat suit offers more protection than the basic model. It is heavier overall and not quite as flexible, but many consider the tradeoffs worthwhile.”*

**Mandalorian Combat Suit** · `a_light_04` · K2 · Tier 2 · 850 credits · DamageImmunity (Bludgeoning) ⚠ **DR 2** *(10%)* · DamageImmunity (Piercing) ⚠ **DR 2** *(10%)* · DamageImmunity (Slashing) ⚠ **DR 2** *(10%)* · **Defence penalty -1** ⚠ *(which Defence type is unresolved — subtype 2)* · ⚠ *Species-restricted (which species is unresolved)* — *“Even the basic combat attire of the Mandalorians provides a formidable defense. The mesh of this armor absorbs some of the impact of physical blows despite its light weight.”*

**Zabrak Combat Suit** · `a_light_05` · K2 · Tier 2 · 750 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“A Zabrak improvement on the combat suit, this armor is good protection where speed and unrestricted movement are more important than bulky plating.”*

**Bonadan Alloy Heavy Suit** · `a_light_06` · K2 · Tier 2 · 900 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Bonadan is an emerging industrial society financing their exploration of the galaxy through production of small arms and armor. They favor heavy materials offering solid defense.”*

**Echani Light Armor** · `a_light_07` · K2 · Tier 2 · 1,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Fire) Resist_15/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Echani prefer elegant design to brute force. The Maktites learned this when their stores of thermal weapons were rendered ineffective by simple changes in the Echani light armor.”*

**Massassi Ceremonial Armor** · `a_light_08` · K2 · Tier 3 · 3,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · Immunity (Critical Hits) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Long-term domination by the Sith has erased the memory of the Massassi rituals for which this armor was designed, but it retains its effectiveness on the battlefield regardless.”*

**Mandalorian Heavy Suit** · `a_light_09` · K2 · Tier 3 · 10,000 credits · DamageImmunity (Bludgeoning) ⚠ **DR 2** *(10%)* · DamageImmunity (Piercing) ⚠ **DR 2** *(10%)* · DamageImmunity (Slashing) ⚠ **DR 2** *(10%)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This heavier Mandalorian combat suit is most commonly used by elite scouts. Besides its strong defense and ability to absorb physical damage, the armor can also be outfitted with upgrades normally restricted to medium armor.”*

**Zabrak Battle Armor** · `a_light_10` · K2 · Tier 3 · 2,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Cold) Resist_20/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“On the far northern continent of the planet Iridonia, the Zabrak produce expensive armor that nonetheless has become very popular on the galactic markets, due to excellent low-temperature defensive properties.”*

**Echani Shield Suit** · `a_light_12` · K2 · Tier 3 · 20,000 credits · DamageImmunity (Electrical) ⚠ **DR 2** *(10%)* · DamageImmunity (Energy) ⚠ **DR 2** *(10%)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“The Echani combined their talents for energy shield design with their armorcrafting skills to develop this innovative combat suit. It provides capable defense that is augmented with a low strength energy shield.”*

**Reinforced Fiber Armor** · `a_light_13` · K2 · Tier 4 · 3,500 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Inspired by craftsmen on worlds where metal is in short supply, this type of light armor consists of jung-ju tree fibers bound with synthetics, offering good, flexible protection.”*

**Zabrak Field Armor** · `a_light_14` · K2 · Tier 4 · 3,250 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Cold) Resist_30/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“This is a higher-quality version of the basic armor produced by the Zabrak. These were often reserved for field commanders, and meant to be easily identified on the battlefield.”*

**Ulic Qel Droma's Mesh Suit** ⚠ **UNIQUE** · `a_light_15` · K2 · Tier 4 · **5,000 credits** ⚠ *(the KOTOR 1 price, which governs; the KOTOR 2 row records 30,000)* · DamageResist (Cold) Resist_20/- · DamageResist (Fire) Resist_20/- · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“After killing his brother during the Exar Kun war, Ulic Qel Droma abandoned this armor and all the trappings of his service to the Dark Side. It's a powerful, if tainted, item.”*

**Electromesh Suit** · `a_light_x08` · K2 · Tier 2 · 5,000 credits · DamageResist (Energy) Resist_5/- · Armor 1 · DEXBonusMax 2 · ⚠ *Species-restricted (which species is unresolved)* — *“This light combat suit is used by Nagai operatives. It is highly resistant to blaster fire and is designed to allow the Nagai to fully capitalize on their naturally high dexterity. It cannot be used with overlays, however.”*

**⚠ Name corrupted in the source** · `g1_a_class5001` · K1 · Tier 3 · 10,000 credits · Ability (Dexterity) 1 · Ability (Strength) 1 · Ability (Strength) 2 · Armor 2 · Armor 1 · Armor 1 — ⚠ *Its name and description fields both carry unrelated text; the properties above are the item’s own. Recorded, not renamed.*

**⚠ Name corrupted in the source** · `g1_a_class5002` · K1 · Tier 3 · 6,000 credits · Armor 2 · Armor 2 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* · Skill bonus +8 ⚠ *(which skill is unresolved — subtype 2)* — ⚠ *Its name and description fields both carry unrelated text; the properties above are the item’s own. Recorded, not renamed.*

**Combat Suit** · `g_a_class4001` · K1 · Tier 1 · 50 credits · ⚠ *Species-restricted (which species is unresolved)* — *“Even the most frugal of mercenaries know they need at least some protection from the rigors of combat, although suits of this type are recommended for light skirmishes only.”*

**Zabrak Combat Suit** · `g_a_class4002` · K1 · Tier 2 · 750 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“A Zabrak improvement on the combat suit, this armor is good protection where speed and unrestricted movement are more important than bulky plating.”*

**Echani Light Armor** · `g_a_class4003` · K1 · Tier 2 · 1,000 credits · DamageResist (Fire) Resist_15/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Echani prefer elegant design to brute force. The Maktites learned this when their stores of thermal weapons were rendered ineffective by simple changes in the Echani light armor.”*

**Cinnagar Weave Armor** · `g_a_class4004` · K1 · Tier 2 · 2,000 credits · DamageResist (Cold) Resist_20/- · DamageResist (Fire) Resist_20/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“A complex organic weave protects this armored suit from extremes in temperature. Armor similar to it proved decisive in defending Cinnagar from the Sith under Naga Sadow.”*

**Massassi Ceremonial Armor** · `g_a_class4005` · K1 · Tier 2 · 3,000 credits · Armor 1 · Immunity (Critical Hits) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Long-term domination by the Sith has erased the memory of the Massassi rituals for which this armor was designed, but it retains its effectiveness on the battlefield regardless.”*

**Darth Bandon's Fiber Armor** ⚠ **UNIQUE** · `g_a_class4006` · K1 · Tier 2 · 5,000 credits · DamageResist (Fire) Resist_25/- · Armor 1 · Armor 2 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Despite the unfortunate fate of Darth Bandon, this light armor remains a desirable asset for any warrior. The silvery polish reflects a pride in craftsmanship rarely seen today.”*

**Darth Bandon's Fiber Armor** ⚠ **UNIQUE** · `g_a_class4007` · K1 · Tier 1 · no sale value · Armor 3 · DamageResist (Fire) Resist_25/- · ⚠ *Species-restricted (which species is unresolved)* — *“Despite the unfortunate fate of Darth Bandon, this light armor remains a desirable asset for any warrior. The silvery polish reflects a pride in craftsmanship rarely seen today.”*

**Darth Bandon's Fiber Armor** ⚠ **UNIQUE** · `g_a_class4008` · K1 · Tier 1 · no sale value · Armor 3 · DamageResist (Fire) Resist_25/- · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Despite the unfortunate fate of Darth Bandon, this light armor remains a desirable asset for any warrior. The silvery polish reflects a pride in craftsmanship rarely seen today.”*

**Echani Fiber Armor** · `g_a_class4009` · K1 · Tier 2 · 900 credits · DamageResist (Cold) Resist_20/- · DamageResist (Fire) Resist_20/- · Armor 1 · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Many elite Echani duelists use armor of this type, though its adaptability has made it popular with professional soldiers and bounty hunters alike.”*

**Heavy Combat Suit** · `g_a_class5001` · K1 · Tier 1 · 100 credits · ⚠ *Species-restricted (which species is unresolved)* — *“This version of the combat suit offers more protection than the basic model. It is heavier overall and not quite as flexible, but many consider the tradeoffs worthwhile.”*

**Bonadan Alloy Heavy Suit** · `g_a_class5002` · K1 · Tier 2 · 900 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Bonadan is an emerging industrial society financing their exploration of the galaxy through production of small arms and armor. They favor heavy materials offering solid defense.”*

**Zabrak Battle Armor** · `g_a_class5003` · K1 · Tier 2 · 2,000 credits · DamageResist (Cold) Resist_20/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“In northern Iridonia the Zabrak produce expensive armor that nonetheless has become very popular on the galactic markets, due to excellent low-temperature defensive properties.”*

**Zabrak Field Armor** · `g_a_class5004` · K1 · Tier 2 · 3,250 credits · DamageResist (Cold) Resist_30/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“This is a higher-quality version of the basic armor produced by the Zabrak. These were often reserved for field commanders, and meant to be easily identified on the battlefield.”*

**Reinforced Fiber Armor** · `g_a_class5005` · K1 · Tier 2 · 3,500 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Inspired by craftsmen on worlds where metal is in short supply, this type of light armor consists of jung-ju tree fibers bound with synthetics, offering good, flexible protection.”*

**Ulic Qel Droma's Mesh Suit** ⚠ **UNIQUE** · `g_a_class5006` · K1 · Tier 2 · 5,000 credits · DamageResist (Cold) Resist_20/- · DamageResist (Fire) Resist_20/- · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“After killing his brother during the Exar Kun war, Ulic Qel Droma abandoned this armor and all the trappings of his service to the Dark Side. It's a powerful, if tainted, item.”*

**Eriadu Prototype Armor** · `g_a_class5007` · K1 · Tier 3 · 6,000 credits · DamageResist (Cold) Resist_15/- · Armor 1 · Armor 3 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor combines good protection and easy movement to allow even a novice to fight like a seasoned veteran, but Eriadu has delayed general production pending further tests.”*

**Eriadu Prototype Armor** · `g_a_class5008` · K1 · Tier 1 · no sale value · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor combines good protection and easy movement to create an impression of competence about the owner, but Eriadu has delayed general production pending further tests.”*

**Eriadu Prototype Armor** · `g_a_class5009` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_30/- · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor combines good protection and easy movement to allow even a novice to fight like a seasoned veteran, but Eriadu has delayed general production pending further tests.”*

**Republic Mod Armor** · `g_a_class5010` · K1 · Tier 2 · 1,000 credits · Armor 1 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“The Republic has prospered militarily by keeping its troops well supplied with modular armor, ensuring they are always prepared for a variety of battle conditions.”*

**GenoHaradan Mesh Armor** · `geno_armor` · K1 · Tier 2 · 5,000 credits · Ability (Dexterity) 3 · Armor 3 · Skill bonus +4 ⚠ *(which skill is unresolved — subtype 2)* · ⚠ *Species-restricted (which species is unresolved)* — *“This perfectly balanced armor provides maximum protection without hampering a Genoharadan agent's ability to stalk his prey in total secrecy.”*

## Medium — 41

**Khoonda Militia Armor** · `a_khoonda` · K2 · Tier 1 · no sale value

**Ubese Environmental Suit** · `a_light_11` · K2 · Tier 3 · 14,750 credits · DamageResist (Cold) Resist_10/- · DamageResist (Electrical) Resist_10/- · DamageResist (Energy) Resist_10/- · DamageResist (Fire) Resist_10/- · ⚠ *Species-restricted (which species is unresolved)* — *“Ubese is the name given to a species believed to exist in the Mid Rim. The very few who actually claim to have encountered the Ubese attribute these advanced environmental suits to the enigmatic species. Though less useful against conventional weapons, this suit is ideal defense against blasters, flames, and cryoban grenades.”*

**Military Suit** · `a_medium_01` · K2 · Tier 1 · 150 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“This standard issue suit provides good protection, but can be heavier and more restrictive than some of its counterparts. Even so, many mercenaries swear the tradeoffs are worth it.”*

**Light Battle Armor** · `a_medium_02` · K2 · Tier 1 · 250 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“Providing solid protection for a minimal cost, this armor is excellent for entrenched troops or guards. A force on the move, however, may find it somewhat constricting.”*

**Echani Battle Armor** · `a_medium_03` · K2 · Tier 1 · 1,750 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor provides solid defense at the cost of some flexibility, although it is still an Echani product and is therefore well suited to quick-moving combat.”*

**Cinnagar War Suit** · `a_medium_04` · K2 · Tier 2 · 3,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Sonic) Resist_15/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“After the Great Hyperspace War a thousand years ago, the heirs of Empress Teta militarized their world and industry, a legacy that produced battle armor still sought after today.”*

**Sith Battle Suit** · `a_medium_05` · K2 · Tier 2 · 1,300 credits · Armor 1 · DEXBonusMax 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This battle armor's name is actually created by Aratech, who named it after the Sith to benefit from their fame (or infamy). This combat suit is very flexible for medium armor.”*

**Bronzium Light Battle Armor** · `a_medium_06` · K2 · Tier 2 · 1,500 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This molded armor is made of better materials than standard military issue, but is still relatively cheap and easy to mass-produce, making it ideal for light militias and the like.”*

**Verpine Fiber Mesh** · `a_medium_07` · K2 · Tier 2 · 4,250 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Raxsus Nuli had plans of planetary conquest in the wake of Sith aggression. Though eclipsed by recent events, the Jedi saw the pirate jailed and his Verpine stockpiles auctioned.”*

**Krath Heavy Armor** · `a_medium_08` · K2 · Tier 3 · 5,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Typical of the old Krath military elite, these suits were worn during slave raids on neighboring systems. Slaving is profitable but risky, so little cost is spared in equipment.”*

**Powered Light Battle Armor** · `a_medium_09` · K2 · Tier 3 · 3,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · Ability (Strength) 1 · DamageResist (Sonic) Resist_25/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This is an early attempt at power-assisted armor. Dampening fields block the noise of servomotors, unintentionally shielding against external extremes in sonic frequencies as well.”*

**Krath Holy Battle Suit** · `a_medium_10` · K2 · Tier 3 · 6,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Cold) Resist_15/- · DamageResist (Fire) Resist_15/- · DamageResist (Sonic) Resist_15/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Many Krath sought to be guards of their dark temples in armor of this type. Cynics dismiss this fervor, noting that guard duty was safer than participating in military slave raids.”*

**Exar Kun's Light Battle Suit** ⚠ **UNIQUE** · `a_medium_11` · K2 · Tier 3 · **6,000 credits** ⚠ *(the KOTOR 1 price, which governs; the KOTOR 2 row records 15,000)* · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Attributed to Exar Kun, this armor may well have been one of those worn by the Dark Lord prior to his defeat forty years ago. He was rarely without considerable, yet flexible, personal armor.”*

**Heavy Cinnagar War Suit** · `a_medium_12` · K2 · Tier 3 · 18,500 credits · DamageResist (Sonic) Resist_20/- · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“After the Great Hyperspace War a thousand years ago, the heirs of Empress Teta militarized their world and industry, a legacy that produced battle armor still sought after today. This heavier variety is still as flexible as medium armor, but is as protective as heavier combat suits.”*

**Verpine Fiber Ultramesh** · `a_medium_13` · K2 · Tier 4 · 22,000 credits · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This Verpine combat suit is the most protective standard medium armor available, surpassing the defensive capabilities of most heavy armor.”*

**Electromesh Armor** · `a_medium_14` · K2 · Tier 4 · 25,500 credits · DamageResist (Energy) Resist_10/- · DEXBonusMax 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This flexible armor is used by Nagai soldiers. It is highly resistant to blaster fire and is designed to allow the Nagai to fully capitalize on their naturally high dexterity.”*

**Jamoh Hogra's Battle Armor** ⚠ **UNIQUE** · `a_medium_15` · K2 · Tier 4 · **10,000 credits** ⚠ *(the KOTOR 1 price, which governs; the KOTOR 2 row records 30,000)* · Ability (Strength) 1 · Armor 4 · Immunity (Critical Hits) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Jamoh Hogra was a Zabrak mercenary who feared for his life after a raid on a Sith dreadnaught. He spent a fortune on his personal armor, only to be killed while in the bath.”*

**Zeison Sha Initiate Armor** · `a_robe_06` · K2 · Tier 1 · 350 credits · Armor 1 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. Zeison Sha initiates are known for their survival skills and resourcefulness. Their flexible armor is very durable and can be upgraded with some underlays. The Outer Rim planet Yanibar was the home of the Zeison Sha, who developed their Force powers as a means of surviving the harsh planet. Zeison Sha stress independence and survival as well as assistance to those in need.”*

**Jal Shey Neophyte Armor** · `a_robe_07` · K2 · Tier 2 · 600 credits · Ability (Charisma) 1 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 4)* · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. Jal Shey neophytes have begun their lifelong quest to understand the nature of the Force. Their light armor carries with it an aura of dignity and competence. The Jal Shey concentrate on intellectual study of the Force, seeking to understand it at a mental level, rather than a spiritual one. Jal Shey are typically exceptional diplomats, but are less successful in physical pursuits.”*

**Jal Shey Advisor Armor** · `a_robe_11` · K2 · Tier 2 · 1,300 credits · Ability (Charisma) 2 · Ability (Wisdom) 1 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 4)* · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. Jal Shey advisors possess a strong understanding of the Force and are widely respected for their wisdom. The Jal Shey concentrate on intellectual study of the Force, seeking to understand it at a mental level, rather than a spiritual one. Jal Shey are typically exceptional diplomats, but are less successful in physical pursuits.”*

**Zeison Sha Warrior Armor** · `a_robe_16` · K2 · Tier 2 · 5,000 credits · Armor 2 · Saving throw +1 ⚠ *(which save is unresolved — subtype 1)* · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. Zeison Sha Warriors are powerful combatants who are particularly skilled in telekenetic Force Powers. Their fortified garments are somewhat restrictive, but do not interfere with their use of the Force. They can be upgraded with some underlays. The Outer Rim planet Yanibar was the home of the Zeison Sha, who developed their Force powers as a means of surviving the harsh planet. Zeison Sha stress independence and survival as well as assistance to those in need.”*

**Jal Shey Mentor Armor** · `a_robe_20` · K2 · Tier 3 · 11,500 credits · Ability (Charisma) 4 · Ability (Wisdom) 1 · Armor 1 · Skill bonus +1 ⚠ *(which skill is unresolved — subtype 4)* · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. Jal Shey mentors are unparalleled in their intellect and often serve as highly respected advisors and teachers. The Jal Shey concentrate on intellectual study of the Force, seeking to understand it at a mental level, rather than a spiritual one. Jal Shey are typically exceptional diplomats, but are less successful in physical pursuits.”*

**Darth Malak's Armor** ⚠ **UNIQUE** · `a_robe_26` · K2 · Tier 4 · 25,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 1 · Armor 4 · Regeneration 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Does not restrict use of Force Powers. It is believed that Darth Malak, the fallen former apprentice of Darth Revan, once possessed this garment. Malak and Revan are credited with starting the Jedi Civil War, which led to the collapse of the Jedi Order.”*

**⚠ Name corrupted in the source** · `g1_a_class6001` · K1 · Tier 4 · 22,000 credits · DamageImmunity (Cold) ⚠ **IMMUNE** *(100%)* · DamageImmunity (Fire) ⚠ **IMMUNE** *(100%)* · DamageImmunity (Sonic) ⚠ **IMMUNE** *(100%)* · Armor 1 · Armor 1 · Armor 1 · Immunity (MindSpells) 0 · Immunity (Poison) 0 — ⚠ *Its name and description fields both carry unrelated text; the properties above are the item’s own. Recorded, not renamed.*

**⚠ Name corrupted in the source** · `g1_a_class8001` · K1 · Tier 3 · 20,000 credits · Ability (Constitution) 1 · Ability (Constitution) 3 · Ability (Strength) 2 · Ability (Strength) 3 · Armor 2 · Armor 4 — ⚠ *Its name and description fields both carry unrelated text; the properties above are the item’s own. Recorded, not renamed.*

**Armored Flight Suit** · `g_a_armrdfsuit` · K2 · Tier 1 · 200 credits · DamageResist (Cold) Resist_20/- — *“This combat-ready flight suit provides additional protection against vacuum for limited periods. Its many models appeal to a wide range of users, from military pilots and mercenaries to fringe explorers and space pirates.”*

**Military Suit** · `g_a_class6001` · K1 · Tier 1 · 150 credits · ⚠ *Species-restricted (which species is unresolved)* — *“This standard issue suit provides good protection, but can be heavier and more restrictive than some of its counterparts. Even so, many mercenaries swear the tradeoffs are worth it.”*

**Echani Battle Armor** · `g_a_class6002` · K1 · Tier 2 · 1,750 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor provides solid defense at the cost of some flexibility, although it is still an Echani product and is therefore well suited to quick-moving combat.”*

**Cinnagar War Suit** · `g_a_class6003` · K1 · Tier 2 · 3,000 credits · DamageResist (Sonic) Resist_15/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“After the Great Hyperspace War a thousand years ago, the heirs of Empress Teta militarized their world and industry, a legacy that produced battle armor still sought after today.”*

**Verpine Fiber Mesh** · `g_a_class6004` · K1 · Tier 2 · 4,250 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Raxsus Nuli had plans of planetary conquest in the wake of Sith aggression. Though eclipsed by recent events, the Jedi saw the pirate jailed and his Verpine stockpiles auctioned.”*

**Arkanian Bond Armor** · `g_a_class6005` · K1 · Tier 2 · 4,500 credits · DamageResist (Cold) Resist_20/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Ancient Arkanians pioneered many unique alloys that lose heat at a very slow rate, producing armor that is very resistant to sudden changes in temperature.”*

**Exar Kun's Light Battle Suit** ⚠ **UNIQUE** · `g_a_class6006` · K1 · Tier 3 · 6,000 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Attributed to Exar Kun, this armor may well have been worn by the Dark Lord prior to his defeat forty years ago. He was rarely without considerable, yet flexible, personal armor.”*

**Davik's War Suit** ⚠ **UNIQUE** · `g_a_class6007` · K1 · Tier 2 · 3,500 credits · DamageResist (Cold) Resist_10/- · DamageResist (Fire) Resist_10/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Davik spent lavishly on his safety, and many a bounty hunter ended up dead in the streets for underestimating both his will to live and the protective qualities of his armor.”*

**Davik's War Suit** ⚠ **UNIQUE** · `g_a_class6008` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_10/- · DamageResist (Fire) Resist_10/- · ⚠ *Species-restricted (which species is unresolved)* — *“Davik spent lavishly on his safety, and many a bounty hunter ended up dead in the streets for underestimating both his will to live and the protective qualities of his armor.”*

**Davik's War Suit** ⚠ **UNIQUE** · `g_a_class6009` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_20/- · DamageResist (Fire) Resist_20/- · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Davik spent lavishly on his safety, and many a bounty hunter ended up dead in the streets for underestimating both his will to live and the protective qualities of his armor.”*

**Light Battle Armor** · `g_a_class7001` · K1 · Tier 1 · 250 credits · ⚠ *Species-restricted (which species is unresolved)* — *“Providing solid protection for a minimal cost, this armor is excellent for entrenched troops or guards. A force on the move, however, may find it somewhat constricting.”*

**Bronzium Light Battle Armor** · `g_a_class7002` · K1 · Tier 2 · 1,500 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This molded armor is made of better materials than standard military issue, but is still relatively cheap and easy to mass-produce, making it ideal for light militias and the like.”*

**Powered Light Battle Armor** · `g_a_class7003` · K1 · Tier 2 · 3,000 credits · Ability (Strength) 1 · DamageResist (Sonic) Resist_25/- · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“This is an early attempt at power-assisted armor. Dampening fields block the noise of servomotors, unintentionally shielding against external extremes in sonic frequencies as well.”*

**Krath Heavy Armor** · `g_a_class7004` · K1 · Tier 2 · 5,000 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Typical of the old Krath military elite, these suits were worn during slave raids on neighboring systems. Slaving is profitable but risky, so little cost is spared in equipment.”*

**Krath Holy Battle Suit** · `g_a_class7005` · K1 · Tier 3 · 6,000 credits · DamageResist (Cold) Resist_15/- · DamageResist (Fire) Resist_15/- · DamageResist (Sonic) Resist_15/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Many Krath sought to be guards of their dark temples in armor of this type. Cynics dismiss this fervor, noting that guard duty was safer than participating in military slave raids.”*

**Jamoh Hogra's Battle Armor** ⚠ **UNIQUE** · `g_a_class7006` · K1 · Tier 3 · 10,000 credits · Ability (Strength) 1 · Armor 4 · Immunity (Critical Hits) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Jamoh Hogra was a Zabrak mercenary who feared for his life after a raid on a Sith dreadnaught. He spent a fortune on his personal armor, only to be killed while in the bath.”*

## Heavy — 34

**Battle Armor** · `a_heavy_01` · K2 · Tier 1 · 400 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“This isn't the heaviest of armor, but it comes close. Designed for heavy militias, it has the protection needed to keep a soldier alive during ranged combat with massive weapons.”*

**Heavy Battle Armor** · `a_heavy_02` · K2 · Tier 1 · 1,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · ⚠ *Species-restricted (which species is unresolved)* — *“More sturdy, yet more restrictive than conventional battle armor, Heavy Battle Armor is excellent in situations where mobility is of secondary concern.”*

**Echani Heavy Armor** · `a_heavy_03` · K2 · Tier 1 · 500 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Echani Heavy Armor is comparable to typical heavy battle armor in terms of protection, but allows for slightly more mobility.”*

**Durasteel Heavy Armor** · `a_heavy_04` · K2 · Tier 2 · 2,500 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Battle armor production thrived on Bonadan as the Republic recovered from war. This model heavy durasteel casing provides superior protection when compared to normal Heavy Battle Armor.”*

**Powered Battle Armor** · `a_heavy_05` · K2 · Tier 2 · 2,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · Ability (Strength) 1 · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“The micro-hydraulics of this armor provides the operator with both protection and strength enhancement. It is rarely owned by anyone other than professional mercenaries and soldiers.”*

**Flex Heavy Armor** · `a_heavy_06` · K2 · Tier 2 · 1,650 credits · Armor 1 · DEXBonusMax 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Flex Heavy Armor allows for greater mobility than even some medium armor. The primary alloy is still durasteel, but it is treated in methods that are poorly understood by most in the Republic. In fact, it is unclear who manufactures these rare suits of armor.”*

**Mandalorian Battle Armor** · `a_heavy_07` · K2 · Tier 2 · 4,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Electrical) Resist_25/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Republic soldiers saw this armor all too often during the Mandalorian War. It's understandable that the conflict could drag on when a fanatical enemy is so defensively outfitted.”*

**Mandalorian Heavy Armor** · `a_heavy_08` · K2 · Tier 3 · 8,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 3 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor is reserved for respected veteran Mandalorians. Immensely sturdy, stabilizers diffuse energy throughout the frame, shielding the wearer from disorienting impacts.”*

**Verpine Zal Alloy Mesh** · `a_heavy_09` · K2 · Tier 3 · 12,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“Using the highly expensive Zal alloy, the Verpine have developed a suit without peer. The only thing greater than the protective capabilities of this armor is the price.”*

**Mandalorian Assault Armor** · `a_heavy_10` · K2 · Tier 3 · 8,000 credits ⚠ *(reconciled to the KOTOR 1 price)* · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This was the armor of the Mandalorian elite frontline troops, a sight that Republic soldiers were all too familiar with during the war.”*

**Corellian Powersuit** · `a_heavy_11` · K2 · Tier 3 · 15,000 credits · Ability (Strength) 2 · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Essentially an improved version of powered battle armor, the powersuit employs a system of servomotors to enhance the wearer's strength.”*

**M'uhk'gfa** · `a_heavy_12` · K2 · Tier 3 · 20,000 credits · DamageResist (Bludgeoning) Resist_10/- · DamageResist (Energy) Resist_5/- · DamageResist (Piercing) Resist_10/- · DamageResist (Slashing) Resist_10/- · ⚠ *Species-restricted (which species is unresolved)* — *“Cumbersome, but powerful armor, M'uhk'gfa is the battle plate used by elite Gamorrean warriors. Traditionally, each Gamorrean warrior would fashion his own battle plate from metal fragments on the battlefields of their victories.”*

**Iotran Braceman Armor** · `a_heavy_13` · K2 · Tier 4 · 22,500 credits · BonusFeats ⚠ cut content · BonusFeats (Targeting 1) · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“The Iotran are a militaristic species from the industrial planet of Iotra on the Outer Rim. Their versatile armor is a favorite among experienced bounty hunters.”*

**Felenar Armor** · `a_heavy_14` · K2 · Tier 4 · 27,500 credits · Armor 2 · DEXBonusMax 4 · ⚠ *Species-restricted (which species is unresolved)* — *“This flexible armor is made of a variety of exotic minerals. Markings suggest that it was created by a species called the Felenar.”*

**Matrix Armor** · `a_heavy_15` · K2 · Tier 4 · 25,000 credits · DamageResist (Energy) Resist_5/- · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“Matrix armor is typically used for starship plating. Adapting it to personal use is expensive and technologically difficult. The armor is particularly resistant to blaster fire.”*

**Mandalore's Armor** ⚠ **UNIQUE** · `a_heavy_x01` · K2 · Tier 3 · 6,000 credits · DamageResist (Electrical) Resist_25/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Mandalore's personal suit of armor is traditional Mandalorian battle armor. Despite the numerous battles it has doubtless survived, it appears to be in exceptional condition. It is said that he will never voluntarily take it off, even while sleeping.”*

**Battle Armor** · `g_a_class8001` · K1 · Tier 1 · 400 credits · ⚠ *Species-restricted (which species is unresolved)* — *“This isn't the heaviest of armor, but it comes close. Designed for heavy militias, it has the protection needed to keep a soldier alive during ranged combat with massive weapons.”*

**Powered Battle Armor** · `g_a_class8002` · K1 · Tier 2 · 2,000 credits · Ability (Strength) 1 · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“The micro-hydraulics of this armor provides the operator with both protection and strength enhancement. It is rare outside of professional mercenaries and soldiers.”*

**Cinnagar Plate Armor** · `g_a_class8003` · K1 · Tier 2 · 4,000 credits · DamageResist (Sonic) Resist_25/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“While much time was spent on the appearance, this armor is still meant for the personal guards of dignitaries, and is therefore highly effective against many forms of attack.”*

**Mandalorian Armor** · `g_a_class8004` · K1 · Tier 3 · 9,000 credits · DamageResist (Sonic) Resist_25/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Mandalorians are among the most feared combatants in the galaxy, and the quality of their gear may be why. Even the lowliest warrior is a threat in such protective armor.”*

**Calo Nord's Battle Armor** ⚠ **UNIQUE** · `g_a_class8005` · K1 · Tier 3 · 10,000 credits · DamageResist (Cold) Resist_10/- · DamageResist (Fire) Resist_10/- · DamageResist (Sonic) Resist_10/- · Armor 1 · Armor 3 · Immunity (Critical Hits) 0 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Commissioned by Calo Nord, this armor was based on heavily modified Mandalorian designs. The maker was killed to appease Nord's ego, ensuring his suit would forever be unique.”*

**Calo Nord's Battle Armor** ⚠ **UNIQUE** · `g_a_class8006` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · Immunity (Critical Hits) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Commissioned by Calo Nord, this armor was based on heavily modified Mandalorian designs. The maker was killed to appease Nord's ego, ensuring his suit would forever be unique.”*

**Calo Nord's Battle Armor** ⚠ **UNIQUE** · `g_a_class8007` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · Immunity (Critical Hits) 0 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Commissioned by Calo Nord, this armor was based on heavily modified Mandalorian designs. The maker was killed to appease Nord's ego, ensuring his suit would forever be unique.”*

**Verpine Zal Alloy Mesh** · `g_a_class8009` · K1 · Tier 3 · 12,000 credits · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“Using the highly expensive Zal alloy, the Verpine have developed a suit without peer. The only thing greater than the protective capabilities of this armor is the price.”*

**Heavy Battle Armor** · `g_a_class9001` · K1 · Tier 2 · 1,000 credits · ⚠ *Species-restricted (which species is unresolved)* — *“This is the heaviest armor available for the soldier that requires maximum protection from direct damage. Some consider the fit claustrophobic, but that's the tradeoff for safety.”*

**Durasteel Heavy Armor** · `g_a_class9002` · K1 · Tier 2 · 2,500 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Battle armor production is thriving on Bonadan as the Republic recovers from war. This model's thinner skin of durasteel reduces weight, but still restricts movement somewhat.”*

**Mandalorian Battle Armor** · `g_a_class9003` · K1 · Tier 2 · 4,000 credits · DamageResist (Electrical) Resist_25/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Republic soldiers saw this armor all too often during the Mandalorian War. It's understandable that the conflict could drag on when a fanatical enemy is so defensively outfitted.”*

**Mandalorian Heavy Armor** · `g_a_class9004` · K1 · Tier 3 · 8,000 credits · Armor 3 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“This armor is reserved for respected veteran Mandalorians. Immensely sturdy, stabilizers diffuse energy throughout the frame, shielding the wearer from disorienting impacts.”*

**Jurgan Kalta's Power Suit** ⚠ **UNIQUE** · `g_a_class9005` · K1 · Tier 3 · 10,000 credits · DamageResist (Cold) Resist_10/- · DamageResist (Cold) Resist_15/- · DamageResist (Fire) Resist_10/- · DamageResist (Fire) Resist_15/- · DamageResist (Sonic) Resist_10/- · DamageResist (Sonic) Resist_15/- · Armor 1 · Armor 3 · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Aided by custom armor like this, Jurgan Kalta had no combat equal, so his enemies tried more exotic attacks. It was a gaxxan brain-slug left on a pillow that proved his undoing.”*

**Jurgan Kalta's Power Suit** ⚠ **UNIQUE** · `g_a_class9006` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · ⚠ *Species-restricted (which species is unresolved)* — *“Aided by custom armor like this, Jurgan Kalta had no combat equal, so his enemies tried more exotic attacks. It was a gaxxan brain-slug left on a pillow that proved his undoing.”*

**Jurgan Kalta's Power Suit** ⚠ **UNIQUE** · `g_a_class9007` · K1 · Tier 1 · no sale value · Armor 4 · DamageResist (Cold) Resist_30/- · DamageResist (Fire) Resist_30/- · DamageResist (Sonic) Resist_30/- · Immunity (MindSpells) 0 · ⚠ *Species-restricted (which species is unresolved)* — *“Aided by custom armor like this, Jurgan Kalta had no combat equal, so his enemies tried more exotic attacks. It was a gaxxan brain-slug left on a pillow that proved his undoing.”*

**Cassus Fett's Battle Armor** ⚠ **UNIQUE** · `g_a_class9009` · K1 · Tier 3 · 15,000 credits · Ability (Strength) 1 · DamageResist (Cold) Resist_10/- · DamageResist (Fire) Resist_10/- · DamageResist (Sonic) Resist_10/- · Armor 1 · Armor 4 · ⚠ *Species-restricted (which species is unresolved)* — *“The armor of Cassus Fett, the most wanted man in known space. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

**Mandalorian Assault Armor** · `g_a_class9010` · K1 · Tier 3 · 8,000 credits · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · Armor 4 · Disguise ⚠ *(which appearance is unresolved)* · ⚠ *Species-restricted (which species is unresolved)* — *“This was the armor of the Mandalorian elite frontline troops, a sight that Republic soldiers were all too familiar with during the war.”*

**Cassus Fett's Battle Armor** ⚠ **UNIQUE** · `g_a_class9011` · K1 · Tier 1 · no sale value · Ability (Strength) 1 · Armor 5 · DamageResist (Cold) Resist_25/- · DamageResist (Fire) Resist_25/- · DamageResist (Sonic) Resist_25/- · ⚠ *Species-restricted (which species is unresolved)* — *“The armor of Cassus Fett, the most wanted man in known space. Famous for killing the captain of a flagship Republic frigate at the Battle of Jaga's Cluster, he is presumed dead.”*

## Robes — 42

**Padawan Robe** · `a_robe_02` · K2 · Tier 1 · 50 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Jedi Order typically wear plain or unassuming garments.”*

**Dark Padawan Robe** · `a_robe_03` · K2 · Tier 1 · 50 credits ⚠ *(KOTOR 2 only — priced equal to its light twin)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple robes, kept modest not by a desire to appear humble, but to offer the greatest freedom of movement during battle.”*

**Baran Do Novice Robe** · `a_robe_04` · K2 · Tier 1 · 100 credits · Ability (Wisdom) 1 · DamageImmunity (Dark Side) ⚠ **DR 2** *(10%)* · DamageImmunity (Light Side) ⚠ **DR 2** *(10%)* · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Novices are those who have begun their training in the Baran Do philosophy, learning how to empty their minds and find tranquility in any situation. The Baran Do are force sensitive members of the Kel Dor race. They seek inner peace and are very patient, consulting with the Force before making decisions.”*

**Matukai Apprentice Robe** · `a_robe_05` · K2 · Tier 1 · 250 credits · Ability (Constitution) 1 · Ability (Dexterity) 1 · Ability (Strength) 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Matukai apprentices master physical meditation by practicing martial arts techniques. Their robes are designed to help them achieve harmony between the mind and body. The Matukai are a group of Force sensitives who use their physical body to channel the Force. The balance of the physical and spiritual is a cornerstone of their philosophy.”*

**Jedi Robe** · `a_robe_08` · K2 · Tier 2 · 100 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 1 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Jedi Order typically wear plain or unassuming garments.”*

**Dark Jedi Robe** · `a_robe_09` · K2 · Tier 2 · **100 credits** ⚠ *(the KOTOR 1 price, which governs; the KOTOR 2 row records 700)* · Armor 1 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple robes, kept modest not by a desire to appear humble, but to offer the greatest freedom of movement during battle.”*

**Norris Robe** · `a_robe_10` · K2 · Tier 2 · 1,100 credits · DamageImmunity (Energy) ⚠ **DR 4** *(20%)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Stained with pigments from the beautiful and rare norris root found on the planet Almar, these robes are naturally resistant to energy.”*

**Gray Jedi Robe** · `a_robe_12` · K2 · Tier 2 · 1,700 credits · Ability (Charisma) 2 · Armor 1 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Gray Jedi are those who, though having completed the teachings of the Jedi, operate independently and outside of the Jedi Council. They are typically seen as misguided, though they have not necessarily succumbed to the Dark Side.”*

**Jedi Knight Robe** · `a_robe_13` · K2 · Tier 2 · 150 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 2 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but this variant offers the additional protection needed by Jedi influencing important events. These robes can be upgraded with some underlays.”*

**Dark Jedi Knight Robe** · `a_robe_14` · K2 · Tier 2 · 150 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 2 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Designed for those who relish personal combat, and know that power comes to those who take it, these robes offer good protection with no hindrance to movement. These robes can be upgraded with some underlays.”*

**Matukai Adept Robe** · `a_robe_15` · K2 · Tier 2 · 4,000 credits · Ability (Constitution) 2 · Ability (Dexterity) 2 · Ability (Strength) 2 · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Matukai adepts are masters at guiding their bodies with the Force. They are capable of astounding physical feats. The Matukai are a group of Force sensitives who use their physical body to channel the Force. The balance of the physical and spiritual is a cornerstone of their philosophy.”*

**Jedi Master Robe** · `a_robe_17` · K2 · Tier 3 · 200 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 3 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but Jedi Masters also know the importance of adequate protection when great challenges must be surmounted. These robes can be upgraded with some underlays.”*

**Dark Jedi Master Robe** · `a_robe_18` · K2 · Tier 3 · 200 credits ⚠ *(reconciled to the KOTOR 1 price)* · Armor 3 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“These robes offer superior protection while still allowing full freedom of movement. They are the robes of the true masters, those whose will and authority go unopposed. These robes can be upgraded with some underlays.”*

**Baran Do Sage Robe** · `a_robe_19` · K2 · Tier 3 · 9,500 credits · Ability (Wisdom) 4 · DamageImmunity (Dark Side) ⚠ **DR 4** *(20%)* · DamageImmunity (Light Side) ⚠ **DR 4** *(20%)* · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Baran Do Sages are the most elite of their Order, able to see into the future, the past, and across the entire galaxy. The Baran Do are force sensitive members of the Kel Dor race. They seek inner peace and are very patient, consulting with the Force before making decisions.”*

**Ossus Keeper Robe** · `a_robe_21` · K2 · Tier 3 · 13,000 credits · Ability (Charisma) 2 · Ability (Intelligence) 4 · Ability (Wisdom) 4 · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“The Keepers of the Hall of Knowledge in the Great Jedi Library maintained the protected archives and acted as references to those who desired a more interactive solution to the their problems.”*

**Natth Cowling** · `a_robe_22` · K2 · Tier 3 · 15,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 3 · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Dyed with water from the tainted Lake Natth on Ambria, these robes infuse the wearer a trace of the dark powers contained within the lake.”*

**Arca Jeth's Robe** ⚠ **UNIQUE** · `a_robe_23` · K2 · Tier 3 · 17,500 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Ability (Wisdom) 2 · Armor 2 · Regeneration Force Points 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Arca Jeth was a powerful Arkanian Jedi Master who was killed in the Great Sith War. His spirit helped provide guidance to Ulic Qel-Droma.”*

**Aleema Keto's Robe** ⚠ **UNIQUE** · `a_robe_24` · K2 · Tier 3 · 19,500 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 2 · Ability (Wisdom) 4 · Armor 3 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Aleema Keto began her training as a Jedi, but while researching the Sith became enthralled by their power and fell to the Dark Side. She was a master of illusions and helped seduce Ulic Qel-Droma to the Dark Side.”*

**Sylvar's Robe** ⚠ **UNIQUE** · `a_robe_25` · K2 · Tier 4 · 20,750 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Ability (Dexterity) 2 · DamageResist (Dark Side) Resist_15/- · DamageResist (Energy) Resist_15/- · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Sylvar was a fellow student of Exar Kun and the wife of the fallen Jedi Crado, who fell to Kun's side during the Sith War many decades past. Despite several major trials, Sylvar ultimately remained true to the Light Side and was a strong voice in the Jedi Order.”*

**Jolee's Robe** ⚠ **UNIQUE** · `a_robe_27` · K2 · Tier 4 · 23,600 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 1)* 0 · Ability (Charisma) 4 · Armor 3 · Regeneration Force Points 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Jolee Bindo remained outside of the Jedi Order in his pursuit of knowledge. These powerful, yet unassuming robes were believed to have been owned by him, though his current whereabouts is unknown. These robes can be upgraded with some underlays.”*

**Thon's Robe** ⚠ **UNIQUE** · `a_robe_28` · K2 · Tier 4 · 25,400 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · BonusFeats (Force Focus) · BonusFeats (Force Immunity Stun) · BonusFeats (Force Jump) · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Thon was an enigmatic Jedi Watchman who kept even his species secret. He was a powerful agent of the Light Side and also trained many Jedi.”*

**Crado's Robe** ⚠ **UNIQUE** · `a_robe_29` · K2 · Tier 4 · 27,200 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 6 · DecreaseAbilityScore (Constitution) Penalty_-2 · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Crado was a Jedi who fell to the power of the Dark Side through the mighty Exar Kun. Crado betrayed his beloved Sylvar and was ultimately obliterated when the Cron Cluster was destroyed. Given how completely Crado was killed, it is questionable whether this robe ever actually belonged to him. Regardless, this garment clearly eminates the power and corruption of the Dark Side.”*

**Nomi's Robe** ⚠ **UNIQUE** · `a_robe_30` · K2 · Tier 4 · 30,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Ability (Wisdom) 4 · Armor 3 · Regeneration Force Points 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Nomi displayed incredible affinity for the Force, but only reluctantly pursued Jedi training following the death of her husband, Andur. She became one of the greatest Jedi of the time, training under Master Thon.”*

**Handmaiden's Robe** ⚠ **UNIQUE** · `a_robe_x01` · K2 · Tier 2 · 4,000 credits · Ability (Charisma) 2 · Armor 3 · UseLimitationPC ⚠ *(unresolved — `iprp_pc` subtype 3)* 0 · ⚠ *Species-restricted (which species is unresolved)* — *“This robe once belonged to the Handmaiden's mother, Arren. It is the only thing of hers the Handmaiden possesses. This robe can be upgraded with some underlays.”*

**Jedi Robe** · `g_a_jedirobe01` · K1 · Tier 1 · 100 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Jedi Order typically wear plain or unassuming garments.”*

**Dark Jedi Robe** · `g_a_jedirobe02` · K1 · Tier 1 · 100 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple robes, kept modest not by a desire to appear humble, but to offer the greatest freedom of movement during battle.”*

**Jedi Robe** · `g_a_jedirobe03` · K1 · Tier 1 · 100 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Jedi Order typically wear plain or unassuming garments.”*

**Jedi Robe** · `g_a_jedirobe04` · K1 · Tier 1 · 100 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Jedi Order typically wear plain or unassuming garments.”*

**Dark Jedi Robe** · `g_a_jedirobe05` · K1 · Tier 1 · 100 credits · Armor 1 · ⚠ *Species-restricted (which species is unresolved)* — *“These are simple robes, kept modest not by a desire to appear humble, but to offer the greatest freedom of movement during battle.”*

**Qel-Droma Robes** · `g_a_jedirobe06` · K1 · Tier 2 · 2,000 credits · Ability (Wisdom) 2 · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Armor 5 · ⚠ *Species-restricted (which species is unresolved)* — *“The Force is strong in the Qel-Droma blood, and many of the family have joined the Jedi Order over the centuries. These robes were created as a gift for Cay Qel-Droma during the war against Exar Kun, and it is said that only one who truly walks the path of the light can wear them. Cay himself wore the robes in his duel against Ulic Qel-Droma, his brother who had fallen to the dark side. Cay was slain in the battle, but his death at his brother's hand eventual lead to Ulic's redemption. These powerful robes then passed down to Duron Qel-Droma, Cay's cousin, when he joined the Jedi. But Duron disappeared shortly after the time of the Great Hunt, and the robes were lost with him.”*

**Jedi Knight Robe** · `g_a_kghtrobe01` · K1 · Tier 1 · 150 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but this variant offers the additional protection needed by Jedi influencing important events.”*

**Dark Jedi Knight Robe** · `g_a_kghtrobe02` · K1 · Tier 1 · 150 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Designed for those who relish personal combat, and know that power comes to those who take it, these robes offer good protection with no hindrance to movement.”*

**Jedi Knight Robe** · `g_a_kghtrobe03` · K1 · Tier 1 · 150 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but this variant offers the additional protection needed by Jedi influencing important events.”*

**Jedi Knight Robe** · `g_a_kghtrobe04` · K1 · Tier 1 · 150 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but this variant offers the additional protection needed by Jedi influencing important events.”*

**Dark Jedi Knight Robe** · `g_a_kghtrobe05` · K1 · Tier 1 · 150 credits · Armor 2 · ⚠ *Species-restricted (which species is unresolved)* — *“Designed for those who relish personal combat, and know that power comes to those who take it, these robes offer good protection with no hindrance to movement.”*

**Jedi Master Robe** · `g_a_mstrrobe01` · K1 · Tier 1 · 200 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but Jedi Masters also know the importance of adequate protection when great challenges must be surmounted.”*

**Dark Jedi Master Robe** · `g_a_mstrrobe02` · K1 · Tier 1 · 200 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“These robes offer superior protection while still allowing full freedom of movement. They are the robes of the true masters, those whose will and authority go unopposed.”*

**Jedi Master Robe** · `g_a_mstrrobe03` · K1 · Tier 1 · 200 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but Jedi Masters also know the importance of adequate protection when great challenges must be surmounted.”*

**Jedi Master Robe** · `g_a_mstrrobe04` · K1 · Tier 1 · 200 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“Members of the Order typically wear plain or unassuming garments, but Jedi Masters also know the importance of adequate protection when great challenges must be surmounted.”*

**Dark Jedi Master Robe** · `g_a_mstrrobe05` · K1 · Tier 1 · 200 credits · Armor 3 · ⚠ *Species-restricted (which species is unresolved)* — *“These robes offer superior protection while still allowing full freedom of movement. They are the robes of the true masters, those whose will and authority go unopposed.”*

**Darth Revan's Robes** ⚠ **UNIQUE** · `g_a_mstrrobe06` · K1 · Tier 2 · 2,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 3)* 0 · Ability (Strength) 4 · Armor 5 · Use Limitation Feat (Jedi Defense) · Regeneration 1 · ⚠ *Species-restricted (which species is unresolved)* — *“Created by the mystical technology of the Star Forge, these robes focus the Dark Side energies of the wearer, fueling their power. The Sith Lord Darth Revan was wearing similar robes when captured by the Jedi, who viewed the garments as an abomination and destroyed them. However the Jedi Council, not being familiar with the origins of the robes, were unaware that the Star Forge would be capable of producing an item of such terrible power a second time.”*

**Star Forge Robes** · `g_a_mstrrobe07` · K1 · Tier 2 · 2,000 credits · UseLimitationAlignmentGroup ⚠ *(unresolved — `iprp_aligngrp` subtype 2)* 0 · Ability (Wisdom) 5 · Armor 5 · Use Limitation Feat (Jedi Defense) · Saving throw +2 ⚠ *(which save is unresolved — subtype 0)* · ⚠ *Species-restricted (which species is unresolved)* — *“Created by the mystical technology of the Star Forge, these robes focus the inherent Force abilities of the wearer, fueling their power. Although the Star Forge itself is an artifact of the Dark Side, these robes were customized using an analysis of the Jedi they were created for, resulting in a powerful light side item that the Jedi can safely use against their enemies without fear of taint or corruption.”*
