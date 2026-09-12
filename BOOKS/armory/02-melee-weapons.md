# Chapter Two — Melee Weapons

**Every melee weapon in both games**, organised by base weapon type, split Base versus
Advanced, and ordered by tier within each. **Wield classes and critical-hit resolution are
taught in Chapter One and not restated here.**

**Where the two games give a shared weapon genuinely different values, KOTOR 1's are
used** — this game is set in 3,956 BBY, and K1 is that era.

**Two kinds of entry are left out deliberately**: nameless placeholder items used to dress
non-player characters, and the innate attacks of creatures. **Neither is something a
character finds, buys or carries.**

**Every weapon in a family shares its family's base die.** What separates an Advanced entry
from a Base one is the properties layered on top of it.

---

# One-handed weapons

## Stun Baton — base die `1`, threat 20 / ×2

Minimal damage; the weapon is the stun effect, not the hit.

### Base

**Stun Baton** · `g_w_stunbaton01` · K1 · Tier 1 · 30 credits · *OnHit: Stun 10*
*"A common weapon, stun batons do minimal damage but can incapacitate a target. The
high-density cells needed for repeated discharge are unwieldy, making it unusable in
the off-hand."*

### Advanced

**Energy Baton** · `w_melee_03` · K2 · Tier 1 · 75 credits · *+1d3 piercing · OnHit:
Stun 14* — *"Energy Batons are commonly employed by police forces who prefer to
incapacitate instead of kill their targets."*

**Bothan Stun Stick** · `g_w_stunbaton02` · K1 · Tier 1 · 230 credits · *Enhancement 1 ·
OnHit: Stun 14* — *"A useful tool for espionage, this weapon is more effective than the
standard stun baton, but is still available on most worlds."*

**Bothan Chuka** · `g_w_stunbaton03` · K1 · Tier 1 · 480 credits · *Enhancement 2 ·
OnHit: Stun 14* — *"A very effective device used by Bothan elite. Some systems consider
simple possession of one as grounds for execution as a spy."*

**Exchange Negotiator** · `w_melee_08` · K2 · Tier 2 · 850 credits · *+1d6 piercing ·
OnHit: Stun 18* — *"A useful tool for espionage, this weapon is more effective than the
standard stun baton, but is still available on most worlds."*

**Rakatan Battle Wand** · `g_w_stunbaton04` · K1 · Tier 2 · 1,480 credits · *Attack +2 ·
+2 electrical · +1d10 ion · Enhancement 2 · OnHit: Stun 14 and 18* — *"Weighted to fit a
Rakatan grip, this item is most like a stun baton. It seems more adaptable than one of
Republic issue."* Three further found-only forms exist at no purchase price
(`g_w_stunbaton05` through `07`), escalating Enhancement to 3 and 4 and adding ion
damage at the top step.

**On `Energy Baton` and `Exchange Negotiator`:** both are genuinely `Stun_Baton` base
items despite K2 numbering them generically rather than continuing K1's naming. The
`1d4` and `1d6` they appear to deal are Damage properties layered on the item, not the
base type's own die.

## Short Sword — base die `1d6`, threat 20 / ×2

### Base

**Short Sword** · `g_w_shortswrd01` · K1 · Tier 1 · 20 credits · *no properties* —
*"Disregarded by most modern warriors, a good short sword can still serve well in
combat if the user is skilled."* K2 carries it identically as `w_melee_01`.

### Advanced

**Massassi Brand** · `g_w_shortswrd02` · K1 · Tier 1 · 75 credits · *Enhancement 1* —
*"During the reign of Naga Sadow the Massassi were transformed into foot soldiers for
the Sith. This was their traditional weapon, altered, as they were, to serve the Dark
Side."*

**Teta's Blade** ⚠ unique · `g_w_shortswrd03` · K1 · Tier 2 · 1,250 credits ·
*Enhancement 3 · OnHit: Poison 10* — *"Attributed to Empress Teta, this blade speaks of
her background as a warrior and her willingness to be on the frontline of the Great
Hyperspace War a thousand years ago."*

**Rodian Blade** · `w_melee_11` · K2 · Tier 2 · 1,150 credits · *Attack +1 · OnHit:
Ability Drain 14* — *"This serrated weapon inflicts great pain upon its victims. Its
design is unsuitable for weapon upgrades."*

**Rodian Death Blade** · `w_melee_17` · K2 · Tier 3 · 6,000 credits · *Attack +1 · +1
slashing · OnHit: Ability Drain 10 and 14* — *"A more advanced version of the Rodian
blade, this savage weapon leaves its victim writhing in pain."*

**Ryyk Blade** · `w_melee_19` · K2 · Tier 3 · 9,000 credits · *+3 slashing ·
Enhancement 2* — *"These short blades are typically used in pairs by Wookiees who prefer
seeing their victims up close before gutting them."*

**Twi'lek Spinning Blade** · `w_melee_x02` and `w_melee_x03` · K2 · Tier 3 · 10,000
credits each · *Attack +1 / +2 slashing respectively, both OnHit: Ability Drain 18* —
*"The deadly Twi'lek Twin Suns each wielded one of these deadly blades."* Two resrefs
because they were a matched pair, one per twin.

## Vibroblade — base die `1d10`, threat 19–20 / ×2

Small enough to serve as an off-hand weapon; cortosis-woven against lightsabers.

### Base

**Vibroblade** · `g_w_vbroshort01` · K1 · Tier 1 · 100 credits · *no properties* —
*"Its small size makes this a good off hand weapon. Echani vibroblades use a rare
cortosis weave to prevent lightsaber sparring damage, allowing traditional swordplay to
continue in the time of Jedi and Sith."* K2 carries it identically as `w_melee_05`.

### Advanced

**Mission's Vibroblade** ⚠ unique · `g_w_vbroshort08` · K1 · Tier 1 · 80 credits ·
*Attack +2 · +1 bludgeoning · +1 energy* — *"Working with few resources, Mission Vao
turned this basic vibroblade into an exceptional weapon almost as adaptable as she
is."*

**Prototype Vibroblade** · `g_w_vbroshort09` · K1 · Tier 1 · 80 credits · *Attack +3 ·
+4 slashing across four properties* — *"A very adaptable model of vibroblade, made for
the user on a budget that will be purchasing upgrades as resources or finances become
available."*

**Vibrocutter** · `vibrocutter` · K2 · Tier 1 · found only · *no properties* — *"This
vibrocutter is used for carving asteroid rock, and it can double as a melee weapon if
necessary."*

**Krath Blood Blade** · `g_w_vbroshort02` · K1 · Tier 1 · 250 credits · *Enhancement 1*
— *"Twisted by the Dark Side, this Krath weapon is as deadly as a modern vibroblade. It
was meant for assassination."*

**Echani Vibroblade** · `g_w_vbroshort03` · K1 · Tier 2 · 1,000 credits · *+2 cold ·
Enhancement 2* — *"Some Echani vibroblades are supercooled to keep them in alignment,
giving them an icy sting."*

**Zabrak Vibroblade** · `w_melee_10` · K2 · Tier 2 · 1,000 credits · *grants Finesse
Melee Weapons · +2 piercing* — *"Though believed to have been constructed by the Zabrak,
this vibroblade is rarely used by them. The Zabrak feel their combat skills sufficient
to make this weapon's fine balance irrelevant."*

**Sanasiki's Blade** ⚠ unique · `g_w_vbroshort04` · K1 · Tier 3 · 7,000 credits ·
*Attack +2 · +1d6 energy · +3 vs droid · Enhancement 2 · Keen* — *"Sanasiki used this
weapon to kill Nelinik, a Zabrak who assassinated the Echani High Protector with battle
droids."* Three found-only forms follow (`vbroshort05` through `07`), trading the
energy damage for ion and slashing and gating behind `Power Attack`.

**Tehk'la Blade** · `w_melee_27` · K2 · Tier 4 · 23,000 credits · *Attack +1 · grants
Critical Strike and Improved Critical Strike · +5 slashing* — *"This weapon is favored
by the Nagai, a species of slender humanoids who appear more dead than alive."*

## Long Sword — base die `1d12`, threat 20 / ×2

### Base

**Long Sword** · `g_w_lngswrd01` · K1 · Tier 1 · 25 credits · *no properties* — *"Here is
where the roots of the lightsaber begin, with traditional swords still wielded today in
many primitive cultures. They are simple, but still effective in the right hands."* K2
carries it identically as `w_melee_02`.

### Advanced

**Krath War Blade** · `g_w_lngswrd02` · K1 · Tier 1 · 150 credits · *Enhancement 1* —
*"Twisted by the Dark Side, the Krath tempered swords with the power of the Force
perhaps even before lightsabers became the weapon of the Jedi, both dark and light."*

**Naga Sadow's Poison Blade** ⚠ unique · `g_w_lngswrd03` · K1 · Tier 2 · 1,500 credits ·
*Enhancement 3 · OnHit: Poison 10* — *"The mere presence of Dark Lord Naga Sadow would
come to imbue his personal weapons with the taint he carried, poisoned as his spirit
was."*

**Trandoshan Sword** · `w_melee_13` · K2 · Tier 2 · 2,050 credits · *Attack +1 · +4
slashing · Massive Criticals +4* — *"While most cultures abandoned the primitive sword
in favor of vibroblades, the Trandoshan sometimes use the weapon as a badge of honor.
This variant is made of the rare ore Chalon."*

**Shyarn** · `w_melee_24` · K2 · Tier 3 · 18,000 credits · *Attack +1 · grants Flurry and
Improved Flurry · +5 slashing* — *"This primitive looking weapon hails from the Cerean
species, who employ it in traditional honor duels. Shyarn are magnetically attracted to
each other, often locking together."*

## Gamorrean Battleaxe — base die `1d12`, threat 20 / ×2

Heavy, unsubtle, and the family with the steepest attack penalties at its top end.

### Base

**Gamorrean Battleaxe** · `g_w_waraxe001` · K1 · Tier 1 · 20 credits · *no properties* —
*"Gamorrean Battleaxes, much like their namesake species, are heavy, unsubtle, and
generally a very damaging influence in almost any situation."*

### Advanced

**Gamorrean War Axe** · `w_melee_09` · K2 · Tier 2 · 800 credits · *+1d8 slashing* — same
description as the base axe.

**Gamorrean Cleaver** · `w_melee_16` · K2 · Tier 2 · 4,000 credits · *Attack −2 · +1d12
slashing · OnHit: Stun 14* — *"Though a most unwieldy weapon, the target of a Gamorrean
Cleaver gets few opportunities to make mistakes."*

**Arg'garok** · `w_melee_25` · K2 · Tier 3 · 18,500 credits · *Attack −5 · grants Power
Attack and Improved Power Attack · +2d12 slashing · OnHit: Stun 18* — *"The impressive
Arg'garok is the most prized Gamorrean weapon. These huge axes are designed to be
wielded by those with a low center of gravity and tremendous strength, making them
awkward for most non-Gamorreans to use."* The −5 attack penalty is the mechanical form
of that awkwardness.

## Vibrosword — base die `1d12`, threat 19–20 / ×2

### Base

**Vibrosword** · `g_w_vbroswrd01` · K1 · Tier 1 · 120 credits · *no properties* —
*"Ultrasonic generators power this Echani-developed weapon design. A rare cortosis weave
that protects against sparring damage ensures that traditional swordplay will endure in
the time of lightsabers."* K2 carries it as `w_melee_06`, identical but for one word of
description.

### Advanced

**Krath Dire Sword** · `g_w_vbroswrd02` · K1 · Tier 1 · 250 credits · *Enhancement 1* —
*"This was a weapon of distinction in the time of the Krath. Sith would grant these
cortosis-laced blades to only the most loyal underlings."*

**Sith Tremor Sword** · `g_w_vbroswrd03` · K1 · Tier 2 · 980 credits · *+2 sonic ·
Enhancement 2* — *"Traced to the Bladeborn, a Sith offshoot dedicated to sword mastery,
these cortosis-laced weapons were given to 'masterblades' who survived no less than ten
lightsaber-wielding warriors in combat."* **K2's version of this weapon carries sonic 3
rather than 2 — a genuine difference between the games, and K1's value is the one used
here.**

**Echani Foil** · `g_w_vbroswrd04` · K1 · Tier 2 · 1,750 credits · *Enhancement 3 · Keen*
— *"These swords were crafted to honor Raskta Fenni, the best Echani duelist of her
time. Imperfections in the difficult lightsaber-deflecting cortosis weave caused few to
survive."*

**GenoHaradan Poison Blade** · `geno_blade` · K1 · Tier 2 · 1,750 credits · *Enhancement
3 · OnHit: Poison 14* — *"Forged by the Genoharadan for the exclusive use of their
agents, this deadly assassin's blade contains a cannister that emits small doses of
poison with each successful hit."*

> **⚠ This weapon's damage die is not settled.** It reads `2d6` in the game data while
> every other weapon in this family reads `1d12`. **It may belong to a different family
> than its damage suggests, or it may simply be an error the games never corrected.**
> **Until that is resolved, treat `1d12` as the working value and `2d6` as the reading a
> Gamemaster could defend.**

**Bacca's Ceremonial Blade** ⚠ unique · `g_w_vbroswrd05` · K1 · Tier 2 · 2,480 credits ·
*+4 energy · +2d6 vs droid · Enhancement 2 (×2) · Massive Criticals 2d6* — *"The great
Bacca was hunting the Shadowlands ages ago when an alien ship crashed through the
forest. He saw that first contact as a warning of the destruction outsiders could bring.
Made from the debris..."* Three further found-only forms (`vbroswrd06` through `08`)
swap the flat energy damage for an `AttackBonus` and `Keen`, gated behind `Critical
Strike` or `Flurry`.

**Echani Vibrosword** · `w_melee_21` · K2 · Tier 3 · 13,500 credits · *+2 cold ·
Enhancement 2* — the two-handed family's cold-damage treatment applied to a one-handed
blade.

**Baragwin Assault Blade** · `g1_w_vbroswrd01` · K1 · Tier 3 · 9,000 credits · *Attack
+5 · +2d6 energy · +2d6 sonic · Keen* — *"This advanced vibrosword is a miracle of miniaturization technology. Not only
does it deliver increased functionality over a normal vibrosword..."* Name resolved from string reference 48160; see Chapter Six for the
identification history.

---

# Two-handed weapons

## Quarterstaff — base die `1d6`, threat 20 / ×2

The cheapest weapon in either game, and the family K2 built three of its stranger
weapons on.

### Base

**Quarterstaff** · `g_w_qtrstaff01` · K1 · Tier 1 · 2 credits · *no properties* —
*"Usually just a smooth staff of wood or light alloys, this is a very simple weapon of
ancient design."* K2 carries it identically as `w_melee_04`.

### Advanced

**Killstick** · `killstick` · K2 · Tier 1 · 2 credits · *properties come from fitted
crystals* — carries the Quarterstaff's own description, but takes lightsaber crystals,
making it the one non-lightsaber weapon in either game that uses that upgrade path.

**Massassi Battle Staff** · `g_w_qtrstaff02` · K1 · Tier 1 · 30 credits · *Enhancement 3*
— *"The Massassi were a proud race altered by the Sith millennia ago, and subsequently
exterminated along with Exar Kun. This weapon was the symbol of a proven warrior."*

**Handmaiden's Staff** ⚠ unique · `w_melee_x01` · K2 · Tier 2 · 1,000 credits · *Attack
+2 · +1d6 bludgeoning · Armor 1 · restricted to one character* — *"Handmaiden's staff
once belonged to her father, a powerful Echani general."*

**Geonosian Electro-Staff** · `w_melee_26` · K2 · Tier 4 · 20,950 credits · *+3d6
electrical across two properties* — *"Geonosians are winged bipeds covered with
protective bony plates. Their electro-staves therefore only rarely find their way off of
their homeworld."*

## Gaffi Stick — base die `1d8`, threat 20 / ×2

### Base

**Gaffi Stick** · `g_w_gaffi001` · K1 · Tier 1 · 20 credits · *no properties* — *"The
gaffi stick, or gaderffii, is the traditional melee weapon of the Sand People. Crafted
out of whatever salvage is at hand, they can be very effective in close combat."*

### Advanced

**Raito's Gaderffii** ⚠ unique · `g_w_qtrstaff03` · K1 · Tier 2 · 980 credits ·
*Enhancement 5* — *"This may have belonged to a Sand People warrior famous among his
kind for killing a young Jedi, but the one tribe that kept the oral history of this
event was wiped out long ago."* Note the resref sits in the Quarterstaff range while the
weapon carries the Gaffi Stick's `1d8` die — one of several places where resref stem and
base type disagree.

**Gand Silencer** · `w_melee_18` · K2 · Tier 3 · 7,590 credits · *Attack +1 · +1d8
piercing · OnHit: Stun 22* — *"It's unclear whether this weapon was designed by the Gand
or to silence them."*

## Wookiee Warblade — base die `1d10`, threat 20 / ×2

### Base

**Wookiee Warblade** · `g_w_warblade001` · K1 · Tier 1 · 20 credits · *no properties* —
*"Though initially they might seem cumbersome, Wookiee Warblades are actually a very
efficient design. Kept in continual motion, they can cut a swath through almost
anything."*

### Advanced

**Freyyr's Warblade** ⚠ unique · `w_melee_30` · K2 · Tier 4 · 29,955 credits · *Attack +1
· +2 slashing · +2d10 slashing · Keen* — *"Carved upon this mighty warblade is a symbol
of the Wookiee chieftain Freyyr. How this weapon found its way off of the Wookiee
homeworld of Kashyyyk is unknown."* The most expensive melee weapon in either game.

## Double-Bladed Sword — base die `2d6`, threat 20 / ×2

Two attacks, Balanced, and a threat range one step worse than the single-bladed
equivalent — more swings, less precision.

### Base

**Double-Bladed Sword** · `g_w_dblswrd001` · K1 · Tier 1 · 100 credits · *no properties*
— *"A difficult weapon to master, the double bladed sword has a grip in the center with
two long blades emerging from either end. Capable of inflicting more damage — but also
less precise — than the single-bladed variant."* K2 carries it identically as
`w_melee_07`.

### Advanced

**Echani Ritual Brand** · `g_w_dblswrd002` · K1 · Tier 1 · 300 credits · *Enhancement 1* —
*"Echani Firedancers use the double bladed Ritual Brand in a dodging and slicing pattern
so graceful it looks more like a dance than combat."*

**Krath Double Sword** · `g_w_dblswrd003` · K1 · Tier 2 · 980 credits · *+1 cold ·
Enhancement 2* — *"Twisted by the Dark Side, the Krath favored weapons of fearsome
appearance requiring brute strength to wield."*

**Ajunta Pall's Blade** ⚠ unique · `g_w_dblswrd005` · K1 · Tier 2 · 2,480 credits · *+4
fire · Enhancement 3* — *"Held by the Dark Jedi even before he fell to the Dark Side,
this may be one of the few truly personal items owned by Ajunta Pall, and remains as
thoroughly corrupted as he."*

**Force Pike** · `w_melee_14` · K2 · Tier 2 · 3,000 credits · *OnHit: Stun 10* — *"This
weapon effectively functions as a long staff topped with a vibroblade. Despite its name,
it is not related to the Force mastered by Jedi."*

**Gand Shockstaff** · `w_melee_23` · K2 · Tier 3 · 16,000 credits · *OnHit: Stun 14* —
*"This weapon was developed by Gand findsmen to help them herd their prey. Its powerful
stunning capabilities are backed up by the weapon's sharp tip."*

## Vibro Double-Blade — base die `2d8`, threat 20 / ×2

The heaviest die in the melee catalogue.

### Base

**Vibro Double-Blade** · `g_w_vbrdblswd01` · K1 · Tier 1 · 200 credits · *no properties* —
*"Ultrasonic vibrations make this double-bladed sword exceptionally deadly. A rare
Echani cortosis weave protects it against lightsaber sparring damage."* K2 carries it
identically as `w_melee_15`.

### Advanced

**Sith War Sword** · `g_w_vbrdblswd02` · K1 · Tier 1 · 500 credits · *Enhancement 1* —
*"Though most favor lightsabers, some Sith prefer the more visceral feel of metal cutting
flesh."* K2's `w_melee_12` is the same item at Tier 2.

**Echani Double-Brand** · `g_w_vbrdblswd03` · K1 · Tier 2 · 1,500 credits · *+3 energy ·
Enhancement 2* — *"Excess energy from the generator in this vibrosword is conducted
directly through the blades. Also possessing a rare lightsaber-deflecting cortosis
weave, this weapon is a deadly Echani masterpiece."*

**Ludo Kressh's War Sword** ⚠ unique · `w_melee_x12` · K2 · Tier 2 · 2,400 credits ·
*Attack +1 · +2 dark side* — a Sith War Sword that *"once belonged"* to Ludo Kressh. The
only melee weapon in either game dealing damage typed to the dark side.

**Yusanis' Brand** · `g_w_vbrdblswd04` · K1 · Tier 3 · 8,000 credits · *Attack +1 · +3
fire · +5 and +1d4 vs droid · Enhancement 2 · Keen · OnHit: Stun 10* — *"Yusanis was the
most famous of Echani warriors, fighting against oppression and villainy until
encountering Darth Revan."* Three found-only forms follow (`vbrdblswd05` through `07`),
trading fire for ion and gating behind `Power Attack` and `Critical Strike`.

**Trandoshan Double-Blade** · `w_melee_20` · K2 · Tier 3 · 10,235 credits · *Attack +2 ·
+4 slashing · Massive Criticals 1d8* — the Chalon-ore treatment applied to the
double-bladed frame.

**Zhaboka** · `w_melee_28` · K2 · Tier 4 · 25,000 credits · *+1d8 slashing · Massive
Criticals 2d6* — *"This variant of the double-bladed sword originated on Iridonia, the
homeworld of the Zabrak. A ceremonial weapon, the Zhaboka began as a simple wooden stick
but has since been refined."*

---

## A caution on item codes

**The code beside each weapon is the games' own identifier**, and it is given so you can
find the item in the game files if you want to. **It is not a reliable guide to what kind
of weapon something is.**

Two examples from this chapter alone: **`Raito's Gaderffii`** carries a code in the
Quarterstaff range while using the Gaffi Stick's `1d8` die, and **`Baragwin Assault
Blade`** uses a prefix no other weapon in its family shares.

> **Read the family heading, not the code.**
