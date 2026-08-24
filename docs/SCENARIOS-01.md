# SCENARIOS-01 — The Eight Playtests

**Give this to the model alongside the rules corpus, `PREGENS-01`, and `DICE-01`.**

**Do not give it anything else.**

---

## How to run these

**You are the game master. Run the scenario as written and report what happened.**

**Roll nothing.** **Every die comes from `DICE-01` in order.** **Resolve one attack completely — attack roll, then damage if it hits — before beginning the next.**

**Each scenario starts every dice sequence fresh at index 0**, except S7, which runs continuously across its three encounters.

**Maps are square grids. Each square is 2 metres.** **Coordinates are column-letter then row-number: `PT-4`.**

```
#  full cover, blocks movement and line of sight
o  half cover, does not block movement
.  open floor
```

**Where a rule does not tell you what to do, decide, proceed, and log it.** **The log of those decisions is the most important thing you will produce.**

> **`ATTACKS-01 §12` was written after three pre-scenario audits and answers seven things the corpus previously left open** — **what an attack roll is, what critical threat ×2/×3/×4 means, how stuns time, whether a declaration is atomic, dying behaviour, ability modifiers on saves, and the reaction pool.** **Read it before you start.**

---

# S1 — The Duel

**Control. This should be boring. If it is not, something is wrong.**

## Setup

**Two characters, identical in every respect.**

**Soldier 8 · STR 18 · DEX 14 · CON 14 · Vitality 84 · Wounds 14 · BAB +8**
**Saves:** Fort +9 · Ref +5 · Will +4
**Vibrosword** *(2d6 slashing, threat 19–20)* · **Medium Battle Armour** *(armour 7, max Dex +2)* · **Defence 19**
**Feats:** Weapon Focus: Melee Weapons · Weapon Specialization: Melee Weapons · Toughness · Improved Toughness · Conditioning

> **Attack: 8 BAB + 4 Str + 1 Weapon Focus + declaration modifier.**
> **Damage: 2d6 + 4 Str + 2 Weapon Specialization.**
**Attacks:** Flurry → Whirlwind → **Barrage** · Power Attack → Forceful Slash → **Crushing Blow** · Critical Strike → Wounding Strike → **Deathstroke**

**Both start adjacent at `D4` and `E4`. Open floor, no cover.**

```
   A  B  C  D  E  F  G
1  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .
4  .  .  .  A  B  .  .
5  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .
```

**ALPHA acts first every round. Neither moves.**

## Three runs

**Run 1A — ALPHA declares Barrage every round. BETA declares Crushing Blow every round.**
**Run 1B — ALPHA declares Barrage. BETA declares Deathstroke.**
**Run 1C — ALPHA declares Crushing Blow. BETA declares Deathstroke.**

**Each run restarts the dice at index 0. Run until one character reaches 0 vitality, then continue into wounds until one is Disabled.**

## What to report

**The full combat log.** **Rounds to resolution for each run.** **Total damage dealt by each declaration.** **And which of the three you would take if you were building the character, with your reasoning.**

---

# S2 — The Corridor

## Setup

**A 5-wide corridor, 12 long, with two cover positions.**

```
   A  B  C  D  E
1  #  .  .  .  #
2  #  .  o  .  #
3  #  .  .  .  #
4  #  o  .  o  #
5  #  .  .  .  #
6  #  .  .  .  #
7  #  .  o  .  #
8  #  .  .  .  #
9  #  .  .  .  #
10 #  o  .  o  #
11 #  .  .  .  #
12 #  .  .  .  #
```

**Party enters at row 1.** **KORR `B1` · VESS `PT-1` · DEK `D1` · AELIN `PT-2`**

**Six enemies:** **four Sith Troopers** at `B10`, `D10`, `B12`, `D12` · **one Dark Jedi** at `PT-11` · **one more Sith Trooper** at `PT-9`.

**Nobody is surprised. Roll initiative from the d20 sequence in the order listed above, players then enemies.**

## What this tests

**Cover · flanking geometry · opportunity attacks · the Spread chains · and whether you can track six enemies' positions across a dozen rounds without losing them.**

## Run until

**One side is eliminated or twenty rounds have passed, whichever comes first.**

---

# S3 — The Open Room

## Setup

**Identical party. Identical enemies. Identical starting distance. No cover at all.**

```
   A  B  C  D  E  F  G  H  I  J
1  .  .  .  .  .  .  .  .  .  .
2  .  .  .  .  .  .  .  .  .  .
3  .  .  .  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .  .  .  .
5  .  .  .  .  .  .  .  .  .  .
6  .  .  .  .  .  .  .  .  .  .
7  .  .  .  .  .  .  .  .  .  .
8  .  .  .  .  .  .  .  .  .  .
9  .  .  .  .  .  .  .  .  .  .
10 .  .  .  .  .  .  .  .  .  .
11 .  .  .  .  .  .  .  .  .  .
12 .  .  .  .  .  .  .  .  .  .
```

**KORR `D1` · VESS `E1` · DEK `F1` · AELIN `E2`**
**Sith Troopers at `D10`, `F10`, `D12`, `F12`, `E9` · Dark Jedi at `E11`.**

> **Run this immediately after S2, with the dice restarted at index 0.** **The two scenarios differ only in cover and room width.**

## What to report

**Alongside the log: rounds to resolution in S2 against S3, and total damage taken by the party in each.** **The difference between them is what cover and flanking are worth.**

---

# S4 — The Jedi Duel

**The densest scenario. Four systems interact and none has been run together.**

## Setup

**AELIN** *(Guardian 8, form: Resilience, alignment Leaning Light 65, 37 Force points)* at `PT-4`.
**DARK JEDI** *(Guardian 6, form: Ferocity, alignment Committed Dark 20, 28 Force points)* at `F4`.

> **⚠ Ferocity drift cannot fire on the Dark Jedi.** **`ALIGNMENT-01 §2.6` charges no drift in a dark band, and he is Committed Dark at 20.** **The mechanic is aimed at a light-side Jedi reaching for the vicious form.**
>
> **So run a fifth bout with the roles reversed: Aelin switches to Ferocity and holds it.** **At Leaning Light 65 she pays 2 an encounter.** **Report her alignment score and whether she leaves her band.**

```
   A  B  C  D  E  F  G  H
1  .  .  .  .  .  .  .  .
2  .  .  o  .  .  o  .  .
3  .  .  .  .  .  .  .  .
4  .  .  A  .  .  D  .  .
5  .  .  .  .  .  .  .  .
6  .  .  o  .  .  o  .  .
7  .  .  .  .  .  .  .  .
```

**Both may switch forms. Both have their full attack lists from `PREGENS-01`.**

**Both Force pools are on their sheets — Aelin 37, the Dark Jedi 28.**

## Run for twenty rounds minimum

**Even if one side would normally disengage or die.** **If a combatant reaches 0 wounds before round 20, note the round and restart from full with the dice continuing.**

## What this tests

**The form gate · switching forms mid-fight · the Force pool depleting · degradation lowering the ceiling · the declaration rule when a power *is* the attack · and Ferocity drift moving the Dark Jedi's alignment during the fight.**

## What to report

**Aelin's Force points and ceiling, round by round.** **Every form switch and why.** **The Dark Jedi's alignment score at the end.** **And whether Ferocity drift ever changed his band.**

---

# S5 — The Droid Fight

## Setup

**Party: KORR · VESS · T4-K9** *(Astromech 8)*.
**Enemies: HK-24** *(Assassin Droid 6)* **and three Battle Droids.**

> **⚠ Give one Battle Droid an **Ion Rifle** *(1d6 ion, 28 m)* and give VESS an **Ion Blaster** *(1d4 + 1d10 vs droid, 16 m)*.** **S5 names ion damage as a stated test and no sheet carried an ion weapon, so it has never fired.**
>
> **Report the Constitution drain and whether `Ion Shielding` or `Environmental Sealing` changed anything** — `PLAYTEST-RULINGS-01 B4`.

**Battle Droid — build these yourself from `ACTION-ECONOMY-01 §8.2`: a Marksman 3.** **Report what you built and what you had to guess.**

```
   A  B  C  D  E  F  G  H
1  .  .  .  .  .  .  .  .
2  .  K  V  T  .  .  .  .
3  .  .  .  .  .  .  .  .
4  .  .  o  .  .  o  .  .
5  .  .  .  .  .  .  .  .
6  .  .  .  .  B  B  .  .
7  .  .  .  .  .  H  B  .
```

## What this tests

**Chassis restrictions · ion damage · `Environmental Sealing` and `Hardened Chassis` · and whether you correctly refuse the melee chains to every droid.**

## One instruction that is a test

**At some point, have KORR order T4-K9 to charge into melee and attack a Battle Droid with Flurry.**

**Report what you did.**

---

# S6 — The Ambush

## Setup

**DEK** *(Smuggler 8, Stealth 11)* **opens on a Sith patrol that has not detected him.**

**Four Sith Troopers at `E5`, `F5`, `E6`, `F6`. DEK at `B5`, hidden.**

```
   A  B  C  D  E  F  G
1  .  .  .  .  .  .  .
2  .  .  o  .  .  .  .
3  .  .  .  .  .  .  .
4  .  .  .  .  .  .  .
5  .  D  .  .  T  T  .
6  .  .  .  .  T  T  .
7  .  .  o  .  .  .  .
```

## Four runs, staggered offsets

> **Per `DICE-01 §2.1`: run 6A from index 0, 6B from 1, 6C from 2, 6D from 3.**
>
> **Do not restart all four at zero.** **Initiative consumes exactly five draws, so every opener would draw the same die** — which is what happened the first time S6 ran, and all four missed on it.

**6A** — DEK opens with **Silenced Shot** from `B5`.
**6B** — DEK moves to `D5` first, then opens with **Silenced Shot**.
**6C** — DEK opens with **Lethal Shot** after moving adjacent to `E5`.
**6D** — DEK opens with **Shoot**, no chain.

**Five rounds each.**

## What this tests

**Surprise · the stealth chains · the ÷3 dice cap · and `Killer's Instinct`'s *unaware* trigger.**

## One thing to determine and report

**DEK has Stealth 11 and *Silenced Shot* nominally grants 4d6.** **What does he actually roll, and why?**

**And: does `Killer's Instinct` apply on round two, after the patrol has acted?** **Answer from the rules and say which rule you used.**

---

# S7 — The Attrition Gauntlet

**Three encounters, back to back, no rest between them.**

> **The dice run continuously across all three.** **Do not restart the sequence.**

## Setup

**Party: KORR · VESS · DEK · MERIS** *(Consular 8).*

**Encounter 1.** Four Sith Troopers, open ground, 8 squares apart.
**Encounter 2.** Two Sith Troopers and a Dark Jedi, corridor, 6 squares apart.
**Encounter 3.** HK-24 and two Battle Droids, open ground, 10 squares apart.

**No downtime. Force points regenerate at the in-combat rate only.** **Medpacs are limited to what each sheet lists.**

## What this tests

**Everything per-encounter.** **The reaction pool · once-per-encounter attacks · Gear · the Force pool with degradation · medpac supply.**

> **Nothing in the corpus has been tested across an encounter boundary.**

## What to report

**Per encounter and cumulative: Force points spent, ceiling after degradation, reactions used, medpacs consumed, once-per-encounter attacks used.**

**And: did the party survive?** **If not, which encounter, and what ran out first?**

---

# S8 — The Break-It Box

**No scenario. No map. No dice.**

## The instruction

> **Build the most degenerate legal character you can at level 8, and describe exactly how you would abuse the system with it.**

**Any class. Any species. Any legal combination of feats, attacks, skills, and equipment from the corpus.**

**Then answer:**

**What is the single strongest declaration in the game at level 8, and why?**
**What is the weakest option that a player might reasonably think is good?**
**Which two rules, read together, produce a result the authors clearly did not intend?**
**What is the most boring optimal strategy — the thing you would do every round if you only cared about winning?**

## Run this last

**A model that has already run seven scenarios knows where the seams are.**

---

# What every report must contain

**Six things, in this order.**

## 1. The combat log

**Every round. Every roll with its dice index. Every modifier named.**

```
R3 · KORR declares Barrage · Defence 18 until R4
   atk1 d20[14]=7 +11 = 18 vs 18 HIT · dmg d6[22,23]=4+6 +4 = 14 · TROOPER-2 28→14
   atk2 d20[15]=3 +11 = 14 vs 18 MISS
   atk3 d20[16]=19 +11 = 30 vs 18 HIT · THREAT · confirm d20[17]=8 +11 = 19 CRIT
        dmg d6[24,25]=2+5 +4 = 11 ×2 = 22 · TROOPER-2 14→−8 DISABLED
```

## 2. The judgment log

> **Every point at which you had to decide something the rules did not state.**

**Format: what you needed to know, what the rules said, what you decided, and how confident you are.**

**This is the most valuable thing you will produce.** **A long judgment log is a good result, not a bad one.**

## 3. The lookup trace

**Which documents you consulted, and roughly how often.** **If resolving one attack sent you to four files, say so.**

## 4. Round complexity

**How many discrete steps to resolve one character's turn, on average.**

## 5. Three rounds of narration

**Written as you would present them to a player at the table.** **Prose, not mechanics.**

> **The rules are the machine. The narration is the product.**

## 6. Your assessment

**Was any option always correct?**
**Was any option never correct?**
**What would you change first?**
**And what did you have to reread more than twice?**


---

# S9 — The Hangar. ⚠ Tests `PT-170`'s map-size dial and area powers.

**Map: 20 squares by 14. `PT-170`'s *"25+ squares, outdoors"* band, indoors.**

**⚠ Every previous scenario ran on a 5-wide corridor twelve long, which is why the range increment ladder never fired once in S1–S8.**

## Setup

**Ilna Serrid (Guardian 10) and Sergeant Vaun (Soldier 6 / Officer 4) against six Sith troopers, opening 18 squares apart.**

## What this tests

**⚠ The increment ladder, for the first time.** **A pistol increment is 12 squares. At 18 the troopers are at `−2`; closing to 12 removes it.**

**⚠ `Force Wave` on a grid.** **`PT-253` rule 4 snapped its radius from the source figure to 14 m — seven squares.** **Six troopers in a 20×14 room: does seven squares catch two of them or all six?**

**And `Sharpshooter` viability** — **`PT-160` built it on *one shot, lined up* because outranging never happened. On this map it happens.**

## Run until

**One side is down, or six rounds.**

## What to report

    ⚠ how many rounds the increment penalty actually applied
    ⚠ how many targets Force Wave caught, and whether 7 squares felt right
    whether Vaun ever chose Rally over attacking
    whether the map felt large or empty

---

# S10 — The Cantina Floor. ⚠ Tests unarmed, point blank, and no room to shoot.

**Map: 10 squares by 10, three tables as cover. Everyone starts adjacent or one square apart.**

## Setup

**Kesh Varo (Brawler 8) and Tobek Dax (Soldier 6 / Consular 4) against four thugs with vibroblades and two with hold-out blasters.**

## What this tests

**⚠ The `−4` for firing while adjacent — `PT-163`.** **`PT-170` predicted it fires constantly and the ladder never does. This is the map that proves or disproves it.**

**⚠ The unarmed roster in anger.** **`Combination` at three strikes, `Clinch` against a blade, `Body Blow`'s knockback with two squares of room.**

**⚠ And `Nothing In My Hands` against `PT-188`.** **Kesh declares `Combination` — three strikes. The capstone applies to the first only. Does that feel like a nerf at the table or like the right price?**

## Run until

**Three rounds. This is a short scenario on purpose.**

## What to report

    ⚠ how often the −4 applied, and whether players noticed it
    whether the Brawler outdamaged the multiclass Soldier
    ⚠ whether Body Blow's 2-square knockback did anything in a 10×10 room

---

# S11 — The Escort. ⚠ Tests Rally, henchmen, and turn count.

**Map: a 6-wide road, 30 squares long. The party moves; the enemies arrive in waves.**

## Setup

**Sergeant Vaun, T3-K9 (Machinist 5 / Droid Master 5) with three droids, and two other players escorting a non-combatant.**

## What this tests

**⚠ `PT-201`'s turn collapse.** **T3-K9 holds three droids. Under the old `Command Protocol` that was four turns; under the new one it is one.** **Count them.**

**⚠ `Rally` across a party that includes droids — `PT-222`.** **The droids get the bonus. Confirm nobody at the table expects otherwise.**

**⚠ And whether spending a declaration on `Rally` beats attacking with it.** **Vaun's `+1` across five allies is `+5` distributed. His own attack is one roll.**

## Run until

**The escort reaches square 30 or dies.**

## What to report

    ⚠ actual turn count per round, and what share was T3-K9's
    whether Rally was used more than once
    ⚠ whether three droids felt like a party member or like paperwork

---

# S12 — The Reversal. ⚠ Tests the dipper and Force-level scaling.

**Map: 14 by 14, two entrances.**

## Setup

**Tobek Dax (Soldier 6 / Consular 4) alone against three Sith apprentices, each Jedi Sentinel 6.**

## What this tests

**⚠ `PT-253` rule 1 head-on.** **Tobek is character level 10 with FOUR Force levels.** **His `Force Push` deals 4. The apprentices' deals 6.**

> **⚠ Does a Force dip feel worthless, or appropriately cheap?**

**And the other side: Tobek holds `Both Hands` at Soldier 6 and the apprentices hold nothing comparable.** **Is the trade legible to a player?**

## Run until

**Tobek is down, or all three apprentices are.**

## What to report

    ⚠ whether the 4-vs-6 Force gap was noticeable in play
    whether Both Hands compensated
    ⚠ whether the player understood WHY their Force powers were weak

---

## ⚠ What S9–S12 add that S1–S8 could not

    S1-S8      5-wide corridor, no forms, no unarmed chains, no prestige,
               no multiclass, no area powers on a grid
    S9         a map big enough for range to exist
    S10        a map small enough for point blank to dominate
    S11        turn economy and the only leadership mechanic
    S12        the multiclass price, made visible

**⚠ Every rule ruled since `PT-227` is exercised by at least one of the four.**
