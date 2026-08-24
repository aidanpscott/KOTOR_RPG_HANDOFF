# FORMS-01 — Lightsaber and Force Forms

**Status: SETTLED. Descriptions received; content folded in.**
**Decision ID: D-AM.**
**Closes:** agenda `§3.4` (`formmask`), `§3.5` (forms as feats), `§3.6` (`exclusion: 0x02`).
**Depends on:** `IMMEDIATE-ITEMS-BATCH` (D-AE, exclusion groups).
**Corrects:** `KOTOR2-DATA-FINDINGS-01 F-3`, and raises a contradiction against `FORCE-POOL-01 v3 §3.3` — see §7.

---

## 1. `formmask` is not a form pointer, and F-3 was wrong

**`KOTOR2-DATA-FINDINGS-01 F-3` reads:** *"This is almost certainly which forms a power works with — the mechanism that makes a form a stance with trade-offs rather than a flat modifier."*

**It is not. The bit ranges do not intersect.**

| Rows | Bits used |
|---|---|
| **Castable powers** (`usertype = 1`) | **0–5** |
| **Shipped forms** (`usertype = 6`) | **6 only** (`0x40`) |
| **Cut form rows** (`usertype = -2`) | 6, 7, 8, 9, 10, 11 |

> **No power carries a form bit. No form carries a power bit. Verified across all 246 rows.**
>
> **A mask cannot point at something whose bits it never sets.** Whatever `formmask` does on a power, it is not naming forms.

### 1.1 What the power bits actually group

| Bit | Powers | Character of the set |
|---|---|---|
| 0 | 18 | Direct damage — Shock, Lightning, Force Storm, Wound, Choke, Kill, Drain Life, Death Field, Force Crush, the Scream line, the Push line, the Droid line |
| 1 | 21 | **Every friendly buff, and nothing else** — Battle Meditation, Force Aura/Shield/Armor, the Valor line, Inspire Followers, the Speed line |
| 2 | 24 | Mind, fear, and control — Fear, Horror, Insanity, Stasis, Stun, Crush Opposition |
| **3** | **18** | **Identical set to bit 0** |
| 4 | 45 | Almost everything hostile |
| 5 | 4 | Knockdown and immobilise — Force Push, Force Whirlwind, Stasis, Stun |

**Bit 1 is exactly the friendly-buff set.** Bit 5 is exactly the knockdown set. **These are effect categories, not form references.**

> **And bits 0 and 3 carry identical sets of eighteen powers.** A field naming eleven distinct forms would not have two bits that always fire together. **The redundancy is itself evidence against the form-pointer reading.**

### 1.2 What this costs, and what it saves

**Lost: the mechanic F-3 called *"the thing that makes forms interesting."*** There is no per-power form interaction table in the source. **It does not exist to be ported.**

**Saved: a cross-product that would have needed authoring across 106 powers and 11 forms.** F-3 recommended reading `formmask` before designing forms, and that was right — **it just turned out to remove work rather than add it.**

**The design already had this coming.** The extract showed the shipped forms collapsed to a single bit while the cut ones carried per-form bits. **The richer version was abandoned during development**; F-3 read the wreckage as the mechanism.

---

## 2. Forms are conditions, not feats

**The agenda carried this as *"forms as feats — a departure needing an ID."* That framing came from the source having them in `spells.2da` rather than `feat.2da`.**

**They are neither. They are persistent conditions in an exclusion group.**

> **A form is a stance you are always in. You are never in *no* form.** That is not a feat, which is a permanent capability, and not a power, which is a thing you cast.
>
> **It is a condition with an exclusion group** — the mechanism `D-AE` already specifies, arrived at from the lightsaber-form case in the first place.

**The source agrees.** All eleven forms carry `exclusion: 0x02` — **the shared group identifier D-AE was designed around.**

### 2.1 Two groups, not one

**Seven lightsaber forms and four Force forms.** The source gives them one exclusion value, but **a character in KOTOR 2 holds one of each simultaneously.**

| Group | Members |
|---|---|
| `form.lightsaber` | Shii-Cho, Makashi, Soresu, Ataru, Shien, Niman, Juyo |
| `form.force` | Focus, Potency, Affinity, Mastery |

**Entering a form clears any other in the same group. The two groups do not interact.**

**This is D-AE working as specified** — named tags rather than a bitmask, equality-checked, no composition question.

### 2.2 The zero-cost problem does not arise

**All eleven carry `forcepoints: 0`, which put them alongside the eight sustained powers in `POWER-COSTS-01 §3`.**

**They are not the same case.** Force Camouflage is a thing you are *sometimes* in and needed a duration. **A form is a thing you are *always* in — there is no off state to price.**

> **Switching forms costs an action. Being in one costs nothing.** That is the correct shape and it requires no duration, no drain, and no activation cost.

---

## 3. `exclusion: 0x02` — the 178-row question, answered

**The agenda asks what else shares the group, on the grounds that 178 rows is too many for forms alone.**

**In KOTOR 2, across all 246 rows:**

| `usertype` | `0x02` | `0x00` | `0x01` |
|---|---|---|---|
| **1** — castable powers | **72** | 26 | 5 |
| **2** — special abilities | 1 | 15 | — |
| **6** — forms | **11** | — | — |
| **−2** — cut | 42 | 5 | — |

> **`0x02` is not a forms group. It is on 72 castable powers and all 11 forms.**
>
> **The field is doing a different job than the name suggests** — most likely *"only one instance of this may be active"*, which is true of a buff and true of a form for different reasons.

**Consequence: do not port `0x02` as a group identifier.** D-AE's named tags are authored, and **`form.lightsaber` and `form.force` are the correct groups regardless of what the source's single value covers.**

**`0x01` is five rows — droid powers and item abilities.** A separate group, and not ours.

---

## 4. What is settled and what is not

### Settled

- **`formmask` is not a form pointer.** F-3 corrected.
- **There is no per-power form interaction to port.**
- **Forms are persistent conditions in exclusion groups**, not feats and not powers
- **Two groups** — lightsaber and Force — held simultaneously, one member each
- **No cost, no duration.** Switching costs an action; being in a form costs nothing.
- **`exclusion: 0x02` is not a forms group** and is not ported

### Not settled

| Item | Status |
|---|---|
| **What each form does** | **Unknown.** `spelldesc` IDs 111623–111633 resolve into `dialog.tlk`, which we do not hold. **`Force_Powers_Table.docx` contains no forms** — checked. |
| **Whether Niman ships** | **GameBanshee lists six lightsaber forms, not seven** — Aggression, Contention, Determination, Ferocity, Perseverance, Resilience, mapping to Ataru, Makashi, Shii-Cho, Juyo, Shien, Soresu. **Niman is absent from their list and present in the 2DA.** Either cut late or undocumented. |
| **Acquisition** | Forms have no prerequisites and no tier marking in the source — **the numbering is nominal, not a chain.** Whatever grants them is in an unread table. |
| **Class gating** | Deferred with the rest of the class-gate question. |

> **The content gap is the same one blocking nothing else: descriptions.** We hold eleven form names, their exclusion behaviour, and the knowledge that they carry no cost. **We do not know what a single one of them does.**

---

## 5. One thing recorded because it was nearly missed

**F-3's recommendation — read `formmask` before designing forms — was correct and it produced the opposite of what it expected.**

**Had the forms design been written first, it would have been built around a power-by-power interaction table that does not exist**, and the error would have surfaced only when someone tried to populate it.

**The finding that killed it took one query:** check whether power bits and form bits ever overlap. **They never do.**


---

## 6. The forms, with their effects

**Descriptions received. `Lightsaber_Forms_Table.docx` and `Force_Forms_Table.docx`.**

### 6.1 Lightsaber forms — seven, with one restored and authored

**Niman is absent from the docx and from GameBanshee.** Two independent sources, same omission — it is in the 2DA and documented nowhere.

> **Restored rather than cut, and named Moderation.** The name follows the other six, which are all abstract nouns rather than Legends form names, and it matches Niman's own lore — the balanced, generalist form.

**Moderation's effects are authored. No source supplies them.** Marked `hybrid_authored`.

**The lore supplies a precise shape.** Wookieepedia records Form VI as **the Moderation Form, the Way of the Rancor, and the diplomat's form** — a hybrid of Forms I–V built deliberately to have no weaknesses rather than any strength, favoured by **Jedi Consulars** who would rather spend their time on study and diplomacy than combat drill.

> *"For superior balance, use the Niman form. This form has no specific strengths, but no weaknesses either."* — **Kavar**
>
> **Kavar is a KOTOR 2 character.** The quote is from the game itself, which is the strongest available evidence that Niman belongs in this era's roster despite its absence from every effects table we hold.

**The numbers follow from that directly.** Every other form carries at least one negative line — Aggression gives up general Defence, Ferocity gives up saves, Contention gives up deflection. **Moderation is the only one with no negative line, and its bonuses are the smallest in the set.** A flat +1 across five stats is what *"no strengths, no weaknesses"* looks like in a modifier table.

**The sixth line is the lore hook and it is mechanically distinctive.** Niman practitioners *"supplement saber strikes with telekinetic pushes, pulls, and lifts"* — **it is the only lightsaber form that touches Force powers at all**, which makes it the Consular's saber form. Exactly who the lore says used it.

> **Caveat: the Force-integration clause depends on rules not yet written.** Whether casting in melee provokes anything is `RULES-03` territory. **If nothing penalises casting in melee, the clause is empty and Moderation needs a different sixth line.**

| Form | Also known as | What it does |
|---|---|---|
| **Determination** | Shii-Cho, Form I | Attack +1; Defence +3; Defence vs. current target −3. **Net +0 against your target, +3 against everyone else** — defensive when outnumbered. |
| **Contention** | Makashi, Form II | Attack +3 **only against lightsaber wielders**; Damage +3; Blaster Deflection −5; Saves vs. Force +2 |
| **Resilience** | Soresu, Form III | Defence vs. current target +2; Blaster Deflection +4; Threat Range −1 |
| **Aggression** | Ataru, Form IV | Defence −2; Defence vs. current target +5; Blaster Deflection −4; Threat Range +1. **Net +3 against your target, −2 against everyone else.** |
| **Perseverance** | Shien, Form V | Attack +2; Defence vs. current target −5; Blaster Deflection +2; Critical Multiplier +1. **Attack bonuses also aid deflection, so net deflection is +4.** |
| **Moderation** | Niman, Form VI | Attack +1; Defence +1; Defence vs. current target +1; Blaster Deflection +1; Saves vs. Force +1. **Casting a Force power does not end your melee stance or provoke.** |
| **Ferocity** | Juyo, Form VII | Defence −4; Defence vs. current target +2; Saves vs. Force **−4**; **Attacks per round +1**; Critical Hit Attack +4 |

**Two mechanics the port must carry that RCR does not have:**

**Defence splits into two values** — general Defence and *Defence against your current target*, **and they are cumulative.** Four of six forms use the split, and three of those set the two in opposite directions. **A single Defence number cannot express Determination or Aggression.**

**Attack modifiers feed blaster deflection.** Perseverance's note says so outright: its stated +2 deflection is really +4 because the +2 attack also applies. **A derived value the engine must compute rather than store.**

### 6.2 Force forms — four, and one is renamed

| 2DA label | Name |
|---|---|
| `FORM_FORCE_I_FOCUS` | **Force Channel** — the docx renames it *Force Channel*; **the 2DA label governs here** |
| `FORM_FORCE_II_POTENCY` | Force Potency |
| `FORM_FORCE_III_AFFINITY` | Force Affinity |
| `FORM_FORCE_IV_MASTERY` | Force Mastery |

| Form | What it does |
|---|---|
| **Force Channel** | FP regeneration **+50% out of combat**; Force power damage +3; Saves vs. Force +2 |
| **Force Potency** | Force power damage **+30%**; **FP cost +20%.** *Favoured by Dark Jedi.* |
| **Force Affinity** | **FP regenerate during combat**, at a reduced rate against the non-combat rate |
| **Force Mastery** | Force power duration +50%; opponents' saves vs. Force −2; **your** saves vs. Force −4; **FP cost +20%** |

### 6.3 Forms do interact with powers — globally, not per power

**F-3 was looking for a per-power table and there is none. But Force forms modify Force powers wholesale:** damage, duration, cost, regeneration, and save DCs.

> **That is the interaction, and it is far cheaper than the cross-product F-3 imagined.** Four forms carrying four modifier sets, against 106 powers carrying nothing.

---

## 7. In-combat regeneration — resolved, and Force Affinity keeps its job

**`FORCE-POOL-01 v3 §3.3` treated in-combat regeneration as universal. Force Affinity's entire stated effect is *FP regenerate during combat*.** That looked like a contradiction and is not.

> **Both are true. In combat, Force points regenerate at 50% of the normal rate, rounded up. Force Affinity removes the halving.**

**So in-combat regeneration is universal, and the form buys the full rate rather than the ability itself.** `regeneration.2da`'s `incombatfpbase: 0.1` is a rate parameter and was never evidence of a gate.

### 7.1 The rates

| Class | Level 1 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| **Guardian** | 1 → **1** | 2 → **1** | 3 → **2** | 4 → **2** | 5 → **3** |
| **Sentinel** | 2 → **1** | 3 → **2** | 4 → **2** | 5 → **3** | 6 → **3** |
| **Consular** | 3 → **2** | 4 → **2** | 5 → **3** | 6 → **3** | 8 → **4** |

*Full rate → in-combat rate. Rounded up, so nobody regenerates zero.*

**What Force Affinity is worth across a five-round fight:**

| | Without | With Force Affinity |
|---|---|---|
| Guardian 5 | 5 | 10 |
| Consular 5 | 10 | 20 |
| Consular 20 | 20 | **40** |

**Roughly one extra casting at low level, two or three at high.** Substantial without being the only route to anything — **which is what the earlier gating proposal would have made it.**

### 7.2 Two forms reduce degradation, and the reduction is per encounter

**Force Mastery reduces ceiling degradation by 10%. Force Affinity reduces it by 5%.**

> **Applied to the encounter's accumulated degradation, not to each cast.** Rounded down, floor of zero.

**This is arithmetic, not preference.** Per-cast degradation values run 1 to 9. **Rounded up, both cuts do nothing at every value** — 10% off 8 is 7.2, back to 8. **Rounded down, both cuts give the identical answer at every value**, because there is no integer between −5% and −10% at that scale.

**At the aggregate they separate cleanly.** A Consular casting fourteen powers across a day accumulates 57 points of degradation:

| | Total | Saved |
|---|---|---|
| Base | 57 | — |
| **Force Mastery** | **51** | 6 |
| **Force Affinity** | **54** | 3 |

**And it is less bookkeeping** — one calculation per fight rather than one per casting.

**Force Potency reduces nothing.** It carries FP cost +20% and damage +30% and pays full attrition. **It is the raw-power form, *favoured by Dark Jedi*, and it should be the most expensive to sustain.**

## 8. Are the Force items finished?

**Yes. Everything in the Force workstream is closed.**

**One clause is contingent:** Moderation's Force-integration line depends on `RULES-03`, which does not exist. If casting in melee turns out to carry no penalty, that line is empty and needs replacing.

| Item | Status |
|---|---|
| Roster, partition, drift tiers | **Closed** — D-AK |
| Per-power costs and degradation | **Closed** — D-AL |
| `formmask`, forms as feats, `exclusion: 0x02` | **Closed** — D-AM |
| Form effects | **Closed** — §6 |
| In-combat regeneration | **Closed** — 50% of normal, rounded up. Force Affinity removes the halving. §7.1 |
| Form degradation modifiers | **Closed** — Mastery −10%, Affinity −5%, applied per encounter to the accumulated total. §7.2 |
| Moderation's effects | **Closed** — §6.1, `hybrid_authored`, drafted to the Legends description |
| Power descriptions | **88 of 106 held.** The 14 authored powers have no description because they do not have one yet; the rest are covered. |
| Acquisition — picks per level per class | **Open, and belongs to classes**, not here |
| Class gates | **Deferred to classes**, as ruled |

---

## 7. Critical Hit Attack +4 — what it modifies

**Ferocity grants *"Critical Hit Attack +4"* and §6.1 never defined it.**

> **It applies to the confirmation roll.**

**`ATTACKS-01 §12.6` establishes that a threat becomes a critical only on a second attack roll against the same Defence.** **That roll is the only thing in the system that is specifically a *critical hit attack*.** **Nothing else fits the phrase.**

**A Juyo duellist adds +4 to every confirmation.** **They do not threaten more often — Ferocity does not touch threat range — they simply fail to convert far less.**

### Why it matters more than it looks

**Confirmation is the one roll in the system with no damage attached and total leverage over damage.** **A Crushing Strike that threatens and fails to confirm deals 23; one that confirms deals 46.**

> **A playtest measured the difference at fourteen points of party damage across one corridor fight — 117 against 96 — and it flipped the headline result of the S2/S3 cover comparison from *corridor slightly worse* to *corridor meaningfully safer*.**

**Which is the argument for ruling it rather than leaving it: a single undefined phrase was deciding the largest measured number in the suite.**

### It is the form's identity

**Juyo is described as the most vicious form of lightsaber combat.** **Ferocity already grants Defence −4, Saves vs. Force −4, and +1 attack per round** — **it is all offence and no protection.**

**Landing criticals is what the offence is for.** **Without the +4, Ferocity is a damage bonus with a Defence penalty and nothing that distinguishes it from Power Attack.**
