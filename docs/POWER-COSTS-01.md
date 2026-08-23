# POWER-COSTS-01 — Per-Power Costs and Ceiling Degradation

**Status: SETTLED. All 106 powers priced, nothing flagged.**
**Decision ID: D-AL.**
**Amends:** `FORCE-POOL-01 v2 §4` — degradation becomes a per-cast value derived from cost and tier.
**Depends on:** `PARTITION-01` (D-AK).
**Naming:** follows `Force_Powers_Table.docx`, the project's naming authority for powers.

---

## 1. Degradation — a percentage of the power's own cost, scaled by tier

| Tier | Rate | Example |
|---|---|---|
| **1** | **10%** of cost | Force Slow, cost 6 → **−1** |
| **2** | **20%** of cost | Force Lightning, cost 14 → **−3** |
| **3** | **30%** of cost | Force Storm, cost 24 → **−8** |

**Rounded up. Applied on each cast.**

### 1.1 Why cost and tier both

**Cost alone would make an expensive tier-1 power tire you as much as a cheap tier-3 one.** Tier alone would make Force Crush at 30 cost the same ceiling as Insanity at 20.

**Together, the two multiply the way they should.** At the same cost of 24, a tier-1 power takes 3 and a tier-3 takes 8.

### 1.2 It scales with level, which was the point

**A seven-encounter day, two powers per fight, tier 3 in the two boss fights:**

| Class | Level | Max | Ceiling at end of day | Floored at |
|---|---|---|---|---|
| Guardian | 5 | 24 | 50% | encounter 4 |
| Guardian | 10 | 46 | 50% | encounter 5 |
| Guardian | 15 | 69 | 49% | encounter 7 |
| Guardian | 20 | 91 | 54% | **never** |
| Sentinel | 5 | 35 | 49% | encounter 6 |
| Sentinel | 10 | 67 | 49% | encounter 7 |
| Sentinel | 15 | 100 | 58% | **never** |
| Sentinel | 20 | 132 | 68% | **never** |
| Consular | 5 | 46 | 50% | encounter 5 |
| Consular | 10 | 88 | 52% | **never** |
| Consular | 15 | 131 | 68% | **never** |
| Consular | 20 | 173 | 76% | **never** |

**This is one modelled casting pattern, not a prediction.** It assumes two powers per fight and a tier-3 power in each boss encounter. **A character who casts more floors sooner; one who conserves may never floor at all.** The table shows the shape of the curve, not what any given table will see.

**The Sentinel sits between the other two at every level**, which is what its d6 Force die should produce — it floors two encounters later than the Guardian at level 5 and clears the day from level 15 onward.

**Tier-3 capacity, Force Storm at cost 24:**

| Consular level | Casts before the floor |
|---|---|
| 5 | 2 |
| 10 | 5 |
| 15 | 8 |
| 20 | 10 |

> **A first ruling of 20/40/60% was tested and halved.** At those rates every character floored in a normal day regardless of level — a level 20 Consular ended at exactly the same 50% as a level 5 one, **which cost the scaling the mechanic exists to produce.** Recorded rather than dropped.

### 1.3 What is replaced and what is kept

**Replaced:** the 12% and 6% rates and the per-encounter trigger. **Ceiling loss now fires per cast.**

**Kept:** the 50% floor, long-rest full restore, short-rest recovery at 75% of lost ceiling capped at two per day.

> **`FORCE-POOL-01 §4.0`'s encounter definition survives but no longer governs degradation.** It still defines the word for every other rule using it — including **alignment drift, which remains once per encounter at the highest tier used.**
>
> **These differ deliberately.** Reaching for the dark side is one moral act however many times you pull the trigger. **Each pull still tires you.**

### 1.4 The pool and the ceiling divide the work

**Within a fight, the pool binds.** A level 5 Consular with 46 points casts three 12-cost powers and is done.

**Across the day, the ceiling binds.** The pool refills between encounters; the ceiling does not.

---

## 2. The tables

**Cost ladder 4–30.** `›` marks tier 2, `››` marks tier 3. **106 powers.**

> **Powers are listed under their own alignment, not their family's.** The mind-invasion chain crosses — **Read Thoughts is universal, Invade Mind and Drain Thoughts are dark** — so it appears in two tables, marked. **It is the only chain in 106 powers that does this.**

### Dark side — 32

*The mind-invasion chain begins with a universal root — see the universal table for Read Thoughts.*

| Power | Tier | Cost | Ceiling | Notes |
|---|---|---|---|---|
| **Force Slow** | 1 | 6 | −1 |  |
| › **Afflict** | 2 | 12 | −3 |  |
| ›› **Plague** | 3 | 20 | −6 |  |
| | | | | |
| **Force Strangle** | 1 | 6 | −1 |  |
| › **Force Choke** | 2 | 14 | −3 |  |
| ›› **Force Kill** | 3 | 22 | −7 |  |
| | | | | |
| **Drain Life** | 1 | 10 | −1 |  |
| › **Death Field** | 2 | 20 | −4 |  |
| | | | | |
| **Fear** | 1 | 6 | −1 |  |
| › **Horror** | 2 | 12 | −3 |  |
| ›› **Insanity** | 3 | 20 | −6 |  |
| | | | | |
| **Force Shock** | 1 | 6 | −1 |  |
| › **Force Lightning** | 2 | 14 | −3 |  |
| ›› **Force Storm** | 3 | 24 | −8 |  |
| | | | | |
| **Crush Opposition I** | 1 | 8 | −1 |  |
| › **Crush Opposition Ii** | 2 | 12 | −3 |  |
| ›› **Crush Opposition Iii** | 3 | 16 | −5 |  |
| ›› **Crush Opposition Iv** | 3 | 20 | −6 |  |
| ›› **Crush Opposition V** | 3 | 24 | −8 |  |
| ›› **Crush Opposition Vi** | 3 | 28 | −9 |  |
| | | | | |
| **Drain Force** | 1 | 4 | −1 |  |
| › **Improved Drain Force** | 2 | 8 | −2 |  |
| ›› **Master Drain Force** | 3 | 14 | −5 |  |
| | | | | |
| **Force Scream** | 1 | 8 | −1 |  |
| › **Improved Force Scream** | 2 | 15 | −3 |  |
| ›› **Master Force Scream** | 3 | 24 | −8 |  |
| | | | | |
| **Dark Fury** | 1 | 8 | −1 |  |
| › **Improved Dark Fury** | 2 | 14 | −3 |  |
| ›› **Master Dark Fury** | 3 | 20 | −6 |  |
| | | | | |
| **Force Crush** | 1 | 30 | −3 |  |
| | | | | |
| › **Invade Mind** | 2 | 16 | −4 | **new** · *chain crosses alignment* |
| ›› **Drain Thoughts** | 3 | 24 | −8 | **new** · *chain crosses alignment* |
| | | | | |

### Light side — 28

| Power | Tier | Cost | Ceiling | Notes |
|---|---|---|---|---|
| **Heal** | 1 | 8 | −1 |  |
| › **Improved Heal** | 2 | 16 | −4 |  |
| ›› **Master Heal** | 3 | 24 | −8 |  |
| | | | | |
| **Stun Droid** | 1 | 6 | −1 |  |
| › **Disable Droid** | 2 | 12 | −3 |  |
| ›› **Destroy Droid** | 3 | 18 | −6 |  |
| | | | | |
| **Force Aura** | 1 | 6 | −1 |  |
| › **Force Shield** | 2 | 12 | −3 |  |
| ›› **Force Armor** | 3 | 20 | −6 |  |
| | | | | |
| **Force Valor** | 1 | 8 | −1 |  |
| › **Knight Valor** | 2 | 15 | −3 |  |
| ›› **Master Valor** | 3 | 24 | −8 |  |
| | | | | |
| **Force Stun** | 1 | 6 | −1 |  |
| › **Force Stasis** | 2 | 14 | −3 |  |
| ›› **Stasis Field** | 3 | 24 | −8 |  |
| | | | | |
| **Force Barrier** | 1 | 6 | −1 |  |
| › **Improved Force Barrier** | 2 | 12 | −3 |  |
| ›› **Master Force Barrier** | 3 | 20 | −6 |  |
| | | | | |
| **Inspire Followers I** | 1 | 8 | −1 |  |
| › **Inspire Followers Ii** | 2 | 12 | −3 |  |
| ›› **Inspire Followers Iii** | 3 | 16 | −5 |  |
| ›› **Inspire Followers Iv** | 3 | 20 | −6 |  |
| ›› **Inspire Followers V** | 3 | 24 | −8 |  |
| ›› **Inspire Followers Vi** | 3 | 28 | −9 |  |
| | | | | |
| **Revitalize** | 1 | 12 | −2 |  |
| › **Improved Revitalize** | 2 | 20 | −4 |  |
| ›› **Master Revitalize** | 3 | 28 | −9 |  |
| | | | | |
| **Force Enlightenment** | 1 | 25 | −3 |  |
| | | | | |

### Universal — 46

| Power | Tier | Cost | Ceiling | Notes |
|---|---|---|---|---|
| **Throw Lightsaber** | 1 | 8 | −1 |  |
| › **Advanced Throw Lightsaber** | 2 | 15 | −3 |  |
| | | | | |
| **Mind Trick** | 1 | 10 | −1 |  |
| › **Advanced Mind Trick** | 2 | 25 | −5 |  |
| | | | | |
| **Burst of Speed** | 1 | 6 | −1 |  |
| › **Knight Speed** | 2 | 12 | −3 |  |
| ›› **Master Speed** | 3 | 18 | −6 |  |
| | | | | |
| **Force Suppression** | 1 | 8 | −1 |  |
| › **Force Breach** | 2 | 15 | −3 |  |
| | | | | |
| **Force Resistance** | 1 | 8 | −1 |  |
| › **Force Immunity** | 2 | 15 | −3 |  |
| | | | | |
| **Force Push** | 1 | 6 | −1 |  |
| › **Force Whirlwind** | 2 | 14 | −3 |  |
| ›› **Force Wave** | 3 | 22 | −7 |  |
| | | | | |
| **Energy Resistance** | 1 | 6 | −1 |  |
| › **Improved Energy Resistance** | 2 | 10 | −2 |  |
| ›› **Master Energy Resistance** | 3 | 16 | −5 |  |
| | | | | |
| **Battle Meditation** | 1 | 12 | −2 |  |
| › **Improved Battle Meditation** | 2 | 20 | −4 |  |
| ›› **Master Battle Meditation** | 3 | 28 | −9 |  |
| | | | | |
| **Battle Meditation (enemy)** | 1 | 12 | −2 |  |
| › **Improved Battle Meditation (enemy)** | 2 | 20 | −4 |  |
| ›› **Master Battle Meditation (enemy)** | 3 | 28 | −9 |  |
| | | | | |
| **Force Body** | 1 | 15 | −2 | 5 rounds |
| › **Improved Force Body** | 2 | 20 | −4 | 5 rounds |
| ›› **Master Force Body** | 3 | 25 | −8 | 5 rounds |
| | | | | |
| **Force Camouflage** | 1 | 8 | −1 | 10 rounds |
| › **Improved Force Camouflage** | 2 | 14 | −3 | 10 rounds |
| ›› **Master Force Camouflage** | 3 | 20 | −6 | 10 rounds |
| | | | | |
| **Force Deflection** | 1 | 6 | −1 | reaction |
| › **Force Redirection** | 2 | 12 | −3 | reaction |
| | | | | |
| **Force Sight** | 1 | 6 | −1 |  |
| | | | | |
| **Force Distraction** | 1 | 15 | −2 |  |
| › **Force Confusion** | 2 | 20 | −4 |  |
| | | | | |
| **Beast Trick** | 1 | 6 | −1 |  |
| › **Beast Confusion** | 2 | 14 | −3 |  |
| ›› **Dominate Beast** | 3 | 22 | −7 | **new** |
| | | | | |
| **Droid Trick** | 1 | 6 | −1 |  |
| › **Droid Confusion** | 2 | 14 | −3 |  |
| | | | | |
| **Breath Control** | 1 | 6 | −1 |  |
| | | | | |
| **Force Grip** | 1 | 4 | −1 | **new** |
| › **Advanced Force Grip** | 2 | 14 | −3 | **new** |
| › **Telekinetic Throw** | 2 | 16 | −4 | **new** |
| | | | | |
| **Force Pull** | 1 | 6 | −1 | **new** |
| › **Mass Pull** | 2 | 14 | −3 | **new** |
| | | | | |
| **Read Thoughts** | 1 | 8 | −1 | **new** · *chain crosses alignment* |
| | | | | |

---

## 3. Level gating uses total character level

**A power's level requirement is measured against total character level, not class level.**

> **A Soldier 8 / Jedi Guardian 1 is character level 9 and qualifies for a level-9 power.**

**Access and acquisition come apart, and that is correct.** The gate measures **character maturity**; the picks measure **class investment**. That Soldier/Guardian can reach a level-9 power but has one Jedi level's worth of picks to spend. **A veteran soldier who finally trains as a Jedi is not a child in the Force — they are untrained, which is a different thing.**

**Jedi-level gates in the source are a separate mechanism** — *"Level 9 Jedi, Force Body"*, *"Level 7 Jedi Watchman or Sith Assassin"* — and read as class gates. **Deferred to the class workstream** with the rest.

---

## 4. The eight that did not fit a per-cast model — resolved three ways

**All eight carry `forcepoints = 0` in KOTOR 2, and the descriptions show they are not one problem.**

### 4.1 Force Deflection and Force Redirection — reactions

**The source has them always-on:** *"This power is always in effect."*

**Rewritten as reactions**, cast when the character is targeted by a ranged attack. Deflection turns the attack aside; **Redirection sends it back and grants +3 to all deflection rolls.**

> **As passives they are free power, and free power that scales with how often you are shot at cannot be priced.** As reactions they cost per bolt — **so a Jedi under sustained fire drains fast**, which is the fiction.

**These are the first content in the project to require `on_reaction`** — a hook `RULES-01 v2`'s companion notes has **zero acceptance coverage**, with attacks of opportunity deferred off it. **Two powers now depend on it**, which forces it to be tested.

### 4.2 Force Camouflage — a duration replaces the toggle

**The source says it lasts until deactivated. That is an artifact of real time, not a design decision.**

**In a real-time game an indefinite toggle costs attention.** In a turn-based one it costs nothing, because a player would simply never turn it off. **The correct translation is a bounded duration: 10 rounds.**

Stealth is used mostly out of combat, so a minute is the right window — long enough to cross a room, short enough to re-cast crossing a compound.

> **Forms are not this category.** A form is a stance you are always in — you are never in *no* form — which makes it a persistent exclusive-group condition, **already handled by D-AE.** Camouflage is a thing you are sometimes in. **Different shapes; they should not be decided together merely because both looked like toggles.**

### 4.3 Force Body — a normal power, priced against what it saves

**It already has a duration — 30 seconds, five rounds. The structure was never the problem.**

**The problem is that it is a discount on everything else**, and the tiers do more than shift the ratio:

| | Split | Total cost of other powers |
|---|---|---|
| Force Body | 50% vitality / 50% Force | **100%** |
| Improved | 40 / 40 | **80%** |
| Master | 30 / 30 | **60%** |

**Worked: four 20-cost powers inside the window.** Without it, 80 Force points. **With Master Force Body, 48 total — 24 Force and 24 vitality. It saves 56 Force points for 24 vitality.**

**Priced at 15 / 20 / 25.** At Master you break even at roughly two powers in the window and profit at three — **a commitment before a hard fight, not something left running.**

> **And it reaches our layer model deliberately.** `FORCE-POOL-01` already spills overreach into vitality. **Force Body makes that spill voluntary** — choosing to bleed to conserve, five rounds at a time.

---

## 5. Costs that depart from their tier

**Force Crush — 30**, the most expensive. A tier-1 root by chain depth, **tier 3 by override**. KOTOR charged 60, double its nearest rival.

**Advanced Mind Trick — 25 at tier 2**, above most tier 3s. **Unresistable by anything not immune to mind-affecting powers.** The price gates it to roughly 3rd level for a Consular, 7th for a Guardian.

**Drain Force — 4**, the cheapest. Drains an enemy's Force points rather than dealing damage — **useless against most of the galaxy.**

**Crush Opposition and Inspire Followers ladder 8 / 12 / 16 / 20 / 24 / 28.** Both run six deep where everything else runs three, **and cost is the only thing left to express the last three steps** once the tier caps at 3.

**Revitalize and Battle Meditation start at 12** — high for tier 1, because both affect the whole party from their first step. KOTOR charged 50 and 35.

---

## 6. Still open

| Item | Status |
|---|---|
| **Class gates** | **Deferred to the class workstream**, as ruled. KOTOR restricts some powers to Sith Lord, Sith Marauder, or any prestige class. Recorded, not applied. |
| **Character gates** | **Resolved.** *Kreia* cut. *Jedi Watchman* and *Sith Assassin* are classes and fold into class gates. |
| **Acquisition** | **Open.** Feat chains with class-differentiated picks are settled; **how many picks per level per class is not.** `classpowergain.2da` holds KOTOR's schedule, unported. |
| **Forms** | **Eleven, deferred.** Persistent exclusive-group conditions under D-AE, not powers. |
| **Force Sight** | **Possible duplicate** of the Miraluka species trait. |

---

## 7. Method

**Costs are authored, not ported.** KOTOR 2 runs 0–60 across ten values on a differently built pool; ours runs 4–30 on RCR's scale. **`FORCE-POOL-01 v2 §5` governs: only the shape ports.**

**Names follow the docx**, a prior conversion carrying *Force Slow*, *Afflict*, *Force Choke*, *Dark Fury*, *Force Deflection*, and *Force Distraction* where the 2DA carries internal labels. **The 2DA governs mechanical values; the docx governs names and prose.**

**One rename departs from both:** `MASS_STASIS` is **Stasis Field**, dropping the docx's *Force* prefix.


---

## 8. Roster additions and restorations

**92 → 106.** Five restorations correcting an over-application, nine new powers.

### 8.1 Five restorations — availability is not deletion

**Five powers were cut from the roster when they should have been recorded as package-restricted.**

> **The error: three availability rulings were applied as roster cuts.** The project already had the right pattern — Force Sight is on the roster and marked Miraluka-only; Battle Meditation is on the roster and marked Bastila-only in a KOTOR 1 package. **These five should have been handled the same way.**

| Power | Restored as | Availability |
|---|---|---|
| **Breath Control** | Universal, T1, 6 | **Not in a KOTOR 1 package.** Available in KOTOR 2 and later. |
| **Beast Trick** | Universal, T1, 6 | **Not in a KOTOR 1 package.** |
| **Beast Confusion** | Universal, T2, 14 | Same. |
| **Droid Trick** | Universal, T1, 6 | **Restricted to a specific set of droids** — likely G0-T0 only. **Revisit with droid classes and racial traits.** |
| **Droid Confusion** | Universal, T2, 14 | Same. |

**Two cuts stand**, because both were category corrections rather than availability rulings:

**`XXXIMPROVED_BEAST_CONTROL`** — genuinely dead in the source. No description where its siblings have one, the chain re-pointed around it, and the `XXX` marker in prefix form where all fifty-six other cut rows use a suffix.

**Wookiee Rage I–III** — **a racial feat for Wookiees**, not a Force power. This also resolves a collision: `Rage` already carried three referents — the RCR feat at p.181, the Wookiee species trait, and Rakata Rage. **A fourth as a Force power would have made the same identifier both a species trait and a thing that trait interacts with.**

### 8.2 The Beast tree completed

| Power | Tier | Cost | Ceiling |
|---|---|---|---|
| Beast Trick | 1 | 6 | −1 |
| › Beast Confusion | 2 | 14 | −3 |
| ›› **Dominate Beast** | 3 | 22 | −7 |

**Restores the three-tier shape the family had before its middle tier was cut from the source.**

### 8.3 Telekinesis — the gap the video-game roster left

**Of 92 powers, roughly six did anything outside a fight.** Both games resolve every scene in combat or scripted dialogue, so the roster inherited that shape. **A tabletop Jedi spends half a session investigating, negotiating, and asking the GM questions.**

**And every attack power was the character emitting something** — energy, sound, constriction, kinetic force. **None was picking up a crate and throwing it**, which is the single most iconic Force attack in the fiction and absent from both games.

| Power | Tier | Cost | Ceiling | Effect |
|---|---|---|---|---|
| **Force Grip** | 1 | **4** | −1 | Move or manipulate one object at range |
| › **Advanced Force Grip** | 2 | 14 | −3 | Lift a large object, or many small ones in an area |
| › **Telekinetic Throw** | 2 | 16 | −4 | Hurl a gripped object as a weapon; **damage by object size** |
| **Force Pull** | 1 | 6 | −1 | Yank an object to your hand; disarm on a contested check |
| › **Mass Pull** | 2 | 14 | −3 | Pull everything unsecured within a radius toward you |

**Force Grip at 4 ties Drain Force as the cheapest in the system** — pure utility with no combat application on its own.

**Telekinetic Throw requires Force Grip rather than standing alone.** You must be able to hold a thing before you can throw it. **It is also the only damage power whose output depends on the environment rather than the caster's level** — devastating in a warehouse, useless in an empty corridor.

> **Name collision, recorded.** RCR p.181 names **Force Grip** among its dark-side skills, alongside Drain Energy, Fear, Force Lightning, and Rage. **Ours is universal telekinetic utility; RCR's is a dark-side attack.** Same name, two mechanics. **Flagged rather than resolved**, given this project's history with `Rage`.

### 8.4 Mind invasion — and the first chain that crosses alignment

| Power | Tier | Align | Cost | Ceiling | Effect |
|---|---|---|---|---|---|
| **Read Thoughts** | 1 | **universal** | 8 | −1 | Read surface thoughts. The target knows it happened. |
| › **Invade Mind** | 2 | **dark** | 16 | −4 | Force past resistance. Wisdom damage, target stunned. |
| ›› **Drain Thoughts** | 3 | **dark** | 24 | −8 | Tear memories out entire. |

**All 30 original dark powers were combat.** A Sith had no way to make someone talk except killing them — **and interrogation is the most characteristic dark-side scene in the setting.**

> **This is the only tree in 106 powers whose alignment changes as it deepens.** Every other family is uniformly light, dark, or universal from root to capstone. Verified.
>
> **And the structure says something the flat trees cannot.** Reading a surface thought is not an act of the dark side; forcing past someone's resistance is. **The chain is a temptation** — the first tier is freely available to any Jedi, and the powers that follow are not.
>
> **Mechanically it means a light-side character can hold the root indefinitely without drift**, since only dark-classified powers drift. Taking the second tier is the choice, and using it is the cost.

### 8.5 No light-side attack powers were added, deliberately

Every light power is heal, buff, defend, or control. **That is correct rather than a gap: light-side Jedi fight with the saber.** Offensive light powers would blur a distinction the alignment system depends on.


---

## 9. A prerequisite-encoding collision, found and fixed

**The source encodes prerequisites as row indices with `_` as the compound separator** — `masterspell: 47_12` means *requires both row 47 and row 12*.

**Powers authored for this project were given label prerequisites** — `READ_THOUGHTS`.

> **Splitting `READ_THOUGHTS` on `_` yields `READ`, which is not a row.** The chain silently broke and the tree read as three separate roots. **It did not error; it produced a wrong answer that looked right.**

**Caught by an alignment-consistency check** that reported zero mixed-alignment trees when one had just been created deliberately.

**Resolution: a resolver that tries the label namespace before splitting on the separator.** Labels are matched whole; only unmatched strings are treated as compound row indices.

**Recorded because the underlying hazard outlives this fix.** **`_` is both a separator and a character that appears in almost every label in the corpus.** Any future field that mixes authored identifiers with source row indices will hit the same collision, and it will fail the same way — silently, with a plausible-looking result.

---

## 10. Form interaction — degradation is reduced at the encounter level

**`FORMS-01 §7.2` gives two Force forms a degradation reduction:** Force Mastery −10%, Force Affinity −5%.

> **Applied to the encounter's accumulated degradation, not to each cast.** Rounded down, floor of zero.

**Per-cast application does not work.** Degradation values run 1 to 9; **rounded up both cuts vanish, and rounded down they become identical**, since no integer sits between −5% and −10% at that scale. **At the aggregate they separate: 6 points saved against 3, across a fourteen-cast day.**

**Force Potency reduces nothing** and carries FP cost +20%. It is the raw-power form and pays full attrition.

---

## 11. C-43 — a counting defect caused by the alignment-crossing chain

**Raised by the library. Confirmed and fixed.**

**The §2 totals were right — 106 — and the per-table counts were wrong.** The dark table rendered **30 rows against a header claiming 32**; universal rendered **48 against 46.**

> **Cause: the table generator grouped by *family* and placed the whole family under its root's alignment.** The mind-invasion chain's root is **Read Thoughts, which is universal**, so **Invade Mind and Drain Thoughts printed under the universal heading** while the header counts came from a per-power tally.
>
> **The first chain in the corpus that crosses alignment broke the first thing that assumed chains do not.**

**Fixed: powers are placed by their own alignment.** The chain now appears in both tables with a note, and the root is cross-referenced from the dark table.

**Worth recording beyond the fix.** `PARTITION-01` and `POWER-COSTS-01` were both authored when every family was uniformly one alignment. **The crossing chain was added deliberately and knowingly, and it still broke a downstream assumption nobody had written down** — because the assumption was in a generator rather than in a rule.

**A totals check would not have caught this. Only a per-category check did.**
