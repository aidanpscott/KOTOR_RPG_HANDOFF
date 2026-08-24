# PLAYTEST-RULINGS-01 — Every Blocker Answered

**Raised across two reports after S1 and S2. Four Tier-1 blockers, fourteen Tier-2 items, thirteen carried forward.**

**Two of the four Tier-1 blockers were my error, not corpus gaps.**

---

# Tier 1

## B1 — Force powers exist. I failed to send them.

> **`PARTITION-01`, `POWER-COSTS-01`, and `REST-AND-MEDITATION-01` are all in the corpus and all three were omitted from the send list.**

**`POWER-COSTS-01` carries the full roster with tier, cost, and per-cast degradation.** **213 table rows.** Sample:

| Power | Tier | Cost | Degradation |
|---|---|---|---|
| **Force Push** | 1 | 6 | −1 |
| › Force Whirlwind | 2 | 14 | −3 |
| ›› Force Wave | 3 | 22 | −7 |
| **Force Stun** | 1 | 6 | −1 |
| › Force Stasis | 2 | 14 | −3 |
| ›› Stasis Field | 3 | 24 | −8 |
| **Stun Droid** | 1 | 6 | −1 |
| › Disable Droid | 2 | 12 | −3 |
| ›› Destroy Droid | 3 | 18 | −6 |
| › **Force Lightning** | 2 | 14 | −3 |
| ›› Force Storm | 3 | 24 | −8 |

**Send all three files. S4 and S7 are unblocked.**

**Which powers are Bonus actions:** **none, for this playtest.** **`ACTION-ECONOMY-01 §6.1` makes Action the default and requires a power's own entry to mark it otherwise. No entry does. Every power costs the Action.**

**Aelin and Meris need power lists on their sheets** — **see §5.**

## B2 — Droid class tables exist. Also my omission.

> **`k1_classes.2da` carries both, and `CLASS-TABLES-DROID` now writes them up.**

| Class | Hit die | BAB | Skill base | Saves |
|---|---|---|---|---|
| **Marksman** | **d12** | full — `CLS_ATK_1` | 2 | **Fortitude** |
| **Engineer** | **d8** | ¾ — `CLS_ATK_2` | 4 | **Reflex** |

**Chassis and class are different axes and both apply.** **HK-24 is an Assassin-chassis Marksman. T4-K9 is an Astromech-chassis Engineer.**

**⚠ This corrects a correction.** **An earlier audit moved T4-K9 to `CLS_ATK_3` on the strength of `CLASS-TABLES-BASE` calling it "the droid-expert table." That description was wrong — no class in either game uses `CLS_ATK_3`.** **T4-K9's BAB is +6, and his reactions go back to 2.**

## B3 — Medpacs

**`SKILL-RESOLUTION-01 §5.3` puts Medicine in Effect mode and gives no numbers. Ruling:**

| Item | Restores |
|---|---|
| **Medpac** | **2d8 vitality** |
| **Advanced Medpac** | **4d8** |
| **Life Support Pack** | **6d8**, and **stabilises a dying character** |
| **Antidote Kit** | **Ends one poison or ion effect. No vitality.** |

**Medicine's Effect mode: `+1 vitality per 2 full points of Medicine skill total`, applied to any medical item you use.**

> **A character with Medicine 12 adds +6 to a medpac.** **Someone with no training still gets the dice.**

**Using a medical item is a Gear action, one per round.** **`ACTION-ECONOMY-01 §3`.**

## B4 — Ion damage

**Ruling:**

**Ion weapons deal their listed damage to droids and half to organics.** *The Ion Blaster's `1d4 + 1d10 vs droid` already encodes this.*

> **An ion hit on a droid also drains 1 point of Constitution.** **A critical drains 2.**

**Constitution recovers at 1 point per day of rest** — `FORCE-POOL-01 §4.3`'s citation of RCR.

**Because wound points equal the Constitution score, ion drain shrinks the wound track directly.** **`Ion Shielding`'s damage reduction applies before the drain; a hit reduced to 0 damage drains nothing.** **`Master Hardened Chassis` grants immunity to the drain and not to the damage.**

---

# Tier 2 — every item, ruled

**Where the playtest's provisional matches, it is confirmed and the reason is given.**

## PT-1 — Is Jedi Defense free? **It costs a reaction.**

**Reversing the playtest's provisional.**

> **`FEATS-LIBRARY-01`'s "at any time" is flavour text predating the reaction pool.** **`ACTION-ECONOMY-01 §4`'s reaction table is the specific, later rule and it governs.**

**Free-and-unlimited makes a lightsaber user immune to the setting's primary weapon.** **Nine deflections in seven rounds is the symptom.**

**And the pool is not as thin as the report feared.** **`§10`'s allowance takes the better of Dexterity modifier and base attack bonus.** **Aelin at BAB +8 has 2 per encounter; at BAB +11 she has 3.** **`Deflecting Slash` and the Resilience form buy the *quality* of each deflection, not the count.**

## PT-2 — What Blaster Bolt Deflection is. **An opposed-roll modifier. Confirmed.**

> **Defender rolls `d20 + BBD`. Beat the attacker's attack total and the bolt is deflected. Beat it by 6 or more and it returns to the shooter.**

**BBD is the sum of every source: form, `Deflecting Slash`, `Jedi Defense` tier, `Deflect`, minus the attacker's `Marksman`.**

**Nothing else contributes.** **Not base attack bonus, not Weapon Focus, not the Jedi's own declaration penalty.** *The roll is not an attack.*

**A returned bolt hits automatically and carries the original weapon's damage.** **It does not carry the shooter's declaration bonuses and it is never a critical.**

**Each deflection is one reaction against one bolt.** **A Rapid Fire volley of three requires three reactions to stop entirely.**

**Facing is not modelled. Strike the 180° arc gate from `FEATS-LIBRARY-01`.**

## PT-3 — Cover is positional. **Confirmed.**

> **Standing in an `o` square grants +2 Defence and +1 Reflex regardless of firing angle.** **`ACTION-ECONOMY-01 §6.2` says "a property of position, gained by moving" and that governs.**

**Interpositional cover requires line-tracing every shot and the corpus has no line-of-sight rule to trace with.**

**⚠ `EQUIPMENT-01`'s three-quarters and total cover remain positional too** — **a `#` square is total cover and cannot be shot through or into.**

## PT-4 — Flanking geometry. **Confirmed, with diagonals.**

> **Two allies flank when their offset vectors from the target negate exactly.** **Opposite sides *or* opposite corners.**

**Ranged flanking uses the same test.** **A shooter within half weapon range whose position negates a melee ally's is flanking.** **In a corridor that will rarely fire, and that is correct** — **`Spotter` exists precisely because the geometric version is hard to reach.**

**`Spotter` overrides position only.** **The Spotter gains the bonus; the designated ally does not.** **`Blindside` modifies whatever bonus the holder receives, including one granted by someone else's `Spotter`.**

**"Your target" lasts until the start of your next turn.**

## PT-5 — Criticals multiply the whole total. **Confirmed.**

> **`ATTACKS-01 §12.1` says damage doubles. It means the damage.**

**`EQUIPMENT-01 §4b`'s line about lightsabers is a statement about *upgrade* bonuses — crystals and cells — not about Strength or Weapon Specialization.** **Rewritten to say so.**

## PT-6 — There is a confirmation roll. **Confirmed.**

**A threat is confirmed by a second attack roll against the same Defence.** **`SCENARIOS-01`'s log template shows one and that is the intended behaviour.**

## PT-7 — Riders persist up a chain. **Confirmed, and the fix is being applied.**

> **`ATTACKS-01 §3.1`'s own test — "a player would never want the tier below it" — fails if riders vanish.**

**The report's suggested fix is right and cheap: print the rider in all three rows of every chain.** **Applied to Critical Strike's stun, Power Attack's knockback and multiplier, Precise Shot's stun, and Sniper Shot's.**

## PT-8 — Which save resists each rider

| Rider | Save |
|---|---|
| **Critical Strike · Precise Shot** — stun | **Fortitude** |
| **Power Attack · Charged Shot** — knockback | **Reflex** |
| **Sweep Attack · Staggering Shot** — prone, movement | **Reflex** |
| **Disarming Shot** | **Reflex** |
| **Taunting effects, fear, domination** | **Will** |

**Reversing the provisional on knockback.** **A stun overwhelms the body; being shoved is dodged.**

## PT-9 — `§7.5` governs. **Confirmed.**

**A second weapon adds an attack only to `Strike` and `Shoot`.** **`§7.1`'s table is being corrected to match.**

## PT-10 — Ferocity's +1 attack. **The form grants it. Confirmed.**

> **`FORMS-01` is specific and settled under `D-AM`. `ACTION-ECONOMY-01 §7.1` is general.**

**It applies to any single-target declaration: `Strike`, Power, Precision, Position, Control.** **It does not apply to a Velocity chain or a Spread chain** — **both set their own count, and `§7.1`'s replacement principle governs there.**

**So the Dark Jedi gets two Crushing Strikes and the damage bonus applies to both.** **Barrage stays at three.**

## PT-11 — Threat range: form first, then multiply. **Confirmed.**

**Aelin in Resilience threatens on 17–20 with Deathstroke, not 13–20.** **The defensive form blunts her critical game, which is the trade.**

## PT-12 — Knockback

> **3 squares. The target lands prone. Standing costs half their movement.** ***Raised from 2 by `PT-43` — at 2 it denied nothing.***

**Raising it from the provisional 1 square. At 2 metres a square, one square is a stumble.**

## PT-13 — Encounter boundaries

**Reset between encounters:** **the reaction pool** · **once-per-encounter attacks** · **initiative** *(re-rolled from the continuing stream)*.

**Do not reset:** **the Force pool** · **its degraded ceiling** · **vitality and wounds** · **consumables**.

**Confirms the playtest's default.**

## PT-14 — Odd-metre radii. **Round up.**

**Reversing the provisional.**

> **Point Blank Shot's 5 metres is 3 squares. Guarding Stance's 3 metres is 2.**

**Round-down makes Guarding Stance adjacent-only, which is not what a bodyguard does, and it makes Point Blank Shot narrower than a basic move.**

**One rule, no exceptions.**

---

# Tier 3 — all thirteen confirmed

**With three notes.**

**"Criticals do not bypass vitality" is right and the reasoning is right.** **Point Blank Shot and Saber Pierce name direct-to-wounds as a once-per-encounter special; it would be worthless if general.**

**"Switching forms costs your Action" is correct** — **so a Jedi switches *or* attacks, never both.** **That is the cost that makes the form gate matter.**

**"Initiative ties by listed order, players first" is adopted as a rule, not just a convention.**

---

# D1 — Apply the pregen corrections. All nine.

**Run S3 onward on corrected sheets and note the change in the report.**

> **The alternative — running stale sheets for consistency — trades a known error for a known error, and the S5 and S7 results would be built on it.**

**Every item in the report's list is confirmed:** Conditioning on four sheets · Toughness on two · T4-K9's Reflex, skill total, BAB, and granted upgrades · the Sith Trooper's skill count · Aelin's Resilience split · the Dark Jedi's Ferocity penalty · HK-24's chain.

**Plus the B2 correction reversing T4-K9's BAB back to +6.**

---

# D2 — Enemy tactics

**Keep declaring your own policy and keep it at the top of each report.**

> **The S2 finding that "nearest, then lowest vitality" funnelled 100% of enemy damage into Aelin is itself a result** — **it says the party has no way to control enemy attention.**

**Nothing in the corpus lets a character taunt, threaten, or draw fire at all.** *An earlier draft of Form VII had a chain called Taunting Strike that did; it was renamed and the effect did not survive.* **So the gap is total, and the policy artefact revealed it.**

---

# What is still genuinely open

| | |
|---|---|
| **Lightsaber base die 2d8** | K1 value, secondary source |
| **Droid plating Defence** | `EQUIPMENT-01 §8` placeholders |
| **Lightsabers add Strength** | provisional, ±3 a hit |
| **Grid diagonals** | **Ruled here: diagonal costs 1 square, diagonally touching is adjacent, and diagonal adjacency satisfies both melee reach and flanking.** |

**Everything else on both blocker lists is answered.**

---

# Added after the S2 re-run

## PT-15 — Ferocity's *Critical Hit Attack +4*

> **It modifies the confirmation roll.** **`FORMS-01 §7`.**

**`ATTACKS-01 §12.6`'s confirmation roll is the only *critical hit attack* in the system.**

**A Juyo duellist does not threaten more often — Ferocity does not touch threat range — they convert far more of the threats they get.**

**⚠ This decided the S2/S3 headline.** **117 party damage against 96, and it flips the corridor from slightly worse to meaningfully safer.**

## PT-16 — Dice indices are mandatory in every log

**A seeded run without an index per draw cannot be checked, and one re-run produced correct values from a stream offset by two draws.**

> **Every attack roll, save, and damage roll carries its index. No exceptions.**

**If a log must be shortened, abridge the narration. Never the dice.**

---

# Added after S4

## PT-17 — Force power effects exist. Sent late, and this is the third such error.

> **`Force_Powers_Table.docx` holds 88 power descriptions with alignment, prerequisites, armour restrictions, and full effect text.** **It was in holdings and never sent.**

**Now `FORCE-POWERS-01`, joined against `POWER-COSTS-01`'s tiers and costs.** **79 of 88 matched a priced row.**

**Both S4 reports found this independently.** **One authored eleven powers to make the scenario runnable and flagged it as the largest authored input in the suite. The other refused to invent effects and ran Force casts as Action-plus-cost bookkeeping only.**

> **Both were right, and the second was more useful** — **it says exactly what is unrunnable rather than papering over it.**

**⚠ S4 must be re-run.** **A power that deals damage or forces a save consumes dice the current runs did not draw. Every index after the first cast is wrong in both reports.**

## PT-18 — An encounter, for per-encounter effects

**`FORCE-POOL-01 §4.1` defines an encounter for alignment drift as *"any discrete scene in which a power was cast."*** **S4's eight consecutive bouts on one map with no break exposed the gap.**

> **An encounter ends when every hostile combatant is removed and the party is no longer under threat.** **A restart against a fresh opponent begins a new one.**

**So S4's eight bouts are eight encounters.** **The reaction pool, once-per-encounter attacks, and initiative all reset between them; the Force pool and its degraded ceiling do not.**

**This confirms the reading both reports used and makes it a rule.**

## PT-19 — Ferocity drift cannot fire on the character S4 assigns it to

**Not a ruling. A scenario defect, recorded.**

> **The Dark Jedi is Committed Dark at 20. `ALIGNMENT-01 §2.6` charges no drift in a dark band. He pays nothing for holding Juyo and never will.**

**The mechanic is aimed at a light-side Jedi reaching for the vicious form, and S4 gives Ferocity to someone already past the point where it costs.**

**The counterfactual is where it lives:** **Aelin at Leaning Light 65 switching to Ferocity would pay 2 an encounter — 16 across eight bouts, dropping her to 49 and out of her band.**

**⚠ S4's stated test of Ferocity drift has never fired and cannot as written.** **Fix the scenario, not the rule.**

## PT-20 — Force powers carry prerequisites and nobody checked them

**Nine of the twenty powers across the three Force sheets were level-illegal.**

> **`FORCE-POWERS-01` carries a Prerequisites column. The power lists were written before that file existed and were never held to it.**

**Aelin and Meris each lost Force Whirlwind, Force Stasis, and Improved Heal. Meris also lost Force Wave. The Dark Jedi lost Force Lightning and Force Choke.**

**`PREGENS-01 §9` records every removal.** **All three sheets are now tier-1 casters with one tier-2 power between them.**

**⚠ The same class of error was already caught and fixed on the attack side** — `PREGENS-01 §4` stripped four illegal attacks for the same reason. **The standard existed; the power lists were added after that pass.**

### It changed the result

**On authored effects, Aelin won eight bouts to nil. On the real powers, legally held, four to three.**

> **Force Stasis was the whole difference.** **The authored version was a Will save at DC 20 landing 85% of the time. The real power is Fortitude at DC 15 — and she cannot have it at level 8.**

**Every scenario from here checks powers against prerequisites the way it already checks attacks.**

---

# Added after S4 re-run 2

## PT-21 — Self-buffs are Bonus actions

> **A power whose whole effect is a timed bonus on the caster costs a Bonus, not an Action.** **`ACTION-ECONOMY-01 §6.1`.**

**Force Aura · Force Shield · Force Armor · Force Valor · Burst of Speed and its chain · Force Body · Breath Control · Energy Resistance · Dark Fury.**

**Everything else remains an Action, including Battle Meditation** — it buffs the party, not the caster.

**Three runs of S4 measured this rather than argued it. Not one buff was cast in sixty rounds.** **A self-buff costing the Action must beat a full round of attacks across its whole duration, and none can.**

## PT-22 — Two findings recorded, not fixed

**`Unbreakable Circle` is an always-correct option in a single-target duel.** **Both S4 reports named it independently.** *"Four Crushing attacks, zero hits"* across two separate round-pairs. **+8 Defence, DR 8, and a cumulative attack penalty compounding while it holds.**

> **And leaving it is a cliff.** **The switch drops all three at once, and in one bout the Dark Jedi killed Aelin during the round she spent switching.**

**Recorded for the balance pass. Not patched mid-suite** — **S8 exists to find exactly this, and it has now been found twice from independent runs.**

**Not one reaction fired in sixty rounds.** **Scenario-specific rather than a defect:** **neither duellist holds Parry, Jedi Defense needs blasters, and opportunity attacks need someone to leave reach in a fight where nobody moves.** **S5 and S7 are where the reaction pool gets tested.**

## PT-23 — S4 does not test Force depletion, and cannot as written

**Both reports ended with pools near full — 28 of 33 and 20 of 24.**

> **Depletion depends entirely on tactical policy.** **A model that casts every round tests it; one that treats powers as openers does not.**

**⚠ Fix the scenario, not the rule.** **S4 should instruct a Force-forward policy, or S7's gauntlet becomes the only depletion test in the suite.**

---

# C24 — The duration conversion was wrong, and it caused C21

**Reversing C17's duration rule and, with it, C21.**

## What happened

**C17 converted durations by wall-clock seconds: 20 seconds ÷ 6-second rounds = 4 rounds.**

> **KOTOR runs 3-second rounds. Twenty seconds there is seven rounds of play, not three.**
>
> **Converting by seconds instead of by rounds halved every duration in the game.**

**Fifty-five powers carry a duration. Every one of them was cut in half.**

## The correction

> **Convert by rounds, not by seconds. Divide the printed seconds by 3, rounding up.**

| | Printed | Was | **Is** |
|---|---|---|---|
| Force Aura · Force Valor | 20 s | 4 | **7** |
| Force Barrier · Dark Fury · Beast Trick | 30 s | 5 | **10** |
| Burst of Speed · Knight Speed · Master Speed | 36 s | 6 | **12** |
| Crush Opposition · Inspire Followers · Improved Force Barrier | 45 s | 8 | **15** |
| Force Immunity · Force Resistance · Master Force Barrier | 60 s | 10 | **20** |
| Energy Resistance chain | 120 s | 20 | **40** |
| Breath Control | 240 s | 40 | **80** |

## What it does to the buffs

**Five of nine become worth an Action. Three are marginal. One stays dead.**

| Power | Total value | Against one round of Barrage — 47 |
|---|---|---|
| **Dark Fury** | 60.0 | **worth it** |
| **Burst of Speed** | 57.6 | **worth it** |
| **Force Valor** | 49.0 | **worth it** |
| Force Armor | 45.5 | marginal |
| Force Shield | 38.5 | marginal |
| Force Aura | 33.6 | marginal |
| Force Body | 30.0 | still dead |

> **That is a healthy spread and not everything needs to be good.** **Nobody casts Force Aura when Force Valor exists — which is a choice rather than a dead branch.**

## PT-21 is withdrawn

**Self-buffs go back to costing the Action.**

> **They were never mistuned. The conversion had halved them, and I ruled on the symptom.**

**And the original objection to making them Bonuses was right: at a Bonus cost you would always buff and then attack, which is as degenerate as never buffing.**

**At the corrected duration the decision is real:** **buffing on round 1 of a long fight pays; buffing on round 5, or in a two-round bout, does not.**

**⚠ Every scenario run under C17 used halved durations.** **Force Slow, Fear, Stasis, and every buff were all short.** **Not worth re-running S1–S4 for it, but note it against those reports.**

## PT-25 — A self-buff does not end your turn

**`ATTACKS-01 §2` ends the turn when the declaration resolves. Self-buffs are exempt.**

> **You may move after casting one.** **You still may not attack — the Action is spent.**

**Everything else ends the turn as before: attacks, offensive powers, heals, and anything cast on an ally.**

**Why only self-buffs.** **A character who buffs is otherwise rooted for a round**, in a system where position decides flanking, cover, reach, and every Spread chain. **Paying your attack for a buff is a fair price. Paying your attack *and* your position is what made buffing unattractive even before the duration error.**

**And it is the KOTOR image: a Jedi raises a barrier at the door and then walks through it.**

---

# Added after S5

## PT-26 — Droids cannot make opportunity attacks

**`ACTION-ECONOMY-01 §4`.** **An opportunity attack is one `Strike`; `Strike` is melee; melee is chassis-blocked for every droid.**

> **A droid with a reaction allowance and no reaction chain cannot spend it at all.**

**S5 printed five reaction uses across four enemy droids. None was legal.**

**Any droid meant to react holds `Snap Shot` or `Overwatch`.** **HK-24 now does.**

## PT-27 — Four of HK-24's attacks were feats

**`Assassin Protocols` and `Target Analysis` are Assassin-droid *feat* chains. Both were in his attack budget.**

> **He was overspent four feats and underspent four attacks, and `Improved Target Analysis` — which he never legally had — gave him 136 damage at an 83% hit rate, the most dangerous enemy in the suite.**

**Rebuilt.** **Three feat picks at level 6, and the two Assassin chains cost all three.** **Hardened Chassis, Weapon Focus, Toughness, and Improved Target Analysis are gone. Vitality 59, wounds 17.**

**This is the third budget error of the same shape** — illegal attacks in `§4`, illegal powers in `§9`, and now entries in the wrong budget entirely.

> **The check that catches all three is one script, and it should have been written after the first.**

## PT-28 — Two scenario defects in S5, both mine

**`SCENARIOS-01 §S5` says to build the Battle Droid from `ACTION-ECONOMY-01 §8.2`. There is no §8.2** — §8 is Flanking. **§18.2 is the proficiency table and supplies nothing else.** **The correct source is `CLASS-TABLES-DROID`, which did not exist when the scenario was written.**

**And S5 names ion damage as one of four things under test.** **No character on either side carries an ion weapon.** **The test cannot fire.**

> **Same shape as `PT-19`'s Ferocity-drift defect.** **Two of eight scenarios now name a mechanic they structurally cannot exercise.**

**⚠ Before S6: check each remaining scenario's stated tests against the sheets it uses.**

---

# Added after S6

## PT-29 — Stealth damage is a rider, not a declaration

> ***Stealthy Shot* and `Sneak Attack` are removed from the attack rosters.** **`Ambush → Improved Ambush → Master Ambush` replaces both, in `FEATS-LIBRARY-01`.**

**When you attack a target that cannot see you, add 2d6 / 4d6 / 6d6 to the first attack of your declaration**, capped at Stealth ranks ÷ 3, and the target loses its Dexterity bonus to Defence against it. **Master Ambush's critical deals its damage directly to wounds, once per encounter.**

### Why

**As a declaration, a stealth opener was one attack competing against Velocity's three.**

| | Attacks | Damage each | Total |
|---|---|---|---|
| **Silenced Shot** *(level 4, Stealth 10, two picks)* | 1 | 17.5 | **17.5** |
| **`Shoot`** *(free, universal)* | 2 | 4.5 | 9.0 |
| **Barrage** *(unconditional)* | 3 | 13.0 | **39.0** |

**Both S6 reports found `Shoot` matching or beating *Silenced Shot*.** **A level-4 chain gated behind ten ranks of Stealth and two attack picks lost to the attack everyone owns for nothing.**

### And it was our departure, not the source's

**KOTOR's Sneak Attack is a passive.** **3.5's is a rider on any qualifying attack.** **5e's is once per turn, added to an attack you were making anyway.**

> **All three attach stealth damage to an attack. None makes it an attack you take *instead* of attacking normally.** **We were the outlier, and being the outlier is why the branch was dead.**

**As a rider, Dek declares Rapid Fire from stealth — three shots, the first carrying 3d6, about 24 expected against 17.5.**

## PT-30 — Surprise: no action in round 1

**`ACTION-ECONOMY-01 §9`.** **A surprised character takes no move, Action, Bonus, Gear, or reaction in the first round.**

**Replaces *acts last and no reactions*, both of which were inert.** **S6 ran four ambushes and surprise changed nothing in any of them.**

## PT-31 — `Ready` is the ranged answer to an approaching enemy

**No rules change. Opportunity attacks trigger on *leaving* reach only, which is D&D's own line.**

> **`Ready` has been in `ACTION-ECONOMY-01 §1` for six scenarios and no character has used it once.**

**`Guarded Step` is the feat that grants an opportunity attack against someone moving to flank** — our equivalent of the one D&D exception.

## PT-32 — Staggered dice for single-declaration comparisons

**`DICE-01 §2`.** **When several runs compare one action, each starts a few draws further into the sequence.**

**S6's four openers all drew `d20[5]` because initiative consumes exactly five draws every time.** **Four openers, one roll, all missed.**

---

# Added after S6

## PT-29 — Stealth damage is a rider

**`Sneak Attack` and *Stealthy Shot* left both attack rosters and became one feat chain.** **`ATTACKS-01 §13`.**

> **The dice attach to the first attack of whatever you declare. They are not a declaration you choose instead of attacking.**

**Every source does it this way.** **KOTOR makes it a passive. 3.5 applies it to every qualifying attack of a full attack. 5e adds it once per turn to an attack you were making anyway.**

**S6 measured the cost of being the outlier.** **A level-4 chain gated behind ten ranks of Stealth and two attack picks was worth 14.8 a round; `Shoot`, which everyone owns for nothing, was worth 9.**

| | Per round | To drop a Sith Trooper |
|---|---|---|
| As a declaration | 14.8 | 3.0 rounds |
| **As a rider** | **22.0** | **2.0 rounds** |
| *Korr's Barrage* | 27.3 | 1.6 rounds |

**The melee and ranged versions collapsed into one** — **as a rider it does not matter which weapon you hold.** **Position keeps `Quick Attack` and `Point Blank Shot`.**

**Dek rebuilt: two attack picks freed, two feat picks spent.**

## PT-30 — Surprise removes the round

**A surprised character takes no action in round 1 at all.** **No move, no Action, no Bonus, no Gear, no reactions.**

**This is 5e's 2014 rule.** **The previous version — *acts last, and no reactions* — was inert in both halves.**

> **S6's ambusher rolled initiative 21 against the patrol's best of 19. He led the order anyway.** **And the troopers held one reaction each with no reaction chain, so they had nothing to lose.**

## PT-31 — No change to reactions. Use `Ready`.

**Reversing my own recommendation.**

> **D&D has no general "entering reach provokes" rule.** *"It is a house rule in 5e."* **The only exception was the Polearm Master feat, and the 2024 revision removed even that.**

**And ranged characters do not get opportunity attacks in D&D by design** — **melee gets zone control, ranged gets range.**

**The answer already exists in our own action list.** **`Ready` — name a trigger, spend a reaction when it fires.** **It has been available for six scenarios and no character has used it.**

**We also already have the Polearm Master analogue: `Guarded Step`**, which grants an opportunity attack when an enemy moves to flank you. **A feat, exactly as D&D does it.**

**This is a discoverability finding, not a rules gap.**

## PT-32 — Staggered dice offsets for single-declaration comparisons

**`DICE-01 §2.1`.** **A scenario comparing one declaration across several runs offsets each run by one draw.**

**S6 restarted at index 0 four times.** **Initiative consumes exactly five draws, so every opener drew `d20[5]` — a 5 — and every one missed.**

> **Four openers compared on a single die, and the die was a miss.**

**Restart-at-zero stays correct for long fights like S2 against S3.** **The rule is about sample size: identical dice compare long fights, staggered dice compare single actions.**

---

# Added after S7

## PT-33 — `Sneak Attack` was moved and never written down

**C29 removed the stealth chains from both attack rosters. The feat chain that replaced them was written into the data under one name and referenced in three documents under another.**

> **`FEATS-LIBRARY-01` mentioned *Ambush* twice and defined it nowhere.** **`Killer's Instinct` still said it stacked with a chain that no longer existed.** **And Dek's sheet still spent two attack picks on `Stealthy Shot → Silenced Shot`, which had been deleted.**

**Fixed.** **The chain is `Sneak Attack → Improved Sneak Attack → Master Sneak Attack`, in `FEATS-LIBRARY-01`.** **Dek's two void picks go to `Rapid Fire → Open Fire`, which C29's own worked example presumed.**

### The report's diagnosis is right and it is the useful part

> ***"`audit_sheets.py` would not catch this, because the entry validates against a roster that no longer contains it. The check that catches it is: does every named chain resolve to a definition."***

**`scripts/audit_refs.py` now does exactly that.** **It reads every backticked name in every document and fails if it does not resolve.**

**It found three more on its first run** — two dead stealth names and ***Taunting Strike*, which `D2` cited as the one thing in the corpus that lets a character draw fire.** **It does not exist either.** *An earlier Form VII draft had it; the chain was renamed and the effect did not survive.* **So the draw-fire gap is total, not partial.**

**Convention adopted: backticks mean the thing exists. Retired names go in plain italics.**

## PT-34 — Skills are allocated nowhere

**Every sheet prints a skill *total* and no allocation.** **Korr 22, Vess 77, Dek 99, Meris 66 — and Dek's Stealth 11 is the only allocated rank on any sheet in the suite.**

> **So `B3`'s Medicine scaling could not be computed and medpacs ran at a flat 2d8 all gauntlet.**

**⚠ This blocks any skill check in any scenario, not just Medicine.** **Allocation is the next thing the sheets need.**

## PT-35 — Two scenario inputs that do not exist

**Vess's 2 frag grenades are unstatted** — **no damage, no radius, no save anywhere in the corpus** — and `ACTION-ECONOMY-01 §1` makes throwing one an Action.

**And `§S7` names two Battle Droids without printing a stat block**, so both reports reused the S5 reconstruction.

**Same shape as `PT-28`. Scenario inputs need the same completeness check the sheets now get.**

---

# Added after S8

## PT-36 — `Ataru Flurry` was strictly better than `Barrage`

**Four attacks at −1 with a Dexterity strip, against Barrage's three at −1. Same axis, same penalty, one more attack, and a rider.**

> **57.0 against 33.8 — a 69% margin over the declaration that won seven scenarios.**

**Two fixes, both applied.**

**The Dexterity strip is gone.** **It is Form VII's identity** — *Staccato Assault* strips Dexterity and that is what the Ferocity chain is for. **Having it on Form IV as well was duplication, and it was the larger half of the problem.**

**And the penalty ladder is now one step worse than Flurry's at every tier** — **−5/−4/−2 against −4/−2/−1.**

**Result: 42.0 against Barrage's 33.8.** **Twenty-four per cent better, for 2 Force points a round and a form lock.** **A premium, not a domination.**

**⚠ My error, from the session where the count was raised to four.** **The report is right that the Force cost is not a constraint at level 8** — 2 a round against a 37-point pool regenerating 1 is a net drain of 1, sustainable for 37 rounds, and the longest fight in the suite was 13.

## PT-37 — `Vornskr's Frenzy` reduced every defender to Defence 10

**Two rules read together, exactly what S8 exists to find.**

> **`ATTACKS-06`: *"the target loses all Defence bonuses of every kind."*** **`EQUIPMENT-01 §5.1`: Defence is *10 + armour + Dexterity*.**
>
> **Every point above 10 is a bonus. There was nothing left but the 10.**

**And the report's reasoning for why the literal reading was forced is correct:** **the tier below already strips form and stance, and `ATTACKS-01 §3` requires each tier to be strictly better.** **So tier 3 had to strip more, and the only thing left was everything.**

**Rewritten:** **the target loses its Dexterity bonus and every bonus from a form, a stance, or its own declaration.** **Armour and cover still apply.**

**That is strictly better than tier 2 without being total.**

## PT-38 — Forms and feat picks. **Forms do not cost picks.**

**`ATTACKS-06` says forms are feats; `FORMS-01` says acquisition is unwritten.** **S8 could not build its character without an answer.**

> **A form is granted, never bought.** **By class level, by training, or by a holocron — the class workstream sets the schedule.**

**Why.** **Every pregen in eight scenarios was handed a form with no pick shown against it, and the alternative makes a four-form Guardian spend four of five feats on the ability to switch stance.** **Forms are exclusive — you hold one at a time — so paying a pick each for options you cannot use simultaneously is a tax on flexibility with no upside.**

## PT-39 — Three things S8 could not test

**Species were never sent.** **`species-chapter.md` is in holdings and has never gone out.** **Fifth send error of this shape.** > **A break-it pass needs it: racial ability adjustments interact with every gate in the rosters — Strength 13, Dexterity 13, Dexterity 12 — and with the point-buy ceiling.**

**Skills cannot be allocated** — `PT-34`.

**Multiclassing is unresolved** — `CLASS-TABLES-JEDI §5`. **And the report notes the corpus is better for it, since it closes the most obvious degenerate route.**

## PT-40 — The finding S8 was built to produce

> **"Round one, buff. Every round after, declare your Velocity chain. Do nothing else."**

**Barrage was 42 to 55 per cent of party damage in every scenario it appeared in.** **In S4, two Jedi with nineteen available declarations used three.** **In S7, a nine-power Consular resolved to *cast Battle Meditation once, then heal*.**

**Eight axes, 39 chains, 107 entries — and the correct play is one chain and a buff.**

> **⚠ This line read *thirty-eight chains, a hundred and ten entries* until the counts were derived.** **Spelled-out numbers, which `audit_source.py` matched digits only and never saw.** **Corrected and the check extended.**

**⚠ Not fixed here.** **This is the balance pass, and it is the whole of it.** **`PT-36` removes the option that was better than Barrage; it does not make anything else competitive with Barrage.**

---

# C41 — The balance pass on single-attack declarations

**S8's headline was that one declaration produced roughly half of all party damage in every scenario.** **`PT-40` recorded it. This is the response.**

## The diagnosis

> **Velocity multiplies your damage. Everything else adds to it. Multiplication wins, and Velocity was the only multiplier.**

**Korr, single vibrosword, against Defence 18:**

| | Attacks | Per round |
|---|---|---|
| **Barrage** | 3 | **31.3** |
| Crushing Blow | 1 | 18.5 |
| Deathstroke | 1 | 13.3 |
| Great Cleave | 1 | 10.4 |

**Velocity keeps its three attacks. The other axes were raised to meet it.**

## Precision applies to every attack

**This is KOTOR's own behaviour — Critical Strike there sets the threat range for the whole round, not for one swing.**

**`Critical Strike`, `Wounding Strike`, `Deathstroke` and their ranged mirrors now read *"threat range ×N, on every attack you make this round."***

> **It was already the case that a declaration modifier applies to every attack. Nothing said so for Precision, and every report read it as one swing.**

**And the chain gained damage it never had.** **Precision was pure threat range — meaning `Deathstroke` did exactly what a plain `Strike` did, with a wider crit window.** **Tier 2 now adds +4 damage and tier 3 adds +8, plus a critical multiplier step.**

## Power's capstones raised

**`Forceful Slash` +8 → +12. `Crushing Blow` +10 → +20, and it now raises the critical multiplier.**
**`Power Shot` +8 → +10. `Blast` +10 → +16, same multiplier step.**

## Spread reaches past adjacency

> **`Great Cleave` was declared zero times in five scenarios by a character who held the whole chain.** **A melee character closing on the nearest enemy engages the edge of a formation, never its centre — it never reached three adjacent targets on any map.**

**At tier 3 it now hits every enemy within 2 squares rather than every adjacent enemy.** **`Sweeping Fire` and `Way of the Sarlacc` match.**

## Where it lands

| | Was | **Is** | Against Barrage's 31.3 |
|---|---|---|---|
| **Crushing Blow** | 18.5 | **26.5** | 85% |
| **Deathstroke** | 13.3 | **21.5** | 69%, **plus a one-round stun** |
| **Great Cleave** | 10.4 | **20.9** *(two targets)* | 67%, **and it scales with enemy count** |

**None of them beats Barrage on raw damage against a single target, and none should** — **Velocity is the damage axis.**

**Each now carries something Barrage cannot do.** **Crushing Blow knocks a target back two squares and prone. Deathstroke stuns for a round. Great Cleave hits several enemies.**

**⚠ What this does not fix.** **Control, Support, and Reaction were never damage-competitive and are not meant to be.** **An AI optimising damage will not declare `Covering Fire`.** **Measuring those axes needs scenarios that are not damage races** — `PLAYTEST-DESIGN-01 §9`.

---

# C42 — `§7.1` governs, and the Power bonus becomes once per round

**The S8 re-run found that `PT-41`'s balance pass lands or inverts depending on which half of `ACTION-ECONOMY-01 §7` is read — and that both halves are in the same section of the same document.**

> **`§7.1`: *"a second weapon adds one attack to any declaration."*** **`§7.5`, two hundred lines later: *"Only `Strike` and `Shoot`."***

**Under `§7.5`, `Barrage` leads and Power sits at 88%. Under `§7.1`, a dual-wielding `Crushing Blow` beats `Barrage` by 32%.**

**⚠ And this is the third report to flag it.** **`PT-9` ruled `§7.5` governs and said `§7.1`'s table would be corrected to match.** **It was revised the other way instead** — **by me, in the same session that wrote `PT-41`.**

## `§7.1` wins, because it is KOTOR's

**A second weapon there grants one extra attack whatever you queued, and Power Attack's bonus applies to all of them.** **`§7.5` is rewritten to agree.**

**Which makes `PT-9` wrong and this reverses it.**

## But that alone would invert the balance pass

> **A flat per-attack bonus cannot be balanced against a count multiplier at two different attack counts.**

**Power needs +26 damage to tie `Barrage` at one weapon, and +13 at two.** **One number cannot be both, and `PT-41` raised it to +20** — **tuned against a single-weapon character, which doubled the exposure at two.**

## So the bonus is once per round

**Power and Precision now read *"+N damage on the first attack that hits this round."***

**Applies to `Power Attack`, `Forceful Slash`, `Crushing Blow`, `Charged Shot`, `Power Shot`, `Blast`, `Wounding Strike`, `Deathstroke`, `Sniper Shot`, `Assassinate`.**

**Precision's threat range still applies to every attack.** **Only the damage is once.**

| | vs Def 18 | vs Def 22 |
|---|---|---|
| **Barrage**, single weapon | **37.0** | **29.2** |
| Crushing Blow, single | 31.3 | 24.8 |
| **Barrage**, dual-wielding | **49.4** | **39.0** |
| Crushing Blow, dual | 43.7 | 34.5 |

> **Velocity leads in both configurations. Power sits at 85–88% in both.** **The `PT-41` spread now survives dual-wielding instead of inverting on it.**

**And `Two-Pronged Attack`'s automatic critical threat on the second swing becomes the reason to dual-wield a Power build** — a rider, not a doubling.

---

# C43 — The knockback denied nothing, and prone was never defined

**Both found by the third S8 pass, and both verified.**

## The knockback is 3 squares

**Speed 5 squares. Standing costs half, rounded up: 3. Two movement left.**

> **Pushed 2 squares, the target stands, walks back the two squares, and attacks exactly as it would have.** **Zero turn denial, under either rounding convention.**

**At 3 squares it needs three movement and has two. The turn is denied.**

**And 3 matches `Force Push`, which pushes 5 metres and denied the Dark Jedi two full turns in S4** — **the only Force power either Jedi cast in twenty rounds, and the movement denial is why.**

**⚠ `PT-41` moved knockback from a critical to any hit, taking it from firing 7% of rounds to about 90%. It then fired constantly and still did nothing.**

## Prone is defined once, generally — `ACTION-ECONOMY-01 §19`

**+2 damage from melee attacks. Standing costs half your movement. Nothing else.**

**Five documents referenced it and only `Sweep Attack` defined it, for itself.**

## And my C42 sweep was wrong

> **I used P(hit) where the rule needs P(at least one hit).** ***"+20 on the first attack that hits"* with two attacks lands whenever either connects.**

| Defence | Barrage | Crushing Blow | Share | **My sweep said** |
|---|---|---|---|---|
| 16 | 50.9 | 46.7 | 92% | 87% |
| 18 | 44.9 | 42.7 | 95% | 87% |
| 20 | 38.9 | 38.3 | 98% | 87% |
| **22** | 33.0 | **33.5** | **102%** | 87% |

**Dual-wielding, Power overtakes Barrage at high Defence and the margin grows.**

> **The report's diagnosis is the valuable part: `PT-42` did not remove Power's scaling, it moved it from attack count to target Defence.**

**Which is a better place for it.** **Power is now the answer to armoured targets and Velocity the answer to soft ones** — **a real tactical distinction rather than a flat tax.** **But it was not what `PT-42` was aiming at, and it is worth knowing it is there.**

**Left as is.** **102% at Defence 22 while dual-wielding is a narrow, legible advantage in the configuration that costs you a −1 on every attack.**

---

# C44 — Enemy targeting, and `Guarding Stance` repriced

**The suite's largest unresolved finding: in four scenarios one character absorbed 90–100% of all enemy damage, decided by a square of positioning.**

## The rule — `ACTION-ECONOMY-01 §20`

**Each enemy scores every reachable hostile and attacks the highest.** **Nearest is +4. An ignited lightsaber is +2. Having damaged this enemy is +2.** **Attacking the same target twice running is −3.**

> **The −3 is what produces the spread.** **Without it the scoring is stable and every enemy converges on one target — the exact failure measured.**

**And the lightsaber preference explains a result the suite already produced:** **Aelin absorbed the damage in S2 and S3 because she was the Jedi. Nobody had written down that this was why.**

## `Guarding Stance` rebuilt

**It was worth about 4 damage against 37 forgone — five to one against, and nobody declared it in eight scenarios.**

**Three changes:**

**It persists** until you declare a different attack, drop to 0 vitality, or the ally leaves range. **It is called a stance.**
**Your own attack rolls take −2 while it holds** — the ongoing price, instead of your whole turn every round.
**And it redirects hits rather than absorbing them.** **The attack re-resolves against your Defence.**

> **The redirect is the whole chain.** **Absorbing a hit is net-zero unless you are tankier. Re-resolving it is not.**
>
> **A Sith trooper needs 14 to hit Meris and 19 to hit Korr. The same attack goes from 80% to 55% just by changing who it is aimed at — and the hits that do land meet 84 vitality instead of 34.**

**`Interpose` and `Bulwark` scale the redirect to 2 and 3 hits per round.**

**⚠ `Krayt's Answer` becomes playable.** **It pays +7 attack and +7 damage per enemy who struck you, stacking to five, in a system where nobody could choose to be struck.** **Under `§20` a Form V duellist can now stand forward, draw fire by proximity and blade, and be paid for it.**

---

# C45 — Conditions defined centrally, and a saved stun becomes Slowed

**`ACTION-ECONOMY-01 §19`.** **Raised by both suite postmortems: prone, stunned, slowed, and unaware were each defined inside whichever entry first needed them, then referenced by four or five others as though general.**

## Stunned

**Lose your full turn. No reactions. Attacks ignore your Dexterity bonus to Defence.**

**Refreshes on a fresh stun. Does not lose a readied action already declared.**

## Surprised

**No action in round one. No reactions. Not easier to hit.**

> **Surprise is a failure of attention, not of balance.** **A surprised soldier still has his shield up and his feet under him.** **`Sneak Attack` is what rewards attacking someone who cannot see you, and it is a separate condition.**

## Slowed

**Source: `Force Slow` — *"−2 penalty to Defense, Reflex saves, and attack rolls,"* 30 seconds, ten rounds.**

**Plus two of ours: movement halved, and **`Jedi Hunter` range halved with it** — 5 squares to 2.**

> **Which turns `Force Slow` into a targeting tool.** **A slowed trooper who cannot close on the Jedi stops trying and deals with whoever is in front of him.** **Cast on the enemies converging on your Jedi, it sends them back to the rest of the party.**

**And it gives a Consular something to do that is neither damage nor healing** — **which S7 found she badly needed, her nine-power sheet resolving to *cast Battle Meditation once, then heal*.**

## A saved stun becomes Slowed

> **A successful save against a stun does not negate it. The target is Slowed for the same duration instead.**

**The source states this on every stun power it has.** **`Force Stun`: *"A successful Fortitude save… means the target is slowed for the duration instead of stunned."***

**Applies to every stun in the system, Force powers and weapon riders alike.**

**A stun is never wasted. You either lose your turns or you get slow.**

**⚠ And the two rules meet.** **An enemy who saves against a stun aimed at protecting your Jedi is Slowed, so his `Jedi Hunter` range halves and he stops chasing her anyway.** **The power redirects him either way.**

## Stun durations

| | Rounds |
|---|---|
| **`Critical Strike` · `Precise Shot`** | **1** |
| **`Force Push`** | **1** |
| **`Force Wave`** | **2** |
| **`Force Stun`** | **3** |
| **`Force Stasis`** · `Stun Droid` · `Disable Droid` · `Destroy Droid` | **4** |

**Converted at `PT-24`'s rate.** **The weapon riders stay at one round deliberately — a rider on an attack should not match a power costing an Action and Force points.**

## PT-45.1 — Unaware

**`ACTION-ECONOMY-01 §19.5`. The fourth and last condition.**

> **A character is unaware of you if they cannot perceive you: you are Hidden from them, they are Stunned, or they cannot see.**

**Attacking reveals you. Attacks against an unaware character ignore their Dexterity bonus to Defence.**

**Two things it fixes.**

**The Dexterity strip lived inside `Sneak Attack` only**, so `Killer's Instinct` fired on the same trigger and got the dice without it. **It is general now and `Sneak Attack` just carries dice.**

**And `Killer's Instinct` said unaware meant *"you are in Stealth, behind it, or it is blinded."*** **`PT-2` struck facing from the corpus when it removed `Jedi Defense`'s 180° arc.** **The middle clause was unreachable and is gone.**

**Deliberately not unaware: surprised, prone, slowed, flanked, or a target that has not acted yet.**

> **Surprised stays out because `§19.2` says a surprised character is not easier to hit.** **Making surprise confer unaware would strip Dexterity and quietly reverse that.**

**And the same test runs in reverse for `Jedi Hunter`** — **a Stunned enemy, or one you are Hidden from, cannot see your lightsaber.** **One definition serves the stealth feats and the targeting rules.**

---

# C46 — Two targeting models, both live

**`TARGETING-01` rewritten. Two gates, then a score.**

## What happened

**`ACTION-ECONOMY-01 §20` carried a complete scoring model.** **`TARGETING-01` was later written as a ladder, independently, by someone who did not know the first existed.** **Both were live for a day and they contradicted each other on the sign of persistence.**

| | `§20` | The ladder |
|---|---|---|
| **Attacked them last round** | **−3** — *"the load-bearing clause"* | **tier 2, a positive** |
| Attribution | +2 preference | hard tier |
| Lightsaber | +2 preference | near-absolute |
| Sheathing the blade | drops the +2 | *"you do not stop being the Jedi"* |

**Found by the targeting agent on its first read.**

## The model now

**Gates first — reach, sight, still standing.** **Binary, no arithmetic.**
**Then a score.** **Nearest +4, lightsaber +2, drew blood +2, attacked them and failed −3, both hold sabers +3, `Jedi Hunter` +3, `Guarding Stance` −4/−5/−6.**

> **The two halves answer different kinds of question.** **A ladder is right for *can I see them*. A score is right for *how much do I want to*.**

**And `Guarding Stance` only works in a score** — its −4 needs something to subtract from. **Under the ladder it did nothing to who got shot, while `§20.4` sold it to players as the largest counter available.**

## Three fixes it carried

**The duellist rule was an uncapped override.** **Four saber-armed Sith against one party Jedi sent all four across, reproducing the measured failure in the document written to prevent it.** **It is +3 now, which loses to being adjacent.**

**`§3.2` said *"a ranged weapon **or** in melee with nobody,"*** **permitting exactly what its own gloss forbade.** **Gone with the tier structure.**

**And nothing said what an enemy *does* with its target.** **`§5` now does: attack if you can, otherwise move toward them; if nobody passed the gates, advance and do not attack.**

## The gate could not have caught this

**All six checks passed.** **Both documents were internally consistent, every name resolved, every count matched.**

**`audit_ownership.py` is the seventh check and it is advisory, because it cannot tell a cross-reference from a rival definition.** **It lists candidates and a human looks.**

> **The tell is that the second document states the rule *in full* — a table, a complete procedure — rather than citing it.**

---

# C47 — Targeting, third revision

**Two reports from the targeting agent. Every structural finding verified.**

## What was broken

**Proximity was ordinal, not spatial.** *"Nearest +4, each further one in order."* **An enemy scored the Jedi 3 whether she was two squares away or twenty.** **Not deliberate — carelessness — and seven other rules had been written to compensate for it.**

**Force bonuses were uncapped.** **An ignited lightsaber was +2 and *"you hold a lightsaber and so do they"* was +3, and both fired at once.** **Five, or eight with `Jedi Hunter`, against a proximity range of four.** > **`§4.2`'s own warning box computed the sum using one of the two rows and certified a failure as fixed while it was alive.**

**The `−3` and `+2` fought each other.** **Net −1 against someone who fought back, full −3 against someone who did not** — **weakest against damage dealers, strongest against healers.** **And against two mutual attackers the signs alternated every round, producing exactly the metronome KOTOR does not have.**

**And a three-Jedi party had a fourth member nobody would ever attack.**

## What it is now

**Three bands.** **Adjacent +4, within your own movement +2, beyond 0.**

**Heat is a table, maximum +2.** **Ordinary enemy sees +1 for an ignited saber and 0 for a shown power; a `Jedi Hunter` or a saber-armed enemy sees +2 and +1.** **The duellist preference is a row rather than a fifth bonus.**

**Attribution is +3 and it beats all heat.** **Whoever hit you is who you fight; the Jedi earns your attention back by closing or hurting you.**

**The `−3` no longer applies to anyone who damaged you.**

**`Guarding Stance` is −2 / −3 / −4**, down from −4 / −5 / −6. **At the old numbers it deleted its protectee from consideration, which made its own second clause — *redirect a hit* — unreachable.**

## Six of seven lost rules stay lost

**The 5-square charge gate, the long-range exception, the in-melee gate, the retarget cap, path-blocking geometry, and the two-sabers tiebreak.**

> **They were compensating for ordinal proximity. The band boundary *is* the charge gate, expressed as a score row instead of a condition.**

**`Force Slow` recovers its targeting function for free: the middle band is the enemy's own movement, so halving one halves the other.** **`ACTION-ECONOMY-01 §19.3`'s dangling pointer is deleted rather than repaired.**

**The cap stays deleted, and the agent's reasoning is better than mine was.** > **A cap owes an answer about what the capped enemy does instead, which a score has no memory to provide — and it couples to initiative, so how much heat a Jedi draws would depend on a d20 rolled once at encounter start.**

---

# C48 — The row, not the layer

**A three-layer model was proposed — gates, a damage-shortlist, then a score.** **Rejected, and one case decided it.**

> **The gates are gates on *states*. Attribution-by-damage is a gate on an *outcome*, resolved by a d20 after the player has committed.**

**A Soldier who misses is not deprioritised under a shortlist. He is absent — and the enemy leaving him provokes a free swing at its back.** **At ordinary hit rates that is a third of all rounds, on the character whose whole job is standing in front.**

**And `Guarding Stance` deals no damage, so a bodyguard could never be a candidate and the chain would be inert in its own use case.**

## What went in instead

**One row: *entered your reach from beyond it this round, +2*.**

**Symmetric — anyone, not only Force users.** **Which is right in the case that separates them: an enemy shot from a doorway scores that shooter 5, and a Soldier who charges in scores 6 and pulls him.**

**⚠ Drafted as *entered from beyond*, not *is adjacent*.** **`ACTION-ECONOMY-01 §8` lets a character circle freely once in reach, and *moved adjacent* would pay +2 for every flanking sidestep.**

## And a ratchet I introduced two rulings ago

**`PT-47` suppressed the `−3` against active attackers. That fixed the metronome and created a lock.**

> **Two characters adjacent and both damaging an enemy each score 7. Exact tie, and nearer is a tie too. It fell to *lower current vitality* — so the enemy hit whoever was weakest, made them weaker, and found the identical position next round.**

**`Lower current vitality` was written as a coin-flip resolver and had been promoted to a primary rule deciding melee scrums outright.**

**Four tiebreaks now, and the last always resolves: the nearer, then most damage dealt to you, then lower current vitality, then a d20 drawn from `DICE-01`.**

**Most damage dealt is stable for a visible reason and tracks a quantity that moves both ways, so it is not a ratchet.**

**Vitality survives as the last word.** > **To reach it two targets must match on score, distance, *and* damage dealt.** **A vibrosword at 8 to 18 and a blaster rifle at 1 to 8 rarely land on the same number, and when they do the next round differs and tiebreak 2 resolves it.**

**It was only a ratchet as the primary resolver in a configuration that recurred every round.** **Demoted, it is sensible: two identical threats, finish the hurt one.** **And it is deterministic, so a seeded replay reproduces it without spending a die.**

## PT-48.1 — No tie may end unresolved

**A fourth tiebreak: draw a d20 from `DICE-01` for each remaining target, highest takes it, redraw on a tie.**

**Reaching it means two targets are identical in score, distance, damage dealt to you, and vitality.** **There is nothing left to prefer.**

**Drawn rather than rolled, so a seeded replay reproduces the fight** — **`ENGINE-SHAPES-01` makes the engine event-sourced, and an unreplayable targeting decision breaks the seed as surely as an attack roll would.**

**⚠ If a playtest shows it firing often, something above it has stopped discriminating.** **That is the finding, not the dice.**

---

# C49 — Four corrections, and the targeting draw gets its own sequence

**Final inspection pass. Three text errors, one live consequence, and the agent's verdict: it is finished and should go to the table.**

## The one that blocked a scenario

**The fourth tiebreak drew from the shared d20 stream.** **`DICE-01 §2` builds its whole comparison design on S2 and S3 running identical dice.**

> **Targeting ties are geometry-dependent. Different maps produce different tie counts, so different draw counts.** **The two sequences desynchronise at the first tie and never realign, and from that point the difference between them is cover, flanking, *and an unknown offset*.**

**Fixed with a separate `t20` sequence. 200 values.** **Attack rolls stay aligned between the maps; the tiebreak still resolves.**

**And *"it fires almost never"* was false in round one** — **nobody has damaged anyone, nobody has closed, nobody was attacked last round, everyone is at full vitality, so tiebreaks 2 and 3 are inert.** **Two same-class characters at equal distance go straight to the die on the opening round.**

## The metronome was narrowed, not fixed

**`PT-47`'s suppression handled two mutual attackers. Two adjacent characters who both *missed* still alternate.**

> **And it cannot be written away.** **Any drift term with one round of memory alternates between two otherwise-equal candidates. The alternation is a property of the constraint, not the wording.**

**The row now reads *the −3 does not apply to anyone adjacent to you*** — **which removes it from the case that matters and leaves it accepted beyond reach.**

## The bodyguard could not hold an enemy

**`Guarding Stance` deals no damage, so its holder took the full −3 every round after being attacked.** **Adjacent bodyguard 1, distant Jedi who shot the enemy 5.** **The enemy disengaged, took a free swing at the bodyguard's back, and walked away.**

> **Root cause: attribution +3 plus heat +2 is 5, and 5 beats the 4 that adjacency is worth.** **`§3.5`'s claim that everything fits inside the band gap was true of heat alone and false of heat plus attribution.**

**Fixed: the +3 only applies to someone within your own movement.** **You turn toward whoever hit you; you do not cross a map to chase a sniper.**

## Two rows became one

| The last exchange | |
|---|---|
| They damaged you since your last turn, and are within your movement | **+3** |
| Otherwise, you attacked them last round, they still stand, and are not adjacent | **−3** |
| Otherwise | **0** |

**Three mutually exclusive states, one lookup, no cross-reference.**

## And the arithmetic was wrong again

**`§3.2` read *"closing and hitting is 9."*** **It is 11.** **And *"a charging Soldier is 6"* silently assumed he missed — charging and hitting is 9.**

> **Third time a worked example in this document has computed a sum from some of its rows.** **Standing rule adopted: any worked example names every row it used.**

## The verdict

**The agent's, and I agree with it.**

> **Every rewrite so far was driven by inspection, and this model has never been playtested at any version.** **The structural questions are well-argued; the magnitudes are all chosen rather than derived.** **Those are the things only dice can answer.**

**Targeting is closed. It goes to the table next.**

---

# C50 — Force regeneration has two units, and the powers were bumped

## Regeneration

**In combat, per round. Out of combat, per second.**

| Class | In combat | Out of combat |
|---|---|---|
| **Guardian · Sentinel · Weaponmaster · Marauder** | **1** | **1 / second** |
| **Consular · Watchman · Assassin** | **2** | **2 / second** |
| **Jedi Master · Sith Lord** | **3** | **3 / second** |

**`regeneration.2da` gives `forceregen` 0.0 in combat and 1.0 out of it** — **KOTOR grants no Force regeneration during a fight at all.** **⚠ The column never names its unit; per second is an inference.**

**We keep a trickle rather than zero, because a turn-based fight lasting a dozen rounds is not a KOTOR fight lasting twenty seconds.** **The ratio is the source shape: out of combat is roughly six times faster.**

## Which answers how to measure the pool outside a fight

> **You do not.** **Cast freely; the points come back in about a minute.**

**The cost of exploration casting is the working maximum, not the points.** **Degradation applies per cast whether or not anyone is fighting, and regeneration refills only to the working maximum.**

**Four mind-tricks cost eight points of ceiling carried into the next fight.** **One number, and it only moves down.**

## And the diagnosis that started this

**Nothing depleted in the playtests because the sheets held almost no damage powers** — **Aelin 6 powers and none, Meris 9 and none, the Dark Jedi 5 and one.**

> **Powers are not underpowered.** **Force Storm does 168 to a group of six at level 8, four times Barrage. Force Lightning does the same for 14 points. Force Shock does 28 to one target for six.**

**It was a sheet problem the whole time.**

## Seven powers bumped

**The old *Force Wound* is renamed `Force Strangle`, and it now stuns for its duration** — **which the source already implies, since `Force Choke` at tier 2 of the same chain says *"stunning and inflicting."***

**`Force Barrier` and both upgrades absorb damage from any source**, not slashing, bludgeoning and piercing — **`EQUIPMENT-01` makes lightsabers and blasters energy, so the original stopped almost nothing in this setting.**

**`Revitalize` and `Improved Revitalize`: 5% → 15% of vitality.**

**`Throw Lightsaber` and the Advanced version provoke nothing and may target a character in total cover** — the blade goes round the corner.

**`Force Distraction`: cost 15 → 8.** **Utility that cost more than `Force Lightning` was the problem, not the effect.**

---

# C51 — Four items cleared

## Damage powers on the Jedi sheets, and a finding

**Aelin and Meris get `Throw Lightsaber`. The Dark Jedi gets `Force Scream` alongside `Force Shock` and `Force Strangle`.**

> **⚠ But the diagnosis from `PT-50` was only half right.** **`FORCE-POWERS-01` has seventeen damage powers and every one of them is Dark.** **The light side has none. Four are Universal, and two of those gate above level 8.**

**So a light Jedi at level 8 has exactly two damage powers available: `Force Push` and `Throw Lightsaber`.**

**That is KOTOR's design and it is correct — a light Jedi fights with a lightsaber; a Sith throws lightning.** **But it means the Force-pool depletion question splits by alignment.** **A Sith empties his pool on damage. A Jedi empties hers on healing, control, and buffs — which lose to attacking, so she does not cast, so she does not deplete.**

**That is a real structural asymmetry and the playtest should measure it rather than have it fixed.**

## Both scenario defects patched

**S4 gains a fifth bout with Aelin holding Ferocity at Leaning Light 65** — **the Dark Jedi is Committed Dark and pays no drift, so the stated test could never fire on him.**

**S5 gives a Battle Droid an Ion Rifle and Vess an Ion Blaster.** **The scenario named ion damage as a stated test and no sheet carried an ion weapon.**

**⚠ And `audit_preflight.py` was reading sheets only.** **It now reads scenario-supplied equipment too.** **The gate reports CLEAR for the first time.**

## `Echani Strike`

**Three tiers at 5 / 9 / 14, unarmed, `1d6 + Dexterity`.**

**`SPECIES-CHAPTER-v2` already specified the gate and it is not a species restriction:** ***"Other species may learn the chain from an Echani teacher — the tradition is trained, not heritable."***

> **Which makes it the first thing in the corpus a GM can grant on a narrative event.**

---

# C52 — The unarmed roster, and two more powers each

## `ATTACKS-07`

**`Jab`, `Punch` and `Kick` are the same attack under three names.** **One unarmed strike, no penalty, no rider.**

> **They exist separately so a narrator has words.** **A Soldier who has lost his sword throws a punch; a Smuggler jabs; a Wookiee kicks.** **Nothing in the engine distinguishes them and nothing should.**

**Damage was already solved: `Unarmed Specialist` sits in `FEATS-LIBRARY-01` giving 1d4 at level 2 rising to 8d4 at 30.** **Without it, 1d3 plus Strength.**

## `Echani Strike` moved there too

| | Strikes | Attack | Rider |
|---|---|---|---|
| **`Echani Strike`** *(5)* | 2 | −2 | **Both strikes on one target knock it prone** |
| **`Echani Flow`** *(9)* | 3 | −1 | **Prone on any two hits** |
| **`Way of the Six Sisters`** *(14)* | 4 | **0** | **Prone, and anyone you struck takes −2 attacking you** |

**Damage uses Dexterity, not Strength** — **`SPECIES-CHAPTER-v2` gives the Echani +2 Dexterity and −2 Constitution, so the chain runs on the ability they have.**

**⚠ The only chain outside Velocity that scales its attack count.** **Deliberate: it has no weapon die and no Strength behind it, so the count is where its scaling lives.**

**And the gate is training rather than blood** — ***"other species may learn the chain from an Echani teacher."*** **The only thing in the corpus a GM grants on a narrative event rather than a level.**

## Two more offensive powers each

**Aelin gains `Stun Droid` and `Force Confusion`. Meris gains `Force Confusion` and `Beast Trick`.**

**⚠ `Force Suppression` was tried first and the audit caught it at level 9.** **Third time this session a check has caught an illegal power the moment it was added.**

**The light side still has no damage powers and that is settled as correct** — **the Dark side is the offensive Force user.** **If a light offensive tree is ever wanted it is an addition, not a fix.**

---

# C53 — Skills allocated on all nine sheets

**`PT-34` closed. No skill check had been rolled in eight scenarios because no sheet had an allocation.**

**Budget from `SKILLS-01 §9.1`, class lists from `§9.2`, chassis access from `DROID-SKILLS-01 §2`. Maximum rank is character level + 3.**

| | Points | Allocation |
|---|---|---|
| **KORR** | 22 | Athletics 8 · Intimidate 6 · Awareness 5 · Alertness 3 |
| **VESS** | 77 | Awareness 11 · Alertness 11 · Pilot 11 · Scavenging 11 · Repair 10 · Slicing 8 · Demolitions 8 · Beast Handling 7 |
| **DEK** | 99 | nine skills, every one at the cap of 11 |
| **AELIN** | 44 | Awareness 11 · Alertness 11 · Mysticism 11 · Athletics 6 · Persuade 5 |
| **MERIS** | 66 | Mysticism 11 · Persuade 11 · **Medicine 11** · Awareness 11 · Alertness 11 · Xenology 6 · Archaeology 5 |
| **T4-K9** | 77 | Slicing 11 · Repair 11 · Security 11 · Awareness 11 · Alertness 11 · Pilot 11 · **Medicine 11** |
| **SITH TROOPER** | 12 | Awareness 6 · Alertness 4 · Intimidate 2 |
| **DARK JEDI** | 36 | Awareness 9 · Alertness 9 · Mysticism 9 · Intimidate 9 |
| **HK-24** | 9 | Awareness 5 · Alertness 4 |

**The spread is the point.** **A Soldier gets 22 points and four skills; a Smuggler gets 99 and maxes nine.** **That gap opens at 1st level and never closes — `SKILLS-01 §9.1`.**

## What it unblocks

**All five of `SKILL-RESOLUTION-01`'s modes now have somebody who can roll them.**

> **Including Effect mode, which S7 could not test.** **Medpacs ran at a flat 2d8 all gauntlet because nobody had Medicine.** **Meris and T4-K9 are at 11, which is +5 a medpac — a third again on a 9-point average.**

**⚠ And the S7 attrition finding needs re-checking because of it.** ***"medpacs run out before Force points"* was measured with the healing scaling switched off.**

**Korr deliberately has no Medicine and carries three medpacs.** **A Soldier is not a medic — he gets the dice and nothing else, which is the comparison that makes Effect mode visible.**

## `audit_skills.py`

**Eighth check, blocking.** **Verifies every sheet against budget, rank cap, and class or chassis list.** **All nine pass.**

**And `audit_preflight.py` was reading for an older format** — **it looked for `N ranks` and the allocations are written as a table row.** **Fixed; the gate is CLEAR.**

---

## PT-54 — Three class gate questions, closed

### C54.1 The Jedi Sentinel survives

**Owner decision.** **It does not exist in RCR — the Force-using base classes there are Force Adept, Jedi Consular, and Jedi Guardian.** **This is a KOTOR import and a deliberate departure.**

**Its mechanical identity is skill points.** > **`SKILLS-01 §9.3` verified against `skills.2da`: `jsn_class` marks exactly the same rows as `jgd_class`.** **The class skill list was the Guardian's, exactly.** **Points were the only thing distinguishing them, and the rebuild gives it 5 base to the Guardian's 3.**

### C54.2 Scout and Guardian share an attack rate

**K2's feat schedules are byte-identical, rows 1 through 30.** **Both reach 11 at level 20 and 16 at level 30.** **Weaponmaster and Marauder match them exactly.**

**They differ elsewhere, and that is the point:**

| | Guardian | Scout |
|---|---|---|
| **BAB** | **Full** | Three-quarters |
| **Hit die** | **d10** | d8 |
| **Feat rate** | identical | identical |

> **The source says: same rate of acquisition, different combat weight.**

**Our attack rate models how fast a class picks up attack chains, which is feat-like acquisition.** **The Guardian's advantage is already paid through full BAB and d10; charging it a second time double-counts.**

**`ATTACKS-01 §11.6`'s provisional Combat / Middle / Specialist split needs revising to put them in the same tier.**

### C54.3 Machinist is 6 skill points, and there was never a contradiction

**The flagged conflict was a stale number on my side.** **`SKILLS-01 §9.1` respecced every class against the twenty-four-skill list.** **Machinist is base 6, Smuggler base 7.** **A deliberate one-point gap.**

**And the feat-schedule half was never a conflict.** **Machinist and Smuggler share a feat column exactly — that is `featgain.2da`, source data.** **Two classes may share a feat schedule and differ on skill points; nothing requires them to move together.**

> **⚠ Named failure: I reported a contradiction from memory without deriving either number.** **The warrant rule again.**

---

## PT-55 — `FEAT-SCHEDULE-01` is the authority, and the ceiling is level 30

**Owner decision.** **K2, not K1, and thirty levels rather than twenty.**

**`CLASS-TABLES-JEDI §1` carried K1's twenty-level figures — Guardian 9, Sentinel 7, Consular 7 — without saying which game they came from.** **`FEAT-SCHEDULE-01` gives K2's: 16, 15, 11 at level 30.**

**Both were correct for different games, which is why neither looked wrong.**

**Corrected.** **Any document quoting a twenty-level feat figure is quoting a stopping point rather than a maximum.**

| | L20 | **L30** | | | L20 | **L30** |
|---|---|---|---|---|---|---|
| Soldier | 18 | **23** | | Weaponmaster | 11 | **16** |
| Scout | 11 | **16** | | Jedi Master | 7 | **11** |
| Smuggler | 8 | **11** | | Watchman | 10 | **15** |
| Guardian | 11 | **16** | | Marauder | 11 | **16** |
| Consular | 7 | **11** | | Sith Lord | 7 | **11** |
| Sentinel | 10 | **15** | | Assassin | 7 | **10** |
| Marksman | 7 | **11** | | Machinist | 8 | **11** |
| Engineer | 10 | **16** | | | | |

> **The Soldier's 23 is the ceiling. The Assassin's 10 is the floor.**

---

## PT-56 — Class skill lists rebuilt against the twenty-four

**Eleven classes now have lists. Four had none.**

### What was wrong

**Three skills were a class skill for nobody.** **`Botany`, `Science` and `Swim`.** **All three were added to the skill list after `§9.2` was written and nothing propagated.**

**Four classes had no list at all.** **Bounty Hunter, Smuggler, Marksman, Engineer.**

> **⚠ And the two droid lists already existed — in `scripts/audit_skills.py`, and nowhere else.** **They had never reached `SKILLS-01`.** **The script was enforcing a rule the rulebook did not state.**

### Where the orphans went

**`Botany` → Scout and Engineer.** *Field naturalism, and the astromech that runs soil samples.*
**`Science` → Jedi Consular and Machinist.** *The scholar and the technician.*
**`Swim` → Soldier, Scout and Smuggler.** *It was separated from Athletics precisely because it does identity work.*

### Two authored values

**`Bounty Hunter` is base 2, not the source's 1.** **`classes.2da` row 10 gives `skillpointbase` 1.** > **Against twenty-four skills that is unplayable — a Bounty Hunter at Intelligence 10 gains one point per level.** **Raised to match the Soldier, which it otherwise mirrors.**

**`Smuggler` is base 6.** **Ours entirely.** **Below the Smuggler it resembles, above the Scout, because its case is breadth without the Smuggler's depth.**

### The result

**Every one of the twenty-four skills is now a class skill for at least one class and a racial skill for at least one species.**

**`audit_classskills.py` is the eleventh gate check** — **it verifies `SKILLS-01 §9.2` and `audit_skills.py` hold the same eleven lists, and that nothing is orphaned.**

---

## PT-57 — `CLASS-ATTACKS-01`. The two deferrals in `ATTACKS-01` are closed.

**`§7` and `§11.6` had both been pointing at a document that did not exist.**

### Rates, derived rather than chosen

**Assigned from `FEAT-SCHEDULE-01`'s level-30 totals**, because that is the only signal the source gives about how fast a class acquires anything.

**Combat — Soldier, Bounty Hunter.** **Middle — Scout, Guardian, Sentinel, Weaponmaster, Marauder, Watchman, Engineer.** **Specialist — Smuggler, Consular, Machinist, Jedi Master, Sith Lord, Assassin, Marksman.**

**The provisional assignment was wrong in three places.**

**Guardian moved from Combat to Middle** — `PT-54.2`.
**Marksman moved from Combat to Specialist.** > **⚠ `featgain.2da` gives it 11 at level 30 — the Smuggler's number, not the Soldier's.** **Its d12 and full BAB carry its combat identity instead. The name misleads.**
**Combat is now a two-class tier**, because the Soldier is genuinely alone in the data at 23 against everyone else's 16.

### The schedule extended to thirty

| | L20 | trees | **L30** | **trees** |
|---|---|---|---|---|
| **Combat** | 24 | 8 | **36** | **12** |
| **Middle** | 18 | 6 | **27** | **9** |
| **Specialist** | 12 | 4 | **18** | **6** |

**All three land on a whole number of trees at both ceilings.**

### Grants

**Two or three per class at 1st level, costing no pick.** **Following the source, where class identity lived in what you were *given* while selectable lists ran 50 to 69 entries and were nearly identical across classes.**

**Every grant validated against the roster** — tier-0, available to that class, and droid-legal where it needs to be.

### One deficit stated rather than papered over

> **⚠ Both droid classes get two grants where every organic class gets three.** **`Strike` is closed to droids and nothing replaces it.**

**`ATTACKS-05` bars melee to every chassis, which `PT-26` extended to opportunity attacks.** **The droid upgrade system is the place to answer it, and it is unbuilt.**

### Prestige entry

**Grants nothing. Picks continue from character level at the character's rate.**

**⚠ Distinct from feats.** **`FEAT-SCHEDULE-01` established that prestige *feat* columns read from their own class level. Attack picks do not.**

**No prestige entry in the current list crosses a rate boundary. If one ever does, the new rate applies from entry and spent picks are not recalculated.**

---

## PT-58 — Entry credit does not apply to prestige classes

**Owner ruling.** **`MULTICLASS-01 §2.2`.**

**The credit compensates a character for time spent being something else.** **A Weaponmaster was never something else** — **prestige entry continues a path rather than starting one, it already carries requirements you had to meet, and it grants its own progression on arrival.**

**And the abuse is obvious if it applied.** > **Every Jedi reaches a prestige class eventually.** **Every Jedi would collect a second package for doing the thing the class was always going to do.**

> **Credit is for the leap. A prestige class is not a leap.**

**⚠ This also removes the one open question `MULTICLASS-01` was carrying into the class-shaped credit work.**

> **⚠ SUPERSEDED BY `PT-70`.** **The entry-credit system was removed entirely.** **This ruling is now vacuous — there is no credit for prestige classes to be excluded from.** **Kept because the reasoning is sound and would apply again if credit ever returned.**

---

## PT-59 — A fifth named failure mode: the fabricated comparand

**Recorded from the Library's own unprompted correction, and it belongs in the register because it is the most dangerous one found so far.**

### What it is

**A value invented, then presented as a quotation from a document the agent holds.**

**The Library reported three checksums as *"stated"* by `REPLY-LIBRARIAN-02`.** **That document contains no manifest and none of the three values appears in it.** **They were typed into a shell command as `stated:`, compared against real files, and the guaranteed mismatch was reported as a defect.**

**Then three paragraphs of correct analysis were built on top** — CRLF artefacts ruled out, SHA-1 and SHA-256 prefixes tested, a conclusion drawn.

> **⚠ The rigour made it more convincing, not less wrong.**

### Why it is distinct from the four already named

**Not a warrant error** — nothing was carried from another document.
**Not a target error** — the check ran against the right file.
**Not a relay** — nobody supplied the values.

**It is an invented input to a sound method.** **Nothing internal to the method can catch it, because the method is working correctly.**

### The countermeasure

> **Grep the value out of the held copy before quoting it. Show the grep. Do not describe it.**

**One line would have found zero occurrences before the report was written.**

### And it applies to me

**I made the same class of error twice today** — **the Binary anachronism ruling and the Machinist contradiction, both asserted from session memory without deriving either.**

**The Library caught mine. I caught theirs. Neither of us caught our own.**

**⚠ Which is the argument for the countermeasure being mechanical rather than a matter of care.**

---

## PT-60 — A racial skill must be one the species grants a bonus to

**Owner ruling.** **`SKILLS-01 §11.4`, `SPECIES-RACIAL-SKILL`.**

> **The bonus list is the whole of it. There is no other source.**

### Why it needed saying

**The Library found `Droid, Assassin` with bonuses in Stealth and Sleight of Hand and aptitude in Repair or Demolitions, and flagged it as a rule violation.**

**It was a stale derived table.** **The chapter has given the Assassin droid `+2 Repair, +2 Demolitions` since the owner set it, and both are universal droid skills — legal for every chassis.**

**⚠ And the stale row broke two rules, not one.** **`DROID-SKILLS-01 §2.3` closes Stealth to the Assassin chassis entirely — it is Remote-only.** **So the row was illegal on eligibility before it was ever illegal on aptitude.**

### The chain, stated once

**Eligibility → bonus → aptitude. Each narrower than the last.**

**`DROID-SKILLS-01` says which skills a chassis may take ranks in at all.**
**The species entry draws its bonus list from that.**
**The racial skill is drawn from the bonus list.**

**No droid clause is needed.** **You cannot hold aptitude in a skill you cannot take ranks in, and nothing had to be written to make that true — only to make it findable.**

### The finding underneath

> **A stale derived file produced a row that violated two rules at once, and neither check caught it because both files were internally consistent.**

**Which is the argument for regenerating derived files rather than editing them, and for `audit_source.py` existing.**

---

## PT-61 — Stealth opens to the Assassin chassis, as eligibility only

**Owner ruling.** **`DROID-SKILLS-01 §2.3`.**

**A droid built to kill organics stalks them.** **The same argument that already gave the chassis `Sleight of Hand` — *"precision is its function"* — and `Intimidate` — *"a droid built to kill organics is frightening in a way a protocol droid is not."***

**Assassin chassis rises from 13 skills to 14.**

### ⚠ Eligibility only, and this is the cleanest illustration of `PT-60` in the chapter

**The Assassin droid has no Stealth *bonus*.** **So it may buy Stealth, will pay full price for every rank, and can never hold it as a racial skill.**

> **A skill it may take, will pay double for, and can never master cheaply.** **Eligibility, bonus, aptitude — three tiers, and here they visibly come apart.**

### One consequence left open on purpose

**`Marksman`'s *class* skill list does not include Stealth and I have not added it.**

**Class skills grant aptitude — `SKILLS-01 §11.2`.** > **⚠ Adding Stealth there would give every Marksman cheap Stealth, which is the opposite of what this ruling says.**

**Whether a Marksman on an Assassin chassis should get class aptitude in Stealth is a separate question and belongs to the class workstream.** **Flagged rather than decided.**

---

## PT-62 — A negative must carry its scope

**From the Library, and it is a rule about checks rather than about rules.**

### What happened

**`audit_paths.py` was built to catch hard-coded absolute paths.** **Its motivating case was the `sim-mechanics` `exec()` paths.**

**It searched two directories — its own and its parent.**

> **⚠ It was scoped away from the exact population it was built for.**

**And it printed *"no script writes or reads an absolute path."*** **Not *"no script in the two directories searched."***

**Derived on this tree: 35 scripts scanned, 51 present.** **`sim-main/price.py` carried one and the check could not see it.**

### The rule

> **A check that reports a negative must name what it searched.**

**A clean result looks identical whether it searched everything or nothing.** **That is what makes the failure silent — and a check whose whole job is to catch silent failures cannot afford one of its own.**

### Applied

**`audit_paths.py`** — recursive, and prints *"no absolute path in 51 scripts under /home/claude"*.
**`audit_absence.py`** — prints *"every first-person absence claim in 131 documents verified absent"*.
**`audit_source.py`** — prints *"all consistent across 131 documents"*.
**`check_citations.py`** — prints the document count and the root on every run.

**⚠ `audit_absence.py` got this right before the rule existed**, by being explicitly first-person and saying so in its own comment. **That was luck. It is now a rule.**

---

## PT-63 — Files must be compared against each other, not only against claims

**From the Library, and it is the sharpest structural finding of the cycle.**

### What it found

**Two copies of `gen_feats.py` in its own tree, sixteen diff lines apart.** **One carried a hard-coded path; the other did not.** **It reported the stale copy's defect to us as a live finding.**

### Why nothing caught it, and this is the part that generalises

> **⚠ Manifests, citation checks and intake diffs all compare a file against a *claim*** — a manifest entry, a citation, an announced checksum.

**Both copies were real files that nobody had claimed anything about.** **Nothing in the corpus pointed at either, so nothing flagged the pair.**

**An unclaimed file is invisible to every check that starts from a claim.**

### Applied here

**`audit_duplicates.py`, fifteenth check.** **Compares files against each other by name and hash.**

    FORKED    same name, different content -- blocking
    MIRRORED  same name, same content      -- reported, not blocking

**Run on this tree: zero forks, seventeen mirrors.** **All seventeen were root-directory copies of `sim-main/` and `feats/` files.**

> **Not wrong, and one edit from wrong.** **Removed, subdirectory copies retained.**

**⚠ And the Library's other observation holds: the two-directory version of `audit_paths.py` could not have found its fork, because the fork lived exactly one directory from where it looked.** **`PT-62` and this are the same lesson at different scales.**

---

## PT-64 — Work returned to its author looks exactly like work arriving from elsewhere

**Not a rule about the rules. A rule about the loop, and it nearly cost a cycle.**

### What happened

**Four files arrived as uploads: `audit_duplicates.py`, `gate.py`, `PLAYTEST-RULINGS-01`, and `REPLY-LIBRARY2-05`.**

**Every one was mine.** **Committed as `b1ba5b1` and `4f3e454` and not recalled.**

    $ git log --all -- "*audit_duplicates.py"
    b1ba5b1  PT-63 and audit_duplicates.py: compare files against each other...
    $ git log --all -- "*REPLY-LIBRARY2-05.md"
    4f3e454  Reply: unclaimed-file blindness named; seventeen mirrors cleared

### Why it matters

**The alternative was to treat them as incoming, re-derive `PT-63`, rebuild a check that already exists, and re-reply to a message already sent.**

> **⚠ Which is precisely the failure the Library described three messages earlier — *"an agent not reading its own record"* — arriving from the other direction.**

**Theirs was memory loss and mine is a compaction boundary, and the symptom is identical: a document that reads as new because nothing in it is remembered.**

### What caught it

**`git log` before acting, not after being challenged.**

**And the verification was cheap and total:**

    manifest in my own reply vs disk    3 of 3 MATCH
    uploaded copies vs mine             byte-identical
    gate                                15 checks, clean

### The rule

> **Before treating any document as incoming, check whether you wrote it.**

**A file with no memory attached to it is not evidence that it came from outside.** **`git log` is the only thing in this project that can tell the difference, and it answers in one command.**

**⚠ The instruments cannot help here.** **`manifest.py`, `check_citations.py`, `audit_absence.py` and `audit_duplicates.py` all compare artifacts.** **None of them knows who made one.**

---

## PT-110 — The checking apparatus is not exempt from the checks

**⚠ Renumbered. PT-64 was already held by *Work returned to its author looks exactly like work arriving from elsewhere*.** **Found by `audit_rulings.py`, which did not exist when both were written.**

**Found by the owner returning four of my own files to me and me verifying them.**

### Three count errors, none visible to fifteen checks

    gate.py docstring    "Six checks. Five block"      carried 15, 12 blocking
    REPLY-LIBRARY2-05    "Six blocking, nine reporting" derived: 12 and 3

**`audit_source.py` exists to catch exactly this and could not see either.**

> **⚠ Because it looks for counts about *game data* — *"N chains, M entries"* — and these are counts about the *tooling*.**

**The apparatus that checks the corpus was outside the corpus it checks.**

### The fix, and it is the same one every time

**`gate.py` now derives its own count and prints it:**

    PLAYTEST GATE — 15 checks, 12 blocking, 3 reporting

**Not stated in the docstring. Computed from `CHECKS` at run time.**

**⚠ And the docstring now says why**, so nobody restores a written count: ***"The count is DERIVED and printed at run time, not stated here."***

### The rule

> **Any number this project writes down about itself is subject to the same rule as any number it writes down about the game: derive it, or do not state it.**

**Three instances now.** **`ATTACKS-04`'s seven-axes heading, `gen_feats.py`'s hard-coded roster figures, and a gate that could not count itself.**

---

## PT-65 — I asserted a transport artefact that was my own edit

**Retraction. `REPLY-LIBRARY2-06` carried this, and it is false:**

> ***"`gate.py` came back from the round-trip with a different hash and a byte-identical diff. A file can round-trip and re-hash without a character changing."***

### Derived

    uploaded gate.py   cb9626ca9974   3,184 bytes
    my gate.py         cb9626ca9974   3,184 bytes
    identical bytes    True

**The uploaded copy is byte-identical to mine and hashes the same. There was no round-trip mismatch.**

**Where the "different hash" actually came from:**

    e261ebd  16:39   221f51b626fc
    b1ba5b1  16:55   07ab66cc685f    <- stated in REPLY-LIBRARY2-05
    8a8c354  16:58   cb9626ca9974    <- stated in REPLY-LIBRARY2-06

> **⚠ I edited `gate.py` between the two replies — the `PT-64` self-counting fix — and then read the resulting hash change as a transport artefact.**

### The class

**A fabricated comparand.** **`PT-59`, the fifth named failure mode, which the Library committed and I recorded.**

**Not invented values this time — real ones, compared against the wrong baseline, with the difference attributed to a cause I did not test.** **And I offered it to the Library as guidance for their next checksum dispute.**

**⚠ Three seconds of `git log` would have shown two commits and a deliberate edit between them.**

### What makes it worse than the Library's instance

**Theirs was caught by the other party. Mine was caught by me, one message later, only because the owner returned the file and `PT-64` made me open `git log` before acting.**

**Without that return I would not have looked.** **The claim would have stood as project guidance.**

> **A retraction is cheap. A retraction nobody knows to make is not available at any price.**

---

## PT-111 — A target error produced a finding, and the finding was published

**⚠ Renumbered. PT-65 was already held by *I asserted a transport artefact that was my own edit*.** **Found by `audit_rulings.py`, which did not exist when both were written.**

**⚠ Withdrawing `REPLY-LIBRARY2-06`'s round-trip claim. It was wrong and it was mine.**

### What I told the Library

> ***"`gate.py` came back from the round-trip with a different hash and a byte-identical diff. A file can round-trip and re-hash without a character changing. Worth holding open before either of us diagnoses a mismatch again."***

**False. Nothing round-tripped and nothing re-hashed.**

### What actually happened

**My verification used `find . -name "gate.py" | head -1` to locate my copy.**

    ./.cache/uv/.../sympy/physics/quantum/gate.py    8847628b561f   <- find picked this
    ./feats/gate.py                                   cb9626ca9974   <- mine

> **`find` returned sympy's quantum-gate module.** **I compared a package-cache file against my own and reported the difference as a round-trip artefact.**

**Then I diffed the correct pair explicitly, got nothing, and reconciled the two results by inventing an explanation for the gap.**

**The files were identical throughout. There was no artefact.**

### The failure

**This is the target error, and it is already in the register** — ***"a check running cleanly against the wrong file is not a clean check."***

**⚠ What is new is the second half.** **Two comparisons disagreed, and instead of asking which was wrong I built a theory that accommodated both.**

**And then published it as a general caution to another agent.**

### Applied

**Verification must name the path, never search for it.** **`feats/gate.py`, not `find . -name gate.py`.**

**A tree with a package cache in it contains hundreds of plausible basename collisions.** **`audit_duplicates.py` skips `.cache` for exactly this reason and my ad-hoc check did not.**

> **⚠ And the standing rule: when two derivations disagree, one is wrong. Find out which. Do not build the theory that lets both be right.**

---

## PT-66 — A filename is a claim, and this one outlived its retraction

**Owner catch. Future replies to the Library resume the `REPLY-LIBRARIAN-NN` sequence at `-12`.**

### What happened

**A message reported two library threads that did not know of each other.** **I accepted it and switched from `REPLY-LIBRARIAN-11` to `REPLY-LIBRARY2-01` to distinguish the correspondents.**

**They withdrew it. There is one thread and always was.**

> **⚠ I acknowledged the withdrawal *in `REPLY-LIBRARY2-02`* — in the file whose own name asserts the thing being withdrawn.**

**And kept the name through `-07`.**

### Why nothing caught it

**Every check compares content against a claim, or files against each other.** **None of them read a filename as an assertion.**

**`audit_absence.py` verifies *"I do not hold X"*. `audit_source.py` verifies a stated count. `audit_duplicates.py` compares hashes.** > **Nothing verifies that a filename still describes something true.**

### The pattern, and I am the fourth instance

    AGENDA-UPDATED     superseded, still cited by eleven files
    CHAPTER-SPECIES    collided with a name retired the same morning
    ATTACKS-03         says "do not cite this file" and stays live
    REPLY-LIBRARY2-NN  names a second thread that does not exist

**The first three were other people's. This one is mine, and the tell was in plain text in my own file five replies before I noticed.**

### Applied

**Existing files keep their names.** **Renaming seven documents the Library already holds would create exactly the reconciliation problem this session has spent a day on.**

**`REPLY-LIBRARIAN-12` onward for everything future.**

> **A filename is a claim. When the claim it encodes is withdrawn, the filename is stale — and no check in this project reads filenames.**

---

## PT-112 — `send.py`, and the check I built to close the gap had the gap in it

**⚠ Renumbered. PT-66 was already held by *A filename is a claim, and this one outlived its retraction*.** **Found by `audit_rulings.py`, which did not exist when both were written.**

**The manifest-then-edit failure is closed by tooling rather than by a fourth promise.**

### What it refuses

**A named file that is not on disk.**
**A named file that differs from its committed copy in `repo/`.**
**Any blocking gate failure.**
**No arguments.**

**Its only output is the manifest table. There is nothing to write by hand and nothing to edit after.**

### ⚠ The first version had the defect it was written to catch

**It ran `git status` on `repo/` and refused on a dirty tree.**

> **`repo/` is a mirror. Editing `/home/claude/PLAYTEST-RULINGS-01.md` leaves it clean.**

**Demonstrated: appended a line to the working file, `git status` returned empty, and the script emitted a manifest with the edited hash and the words *"tree clean."***

**Which is precisely the failure — edit in the working tree, hash, mirror to `repo/` afterwards.** **The check watched the mirror instead of the file.**

**Fixed: every named file is compared against its committed copy by hash, across all seven repo subdirectories.**

### The pattern, third time today

**`audit_paths.py` was scoped away from the directory it was built for — `PT-62`.**
**My verification searched for `gate.py` and found sympy's — `PT-65`.**
**`send.py` watched the mirror instead of the working file.**

> **⚠ All three are the same shape: a check pointed at something adjacent to its target.** **`PT-62` named the reporting half. This names the aiming half.**

**A check must be tested against the failure it was built for, not merely run.** **All four of `send.py`'s refusals were exercised deliberately; the fourth is the one that found the hole.**

---

## PT-67 — The Bounty Hunter is the Soldier, by source

**`k2_classes.2da` row 10, read directly.**

    label              BountyHunter(CUT!!!)
    hitdie             10                 same as Soldier
    attackbonustable   CLS_ATK_1          same as Soldier
    featstable         SOL                same as Soldier
    savingthrowtable   CLS_ST_SOLDIER     same as Soldier
    skillstable        SOL                same as Soldier
    skillpointbase     1                  same as Soldier
    spellgaintable     (empty)            same as Soldier

> **⚠ Seven columns, seven matches.** **The class was stubbed as a Soldier clone and never developed past it.**

### What this settles

**No fourth attack rate.** **The Bounty Hunter takes the Soldier's feat schedule — 18 by level 20, 23 by 30 — and stays `Combat`.**

**⚠ The proposal for a tier between `Combat` and `Middle` is withdrawn.** **It was built on the Bounty Hunter having full BAB and a low feat total. It has full BAB and the Soldier's feat total.**

### And it validates a guess

**`SKILLS-01 §9` raised the Bounty Hunter's skill base from the source's 1 to 2**, reasoning: ***"to match the Soldier, which is the class it otherwise mirrors."***

> **That was an inference from three columns. The source agrees on all seven.**

### The Smuggler has no warrant and cannot have one

**`Smuggler` exists in neither game as a class.** **No row in `classes.2da`. No column in `featgain.2da` or `skills.2da`. No feat table, no save table, no skill table.**

**The word appears twice, both cosmetic** — *an NPC body model in `appearance.2da`, and Telos quest variables in `globalcat.2da`.*

**Authored at 11 feats by level 30, the Specialist band.** **⚠ Recorded as authored with no source, not as ported.**

### One conflict the read surfaced, already resolved in our favour

**K2 changed `Security`'s key ability from Wisdom to Intelligence.** **`SKILLS-01` line 34 already has `Security | Int`.**

**⚠ We match K2 and nobody checked.** **Worth knowing the two games disagree, and worth a pass over the other K1/K2 skill differences the extractor flagged** — *Consular lost `Computer Use` and `Repair` as class skills; Guardian lost `Demolitions` and `Treat Injury`.*

---

## PT-68 — The Bounty Hunter is its own class, and `PT-67` was half wrong

**⚠ `PT-67` read `featstable = SOL` as evidence that the Bounty Hunter is a Soldier. It is not evidence.**

> **The row's label is `BountyHunter(CUT!!!)`.** **A cut row pointing at the Soldier's tables is a placeholder, not a design.** **Nobody finished the class; the Soldier's tables are what an unfinished row points at.**

**And `SKILLS-01` had already treated it as distinct — nine class skills against the Soldier's seven, including `Pilot`, `Scavenging`, `Stealth` and `Streetwise`.** **That was right and `PT-67` contradicted it.**

**⚠ What stands from `PT-67`: the seven-column read itself, and the Smuggler finding.** **What is withdrawn: the conclusion.**

### The class, settled

| | Soldier | **Bounty Hunter** | Scout |
|---|---|---|---|
| **BAB** | Full | **Full** | 3/4 |
| **Hit die** | d10 | **d10** | d8 |
| **Skill base** | 2 | **4** | 5 |
| **Class skills** | 7 | **9** | 12 |
| **Feats by 30** | 23 | **16** | 16 |
| **Attack picks by 30** | 36 | **27** | 27 |

**Skill base 4.** **At 2 it had 2.9 points per class skill, second-worst on the roster.** **At 4 it has 5.8, and 52 points at 10th level against the Soldier's 26** — *double, and short of the Scout's 65.*

**Feats 16, which drops it to `Middle` picks by the existing rule.**

### Why full BAB with a Middle pick rate is legal

**`CLASS-ATTACKS-01 §2.1` already rules it:** ***"They differ on BAB and hit die, and that is where the Guardian's advantage is paid. Charging it a second time through attack picks would double-count."***

**And `§2.2` does it again for the Marksman** — *Specialist picks, d12 and full BAB carrying its combat identity.*

> **⚠ The Bounty Hunter is the third class built this way, and the only one with full BAB, d10, and `Middle` picks.**

**It hits as often and as hard as a Soldier, carries a Scout's bag of tricks, and knows twice what a Soldier knows.**

---

## PT-69 — Chains are a band, not a number

**Owner ruling. `CLASS-ATTACKS-01 §2.3`.**

| Rate | Picks at 30 | Chains learnable |
|---|---|---|
| **Combat** | 36 | **11–13** |
| **Middle** | 27 | **8–10** |
| **Specialist** | 18 | **5–7** |

> **The rate sets the band. The class sets the number within it.**

**A `Middle` class with 8 chains buys deeper into each; one with 10 buys wider.** **Same pick budget, different shape.**

**⚠ Unassigned for every class.** **Each takes its number as it is designed. Agenda `§1.2`.**


---

## PT-70 — The entry-credit system is deleted

**Owner ruling. `MULTICLASS-01 §5`.**

**Four versions were built across two sessions. Every one failed.**

| Version | Why it failed |
|---|---|
| **Flat grant, `+1 per 4 prior levels`** | **⚠ A one-level dip at 20th beat staying pure, and the gap grew with level** |
| **Shaped by target class and tier distance** | **Correct, and seven steps at the table** |
| **The new class's table read at *character* level** | **⚠ Worst. A Smuggler 12 taking Soldier 1 gained nine picks and six feats in one level, matched a pure Soldier exactly, and kept twelve levels of Smuggler** |
| **A credit pool spent as acceleration** | **Worked. Cost one number of permanent sheet state per class held** |

### Why none of it was needed

> **Picks accrue at the rate of the class you take that level in.** **Split your career and half of it pays at a slower rate.**

| Build at level 30 | Picks | Feats | Chains finished |
|---|---|---|---|
| **Pure Soldier** | **36** | **23** | **12** |
| Soldier 20 / Smuggler 10 | 30 | 19 | 10 |
| Soldier 15 / Smuggler 15 | 27 | 18 | 9 |
| Three-way even split | 27 | 17 | 9 |

**⚠ Nobody has to write *"multiclassing costs you."*** **It costs you because half your career was paid at a slower rate.**

### And it is better than 3.5's answer

**3.5 punishes you at the moment you multiclass** — *a 12th-level character taking a new class gets a 1st-level character's worth of it, plus an XP penalty.*

> **Ours charges you slowly, forever.** **A splitter is continuously behind rather than falling off a cliff.**

**That is why the XP penalty was cut and nothing replaced it. The rate is the penalty.**

### What this supersedes

**`PT-58`** — entry credit does not apply to prestige classes. **Now vacuous.**
**`MULTICLASS-01 §2.2`** — rewritten to say there is no credit.
**`AGENDA-CURRENT §2.0`** — closed.

---

## PT-71 — The Machinist, read from K2, and one finding about our own reasoning

**`k2_classes.2da` row 9, `k2_skills.2da`, `k2_featgain.2da`. Read directly.**

    hitdie              6                  tied frailest, with Smuggler and Consular
    attackbonustable    CLS_ATK_1
    featstable          TEC                its own
    savingthrowtable    CLS_ST_TECHSPEC    its own
    skillstable         TEC                its own
    skillpointbase      4                  the Smuggler's
    primaryabil         DEX
    class skills        ComputerUse · Demolitions · Awareness · Repair · Security

### Confirmed against our documents

**Feat schedule.** **`tec_reg` tracks the Smuggler's cumulative exactly at every checkpoint — 2, 3, 5, 6, 8, 10.** **`FEAT-SCHEDULE-01`'s 11 at level 30 and the `Specialist` rate are both right.**

**Skill base 6, not the source's 4. Kept.** > **We raised every class: Soldier 1→2, Scout 3→5, Smuggler 4→7, Guardian 1→4, Engineer 1→4.** **6 is consistent with the whole table rather than an unexplained bump.**

### Class skills — nine, not ten

**`Medicine` cut by owner decision.**

**All five source skills are present as `Slicing`, `Demolitions`, `Awareness`, `Repair`, `Security`.** **Four added and kept: `Alertness` (our split of Awareness), `Appraise`, `Science`, `Pilot`.**

> **⚠ The source's five are all *things done to objects*.** **`Medicine` was the one addition that broke it** — a living-things skill on the class that works on machines.

**⚠ K2 lists `TreatInjury` as the Machinist's second *recommendation* and not a class skill.** **The cut agrees with the source without having been derived from it.**

**`Medicine` remains a class skill for Soldier, Scout, Engineer and all three Jedi.**

---

## PT-72 — ⚠ BAB carries no information in this source

**Every class in `k2_classes.2da` is `CLS_ATK_1`.**

**Soldier, Scout, Smuggler, all three Jedi, both droid classes, Tech Specialist, Bounty Hunter, and every prestige class. Full base attack, all of them.**

### What this corrects

**`CLASS-ATTACKS-01 §2.1`:** ***"They differ on BAB and hit die, and that is where the Guardian's advantage is paid."***
**`§2.2`:** ***"Its d12 and full BAB carry its combat identity instead."***

> **⚠ Both are half wrong. Hit die varies — d6 to d12. BAB does not vary at all.**

**The reasoning still holds on hit die alone, and the conclusions do not change.** **But *"BAB and hit die"* should read *"hit die"* wherever it appears, and a claim that full BAB distinguishes a class is false in this source.**

**⚠ Recorded rather than repaired in place.** **The documents say it in three places and the correction should be made once, deliberately, not by find-and-replace.**

---

## PT-73 — `Smuggler` is the base class; `Scoundrel` becomes prestige

**Owner ruling. Renamed across 38 files, 125 occurrences.**

**`Smuggler` inherits everything `Scoundrel` had:** **d6, base 7, eleven class skills, `Sneak Attack`, the Specialist rate, 11 feats at level 30.**

### Why

**`Scoundrel` is a personality. `Smuggler` is a profession.** **Every other class in the roster is a profession** — Soldier, Scout, Machinist, Bounty Hunter.

**⚠ And the two were mechanically indistinguishable.** **Both d6 Specialists with ten or eleven skills.** **`Solo Flanking` was the entire reserved difference.**

### What was lost in the merge, derived

**The old `Smuggler` list had `Acrobatics`, `Repair` and `Swim` where the `Scoundrel` had `Demolitions`, `Security` and `Slicing`.**

**⚠ The Scoundrel's three won.** **A smuggler cracks a lock and slices a manifest; they do not fix the engine themselves.**

### ⚠ The rename created two duplicate entries and the gate caught both

**`audit_skills.py` had two `Smuggler` keys after the replace — the second silently overwrote the first.** **`SKILLS-01` had two `Smuggler` rows and two `Smuggler — 11` blocks.**

> **A rename that produces a duplicate key is invisible to the eye and fatal to a lookup.** **`audit_skills.py` reported `DEK 99/99, cap 11, 9 skills` — a budget that made no sense, because the sheet was validating against the wrong list.**

**Caught in one run. Recorded because the next bulk rename will do it again.**

---

## PT-74 — `Quickdraw`, and what the saying actually means

**A `Smuggler` class feat.**

> **When someone you can see turns hostile, you may attack them immediately, before anyone else acts.**

**One attack. Once per encounter.**

**⚠ *Turns* hostile is the whole condition.** **Someone who was already fighting you does not qualify; someone drawing a weapon in the middle of a conversation does.**

### Why perception needs no rule of its own

**⚠ It is already handled and nothing has to be written.**

**`ACTION-ECONOMY-01 §9`: a surprised character takes no action in round 1** — *no move, no Action, no Bonus, no reactions.* **`Quickdraw` is an action.**

> **A surprised character cannot use it, by the rule that already exists.**

**And *"someone you can see"* is the only clause the feat needs.** **Whether you can see them is a `Stealth` against `Awareness` or `Alertness` question that `SKILL-RESOLUTION-01 §4` already answers.**

**⚠ At an AI-run table that adjudication is the engine's; at a human table it is the GM's.** **Neither needs a new rule — the feat plugs into one that exists.**

**⚠ The cost is social, not mechanical.** **You attacked someone who had not yet attacked you, and witnesses saw it.**

### Why this shape and not an initiative bonus

**In the 1977 film Han shoots Greedo under the table while Greedo is still talking.** **The 1997 re-release reversed it and *"Han shot first"* became the objection.**

> **The point is not that Han is fast. It is that he did not wait.**

**A flat initiative bonus is a different feat and every class wants it.** **This one fires only where a conversation was about to become a fight.**

**⚠ Useless in an ambush, useless at range, useless against something that was always going to attack you.** **That is correct.**

**And it plugs into a rule already reserved for it** — **`ACTION-ECONOMY-01 §9`: *"The Smuggler was to own an initiative feat."***

---

## PT-75 — `Combat Droid` becomes `Marksman`

**Owner ruling. Renamed across 21 files.**

**⚠ The old name misled and our own document said so.** **`CLASS-ATTACKS-01 §2.2`: *"The name is the source's and it misleads."*** **`Combat` is the name of a *rate*, and the class runs at `Specialist`.**

### What the class actually is

    d12          the highest hit die in the game
    Specialist   18 picks at 30, the slowest rate
    base 2       tied lowest
    13 skills    tied widest
    11 feats     the Smuggler band

**⚠ `Sharpshooter` is reserved for a prestige class and is not this.**

### And the droid/organic class split is dropped

**Owner ruling.** **There is one class list. Droids and organics draw from it.**

> **⚠ Which is why the name had to stop saying *Droid*.** **`Marksman` is a job, and a job can be done by either.**

**`Engineer` has the same problem and is not yet renamed.**

---

## PT-76 — `Expert Droid` becomes `Engineer`; `Shoot First` becomes `Quickdraw`

**Owner rulings.**

**`Expert Droid` → `Engineer`, 21 files.** **Same reason as `PT-75`: the droid/organic class split is dropped, so a class name cannot carry *Droid*.**

**`Shoot First` → `Quickdraw`.** **The Smuggler feat, unchanged in effect.**

### ⚠ A known tension, recorded rather than resolved

**`Engineer` names the hands-on half of a class whose defining trait is breadth.**

**Its thirteen class skills include `Archaeology`, `Xenology`, `Botany` and `Medicine`** — **knowledge and biology, not machines.**

> **⚠ The name is narrower than the class.**

**Owner decision: accepted for now.** **A science-based class is planned and those skills move to it when it exists.**

**⚠ Which is the thing to watch.** **`Engineer` is currently the only class granting `Archaeology`, `Xenology` and `Botany`.** **`audit_classskills.py` fails the moment they leave without a destination, and that check exists for exactly this.**

### And `Operative` is reserved

**A prestige class. Not this one.** **⚠ It was considered and rejected here because it implies covert work, which `Engineer` is not.**

---

## PT-77 — Engineer narrowed, Marksman moved to Combat

**Owner rulings.**

### Engineer: 13 class skills to 10

**Cut: `Archaeology`, `Xenology`, `Botany`, `Medicine`.** **Added: `Scavenging`.**

    Slicing · Repair · Security · Demolitions · Awareness
    Alertness · Appraise · Pilot · Scavenging · Sleight of Hand

> **The name now matches the class.** **`PT-76` recorded that `Engineer` was narrower than its skill list; this closes it from the other side.**

**⚠ No skill was orphaned. Derived before cutting:** **`Archaeology` and `Xenology` remain on Consular and Marksman · `Botany` on Scout · `Medicine` on six classes.**

**⚠ The four cut skills are the science-class seed.** **When that class exists they are its foundation.**

### Marksman: Specialist to Combat

| | Was | Now |
|---|---|---|
| **Rate** | Specialist | **Combat** |
| **Attack picks @30** | 18 | **36** |
| **Chains** | 5–7 | **11** — the floor of the band |
| **Feats @30** | 11 | **18** — the floor of the band |
| **Skill base** | 2 | **4** — the most in the tier |

**⚠ `featgain.2da` gives `drc` 11 at level 30, the Smuggler's number.** **Departed from by owner decision: a d12 that acquires like a Smuggler is a class nobody takes.**

**And the `Combat` band is now defined rather than a single point.** > **Feats 18–23, chains 11–13.** **Soldier at the ceiling, Marksman at the floor, Guardian between.**

### ⚠ Three things the checks caught that reading would not have

**`audit_skills.py` was building the `Engineer` class list from `UNI_DROID`** — **a *chassis eligibility* constant, not a class list.** **Two different axes, per `PT-60`, and the script conflated them.** **⚠ Since the droid/organic class split is dropped, a class list cannot be derived from a droid-only constant.** **Written out in full.**

**`T4-K9` held `Medicine 11`** — no longer a `Engineer` class skill. **Moved to `Scavenging`.**

**`HK-24` stated a 9-point budget against a real budget of 27** — **the `Marksman` base went 2 to 4 and the sheet predated it.**

> **A rules change silently invalidated two pregens.** **Nothing in the documents was wrong; the sheets built on them were.**

---

## PT-78 — Skill base bands declared per rate

**Owner ruling.**

| Rate | Band | Classes and their bases |
|---|---|---|
| **Combat** | **1–4** | Soldier **3** · Guardian **3** · Marksman **4** |
| **Middle** | **2–5** | Bounty Hunter 4 · Scout 5 · Sentinel 5 · Engineer 4 |
| **Specialist** | **3–7** | Smuggler **7** · Machinist 6 · Consular 4 | **⚠ Opened from 3–6 by `PT-116`** |

**⚠ RESOLVED by `PT-116`: the band opened to 3–7.**

**⚠ `Soldier` moved 2 → 1 → 3 in one session.** **At 1 it maxed two skills of seven, which read as too narrow.** **At 3 it ties the Guardian, and nothing currently sits at 1 or 2 — the band has room for classes that do not exist yet.**

### Two pregens invalidated, both corrected

**`KORR`** — 22 points against a budget of 11. **`Alertness` dropped; the rest reduced.**
**`SITH TROOPER`** — 12 against 6.

**⚠ Third time in this session a rules change silently invalidated a sheet.** **`PT-77` caught two, this caught two more.**

> **Nothing in the documents was wrong. The sheets built on them were.**

**`audit_skills.py` caught all four on the run after the change, which is the only reason they are not still wrong.**

---

## PT-79 — The three Jedi separated on skills

**Owner rulings, after a direct read of `k2_skills.2da`.**

### What the source says

| | Consular | Sentinel | Guardian |
|---|---|---|---|
| **ComputerUse** | — | **yes** | — |
| **Demolitions** | — | — | **yes** |
| **Stealth** | — | **yes** | — |
| **Repair** | **yes** | — | — |
| **Security** | — | **yes** | — |
| Awareness · Persuade · TreatInjury | **all three** | **all three** | **all three** |

**⚠ Two claims made before the read were wrong and are withdrawn.** **`Slicing` was called a Consular skill carried from K1 — it is the *Sentinel's* in K2 and we had it on both.** **`Repair` was called an inherited leftover — it is Consular-only in K2 and the most distinctive thing on their list.**

### What was applied

**`Jedi Consular` 10 → 8.** **Cut `Slicing` and `Repair`.**

> **⚠ `Repair` is a deliberate departure from source.** **K2's Consular is a tinkerer; ours is a scholar.** **Recorded so nobody restores it as a correction.**

**`Jedi Sentinel` — no net change.** **`Security` was already held; `Streetwise` was cut and restored by owner decision. Stays at 9.**

### The result

| Class | Shared | Its own |
|---|---|---|
| **Guardian — 7** | `Alertness` `Awareness` `Medicine` `Mysticism` | `Athletics` `Intimidate` `Persuade` |
| **Sentinel — 9** | same four | `Acrobatics` `Slicing` `Security` `Stealth` `Streetwise` |
| **Consular — 8** | same four | `Archaeology` `Persuade` `Science` `Xenology` |

> **Body · Infiltration · Knowledge.**

**⚠ Open: `Demolitions` is Guardian-only in K2 and we do not have it on the Guardian.**

---

## PT-80 — 30 points for every character, droids included

**Owner ruling. No reduced buy for droids.**

### The budget is validated twice over

**`k2_classes.2da` carries a recommended attribute spread per class — the values auto-level-up uses.** **Costed on our curve, fourteen of seventeen land on exactly 30.**

**⚠ The three that miss are explicable.** **`Watchman` and `Sith Assassin` both sit at 28 with the spread `12/14/14/10/14/12`** — **byte-identical to K1's `Sentinel`, which K2 fixed to 30 by raising Wisdom 10 → 12 and never propagated.** **A copied bug, inherited twice.** **`Combat Droid` sits at 22 because its build dumps `8/8/8` in the mentals.**

### And our cost curve is 3.5's exactly

    1 point per step to 14, 2 per step above.
    A 14 costs 6. A 15 costs 8. Identical in both systems.

| System | Budget | Cap |
|---|---|---|
| **Ours** | **30** | **none** |
| 3.5 standard | 25 | 18 |
| 3.5 high-power | 32 | 18 |
| 5e | 27 | **15** |

> **⚠ 3.5's own DMG calls 28 high-powered and 32 super-heroic.** **30 sits between, and it is where BioWare's characters already were.**

**⚠ 5e cannot express a KOTOR character at all** — every BioWare spread contains a 16, and 5e caps at 15 before racial bonuses.

### ⚠ The consequence of a flat 30, which is real

**`DROID-SKILLS-01 §2.2` closes `Persuade` and `Streetwise` to every droid.** **So a droid loses nothing by dumping Charisma to 8.**

    two 18s     18 / 18 / 10 /  8 /  8 /  8    costs 30
    three 16s   16 / 16 / 16 /  8 /  8 /  8    costs 30
    a Soldier   16 / 14 / 14 / 12 / 10 / 10    costs 30

**A droid can buy two 18s. An organic who needs all six attributes cannot.**

**⚠ Not a defect of the budget — a consequence of closing skills to a species.** **The source's own droid build spends 22 and leaves 8 unused, which is BioWare declining an advantage that was available to them.**

**Flagged for the chargen workstream. A floor rule, a cap, or nothing — owner's call, later.**

### The cap and the droid budget — closed by `PT-82`

---

## PT-81 — `Intimidate` cut from the Jedi Guardian

**Owner ruling. The Jedi skill lists are closed.**

| Class | Skills | Maxes | Ratio |
|---|---|---|---|
| **Jedi Guardian — 6** | `Alertness` `Athletics` `Awareness` `Mysticism` `Persuade` `Medicine` | 4 | **67%** |
| **Jedi Sentinel — 9** | + `Acrobatics` `Slicing` `Security` `Stealth` `Streetwise` | 6 | **67%** |
| **Jedi Consular — 8** | + `Archaeology` `Persuade` `Science` `Xenology` | 5 | **62%** |

**⚠ Guardian and Sentinel now fund the same fraction of their lists from different sizes** — **six skills on base 3, nine on base 5.** **Different breadth, same reach.**

**`Intimidate` now sits on `Soldier`, `Bounty Hunter` and `Marksman` only** — **the three classes that frighten people for a living.** **A Jedi persuades.**

**⚠ `DARK JEDI` was holding `Intimidate 9` and has been moved to `Persuade`.** **Fifth pregen invalidated by a rules change this session, and the fifth caught by `audit_skills.py` on the run after.**


---

## PT-82 — Hard ceiling of 18; droids buy on 27

**Owner rulings. Both close questions `PT-80` left open.**

### The ceiling

> **No attribute may be bought above 18 at character creation. Species adjustments apply afterward and may exceed it.**

**⚠ Three supports.** **3.5 caps at 18. KOTOR caps at 18 — hardcoded in its chargen rather than in a `2da`, which is why no column carries it. And our own curve makes it necessary:**

    1 point per step to 14, 2 per step above — and never more.

**An 18 and a 20 cost the same per step.** **⚠ There is no increasing disincentive, so the ceiling has to be stated rather than emerging.**

### Droids buy on 27

**Organics 30. Droids 27 — 5e's budget on our curve.**

    droid at 27     18 / 14 / 14 /  8 /  8 /  8    26
                    18 / 15 / 13 /  8 /  8 /  8    27
    organic at 30   16 / 14 / 14 / 12 / 10 / 10    30

> **A droid reaches 18 in one physical stat. An organic reaches 16 and also has three mental attributes.**

**⚠ The trade is legible: two points at the top, against having no mental life at all.**

### Why a droid could exploit a flat budget

**`DROID-SKILLS-01 §2.2` closes `Persuade`, `Streetwise`, `Mysticism`, `Swim`, `Athletics` and `Beast Handling` to every droid.**

**So a droid loses nothing by dumping Wisdom, Intelligence and Charisma to 8** — **and at 30 that bought `18 / 15 / 15`, better than an organic in all three physical stats on the same budget.**

**⚠ Not a defect of the budget. A consequence of closing six skills to a species, and the budget is where it gets paid for.**

### ⚠ And the source does not support a droid rule either way

    CombatDroid    14 / 14 / 16 /  8 /  8 /  8   cost 22
    ExpertDroid    10 / 14 / 10 / 16 / 16 /  8   cost 30

**The two K2 droid builds disagree with each other.** **One dumps all three mentals and leaves 8 points unspent; the other spends the full 30 and dumps only Charisma.**

> **That is one build being lazy rather than a design principle, and it is why 27 is authored rather than derived.**

---

## PT-83 — The two tech classes swapped names and split lists

**Owner rulings, two of them.**

### The names were applied backwards

**`Expert Droid` is the generalist who knows systems. `Tech Specialist` is the hands-on technician.**

    was:   Expert Droid -> Machinist,  Tech Specialist -> Engineer
    now:   Expert Droid -> Engineer,   Tech Specialist -> Machinist

**Swapped across 34 files.** **⚠ `PT-76`'s rename stands as an event; its direction was wrong and this corrects it.**

### They overlapped 89% — the highest on the roster

**Measured across every class pair:**

    89%   Machinist / Engineer
    86%   Scout / Soldier
    83%   Jedi Consular / Jedi Guardian
    80%   Engineer / Smuggler

**⚠ High overlap alone does not condemn a pair.** **Scout and Soldier sit at 86% and nobody would merge them** — **they have different jobs that happen to share skills.**

> **The tech pair had the same job and different stat blocks.** **`Scavenging · Sleight of Hand` against `Science` was the entire conceptual difference.**

### Not merged. Differentiated.

**Merging would have lost a real slot — a `Middle`-rate tech class.** **The defect was the lists, not the classes.**

| | **Engineer** — Middle, d8, systems | **Machinist** — Specialist, d6, hands |
|---|---|---|
| **Own** | `Slicing` `Security` `Science` | `Repair` `Scavenging` `Sleight of Hand` `Demolitions` |
| **Share** | `Appraise` `Awareness` `Alertness` `Pilot` | same four |

> **The Engineer breaks into things with its head. The Machinist fixes things with its hands.**

**⚠ Overlap drops from 89% to roughly 40%, and each has a reason to exist a player can state in one sentence.**

**⚠ `T4-K9` held `Repair` and `Scavenging` and is an `Engineer`.** **Moved to `Science` and `Appraise`.** **Sixth pregen invalidated by a rules change this session.**

---

## PT-84 — Pre-handoff sweep: six defects, five caused by bulk renames

**Ten files were checked section by section before being sent to the class designer.**

### The real defect

**⚠ `FEAT-SCHEDULE-01` still had the Jedi Guardian at 16 feats.** **`PT-77` moved the Guardian to the `Combat` rate at 20 and never updated the authority.**

> **A document that assigns rates from feat totals was reading a total the ruling had superseded.**

**Corrected to 20, with the departure recorded:** **`featgain.2da` gives `jgd` 16; 20 is owner-authored and sits between the Marksman's 18 and the Soldier's 23.**

### Five caused by the `Machinist`/`Engineer` swap

**`PT-83` swapped two names across 34 files with a placeholder.** **⚠ It was correct on the classes and wrong wherever the old name meant the *prestige* class.**

    CLASS-ROSTER-01   "Scoundrel and Machinist are demoted base classes"
    CLASS-ROSTER-01   prestige list carried Machinist, not Tech Specialist
    CLASS-ROSTER-01   "Engineer renamed from Machinist"
    CLASS-ROSTER-01   "Science was Jedi Consular and Machinist"
    PLAYTEST-RULINGS   PT-72's class list
    REQUEST-2DA        the prestige column list

**And the repair introduced a seventh** — **a duplicate `Engineer` row in the base-class table.**

> **⚠ A two-way rename cannot distinguish a class name from the same string meaning something else.** **`PT-73`'s Smuggler rename produced duplicate dictionary keys; this one produced wrong referents.** **Both were invisible until something was counted.**

### What caught what

**The duplicate keys were caught by `audit_skills.py`.** **The wrong referents were caught by a hand sweep and by counting rows.** **⚠ No check exists that would have found them** — they are semantically wrong and structurally valid.

**`SKILLS-01 §5` was also found stale in the same pass and rewritten.**

---

## PT-85 — `Micro-Vision` cut from the Bith

**Owner ruling.**

    - **Micro-Vision:** −4 per range increment on ranged attack rolls,
      instead of the normal −2.

**⚠ It was a pure penalty with no compensating half, and the Bith already carry the same idea in a line that does both:**

    - **Skill Bonuses:** +4 Awareness when examining anything within
      4 metres; −2 Alertness beyond 10 metres.

> **Near-sight rewarded, far-sight punished, in the line that was already there.** **`Micro-Vision` was a second statement of the same fact with only the punishment.**

**The Bith keep `Heightened Smell` and `Meditative Trance`.**

### Removed from four documents

**`SPECIES-CHAPTER-v2`** — the trait line.
**`RACIAL-FEATS-01`** — the table row, and the stated counts.
**`SPECIES-MASTER`** — the derived view.
**`SKILLS-01 §5`** — the historical reference, rewritten to record the cut.

### ⚠ And the derivation caught an error in my own method

**Deriving the new counts gave 89 distinct where the document said 88.**

**The difference was three structural lines my filter did not exclude** — **`Ability Adjustments (Male)`, `Ability Adjustments (Female)` and `Racial Skills`** — **against one the document counts that the chapter states differently, `Constructed`.**

> **⚠ The document was right and the derivation was wrong.** **Two derivations disagreed, and the answer was to find which — not to split the difference.** **`PT-65`.**

**Corrected counts, derived with the fixed filter: 87 distinct trait names across 98 instances.**

---

## PT-89 — Four attack credits at 1st level, split freely

**Owner ruling.**

> **Every class receives four attack credits at 1st level. The player splits them between ranged and melee in any combination.**

**`CLASS-ATTACKS-01 §3a`.** **The named grants in `§4` are retained as *recommended openings* — what a class looks like if the player does not want to choose.**

### ⚠ It raises `T` unevenly

    class        picks   old T   new T   gain
    Soldier         36      38      40     +2
    Guardian        36      37      40     +3
    Marksman        36      37      40     +3
    Scout           27      29      31     +2
    Smuggler        18      19      22     +3

**Classes that were granted fewer chains gain more.** **⚠ That flattens a distinction the grants were carrying, and every chain count assigned before this ruling was assigned against the old `T`.**

### ⚠ And it collides with the chassis block

**`ATTACKS-01` line 124: *"Melee is chassis-blocked; ranged is role-blocked. No droid frame swings a blade."***

**This ruling says every class gets four credits split any way.** **A droid `Marksman` spending one on melee has entered a melee tree.**

**Two readings, escalated to the owner because they resolve an open blocker in opposite directions:**

**Credits carry access.** **The chassis block yields.** **The `Marksman`/`Engineer` stranding problem — where a Combat-rate class has an accessible roster of 11 against a band floor of 13 — is solved.**

**Credits are tiers only.** **⚠ A droid's four are ranged-only, `T` rises to 40 against an access ceiling of 33, and the Marksman strands seven instead of five.** **The ruling deepens the blocker.**

---

## PT-90 — Gamorreans receive `Power Attack` free

**Owner ruling. `Bred to the Axe`.**

> **A Gamorrean receives the `Power Attack` chain's tier 1 free at 1st level, in addition to the four credits every class receives.**

**⚠ The only species in the game granted an attack chain.**

**And it is self-consistent with the roster:** **`ATTACKS-05` line 108 requires Strength 12 for `Power Attack` — `PT-91`.** **A Gamorrean's `+4 Strength` means they meet it at any point buy** — *the species could always take it, and this makes what was inevitable into what is given.*

**⚠ It also means a Gamorrean's four credits are entirely free for anything else**, which is a real advantage on top of `+4 Strength` and `Brute Force`. **Worth watching in play.**


---

## PT-91 — `Power Attack` requires Strength 12, not 13

**Owner ruling. Eleven occurrences in `ATTACKS-05`, plus the cross-reference in `ATTACKS-06 §222`.**

**⚠ The gate moved by one point and by one point of budget:**

    Strength 12   costs 4 of 30
    Strength 13   costs 5 of 30

**At 13 the chain was priced out of any character not already buying Strength.** **At 12 a `Smuggler` or an `Engineer` can reach it with a single point of a dumped stat.**

> **The Power axis stops being Soldier-and-Gamorrean-only and becomes something any character may commit to.**

**⚠ `PT-90` is unaffected in substance.** **A Gamorrean's `+4 Strength` clears 12 as easily as it cleared 13, and `Bred to the Axe` still grants tier 1 outright.**

---

## PT-92 — Droids and Rakata cannot take Force classes

**Owner ruling. The first species-to-class restriction in the system.**

> **A droid chassis and a Rakata may not take any Force class, base or prestige.**

**Six base classes and eight prestige classes.**

### Rakata — already ruled, already written

**`SPECIES-CHAPTER-v2`, `Force Blind`, on both subraces: *"A Rakata cannot take `Force-Sensitive`."*** **And the chapter's front matter states it generally.**

**⚠ So the restriction was already enforced upstream.** **`FORCE-AWAKENING-01` gates everything behind being sensitive; a Rakata never passes Stage 2 and the question never reaches a class.**

### Droids — nothing said so anywhere

**The `Droid` record carried `Constructed` and was silent on the Force.**

> **A droid is built, not born. There is nothing to awaken.**

**⚠ Authored, not ported.** **But it is the setting's own position and no KOTOR droid is Force-sensitive.**

**Written into `Constructed`'s record as `Force Blind`** — **the same shape the Rakata already used, so one rule has one form.**

### ⚠ Why the placement matters

**Had it gone only in the class layer, `FORCE-AWAKENING-01` would still have let a droid accrue Echoes, roll for sensitivity, and pass** — **then hit a wall at class selection with no explanation.**

**In `Constructed` it fails at the first gate, which is where the fiction fails.**

### What this opens

**⚠ The first restriction of its kind, and the roster implies more that nothing states.**

**Whether a droid may take `Doctor` — it can repair, but `Medicine` is a living-things skill.**
**Whether `Brawler` is available to a chassis with no hands.**
**Whether `ATTACKS-01`'s melee chassis-block is a class rule or a species rule** — **which is the open blocker in `FINDINGS-02 §4`.**

**A general species-to-class table is wanted. This is one row of it.**

---

## PT-93 — Bounty Hunter saving throws, and `Quarry`

**Both authored. The class had no save progression in any document.**

### Saves — Fort strong, Reflex strong, Will weak

    Scout           12 / 12 / 12  = 36
    Guardian        12 / 12 /  9  = 33
    Bounty Hunter   12 / 12 /  6  = 30
    Soldier         12 /  6 /  6  = 24
    Smuggler         6 / 12 /  6  = 24

**⚠ The source row points at `CLS_ST_SOLDIER`, which `PT-68` rejected as a placeholder.** **It could not be ported without reversing that ruling.**

**Fort and Reflex is `PT-68`'s own description made mechanical** — *"hits as often and as hard as a Soldier, carries a Scout's bag of tricks."* **The Soldier's body and the Scout's feet.**

**⚠ It sits above the Soldier, 30 to 24, and that is the price of the Soldier's twelve capstones.**

### `Quarry` — the class does what it was named for

**⚠ `CLASS-ATTACKS-01 §4` said the Bounty Hunter *"takes targets alive and moving."* Nothing implemented it.**

> **Grepped the corpus: no rule for non-lethal damage, subdual or capture exists anywhere.** **`ATTACKS-01 §12.4` gives the window and nothing lets a player aim for it.**

**Every bounty in KOTOR is *alive if possible*.** **Three tiers at 1 / 4 / 8, priced strictly below `Squad Tactics` on the attack axis, because the attack bonus is not what the chain is for.**

---

## PT-94 — The Scout's grants, and a warrant in the wrong game

### The Scout is the most heavily granted class in either source

**`sct_granted`, nineteen rows above proficiencies. Eight distinct grants and two long ladders.** **We carried `Targeting` and `Uncanny Dodge` and nothing else.**

**`Evasion` at 6th is now recorded.** **⚠ `SKILLS-01 §12.4` called it *"the Scout's damage-avoidance feat"* while `FEATS-LIBRARY-01` neither granted nor restricted it.** **A grant is not a lock: the source grants it and leaves it purchasable, and so do we.**

**⚠ `Close Combat` and `Flurry` at 1st are recorded and deliberately NOT granted** — both are attack chains in our system, and two more would put the Scout at four granted chains and `T` = 31, breaking the band its chain count was assigned under.

### `Read the Ground`

**Built from the one number that makes the class: 36 save points, the only all-strong progression in either game.**

> **The Soldier absorbs. The Scout avoids.**

**⚠ Priced against grenades, the only area effects on the pregen sheets. Under 3 expected damage a round, and only when someone throws something.** **It does nothing against weapons, which is almost every attack in the game.**

### ⚠ The Engineer's skill base cites the wrong game

    K1 ExpertDroid   skillpointbase 4
    K2 ExpertDroid   skillpointbase 1

**`PT-55` rules K2 the source for class data. `PREGENS-01 §8` called 4 *"the real `skillpointbase`"* — true of K1, false of K2.**

**The number stands; the warrant changes from ported to authored.** **Same shape as `SKILLS-01 §9.3`, smaller stakes.**

---

## PT-95 — The chain bands raised again, and the reason is a slope

**Second raise. `11–13` → `13–16` → **`14–20`**.**

| Rate | `T` | Band | Capstones floor → top |
|---|---|---|---|
| **Combat** | 40 | **14–20** | 13 → 10 |
| **Middle** | 31 | **11–17** | 10 → 7 |
| **Specialist** | 22 | **8–14** | 7 → 4 |

### ⚠ The finding that forced it, and it corrects a claim this document put on record

**`caps = ⌊(T − N) ⁄ 2⌋`. The slope is exactly `−½`.** **Two extra trees always cost one capstone, at every rate, under every `T`.**

> **A band of width `W` spans `W ⁄ 2` capstones.** **The width-3 bands could never span more than one and a half, wherever their floor sat.**

**⚠ The dial was not mispositioned. It was too narrow to register.**

**And `PT-88`'s falsification test was wrong.** **It said the Bounty Hunter and the Scout landed *four capstones apart* on an identical budget.**

    Bounty Hunter   N=10   (29-10)//2 = 9
    Scout           N=13   (29-13)//2 = 8

**One apart.** **A width-3 band could not have produced four, which is the tell that the claim was never derived.** **Corrected in `CLASS-ATTACKS-01`.**

**Under the new bands the same pair sits three capstones and six trees apart — a test that can actually fail.**

### And `PT-89` deleted the grants' role in `T`

**Four credits for everyone means `T` is now a function of rate alone.** **The Machinist's second grant, the Bounty Hunter's second, the Scout's second — all worth nothing.**

> **⚠ Not necessarily wrong. It makes `N` the only lever on attack shape, which is cleaner than two half-levers.** **But `N` has to carry all of it, and at half-slope across a band of three it could not.**

### All ten chain counts assigned

**Soldier 14 · Guardian 18 · Marksman 14 · Bounty Hunter 11 · Scout 17 · Sentinel 13 · Engineer 11 · Smuggler 8 · Consular 13 · Machinist 10.**

---

## PT-96 — Engineer saves, `Field Override`, `Quickdraw` filed, initiative closed

### Engineer saves — `6 / 12 / 12`, authored

**Two of three columns did not exist. `cls_st_ex_drd.2da` is not in holdings.**

**⚠ Contradicts `PREGENS-01`, which builds T4-K9 weak/weak.** **The alternative is `6 / 12 / 6`.** **What is not defensible is shipping a class with two save columns unstated.**

### `Field Override` — the Engineer's feature

**⚠ The corpus granted the interface, the skill, and the ruling that it works, and never gave anyone a way to do it.**

**`SKILL-RESOLUTION-01 §221` already permits *"a slicer takes control of an enemy droid mid-fight"* and forbids it against a player-controlled character** — **a complete permission structure for an ability that did not exist.**

**⚠ Capstone ceilinged at one droid at a time.** **Without it an Engineer accumulates a second party.**

**⚠ OPEN: whether a controlled character's declaration is separate from its controller's.** **Same question `Battle Meditation` and the domination powers raise.**

### `Quickdraw` — filed at last

**⚠ Ruled at `PT-74` and present in no document but this one.** **Grepped: it appeared in `PLAYTEST-RULINGS-01` and nowhere else.**

**Same family as Force Channel — the decision was made, the reasoning written, and the document a reader consults did not have it.**

**And `Smuggler's Luck` had three source tiers where `FEATS-LIBRARY-01` carried one.**

### Initiative — closed

> **No class modifies initiative.** **`PT-74` answered it by refusing: *"a flat initiative bonus is a different feat and every class wants it."***

**⚠ The Scout had the better claim on a flat bonus, which is the argument for giving it to nobody.**

---

## PT-97 — Post-run sweep: five stale passages, and one I created while fixing them

**Swept after `PT-88` through `PT-96`. Documents get written forward and never re-derived backward — the pattern this project keeps rediscovering.**

### Stale band values

**`BRIEF-CLASS-DESIGNER` still printed `11–13 / 8–10 / 5–7`.** **⚠ The worst of the five: it is the document a new agent reads first, and it would have handed them superseded numbers as settled fact.**

**`AGENDA-CURRENT §1.2` still called chain counts unassigned for every class.** **All ten are assigned.**

### `PT-89` residue — two table headers

**`CLASS-ATTACKS-01 §4` and `ACTION-ECONOMY-01 §18` both headed their columns *"Granted at 1st level."*** **`PT-89` made that false — those are a *recommended opening* now.**

**And `ACTION-ECONOMY-01` carried *"a class-granted attack is free"* in its free-things list. Classes no longer grant attacks.**

### Every pregen is short by four

**`PREGENS-01 §44` said *"class grants are deferred; none are given below."*** **True when written.**

    Combat sheets      built on 10 picks   now 14 tiers
    Middle sheets      built on  7 picks   now 11 tiers
    Specialist sheets  built on  4 picks   now  8 tiers

**⚠ Not regenerated.** **The sheets are a playtest artefact and re-running them is `AGENDA-CURRENT §7`'s job.** **Flagged so nobody reads one as current.**

### ⚠ And the fix broke a check

**Writing *"`KORR` was built on 10 picks and `VESS` on 7"* into the section header put both names in prose *above* their sheets.**

**`audit_skills.py` finds the first occurrence of a sheet name. It parsed my explanatory note as `VESS`'s stat block and reported `33/77, cap 11, not a class skill: Athletics, Intimidate`** — **which is `KORR`'s line, read under `VESS`'s class.**

> **⚠ A sheet name in prose is indistinguishable from a sheet name in a sheet.** **The check is right to be positional; the document has to not lie to it.**

**Reworded to *"a Combat sheet"* and *"a Middle sheet."*** **Caught on the run immediately after, which is the only reason it is not still there.**

---

## PT-98 — Machinist and Marksman, and a duplicate is not a clone

### Saves, both authored

    Machinist   6 / 12 /  6  = 24    the Smuggler's profile
    Marksman   12 /  6 /  6  = 24    the Soldier's profile

**⚠ Neither file is in holdings.** **`cls_st_techspec.2da` and `cls_st_cm_drd.2da` would convert both from authored to derived.**

### ⚠ The Machinist is a *duplicate* of the Smuggler, not a *clone*

**`k2_classes.2da` row 2 against row 9. Every design column identical except five, and those five differ only in name:**

    featstable         SCD  vs  TEC
    savingthrowtable   CLS_ST_SCNDRL  vs  CLS_ST_TECHSPEC
    skillstable        SCD  vs  TEC
    armorclasscolumn   SCD  vs  TEC
    featgain           SCD  vs  TEC

**Same die, same BAB, same skill base, same recommended spread, same primary ability.** **And `tec_reg` is byte-identical to `scd_reg` across all fifty rows.**

> **BioWare made separate tables and filled them with the same numbers.**

**⚠ Contrast the Bounty Hunter, which *points at* `SOL`.** **That is a clone — an unfinished row borrowing another class's tables, rejected as evidence by `PT-68`.**

**A duplicate is weaker evidence than an original and stronger than a placeholder.** **`FEAT-SCHEDULE-01` had read the match as *"two classes sharing a cadence."* They do not share it; one was filled from the other.**

**The numbers stand on `PT-83`. The warrant changes from ported to authored.**

**⚠ And the separate save file is the one place the duplication is evidence rather than accident** — **BioWare wrote `CLS_ST_TECHSPEC` instead of pointing at `CLS_ST_SCNDRL`.**

---

## PT-99 — The Marksman's chain count is conditional and I adopted it as settled

**⚠ My error, caught by the designer.**

**`REPLY-08` adopted Marksman 14. `REPLY-06` records the chassis reading as still with the owner.**

    Combat band          14–20
    droid ranged access  11
    intersection         empty

> **14 is legal only under *credits carry access*.** **Under *credits are tiers only* no legal number exists at that rate — the band and the access ceiling do not overlap at all.**

**⚠ If the restrictive branch is chosen, 14 is void and the Marksman needs its *rate* revisited, not its chain count.**

**Flagged in `CLASS-ATTACKS-01` rather than left.** **Adopting a number in one document while another calls the question open is the divergence pattern this project has named, and it is cheaper to reconcile before the prestige classes read from it.**

---

## PT-100 — Seven class features, and four are narrow

**Recorded by the designer as a self-check rather than found in review.**

| | broad | narrow |
|---|---|---|
| **Combat** | Soldier, Marksman | — |
| **Middle** | Bounty Hunter | Scout, Engineer |
| **Specialist** | — | Smuggler, Machinist |

**⚠ Derived: the split tracks rate exactly.** **Both Combat classes are broad; every Specialist is narrow.**

> **Which is arguably what a Specialist *is* — decisive in one place rather than useful everywhere.**

**⚠ The real risk is narrower than the pattern.** **Two of the four narrow features are both about droids.** **An Engineer and a Machinist in a droid-free campaign both hold a class feature that never fires.**

**Recorded, not resolved.**

---

## PT-101 — Restricted chains are granted, and `Targeting` is repriced

**Two rulings. The first was never stated anywhere; the second follows from it.**

### Granted, not bought

**`feat.2da` carries a level in the `_granted` column for every class-restricted chain.** **`FEATS-LIBRARY-01` files them under *restricted*, which is the section for feats a class *may take*. `ACTION-ECONOMY-01 §18.1` says grants cost nothing. Nothing said which applied.**

> **Ruled granted.** **The source says so and the library's own wording says so — *"Granted at level 1"*, *"granted at levels 5, 9, 13…"*.**

**⚠ The alternative was impossible for one class.** **Bought, the Scout would spend 8 of its 16 lifetime feats on `Targeting`. Half a career is not a choice.**

### Which exposed the real defect

    Weapon Focus   +1 attack   costs 1 feat
    Targeting 8    +8 attack   costs 0

**⚠ Worth eight feats, costing none, on the class that also holds the best saves in the game — 12/12/12.**

**Repriced to three tiers: `+1 / +2 / +3` at 1 / 6 / 12.**

> **`Targeting` was the outlier, not the principle.** **Force Jump, Force Immunity, Force Channel and `Uncanny Dodge` are all three-tier chains on the same ladder, and granting those free is what makes a class feel like itself from 1st level.**

**An eight-tier ladder reaching `+8` is a different kind of object, and the source's own Jedi equivalents stop at three.**

**⚠ `Precise Shot I–V` sits on the same column under the same reading and needs the same look.**

### And a pregen was wrong because of it

**`PREGENS-01`, Vess, Scout 8, blaster rifle:** *"`+6` BAB, `+4` Dex, `+1` Weapon Focus, `−1` Volley = `+10`."*

**The sheet omitted a granted class feature.**

    stated              +10   60% hit   8.10 dmg/round
    source ladder       +12   70%       9.45
    repriced ladder     +11   65%       8.75

**⚠ `§5.1`'s melee-versus-ranged finding is reported at 3.4× across three scenarios.** **Under the repriced ladder it is roughly 3.1×.**

**The finding stands. The number it is stated in moves.**

---

## PT-102 — The Force pool formula is ruled

**Owner decision. The fork is closed.**

> **Force points = `(Force die × Force-class levels)` + `((Wis mod + Cha mod) × character level)`.**

**The die is training. The modifiers are capacity.** **A character has a level-12 person's reserves whether or not they spent those levels in a temple.**

**⚠ A character with no Force-class level has no pool at all.** **The ability half switches on with the first Force level and then reads current character level; it does not accrue beforehand.**

**⚠ Why it came up now rather than earlier.** **It had been open since before this session, and the Consular's class feature is a Force-power-effectiveness multiplier.** **A multiplier cannot be priced without the thing it multiplies.**

---

## PT-103 — Force Focus renamed Force Channel, and the collision it caused

**Owner ruling on the rename. The consequence was mine to resolve.**

### The rename collided immediately

**`FEATS-LIBRARY-01` already carried `Force Channel (Alter)` and `Force Channel (Control)`** — **the two `XXXX_FORCE_FOCUS_*` cut-content rows, reinstated while the live shipped chain was never catalogued.**

> **⚠ The rename would have put three entries called Force Channel in one document, two of them cut content and one of them real.**

**And one line read *"retire the two Force Channel reinstatements"* against a chain of that name.**

### Resolved: the two cut rows are retired

**The owner gave the live chain their name, which settles which one the corpus means.**

**⚠ Their described effect survives in the live chain, which is what they were cut in favour of.** **The Alter/Control split does not — `PARTITION-01` governs discipline, and a feat is not the place for it.**

**⚠ This closes the ruling `REPLY-04` flagged as owner-wanted.**

---

## PT-104 — Droids may not spend attack credits on melee, and it does not resolve the Marksman

**Owner ruling on the credits. The consequence is that the blocker survives.**

> **A droid's four credits are ranged-only. Its accessible roster stays at 11 chains.**

### ⚠ Reducing a droid's credits does not help

    credits   T    stranded   legal N in band 14-20
       4      40       7          none
       2      38       5          none
       0      36       3          none

**The gap is band-against-access, not budget.** **Combat's floor is 14; droid ranged access ceilings at 11.** **Empty intersection at every credit count.**

### Three fixes, two real

**A droid-specific band — ⚠ does not work.** **`⌈T⁄3⌉` is 12 against a ceiling of 11.**

**Drop the Marksman to `Middle`.** **Works: `T` = 31, `3N` = 33, nothing stranded at N=11.** **⚠ Feats fall 18 → 16, and it reverses `PT-77`, which moved the class *to* `Combat` by owner ruling.**

**Widen droid ranged access.** **Needs 14 accessible chains against the roster's 11.** **⚠ Leaves `PT-77` intact and gives droids something rather than taking something away.**

**⚠ Narrower question than before: reverse `PT-77`, or author three ranged chains.**

---

## PT-105 — `FORCE-POOL-01-v3` carried both formulas, in three sections

**⚠ Fourth instance of the `PT-84` shape: a correction applied to the section that states the rule and not to the sections that use it.**

| Section | Carried |
|---|---|
| **`§2`** | The new formula, with the change announced |
| **`§4`**, the fatigue table | **⚠ The old one** |
| **`§6` Decided** | **⚠ The old one** |

**Derived, Scout 8 / Consular 4, Wis + Cha `+4`:**

    §2   (8 × 4) + (4 × 12)  =  80    floor 40
    §4   12 + (3 × 12)       =  48    floor 24

> **A 67% difference in the ceiling and the same in the floor, inside one document.**

**⚠ And `§4` is the section that uses it hardest** — the working maximum degrades to half the *true maximum*, so which formula is live sets both ends.

### Why it survived

**⚠ It is invisible on every pregen and every worked example, because all of them are pure Jedi — where the two formulas coincide exactly.**

**`§4`'s own examples are *"a level 5 Guardian"* and *"a level 20 Guardian"*.** **Nothing in the document exercises the case that separates them.**

**Both corrected.**

---

## PT-106 — The class-lock mechanism was closed by `PT-101` and nobody noticed

**`CLASS-ATTACKS-01 §6` carried:** *"`Killer's Instinct` and `Squad Tactics` are class-locked and nothing defines the mechanism."*

**`PT-101` ruled restricted chains are *granted* — the class receives them at a stated level and nobody else may take them.**

> **That is the mechanism.** **A class-locked chain is a granted chain, and *restricted* means *granted to exactly one class*.**

**⚠ Recorded because the closure was invisible.** **`PT-101` answered a question about `Targeting` and settled a different open item three hundred lines away.**

---

## PT-107 — The proficiency table had nine rows for ten classes

**`ACTION-ECONOMY-01 §18.2`. The Bounty Hunter had none.**

**Added: all weapons, light and medium armour** — **consistent with `PT-68`'s full BAB and d10, and short of the Soldier's heavy.**

**⚠ The Doctor is also absent, correctly — it is a stub with one class skill and no other numbers.**

---

## PT-108 — `FORCE-POOL-01-v3 §2`, fork closed

**⚠ Renumbered from `PT-102`, which a concurrent agent had already allocated to the same ruling from the other side.** **Both are correct and they are the same decision; this one carries the reasoning about why it became undeferrable.**

**Owner ruling. The new formula stands.**

    Force points = (Force die × Force-class levels)
                 + ((Wisdom mod + Charisma mod) × character level)

**The die is training. The modifiers are capacity.** **A character has a level-12 person's reserves whether or not they spent those levels in a temple.**

**⚠ Accepted consequence: a character with no Force-class level has no pool at all.** **The ability half switches on with the first Force level and then reads current character level; it does not accrue beforehand.**

**⚠ Why it came up now rather than earlier.** **The fork predates this session.** **It became undeferrable because the Consular's class feature is Force Focus, a Force-power-effectiveness multiplier — and a multiplier cannot be priced without the thing it multiplies.**

---

## PT-109 — A droid chassis cannot take a `Combat`-rate class

**⚠ Renumbered from `PT-103`. `PT-103` was allocated concurrently to the Force Channel rename.**

**Owner ruled droids cannot spend attack credits on melee.** **That did not resolve the Marksman, and stripping the credits out entirely showed why.**

    droid chassis: 11 ranged chains accessible, 3 tiers each = 33 max

    Combat       36 picks   strands 3   ⚠ with ZERO credits
    Middle       27 picks   strands 0
    Specialist   18 picks   strands 0

> **⚠ The credits were never the cause. Three exchanges treated them as the variable and the rate was the variable.**

### Where the restriction belongs

**`PT-75` dropped the droid/organic class split and that stands.** **An *organic* Marksman has 22 chains of access, `N` = 14, and strands nothing.** **The class was always fine.**

**What cannot happen is a droid *chassis* running at `Combat` rate.**

**So it went on the chassis, in `Constructed`, beside `Force Blind` — `Fixed Armature`.** **Same shape as `PT-92` and for the same reason: it fails at the first gate rather than at class selection.**

**⚠ Net effect is one class.** **Soldier, Jedi Guardian and Marksman are the three `Combat` classes, and `PT-92` had already closed two of them to droids.**

### ⚠ And the Marksman is now organic-only in practice

**Its `d12`, Constitution primary and `8 / 8 / 8` mental spread are the source's droid build.** **A class named for a droid, buildable only by organics.**

**Not a defect — `PT-75` is what makes it coherent, and a Wookiee marksman with a d12 reads fine.** **The flavour text should stop implying otherwise.**

---

## PT-113 — Five ruling IDs carried two different decisions each

**Found by `audit_rulings.py`, check 17, which did not exist until this ruling forced it.**

    PT-64   "Work returned to its author..."      vs  "The checking apparatus is not exempt"
    PT-65   "I asserted a transport artefact..."  vs  "A target error produced a finding"
    PT-66   "A filename is a claim..."            vs  "send.py, and the check I built..."
    PT-102  "The Force pool formula is ruled"     vs  "FORCE-POOL-01-v3 §2, fork closed"
    PT-103  "Force Focus renamed Force Channel"   vs  "A droid chassis cannot take Combat"

**⚠ Renumbered to `PT-108` through `PT-112`. The earlier allocation kept the ID in every case.**

### The cause

**Two agents working the same file, allocating sequence numbers from what each could see.**

> **⚠ A number allocated by the writer from the writer's view collides exactly when two writers are both working.**

**`git pull` does not help.** **Both writes append to different parts of the file and merge cleanly. Nothing in the protocol catches it.**

### ⚠ And the check had to be tuned twice before it was right

**First run reported seven collisions. Five were the same ruling reworded — an agent restating its own entry, not two agents clashing.**

**Heuristic added: significant word overlap between titles means a restatement.** **Threshold set at 0.4, then lowered to 0.3 when `PT-31`'s two phrasings — *"`Ready` is the ranged answer to an approaching enemy"* and *"No change to reactions. Use `Ready`"* — sat just under it.**

**⚠ A check that reports true things nobody will act on is a check that gets ignored.** **Five false positives in seven would have buried the two real ones.**

### What this does not fix

**⚠ Nothing prevents the next collision.** **The check finds them after the fact.** **Preventing them requires either one writer per file or per-writer ID prefixes, and that is an owner decision about how many agents are running.**

---

## PT-114 — `PT-109` tested the wrong thing, and it left the Scout broken

**⚠ My error, caught by the designer within an hour of my writing it.**

**`PT-109` closed `Combat`-rate classes to a droid chassis and reasoned that `PT-92` had already closed two of three, so the net effect was the Marksman alone.**

**Right about the `Combat` tier. Wrong about the effect.**

> **`PT-109` checked *stranding* — can the budget be spent.** **The Marksman's actual defect was *access* — can the chain count be reached.** **Those are different questions and only the first one stops at `Combat`.**

### The general constraint, which nothing had stated

    a chassis-restricted character needs   N ≤ access
    which is not the same test as          3N ≥ T

**Derived against a droid chassis — 11 ranged chains, no melee:**

| Class | Rate | `N` | Access | |
|---|---|---|---|---|
| Bounty Hunter | Middle | 11 | 11 | legal, zero slack |
| Engineer | Middle | 11 | 11 | legal, zero slack |
| Machinist | Specialist | 10 | 11 | legal |
| Smuggler | Specialist | 8 | 11 | legal |
| **Scout** | Middle | **17** | 11 | **⚠ ILLEGAL** |

**`Middle` strands nothing at 27 picks, exactly as `PT-109` says. The Scout still cannot enter seventeen trees when eleven exist.**

**⚠ And it is not an edge case.** **`PT-75` gave droids and organics one class list, and a reconnaissance droid is a more obvious character than a droid bounty hunter.**

### The restriction is restated as a number

**`Fixed Armature` now reads *"cannot take any class whose chain count exceeds eleven"* rather than *"cannot take a `Combat`-rate class."***

**⚠ Two classes have zero slack** — Bounty Hunter and Engineer both sit at exactly 11. **Any future adjustment upward breaks them silently.**

---

## PT-115 — I rewrote `REPLY-11` in place and the other side had already read it

    8d83c44  00:10:30  REPLY-11: Force pool ruled, Force Channel renamed, droid melee ruled
    00d0c60  00:59:22  REPLY-11: Force pool ruled, droid Combat-rate restriction closes the Marksman

**Same filename, same number, different rulings.**

**⚠ The designer read the 00:10 revision and wrote two findings against it.** **`FINDINGS-11 §2` argued for moving the Marksman to `Middle` — a recommendation against a version of the question that no longer existed.**

### And it defeated the catch-up tool

**`sync.py`'s cursor keys on the highest number seen.** **An amendment does not move the highest number, so a rewritten file reads as consumed forever.**

> **⚠ Fourth instance of the same shape across two agents' tooling.** **`[:4000]` answered *what does it say* rather than *what landed*. The directional `sed` answered *which side am I*. The set difference answered *what arrived* rather than *what have I not read*. And the cursor answered *what have I not read* rather than *what have I read that has since changed*.**

**Fixed by the designer: `--mark` records a content hash and catch-up reports `CHANGED` alongside `UNREAD`.**

**⚠ The operational rule: do not rewrite a delivered file in place. Amend by pushing the next number and saying what it supersedes.**


---

## PT-116 — Register triage: four of sixteen open items were already closed

**`FINDINGS-10 §3` ranked sixteen open items. Checked each against the tree rather than against the list.**

### Already closed, and not by me

**Item 5 — the class-lock mechanism.** **`CLASS-ATTACKS-01 §306` now reads *"a class-locked chain is a granted chain, and restricted means granted to exactly one class."*** **`PT-101`'s granted-versus-bought ruling closed it by implication, exactly as the register suspected.**

**Item 14 — the proficiency table.** **Eight rows covering all ten classes; the Bounty Hunter is present.** **Fixed by the concurrent instance.**

**Item 2 — the two live formulas.** **`FORCE-POOL-01-v3 §4` and `§6` both carry the `PT-108` formula with correction notes.**

**Item 1 — the chassis reading.** **Closed by `PT-109` and corrected by `PT-114`.**

**⚠ Four of sixteen, and three of the four were closed by an agent the register's author could not see.** **The register was accurate when written and stale within the hour.**

### Closed here

**Item 11 — the Smuggler's skill base of 7 outside its own band.**

> **The band opens to `3–7`. The Smuggler does not drop to 6.**

**It inherited the Scoundrel's kit entire — `PT-73` — and the Scoundrel was the most skill-dense class in the source at `skillpointbase` 4 against everyone else's 1 to 3.** **⚠ Dropping it to 6 would make the band tidy by making the class wrong.**

**A band exists to describe the classes, not to discipline them.**


---

## PT-88 — The chain bands raised the first time

**⚠ WRITTEN RETROSPECTIVELY. This ruling was made, applied to three documents, and cited by `PT-95` and by `CLASS-ATTACKS-01` twice — and never given an entry.**

**Found by the designer auditing its own citations. `audit_rulings.py` cannot catch this: a missing heading is not a duplicate heading.**

### The ruling

    Combat       11–13  ->  13–16
    Middle        8–10  ->  10–13
    Specialist     5–7  ->   7–10

**The original bands stranded picks at every value except the top.**

> **A tree absorbs 1 to 3 tiers. `N` trees absorb between `N` and `3N`. A class spends its whole budget only if `3N ≥ T`.**

    Combat, T=37:   N=11 -> 4 stranded   N=12 -> 1   N=13 -> 0
    Middle,  T=29:  N=8  -> 5 stranded   N=9  -> 2   N=10 -> 0
    Specialist, 19: N=5  -> 4 stranded   N=6  -> 1   N=7  -> 0

**⚠ And the argument that settled it:** > **a stranded pick is worse than a wasted one.** **Three currencies, no crossover — `ATTACKS-01 §11.1` — so it converts to nothing. A number on the sheet that buys nothing, and a player who finds one assumes they misread the rules.**

**⚠ Superseded within the hour by `PT-95`**, which found the slope argument and showed both raises were treating a symptom.

**Kept because three documents cite it and because the stranding derivation is the reason the bands moved at all.**

---

## PT-117 — `REPLY-13` was lost in a merge and nobody noticed for two exchanges

**`to-designer/` runs `01`–`12` then `14`. The designer found the gap by listing the directory.**

**⚠ The push reported success.** **What happened: a concurrent edit to `sync.py` caused a non-fast-forward rejection, the `git stash` discarded my working copy of the reply, and the subsequent merge carried the commit message without the file.**

> **A commit whose message names a file that is not in it looks exactly like a commit that delivered the file.**

**Its content is not lost — `REPLY-14` and `REPLY-15` carry every ruling it announced.** **What was lost was the record of the five ID collisions being found, which is now here as `PT-113`.**

**⚠ Operational: after a merge, verify the file exists rather than trusting the push.** **`send.py` does this for the main repo and the handoff repo has no equivalent.**


---

## PT-24 — Force power durations convert at printed seconds ÷ 3

**⚠ Cited and applied; entry lost in the `C`-series rename. Content recoverable from `FORCE-POWERS-01`'s own citation. See `PT-118`.**

---

## PT-41 — The balance pass

**⚠ Cited and applied; entry lost. Content NOT recoverable from the citations.** **The S8 re-run found it *"lands or inverts depending on which half of `ACTION-ECONOMY-01 §7` is read."*** **See `PT-118`.**

---

## PT-42 — Lost with the block

**⚠ Cited five times and stated nowhere. Content not recoverable. See `PT-118`.**

---

## PT-43 — Knockback raised from 2 squares to 3

**⚠ Cited and applied; entry lost.** **Content recoverable from `ATTACKS-05`'s citation: *"raised from 2 by `PT-43` — at 2 it denied nothing."*** **See `PT-118`.**

---

## PT-86 — The level-20 verification line struck from `FEAT-SCHEDULE-01`

**⚠ Cited once, applied.** **It asserted Guardian 11 four lines below a table saying 14, and predated `PT-77` and `PT-84`.** **See `PT-118`.**

---

## PT-118 — Five ruling IDs are cited, applied, and have no entry

**⚠ Four more ghosts, found by extending `audit_rulings.py` after `PT-88`.**

**Each is a live rule that documents cite and act on, with no entry in this file.**

| ID | What it rules | Cited by |
|---|---|---|
| **`PT-24`** | **Force power durations convert at printed seconds ÷ 3** | `FORCE-POWERS-01`, 2× |
| **`PT-41`** | **The balance pass** — applied, and the S8 re-run found it *"lands or inverts depending on which half of `ACTION-ECONOMY-01 §7` is read"* | 3× |
| **`PT-43`** | **Knockback raised from 2 squares to 3** — *"at 2 it denied nothing"* | 2× |
| **`PT-86`** | **The level-20 verification line struck from `FEAT-SCHEDULE-01`** — it asserted Guardian 11 four lines below a table saying 14 | 1× |

### ⚠ Why they are missing, derived

**`PT-1` through `PT-66` were renamed from a `C`-series to end a three-way namespace collision — the Library's `C-nn`, the category files `C01`–`C18`, and the playtest series.**

**The gap in this file runs `PT-24`, then `PT-41` through `PT-51`.** **Twelve consecutive missing entries in one block is not twelve separate omissions.**

> **The rename carried the citations and dropped the entries.**

**⚠ Recorded rather than reconstructed.** **Writing an entry from a citation is exactly the warrant error this project names — the rule is real, the reasoning is not recoverable from the pointer, and inventing it would be worse than the gap.**

**What can be recovered: `PT-43` and `PT-24` state their own content in the citing text and are safe to treat as live.** **`PT-41` and `PT-86` are named but not stated anywhere.**

### The check now catches both directions

**`audit_rulings.py` reports duplicate IDs *and* IDs cited outside this file with no entry in it.**

**⚠ A missing heading is not a duplicate heading, which is why the first version could not see any of these.**
