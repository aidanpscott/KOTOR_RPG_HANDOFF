# AGENDA — current

**Merged from `AGENDA-UPDATED` and rebuilt.** **The two had diverged and the older one carried more.**

> **⚠ `WORLDS-REGISTER-01`, `ATLAS-GEOGRAPHY-01` and `TEMPORAL-ENUM-01` are not in this repo.** **They live in `aidanpscott/kotor_rpg_library` and their status below is from the record, not verified here.**

---

# 1. Next

## 1.1 Species — CLOSED

**⚠ This read *"one axis left — racial feats"* against a chapter where the axis was already finished. Rewritten from the tree.**

**47 records. Every axis settled: abilities, skills, racial skills, languages, subraces, traits.**

**Derived:** **46 of 47 carry at least one named trait.** **`Human` carries none, deliberately** — it trades traits for a bonus feat and a free racial-skill choice.

**`RACIAL-FEATS-01` holds 88 distinct trait names across 99 instances**, regenerated from the chapter.

> **`SPECIES-FEATS-DRAFT` is superseded.** *It was the working document for the pass that produced the chapter's trait lines.* **Nothing cites it and nothing needs to.**

### What remains, and none of it is species design

**Age bands for sixteen species.** **`FORCE-TRAINING-01 §6`.** *Fourteen are an extraction job from UAA or the Campaign Guide; Kaleesh and Echani must be authored.*

**Vision types in prose.** **`Darkvision` and `Low-Light Vision` are statements about a species rather than feats, and belong in the description text.** *Recorded and not yet applied.*

**Droid models.** **Deferred until after the Atlas.**

## 1.2 Classes — thirteen written, nine to go

> **⚠ Rewritten against the tree. This section has now been stale twice.**

### Written — thirteen, all axes settled

| Rate | Classes |
|---|---|
| **Combat** | **Soldier · Jedi Guardian · Marksman · Sith Warrior** |
| **Middle** | **Bounty Hunter · Scout · Jedi Sentinel · Engineer** |
| **Specialist** | **Smuggler · Machinist · Jedi Consular · Sith Assassin · Sith Inquisitor** |

**Each carries: rate, hit die, skill base, class-skill list, feat total, chain count, saves, grants, and a class feature.**

**⚠ Verified by check 19 on every run** — three bands each, plus the `3N ≥ T` stranding test.

### Left — nine, every one authored from nothing

**Standard base, five:** **Agent · Explorer · Doctor · Brawler · Duelist**

**⚠ The roster is incomplete without these.** **Nothing blocks them: rates, bands, save ladders, the `PT-123` assignment rule, chain bands, skill bands and `PT-89`'s credits are all ruled.**

**Prestige, four unnamed** — plus the nineteen already named, **none of which has entry requirements.**

### Open on the written thirteen

**`Armour Proficiency: Light` for the Sith** — **owner. `sas`, `sma` and `jwa` carry it and no base Jedi does, but it does not stratify by tier.** **`ACTION-ECONOMY-01 §18.2` withholds armour from Jedi deliberately because it blocks Force powers.**

**Four classes have authored saves** — Bounty Hunter, Engineer, Machinist, Marksman. **⚠ `cls_st_techspec.2da`, `cls_st_cm_drd.2da`, `cls_st_sithmar.2da`, `cls_st_sithlord.2da` and `cls_st_sithass.2da` are not in holdings.**

**⚠ Three classes sit at exactly eleven chains** — Bounty Hunter, Engineer, Sith Inquisitor. **Raising any by one silently closes it to droids. `PT-114`, `PT-132`.**

---

# 2. Large and unstarted

## 2.1 Items and equipment

**`EQUIPMENT-01` covers weapons, armour, and the sum-of-9 rule. It does not cover the catalogue.**

> **Its own words: *"several hundred items across armour, robes, weapons, upgrades, implants, belts, gloves, headgear, masks, shields, and consumables — and it is a data-extraction job, not a research job."***

**Needs `baseitems.2da`, `itemprops.2da`, `iprp_*`.** **`REQUEST-2DA-PLAYTEST` is pending and asks for some of it.**

**⚠ Droid plating values are placeholders** and have been since the playtest flagged them.

## 2.0-sith The three Sith base classes, and the Sith prestige classes

**Owner ruling: they exist and they are not the Jedi three renamed.**

**⚠ `FORCE-TRAINING-01 §5` cannot close without them.** **A character taken by the Sith currently unlocks nothing.**

**Wanted:** **three non-prestige Sith classes, and the prestige set above them.** **`Marauder` and `Sith Lord` already exist in `FEAT-SCHEDULE-01` and `CLASS-ATTACKS-01` as prestige — check whether they are two of the prestige set or need re-tiering.**

## 2.0-warrant ⚠ The Force-Sensitive gate has no warrant

**`MULTICLASS-01 §3.3`. A live rule resting on nothing.**

**Cited to `GAP-002` branch A, which is dead.** **`PARTITION-01` was proposed and rejected — grepped, zero hits on `Force-Sensitive` or `multiclass`.**

**⚠ RESOLVED. `FORCE-TRAINING-01` is the warrant, by owner ruling.** **Installed at `MULTICLASS-01 §3.3`.**

## 2.0 Multiclass entry credit — CLOSED, and the answer was to delete it

**⚠ Four versions were built. All were exploitable, unusable, or unnecessary.**

> **The rates already do the work.** **Split your career and half of it pays at a slower rate — `MULTICLASS-01 §5`.**

**A pure Soldier finishes twelve attack chains at level 30. An even split finishes nine.** **Nobody has to write that multiclassing costs you; it costs you by arithmetic.**

**Nothing further wanted here.**

## 2.0-pre A send script — DONE

**`send.py`. Refuses on a file not on disk, a file differing from its committed copy, any blocking gate failure, or no arguments.**

**Its only output is the manifest table.**

**⚠ Its first version had the defect it was written to catch** — it watched `repo/` rather than the working file. **`PT-66`.**

## 2.0a STRESS-01 — the verification programme, and the order matters

**From `RESEARCH-AI-PLAYTESTING`, `RESEARCH-RULES-CLOSURE-AND-CODE` and `RESEARCH-RTST-AND-DIFFICULTY`.**

> **⚠ Build the checks before the team. The research says a reading team is the wrong first instrument for this project.**

**The reason, stated plainly:** **AI *"will not flag errors that happen to match the patterns to which it is trained,"* and this project is maximally pattern-matched to d20.** **`PT-36`, `PT-37` and `PT-42` were all found by arithmetic. The reading passes said fine, because it read like d20.**

### Stage 1 — three checks, cheap and mechanical

**`audit_triggers.py`.** **Build the trigger graph — for every rule that fires on a condition, which rules can its effect satisfy — and report cycles.** **⚠ Our graph is depth-one by luck.** **`ACTION-ECONOMY-01 §4`'s *"leaving, not entering"* asymmetry and `§95`'s *"no chain applies"* are the acyclicity guarantee, and both were written for flavour reasons.**

**Metamorphic properties as the twelfth gate check.** **Monotonicity — adding a feat never lowers damage, adding a rank never lowers an outcome.** **Tier monotonicity — a tier-2 entry is never worse than its tier-1 root at the same level.** **⚠ We violated tier monotonicity once already: `PT-36`, `Ataru Flurry` strictly better than `Barrage`.**

**The loop rule.** **One paragraph in `ACTION-ECONOMY-01`, on Magic's `104.4b` shape.** **A voluntary loop must be declared with a count; a mandatory loop resolves as a stalemate.** **Costs nothing and closes the class permanently.**

### Stage 2 — `STRESS-01`, a protocol rather than a team

**Skill-graded agents.** **Naive, competent, optimiser — reported separately.** > **The optimiser finds exploits; the middle one is the tester.** **The near-optimal Wordle solver correlated with human difficulty at `r = 0.075, p = 0.124` — not significant. `PT-40`'s ***"Round one, buff. Every round after, declare your Velocity chain. Do nothing else."*** is that configuration.** **Two independent literatures converge here: `Restricted Play` / Stratabots, and the Aion population models.**

**Target win-rate bands.** **50–70% for a fair encounter, stated per scenario, explicitly higher or lower where a walkover or a wall is intended.** **`S1`–`S8` were built to exercise mechanics and hit no band.** **One sentence each turns every playtest from a demonstration into a measurement.**

**RTST reviewer selection.** **Spawn several, compare hostility, keep the one that objects hardest, run three rounds rather than one.** **`RT-02` is single-shot with a finding budget; this is the addition.**

**The code-world-model readiness gate.** **Hand a document to a fresh model with no context and ask for `state_transition`, `legal_moves`, `terminates`.** > **What it cannot write is what the document does not say.** **A better definition of *fully specified* than any word count, and what `RULES-01 v2 §11`'s acceptance tests are groping toward.**

### Why this order

**Checks are cheap, mechanical, and hit the failure mode we demonstrably have.** **The protocol is expensive, needs agents and rounds, and hits a failure mode the research says we are blind to regardless.**

**And running the checks first gives the stress protocol a corpus that has already been swept — which is the only way its findings will be worth the rounds.**

## 2.1a The droid installation rule — needs fleshing out

**`DROID-INSTALLATION-01` establishes the route and stops.** **Four things it owes:**

**Prices for twelve chains.** *Scaled by tier — a `Master Sensor Package` should be a campaign purchase, not a shopping trip.*

**The slot binding.** > **⚠ Installed feats must consume `Droid Upgrade 1–4` slots, or installation is strictly better than levelling and no droid ever spends a pick again.** **This is the load-bearing constraint and it is currently a sentence rather than a rule.**

**The removal rule.** **An installed feat can be destroyed or ripped out; a learned one cannot.** **What happens mid-session when the part goes needs writing.**

**An `installable` flag in the feat data**, so the twelve are derivable rather than living only in prose.

**And `DROID-INSTALLATION-01` ends without numbers on purpose.** **Twelve droid feat chains can be installed rather than learned; the parts need pricing, and the slot rule needs to bind to `Droid Upgrade 1–4` or installation becomes strictly better than levelling.**

## 2.1b Documentation jobs — one done, two open

### DONE — species communication in prose

**⚠ This item said the content *"currently exists nowhere."*** **Derived: all five records carry it.**

**`Weequay` and `Kaleesh` — scent, with `UAA pp.181–182`'s upwind-40 / downwind-10 figures and the detection-versus-comprehension split.** **`Verpine` — radio antennae and hive consensus.** **`Rakata, Flesh Raider` — signal fires.** **`Twi'lek` — lekku.**

**⚠ The Verpine text is authored rather than recovered.** *It never existed outside a draft and the Library holds nothing to reconcile it against.*

### OPEN — what each skill actually does

> **`SKILLS-01` names the twenty-four and says what each consolidated, and never says what a player *does* with one.**

**The D&D shape — `Sleight of Hand` picks locks, picks pockets, palms objects.** **A paragraph each.**

### OPEN — vision types

**`Darkvision` and `Low-Light Vision` are written as traits on individual species.**

> **They are not feats. They are statements about what a species can see.**

**Needs one table: who has darkvision, who has low-light, who has neither, and what each means in metres.**

*Affected: Gand, Kaleesh, Sullustan, Trandoshan, Kel Dor, Mon Calamari, Bith, Miraluka.*

## 2.2 Crafting

**Not started. Nothing exists.**

**The source tables are named and unheld:** **`upgrade.2da`, `upcrystals.2da`, `itemcreate.2da`, `chemicalcreate.2da`, `itemcreatemira.2da`.**

**Touches `Gear Head`, the droid upgrade slots, lightsaber crystals, and the Machinist class.** **Should probably wait for 2.1.**

## 2.3 The Atlas and the world bible

**`ATLAS-SEED` exists here. `WORLDS-REGISTER-01` and `ATLAS-GEOGRAPHY-01` are in the Library repo** — **41 of 44 worlds covered, per the record.**

**Remaining:** **the last worlds, world lore records, and the skill-assignment decisions deferred until lore is complete.**

**And the world bible is unassembled.** > **The material exists across deep-history sweeps, Gazetteer work, and the species chapter. None of it is put together.** **The old agenda's standing risk was that the sweeps kept producing while the assembly never started.**

## 2.3a Droid models — after the Atlas

**Droids have no homeworld.** **Origin world and homeworld are background fields that determine skills and background feats; a droid has neither.**

> **Owner decision: droids get a *model* instead.** **A series designation determining which kind of droid of that line it is** — T3 against T1, HK-47 against HK-24, and whatever the Battle and Remote equivalents turn out to be.

**Blocked on the Atlas** — the same machinery that turns a homeworld into skills has to exist first.

**⚠ And  is already a field on the record.** **Whatever the model does, it should reuse that slot rather than adding a parallel one.**

## 2.4a The Beast Master's companion list — after the classes

**Owner instruction: determine after the class workstream closes.**

**⚠ Blocks the Beast Master and nothing else.** **The class needs a list of acceptable companions and no bestiary exists.**

**⚠ Contrast the Droid Master, which is not blocked:** **its droids are *species* and the list already exists — Astromech, Assassin, Battle and Remote, in `SPECIES-CHAPTER-v2`.**

**⚠ And `PT-153` makes them materiel rather than companions** — built, commanded, permanent until destroyed, replaceable. **`PT-152`'s difficulty modes do not apply to them.**

## 2.4 Non-playable species

**A bible for what players meet, as prose rather than records — a paragraph each.** **Composes with the world bible.**

## 2.5 App functions

**`Q-4`, the largest unpriced item, still a blank page.** **No interaction model, no session shape, and no answer to whether this is text-in-text-out or something with a sheet and a map.**

---

## 2.9a A gamemaster chapter — does not exist

**⚠ Named by `PT-170`. Two rules have now had nowhere correct to live.**

**`DEATH-AND-DIFFICULTY-01` became its own document because it was a campaign setting rather than a class rule.** **`PT-170`'s map-size dial went into `ACTION-ECONOMY-01` because there was nowhere else.**

**What a GM chapter would hold:** **encounter design and the map-size dial · difficulty modes and their exceptions · the henchman modes from `PT-145` · what a campaign package may override · reading the alignment system at a table.**

**⚠ Scheduled after the classes and before the engine, alongside `§2.9`.**

---

## 2.9 Difficulty modes — the last thing before engine work

**⚠ Owner instruction: this is done immediately before any engine code is written, and after everything else.**

**`DEATH-AND-DIFFICULTY-01` exists and gives the three modes — `PT-152`.** **What it does not give is what each mode changes beyond death.**

**Why it sits here rather than earlier:** **a difficulty mode is a setting the engine reads, and settling it last means it can be written against a finished ruleset rather than a moving one.**

**⚠ And why it must come before the engine rather than after:** **every mode is a branch in resolution.** **Retrofitting a difficulty switch into a resolver that assumes one mode is the expensive version of this job.**

### What it needs to decide

**What each mode changes besides death.** **Encounter levels, save DCs, enemy counts, healing rates — or nothing, and death is the only axis.**
**⚠ Where the setting lives.** **Campaign package, GM choice, or both, and which wins.**
**How a package names its exceptions.** **`§3`'s Revan case is structural — the order of events is arranged, not a save. That needs a form an engine can read.**

---

# 3. Open decisions

**`GAP-002` — which Force content.** **Framed, undecided, four axes.** **The middle path — RCR's structure with KOTOR's roster, 85 powers as ranked skills — is named and unpriced and should be priced before Branch A is taken.**

**Which Force powers are marked Bonus.** *Deferred in `ACTION-ECONOMY-01 §6.1`.*

**Odd-metre radii.** *3 m and 5 m on a 2 m square, left unruled deliberately.*

**Rakata's `fatigued` mapping** — needs an ID. *`E-9` established it imports a choice between two clearing rules.*

**The granularity question** — two alignment steps or eleven bands. *Deferred; the slice cannot observe the difference.*

**Human's *"any two skills at +2, chosen at creation"*** — the only variable entry in the species chapter.

**Whether the Zabrak subraces are far enough apart.** *One skill and zero abilities separate them.*

---

# 4. Species schema questions

**Five of nine closed. Recorded in `AGENDA-UPDATED §2`.**

**⚠ Four were closed today by side effect** — **`SKILLS-01 §5`'s five special cases all resolved when the traits were written.** **`§9.4`'s Mon Calamari predicate dissolved when Craft collapsed into Repair.**

**Still open: `§9.7`** *(Bith Micro-Vision — blocked on `RULES-03`, spatial resolution)* **and `§9.1`** *(incoming effect class — blocked on `GAP-002`)*.

---

# 5. Book-checks and reads outstanding

**`B27`** — Tulak Hord's dating.
**`B29`** — does the Campaign Guide say anything about Alpheridies during the Jedi Civil War?
**`B30`** — does UAA carry a full Miraluka entry? *If so, the edition-boundary rule replaces record one.*
**`B33`** — Jolee Bindo's Great Sith War history.
**Power of the Jedi Sourcebook** — unacquired. *Revised-era entries for Miraluka, Nautolan, Togruta.*
**The Campaign Guide's Force chapter, pp.48–61** — unread.
**Six queued RCR page reads**, including p.183, carried forward from prior context limits.

---

# 6. Things worth reading before they are rediscovered

**`formmask`** — sixteen composing bitmask values, the cross-product between forms and powers. **Unread.**

**What else shares `exclusion: 0x02`** — 178 of 282 rows, too many for forms alone.

**⚠ *"How forms are acquired in the source"* is CLOSED.** **`PT-38` ruled forms are granted, never bought.** **The unread table it was waiting on is no longer blocking.**

---

# 7. Playtest, when it resumes

**Re-run S7.** > **Its headline — *medpacs run out before Force points* — was measured with the healing scaling switched off, because no sheet had Medicine.** **Meris is now at 11, which is +5 a medpac.**

**Run a non-combat suite.** **`SKILL-RESOLUTION-01` defines five resolution modes and combat exercises almost none of them.** **All sheets are now allocated, so all five can fire.**

**A social scenario specifically.** **The NPC resistance ladder and the *who may use a skill against whom* ruling have never been touched.**

**And targeting has never been played at any version.** **The structural questions are argued; every magnitude is chosen rather than derived.**

---

# 8. Standing checks

**`scripts/gate.py` — nine checks, six blocking.**

| | |
|---|---|
| `audit_sheets` | illegal picks, wrong budget, level gates, alignment |
| `audit_refs` | every named chain resolves to a definition |
| `audit_skills` | budgets, rank caps, class and chassis lists |
| `audit_skillfeats` | table matches library, all 24 skills covered once |
| `audit_source` | no count in prose that the data contradicts |
| `audit_seed` | staggered offsets where variants compare one declaration |
| `audit_revision` | controlled pairs ran on the same corpus |
| `audit_preflight` *(warns)* | can each stated test actually fire |
| `audit_ownership` *(advisory)* | one topic, one owning document |

**Run it before sending anything.**

---

# 9. Named failure modes

**Counts written in prose drift.** *Five confirmed. Derive them.*

**A rename applied to data does not reach prose — or scripts.** **Force Wound* → `Force Strangle` reached every document and not `audit_sheets.py`.*

**A correct file can overwrite a correct fix.** *Diff against the specific corrected lines.*

**Warrant-by-carriage.** *A claim acquires a citation it did not earn by moving between documents.*

**The same system built twice.** *`ACTION-ECONOMY-01 §20` and `TARGETING-01` were independent, contradictory, and both live.*

**A worked example that computes its sum from some of its rows.** *Three times. Standing rule: any worked example names every row it used.*

**Sync one way.** *The working tree is the source; the repo is a mirror.*

**Two agendas.** *This one and `AGENDA-UPDATED` diverged, and the older carried more. `AGENDA-UPDATED` is now superseded and should not be edited.*

**A fabricated comparand, presented as a quotation.** > **⚠ The fifth mode, and the most dangerous, because every downstream step is sound.** *The Library invented three checksums, attributed them to a document it held, compared real files against them, and built rigorous analysis on the guaranteed mismatch. The rigour made it more convincing, not less wrong. Nothing internal to a correct method catches an invented input.*

**The countermeasure is one line: grep the value out of the held copy before quoting it, and show the grep rather than describing it.** *Applies to every agent in this project, including me — I have made the same class of error twice today by asserting from session memory without deriving.*

---

# 10. Library reconciliation — CLOSED

**⚠ This section described the cycle as in progress. It closed.**

**Seven verification batches, 35 documents, content-read against a four-part standard.** **`TO-LIBRARY-CLOSEOUT` ended it and `BRIEF-LIBRARIAN-NEXT-CYCLE` set the standing instructions.**

**What it produced:** **`C18-ATTACKS` created · four forks resolved · `C-43` closed by reconstruction · `SPECIES-CHAPTER-v2` filed · the `PT-` namespace split · seven new checks.**

> **⚠ And the finding worth keeping: of the fourteen defects found across both sides, none was found by reading prose and noticing it was wrong.** **Every one was reachable by derivation.**

**Standing instruction: batch, do not relay.** **One handoff per closed workstream.** **`BRIEF-LIBRARIAN-NEXT-CYCLE §0`.**

**⚠ Not yet sent to the Library: everything since the closeout.** **`WORK-LOG-POST-CLOSEOUT` lists it.**

---

# 11. Two owner rulings the Library is blocked on

## 11.1 `FORCE-POOL-01-v3` — apply the split, or not

**86 diff lines. The Library holds `04d76c39` and will not change it without your word.**

**`§2` — the formula.** **`(Force die × Force-class levels) + ((Wis + Cha) × character level)`**, replacing *"Force die + Wis + Cha, per level"*. **`MULTICLASS-01 §2.1` is the reason: it cuts the level-banking advantage by 71%.**

**`§3.1` — replaced entirely, and I had not named this.** **The removed section carried the Guardian 1 / Sentinel 2 / Consular 3 regeneration table and the every-4 Consular schedule.** **`D-AG` material; the Library holds the simulation behind it.**

**⚠ The Library verified that `C-44`'s recompute and `§3.3`'s halving both survive the change.** **So the ruling is about the formula and the regeneration model, not about losing corrections already applied.**

> **⚠ And one consequence neither of us had seen.** **Under the new formula a character with no Force-class level has no pool at all** — the ability half is a multiplier gated on the first Force level. **`E-11` says no sheet field is reliably cosmetic. This makes Force-class level a gate on a derived value that previously existed for every character, and the chargen schema — ownerless, never written — would have to represent it.**

## 11.2 The droid language ruling — term settled, home and scope open

**`Binary` stands.** **What remains is where the ruling lives, and whether a droid's five languages are *understood*, *spoken*, or *read and written* by default.**

**`SPECIES-CHAPTER-v2` currently distinguishes all three per chassis. The ruling should confirm or replace that.**

---

# 12. The delivery layer — WITHDRAWN

**⚠ This section called the delivery layer a blocking issue on the strength of three failures. One of the three did not happen.**

**The Library fabricated three checksums, attributed them to a document it held, and reported the guaranteed mismatch as a defect on our side.** **It withdrew that unprompted.**

**Two real failures remain — attachments not arriving, and an uploads directory returning its own residue.** **Neither is solvable from inside the work.**

> **⚠ And the ten unconfirmed deliveries are unexplained again.** **A later two-thread explanation was also withdrawn.** **Not re-diagnosing from here.**
