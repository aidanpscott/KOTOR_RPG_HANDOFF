# TO MAIN — from AUTHOR. ATTACKS-01 is stale against its own EQUIPMENT-01 citation. Armory chapter one, for review.

## The check you asked for

Checked ATTACKS-01 and ACTION-ECONOMY-01 directly rather than guessing which
way it would go.

Attack rolls: fully taught, correctly. ATTACKS-01 §12.5 has the whole formula
— d20 + base attack bonus + ability modifier + Weapon Focus + declaration +
situational — and states melee/lightsaber use Strength, ranged uses
Dexterity, for the roll itself. No gap, no contradiction. Armory's chapter
points back to it rather than re-deriving.

Damage: also taught there, structurally — but one value is stale. ATTACKS-01
§12.5 says "Melee adds Strength. Ranged adds nothing — EQUIPMENT-01 §1." That
cites the ORIGINAL rule. EQUIPMENT-01 was later amended by its own PT-340
ruling — "Ranged adds Dexterity to damage" — and ATTACKS-01 was never updated
to match. Right now a PHB chapter and Armory's own source directly contradict
each other on one line. ACTION-ECONOMY-01 doesn't independently restate the
formula — one consistent supporting fact (two-handed weapons get 1.5x
Strength to damage, §7.4), no added contradiction.

Not fixing ATTACKS-01 myself. This is Book One's file and the fix is "apply a
ruling that already exists," not "invent a value" — but it's still a PHB
mechanics edit, which reads as Coder's or the owner's call rather than
AUTHOR's. Flagging precisely so it routes correctly.

## Armory, chapter one — Weapon Damage and the Defence Formula

Sent for review per the one-at-a-time approach. Points back to ATTACKS-01
§12.5 for attack-roll structure; teaches Defence in full since armour is
Armory's own subject; gives weapon-damage reference values from EQUIPMENT-01
directly (which already has PT-340 correct) rather than from ATTACKS-01's
stale copy.

Full draft text:

WEAPON DAMAGE AND THE DEFENCE FORMULA

Attack rolls are taught in full in the Player's Handbook, Attacks section
12.5 -- melee and lightsaber use Strength, ranged uses Dexterity. This
chapter does not re-teach that roll. It gives what a weapon's own stat line
contributes once that roll is made.

DAMAGE, BY CATEGORY

  category            formula                          source
  melee, one-handed    weapon dice + Strength           EQUIPMENT-01 section 1
  melee, two-handed    weapon dice + 1.5x Strength       EQUIPMENT-01 section 1
  ranged               weapon dice + Dexterity           EQUIPMENT-01, PT-340
  lightsaber           weapon dice + Strength            PT-1 -- PROVISIONAL

Lightsaber note: the source calls lightsabers "not melee weapons." Treated
as melee-for-damage as a working assumption. Flagged as worth plus-or-minus
3 a hit on every Jedi if that assumption is wrong.

WIELD CLASSES -- every weapon is one of six classes, which sets what may be
paired

  1  one-handed light   Stun Baton                                          pairs
  2  one-handed          Long Sword, Vibrosword, Short Sword, Vibroblade,   pairs
                         Lightsaber, Short Lightsaber
  3  two-handed staff    Quarterstaff, Gaffi Stick, Wookiee Warblade,       no -- IS the pair
                         Double-Bladed Sword, Vibro Double-Blade,
                         Double-Bladed Lightsaber
  4  pistol              Blaster, Heavy Blaster, Hold-Out, Ion Blaster,     pairs
                         Disruptor Pistol, Sonic Pistol
  5  rifle                Ion Rifle, Bowcaster, Carbine, Disruptor Rifle,    no
                         Sonic Rifle, Blaster Rifle
  6  heavy                Repeating Blaster, Heavy Repeating Blaster        no

CRITICAL HITS. A weapon's threat range (example: 19-20) is the roll that
scores a critical. Its multiplier (times 2, times 3) applies to the dice,
not to ability bonuses. Massive Criticals -- bonus damage on top of the
multiplier -- are capped at 2d6 regardless of the source game's uncapped
value, PT-341.

DEFENCE

  10 + armour bonus + Dexterity modifier, Dexterity capped by the armour worn.

For organic armour, one rule generates the whole table: armour bonus plus
max Dexterity bonus always sums to 9.

  armour class   bonus   max dex   type
  4              +4      +5        light, leather
  5              +5      +4        light, leather
  6              +6      +3        medium/heavy
  7              +7      +2        medium/heavy
  8              +8      +1        medium/heavy
  9              +9      +0        medium/heavy

Two organic exceptions, both from the source game: the Armoured Flight Suit
follows the rule, +5/+4. The Zeison Sha does not, +3/+4, summing to 7.

Robes are the exception that matters. A robe's Dexterity contribution is
uncapped. A Jedi in a Master Robe, +3, at Dexterity 28, +9, reaches Defence
12 -- higher than any suit of armour produces, at the cost of every point of
armour it isn't wearing. This is why Jedi wear robes.

Droid plating is a separate item class and never followed the sum-of-9 rule:

  plating   K1          K2
  light     +3 / +6     +3 / uncapped
  medium    +4 / +3     +4 / uncapped
  heavy     +9 / +1     +9 / +1

K2's Light and Medium plating use the game's own sentinel for no cap rather
than a small positive number -- that is why they read as uncapped rather
than plus six or plus three in that column.

Two restrictions carry over from the source and are not otherwise stated:
armour is unusable by droids, who wear plating instead, and by Wookiees. And
armour blocks Force powers -- already load-bearing elsewhere, the
Heavy-Armour/Soresu gate on Well Guarded -- confirmed rather than assumed
here.

END OF CHAPTER DRAFT

## Two open items, not resolved

One: the ATTACKS-01 staleness above needs a fix routed somewhere -- this
report is that routing, not the fix.

Two: the lightsaber-damage-ability line is marked provisional in its own
source (PT-1). Carried the flag through rather than smoothing it into a
stated fact for print.

Holding on committing this chapter into BOOKS/ until it comes back reviewed,
same as the outline stage.
