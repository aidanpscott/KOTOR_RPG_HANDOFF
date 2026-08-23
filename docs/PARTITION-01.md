# PARTITION-01 — The Force Power Roster, Partition, and Drift Tiers

**Status: SETTLED.**
**Decision ID: D-AK.**
**Closes:** `GAP-002 §4` (the partition), agenda `§3.2` (light/dark/universal), `§3.3` (drift tier assignments).
**Unblocks:** `§3.7` / `§6.1` — the Dashade incoming-effect-class predicate.
**Depends on:** `ALIGNMENT-01 v2` (drift tiers, cost multipliers), `FORCE-POOL-01 v2` (per-power costs).
**Source:** the 2DA handler's `force_power_extract.tsv`, both games, all fields. `source_system: kotor_game` throughout.

---

## 1. The roster

**KOTOR 2's power list, with four rows cut.**

| | Dark | Light | Universal | Total |
|---|---|---|---|---|
| **PC-facing** | 30 | 28 | 41 | **99** |
| NPC-only | — | — | 3 | 3 |
| **Roster** | **30** | **28** | **44** | **102** |

**Plus 11 forms** at `usertype = 6`, handled separately — see `§3.4`/`§3.5` of the agenda.

### 1.1 What was cut, and why

**`XXXFORCE_POWER_IMPROVED_BEAST_CONTROL` — cut content that never moved to `usertype = -2`.**

Three independent signals, and they agree:

- **No `spelldesc`.** Its siblings Beast Trick (49184) and Beast Confusion (108459) both carry one. Every other shipped power in the family has a description.
- **The chain skips it.** Beast Confusion's prerequisite is row **182**, not 183 — **the chain was re-pointed around it**, which is what happens when a power is cut late.
- **The `XXX` marker is on the wrong side.** Every other cut row reads `FORCE_POWER_..._XXX` as a suffix; this reads `XXXFORCE_POWER_...` as a prefix. **Fifty-six other `XXX` rows in K2 use the suffix form.**

**Wookiee Rage I, II, and III — not Force powers.**

**It is a species trait**, and RCR p.182's sidebar already governs it: a Wookiee Force-user gains no Dark Side Point for raging naturally, but **does** if they combine rage with a Force skill.

> **Cutting it resolves a collision rather than creating one.** `Rage` was already carrying three referents — the RCR feat named at p.181, the Wookiee species trait, and Rakata Rage. **A fourth as a Force power would have been the worst of them**, because it would have made the same identifier both a species trait and a thing that trait interacts with.

**Verified: nothing depends on them.** No power in either game lists a Wookiee Rage row as a prerequisite, and the three rows carry no prerequisites themselves. Clean removal.

### 1.2 What was added

**`FORCE_POWER_BEAST_DOMINATION` — authored, universal, third tier of the Beast chain.**

**Beast Trick → Beast Confusion → Beast Domination.** The family was built as a three-tier chain, the middle tier was cut, and the remaining two were re-pointed. **This restores the intended shape rather than inventing one.**

**Universal**, matching its siblings. **Marked `hybrid_authored`** — no game data supports it, and the record should say so.

### 1.3 The three NPC-only rows

**`BAT_MED_ENEMY`, `IMP_BAT_MED_ENEMY`, `MAS_BAT_MED_ENEMY`** — the enemy-cast variants of Battle Meditation.

**On the roster, off the character-creation list.** An enemy commander using Battle Meditation against the party is a real encounter, and having the mechanical version is better than improvising it. **Universal, like their PC counterparts.**

---

## 2. The partition

**Every power classifies as light, dark, or universal. Nothing is unclassified.**

### 2.1 The blank field was not an absence

**K2's `goodevil` is blank on 45 rows. K1 writes `-` where K2 writes nothing.**

**Sixteen of the forty-five are K1 powers** — Force Push, Force Wave, Lightsaber Throw, the Speed line, the Resist line, Affect Mind, Dominate, Force Breach, Force Immunity, Suppress Force, Force Whirlwind. **K1 marks every one of them `-`.**

> **So K2 stopped writing the marker rather than leaving powers unclassified.** The blank is an encoding change, not missing data. **This is the kind of thing that reads as a gap and is not one**, and it should be recorded so nobody re-raises it.

**The remaining twenty-nine are new K2 content and were ruled universal by the owner:** Battle Meditation, Force Body, Force Camouflage, Force Repulsion and Redirection, Force Sight, Precognition and Battle Precognition, the Trick/Confusion family, Master Energy Resistance, Breath Control.

### 2.2 The shape of the result, and what it means for alignment

**KOTOR 1 was a deliberate 14/14/14** — perfectly symmetric by construction.

**KOTOR 2 grew to 30/28/44, and the growth went almost entirely into universal.** Dark grew by 16, light by 14, **universal by 30**.

> **The second game's new content is mostly tools rather than moral choices.**

**This matters directly for `ALIGNMENT-01`.** Only **30 of 102** powers drift alignment at all, and drift is assessed once per encounter at the highest tier used.

**So a Jedi can carry a large and varied power list and rarely trigger drift.** Reaching for the dark side stays a distinct act rather than something that happens incidentally — **which is exactly the behaviour the per-encounter rule was written to produce**, arrived at from the content side rather than the mechanical one.

---

## 3. Drift tiers — derived, not authored

> **The tier is the chain depth.** Twenty-seven of thirty dark powers need no decision at all.

### 3.1 The rule

**Tier = position in the prerequisite chain, capped at 3.**

| Tier | Depth | Count | Drift *(per `ALIGNMENT-01 §2.1`)* |
|---|---|---|---|
| **1** | root | 10 | 2, or 1 in the Neutral band |
| **2** | one prerequisite deep | 9 | 3, or 2 in Neutral |
| **3** | two or more deep | 11 | 4, or 3 in Neutral |

### 3.2 The families confirm the tiers that were written from fiction

| Tier 1 | Tier 2 | Tier 3 |
|---|---|---|
| Fear | Horror | Insanity |
| Shock | Lightning | Force Storm |
| Slow | Affliction | Plague |
| Wound | Choke | Kill |
| Drain Force | Improved Drain Force | Master Drain Force |
| Force Scream | Improved Force Scream | Master Force Scream |
| Fury | Improved Fury | Master Fury |
| Crush Opposition I | Crush Opposition II | Crush Opposition III–VI |
| Drain Life | Death Field | — |

> **`ALIGNMENT-01 §2.1` lists Fear and Slow as tier 1, Choke and Lightning as tier 2, Force Storm and Insanity as tier 3.** Those examples were written from the fiction before this data was read. **Every one matches its chain depth.**
>
> **Two independent derivations agreeing is the strongest evidence available here** — the tiers were not fitted to the data, and the data was not fitted to the tiers.

### 3.3 One authored override

**Force Crush is a depth-1 root costing 60 — the most expensive power in either game.**

**By depth it is tier 1. By weight it is obviously tier 3.**

> **Something costing three times what Force Storm costs should not be the cheapest thing a character can do to their alignment.**

**Overridden to tier 3. Recorded as the single exception to the depth rule.**

### 3.4 Crush Opposition caps by the general rule

**It runs six deep** — the only chain in either game to do so — and it is **one of only two class-gated powers in 282 rows**, restricted to Sith Lord.

**Six steps is a class progression, not a power chain.** IV, V, and VI cap at tier 3 under the general rule and need no special handling.

**One consequence, recorded rather than resolved:** a Sith Lord's signature power keeps getting mechanically stronger while it stops getting morally heavier. **Defensible — the moral weight of calling on the dark side does not obviously scale past a point — but it is a consequence of the cap rather than a decision, and someone should be able to find it stated.**

---

## 4. What this closes and what it opens

### Closed

- **The roster** — 102 powers, four cut, one authored, three NPC-only
- **The partition** — 30 dark, 28 light, 44 universal, nothing unclassified
- **Drift tiers** — derived from chain depth for 29 of 30, one override
- **`GAP-002 §4`**, the partition question, in full

### Opens or remains

| Item | Status |
|---|---|
| **`§3.7` / `§6.1` — the Dashade predicate** | **Unblocked.** *Mind-influencing Force skills* can now be defined against a real roster instead of an open category. The candidates are in the Trick/Confusion family plus Affect Mind, Dominate, Fear, Horror, and Insanity. |
| **Per-power costs** | **Not ported.** K2's ladder runs 0–60 across ten values; RCR's scale is 4–20 across three tiers. **`FORCE-POOL-01 v2 §5` governs** — only the shape ports. |
| **Power descriptions** | **The largest remaining gap.** `name` and `spelldesc` are string IDs into `dialog.tlk`. **96 of 103 K2 powers carry a `spelldesc` ID**, so the references exist and are resolvable — but **nothing in the corpus states what any power does.** The owner has an approach; it is not yet specified. |
| **A cut-content sweep** | **Recommended and not run.** One cut power survived at `usertype = 1` with its chain re-pointed around it. **There may be others** — rows with no `spelldesc` sitting among powers that all have one is the signature. Cheap now, expensive during authoring. |
| **`§3.4` `formmask`, `§3.5` forms as feats** | **Untouched by this decision.** Forms are `usertype = 6` and were excluded from the partition. |

---

## 5. One finding carried from the extract

**The shipped forms all carry a single `formmask` bit (`0x40`). The cut `XXX_FORM` rows carry per-form bits** — `0x40`, `0x80`, `0x100`, `0x200`, `0x800`.

> **The design collapsed during development.** The power side still encodes which form *families* a power interacts with; the form side stopped being individually addressable.

**This is evidence on `§3.5`** — whether forms are stances with trade-offs or flat modifiers. **The source abandoned the richer version.** Recorded here because it came from this extract; it belongs to the forms decision when that is taken.

---

## 6. Amendments — the mental-influence trees, and further cuts

**Applied after the roster was first counted. `PARTITION-01` supersedes its own §1 counts with those below.**

### 6.1 Roster changes

**Cut:** `BREATH_CONTROL`, `BEAST_TRICK`, `BEAST_CONFUSION`, `DROID_TRICK`, `DROID_CONFUSION`.

> **`BEAST_DOMINATION` is withdrawn.** It was authored to complete the Beast tree; cutting Beast Trick and Beast Confusion removes the tree it completed.
>
> **Droid Trick and Droid Confusion are a G0-T0 feat**, not player powers. **Held for the KOTOR 2 campaign package** rather than deleted.

**Moved to feats:** `PRECOGNITION` and `BATTLE_PRECOGNITION`. Both zero-cost passives; **both moved, since Battle Precognition is Precognition's sibling and splitting them would leave one power in each system.**

**Also to be handled as feats, later:** the six lightsaber forms and the four Force forms. **Excluded from the power roster entirely** — they are `usertype = 6` and were never in the partition.

### 6.2 The two mental-influence trees

**The source carries four rows across two trees that were never merged.**

| Tree | Tier 1 | Tier 2 | Cost | Rate | Games |
|---|---|---|---|---|---|
| **A** | **Mind Trick** *(was Affect Mind)* | **Advanced Mind Trick** *(was Dominate)* | 10 / 25 | **6%** | both |
| **B** | **Force Distraction** *(was Mind Trick)* | **Force Confusion** *(was Confusion)* | 15 / 20 | 12% | both |

**All four universal. No drift either way.**

> **The name `Mind Trick` moved.** It was row 181 and is now row 6. **Any reference written before this ruling that says "Mind Trick" meant the costed combat power, not the free social one.** Noted on both records.

**Advanced Mind Trick ignores resistance** — any creature not immune to mind-affecting powers cannot resist it. **That is why it costs more than Force Confusion despite sitting in the cheaper tree.** The trees cross over at their second tier, deliberately.

**The gate this creates:** at 10, **only a Consular can cast Mind Trick at 1st level** — Guardian and Sentinel pools are 6 and 9. **Advanced Mind Trick is unreachable until 3rd for a Consular, 5th for a Sentinel, 7th for a Guardian.** Accepted; an unresistable effect should not be a first-level option.

### 6.3 The low-impact degradation rate

**The dialogue tree degrades the Force ceiling at 6% rather than 12%** — see `FORCE-POOL-01 v2 §4.0b`.

**And this ruling forced a definition the corpus was missing.** `FORCE-POOL-01` used the word *encounter* throughout without defining it. **An encounter is any discrete scene in which a power was cast, not combat only** — otherwise dialogue powers have no long-term cost at all, since the pool refills out of combat and the ceiling never moves.

### 6.4 Powers restored to KOTOR 1

**Most of KOTOR 2's additions come back to the first game.** Master tiers of existing trees; all the new trees — Force Barrier, Battle Meditation, Crush Opposition, Force Body, Drain Force, Force Camouflage, Force Scream, Fury, Inspire Followers, Revitalize; Force Repulsion and Force Redirection; and both mental-influence trees.

**KOTOR 2 only: `FORCE_ENLIGHTENMENT`.**

### 6.5 Package-level notes, tied to powers rather than to the roster

**These are campaign-package rules and change no mechanical value.**

**`FORCE_SIGHT` is a Miraluka racial.** Learnable by others **only by being taught**, never through level-up.

> **This is the first power with a species prerequisite, and it may be a duplicate.** Miraluka already carry Force Sight as a species trait in the species records. **The power and the trait may be the same thing wearing two hats** — to be resolved when packages are built.

**`BATTLE_MEDITATION`, in a KOTOR 1-era package: Bastila only.** No other character has the tree.

### 6.6 Descriptions — the gap is closed

**`Force_Powers_Table.docx` supplies descriptions for 88 powers**, with alignment, prerequisites, requirements, and notes.

**It is a conversion someone already made, not the raw game.** It lists **Force Distraction** and carries no Affect Mind — the same rename ruled here, arrived at independently. **Treat it as a secondary source and mark values taken from it accordingly.**

**Its own counts are 35 universal, 29 dark, 24 light — 88 of the roster.** Where it and the 2DA disagree, **the 2DA governs on mechanical values and the docx supplies prose.**
