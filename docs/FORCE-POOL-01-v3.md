# FORCE-POOL-01 v3 — The Force Economy

**Status: SETTLED.** Two mechanics-agent rounds run; one recommendation withdrawn by its author, one proposal withdrawn by the integrator.
**Decision ID: D-AG.**
**Supersedes:** `FORCE-POOL-01` v1 and v2, and `GAP-001b`'s rename-only resolution.
**Fuses in:** `REST-AND-MEDITATION-01` (D-AI) rest units, and `POWER-COSTS-01 §1` (D-AL) degradation. **Both remain live documents** — see §8.
**Depends on:** `GAP-002` (Branch C with hybrid elements), `ALIGNMENT-01` (cost multipliers by band).
**Sources:** KOTOR 1 and 2 `classes.2da`, `regeneration.2da`, `spells.2da`, `featgain.2da`, `cls_atk_*`, `cls_st_jedi_*`. All values `source_system: kotor_game`, adopted deliberately.

---

## 1. The layer

**A dedicated Force pool exists and sits in front of vitality.**

| Layer | Behaviour |
|---|---|
| **Force pool** | Normal casting drains it. Regenerates. Class-differentiated in size. |
| **Vitality** | Casting past an empty pool spills into vitality — the character takes damage to keep casting. |

**Vitality is also the damage buffer**, so overreach costs survivability. RCR's coupling is preserved exactly where it earns its keep — at the moment of pushing too far — without taxing every casting.

**Why the pool exists now when `GAP-001b` deferred it.** That resolution was conditional on `GAP-002`, and rested on Force skills being bought with skill points: under ranked skills there is already an acquisition cost, so a per-use pool taxes twice. **Under feat-chain acquisition there is no learning cost** — Force feats arrive through class progression like a Fighter's bonus combat feats. The per-use cost becomes the only limiter, which is what makes a pool worth having.

---

## 2. The formula

**Force points = `(Force die × Force-class levels)` + `((Wisdom modifier + Charisma modifier) × character level)`. Maximum Force die on the first Force-class level.**

> **⚠ Changed. This section previously read *"Force die + Wisdom modifier + Charisma modifier, per level"* — everything hanging off Jedi level.**

**`MULTICLASS-01 §2.1` is the reason.** **Under the old formula a banked level was worth a whole Force die *plus both modifiers*, which made delaying your first Jedi level worth roughly three times the pool.** **Splitting it drops the banking advantage by 71% and leaves an honest multiclass route within 20% of a pure Jedi.**

**The die is training. The modifiers are capacity.** **A character has a level-12 person's reserves whether or not they spent those levels in a temple.**

**⚠ A character with no Force-class level has no pool at all.** **The ability half is a multiplier that switches on with the first Force level and then reads current character level — it does not accrue beforehand.**

| Class | Force die | Hit die |
|---|---|---|
| Jedi Guardian | 4 | 10 |
| Jedi Sentinel | 6 | 8 |
| Jedi Consular | 8 | 6 |

*(`k1_classes.2da`. KOTOR 2's prestige classes continue the pattern: Weaponmaster and Marauder 6, Watchman and Assassin 8, Master and Lord 10.)*

**`forcedie` sits beside `hitdie` in the same table** — the game's own statement that the pool is built the way vitality is built. **No base lookup table exists in either game's data**; the mechanics agent searched `cls_spgn_jedi.2da` (which is the powers-known table, 2 at level 1 and +1 per level), `classpowergain.2da`, `forceshields.2da`, all `cls_st_*` and `cls_atk_*`, and both games' `classes.2da` and `spells.2da`. The base calculation is runtime, not stored.

**Both ability modifiers contribute.** StrategyWiki reports totals adjusted by (Wisdom + Charisma) × Jedi level. **Secondary, unverifiable from the data**, but consistent with every observable fact.

> **The formula is `hybrid_authored`, not ported.** It reuses the engine's vitality machinery, matches the stored inputs, and is consistent with reported behaviour. KOTOR's actual arithmetic is not recoverable.

**Not adopted:** the flat +40 from Force Sensitive and +50 from Consular dark Mastery — both KOTOR-scale. **Costs are RCR-scale**, roughly 4–20 across the tiers, not KOTOR's 10–60.

---

## 3. Regeneration — SETTLED

### 3.1 Two rates, and the unit changes with the situation

**In combat, per round. Out of combat, per second.**

| Class | **In combat** *(per round)* | **Out of combat** *(per second)* |
|---|---|---|
| **Guardian · Sentinel · Weaponmaster · Marauder** | **1** | **1** |
| **Consular · Watchman · Assassin** | **2** | **2** |
| **Jedi Master · Sith Lord** | **3** | **3** |

**Flat points. No dice, no fractions.**

**In combat, once per round on the character's own turn** — not on every combatant's turn, which would mean up to eight ticks a round in a large fight.

**Fills the current pool up to the *working* maximum, never past it.**

### Why the unit changes

**The source does the same thing and more sharply.** **`regeneration.2da` gives `forceregen` 0.0 in combat and 1.0 out of it** — **KOTOR grants no Force regeneration during a fight at all.**

> **⚠ The column states `1.0` and never names its unit.** **Per second is the reading that matches play, and it is an inference.**

**We keep a small in-combat trickle rather than zero**, because a turn-based fight lasting a dozen rounds is not a KOTOR fight lasting twenty seconds. **But the ratio is the source's shape: out of combat is roughly six times faster at every tier.**

**A 71-point pool refills in 71 seconds for a Guardian, 36 for a Consular, 24 for a Jedi Master.**

### What this means for casting outside a fight

> **Out of combat, cast as much as your points allow. They come back in about a minute.**

**So the cost of exploration casting is not points. It is the working maximum.**

**Degradation applies per cast whether or not anyone is fighting** — **and regeneration refills to the working maximum, which just dropped.** **Four mind-tricks cost you eight points of ceiling you carry into the next fight and do not get back until you meditate.**

**That is the thing a Jedi budgets across a day, and it needs no clock-watching: one number, and it only moves down.**

### 3.2 This is a magnitude departure, and it is deliberate

**KOTOR's in-combat rate refunds about 3.3% of maximum across a five-round fight** — roughly 1.4 points for a level 5 Consular. Proportional regeneration is mathematically correct and produces `working_max / 150` per round, or **0.28 points**, which no one can track at a table.

> **This system will be published for people to play with dice and paper.** The shape is ported; the magnitude is authored. Recorded as a departure rather than smuggled in as a port.

### 3.3 In-combat regeneration is a port, and it runs at half rate

**Previously logged wrong on our side twice.** KOTOR 1's table gives `forceregen: 0.0` in combat and an early finding generalised from it. **KOTOR 2 carries `incombatfpbase: 0.1`** — so in-combat regeneration exists, and adopting it is a port rather than a departure.

> **But it is halved. In combat, Force points regenerate at 50% of the §3.1 rate, rounded up.**

| Class | L1 | L5 | L10 | L15 | L20 |
|---|---|---|---|---|---|
| Guardian | 1 | 1 | 2 | 2 | 3 |
| Sentinel | 1 | 2 | 2 | 3 | 3 |
| Consular | 2 | 2 | 3 | 3 | 4 |

**Rounded up, so no character regenerates zero.**

**The Force Affinity form removes the halving** — see `FORMS-01 §7.1`. **That is what the form buys: the full rate in combat, not the ability to regenerate at all.**

> **This resolves an apparent contradiction rather than creating one.** Force Affinity's stated effect is *"FP regenerate during combat"*, which read as though in-combat regeneration were gated behind it. **It is not — the halving is.** `incombatfpbase` was always a rate parameter and never evidence of a gate.

### 3.4 Wisdom does not boost the rate

`wismodbonus` is `0.00`. **Community sources claiming Wisdom improves regeneration are wrong.** Wisdom feeds the maximum, not the rate. *Recorded because the claim was carried in this project's notes before the file was read.*

---

## 4. Fatigue — SETTLED

**The working maximum degrades across the day. The floor is half the true maximum.**

> **This section is fused.** It was superseded twice — by **D-AI** (`REST-AND-MEDITATION-01`, which removed the rest units it named) and by **D-AL** (`POWER-COSTS-01 §1`, which replaced the degradation model). **v2 required three documents read in the correct order to answer what a long rest does.** Both supersessions are now folded in; the withdrawn versions are recorded in §4.6.

| Element | Rule |
|---|---|
| **True maximum** | Force die + Wis mod + Cha mod, per level. Maximum die at 1st. |
| **Working maximum** | Degrades during the day; never below **half** the true maximum |
| **Degradation** | **A percentage of each power's own cost, scaled by tier — see §4.2** |
| **Trigger** | **Per cast.** Not per encounter. |
| **Recovery** | **Meditation, in RCR's hours and days — see §4.3** |
| **Regeneration** | Refills the current pool up to the **working** maximum, never past it |

### 4.1 What an encounter is — the definition, retained

> **An encounter is any discrete scene in which a power was cast. Not combat only.**

**Undefined until it mattered.** The document used the word throughout and never said what it meant; an integrator inferred "combat" and stated a consequence from it as though it were settled.

**It no longer governs degradation** — that is per cast now. **It still defines the word for every other rule that uses it, and one of those is load-bearing:** `ALIGNMENT-01 v2 §2.1`'s drift fires **once per encounter at the highest tier used.**

> **The two differ deliberately. Reaching for the dark side is one moral act however many times you pull the trigger. Each pull still tires you.**

### 4.2 Degradation — cost and tier together

| Tier | Rate | Example |
|---|---|---|
| **1** | **10%** of the power's cost | Force Slow, cost 6 → **−1** |
| **2** | **20%** of cost | Force Lightning, cost 14 → **−3** |
| **3** | **30%** of cost | Force Storm, cost 24 → **−8** |

**Rounded up, applied on each cast. Full per-power values in `POWER-COSTS-01 §2`.**

**Cost alone would make an expensive tier-1 power tire you as much as a cheap tier-3 one. Tier alone would make Force Crush at 30 cost the same as Insanity at 20.** Together they multiply correctly — at the same cost of 24, a tier-1 power takes 3 and a tier-3 takes 8.

**And a flat number against a growing pool is a shrinking proportion**, which is the point: **higher-level Jedi cast more before tiring.** A level 5 Guardian floors at encounter 4 of a seven-encounter day; a level 20 Guardian never floors.

### 4.3 Recovery — meditation, in hours and days

**RCR has no long rest and no short rest.** Neither term is defined and no unit of rest exists as a game object. **Healing is metered per hour and per day** (p.160): 1 vitality per character level per hour, 1 wound point per day, 1 ability point per day.

**Rest and meditation are different activities.**

| | **Rest** | **Meditation** |
|---|---|---|
| Who | Anyone | Force-sensitive characters only |
| Vitality | 1 per level per hour | **none** |
| Wound / ability points | 1 each per day | **none** |
| Force pool | Refills to the **working** maximum | Refills, **and restores the working maximum** |
| Alignment | **none** | **±1 per day toward the character's side** |

| Meditation | Restores |
|---|---|
| **One hour** | **75% of lost ceiling.** Maximum **two per day.** |
| **Eight hours** | **The true maximum in full**, plus the alignment shift |
| *(Eight hours of ordinary rest)* | *Pool to working maximum. Ceiling unchanged. Full physical healing.* |

**Meditation is not "light, nonstrenuous activity."** RCR p.160 permits light activity while healing naturally; **meditation is excluded by declaration** — a focused discipline that occupies the character completely.

> **An hour spent meditating is not an hour of rest.** The two consume the same resource and cannot be spent twice. **That is the whole of the opportunity cost, and it is expressible entirely in RCR's own units.**

**A Force user who sleeps normally wakes healed, pool full, ceiling still degraded. One who meditates wakes at full capacity and has not healed. A wounded Jedi cannot afford to meditate.**

**Full treatment, including the alignment coupling and the assisted-healing interactions, in `REST-AND-MEDITATION-01` (D-AI).**

### 4.4 The two-rest cap does the work a percentage was doing

Under unlimited rests, a 50% restore let rest-spam stabilise a character near 90% of true maximum. **With two, even a 100% restore ends the day at 74–77%.** The abuse case is structurally gone.

At 25% and 50% the rests barely register. **75% is taken:** two rests produce a visible recovery, the day still ends meaningfully degraded, and a rest never fully undoes the damage — so the eight-hour meditation keeps its role.

### 4.5 The scoped negative

**"Pool empties" as a trigger never fires — but only under normal pacing.** The simulation assumed enough downtime between encounters for a full refill. **In a running sequence that denies downtime**, the pool empties and the trigger would fire.

**Two findings from the no-downtime run, neither of which revives it:** denied downtime is already severe without any ceiling mechanic — a level 15 Consular loses 56% of their castings — and **the ceiling contributes nothing there**, since current Force points bind at every step and the ceiling sits well above them.

### 4.6 Three superseded models, recorded

**Each was tested and replaced. Kept because a rejection with its reason is recoverable and a deleted one is not.**

**`max(2, character level)` flat, per encounter.** Withdrawn by its own author. **The class ratio was identical across all three modes tested — 1.89x, 2.00x, 1.82x** — so it bought no differentiation, only punishment. A true statement about the classes, already fully expressed by the pool formula. **Redundancy called expressive.**

**12% of true maximum per encounter, with a 6% low-impact tier.** Replaced by D-AL. **Per-encounter scoring could not distinguish one casting from six**, and a percentage of maximum cannot produce the level scaling the mechanic exists for.

**20/40/60% of cost by tier.** Tested and halved to 10/20/30. **At those rates every character floored in a normal day regardless of level** — a level 20 Consular ended at exactly the same 50% as a level 5 one.

## 5. Power costs — tiered, and the blend matters

| Character level | Top tier available | Typical cost paid |
|---|---|---|
| 1–5 | Tier 1 | 6 |
| 6–9 | Tier 2 | **9** |
| 10–12 | Tier 2 | 12 |
| 13–16 | Tier 3 | **16** |
| 17–20 | Tier 3 | 20 |

**The right column is a modelling assumption, not a rule.** Powers cost 6, 12, or 20 by tier. But a character does not cast their most expensive power every turn — a level 13 Guardian mixes Force Speed and Force Jump with the occasional Force Storm, so the *average* sits between tiers and rises smoothly.

> **This correction removed most of an apparent defect.** Modelled as top-tier-only, the castings-per-fight curve sawtooths downward at levels 6 and 13, and the Guardian appeared to "dry out in normal fights at 11 of 15 levels." **That was measuring spam.** Blended, the curve tracks the design target within ±1 at nearly every level.

**Record it explicitly so it does not silently drift.** The next person to model this should not rediscover the sawtooth and try to fix a problem that is not there.

### 5.1 Class-differentiated costs — proposed, then withdrawn

**The proposal:** give each class its own cost ladder, so Guardians reach tier 2 at level 9 and tier 3 at level 17 while Consulars reach them at 6 and 13. Rationale: Guardians take Force Speed and Force Jump, Consulars take Force Storm and Insanity, so they should not be modelled as paying the same costs.

**It works on the metric it was aimed at** — Guardian "dry in normal fight" drops from 11 of 15 levels to 0.

**And that is why it is wrong.** Under class-differentiated costs a Guardian can cast **every round of every fight at every level**. The constraint disappears entirely.

> **The design intent is that a Guardian must ration.** The lightsaber is the primary weapon; the Force supplements it. A Guardian who can spam powers instead of swinging is the failure state, not the goal.

**Withdrawn.** The uniform ladder already produces the intended behaviour: sparing use (1–2 per normal fight) is affordable from level 3 onward, boss fights allow 2–4 castings, and spam is capped at 3–5 in a five-round fight.

**Recorded rather than deleted**, per the rule that two corrections in this project were only recoverable because a rejection had been written down.

### 5.2 The curve — validated once, and the numbers have since moved

**As originally recorded:** a level 13 Guardian casts **Force Storm three times and goes dry on round four.** Pool 60, cost 20, regen 3. **Predicted by the owner from the fiction and confirmed by simulation independently** — the strongest validation this project produced.

> **That arithmetic is stale and the result has changed. Two inputs moved after it was recorded.**
>
> **`POWER-COSTS-01` (D-AL) prices Force Storm at 24, not 20.** The original figure was KOTOR's, before the RCR-scale repricing.
>
> **`FORMS-01` (D-AM) halves in-combat regeneration**, so a level 13 Guardian regains **2 per round, not 3.**

**Recomputed:** pool 60, cost 24, regen 2 → **two Force Storms, dry on round three.**

| | Then | Now |
|---|---|---|
| Force Storm cost | 20 | **24** |
| In-combat regen, L13 Guardian | 3 | **2** |
| Castings before dry | 3 | **2** |
| Dry on round | 4 | **3** |

**The validation was sound when it was made.** It confirmed the model against play-feel under the numbers then in force, and both numbers changed for reasons unrelated to it. **This is not a defect in the validation — it is a validation whose inputs were superseded.**

**What it now says about the design is a live question.** Three Force Storms was the owner's prediction from play experience. **Two may be correct — Force Storm is a tier-3 capstone and a Guardian is not a Consular — or it may be a signal that the repricing went one step too far for the class that leans on the saber anyway.**

**Flagged rather than resolved. `C-44`.**

**The level 8 Guardian figure is unaffected** — two cheap utility powers plus two heavier ones, with points to spare. That case used tier-1 and tier-2 costs, neither of which moved.

## 6. Decided / open

### Decided

- Dedicated pool layered in front of vitality; overreach spills into vitality
- Maximum = Force die + Wis mod + Cha mod per level, max die at 1st
- Costs RCR-scale and tiered; typical cost blends across available tiers
- Regeneration flat, per own turn, 3/2/1 base, +1 every 4/5/5 levels
- In-combat regeneration ported from KOTOR 2, not authored
- Wisdom feeds the maximum, not the rate
- Working maximum degrades **10/20/30% of the power's cost by tier, per cast**, floor at 50%
- **One hour of meditation** restores 75% of lost ceiling, two per day; **eight hours** restores the true maximum
- Rest and meditation are distinct activities in RCR's hours and days
- Uniform cost ladder across classes — class-differentiated costs withdrawn

### Open

| Item | Blocked on |
|---|---|
| **The casting profile** | **The weakest assumption in the model.** Cast rates of 40% / 55% / 70% of rounds are invented — not in any `.2da`, not in RCR, not derivable. End-of-day ceiling is robust across the whole plausible range (65–68%), but **vitality spill swings from 0 to 82** across it. One recorded session counting powers cast per encounter per class would move this from assumption to measurement. |
| ~~Meditation's opportunity cost~~ | **Closed by D-AI.** Meditation is not light nonstrenuous activity; an hour meditating is an hour not resting. |
| **Whether the ceiling should bite before level 15** | Owner decision, now that §4.4 states what it currently is |

---

## 7. Change log

| Version | Change | Cause |
|---|---|---|
| v1 | Pool ratified; six items open | Closed a dependency every number rested on |
| **v2** | Regeneration settled flat per turn | Proportional was correct and unusable at a table |
| **v2** | Degradation settled at proportional 12% | **Agent withdrew `max(2, level)`** — the class ratio is identical across all modes, so it bought punishment without differentiation |
| **v2** | Short rest settled at 75%, two per long rest | The cap made the abuse case structural rather than a tuning problem |
| **v2** | Typical cost recorded as a blend | Top-tier-only modelling produced a sawtooth and a Guardian problem that did not exist |
| **v2** | Class-differentiated costs withdrawn | Fixed the metric by removing the constraint the design depends on |
| **v3** | **§4 fused** — D-AI's rest units and D-AL's degradation folded in | **v2 §4 required three documents read in order to answer what a long rest does.** Its stated numbers were dead twice over and it named units that do not exist. |
| **v3** | Three superseded degradation models recorded in §4.6 | A rejection with its reason is recoverable; a deleted one is not |
| **v3** | **In-combat regeneration halved**, Force Affinity removes the halving | `FORMS-01` §7.1. The form's effect and the universal rate are compatible once the halving is stated. |
| **v3** | §5.2's validation arithmetic marked stale | **C-44.** Two inputs moved after it was recorded — Force Storm repriced 20→24, in-combat regen halved. Result changes from three castings to two. |

---

## 8. What was fused, and what stayed separate

**Fused into §4**, because v2's text gave a wrong answer when read alone:

- **`REST-AND-MEDITATION-01` (D-AI)** — the rest-and-meditation distinction and the hour/day units. **v2 §4 named "short rest" and "long rest", which RCR does not define and which D-AI removed.**
- **`POWER-COSTS-01 §1` (D-AL)** — the degradation model. **v2 §4 stated 12% of maximum per encounter, superseded twice.**

**Both remain live documents and were not absorbed.** `REST-AND-MEDITATION-01` also carries the meditation/alignment coupling, the fourth atonement route, and the wound-versus-vitality clock — none of which belong in a Force-economy document. `POWER-COSTS-01` carries the 106-power table, which is its actual content.

**What §4 now holds is the pool's view of both.** Anything beyond that is in the source documents and cited from here.

### 8.1 Why this fusion and not `RULES-01 v2`'s

**`RULES-01 v2` stays unrevised because corrections are still accumulating against it and none are adopted** — its companion says so outright: *nothing below is adopted.* **Fusing it would freeze arguments that are still open.**

**This is the opposite case.** Both overlays are **settled decisions with IDs**. Nothing is pending. **There was no disagreement to preserve — only three documents describing one mechanic, with the foundational one wrong.**

> **A document that looks authoritative and is not is the failure this project already names.** v2 §4 was that document.

### 8.2 One check this thread cannot run on itself

**The fusion should be verified against both source documents before v3 replaces v2** — that nothing was dropped in the merge and no number changed in transit.

**That is the library's function and not the integrator's.** Requested rather than assumed.

---

## Attacks that spend Force points

**`ATTACKS-06` gives Form IV, Aggression — Ataru — two chains that draw on this pool.** *"Intensive use of the Force to maximise speed and agility… Ataru is extremely exhausting."*

| Chain | Cost per use |
|---|---|
| **Hawk-Bat Swoop → Vaulting Strike → Ataru Leap** | **1 Force point** |
| **Saber Swarm → Rapid Cascade → Ataru Flurry** | **2 Force points** |

**These are the only attacks in three rosters that spend from the pool.**

### They do not degrade the ceiling

> **Degradation is defined per power tier — 10, 20, or 30 per cent of the power's cost, by the tier of the power cast.** **An attack has no tier in that sense, so the rule would name no number.**

**Force points spent on an attack are spent and gone. The maximum does not move.**

**An Ataru duellist runs dry; they do not shrink their ceiling.**

### What it costs in practice

**A Velocity chain is declared most rounds.** **A duellist using Saber Swarm through a long fight spends 2 points a round for the whole encounter** — **which is a real constraint against a Guardian's pool, and the reason Ataru is described as exhausting rather than merely fast.**

**In-combat regeneration runs at 50 per cent of the out-of-combat rate (§3.3), so the pool does not refill meaningfully mid-fight.**
