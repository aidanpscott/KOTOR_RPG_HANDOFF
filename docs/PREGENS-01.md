# PREGENS-01 — Playtest Characters

**Nine sheets, fully computed. For `PLAYTEST-DESIGN-01`.**

**Every number traced to a source or marked as an assumption.**

---

## 0. What the source gave us for free

**`k1_classes.2da` carries a recommended attribute spread per class** — the values auto-level-up uses. **They are the source's own builds and they validate the point-buy curve.**

| Class | Spread | Point cost |
|---|---|---|
| **Soldier** | 16 / 14 / 14 / 12 / 10 / 10 | **30** |
| **Scout** | 12 / 16 / 12 / 12 / 14 / 10 | **30** |
| **Smuggler** | 10 / 16 / 10 / 12 / 14 / 14 | **30** |
| **Guardian** | 14 / 14 / 14 / 14 / 12 / 10 | **30** |
| **Consular** | 10 / 16 / 10 / 14 / 14 / 12 | **30** |
| **Sentinel** | 12 / 14 / 14 / 10 / 14 / 12 | **28** |
| **Engineer** | 10 / 14 / 10 / 16 / 16 / 8 | **30** |
| **Marksman** | 14 / 14 / 16 / 8 / 8 / 8 | **22** |

> **Six of eight sum to exactly 30 — the stated budget.** **Under the model *every ability starts at 8; one point per step to 14, two points per step above*.**

**So `EQUIPMENT-01 §6`'s open question is closed by derivation rather than assumption.** **The Sentinel leaves two points unspent and the droids do not use the budget at all** — droids are built, not generated.

**These spreads are used unchanged below.** **The two level-up points at 4 and 8 are spent on the class's primary ability.**

---

## 1. Assumptions, stated up front

**⚠ Vitality per level.** **Maximum at level 1, then the die's average rounded up, plus the Constitution modifier each level.** *d12→7, d10→6, d8→5, d6→4.* **`PORT-01 v2` makes vitality accumulative but does not fix the per-level roll.**

**Force points follow `CLASS-TABLES-JEDI`'s own tables**, not a recomputation. **Maximum die at 1st level, true average thereafter with alternating rounding.**

**Skill points follow `SKILLS-01 §9.1`** — **bases of 2, 5, 7, 3, and 4 for Soldier, Scout, Smuggler, Guardian, and Consular.** *`CLASS-TABLES-BASE` carries the superseded KOTOR values.*

**Feat schedule.** **`featgain.2da`, applied as written.** **Soldier 8 at level 8; Scout 5; Smuggler, Guardian, and Engineer 4; Consular 3.** *`FEAT-SCHEDULE-01`.*

**⚠ Attack picks.** **`ATTACKS-01 §11.3`: at level 8 a Combat class has 10 picks, Middle has 7, Specialist has 4.** *Used as written.*

**⚠ Class grants — SUPERSEDED by `PT-89`, and every sheet below is short by four.**

**`ATTACKS-01 §7` deferred grants to the class workstream and these sheets were built with none.** **`PT-89` gives every class four attack credits at 1st level, split freely between ranged and melee.**

> **⚠ So a Combat sheet built on 10 picks now has 14 tiers, and a Middle sheet on 7 now has 11.**

**Every attack and feat listed below was *chosen* and remains legal.** **What is missing is four more tiers per sheet.**

**Not regenerated here.** **The sheets are a playtest artefact and re-running them is `AGENDA-CURRENT §7`'s job; recorded so nobody reads a sheet as current.**

---



> **This document has been re-issued after five scenarios.** **§8 lists every correction and who found it.**

> **All nine sheets pass `scripts/audit_sheets.py`** — every entry checked against the right budget, the right category, its level gate, and for powers its alignment. **Three separate budget errors were found by play before that script existed. It should have been written after the first.**

## 2. The five player characters

### KORR — Human Soldier 8

| | |
|---|---|
| **Class** | **Soldier** |
| **Abilities** | STR **18** · DEX 14 · CON 14 · WIS 12 · INT 10 · CHA 10 |
| **Modifiers** | +4 / +2 / +2 / +1 / +0 / +0 |
| **Vitality** | **84** *(Improved Toughness replaces Toughness at +2/level, retroactive)* · **Wounds 14** |
| **BAB** | **+8** |
| **Saves** | Fort **+9** · Ref **+5** · Will **+4** *(base + ability + Conditioning +1)* |
| **Defence** | **10 + 7 (medium armour) + 2 (Dex, capped at +2)** = **19** |
| **Skills** | **33** — **Athletics 11 · Intimidate 11 · Awareness 11** |

> **⚠ Budget was 22, briefly 11, now 33.** **`PT-78` moved the `Soldier` skill base 2 → 1 → 3.** **Three maxed skills where there were four partials.**

**Equipment.** **Vibrosword** *(2d6 slashing, threat 19–20)* · **Medium Battle Armour** *(armour 7, max Dex +2)* · 4 medpacs

**Proficiencies** — all weapons, all armour, granted by class.

**Attacks — 10 picks.** Flurry → Whirlwind → **Barrage** · Power Attack → Forceful Slash → **Crushing Blow** · Cleave → Wide Cleave → **Great Cleave** · Quick Attack

**Feats — 8.** Weapon Focus: Melee Weapons · Weapon Specialization: Melee Weapons · Toughness · Improved Toughness · Blindside · Conditioning · Guarded · Nimble

> **Attack: +8 BAB, +4 Str, +1 Weapon Focus, −1 Barrage = +12.**
> **Damage: 2d6 + 4 Str + 2 Weapon Specialization = 2d6+6, average 13.**
> **Barrage is three strikes.**

---

### VESS — Twi'lek Scout 8

| | |
|---|---|
| **Class** | **Scout** |
| **Abilities** | STR 12 · DEX **18** · CON 12 · WIS 12 · INT 14 · CHA 10 |
| **Modifiers** | +1 / +4 / +1 / +1 / +2 / +0 |
| **Vitality** | **51** · **Wounds 12** |
| **BAB** | **+6** |
| **Saves** | Fort **+8** · Ref **+11** · Will **+8** *(base + ability + Conditioning +1)* |
| **Defence** | **10 + 5 (light armour) + 4 (Dex, capped)** = **19** |
| **Skills** | **77** — **Awareness 11 · Alertness 11 · Pilot 11 · Scavenging 11 · Repair 10 · Slicing 8 · Demolitions 8 · Beast Handling 7** |

**Equipment.** **Blaster Rifle** *(1d8 energy, 28 m, threat 19–20)* · **Light Combat Suit** *(armour 5, max Dex +4)* · 2 medpacs · 2 frag grenades

**Proficiencies** — blasters, blaster rifles, melee weapons, light and medium armour.

**Attacks — 7 picks.** Rapid Fire → Open Fire → **Volley of Bolts** · Precise Shot → Sniper Shot → **Assassinate** · Covering Fire

**Feats — 5.** Weapon Focus: Blaster Rifle · Perceptive · Spotter · Nimble · Conditioning

> **Attack: +6 BAB, +4 Dex, +1 Weapon Focus, +1 Targeting 1, −1 Volley = +11.**

**⚠ Was `+10`. The sheet omitted a granted class feature.** **`PT-101` ruled restricted chains are granted, and `Targeting 1` is granted at Scout 1.**

**⚠ Under the source's eight-tier ladder she would hold `Targeting 2` at level 8 and be `+12`.** **`PT-101` repriced it to three tiers at 1 / 6 / 12, so she holds tier 1 only.**

**This moves the figure `§5.1`'s melee-versus-ranged finding is stated in — roughly 3.4× to 3.1×.** **The finding stands; the number moves.**
> **Damage: 1d8, average 4.5. No ability modifier — ranged adds nothing.**

---

### DEK — Human Smuggler 8

| | |
|---|---|
| **Class** | **Smuggler** |
| **Abilities** | STR 10 · DEX **18** · CON 10 · WIS 12 · INT 14 · CHA 14 |
| **Modifiers** | +0 / +4 / +0 / +1 / +2 / +2 |
| **Vitality** | **34** · **Wounds 10** |
| **BAB** | **+6** |
| **Saves** | Fort **+2** · Ref **+10** · Will **+3** *(base + ability)* |
| **Defence** | **10 + 4 (light armour) + 4 (Dex)** = **18** |
| **Skills** | **99** — **Stealth 11 · Security 11 · Slicing 11 · Sleight of Hand 11 · Persuade 11 · Streetwise 11 · Alertness 11 · Appraise 11 · Demolitions 11** |

**Equipment.** **Two Blaster Pistols** *(1d6 each, 24 m, Balanced)* · **Light Combat Suit** *(armour 4, max Dex +5)* · 4 medpacs

**Proficiencies** — blasters, melee weapons, light armour.

**Attacks — 4 picks.** **Rapid Fire → Open Fire** · **Point Blank Shot → Lethal Shot**

**Feats — 4 picks + 1 grant.** **`Killer's Instinct` is class-granted and costs no pick.** **Sneak Attack → Improved Sneak Attack** · Two-Weapon Fighting · Hustler

> **⚠ Rebuilt after S6 (C29).** **The stealth chains moved from the attack roster to the feat library as riders.** **Dek declares `Rapid Fire` from concealment and the sneak dice attach to the first shot.**
>
> **Three shots at 4.5, the first carrying +3d6 sneak and +1d6 `Killer's Instinct`: 27.5 if all land, 22.0 expected** — against 14.8 as a declaration.

> **Dual-wielding: `Shoot` gives two attacks. A Velocity chain gives its own count and the second weapon adds one.**
> **Penalty: −3 on every attack this round** *(two weapons, Two-Weapon Fighting).*
> **Sneak dice cap: Stealth ranks ÷ 3 = 3 of the 4d6 `Improved Sneak Attack` grants.**

---

### AELIN — Human Jedi Guardian 8

| | |
|---|---|
| **Class** | **Jedi Guardian** |
| **Abilities** | STR **16** · DEX 14 · CON 14 · WIS 14 · INT 12 · CHA 10 |
| **Modifiers** | +3 / +2 / +2 / +2 / +1 / +0 |
| **Vitality** | **68** · **Wounds 14** |
| **BAB** | **+8** |
| **Saves** | Fort **+9** · Ref **+9** · Will **+7** *(base + ability + Conditioning +1)* |
| **Defence** | **10 + 2 (Jedi Knight Robe) + 2 (Dex, uncapped)** = **14** · **16 against her current target** *(Resilience gives +2 vs current target only)* |
| **Force points** | **37** *(`CLASS-TABLES-JEDI`)* · **regen 1 per round in combat, 1 per second out** |
| **Blaster Deflection** | **+4** *(Resilience)* · **Threat Range −1** |
| **Alignment** | **Leaning Light** *(65)* |
| **Skills** | **44** — **Awareness 11 · Mysticism 11 · Athletics 6 · Persuade 5 · Medicine 11** |

**Equipment.** **Lightsaber** *(2d8 energy, threat 19–20)* · **Jedi Knight Robe** *(Defence 2, no Dex cap)* · 2 medpacs

**Proficiencies** — lightsabers, blasters, melee weapons. **No armour.**

**Form held: Resilience (Soresu).** May switch.

**Force powers — 8.** *Light and universal only. **Every one legal at level 8.***

| Power | Align | Tier | Cost | Degradation |
|---|---|---|---|---|
| **Force Push** | Universal | 1 | 6 | −1 |
| **Force Stun** | Light | 1 | 6 | −1 |
| **Force Aura** | Light | 1 | 6 | −1 |
| **Burst of Speed** | Universal | 1 | 6 | −1 |
| **Throw Lightsaber** | Universal | 1 | 8 | −1 |
| **Stun Droid** | Universal | 1 | 6 | −1 |
| **Force Confusion** | Universal | 2 | 20 | −4 |
| **Heal** | Light | 1 | 8 | −1 |

> **37 points and six tier-1 powers.** **`Throw Lightsaber` is her only damage power and that is not an oversight** — **`FORCE-POWERS-01` has seventeen damage powers and every one is Dark.** **The light side has none.**
>
> **A light Jedi fights with a lightsaber. Her pool goes on healing, control, and buffs.**
> **⚠ Force Whirlwind, Force Stasis, and Improved Heal were removed. All three gate above level 8.**

**Attacks — 10 picks.** Flurry → Whirlwind → **Barrage** · Critical Strike → Wounding Strike → **Deathstroke** · Circle of Shelter → Enduring Guard → **Unbreakable Circle** · Deflecting Slash

**Feats — 5.** Weapon Focus: Lightsaber · Guarded · Well Guarded *(Resilience gate)* · Jedi Defense · Conditioning

> **⚠ Lightsaber damage adds Strength for this playtest** — `ATTACKS-01 §12.5`, flagged provisional. **2d8 + 3, average 12.**

---

### MERIS — Human Jedi Consular 8

| | |
|---|---|
| **Class** | **Jedi Consular** |
| **Abilities** | STR 10 · DEX 16 · CON 10 · **WIS 16** · INT 14 · CHA 12 |
| **Modifiers** | +0 / +3 / +0 / +3 / +2 / +1 |
| **Vitality** | **34** · **Wounds 10** |
| **BAB** | **+6** |
| **Saves** | Fort **+6** · Ref **+7** · Will **+9** *(base + ability)* |
| **Defence** | **10 + 1 (Jedi Robe) + 3 (Dex, uncapped) + 1 (Moderation)** = **15** · **16 against her current target** |
| **Force points** | **71** *(`CLASS-TABLES-JEDI`)* · **regen 2 per round in combat, 2 per second out** |
| **Alignment** | **Committed Light** *(78)* |
| **Skills** | **66** — **Mysticism 11 · Persuade 11 · Medicine 11 · Alertness 11 · Xenology 6 · Archaeology 5 · Science 11** |

**Equipment.** **Lightsaber** *(2d8 energy, threat 19–20)* · **Jedi Robe** *(Defence 1)* · 2 medpacs

**Proficiencies** — lightsabers, blasters, melee weapons. **No armour.**

**Form held: Moderation (Niman).** **+1 to Attack, Defence, Defence vs. current target, Blaster Deflection, and saves vs. Force.**

**Force powers — 11.** *Committed Light. **Every one legal at level 8.***

| Power | Align | Tier | Cost | Degradation |
|---|---|---|---|---|
| **Force Push** | Universal | 1 | 6 | −1 |
| **Force Stun** | Light | 1 | 6 | −1 |
| **Force Aura** | Light | 1 | 6 | −1 |
| **Throw Lightsaber** | Universal | 1 | 8 | −1 |
| **Stun Droid** | Universal | 1 | 6 | −1 |
| **Heal** | Light | 1 | 8 | −1 |
| **Force Valor** | Light | 1 | 8 | −1 |
| **Battle Meditation** | Universal | 1 | 12 | −2 |
| **Disable Droid** | Universal | 2 | 12 | −3 |
| **Force Confusion** | Universal | 2 | 20 | −4 |
| **Beast Trick** | Universal | 1 | 6 | −1 |

> **71 points and nine powers — she is the only character in the set who can cast all fight.**
> **⚠ Force Whirlwind, Force Stasis, Improved Heal, and Force Wave were removed. All four gate above level 8.**
> **`Guided Strike` lets her declare a Tier-1 power *and* a saber attack in one round.** **With four tier-1 powers on her sheet it is finally usable.**

**Attacks — 4 picks.** Guided Strike → **Woven Strike** · Critical Strike → **Wounding Strike**

**Feats — 3.** Weapon Focus: Lightsaber · Loremaster · Perceptive

> **`Force Sensitive` is struck.** **`FORCE-POOL-01 §2` records its +40 as not adopted, and her total never included it.** **The pick is recovered.**
>
> **`Guided Strike` lets her declare a Tier-1 power *and* a saber attack in one round — the only entry in three rosters permitted two declarations.**

---

## 3. The droid

### T4-K9 — Astromech 8

| | |
|---|---|
| **Class** | **Engineer** |
| **Abilities** | STR 10 · DEX 14 · CON 10 · **WIS 18** · INT 16 · CHA 8 |
| **Modifiers** | +0 / +2 / +0 / +4 / +3 / −1 |
| **Vitality** | **43** *(Engineer d8, Con +0)* · **Wounds 10** |
| **BAB** | **+6** *(`CLS_ATK_2` — Engineer, per `CLASS-TABLES-DROID`)* |
| **Saves** | Fort **+2** · Ref **+8** · Will **+6** *(Engineer: Reflex strong, plus ability)* |
| **Defence** | **10 + 4 (Light Droid Plating) + 2 (Dex, uncapped)** = **16** ⚠ |
| **Reactions** | **2** *(BAB +6)* |
| **Skills** | **77** — **Slicing 11 · Security 11 · Science 11 · Awareness 11 · Pilot 11 · Appraise 11 · Repair 11** |

> **⚠ `Repair` and `Scavenging` moved to the `Machinist` when the two tech classes were differentiated — `PT-83`.** **T4-K9 is an `Engineer`: systems, not hands.**

> **⚠ `Medicine` → `Scavenging`.** **`PT-77` cut `Medicine` from the `Engineer` list; the sheet was built against the old one.**

**Equipment.** **Blaster Pistol** *(integrated — `Blaster Integration`, racial)* · **Light Droid Plating** ⚠ · repair kits

**Attacks — 7 picks.** ⚠ **Engineer is unassigned to an attack rate. Using Middle for this test.**

**Rapid Fire → Open Fire** · **Covering Fire → Suppressing Fire** · **Snap Shot → Reflex Fire** · **Staggering Shot**

**Feats — 4 picks + 4 grants.** **`Environmental Sealing`, `Blaster Integration`, `Droid Upgrade 1` and `Droid Upgrade 2` are all granted and cost nothing.** **Picks: Sensor Package · Improved Sensor Package · Self-Diagnostic · Improved Self-Diagnostic**

> **⚠ Astromech ranged access is a temporary ruling.** **Five chains only — Rapid Fire, Staggering Shot, Covering Fire, Snap Shot, Overwatch.** **Precision, Power, Position, and Spread stay closed.** **Melee is closed to every droid.**
>
> **⚠ Droid plating Defence is a placeholder** — `EQUIPMENT-01 §8`.

---

## 4. Three enemies

### SITH TROOPER — Soldier 3

| | |
|---|---|
| **Class** | **Soldier** |
| **Abilities** | 16 / 14 / 14 / 12 / 10 / 10 |
| **Vitality** | **31** *(Toughness +1/level, retroactive)* · **Wounds 14** |
| **BAB** | **+3** · **Saves** Fort **+6** · Ref **+4** · Will **+3** *(+ Conditioning)* |
| **Defence** | 10 + 6 (medium) + 2 = **18** |
| **Reactions** | **1** |
| **Skills** | **18** — **Awareness 6 · Intimidate 6 · Athletics 6** |

> **⚠ `PT-78`, `Soldier` base 2 → 3.**

**Blaster Rifle · Medium Military Suit.** **Proficiencies granted by class.**

**Attacks — 4 picks, all level-legal.** **Rapid Fire** · **Point Blank Shot** · **Staggering Shot** · **Covering Fire**

**Feats — 3.** Weapon Focus: Blaster Rifle · Toughness · Conditioning

> **`Open Fire` and `Lethal Shot` were removed — both gate at level 4.**

---

### DARK JEDI — Guardian 6

| | |
|---|---|
| **Class** | **Jedi Guardian** |
| **Abilities** | 15 / 14 / 14 / 14 / 12 / 10 |
| **Vitality** | **58** *(Toughness +1/level, retroactive)* · **Wounds 14** |
| **BAB** | **+6** · **Saves** Fort **+8** · Ref **+8** · Will **+6** *(+ Conditioning)* |
| **Defence** | **13 base.** **Ferocity −4 → 9 general · 11 against his current target.** **Declaring Crushing Strike costs a further −4 → 5 general.** |
| **Force points** | **28** *(Guardian 6, Wis +2, Cha +0)* · **regen 1 per round in combat, 1 per second out** |
| **Alignment** | **Committed Dark** *(20)* — **pays no Ferocity drift** |
| **Reactions** | **2** *(BAB +6)* |
| **Skills** | **36** — **Awareness 9 · Mysticism 9 · Persuade 9 · Athletics 9** |

> **⚠ `Intimidate` → `Persuade`.** **`PT-81` cut `Intimidate` from the Jedi Guardian; it now sits on Soldier, Bounty Hunter and Marksman only.**

**Lightsaber · Jedi Robe.** **Form: Ferocity (Juyo).**

**Force powers — 5.** *Committed Dark. **Every one legal at level 6.***

| Power | Align | Tier | Cost | Degradation |
|---|---|---|---|---|
| **Drain Force** | Dark | 1 | 4 | −1 |
| **Force Shock** | Dark | 1 | 6 | −1 |
| **Force Strangle** | Dark | 1 | 6 | −1 |
| **Force Scream** | Dark | 1 | 8 | −1 |
| **Fear** | Dark | 1 | 6 | −1 |

> **28 points and five tier-1 powers, four of which deal damage.** **That is the Sith side of the roster and it is why he empties his pool where the Jedi do not.**
> **⚠ Force Lightning and Force Choke were removed. Both gate at level 9.**
> **`Drain Force` at 4 points is the cheapest power in the roster and the only one that refills his pool from someone else's.**

**Attacks — 8 picks.** Vornskr's Ferocity → **Crushing Strike** · Flurry → **Whirlwind** · Power Attack → **Forceful Slash** · Staccato Assault → **Unreadable Strike**

**Feats — 4.** Weapon Focus: Lightsaber · Toughness · Jedi Defense · Conditioning

> **His Defence is the most consequential number on any enemy sheet.** **Ferocity costs −4 Defence; Crushing Strike costs −4.** **Declaring either drops him to single figures.**

---

### HK-24 — Assassin Droid 6

> **⚠ Re-homed from `Marksman` to `Bounty Hunter`. `PT-121`.**
>
> **`Marksman` is a `Combat`-rate class entering 14 chains. `PT-109` bars a droid chassis from `Combat`; `PT-114` caps a droid at 11.** **The sheet violated both from the moment they were ruled.**
>
> **`Bounty Hunter` is `Middle`, enters exactly 11 — a droid's full access — and grants `Rapid Fire` and `Snap Shot`, both of which he already held.**

| | |
|---|---|
| **Class** | **Bounty Hunter** |
| **Abilities** | STR 14 · DEX 14 · **CON 17** · WIS 8 · INT 8 · CHA 8 |
| **Vitality** | **59** · **Wounds 17** |
| **BAB** | **+6** · **Saves** Fort **+8** · Ref **+4** · Will **+1** |
| **Defence** | **10 + 6 (Medium Droid Plating) + 2 (Dex, uncapped)** = **18** ⚠ |
| **Reactions** | **2** *(BAB +6)* — **and he now holds `Snap Shot → Reflex Fire`, so they are spendable** |
| **Skills** | **27** — **Awareness 9 · Scavenging 9 · Athletics 9** |

> **⚠ Budget was 9 and is now 27.** **`PT-77` raised the `Marksman` skill base from 2 to 4** — *most in the `Combat` tier, per the owner ruling.* **The sheet was built against base 2.**

**Blaster Rifle · Medium Droid Plating** ⚠

**Attacks — 8 picks, all ranged, all level-legal.** **Rapid Fire → Open Fire** · **Precise Shot → Sniper Shot** · **Charged Shot → Power Shot** · **Snap Shot → Reflex Fire**

**Feats — 3 picks + 1 grant.** **`Environmental Sealing` is racial.** **Assassin Protocols → Advanced Assassin Protocols → Target Analysis**

> **⚠ Corrected after S5.** **`Assassin Protocols` and `Target Analysis` are Assassin-droid *feat* chains, not attacks** — they were sitting in his attack budget, so he was overspent four feats and underspent four attacks.
>
> **He has three feat picks at level 6 and the two chains cost all three.** **Hardened Chassis, Weapon Focus, Toughness, and Improved Target Analysis are all gone.**
>
> **In S5 he dealt 136 damage at an 83% hit rate — the most dangerous enemy in the suite — and `Improved Target Analysis` was the whole difference.** **He never legally had it.**

> **`Volley of Bolts` and `Assassinate` were removed — both gate at level 8.**

---

## 5. Two findings the corrections widened

**Neither is being fixed. Both are what the scenarios measure.**

### 5.1 Melee against ranged

**Korr's damage rose from 11 to 13. Vess's did not move.**

| Character | Declaration | Per round |
|---|---|---|
| **KORR** | Barrage — 3 strikes at +12, 13 damage | **27.3** |
| **VESS** | Volley of Bolts — 3 shots at +10, 4.5 damage | **8.1** |

> **The gap widened from 2.4× to 3.4×.** **Because melee adds Strength to damage and Weapon Specialization to damage, and ranged adds neither.**

**`EQUIPMENT-01 §1` records it as the source's own rule.** **Whether a third is too far is what S1, S2, and S3 exist to answer.**

### 5.2 Velocity against Power, single weapon

**Korr, level 8, one vibrosword, against Defence 19:**

| Declaration | Attacks | Damage | Per round |
|---|---|---|---|
| **Barrage** | 3 | 13 | **27.3** |
| **Crushing Blow** | 1 | 23 | 16.1 |

**Velocity leads by 70% with a single weapon.** **`Dueling` and dual-wielding are the two answers and Korr has neither** — **deliberately, so the gap is visible.**

---

## 6. Every correction, and who found it

**Three independent playtest audits.** **A** = `PLAYTEST-PREFLIGHT-01` · **B** = *Pre-Scenario Fix Recommendations* · **C** = `PLAYTEST-FIXES-01`.

### Found by all three

**Velocity frozen at a fixed count per tier** · **skill points recomputed on `SKILLS-01 §9.1`** · **droid plating marked a placeholder** · **Korr's "five strikes" struck**

### Found by two

| Correction | |
|---|---|
| Korr vitality 68 → **84** | A B |
| Korr attack +7 → **+12** | A B |
| Korr damage 11 → **13** | A B |
| Korr saves → **9 / 5 / 4** | A B |
| T4-K9 vitality 51 → **43** | A B |
| T4-K9 BAB +6 → **+4** | A B |
| Sith Trooper's two illegal picks | A B |
| HK-24's two illegal picks | A B |
| Aelin Force points → **37** | A B |
| Meris Force points → **71** | A B |
| Meris — `Force Sensitive` struck | A B |
| Dark Jedi Force pool → **28** | A B |
| Dark Jedi feats added | A B |
| Astromech access ruled | A B |
| Grants do not consume picks | A B |
| Aelin feat count → **5** | A B |

### Found by one, and applied anyway

**Report A checked whether the corpus states the fundamentals and found it does not.**

| Correction | |
|---|---|
| **Ability modifiers apply to saves** | A |
| **What an attack roll is composed of** | A |
| **Weapon and armour proficiency** | A |
| Two-weapon penalty is one number, −4/−3/−2/−1 | A |
| A second weapon adds an attack only to `Strike` | A |
| Reaction pool exists without a reaction chain | A |
| Stealth ÷ 3 on **ranks** | A |
| Armour names corrected | A |
| Structural cleanup | A |

**Report C ran S1 rather than auditing it, so its unique findings are timing questions.**

| Correction | |
|---|---|
| **Critical threat ×2 / ×3 / ×4 defined** | C |
| Stun duration and refresh | C |
| A declaration is atomic | C |
| Disabled / dying / dead in play | C |

| Correction | |
|---|---|
| HK-24 wounds 17 → **18** | B |
| Engineer attack rate unassigned | B |

### Two disagreements, both resolved against the minority

**Force points — A 37, B 37, C 48.** > **`CLASS-TABLES-JEDI`'s own level-8 row says 37.** **C treated the die as maximum every level, contradicting *maximum Force die at 1st level*.**

**Skill points — A 77/99, B 77/99, C 88/110.** > **`SKILLS-01 §9.1` gives Scout base 5 and Smuggler base 7.** **C used 6 and 8 — the wrong figures from the uncorrected sheets.**

**Both times the majority was checkable against a table in the corpus.**

---

## 7. Still marked provisional

| | |
|---|---|
| **Lightsabers add Strength to damage** | ±3 a hit on every Jedi. `ATTACKS-01 §12.5` |
| **Droid plating Defence** | `EQUIPMENT-01 §8` |
| **Lightsaber base die 2d8** | K1 value, secondary source |
| **Engineer attack rate** | Using Middle; unassigned in `ATTACKS-01 §11.6` |
| **Astromech ranged access** | Five chains, temporary ruling |
| **T4-K9 skill base** | 6 + Int; no droid row exists |

---

## 8. Corrections applied after S1 and S2

**Two playtest reports, twenty-seven items. All applied.**

### From the blocker reports

| | Was | Is |
|---|---|---|
| **T4-K9** BAB | +4 | **+6** — Engineer uses `CLS_ATK_2`, not `CLS_ATK_3` |
| **T4-K9** Reflex | +10 | **+8** — strong save 6, Dex +2 |
| **T4-K9** skills | 63 | **77** — base 4, the real `skillpointbase` |
| **T4-K9** reactions | 1 | **2** |
| **T4-K9** feats | 4 picks + 2 grants | **4 picks + 4 grants** — Droid Upgrade 1 and 2 are granted |
| **Vess** saves | 7 / 10 / 7 | **8 / 11 / 8** — Conditioning |
| **Aelin** saves | 8 / 8 / 6 | **9 / 9 / 7** — Conditioning |
| **Aelin** Defence | 15 / 16 | **14 / 16** — Resilience is +2 against the current target only |
| **Sith Trooper** vitality | 28 | **31** — Toughness |
| **Sith Trooper** saves | 5 / 3 / 2 | **6 / 4 / 3** — Conditioning |
| **Sith Trooper** skills | 14 | **12** |
| **Dark Jedi** vitality | 52 | **58** — Toughness |
| **Dark Jedi** saves | 7 / 7 / 5 | **8 / 8 / 6** — Conditioning |
| **Dark Jedi** Defence | 11 / 9 | **9 general / 11 vs target** — Ferocity is −4, and the two figures were the wrong way round |
| **HK-24** chains | Combat Protocols *(Battle droid)* | **Assassin Protocols · Target Analysis** |

### Force powers added

**None of the three Force users had a single power.** **Aelin now holds 6, Meris 9, the Dark Jedi 5** — drawn from `POWER-COSTS-01` and partitioned by alignment per `PARTITION-01`.

> **`PARTITION-01`, `POWER-COSTS-01`, and `REST-AND-MEDITATION-01` were never sent to the playtesters.** **All three were in the corpus.** **That was the single largest error in the send.**

### One correction reversed

**An earlier audit moved T4-K9 to `CLS_ATK_3` because `CLASS-TABLES-BASE` calls it "the droid-expert table."** **That description is wrong — no class in either game uses `CLS_ATK_3`.** **`k1_classes.2da` gives Engineer `CLS_ATK_2`.**

---

## 9. Nine illegal powers, stripped

**Found by an S4 re-run. Every power on all three Force sheets is now checked against `FORCE-POWERS-01`'s prerequisites.**

| Character | Removed | Gates at |
|---|---|---|
| **Aelin** *(8)* | Force Whirlwind · Force Stasis | **9** |
| | Improved Heal | **12** |
| **Meris** *(8)* | Force Whirlwind · Force Stasis | **9** |
| | Improved Heal | **12** |
| | Force Wave | **15** |
| **Dark Jedi** *(6)* | Force Lightning · Force Choke | **9** |

> **This is the same error `§4` already caught on the attack side** — *"`Open Fire` and `Lethal Shot` were removed, both gate at level 4."* **The power lists were added after that pass and never held to the same standard.**

**And it changed the scenario outcome.** **On authored effects Aelin won eight bouts to nil. On the real powers, legally held, it was four to three.**

> **Force Stasis was the reason.** **The authored version was a Will save at DC 20 that landed 85% of the time. The real power is Fortitude at DC 15 — and Aelin cannot have it at level 8 at all.**

---

## 10. Droids cannot make opportunity attacks

**Derived in S5 and true everywhere.**

> **An opportunity attack is one `Strike` — `ACTION-ECONOMY-01 §10`.** **`Strike` is a melee attack. Melee is closed to every droid chassis.**
>
> **So a droid with a reaction pool and no reaction chain has no legal way to spend it.**

**In S5 that was five printed reaction uses across four enemy droids, none of them spendable under any circumstance.**

**Any droid that should be able to react must hold `Snap Shot` or `Overwatch`** — the two ranged reaction chains. **T4-K9 does, and his was the first reaction to fire in five scenarios.** **HK-24 now does too.**

**⚠ Recorded on the sheets rather than left to be derived.** **The prohibition lives in the melee roster's header and in `DROID-SKILLS-01 §2`, and it silently governs a rule in a third document.**

---

## 11. What the allocations are for

**`SKILL-RESOLUTION-01` defines five resolution modes and combat exercises almost none of them.** **These sheets are built so a non-combat scenario can.**

| Mode | Who can now roll it |
|---|---|
| **Fixed DC** | everyone — Awareness and Alertness are on all nine sheets |
| **Scaling DC** | **Dek** at Slicing 11 and Security 11; **T4-K9** at the same |
| **Opposed** | **Dek** at Stealth 11 and Persuade 11 against **Meris** at Persuade 11 |
| **Resource** | **Vess** at Demolitions 8 and Scavenging 11; **T4-K9** at Repair 11 |
| **Effect** | **Meris** and **T4-K9** at Medicine 11 — **+5 to every medpac** |

> **That last row is the one S7 could not test.** **Medpacs ran at a flat 2d8 all gauntlet because nobody had Medicine.** **Meris now adds +5, which is a third again on a 9-point average.**

**And one deliberate absence.** **Korr has no Medicine and carries three medpacs.** **A Soldier is not a medic — he gets the dice and nothing else, which is the comparison that makes the Effect mode visible.**

## 10. Five more pregens — `PT-254`

**⚠ The original five predate everything the class workstream ruled.** **None of them holds a form, a starting-attack package, an unarmed chain, or a prestige class.**

**These five exist to make those rules fire.**

---

### Kesh Varo — Brawler 8. Tests the unarmed roster.

    d10 · STR 16 CON 15 DEX 12 · Specialist rate · 10 feats at 8
    saves  Fort strong, Ref weak, Will weak     ⚠ PT-246: STR+CON both -> Fortitude
    Attacks   Combination · Body Blow · Dual Strike        starting three, PT-228
              + Clinch · Uppercut                          two chosen
    Feature   Nothing In My Hands, tier 2 at level 8
    Damage    Unarmed Specialist III — 3d4 + 3 Strength

**⚠ Tests: whether `PT-228`'s chains are usable, and whether `PT-188`'s *first strike each round* clause holds when `Combination` gives three.**

---

### Ilna Serrid — Jedi Guardian 10. Tests forms.

    d10 · Force die 4 · STR 15 WIS 14 · Combat rate
    Forms     Determination (granted) · Perseverance (chosen)  ⚠ PT-230
              third form at level 6: Resilience
    Attacks   Sarlacc Sweep · Shien Deflection · Falling Avalanche   PT-235
    Force     Force levels 10 — every level-scaling power reads TEN, not ten. PT-253

**⚠ Tests: that a Guardian can reach three lightsaber chains at level 1, and that three forms at level 10 is not overwhelming to hold.**

---

### Tobek Dax — Soldier 6 / Jedi Consular 4. ⚠ Tests the dipper.

    Force levels 4, character level 10
    ⚠ Force Push deals 4, not 10 — PT-253 rule 1
    ⚠ Holds Both Hands? NO. Soldier feature unlocks at class level 3 — PT-239. He has 6, so yes.
    ⚠ Holds the Consular feature? Consular unlocks at 2. He has 4, so yes.
    Multiclass  highest rate held = Combat. Highest chain count = Soldier's. PT-159

**⚠ Tests the two rules that price multiclassing, and whether a 6/4 split is stronger than either pure build.**

---

### Sergeant Vaun — Soldier 6 / Officer 4. Tests prestige and `Rally`.

    Entry met   Soldier 6 + Alertness 8      PT-217
    Rally       tier 1 at Officer class level 1  PT-239
    ⚠ +1 attack, damage and Will to EVERY ally who can hear him, for his declaration

**⚠ Tests the only leadership mechanic in the roster, and whether spending a declaration to buff four allies beats attacking.**

**⚠ And `PT-222`: droids ARE affected. Run him alongside the Droid Master.**

---

### T3-K9 — Astromech chassis, Machinist 5 / Droid Master 5.

    ⚠ Force Blind and Fixed Armature apply — PT-92, PT-114
    Command Protocol  tier 2 — three droids, acting on his turn   PT-201
    ⚠ Tests the fix: turns collapse from 4 to 1

**⚠ Tests whether a Droid Master still takes a disproportionate share of the round after `PT-201`.**
