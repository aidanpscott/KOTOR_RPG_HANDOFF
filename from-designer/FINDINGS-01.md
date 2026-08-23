# CLASS-DESIGNER-FINDINGS-01 — first pass

**Read: eleven project documents, twenty `2da` tables. Everything below is derived at the point of assertion. Authored, ported and derived are marked.**

---

## The question

> **Does a class's chain count mean chains it can *finish*, or chains it may *hold*?**

**`MULTICLASS-01 §5` and the player-facing text both compute it as picks ÷ 3 — Soldier 36 → 12, 30 → 10, 27 → 9. `PT-69` treats it as something two classes at the same pick budget can differ on. Those are different quantities under one word, and §4 of this document shows the band does not survive either reading unchanged.**

**Nothing else in here blocks me. I can proceed on everything while this is open, except the chain counts themselves.**

---

# 1 — `FEAT-SCHEDULE-01` holds three values for the Guardian and two for the Marksman

**Derived: cumulated `jgd_reg` and `drc_reg`, `k2_featgain.2da`, rows 1–30.**

| | L20 | L30 |
|---|---|---|
| **`jgd`** | **11** | **16** |
| **`drc`** | **7** | **11** |

**What the document prints:**

| | header table | Totals table | the 30-row grid | the verification line |
|---|---|---|---|---|
| **Guardian L30** | **20** | 16 | 16 | — |
| **Guardian L20** | **14** | 11 | 11 | **11** |
| **Marksman L30** | **18** | **18** | 11 | — |
| **Marksman L20** | **14** | **14** | 7 | — |

**Both departures are legitimate and on record.** `PT-77` authored the Marksman's 18; `PT-84` authored the Guardian's 20. **Neither reached the grid.**

> **⚠ So neither authored total has a curve.**

**The Guardian needs four more grants across thirty levels than its column produces. The Marksman needs seven.** **No row of the grid was changed, so the only level-by-level schedule in the corpus still emits 16 and 11.**

**Which is what every sheet is built from.** **Aelin holds 5 feats at Guardian 8 — the grid's value. HK-24 holds 3 at Marksman 6 — the grid's value.** **Neither sheet is wrong; there is no other schedule to build them from.**

**Two more things in the same document.** **The header carries `Source: featgain.2da, KOTOR 2` over two numbers that are not from it.** **And the line *"Verified: the six stated totals at level 20 all reconcile against the rows… Guardian 11"* sits four lines above a table that says 14.**

**`PT-84` was the sweep written to catch exactly this and it corrected one cell of one table, then reported the item closed.**

---

# 2 — Three rate assignments are stale, in four places

**Current owner intent, assembled from `PT-57` → `PT-68` → `PT-77` → `PT-84`:**

| Rate | Classes |
|---|---|
| **Combat** | **Soldier · Jedi Guardian · Marksman** |
| **Middle** | **Bounty Hunter · Scout · Jedi Sentinel · Weaponmaster · Marauder · Watchman · Engineer** |
| **Specialist** | **Smuggler · Jedi Consular · Machinist · Jedi Master · Sith Lord · Sith Assassin** |

**`CLASS-ATTACKS-01 §2`'s table is correct and current. The prose around it is not.**

**`ATTACKS-01 §11.6`** still prints `PT-57`'s three corrections verbatim — *Guardian moved from Combat to Middle · Marksman moved to Specialist · Combat is now a two-class tier.* **All three superseded.**

**`CLASS-ATTACKS-01 §2.2a`** says *"⚠ The Marksman is Specialist, not Combat"* — **in the same section whose table puts it in Combat.**

**`CLASS-ATTACKS-01 §2.1`**, headed *"Scout and Guardian share a rate"*, is retained in full **above a table that separates them**, and its argument — *"charging it a second time through attack picks would double-count"* — is now the live case against its own table. **`PT-77` overturned `PT-54.2` and never withdrew it.**

**`PREGENS-01 §7`** still lists the Engineer's attack rate as unassigned. **`PT-57` assigned it Middle.**

**The sheets follow the table, not the prose** — Aelin 10 picks at 8, the Dark Jedi 8 at 6, HK-24 8 at 6, all Combat. **Nothing needs rebuilding. Four passages need striking.**

---

# 3 — The Bounty Hunter's skill row does not follow the formula

**`SKILLS-01 §9.1`. Formula: `(base + Int mod) × 4` at 1st, `base + Int mod` after. At Int 12 every row checks but one.**

| Bounty Hunter, base 4 | L1 | L5 | L10 | L20 | L30 |
|---|---|---|---|---|---|
| **Printed** | 16 | 52 | 92 | 132 | 165 |
| **Derived** | **20** | **40** | **65** | **115** | 165 |

**The printed row is the Soldier's — 16 / 32 / 52 / 92 / 132 — with the L5 cell dropped, shifted left, and 165 appended.** **Consular, Marksman and Engineer are also base 4 and print 20 / 40 / 65 / 115 / 165 correctly, so the right row is already in the table three times.**

**Same section, two more.** *"A Soldier ends with 99 career points at level 30 and a Smuggler with 264."* **99 is base 3 at Intelligence 10. 264 is base 7 at Intelligence 12. The table says 132.** Two assumptions in one sentence.

**And:** *"**`Smuggler` is ours entirely and is set at 6** — below the Smuggler it resembles, above the Scout."* **The Smuggler is base 7 four lines above. This is the Machinist.** It is `PT-56`'s own wording carried through the `PT-73` rename.

**`PT-84` names this defect class** — *"`PT-73`'s Smuggler rename produced duplicate dictionary keys"* — **and two instances survived the sweep. Here is the second:**

> **⚠ `CLASS-ATTACKS-01 §4` has two `Smuggler` rows. Eleven rows for ten classes.**

**One is the Scoundrel's grants correctly renamed — `Precise Shot` · `Sneak Attack`, which matches `scd_granted` in `feat.2da`.** **The other — `Snap Shot` · `Point Blank Shot`, *"ours to define and this is the definition"* — is the pre-merge Smuggler's and now belongs to no class.** **Hold that row; §7 wants it.**

---

# 4 — The chain band is arithmetically empty

**A chain is three tiers. Grants cost no pick (`PT-57`, `ACTION-ECONOMY-01 §18.1`), so they add free tiers. No class in `CLASS-ATTACKS-01 §4` has more than two granted chains.**

| Rate | Picks | + max grants | **Chains completable** | **Band top** | Tiers the top needs |
|---|---|---|---|---|---|
| **Combat** | 36 | 2 | **12** | 13 | **39** |
| **Middle** | 27 | 2 | **9** | 10 | **30** |
| **Specialist** | 18 | 2 | **6** | 7 | **21** |

> **⚠ The top of every band is unreachable by every class in the game.**

**Reaching it would take three granted tier-1s in three separate chains. Nothing has three.**

**The Guardian is assigned 13.** That is two above what its budget buys.
**The Marksman is assigned 11**, the floor, which leaves four tiers it cannot spend inside its own count.
**The Soldier is entered as "12–13"** — a range, in the column that was meant to replace the range.

**Under the completions reading the band collapses to a single value per rate — 12 / 9 / 6 — and there is nothing for a class to choose.** **Under the access reading it is a roster restriction, and `CLASS-ATTACKS-01 §6` says the restriction mechanism does not exist:** *"`Killer's Instinct` and `Squad Tactics` are class-locked and nothing defines the mechanism."*

**That is the question at the top. It is the only thing in the class workstream I cannot start without.**

---

# 5 — `SKILLS-01 §9.3` is a K1 read overturning a K2 fact, and `PT-54.1` rests on it

**§9.3 reads:** *"The Jedi Sentinel has three class skills in the source, not six… **Verified against `skills.2da`: `jsn_class` marks exactly the same three rows as `jgd_class`.** The six-skill list belongs to the Consular. **Both documents need correcting.**"*

**True of `skills.2da`. False of `k2_skills.2da`. Derived from both:**

| | K1 | K2 |
|---|---|---|
| **Guardian** | Awareness · Persuade · TreatInjury — **3** | + Demolitions — **4** |
| **Sentinel** | the identical 3 | ComputerUse · Stealth · Awareness · Persuade · Security · TreatInjury — **6** |
| **Consular** | **6** | Awareness · Persuade · Repair · TreatInjury — **4** |

**`PT-55` rules K2 the source for class data.** **`PT-79` did the K2 read and got exactly this.** **Neither withdrew §9.3, and it still instructs two documents to be corrected toward the K1 value.**

**It matters because `PT-54.1` — the ruling that keeps the Sentinel in the game — cites it:** *"The class skill list was the Guardian's, exactly. Points were the only thing distinguishing them."* **In K2 they were never identical.**

**And the Sentinel's own K2 six are Slicing, Stealth and Security** — **the three that `SKILLS-01 §9.4` then re-authors as a judgement call:** *"Security, Stealth, and Streetwise make them the one who hunts dark siders rather than duels them — which is what the class is for and what the source never expressed mechanically."*

> **The source expressed it. In the other game.**

**The Sentinel should survive. The warrant needs replacing** — the present one is a target error of the kind `PT-65` names, right file and wrong game, and it is load-bearing for a class's existence.

---

# 6 — `feat.2da` grants a three-tier chain to the Consular and no document holds it

**Derived from `feat.2da`, `jcn_granted`:**

    FORCE_FOCUS            granted at  1    no level gate
    FORCE_FOCUS_ADVANCED   granted at  6    mincharlevel 4
    FORCE_FOCUS_MASTERY    granted at 12    mincharlevel 8

**`usetype` blank — passive, so a feat rather than an attack. Gate ladder 1 / 4 / 8, which is `ATTACKS-01 §3.4`'s base ladder.**

**Grepped across all eleven documents: `Force Focus` — zero hits.**

**What `FEATS-LIBRARY-01` does hold is `Force Channel (Alter)` and `Force Channel (Control)`, marked *"Reinstated from cut content… Secondary source,"* filed under **Restricted — owner unassigned**.** **Those are `XXXX_FORCE_FOCUS_ALTER` and `XXXX_FORCE_FOCUS_CONTROL` — the cut rows.**

> **⚠ The two cut rows were reinstated and the live shipped chain was never catalogued.**

**This is the Consular's missing identity.** **`FEATS-LIBRARY-01` gives the Guardian one restricted chain (`Force Jump`, granted 1 / 6 / 12 ✓) and the Sentinel one (`Force Immunity`, granted 1 / 6 / 12 ✓) and the Consular none.** **The source assigns it a chain on the identical schedule, and we have it filed as unassigned cut content.**

**Two more of the same shape:**

**`POWER_BLAST` → `IMPROVED_POWER_BLAST` (4) → `MASTER_POWER_BLAST` (8).** `usetype` 1 — ranged active. **Granted to `sol` at 1st level *alongside* `POWER_ATTACK`.** Zero hits in the documents. **`CLASS-ATTACKS-01 §4` quotes *"the source grants Power Attack by name"* and gives the Soldier no ranged grant; the source gave it both.** *I cannot tell whether `ATTACKS-04` renamed it — `Charged Shot` is the obvious candidate — because I do not hold `ATTACKS-04`.*

**`SCOUNDRELS_LUCK` is three tiers in `feat.2da`, all granted to `scd`.** **`FEATS-LIBRARY-01`'s `Smuggler's Luck` is one.** **A three-tier chain was collapsed to a single tier, and it is the one asset the prestige Scoundrel could have kept.**

---

# 7 — Classes that should not exist

## Tech Specialist

**Derived, `k2_classes.2da` row 9 against row 2:**

    Scoundrel        hitdie 6  CLS_ATK_1  base 4  10/16/10/12/14/14  DEX  forcedie 0
    TechSpecialist   hitdie 6  CLS_ATK_1  base 4  10/16/10/12/14/14  DEX  forcedie 0

**Identical on every design column.**
**`tec_reg` is byte-identical to `scd_reg` across all fifty rows of `k2_featgain.2da`.**
**`tec_class` is byte-identical to `drc_class` — the Combat Droid's list — in `k2_skills.2da`.**
**`tec_granted` in `feat.2da` is five proficiencies and nothing else.** *It is the only class in either game with no granted class feature.*

**`PT-68` rejected `BountyHunter(CUT!!!)` because *"a cut row pointing at another class's tables is a placeholder, not a design."*** **The Tech Specialist's row copies the Scoundrel, its skill column copies the Combat Droid, and the same argument has never been put to it.**

**It is also the roster's one class whose skill list is a function of the entrant.** **That is a rule, not an identity.** **Cut it, or give it the thing the source declined to.**

## Scoundrel

**The brief names it. What I can add is the size of the hole.**

**`scd_granted`: `Critical Strike` at 1, `Sniper Shot` at 1, `Scoundrel's Luck` at 1, and `Sneak Attack` 1d6 → 10d6 at every odd level from 1 to 19.** **`PT-73` gave the Smuggler all of it, and `Scoundrel's Luck` went too — renamed `Smuggler's Luck` and cut to one tier.**

> **The class has been stripped of its numbers, its feats, and the name of its own signature feat. There is nothing left to write an entry requirement *for*.**

**If it survives, the unowned grant row from §3 is what it should be** — `Snap Shot` · `Point Blank Shot`, *close, fast, and gone.* **That is the pre-merge Smuggler's identity, it is the only unclaimed one in the corpus, and it is a genuinely different class from the Scoundrel-Smuggler that absorbed it: the close-range pistol duellist rather than the sneak.** **Otherwise cut it and let the Smuggler have the whole lane.**

---

# 8 — The pair that is about to be the tech pair again

**Derived: `feat.2da` grants the `Sneak Attack` ladder to exactly three classes — `scd`, `sas`, `jwa`.**

| | Ladder | Cap |
|---|---|---|
| **Smuggler** *(`scd`)* | 1, 3, 5, 7 … 19 | **10d6** |
| **Sith Assassin** *(`sas`)* | **1, 3, 5, 7 … 19 — byte-identical** | **10d6** |
| **Jedi Watchman** *(`jwa`)* | 1, 4, 7, 10, 13, 16, 19 | 7d6 |

**`FEATS-LIBRARY-01`'s `Killer's Instinct` note already says *"granted to the three classes that carried Sneak Attack in the source"* — without naming them, and while filing the feat under `## Smuggler`.** **These are the three.**

> **⚠ The Sith Assassin is not thematically near the Smuggler. It is granted the identical mechanic on the identical schedule.**

**And it is the class `CLASS-ROSTER-01` just promoted from prestige to base with *"feat total 10 exists; everything else is new."*** **That is where the 89% overlap recurs, and it is cheap to prevent before the class is written rather than after.**

**The Watchman is the source's own answer and the shape to copy: same mechanic, slower ladder, lower cap.** **Three classes can carry stealth damage if they carry it at three speeds.**

**One more, not the same problem but worth knowing before it is designed.** **Gunslinger and Sharpshooter have no source signal at all.** **`WEAPON_PROF_BLASTER` and `WEAPON_PROF_BLASTER_RIFLE` are both in the universal set; `sol`, `sct`, `scd`, `drc` and `tec` are granted both, `drx` and the three Jedi blaster only. No class in either game is built around one and denied the other.** **The pistol/rifle line is entirely ours, and the only hook that exists for it is the proficiency ladder everyone can already buy. Something will have to be authored; nothing can be ported.**

---

# 9 — Two things the source answers that we have not asked it

## The Jolee slot is in RCR, not in the games

**`forcedie` is nonzero on exactly six rows of `k2_classes.2da` — the three Jedi and their three prestige classes.** **The games have no non-institutional Force user either, so `CLASS-ROSTER-01 §7`'s hole cannot be filled by porting.**

**But `PT-54.1` records the answer in passing:** *"the Force-using base classes there are Force Adept, Jedi Consular, and Jedi Guardian."*

> **RCR — the mechanical foundation — already ships a Force base class that belongs to no order.** **It was cited as evidence that the Sentinel is an import, and then dropped.**

**That is the slot, and it is in the governing rulebook rather than in the games, which is why looking at the `2da` set never found it.**

## What a Soldier does that a Scout cannot — the source has a blunt answer, and it is not damage

**Derived, `cls_st_*` at level 20:**

| Class | Fort | Ref | Will | **Total** |
|---|---|---|---|---|
| **Soldier** | 12 | 6 | 6 | **24** |
| **Smuggler** *(`scndrl`)* | 6 | 12 | 6 | **24** |
| **Guardian · Sentinel** | 12 | 12 | 9 | **33** |
| **Consular** | 12 | 9 | 12 | **33** |
| **Scout** | **12** | **12** | **12** | **36** |

> **⚠ The Scout has three strong saves. It is the most durable character in the game against everything that is not a weapon, by twelve points over the Soldier.**

**That is a full +4 on every save at 20 and it has never been stated anywhere in the corpus. It is most of the answer to the brief's headline question, and it comes from a file nobody had opened.**

**And a third progression exists that no document names.** **Strong reaches 12 at 20, weak reaches 6, and a middle one reaches 9** — Guardian and Sentinel Will, Consular Reflex, roughly two points per five levels. **Aelin's Will `+7` is correct because of it: base 4, Wisdom +2, `Conditioning` +1.**

**Twelve new classes need save progressions and there is no published ladder to assign from. It should be written down before the classes are, not after.**

---

# 10 — Smaller, and grouped

**Counts that disagree with themselves.** **Skills are 22 (`SKILLS-01 §1` heading), 23 (`SKILLS-01 §11.2`, `FEATS-LIBRARY-01`'s `Skill Focus`, `SKILL-RESOLUTION-01`'s dependency line) and 24 (`SKILLS-01 §12`, the brief, and the table itself). The table has 24.** **`ATTACKS-05` is 11 chains in `ATTACKS-01 §4` and 14 in `FEATS-LIBRARY-01`'s header.** **Attack entries total 104 by summing the three rosters, 107 in `FEATS-LIBRARY-01` and 110 in `ATTACKS-01 §11.4` — and *"107 of 110 cost you your declaration"* counts three reaction chains as three entries where they are nine.**

**`SKILL-RESOLUTION-01 §5.5`** says seventeen skills have no resource dimension and lists sixteen. **The answer is eighteen; `Science` and `Medicine` are the two missing from the list.**

**`SKILLS-01 §9.5`** counts the Machinist's list at nine with six Intelligence keys. **`§9.2` gives eight, of which four are Intelligence.** **Its proposed fix offers `Sleight of Hand`, which the class already holds.** **The defect underneath is real and slightly worse than stated: at Intelligence 16 the Machinist has 36 points at 1st level against 8 skills × 4 maximum ranks = 32, so four points have nowhere to go.**

**`MULTICLASS-01`.** **`§2.2b`'s powers column contradicts `§2.2a`'s own rule.** `classpowergain.2da` gives `jgd` 2 at Jedi level 1 and +1 after, so powers = Jedi levels + 1: **Guardian 4 → 5, 7 → 8, 11 → 12.** The table prints 8, 10, 13. **And the *"levels spent at 1"* column reads 7 / 4 / 0 down rows that bank progressively harder — it is upside down, and the sentence beneath it is attached to the route that does not bank.** **60 → 18 is a 70% reduction, not 71%.** **`§3` still prints *"Entry credit applies on first taking any class you do not already hold"* and `§6` still adjudicates collecting it twice; `PT-70` deleted the system — and `§3` is the rules-proper half, so it would ship.** **`§3.3` says three Force classes receive `Force-Sensitive` free. There are six.**

**The droid/organic split is still live in two places.** **`CLASS-ATTACKS-01 §4.1` and `ACTION-ECONOMY-01 §18.2` both call the Marksman and Engineer *"the two droid classes"* and grant them droid plating instead of armour.** **`PT-75` dropped the split.** **As written an organic Marksman is denied `Strike` because *"`ATTACKS-05` closes it to every droid"* and is proficient in plating they cannot wear.** **`§18.2`'s table also has nine rows for ten built classes — the Bounty Hunter is missing, and its one restricted chain is `Weapon Proficiency: Wrist-Mounted`, which under that section's own rule should be granted rather than sold to the class it defines.**

**`PT-77`'s no-orphan check.** *"`Archaeology` and `Xenology` remain on Consular and Marksman."* **The Marksman's list has neither. Both survive on the Consular alone — which is what `SKILLS-01 §5` says the Explorer exists to fix.** The conclusion held; the derivation did not.

**`PREGENS-01` bookkeeping.** **`§1` states the Soldier's skill base as 2 and the Guardian's level-8 feats as 4; the sheets use 3 and 5, which are current.** **HK-24's vitality of 59 is d12 with Constitution +2 across six levels; his sheet says Constitution 17, which gives 65.** **His wounds print 17 while `§8` records a correction to 18.** **Aelin's block says eight powers and six tier-1; the table lists eight of which seven are tier 1, and `§8` says six.** **Meris's header says eleven and its prose says nine; the table lists eleven.** **And `FEATS-LIBRARY-01` still carries `Force Sensitive` at +40 Force points, which `PREGENS-01` records as not adopted and struck from a sheet.**

**Three warrant nits, no numbers affected.** **`CLASS-ATTACKS-01 §2.2a` and `PT-57` and `PT-77` all say the Marksman's 11 is *"the Smuggler's number"*; `drc_reg` is byte-identical to `jcn_reg`, the Consular's. Same total, different column — and `FEAT-SCHEDULE-01`'s own cadence grouping has it right.** **`MULTICLASS-01` cites `cls_spgn_jedi.2da`; the file is `classpowergain.2da`.** **`CLASS-ATTACKS-01 §2.2a` cites `featgain.2da` for a level-30 figure; that file has twenty rows.**

---

# What I want to do next

**Nothing here needs a decision except the chain question.** **Given an answer to it I would take the class workstream in this order:**

**Class features first, not chain counts** — because §6 shows the source has more class-defining content than the corpus holds, and the twelve unwritten classes should be designed against a complete picture of what the eleven built ones actually do.

**Then the save progressions**, which are three named ladders and half a day's work, and which twelve classes need before any of them can be written.

**Then the twelve.**

**Prestige entry requirements last**, because nineteen of them are a mechanical consequence of what the base classes turn out to be, and writing them first would fix the base classes by accident.
