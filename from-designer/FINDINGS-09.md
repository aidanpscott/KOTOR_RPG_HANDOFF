# FINDINGS-09 — Jedi Guardian and Jedi Sentinel

**Written while `to-designer/` was empty. Both are writable without the Force documents; the Consular is not, and §4 restates why.**

**⚠ §3 is the largest structural finding since the feat schedule and it is not about the Jedi. It affects six classes and one pregen is wrong because of it.**

---

# 1 — The Jedi Guardian

## 1.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Combat** | **Authored.** `PT-77` by implication, recorded in `PT-84`. *`jgd_reg` derives 16, which is Middle* |
| **Hit die** | **d10** | **Ported.** `k2_classes.2da` row 3 |
| **Force die** | **4** | **Ported.** `forcedie 4` — the smallest of the three |
| **Primary ability** | **Strength** | **Ported.** *The only Force class with a physical primary* |
| **Base attack** | **Full** | **Ported.** *Informative here — K1 also gave it `CLS_ATK_1` where it gave the Sentinel and Consular `CLS_ATK_2`* |
| **Saves** | **12 / 12 / 9** — Fort strong, Reflex strong, **Will on the third progression** | **Derived.** `cls_st_jedi_g.2da` |
| **Skill base** | **3** | **Authored.** `PT-78` |
| **Class skills** | **6** — Alertness · Athletics · Awareness · Mysticism · Persuade · Medicine | **Authored.** `PT-81` cut `Intimidate` |
| **Feats at 30** | **20** | **Authored.** `PT-84`. *Derived is 16* |
| **Attack picks at 30** | **36**, `T` = 40 | **Derived** |
| **Chains entered** | **18** | **Authored**, adopted `REPLY-08` |
| **Powers known** | **2 at 1st, `Jedi levels + 1` thereafter — 9 at 8, 31 at 30** | **Derived.** `classpowergain.2da`, `jgd` |
| **Recommended opening** | `Sarlacc Sweep` | **Authored** |
| **Restricted chain** | `Force Jump` → Advanced → Mastery, at 1 / 6 / 12 | **Ported.** `jgd_granted` |

## 1.2 The class feature already exists and it is the right one

**`Force Jump` is granted at 1 / 6 / 12 and is catalogued.** **I was asked for what the class does that no other class can and the answer is already in the library — as with the Smuggler, I have nothing better and would not manufacture something to sit beside it.**

**It is the only thing in the corpus that closes distance.** **In a system where one declaration ends your turn — `ATTACKS-01 §2` — a melee character who spends a round walking has spent the round. `Force Jump` is the Guardian not spending it.**

**⚠ One clause in it is inert as written.** **`FEATS-LIBRARY-01`:** *"Counts as an ambush against an unengaged opponent — the `Sneak Attack` dice apply if you hold them."*

**Derived: `Sneak Attack` is granted to `scd`, `sas` and `jwa` only. A Guardian never holds it.** **The clause can only fire on a multiclass character who took Smuggler, Sith Assassin or Jedi Watchman levels — and `jwa` is the Guardian's own prestige line, so it is not idle, but it is doing nothing for the base class at any level.**

**Not a defect. Worth a note in the entry saying so, or a reader will look for the dice and not find them.**

## 1.3 What is missing is the second half of `Sarlacc Sweep`'s job

**`CLASS-ATTACKS-01 §4` gives the reasoning for the opening as *"the blade first. A crowd answer at 1st level."*** **That is right and it is a credit spend, not a class feature.**

**The Guardian's derived shape is: the largest hit die of the three, the smallest Force die, Strength primary, full BAB, and 11 capstones at `N` = 18.** **It is the Jedi who solves problems with the blade and carries the Force as a reserve.**

> **`Force Jump` gets him there. Nothing gets him out.**

**I considered proposing a disengagement chain and decided against it.** **`Guarded Step` already punishes an enemy for flanking, `Parry` is a melee reaction chain in `ATTACKS-05`, and adding a third movement mechanic to the class that already owns the only one would be piling onto a strength rather than answering a weakness.** **Recording the considered no, per `REPLY-07`'s own standard.**

---

# 2 — The Jedi Sentinel

## 2.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Middle** | **Derived.** `jsn_reg` gives 15 at 30 |
| **Hit die** | **d8** | **Ported** |
| **Force die** | **6** | **Ported** |
| **Primary ability** | **Dexterity** | **Ported** |
| **Saves** | **12 / 12 / 9** — **identical to the Guardian's** | **Derived.** `cls_st_jedi_s.2da` |
| **Skill base** | **5** | **Authored.** `PT-78` |
| **Class skills** | **9** — Acrobatics · Alertness · Awareness · Slicing · Mysticism · Security · Stealth · Streetwise · Medicine | **Authored.** `PT-79` |
| **Feats at 30** | **15** | **Derived** |
| **Attack picks at 30** | **27**, `T` = 31 | **Derived** |
| **Chains entered** | **13** | **Authored**, adopted `REPLY-08` |
| **Powers known** | **identical to the Guardian — 9 at 8, 31 at 30** | **Derived.** `classpowergain.2da`, `jsn` |
| **Recommended opening** | `Deflecting Slash` | **Authored** |
| **Restricted chain** | `Force Immunity: Fear` → Stun → Paralysis, at 1 / 6 / 12 | **Ported.** `jsn_granted` |

**⚠ The Sentinel and the Guardian have identical save progressions and identical power progressions.** **The classes separate on hit die, Force die, skill base, feat rate, chain count and skill list — six axes — and on nothing defensive or Force-economic.** **`PT-54.1`'s worry that the two were the same class was narrower than it looked but not baseless.**

## 2.2 ⚠ The immunity ladder is the strongest defensive package in the class system, and it may be free

**`FEATS-LIBRARY-01`, tier 2, at level 6:** *"Immune to Force Push, Force Wave, Stun, Critical Strike and Sniper Shot stuns, Concussion Grenades, Flash mines, On-Hit: Stun."*

**Priced against the corpus's own statement of what a stun is worth.** **`ATTACKS-01 §12.3`:** *"A stun prevents the target's next full turn… Refresh is the load-bearing clause. Without it a Precision build cannot lock a target, and with it, it can."*

**In a system with one declaration per round, denying a turn is the most valuable effect there is.** **A Combat character's turn is about 27 damage at level 8 — `PREGENS-01 §5.1`, Korr's `Barrage`.**

> **From 6th level the Sentinel is immune to every stun in the game, from every source, with no save.** **Enemy Precision chains do nothing to it. `Force Push` and `Force Wave` do nothing to it.**

**And it stacks with a strong Fortitude — `PT-8` puts weapon stuns on Fortitude and `PREGENS-01 §9` puts `Force Stasis` there too, so the Sentinel is immune to a category it would already have saved against.**

**⚠ Compare what other classes pay for far less.** **`Read the Ground` costs the Scout three feats and gives one ally a *chance* at half damage from one narrow category. `Force Immunity` gives the Sentinel total immunity to the category that matters most.**

**Whether that is a problem turns entirely on §3.**

---

# 3 — ⚠ The corpus never says whether a class's restricted chain is granted or bought

**This is the finding and it is not about the Jedi.**

**`feat.2da` carries a level in the `_granted` column for every class-restricted chain in the game:**

    Scout        TARGETING_1..8        sct_granted  1, 5, 9, 13, 17, 21, 25, 29
                 UNCANNY_DODGE_1, 2    sct_granted  4, 7
                 EVASION               sct_granted  6
    Guardian     FORCE_JUMP  x3        jgd_granted  1, 6, 12
    Sentinel     FORCE_IMMUNITY x3     jsn_granted  1, 6, 12
    Consular     FORCE_FOCUS x3        jcn_granted  1, 6, 12
    all Force    JEDI_DEFENSE          9 columns    1
    all Force    UNARMED_SPECIALIST I–VIII          2, 6, 10, 14, 18, 22, 26, 30

**`FEATS-LIBRARY-01` files all of them in `§5 Restricted — by class or chassis`, which is the section for feats a class *may take*.** **`ACTION-ECONOMY-01 §18.1` says grants cost nothing.** **Nothing states which of the two applies to these.**

## 3.1 The two readings differ enormously

**If bought:** **the Sentinel spends 3 of its 15 lifetime feats on immunity — 20% — which is a real price and the §2.2 concern mostly dissolves.** **The Scout spends 8 feats on `Targeting`, which is impossible: it has 16 total and the ladder would be half its career.**

**If granted:** **`Targeting 8` is `+8` to attack with blasters, free, by level 29.** **`Weapon Focus` is `+1` for a feat, so the ladder is worth eight feats and costs none.** **It is the largest single modifier in the game and no document mentions it outside the library entry.**

> **⚠ The library's own wording says granted — *"Granted at level 1"*, *"granted at levels 5, 9, 13…"* — and `feat.2da` agrees. So the Scout gets `+8` attack free and the Sentinel gets blanket stun immunity free.**

## 3.2 And one pregen is already wrong because of it

**`PREGENS-01`, Vess, Scout 8:** *"Attack: `+6` BAB, `+4` Dex, `+1` Weapon Focus, `−1` Volley = `+10`."*

**Derived: `TARGETING_2` is granted at Scout level 5 and is `+2` attack with blasters. Vess is level 8 and carries a blaster rifle.**

> **Her attack should be `+12`, not `+10`. The sheet omits a class feature the library says she is granted.**

**⚠ And it moves the finding `PREGENS-01 §5.1` is built on.** **Vess at `Volley of Bolts`, three shots against Defence 19, was 8.1 a round against Korr's 27.3 — the 3.4× melee-versus-ranged gap the scenarios exist to measure.** **At `+12` her hit rate rises from 60% to 70% and the round becomes 9.45, closing the gap to 2.9×.**

**That does not overturn the finding. It changes the number the finding is stated in, and three scenarios are reported against it.**

## 3.3 What I would rule, and it is not mine

**Granted, as the source and the library both say — with `Targeting` repriced.**

**`Targeting` is the outlier, not the principle.** **`Force Jump`, `Force Immunity`, `Force Focus` and `Uncanny Dodge` are all three-tier chains on the 1 / 6 / 12 ladder and giving them free is what makes a class feel like itself from 1st level.** **An eight-tier ladder reaching `+8` is a different kind of object and the source's own Jedi equivalents stop at three.**

**⚠ If it stays as printed, the Scout at level 29 has `+8` attack that no other class can approach, and the class already holds the best saves in the game.**

---

# 4 — The Consular, and what it still needs

**Unchanged from `FINDINGS-08 §3`.** **Its feature is `Force Focus`, whose effect is a Force-power-effectiveness multiplier pending string rows `1257 / 1259 / 1260`.**

**⚠ And the derivation below is why it cannot be estimated around.**

    powers known at 30      Guardian 31    Sentinel 31    Consular 41
    Force die               Guardian  4    Sentinel  6    Consular  8

**Derived from `classpowergain.2da` and `k2_classes.2da`.** **The Consular knows ten more powers than either other Jedi and carries twice the Guardian's Force die.** **A multiplier on power effectiveness applied to that base is a different object from the same multiplier applied to the Guardian's, and I cannot price it without `POWER-COSTS-01` and `FORCE-POWERS-01`.**

**Needed: `FORCE-POOL-01-v3`, `POWER-COSTS-01`, `FORCE-POWERS-01`.**

---

# 5 — Two smaller ports, both uncatalogued

**The unarmed ladder.** **`COMPLEX_UNARMED_ANIMS` at 1st and `UNARMED_SPECIALIST_I`–`VIII` at 2, 6, 10, 14, 18, 22, 26, 30 are granted to **all nine Force class columns** — the three Jedi, the three Sith, and the three Jedi prestige classes.** **`FEATS-LIBRARY-01` files `Unarmed Specialist` under **Restricted — owner unassigned** with *"Granted at level 2"* and does not say to whom.** **It is every Force class, and it is the mechanical basis for a Jedi who fights without a weapon — which `ATTACKS-07`'s Echani chain and the Handmaiden both assume.**

**`Jedi Defense`.** **Granted at 1st to all nine Force columns, and also filed under **owner unassigned**.** **`PT-1` already ruled it costs a reaction, so the mechanic is settled; only its ownership is not written down.**

> **⚠ Both are the `Force Focus` pattern again: real source content, correct in the library, filed as belonging to nobody.** **That bucket now holds three things I have found that have known owners. It is worth a pass of its own rather than one entry at a time.**

---

# The question

> **Nothing blocking. Guardian and Sentinel are complete; the Consular waits on the three Force documents.**

**The decision I most want is `§3` — granted or bought — because it changes six classes, and `§3.2` says one pregen and one measured scenario result move with it.**
