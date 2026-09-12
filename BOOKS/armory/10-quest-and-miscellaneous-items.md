# Chapter Ten — Quest and Miscellaneous Items

**The things that do not fit anywhere else.** Story objects, currency, playing cards — and
two categories that this game invented outright.

**89 items, all of them catalogued below.**

---

## Quest items

**20 items:** datapads (2), droid parts (5), and story objects (13).

**Datapads and droid parts are what they sound like** — narrative props and repair
components. **Story objects** are flagged for a plot rather than built for combat.

**None of these have combat properties**, and a Gamemaster should treat them as what the
story needs them to be.

**⚠ The games file far more than thirteen things as story objects — 147 in all.** **134 of
them are upgrade components**, and they are catalogued in Chapter Six with the rest of the
upgrade tree rather than counted twice here. **What is left is the thirteen that are
genuinely story objects.**

## Miscellaneous items

**69 items across five categories.**

**Credits** (15 entries) are the currency itself, represented as an item so that it
stacks. **Misc** (3) is a small residual category — cosmetic rather than mechanical.
**Pazaak** (24) are the physical playing cards. **The other two categories are this game's
own**, and they are the subject of the next section.

**⚠ The pazaak cards exist here; pazaak's own rules do not yet exist anywhere in this
set.** The cards are catalogued regardless — **a Gamemaster who wants to run a hand of
pazaak has the props and will need to supply the game.**

## ⚠ Two categories here do not exist in either game

**This is the furthest this book goes beyond its source**, and both cases are marked
wherever they appear.

### The shock arm

**Chassis-integrated hardware for droids**, in two versions — a `1d6` standard arm that
Astromech and Remote droids **begin play with**, needing no upgrade prerequisite, and a
`2d6` advanced version **gated behind `Droid Upgrade 2`.** Both take ordinary melee grip and
cell upgrades. **Full rows are in the catalogue below.**

**⚠ A shock arm is not a weapon, and that distinction carries real consequences.** It
occupies **no weapon slot**, **cannot be disarmed, dropped or sold**, and **a droid may
still carry a blaster in its actual weapon slots.**

**It is chassis hardware — the same category a beast's claws belong to** — which means it
does not pass through this book's wield classes at all. **It is also why droids being
barred from melee weapons does not bar them from this.**

### Boots

**25 items, and they exist because KOTOR has no foot slot.**

**That is not an oversight on this book's part — it is verifiable in the games' own
equipment table**, which covers implant, head, armour, hands, arms, weapons and belt, **and
nothing below the waist.**

**The belt category was used as the template** — utility-flavoured, spread across all four
tiers — and the item codes use the `a_boots_NN` pattern, **which is unused in both games'
item sets**, so they collide with nothing.

> **This is new equipment rather than a conversion, and it is the clearest example in this
> book of this game adding to KOTOR's design rather than translating it.**

---

# The catalogue

**All 89 items, by category**, with resref, which game each comes from, tier, price and the
item's own description.

**⚠ Six descriptions are truncated in the games' own data** and are marked where they occur.
The truncation is the source's, not this book's.

**⚠ `no sale value` means a price of zero in the item file** — a keycard or a comlink cannot
be sold. It does not mean the item is worthless to a party.

---

# Quest items

## Datapads — 2

**Datapad** · `g_i_datapad001` · K2+K1 · Tier 1 · 1 credit — *“Data storage devices like these are common, though they may vary in quality depending on what features are included.”*

**Datapad** ⚠ **UNIQUE** · `geno_datapad` · K1 · Tier 2 · 1,250 credits — *“This datapad contains a single short, cryptic message: The Genoharadan say to see Hulas on Manaan. Come alone or not at all.”*

## Droid parts — 5

**These five are the HK rebuild parts.** Four of them are the droid-construction parts Chapter Fourteen builds from; **the fifth, the `HK Protocol Pacifist Package`, is a behaviour-core download for one particular droid rather than a construction part**, and Chapter Fourteen says so.

**HK Droid Processor** · `hkpart01` · K2 · Tier 1 · 327 credits — *“This item looks like a digitally encoded processor for an HK unit.”*

**HK Chassis** · `hkpart02` · K2 · Tier 2 · 1,500 credits — *“The chassis for this HK unit looks largely intact except for some noticeable blaster scoring in the chest region, where the control cluster would be.”*

**HK Control Cluster** · `hkpart03` · K2 · Tier 1 · 250 credits — *“This control cluster looks like it was singed by blaster fire, but it looks like the durasteel shell surrounding kept it intact despite the damage.”*

**HK Vocabulator** · `hkpart04` · K2 · Tier 1 · 114 credits — *“This device looks like an HK vocabulator unit that allows a droid to speak and communicate with others.”*

**HK Protocol Pacifist Package** · `hkpart05` · K2 · Tier 1 · 215 credits — *“This upgrade looks like it is designed to be downloaded into a droid's behavior core.”*

## Story objects — 13

**Broken Item** · `brokenitem` · K2 · Tier 1 · 5 credits — *“This might once have been used as components or chemicals, but now is almost worthless. (Bashing containers can sometimes damage fragile contents).”*

**Comlink** ⚠ **UNIQUE** · `comlink` · K2 · Tier 1 · no sale value — *“Comlinks are a standard, short range communication device. [Party members can use it to contact you to provide information or warn you of danger.]”*

**Gizka Poison** · `g_i_gizkapois001` · K1 · Tier 1 · 350 credits — *“Any gizka ingesting one of these toxic pellets will die within a few seconds. It will also cause the creature to attack all other gizka in the area, infecting them as well.”*

**Keycard** · `g_i_pltuseitm01` · K2+K1 · Tier 1 · no sale value — *“Keycards are the standard method of accessing most of the technology used in Republic space. Each card has a specific purpose and is designed to be almost tamper-proof.”*

**Armor Reinforcement** · `g_i_upgrade005` · K2+K1 · Tier 1 · 350 credits — *“Special: Upgrade Item, Armor Durasteel reinforcement is a complicated armor application that increases protective qualities. The modifications require a workbench with adequate tools and armor of high quality marked as”* ⚠ *(description truncated in source)*

**Mesh Underlay** · `g_i_upgrade006` · K2+K1 · Tier 1 · 300 credits — *“Special: Upgrade Item, Armor Mesh underlay can have a variety of effects, depending on the nature of the armor it is applied to. The modifications require a workbench with adequate tools and armor of high quality marked as”* ⚠ *(description truncated in source)*

**Durasteel Bonding Alloy** · `g_i_upgrade008` · K2+K1 · Tier 1 · 100 credits — *“Special: Upgrade Item, Melee Application of this alloy can strengthen a melee weapon, increasing damage and possibly resistance to damage. The modifications require a workbench with adequate tools and a weapon of high quality marked as”* ⚠ *(description truncated in source)*

**Energy Projector** · `g_i_upgrade009` · K2+K1 · Tier 1 · 150 credits — *“Special: Upgrade Item, Melee This modular projector can cause a melee weapon to do additional energy-based damage. The modifications require a workbench with adequate tools and a weapon of high quality marked as”* ⚠ *(description truncated in source)*

**Lightsaber Energy Cell Fixture** ⚠ **UNIQUE** · `lspart01` · K2 · Tier 1 · no sale value — *“The energy cell is one of three components needed to construct a lightsaber. This basic fixture can later be enhanced with an energy cell upgrade.”*

**Lightsaber Emitter Fixture** ⚠ **UNIQUE** · `lspart02` · K2 · Tier 1 · no sale value — *“The emitter is one of three components needed to construct a lightsaber. This basic fixture can later be enhanced with an emitter upgrade.”*

**Lightsaber Focusing Lens Fixture** ⚠ **UNIQUE** · `lspart03` · K2 · Tier 1 · no sale value — *“The focusing lens is one of three components needed to construct a lightsaber. This basic fixture can later be enhanced with a lens upgrade.”*

**Absorption Underlay Mk 1** · `ptar_sbpasscrd` · K1 · Tier 1 · no sale value — *“Mesh Underlay Mk 2”* ⚠ *(description truncated in source)*

**Krayt Dragon Pearl** · `tat18_dragonprl` · K1 · Tier 2 · 2,500 credits — *“Special: Upgrade Item, Lightsaber Damage: +2 Attack: +3 Taken from the gullet of a krayt dragon, this crystalline "pearl" appears to have refractory qualities that might allow it to function as a lightsaber crystal once”* ⚠ *(description truncated in source)*

---

# Miscellaneous items

## Credits — 15

**Currency as an item, in fifteen denominations.** The `Cost` column is the face value.

**Credits** · `g_i_credits001` · K2+K1 · Tier 1 · no sale value — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits002` · K2+K1 · Tier 1 · 10 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits003` · K2+K1 · Tier 1 · 25 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits004` · K2+K1 · Tier 1 · 50 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits005` · K2+K1 · Tier 1 · 100 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits006` · K2+K1 · Tier 1 · 200 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits007` · K2+K1 · Tier 1 · 300 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits008` · K2+K1 · Tier 1 · 400 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits009` · K2+K1 · Tier 1 · 500 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits010` · K2+K1 · Tier 2 · 1,000 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits011` · K2+K1 · Tier 2 · 2,000 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits012` · K2+K1 · Tier 2 · 3,000 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits013` · K2+K1 · Tier 2 · 4,000 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits014` · K2+K1 · Tier 2 · 5,000 credits — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

**Credits** · `g_i_credits015` · K2+K1 · Tier 1 · 1 credit — *“Republic credits are the standard monetary unit in the galaxy. Other units may be traded on some of the Rim worlds, but all can generally be transferred into the Republic credit.”*

## Misc — 3

**Aesthetic Item** · `g_i_asthitem001` · K2+K1 · Tier 1 · no sale value — *“There are a number of unique items in the universe. You have just found one.”*

**Pazaak Deck** ⚠ **UNIQUE** · `g_i_pazdeck` · K2+K1 · Tier 1 · no sale value — *“This is a standard pazaak deck, complete with side deck cards.”*

**Recording Rod** · `g_i_recordrod01` · K1 · Tier 1 · no sale value — *“These rods are used to record audio logs. They are popular among researchers and politicians.”*

## Pazaak — 24

**Pazaak Card +1** · `g_i_pazcard_001` · K2+K1 · Tier 1 · 100 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +2** · `g_i_pazcard_002` · K2+K1 · Tier 1 · 75 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +3** · `g_i_pazcard_003` · K2+K1 · Tier 1 · 50 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +4** · `g_i_pazcard_004` · K2+K1 · Tier 1 · 25 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +5** · `g_i_pazcard_005` · K2+K1 · Tier 1 · 12 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +6** · `g_i_pazcard_006` · K2+K1 · Tier 1 · 5 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -1** · `g_i_pazcard_007` · K2+K1 · Tier 1 · 100 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -2** · `g_i_pazcard_008` · K2+K1 · Tier 1 · 75 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -3** · `g_i_pazcard_009` · K2+K1 · Tier 1 · 25 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -4** · `g_i_pazcard_010` · K2+K1 · Tier 1 · 25 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -5** · `g_i_pazcard_011` · K2+K1 · Tier 1 · 12 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card -6** · `g_i_pazcard_012` · K2+K1 · Tier 1 · 5 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-1** · `g_i_pazcard_013` · K2+K1 · Tier 1 · 200 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-2** · `g_i_pazcard_014` · K2+K1 · Tier 1 · 150 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-3** · `g_i_pazcard_015` · K2+K1 · Tier 1 · 125 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-4** · `g_i_pazcard_016` · K2+K1 · Tier 1 · 100 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-5** · `g_i_pazcard_017` · K2+K1 · Tier 1 · 75 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/-6** · `g_i_pazcard_018` · K2+K1 · Tier 1 · 50 credits — *“This is a standard pazaak side deck card, for use with a pazaak deck.”*

**Pazaak Card +/- 1/2** · `g_i_pazcard_019` · K2 · Tier 1 · 500 credits — *“This is an advanced pazaak side deck card, for use with a pazaak deck. This card can change both its sign and its value.”*

**Pazaak Card Double** · `g_i_pazcard_020` · K2 · Tier 1 · 200 credits — *“This is an advanced pazaak side deck card, for use with a pazaak deck. This card doubles the value of last flipped card.”*

**Pazaak Card Tie Breaker** · `g_i_pazcard_021` · K2 · Tier 1 · 300 credits — *“This is an advanced pazaak side deck card, for use with a pazaak deck. If the score is tied (and the opponent has chosen to stand), then playing this card results in a win.”*

**Pazaak Card Flip 2&4** · `g_i_pazcard_022` · K2 · Tier 1 · 150 credits — *“This is an advanced pazaak side deck card, for use with a pazaak deck. This card changes the sign (positive or negative) of all of your 2s and 4s in play.”*

**Pazaak Card Flip 3&6** · `g_i_pazcard_023` · K2 · Tier 1 · 175 credits — *“This is an advanced pazaak side deck card, for use with a pazaak deck. This card changes the sign (positive or negative) of all of your 3s and 6s in play.”*

**Pazaak Side Deck** ⚠ **UNIQUE** · `g_i_pazsidebd001` · K2+K1 · Tier 1 · no sale value — *“Pazaak requires both a main deck and a side deck. You can store all your side deck cards here and bring them out when you start a game.”*

---

# ⚠ Authored — the two categories that are this game's own

## Shock arms — 2

**⚠ Shock Arm** · `a_shockarm_01` · ⚠ AUTHORED · Tier 1 · 120 credits · **1d6 electrical, 20 ×2** · ⚠ **yes — `melee/grip`, `melee/cell`** · ⚠ **Chassis standard: `Astromech` and `Remote` begin play with one. No `Droid Upgrade` prerequisite.** — *“A manipulator arm with a discharge coil in the wrist. Every astromech has one; most never use it for anything but spot-welding.”*

**⚠ Advanced Shock Arm** · `a_shockarm_02` · ⚠ AUTHORED · Tier 2 · 500 credits · **2d6 electrical, 20 ×2** · ⚠ yes · ⚠ **Use Limitation Feat (`Droid Upgrade 2`)** — *“A heavier coil and a second capacitor. The arm was never meant to carry this and the housing scorches. ⚠ The naming follows the game's own — `Stun Ray` to `Advanced Stun Ray`, `Flame Thrower` to `Advanced Flame Thrower`.”*

## Boots — 25

**Dockworker's Treads** · `a_boots_01` · ⚠ AUTHORED · Tier 1 · 40 credits — *“Thick-soled and unglamorous, standard issue on a hundred cargo docks. The grip is the point.”*

**Spacer's Magboots** · `a_boots_02` · ⚠ AUTHORED · Tier 1 · 75 credits · Skill: Athletics +1 — *“Electromagnetic soles that hold to a hull plate. Every freighter crew owns a pair and most have never switched them on.”*

**Tarisian Streetwalkers** · `a_boots_03` · ⚠ AUTHORED · Tier 1 · 60 credits · Skill: Stealth +1 — *“Soft-soled and cut low, made for the Lower City where being heard is being found.”*

**Dune Striders** · `a_boots_04` · ⚠ AUTHORED · Tier 1 · 90 credits · ⚠ Saving Throws: Fortitude +1 vs heat — *“Layered wraps over a hardened sole. Tatooine sand gets into everything; these take longer than most.”*

**Kashyyyk Climbing Boots** · `a_boots_05` · ⚠ AUTHORED · Tier 2 · 400 credits · Skill: Athletics +2 — *“Wroshyr bark grips wroshyr bark. The Wookiees do not sell these so much as permit their manufacture.”*

**Republic Marching Boots** · `a_boots_06` · ⚠ AUTHORED · Tier 2 · 550 credits · ⚠ Saving Throws: Fortitude +1 — *“Issued by the quartermaster and complained about by everyone who has ever worn them. They outlast the complaints.”*

**Sith Trooper Greaves** · `a_boots_07` · ⚠ AUTHORED · Tier 2 · 900 credits · ⚠ Defence +1 — *“Armoured to the knee. The sound they make on a deck plate is deliberate.”*

**⚠ Corellian Smuggler's Softsoles** · `a_boots_08` · ⚠ AUTHORED · Tier 4 · 28,000 credits · ⚠ **Skill: Stealth +5 · Dexterity +1** — *“No metal anywhere in the construction — not a rivet, not a lace eyelet. Corellian-made, and the only pair a spice runner will ever admit to owning. Customs scanners find nothing because there is nothing to find.”*

**Echani Duelling Slippers** · `a_boots_09` · ⚠ AUTHORED · Tier 2 · 1,200 credits · ⚠ Dexterity +1 — *“Almost nothing between foot and floor. An Echani will tell you that is the point and decline to elaborate.”*

**Mandalorian Battle Greaves** · `a_boots_10` · ⚠ AUTHORED · Tier 3 · 6,500 credits · ⚠ Defence +2 · Saving Throws: Fortitude +1 — *“Beskar-faced and older than the wearer, most likely. Mandalorians do not discard armour; they inherit it.”*

**Cortosis-Weave Boots** · `a_boots_11` · ⚠ AUTHORED · Tier 3 · 9,000 credits · ⚠ Damage Resistance: Energy 2 — *“A thin cortosis lattice through the sole and upper. Expensive, heavy, and the reason some duellists still have legs.”*

**Jedi Traveller's Boots** · `a_boots_12` · ⚠ AUTHORED · Tier 3 · 8,000 credits · ⚠ Saving Throws: Will +1 · Skill: Athletics +2 — *“Plain, hard-wearing, and repaired rather than replaced. A Jedi who has worn out three pairs has been somewhere.”*

**Zeltron Gravity Shoes** · `a_boots_13` · ⚠ AUTHORED · Tier 3 · 11,000 credits · ⚠ Dexterity +2 — *“Miniature repulsors take a fraction of the wearer's weight. Ostentatious, effective, and audible to anyone listening for them.”*

**Refinery Sole-Guards** · `a_boots_16` · ⚠ AUTHORED · Tier 1 · 55 credits · ⚠ Saving Throws: Fortitude +1 vs acid — *“Chemical-resistant to the ankle. Standard on any world where the ground occasionally eats people.”*

**Ithorian Wading Boots** · `a_boots_17` · ⚠ AUTHORED · Tier 1 · 70 credits · Skill: Survival +1 — *“Broad and flat, made for herd-work in wetland restoration zones. They look ridiculous and they do not sink.”*

**Salvager's Steel-Toes** · `a_boots_18` · ⚠ AUTHORED · Tier 1 · 85 credits · Skill: Repair +1 — *“A plate over the toe and a magnetic strip in the heel that holds dropped fasteners. Scavengers swear by the heel.”*

**Undercity Waders** · `a_boots_19` · ⚠ AUTHORED · Tier 1 · 45 credits · ⚠ Saving Throws: Fortitude +1 vs disease — *“Sealed to mid-calf. What runs in the Taris Undercity is not water and the boots know it.”*

**Cantina Dress Boots** · `a_boots_20` · ⚠ AUTHORED · Tier 1 · 120 credits · Skill: Persuade +1 — *“Polished, impractical, and worth precisely what the person across the table thinks they cost.”*

**Selkath Pressure Boots** · `a_boots_21` · ⚠ AUTHORED · Tier 2 · 480 credits · ⚠ Saving Throws: Fortitude +2 vs pressure — *“Rated for the Hrakert shelf. Manaan sells them freely and will not explain how they are made.”*

**Czerka Surveyor's Boots** · `a_boots_22` · ⚠ AUTHORED · Tier 2 · 620 credits · Skill: Awareness +2 — *“Sensor plates in the sole read substrate density as you walk. Czerka issues them and bills the client.”*

**Onderon Ridgewalkers** · `a_boots_23` · ⚠ AUTHORED · Tier 2 · 700 credits · Skill: Athletics +1 · Skill: Survival +1 — *“Cut for the beast-trails above Iziz, where a slip is a long way down and a short way to a drexl.”*

**Sith Academy Initiate Boots** · `a_boots_24` · ⚠ AUTHORED · Tier 2 · 850 credits · ⚠ Saving Throws: Will +1 — *“Issued on Korriban and reclaimed from the dead. Most pairs have had several owners and none of them chose the colour.”*

**Nar Shaddaa Slipsoles** · `a_boots_25` · ⚠ AUTHORED · Tier 2 · 1,050 credits · Skill: Stealth +2 · Skill: Sleight of Hand +1 — *“Sold in the refugee quarter by someone who will not be there tomorrow. They work, which is the surprising part.”*

**Krath War Boots** · `a_boots_14` · ⚠ AUTHORED · Tier 4 · 24,000 credits · ⚠ Defence +3 · Damage Resistance: Energy 3 — *“Salvaged from a war fifty years gone. The Krath built for a kind of fighting nobody does any more.”*

**Vanguard Assault Boots** · `a_boots_15` · ⚠ AUTHORED · Tier 4 · 31,000 credits · ⚠ Defence +3 · Dexterity +1 · Saving Throws: Fortitude +2 — *“Powered ankle assists and a sealed sole. The closest thing to walking armour anyone makes at this scale.”*
