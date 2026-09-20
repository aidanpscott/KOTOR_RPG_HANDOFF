# RULES-01 v2 — Core Resolution & Effect System

**Status:** Draft 2. Supersedes v1 in full.
**Source:** SRD 3.5 (d20srd.org). See §14.
**Depends on:** nothing. Foundation layer.
**Acceptance:** §11. This document is not done until the spec in §11 runs and passes.

---

## 0. What changed from v1

Five rounds of adversarial review. The substantive corrections:

| v1 said | v2 says | Why |
|---|---|---|
| Derived values implied | **Derived values are unreachable except through the pipeline** | Storing AC/saves rebuilds the drift bug in code instead of in the model |
| No hook system | **Named hooks are the extensibility spine** | Sneak attack, DR, resistance, AoO, crits, death triggers are all hook consumers |
| Conditions are modifier bundles | **Conditions also gate action legality** | The legality layer is the retrofit-hostile piece |
| Effects modify rolls and values | **Effects also modify action plans** | `haste` grants an attack, which is not a number |
| Effects write stats | **Effects write scores; everything re-derives** | 3.5e distinguishes "bonus to Str" from "bonus to Str-based checks" |
| Discipline by convention | **Discipline by interface** | Solo codebases can't enforce conventions; they can enforce types |
| — | **Save-modifies-effect, equipment-as-effect, viewer-scoped reads** | All cheap now, special-cased forever if skipped |

---

## 1. Governing principles

Three rules that constrain everything below. Violations here are architectural, not stylistic.

### 1.1 Interfaces over conventions

Do not rely on remembering. Make the wrong thing unavailable.

- The state object is **private**. The only exported reads are viewer-scoped accessors. There is no global read to accidentally write.
- Derived values (AC, saves, attack bonus, skill totals, speed) have **no setter and no stored field**. They are reachable only as functions over the current effect set.
- If a rule below can be enforced by a type or a module boundary, enforce it there rather than documenting it.

### 1.2 Derived values are computed, never stored

The single most important choice in this document. AC is not a number on a character; it is a function evaluated at resolution time over whatever effects are active. Store it and you have reintroduced state drift into code, where it is harder to see than in an LLM.

### 1.3 Control flow with the narrator

```
LLM declares INTENT → engine RESOLVES → LLM NARRATES the resolved outcome
```

The model never proposes a number, never narrates ahead of resolution, and never selects anything that mutates state. Where the narrator has latitude — tone, phrasing, sensory detail — that latitude is over things that commit nothing. **Bound what mutates; leave affect free.**

---

## 2. The resolution pipeline

One code path for every d20 resolution.

```
resolve(check_type, actor, target?, context) → Resolution
```

1. **Build context** — the `ResolutionContext` (§5.3): actor, target, action, zone relations, engagement relations, environment.
2. **Fire `before_roll` hooks.**
3. **Collect** effects applicable to `check_type` for `actor`.
4. **Evaluate predicates** — each conditional modifier's predicate against the context.
5. **Resolve stacking** per §4.
6. **Roll** 1d20 from the seeded RNG (§10).
7. **Sum** roll + base + net modifiers.
8. **Compare** to DC or opposed result.
9. **Apply overrides** — natural 20/1 auto-success/failure on attacks and saves. **Skill checks and ability checks have no natural 20 rule in 3.5e.** Common implementation error.
10. **Confirm crits if threatened** — a natural 20 (or in-range roll) on an attack is an automatic hit but only a *threat*. Confirmation is a **nested `resolve()` inside the current one**, and it occupies a cursor position (§6.3): hooks may fire between the attack and its confirmation.
11. **Fire outcome hooks** — `on_hit`, `on_miss`, `on_damage`, `on_kill` as applicable, in priority order (§3.1).
12. **Emit `Resolution`.**

### 2.1 Resolution returns a breakdown, never an integer

```yaml
resolution:
  check: attack_roll
  die: 14
  components:
    - { label: "BAB",        value: +5, type: untyped }
    - { label: "Str",        value: +2, type: untyped }
    - { label: "+1 longsword", value: +1, type: enhancement, source: item.longsword_01 }
    - { label: "flanking",   value: +2, type: untyped, source: engagement }
  total: 24
  target_value: 18
  target_label: AC
  outcome: hit
```

Never collapse internally. This is what makes "show the dice" free — the display is a render of data that already exists, not a reconstruction, and reconstructions are eventually wrong.

---

## 3. Hook points

The extensibility spine. Get this set right and most of the remaining 3.5e library is data entry.

| Hook | Fires | Consumers |
|---|---|---|
| `on_action_plan_build` | when available actions are enumerated | conditions (legality), `haste` (extra attack) |
| `before_roll` | before any d20 | true strike, luck rerolls, aid another |
| `on_hit` / `on_miss` | after attack resolution | sneak attack, on-crit riders, bane weapons |
| `on_damage` | before damage applies | DR, energy resistance, damage conversion |
| `on_kill` | when a creature drops | death triggers, XP, quest predicates, faction clocks |
| `on_turn_start` / `on_turn_end` | turn boundaries | duration expiry, ongoing damage, saves to end effects |
| `on_reaction` | when a reaction opportunity opens | attacks of opportunity, readied actions |
| `on_state_change` | after any committed mutation | knowledge-gate satisfaction check (RULES-02), observation events |

### 3.1 Hooks declare a priority — REPLAY-CRITICAL

Every hook registration carries a **phase ordinal**. The engine sorts by it before firing.

Without this, two hooks touching the same value execute in registration order, which depends on load sequence rather than on logged data — and the bit-identical replay guarantee in §10 is **false**. This is one field and it is not optional.

Ordering matters most on `on_damage`, where the phases are fixed:

```
100  base damage
200  additive modifiers          (Str, weapon enhancement)
300  multipliers                 (critical hits)
400  non-multiplied riders       (sneak attack, flaming — these never multiply)
500  conversion                  (e.g. damage type changes)
600  reduction                   (DR, then energy resistance per type)
700  apply
```

**Damage is a pipeline with phases, not a modifier sum.** Critical hits multiply, precision damage does not multiply, and energy riders do not multiply — no amount of typed-stacking machinery expresses that. This is the general answer to §15.2: effect application order *is* non-commutative, and the resolution is a declared phase per hook rather than a rule per case.

### 3.2 `on_state_change` cascade bound — REPLAY-CRITICAL

`on_state_change` drives knowledge-gate satisfaction (RULES-02). A reveal sets a flag; setting a flag is a mutation; that fires `on_state_change`; which may satisfy another gate. Unbounded, this is an infinite loop inside a committed transaction.

**Settle-then-fire, not fire-per-mutation:**

1. Collect all mutations from the current resolution.
2. Apply them.
3. Run **one** evaluation sweep over the resulting state.
4. Repeat from 1 if the sweep produced new mutations.
5. **Hard iteration cap (suggest 8). On breach, log and halt the sweep — never throw.** A stuck cascade must be diagnosable from the event log, not a crash mid-session.

**Sweep granularity is per-action, not per-plan-entry.** Per-entry would interleave knowledge reveals into the middle of a full attack, producing narration in an order nobody authored.

---

## 4. Bonus type registry

| Type | Stacks with itself? | Notes |
|---|---|---|
| **Untyped** | ✅ | Not a type — the *absence* of one. Stacks unless from the same effect. Note this is a *bonus* rule: same-source penalties and repeat casts of the same spell are governed by overlap (§5.4), not by type. Two rules, cross-referenced, not one. |
| **Dodge** | ✅ | Always, even with other dodge. Applies vs. touch. Never granted by spells or items. **Loss when the Dex bonus to AC is lost is a predicate (§5.3), not a note here** — implemented in the type table it becomes a special case inside the AC function. |
| **Circumstance** | ✅ | Unless arising from essentially the same source — requires `source_tag` to evaluate. |
| Alchemical | ❌ highest | |
| Armor | ❌ highest | Excluded from touch AC. |
| Competence | ❌ highest | Attacks, saves, skills, caster level checks. **Not** ability checks, damage, or initiative. |
| Deflection | ❌ highest | Stacks with all other AC types. Applies vs. touch. |
| Enhancement | ❌ highest | Per object / creature / ability score. Enhancement-to-natural-armor is distinct from natural armor; they stack. |
| Insight, Luck, Morale | ❌ highest | Morale: mindless creatures immune. |
| Natural armor | ❌ highest | Excluded from touch AC. |
| Profane, Sacred, Resistance | ❌ highest | Resistance applies to saves. |
| Racial | ❌ highest | Narrow. Racial **ability adjustments** (elf +2 Dex / −2 Con) are inherent score changes and attach at the score level per §5.1 — they are not typed modifiers and do not belong in this table. The type is only used for the handful of racial bonuses on skills and saves (e.g. dwarven saves vs. poison). |
| Shield | ❌ highest | Excluded from touch AC. |
| Size | ❌ highest | |

**Master rule:** where modifiers don't stack, apply the **best bonus and the worst penalty**.

**Penalties** stack regardless of type unless from the same source. Implement as effects with negative magnitude plus a `stacks_as_penalty` flag — not a parallel system.

Only the type *field* and the resolution *rule* are structural. The twenty type names are data.

---

## 5. The Effect object

```yaml
effect:
  id: eff.haste.7c21
  definition: srd.spell.haste
  source_tag: spell.haste
  origin: actor.wizard_01
  targets: [actor.fighter_01, actor.rogue_01]

  modifiers:
    - applies_to: [attack_roll]
      value: +1
      bonus_type: competence
    - applies_to: [ac]
      value: +1
      bonus_type: dodge
    - applies_to: [save.reflex]
      value: +1
      bonus_type: dodge
    - applies_to: [speed.land]
      value: +30
      bonus_type: enhancement

  action_plan_modifiers:              # see §6
    - hook: on_action_plan_build
      when: action.type == full_attack
      operation: append_attack
      params: { at_bab: highest }

  save:                               # see §5.2
    type: null                        # haste allows none

  duration:
    kind: rounds
    value: 10                         # resolved at creation, not stored as CL formula
    expires_at: 1247                  # absolute game-time round
    tick_point: originator_turn_start

  suppressible: true
  dispellable: true
  tags: [magic, transmutation]
```

### 5.1 Effects write scores, not derived values

`bull's strength` is **not** "+4 to attack and damage." It is an enhancement effect on the **Strength score**, from which attack, damage, Climb, Jump, and carrying capacity all re-derive.

Model it as a derived-value write and you get the wrong answer everywhere 3.5e distinguishes a bonus *to Str* from a bonus *to Str-based checks*. The derivation graph is:

```
score → modifier → derived values → resolution
```

Effects attach at the highest applicable level. A `+2 competence to Climb` attaches at the derived level; `bull's strength` attaches at the score level and cascades.

#### Accumulative derivations — an explicit exception

Some values are **not** pure derivations and must not be forced through the graph. They are accumulated at discrete events rather than computed continuously:

- **Maximum HP** — a function of Con *at each level-up*, summed, not of current Con.
- **Skill points** and **feat selection** — allocated at level-up, not recomputed.

Consequences for a mid-session Con change, all authored rules rather than emergent ones:

- A Con effect that raises max HP raises **current HP by the same amount**.
- On expiry, current HP drops back by that amount, **but never below 1** — temporary Con loss does not kill retroactively.

This is named here deliberately. Left in open questions, the temptation is to solve it generally inside the derivation graph, which costs a week and produces a worse answer than four lines of explicit rule.

### 5.2 Save-modifies-effect scaffolding

```yaml
save:
  type: reflex
  dc: 17
  on_success: half        # negates | half | partial | none
  partial_result: shaken  # when on_success == partial
```

Half-on-save is far too common to bolt on later. Every effect carries an optional save block.

### 5.3 Conditional modifiers and the ResolutionContext

Flanking, cover, favored enemy, bane weapons, higher ground, invisibility — all apply only for specific actor/target/situation triples. Every modifier may carry a predicate evaluated against:

```yaml
resolution_context:
  actor, target, action
  zone_relation:        { same | adjacent | distant, distance_ft }
  engagement_relation:  { engaged, flanked_by, threatened_by }
  perception:           { actor_can_see_target, target_can_see_actor }
  environment:          { cover, concealment, lighting, terrain }
```

Build modifiers as unconditional in v1 and every conditional bonus thereafter is a special case. This is not deferrable.

### 5.4 Identity and source tracking

Needed to distinguish **stacking** from **overlap**: the same spell cast twice yields the better or longer instance, not the sum. Also gives `dispel` something to target and `source_tag` its circumstance-stacking evaluation.

---

## 6. Action plans

The layer v1 lacked entirely, and the reason `haste` broke it.

An action does not resolve directly. It produces a **plan** — an ordered sequence of resolutions — which effects may modify.

A full attack at BAB +6/+1 yields a two-entry plan. `haste` appends a third at highest BAB. No part of the modifier system is involved, which is precisely why the modifier system alone couldn't express it.

Plan operations: `append_attack`, `remove_action`, `substitute_action`, `constrain_movement`, `force_action`.

`substitute_action` is also how NPC compliance sabotage resolves (RULES-02) — misleading execution is a *different action with a different outcome*, not a shading of the requested one.

### 6.1 Plans are built at execution, never at declaration — REPLAY-CRITICAL

**Plans are derived values.** §1.2 applies here verbatim, one layer up.

If a plan is constructed when the action is declared and `haste` drops between entry two and entry three, entry three must not exist. Constructing the full sequence up front and then walking it is **caching a derived value**, and it is the natural reading of "build the plan, then execute the plan" — which is why it is called out explicitly here.

The correct shape: the plan exposes *what comes next*, evaluated against current state each time.

```
enumerate_legal_actions(actor, context)         # legality filter — §7
  → open_plan(action, actor)
  → while plan.has_next():
        entry = plan.next(current_context)      # built now, not earlier
        fire on_action_plan_build hooks         # effects may modify the remaining plan
        resolve(entry)                          # §2
        fire on_reaction / on_state_change opportunities
```

### 6.2 Plan entries bind targets late

Your target dies on attack one of three. RAW permits redirecting remaining iteratives to another target in reach. If `entry.target` is bound at build time, that is inexpressible and becomes a special case.

**Targets resolve at entry execution**, against the context as of that moment.

### 6.3 A plan is a cursor, not a batch

The plan holds a **position**. Entries execute one at a time. Hooks fire between entries. This is required for interruptions, readied actions, and attacks of opportunity — but it is equally required for the ordinary case in §6.2, and for crit confirmation (§2 step 10), which is a nested resolution occupying a cursor position.

### 6.4 The discriminating test: Cleave

`Cleave` appends a plan entry **mid-execution, from an `on_kill` hook, into the currently-running plan.** That is `haste`'s mechanism with a trigger instead of a duration.

If Cleave works without special-casing, this layer is real. `Great Cleave` is the recursive form and will immediately reveal whether a loop guard is needed — it is, and the bound is one cleave per kill with a per-round iteration cap logged like §3.2.

Cleave is also a **feat, not a spell**, which stresses the §8 claim that feats, spells, and equipment share one effect schema. It is item 1.5 in the acceptance spec (§11).

---

## 7. Conditions and action legality

Conditions are named modifier bundles **that can also forbid actions.** The bundle is easy. The legality layer is the retrofit-hostile part.

```yaml
condition.entangled:
  modifiers:
    - { applies_to: [attack_roll], value: -2, bonus_type: untyped }
    - { applies_to: [score.dex],   value: -4, bonus_type: untyped }
  legality:
    - forbid: move                   # or halve, per source
    - require_check:
        action: cast_spell
        check: concentration
        dc: "15 + spell_level"
        on_failure: [action_lost, slot_lost]   # action_lost | slot_lost | no_effect
```

v1 condition set — **twenty**: *shaken, panicked, cowering, sickened, nauseated, fatigued, exhausted, dazed, stunned, slowed, prone, flat-footed, blinded, deafened, entangled, grappled, held, helpless, staggered, disabled.*

> **⚠⚠ `dying` AND `dead` ARE NOT ON THIS LIST, AND THEY USED TO BE — `PT-2167`.** They are `VitalityState` values that `applyDamage` already produces and `projectPlayState` already folds, and **`VitalityState` remains their sole producer.** A condition system that tracked its own copy would be one fact in two places, which is the shape that has produced silent drift everywhere it has been allowed. **Anything here that needs to know whether a creature is dying or dead reads it from `VitalityState` directly** — the target-type categories and the escalation rules included.
>
> **⚠ THE SET WAS TWENTY, BECAME NINETEEN, AND IS TWENTY AGAIN.** Two left (`dying`, `dead`) and two arrived: `slowed` and `held`, both below, both for the same reason — **a real mechanic in the corpus with no member here to carry it.**

**Escalation** is per-condition data: `fatigued` + `fatigued` → `exhausted`; `shaken` + `shaken` → `shaken` (⚠ **never** `panicked` — the fear ladder escalates by SAVE MARGIN, not by stacking. `PT-445`).

**Like penalties don't stack:** two `shaken` sources give one −2, both being morale penalties in the fear category.

#### Target types — `PT-459`

**⚠ Every attack, power and effect declares a `targets:` set from `sentient` · `beast` · `droid`. Omitted means all three.**

| Class | Targets | Example |
|---|---|---|
| **`mind`** | **`sentient` only** | `Force Distraction` · `Force Confusion` · `Mind Trick` · `Dominate Mind` |
| **`fear`** | **`sentient` · `beast`** | `Fear` · `Horror` · `Insanity` · a beast's `Roar` |
| **`life`** | **`sentient` · `beast`** | **healing — `Heal`, `Improved Heal`, `Master Heal`, all three `Revitalize`** · draining · **all five poison types** |
| **`system`** | **`droid` only** | ion · slicing · `Stun Droid` · `Disable Droid` · `Destroy Droid` |
| **`physical`** | **all three** | every weapon attack |

> **⚠⚠ THE EXAMPLES WERE A TIER CHAIN AND TWO OF THEM ARE NOT IN IT — `PT-2435`, `PT-2438`.** This cell read *`Mind Trick` · `Dominate Mind` · `Force Confusion`*, which reads as one ladder and is two. **`Force Confusion`'s lower tier is `Force Distraction`**, not `Mind Trick`: they are K2's `FORCE_POWER_CONFUSION` and `FORCE_POWER_MIND_TRICK`, and `Force Distraction` is that second power's description **verbatim** — diffed against `dialog.tlk`, the only differences being the name and 30 seconds read as 10 rounds.
>
> **⚠ `Mind Trick` AND `Dominate Mind` ARE THE OTHER GAME'S LINEAGE** — K1's `FORCE_POWER_AFFECT_MIND` and `FORCE_POWER_DOMINATE`, both conversation-only, both carrying no combat mechanic at all. They stay in this class because they are still `mind` and still `sentient`-only; they are listed after the pair that IS a chain rather than interleaved with it. **A name that outlives its rule** — the class was right, the worked example had stopped being one.

**⚠ This is not new. It was written 36 separate times.** **`force/FORCE-POWERS-01` carries a target clause on 36 of its 92 rows** — *"This power does not affect droids"* twenty-six times, plus the `Battle Meditation`, `Heal` and `Revitalize` variants. **`Force Confusion` already reads *"only works on sentients; beasts and droids are immune."***

> **⚠ One property replaces thirty-six sentences, and it makes the EXCEPTIONS visible.** **`Force Whirlwind`'s *"does not affect droids equipped with energy shield hardware"* is now a stated exception rather than one line among ninety-two.**

**⚠ `fear` is SEPARATE from `mind`, and narrower than it looks.** **`Fear`, `Horror` and `Insanity` say *does not affect droids* and say NOTHING about beasts.** **Under `mind → sentient only` a rancor would be immune to a rancor's `Roar`.** **A beast can be frightened; `fear` therefore takes `sentient` and `beast`.**

**⚠ Consequence, stated because it is not free: NO POISON WORKS ON DROIDS.** **All five types — `PT-455`, `PT-457`.** **A Beast Master facing a droid party has a companion whose venom does nothing, and four tags go dead in that fight.**

#### `held` — `PT-2264`

**⚠⚠ THE TWENTY-SECOND CONDITION NAMED, AND THE TWENTIETH IN THE SET.** It
arrives for the reason `slowed` did: **a mechanic already written all over the
corpus with no member here to carry it.**

- **`Force Root`**, `FORCE-POWERS-01`: *"the target cannot move at all. ⚠ It
  is NOT paralysed — it may still attack anything already within its reach,
  and may still be attacked normally."*
- **Five beast attacks**, `BEASTS-ATTACKS-01` — `Maw`, `Skewer`, `Latch On`,
  `Coil`, `Throatlock`: *"held — it cannot move away, though it may still
  act."*

> **⚠⚠ `entangled` WAS CHECKED FIRST AND DOES NOT ABSORB IT.** `entangled` is
> the one condition above with a worked bundle in `§7`, and it forbids
> movement — but it also states **−2 to attack rolls, −4 Dexterity, and a
> concentration check to cast.** `Force Root`'s own row states −6 to Defence
> and Reflex and **no attack penalty at all**, deliberately. Using `entangled`
> would re-impose through the condition the exact penalty the power's
> modifier rows exist to exclude.
>
> **⚠ `grappled` IS MUTUAL AND `held` IS NOT.** A grapple binds both parties.
> **`Coil` is the proof that `held` binds only one**: it applies `held` and
> states no constraint on the snake whatsoever. Where a holder IS constrained
> — `Maw`, `Skewer`, `Latch On` — **each attack says so in its own sentence**,
> because a rancor with something in its jaws cannot bite elsewhere. That is a
> fact about jaws, not about this condition.
>
> **⚠ AND `immobilised` IS NOT A CANDIDATE, IT IS A WORD.** It is defined
> nowhere; it appears inside the Zakkeg's `Unyielding` prose, as a category
> label in `FORMS-01`, and as flavour in `SPECIES-CHAPTER-v2`.
> `PROPERTY-VOCAB-01` has already ruled on this exact usage: *"the feat
> invented its own words"*, and *"If the engine has a category, a feat MUST
> NAME IT rather than describe it."*

**`held` — you are anchored where you stand, and nothing else is wrong with
you.**

- **Your Move budget is zero.** Not halved — `slowed` is the halving.
- **Everything else is untouched.** Action, Bonus, Gear and reactions all
  survive, you attack at no penalty, and your Defence is unchanged.
- **You are a normal target.** `Force Root` states it outright — *"may still
  be attacked normally"* — so this is not a step on the road to `helpless`.

> **⚠⚠ THE DIFFERENCE FROM `stunned` IS THE WHOLE POINT, AND IT IS THE SAME
> DISTANCE `§395` PUTS BETWEEN `stunned` AND `helpless`.** `stunned` takes
> what you DO and leaves you able to get out of the way. **`held` takes the
> getting out of the way and leaves everything you do.** They are opposites,
> and a build that collapsed either into the other would lose a real choice.

#### `slowed` — `PT-2167`

**⚠⚠ THE TWENTY-FIRST CONDITION, AND IT IS A RULES CHANGE MADE DELIBERATELY RATHER THAN A DATA MAPPING.** `Slow` is row 5 of `iprp_onhit.2da` in **both** games and **twenty-four real items carry it** — the second-commonest on-hit property in the corpus after `Stun`. It had nowhere to go: the nineteen above contain no synonym for it.

> **⚠ `staggered` WAS CHECKED FIRST AND DOES NOT ABSORB IT.** `staggered` is *one action and no more* — a creature at exactly zero vitality in the source ruleset. `slowed` is a creature acting at reduced rate while perfectly healthy. Collapsing the two would make every Sonic Detonator hit read as a mortal wound.

**`slowed` — you are moving and reacting at half pace.**

- **Your Move budget is halved**, rounded down.
- **You lose your Bonus budget for the round.** ⚠ `ACTION-ECONOMY-01 §2` grants a Bonus only for a self-directed Force power, so this bites a Jedi holding `Burst of Speed` or `Force Valor` and costs most creatures nothing. **Stated rather than dropped:** a condition that took a budget most targets do not have would look inert in testing and would not be.
- **`−1` on attack rolls, on Defence, and on Reflex saves.**
- **⚠ It does NOT cost you your Action.** That is `stunned`, and the two are one rung apart on purpose — the source ladders them that way and so does this.

**Dependents: three powers, and twenty-four items.** *`Slow` is an on-hit property in the source — the twenty-four items — and `PT-2229` additionally ruled that `Force Slow` **is** this condition, since it carried a Will save with nothing for the save to prevent. `Force Mire` and `Force Plague` carry it too.* ⚠⚠ **AND `Force Slow` APPLIES IT WITHOUT THE MOVEMENT HALVING — `PT-2366`.** *Its own prose states `−2` on three rolls and says nothing about movement; that silence is absence, not omission. `Force Mire`'s* “AND the target's speed is halved” *is Mire's own distinguishing addition, not a restatement, and it is what the two tiers are told apart by. Carried as `condition_spares: movement` on the power's own row.* ⚠ **This line read *“dependents: none yet”* until `PT-2366`** — a census written before the powers were wired, left standing through every slice since.

#### `stunned` — `PT-2167`

**⚠⚠ THE MOST COMMON CONDITION IN THE CORPUS BY A WIDE MARGIN.** `Stun` is on **forty-nine** items, and five Force powers apply it — `Force Push`, `Force Stasis`, `Force Stasis Field`, `Force Stun` and `Force Wave`.

**`stunned` — you cannot act.**

- **You lose your Action and your Bonus for the round.** ⚠ Same note as `slowed` on the Bonus: `§2` grants one only for a self-directed Force power.
- **You keep your Move.** ⚠ **OWNER-RULED SHAPE, AND IT IS THE POINT OF THE LADDER:** `stunned` takes what you DO and leaves you able to get out of the way. A condition that took everything is `helpless`, which is two rungs further on.
- **You lose your Dexterity bonus to Defence**, and attacks against you are made as against a `flat-footed` target.
- **You keep your Reaction pool.** ⚠ A reaction is not an action and is not spent on your turn; taking it here would make `stunned` and `helpless` the same condition with different names.

**Dependents: `Immunity (Paralysis)` — nine catalogue items — and `Immunity (MindSpells)`, thirty-five.** *Neither is wired; both are read and named at `PT-2158`.*

#### `blinded` — `PT-470`

**⚠ It has been in the v1 condition set since the set was written, with no defined effect, and THREE species traits already depend on it.**

**`blinded` — you cannot see.**

- **You lose your Dexterity bonus to Defence and take a further `−2` Defence.** Attacks against you are made as against a `flat-footed` target. ⚠ **ONE EXCEPTION — `PT-2150`: a Togruta who passes `Spatial Awareness`' `Alertness` check at DC 13 KEEPS the Dexterity bonus.** The further `−2` and the flat-footed treatment still apply to them.
- **Your own attacks take `−4`.**
- **⚠ You do not know what you are targeting.** **You must name a SQUARE rather than a creature. If the creature is not in that square, the attack misses automatically.** *`PT-471` — owner ruling.*
- **Sight-based checks automatically fail.**

> **⚠ A blinded creature CAN still act and CAN still attack.** **The Togruta's `Spatial Awareness` — *when blinded, an Alertness check at DC 13* — assumes exactly that, and a condition that stopped all action would make that trait meaningless.**

⚠⚠ **ENFORCED AT `PT-2389`** — *the `−4` and the `−2` are modifier rows; the square-naming is an aiming cursor the blinded character alone is given, because walking into what you mean to hit names a CREATURE.* ⚠ **Two clauses remain unbuilt and are named rather than left silent: the Dexterity loss (a term removed from the defence derivation, not a number added to it) and *“sight-based checks automatically fail”* (nothing marks a check as sight-based).**

**Dependents: Miraluka `Second Sight` (cannot be blinded) · `Nictitating Membrane` (immune to light, sand, smoke, spray) · Togruta `Spatial Awareness` (keeps the Dexterity bonus to Defence — `PT-2150`).**

#### `paralysed` — `PT-2392`

**⚠⚠⚠ THE TWENTY-FIRST, AND THE FIRST ADDED BECAUSE SOMETHING APPLIES IT.** *Every other member of this set came from the v1 list. This one arrives because the* **Paralysis Dart** *is already on the shelf —* `Secondary: Paralysis · Duration: 9sec · Save: DC20 for Slow for 3sec` *— and the item reader has been refusing it for as long as it has existed, because* `paralysis` *was not a word this ruleset knew.*

**`paralysed` — you cannot act and you cannot move.**

- **You lose your Action and your Bonus.**
- **Your Move budget is zero.** ⚠ The `held` sentinel, not a divisor.
- **You are treated as `helpless` for combat resolution.**

> **⚠⚠ THAT PAIR IS THE WHOLE LADDER, AND THIS IS ITS TOP RUNG.** **`stunned` takes what you DO and leaves you able to get out of the way. `held` takes the getting out of the way and leaves everything you do. `paralysed` takes both.** *A build that gave it only one would be one of the other two under a third name.*

**⚠⚠ AND *"TREATED AS `helpless`"* ADDS NO NUMBER YET.** *`PT-2369` settled that `helpless` is a* **comparison this ruleset never applies** *— so it has none of its own to lend, exactly as `stunned` and `blinded` are written in terms of `flat-footed` and carry nothing for it either. The numbers arrive when the comparison is given some.*

**⚠ AND YOU CANNOT STAND OUT OF IT.** *`prone` is the only member of `endableConditions`. A paralysed creature spending an Action it does not have, to end a condition it cannot fight, would be `PT-2366`'s deadlock solved in the wrong direction.*

**⚠ ITS EFFECT IS RULED, NOT PORTED.** *The dart's `dialog.tlk` entry has* **no description at all**, *and the corpus's only other uses of the word are an immunity and two negatives —* "it is NOT paralysed". *`PT-2392` is where the meaning comes from.*

#### Comparisons, not states — `flat-footed` and `helpless`, `PT-2369`

**⚠⚠⚠ TWO OF THE TWENTY ARE NEVER APPLIED TO ANYBODY.** They are terms the OTHER conditions' rules are written in:

| Written in | Says |
|---|---|
| **`stunned`** | *"attacks against you are made as against a `flat-footed` target"* |
| **`blinded`** | the same sentence |
| **`Force Sleep`** | *"attacks against them are made as against a `helpless` target"* — and what it applies is **cannot act** |

**⚠⚠ `helpless` WAS ON THE SHELF AS AN APPLIED CONDITION AND WAS WRONG.** *The reader took the only ruled condition-word in `Force Sleep`'s row without seeing it was a comparison — the shape `PT-2265` already named. **And `helpless` forbids nothing, so for as long as it was there the power did nothing at all.***

**⚠⚠ THE SOURCE SETTLES IT.** *`helpless` is not a game term: **43 `dialog.tlk` strings contain the word across both games and every one is dialogue prose.** There is no sleep power in either `spells.2da` to port — `Force Sleep` is authored. `EffectSleep()` is declared with no description at all, and its single use in 638 K2 scripts pairs it with `EffectParalyze()`, so sleep alone does not stop a creature acting in the engine either.*

**They stay in the set of twenty, because the set is this document's.** *What they leave is the count of conditions still awaiting enforcement — **a term nothing can ever apply is not work outstanding**, and counting them as such overstated the real remaining scope by more than three times.*

> **⚠ `§7`'s LADDER STILL CALLS `helpless` A CONDITION** — *"a condition that took everything is `helpless`, which is two rungs further on"*, in `stunned`'s own prose. **Left as written and flagged rather than rewritten:** it describes a severity, and whether the ladder wants a real top rung is its own question.

#### `prone` — `PT-2366`

**⚠⚠ THE SOURCE STATES NO NUMBERS, AND THAT IS THE RULE RATHER THAN A GAP IN IT.** `Knockdown` is an ENGINE CALL — `EffectKnockdown()`, opcode 134 — so there is nothing further to read. It was measured across **all 1,774 K1 and 638 K2 shipped `.nss` files**: the only one that names it is `nwscript` itself, the declaration. No script in either game uses it, so no worked example exists.

> *"This effect knocks creatures off their feet, they will sit until the effect is removed. This should be applied as a temporary effect with a 3 second duration minimum (1 second to fall, 1 second sitting, 1 second to get up)."*

**`prone` — you are off your feet.**

- **You lose your Action.**
- **Your Move budget is zero.** ⚠ The same `held` sentinel, not a second spelling of *cannot move*.
- **⚠⚠ AND NOTHING ELSE.** **No Defence penalty, no attack penalty, and you are not easier to hit.** *Every other d20 ruleset charges `−4` here. This source charges nothing, and `PT-2366` ruled the silence is an answer: “inventing one to make it feel more complete than the source actually is would be the opposite of the faithfulness this project holds everywhere else.”*
- **You keep your Bonus.** *`slowed` loses it because `§7` says so in words. Nothing says so here.*

**⚠⚠ IT IS DURATIONLESS — `roundsLeft` is null.** *`iprp_onhitdur` has no `Knockdown` row, so no duration or chance column exists for it, and all seventeen shipped items apply it with neither. The 3-second figure is read as an ANIMATION FLOOR rather than a game duration — the comment's own* "until the effect is removed" *is at least as natural a reading, and it is the one this corpus already used.*

**⚠⚠⚠ SO IT IS ENDED BY STANDING UP, AND IT IS THE ONLY CONDITION THAT IS.** **Spend your Action to get up.** *`§7`'s legality layer forbids a prone creature its Action, and this condition never expires — so a mechanism that required a free Action would leave a knocked-down creature on the floor for the rest of the game. **Standing up is paid for with the Action rather than gated on it.** One per turn.*

> **⚠ THE MECHANISM IS GENERIC, THE MEMBERSHIP IS NOT.** *`PT-2366`: build it as infrastructure a future condition may need. But you do not stand out of being stunned — `prone` is the only member today, and it qualifies because the source's own three seconds spends one of them* getting up.

**Dependents: `Immunity (Knockdown)` — `iprp_immunity` row 6, a real engine-level immunity type beside `Fear` (row 5) and `Paralysis` (row 7).** *⚠ **No catalogue item carries it**, so nothing is waiting on it. Recorded because the source names it and a future item may.*

**⚠ THE SAVE IS THE ITEM'S, NOT THE CONDITION'S.** *All seventeen state a DC and a kind on their own row. The source is not consistent about which — the Handmaiden's `Echani Strike` says **Fortitude** at DC 15 + attacker level, a grenade says **Reflex** — and ours carry Reflex, authored.*

#### Fear effects — `PT-445`, `PT-446`

**⚠ `fear` is a CATEGORY, not a condition.** *A `fear effect` is anything that applies `shaken`, `panicked` or `cowering` — a Force power, an Intimidate check, a beast's roar, an item's on-hit property. ⚠ A plasma grenade, if it does.*

**⚠ PORTED, not authored.** *`k2_iprp_immunity.2da` row 5 is `Fear`, an engine-level immunity TYPE; `k2_iprp_onhit.2da` row 4 is `Fear` as an on-hit effect type. The source already abstracts exactly this way, which is why `FORCE_IMMUNITY_FEAR` has an empty `spellid` — it flags a type, it does not enumerate powers.*

**⚠ `frightened` is CUT. THREE conditions inside one category — `PT-447`.** *`frightened` was `shaken` plus fleeing, which is `panicked` under another name. `cowering` is the games' own `Fear`, which does not make you nervous — it makes you helpless.*

| Condition | Effect |
|---|---|
| **`shaken`** | **`−2` on attacks, saves and skill checks.** |
| **`panicked`** | **`shaken`, and it must move away from the source and cannot approach it.** |
| **`cowering`** | **⚠ It cannot act.** |

**Every fear condition ends on a save at the end of the creature's turn.**

**⚠ A creature that saves against a fear effect is `shaken` anyway.** *Fear that misses still lands.* **⚠ EXCEPTION: the `Fear` power negates entirely — `PT-449`. An effect may state that it does not leave the residual.**

**`immune to fear effects` means none of the three can be applied — including that trailing `shaken`.** *Held by `Cold Calculation`, `Blood Frenzy`, and the Sentinel's `Force Immunity: Fear`.*

**⚠ `MindSpells` is a SEPARATE engine category — `iprp_immunity` row 2.** *`Cold Blood` and `Nerve Tendrils` bundle fear with mind-influencing powers. The source treats them as two immunities. Recorded as a departure, `PT-446`.*

> **⚠ SAVE-ENDS-EACH-TURN IS DELIBERATE, and it matters most for `cowering`.** **The games run fixed durations — the `Fear` power cowers for 2 rounds, `Horror` for 4.** **`PT-201` cost a rebuild because one player was consuming 62% of the round; a character who cannot act for four rounds is a player not playing.** **One failed save costs one turn.**

---

## 8. Equipment as effect source

A `+1 flaming longsword` is a modifier bundle with the same schema as a spell — an enhancement modifier on attack and damage, plus an `on_hit` hook adding fire damage. Equipping and unequipping are effect application and removal.

Cheap now. Special-cased forever if skipped.

---

## 9. Duration, expiry, concentration

**Duration kinds:** `instantaneous`, `rounds`, `minutes`, `hours`, `days`, `permanent`, `concentration`, `until_discharged`, `until_dispelled`, `until_end_of_next_turn`.

- Resolve duration **at creation**. A CL 10 `bless` stores 100 rounds, not `10 × CL`.
- Store an **absolute expiry** in game-time rounds and expire by comparison. **Never decrement counters** — decrementing is a mutation replay can't cleanly reconstruct (§10).
- **Tick point is fixed at start of the originator's turn**, per 3.5e convention.
- **Tick order within a tick point is by creation index from the log** — REPLAY-CRITICAL. When several effects expire on the same round at the same tick point, undefined ordering makes replay non-deterministic in exactly the way §3.1 describes.

**Concentration** is structurally distinct: effect life is tied to an ongoing action rather than a countdown. It holds the **action ID** of the originating action, and the engine maintains an active-actions index derived from the log. Not a reference to derived action state — that is circular. An action ID is stable, loggable, and replay-safe.

Three separate termination paths, each needing its own hook:

| Ends on | Hook |
|---|---|
| Damage without a successful Concentration check | `on_damage` |
| The originator taking any other standard action | `on_action_plan_build` |
| Unconsciousness | `on_state_change` |

**Suppression is a flag, never a delete.** An antimagic field that ends restores the effect with remaining duration intact.

Lifecycle: `created → active → (suppressed ⇄ active) → expired | dispelled | removed`

---

## 10. Event sourcing, RNG, and viewer-scoped state

- State is **derived by replay** of an append-only event log. State is never the primary artifact.
- Every event records the **RNG seed and draw index**. Replay is bit-identical.
- Every event carries a **visibility set**. Per-player state is the replay filtered to events that player can see. Single-player is the degenerate case where the viewer sees everything.
- **No code path reads global state directly** — enforced by §1.1, not by discipline.

Gives us: save/load, undo, deterministic bug reproduction, regression tests asserting engine state against recorded sessions, the rollback the death policy needs, and multiplayer visibility for one field.

**For the playtest:** improvised facts append to the log tagged `improvised_fact`. No queue, no merge, no promotion workflow — those stay in month three. Only the recording moves up, because the fiction-breaking log can't be read if improvisations vanish.

---

## 11. Acceptance specification

**This document is not done until these eight run and pass.** Ordered so the structurally weird cases come first — restructuring the hook set at effect two means migrating two effects, not five.

| # | Effect | Axis it stresses |
|---|---|---|
| 1 | **haste** | action economy — modifies what you can *do*, not a number |
| 1.5 | **Cleave / Great Cleave** | plan mutation **mid-execution** from `on_kill`; recursion guard; feat-not-spell on the shared schema |
| 2 | **entangle** | condition bundle + action legality + `require_check` with `on_failure` |
| 3 | **invisibility** | perception state; flips conditional modifiers on the attacker side |
| 4 | **true strike** | single-use consumed modifier, huge untyped bonus |
| 5 | **+1 flaming longsword, on a crit** | equipment-as-effect (§8) + the `on_damage` phase order (§3.1) — fire damage and precision damage must *not* multiply while Str and enhancement do |
| 6 | **fireball** | save-for-half, energy type, zone geometry |
| 7 | **protection from evil** | multiple typed bonuses + compulsion suppression |
| 8 | **bull's strength** + a Str item | score cascade + same-type overlap |
| 9 | **bless** | typed bonus, area, ally-conditional, duration |

**Timebox:** if 1 and 1.5 are clean, the plan layer is sound; if 2 is clean, the pipeline is. Finish the set, then stop and build the slice. "Definition of done" must not become a second design project.

Do not substitute the twelve slice spells for this set. Those are the twelve that happen to fit.

---

## 12. v1 scope

Pipeline complete; content library tiny. Adding the 41st spell is data entry.

**In:** full modifier pipeline, all bonus types, effect object with saves and predicates, action plans, action legality, conditions, hooks, AC variants, equipment-as-effect, event sourcing, seeded RNG, viewer-scoped reads, four classes to level 6, ~20 monsters, ~40 spells, ~30 feats.

**Deferred (data or leaf):** additional bonus type names, DR and energy resistance (hook consumers), attacks of opportunity, spell resistance, most of the condition library, item creation, turning.

**Moved into v1:** **iterative attacks from BAB.** Previously deferred as trivial arithmetic. They are the primary consumer of the plan layer, and `haste`'s `append_attack at_bab: highest` is meaningless without them — acceptance test 1 is not a real test of a single-entry plan.

**Deferred (architecture-touching — not "twenty more data entries"):** `polymorph` replaces the base layer of the derivation graph mid-combat; `summoning` instantiates new actors with their own initiative slots and tactical policy. Also banned for v1: grapple, epic rules.

**Not deferrable, despite feeling like it:** the engagement graph. Without it, flanking is "any two allies in the enemy's zone," which is automatic from round one, and rogues sneak attack every round. See RULES-03.

---

## 13. Honest cost estimates

Recalibration pass, because four rounds of review with one side attacking selects for accepting the attacker's cost estimates. The reviewer had no stake in this calendar.

| Item | Called | Actually |
|---|---|---|
| Event sourcing | "one field" | Field is cheap; the **discipline** constrains every read for the project's life. §1.1 converts it to an interface cost, paid once, up front. Will slow month one. |
| Hook points | "get them right and the rest is data entry" | Circular — you learn the right set by implementing effects. **Expect one restructure around effect 2.** Budget it as normal, not failure. |
| Weighted zone edges | "one integer per edge" | Correct as code cost, wrong as **authoring** cost. Mitigated by defaulting every adjacency to a standard distance and authoring only exceptions — the chasm, the long gallery. |
| Canon capture | "doesn't bite until session eight" | Wrong. Needed **for** the playtest, or fiction-breaking can't be measured. Reduced to a tagged log append (§10). |

---

## 14. Licensing

SRD 3.5 is distributed under the Open Game License 1.0a. If this ships — even internally — the OGL requires the license text and a Section 15 copyright notice to travel with it. Add `LICENSE-OGL.md` before the first build.

Forgotten Realms and *Baldur's Gate: Dark Alliance* are **not** SRD content and are not OGL-covered. Personal use only, per DECISION-001.

---

## 15. Open questions

**Resolved since v2 draft 1 — kept for the record:**

- ~~Racial bonus stacking~~ → §4. Ability adjustments are score-level, not typed modifiers.
- ~~Effect application order~~ → §3.1. Yes, non-commutative. Answered by declared hook phases, not per-case rules.
- ~~Retroactive score changes~~ → §5.1. An explicit accumulative-derivation exception, deliberately not solved inside the graph.
- ~~Concentration referent~~ → §9. Action ID plus a derived active-actions index.

**Still open — discoverable while building, cheaper to fix there:**

1. **Same-source detection for circumstance bonuses** — `source_tag` is proposed and untested against real cases.
2. **Cascade iteration cap value** — 8 is a guess. The log will tell us what real campaigns hit.
3. **`on_damage` phase ordinals** — the §3.1 phases are right in order; the numeric gaps between them are arbitrary and may need widening once DR and resistance land.

---

## 16. Status

Four replay-determinism defects are fixed: hook priority (§3.1), cascade bound (§3.2), plan build timing (§6.1), tick order (§9). Before these, the bit-identical replay claim in §10 was false whenever two hooks touched the same value.

**No further design documents before code.** RULES-03 (combat, spatial graphs, zone dialect) is written *after* the acceptance spec runs, because the spec will change what RULES-03 needs to say.

Next artifact is a passing test suite, not a draft.
