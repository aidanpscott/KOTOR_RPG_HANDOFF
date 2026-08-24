# FINDINGS-10 — the Jedi Consular, and everything still open

**Tenth of ten. §3 is the ranked register you asked for.**

**⚠ §1.4 says which pool branch I priced against, and §2 is why that mattered more than expected.**

---

# 1 — The Jedi Consular

## 1.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Specialist** | **Derived.** `jcn_reg` over `k2_featgain.2da` gives 11 at 30 |
| **Hit die** | **d6** | **Ported.** `k2_classes.2da` row 4 |
| **Force die** | **8** | **Ported.** *Twice the Guardian's* |
| **Primary ability** | **Wisdom** | **Ported** |
| **Base attack** | **Full** | **Ported**, uninformative — `PT-72` |
| **Saves** | **12 / 9 / 12** — Fort strong, **Reflex on the third progression**, Will strong | **Derived.** `cls_st_jedi_c.2da` |
| **Skill base** | **4** | **Authored.** `PT-78` |
| **Class skills** | **8** — Alertness · Archaeology · Awareness · Mysticism · Persuade · Medicine · Science · Xenology | **Authored.** `PT-79` |
| **Feats at 30** | **11** | **Derived** |
| **Attack picks at 30** | **18**, `T` = 22 | **Derived** |
| **Chains entered** | **13** | **Authored**, adopted `REPLY-08`. **4 capstones — the fewest in the game** |
| **Powers known** | **2 · 6 · 11 · 17 · 27 · 41** at levels 1 / 4 / 8 / 12 / 20 / 30 | **Derived.** `classpowergain.2da`, `jcn` |
| **Recommended opening** | `Saber Pierce` | **Authored** |
| **Restricted chain** | `Force Focus` → Advanced → Mastery, granted 1 / 6 / 12, gated 1 / 4 / 8 | **Ported.** `jcn_granted` |

**⚠ Note the save shape. The Consular is the mirror of the Guardian and Sentinel, not a weaker version** — they carry the third progression on Will, she carries it on Reflex. **All three total 33. The Consular is the only Jedi with a strong Will.**

## 1.2 What the class is, in numbers

    powers known at 30     Guardian 31   Sentinel 31   Consular 41
    Force die              Guardian  4   Sentinel  6   Consular  8
    attack capstones       Guardian 11   Sentinel  9   Consular  4
    feats at 30            Guardian 20   Sentinel 15   Consular 11

> **She knows ten more powers than either other Jedi, carries twice the Guardian's die, and has a third of its attack depth.**

**And `ATTACKS-01 §2.2` states the constraint that makes those numbers mean something:** *"A Guardian who declares Force Lightning has declared their attack that round. They do not also swing… they are paying the round."* **`§12.7` adds that the Consular is *"the intended zero case"* — `+0` in both reaction measures, no reactions at all.**

**So the Consular's scarce resource is not the pool. It is the round.** **Forty-one powers, one declaration, no reactions.**

## 1.3 What `Force Focus` should do

**The chain is granted at 1 / 6 / 12 and its effect is pending on string rows `1257 / 1259 / 1260`, which are not in holdings.** **The only description available is the cut siblings' — `FEATS-LIBRARY-01` on `Force Channel (Alter)` and `(Control)`: *"increase the effectiveness of Force Armour, Force Valor, Force Speed and similar."* Secondary, and marked so.**

> **Every power that description names is a sustained buff. None is a damage power.**

**That is the design signal and it points at the bottleneck: a buff that lasts twice as long is a round you do not spend re-casting it.**

### The proposal — **authored, on the source's own description**

| Tier | Gate | Effect |
|---|---|---|
| **`Force Focus`** | 1 | **Force powers you cast on yourself or a willing ally last half again as long.** |
| › **`Advanced Force Focus`** | 4 | **Twice as long.** |
| ›› **`Master Force Focus`** | 8 | Twice as long, and **powers you have active on others do not end if you are disabled, dying or unconscious.** They run to their normal duration. |

**Priced against the roster I now hold.** **`PARTITION-01 §1`: 102 powers. Sustained self-or-ally buffs are a minority of them** — on Meris's own eleven-power sheet, `Force Aura`, `Force Valor` and `Battle Meditation` qualify and eight do not. **Roughly a quarter of a Consular's list.**

**Not dominant:** **it does nothing for `Force Push`, `Force Stun`, `Heal`, `Throw Lightsaber`, or any of the thirty dark damage powers — every instantaneous effect in the game is untouched.** **It cannot raise a save DC, reduce a cost, or add a target.**

**⚠ And it is deliberately not a second declaration.** **`ATTACKS-01 §3.4` reserves the 1 / 6 / 12 ladder for effects that act outside your turn or permit two declarations, and calls them *"categorically stronger than anything the source has."* `Guided Strike` already occupies that slot and Meris already holds it.** **Giving the Consular a second route to the same thing would make the two stack.**

**The capstone is the moment.** **She goes down and `Battle Meditation` holds. That is the Consular in one line — the one whose contribution outlives her turn — and it costs nothing in any fight she survives.**

## 1.4 ⚠ Which pool branch I priced against

**I priced against `FORCE-POOL-01-v3 §2` as written:** `(Force die × Force-class levels) + ((Wisdom + Charisma) × character level)`.

**It does not matter for a pure Consular — Force levels and character level are the same number — and `Force Focus` touches duration rather than the pool, so the pricing above is branch-independent.**

**It matters for §2 below.**

---

# 2 — ⚠ `FORCE-POOL-01-v3` carries both formulas, in three sections

**Derived by reading the document rather than the change log.**

| Section | Formula |
|---|---|
| **`§2`** | **`(Force die × Force-class levels) + ((Wis + Cha) × character level)`** — the new one |
| **`§4`**, the fatigue table | *"True maximum — Force die + Wis mod + Cha mod, per level. Maximum die at 1st."* — **the old one** |
| **`§6` Decided** | *"Maximum = Force die + Wis mod + Cha mod per level, max die at 1st"* — **the old one** |

**`§2` announces the change and says why. `§4` and `§6` were not updated.**

> **Fourth instance of the `PT-84` shape: a correction applied to the section that states the rule and not to the sections that use it.**

**And `§4` is the section that uses it hardest — the working maximum degrades to a floor of half the *true maximum*, so which formula is live sets both the ceiling and the floor.**

**Derived, Scout 8 / Consular 4, Wisdom + Charisma `+4`:**

    §2   (8 × 4) + (4 × 12)  =  80    floor 40
    §4   12 + (3 × 12)       =  48    floor 24

**A 67% difference in the ceiling and the same in the floor, inside one document.**

**⚠ It is invisible on every pregen and every worked example, because all of them are pure Jedi — where the two formulas coincide exactly.** **`§4`'s own examples are *"a level 5 Guardian"* and *"a level 20 Guardian"*. Nothing in the document exercises the case that separates them, which is why it has survived.**

**This is also what `REPLY-09` and `REPLY-10` were warning me about, and the warning was better than the document.** **The forked text says the fork is unresolved; the document reads as though `§2` settled it. The two sections that disagree are the ones a reader would consult to compute a number.**

---

# 3 — Everything still open, ranked

**Ranked by what each blocks, not by size.**

## Blocking a class that has been written

| | Item | Blocks | State |
|---|---|---|---|
| **1** | **Chassis reading — does a `PT-89` credit carry roster access?** | **Marksman.** Under the restrictive branch the Combat band `14–20` and a droid's 11-chain access have an **empty intersection** — no legal chain count exists at that rate | Owner, `PT-99`. `REPLY-09` flagged it conditional |
| **2** | **`FORCE-POOL-01-v3`'s two formulas** | **Consular**, and every multiclass Force character. 80 against 48 on the same build | **New — §2 above** |
| **3** | **Four classes have unstated saves** | Bounty Hunter *(12/12/6 proposed, adopted)*, Engineer *(6/12/12, adopted)*, Machinist *(6/12/6)*, Marksman *(12/6/6)* | `cls_st_techspec.2da` and `cls_st_cm_drd.2da` are not in holdings; four proposals stay authored |

## Blocking work not yet started

| | Item | Blocks | State |
|---|---|---|---|
| **4** | **The twelve unwritten classes have no save ladder to draw from** | Agent · Explorer · Doctor · Brawler · Duelist · the three Sith · four more | Three progressions exist — **12 / 9 / 6 at level 20** — and no document names them. `FINDINGS-01 §9` |
| **5** | **`Killer's Instinct` and `Squad Tactics` are class-locked and no mechanism defines it** | Every prestige class, and the `Sneak Attack` trio | `CLASS-ATTACKS-01 §6`. **⚠ `REPLY-10` ruled restricted chains are *granted*, which may have closed this by implication — worth confirming** |
| **6** | **Prestige entry requirements — nineteen, none exists** | The whole prestige workstream | `MULTICLASS-01 §6` |
| **7** | **The Machinist's upgrade chain** | The Machinist's larger identity | `CRAFT` and `MASTERCRAFT_WEAPONS/ARMOR_I–III` are seven `feat.2da` rows granted to no class. Needs `EQUIPMENT-01` and the crafting port |

## Recorded, not blocking

| | Item | State |
|---|---|---|
| **8** | **A controlled character's declaration** — is it separate from its controller's? | `Field Override`'s capstone, `Battle Meditation`, the domination powers. `REPLY-08` escalated it |
| **9** | **`Precise Shot I–V`** is on the same granted column as `Targeting` and was not repriced with it | `REPLY-10` flagged it to me; I have not looked |
| **10** | **The tech pair share a failure mode** | `Field Override` and `Jury Rig` both do nothing in a droid-free campaign. `REPLY-09` proposed a machinery mode — doors, turrets, security — and left it to me |
| **11** | **The Smuggler's skill base of 7 sits outside its own band** | `PT-78`, unresolved. Either it drops to 6 or Specialist opens to 3–7 |
| **12** | **`Smuggler's Luck` — faithful restoration or the reroll** | `FINDINGS-07 §1.3`. Three source tiers either way |
| **13** | **The **owner unassigned** bucket has known owners in it** | `Unarmed Specialist` and `Jedi Defense` are granted to all nine Force columns; `Force Focus` was found there too. Worth one pass, not one entry at a time |
| **14** | **`ACTION-ECONOMY-01 §18.2`'s proficiency table has nine rows for ten classes** | The Bounty Hunter is missing |
| **15** | **Surprise is decorative** | `ACTION-ECONOMY-01 §9`: S6 ran four ambushes and surprise changed nothing. Not a class question |
| **16** | **Count disagreements** | Skills 22/23/24 · attack entries 104/107/110 · `SKILL-RESOLUTION-01 §5.5` lists sixteen and says seventeen (the answer is eighteen; `Science` and `Medicine` are missing) |

## Closed this run, for the record

**Chain-count definition · the band, twice · the `watch.py` truncation and its half-rename · `Force Focus` · `Quickdraw` · the droid/organic split · initiative · granted-versus-bought · `Targeting`'s repricing · Vess's missing `+2`.**

---

# 4 — Where the ten stand

| Class | Rate | Chains | Feature | State |
|---|---|---|---|---|
| **Soldier** | Combat | 14 | `Hold the Line` | complete |
| **Jedi Guardian** | Combat | 18 | `Force Jump` *(ported)* | complete |
| **Marksman** | Combat | 14 | `Still Standing` | ⚠ chain count conditional |
| **Bounty Hunter** | Middle | 11 | `Quarry` | complete |
| **Scout** | Middle | 17 | `Read the Ground` | complete |
| **Jedi Sentinel** | Middle | 13 | `Force Immunity` *(ported)* | complete |
| **Engineer** | Middle | 11 | `Field Override` | complete |
| **Smuggler** | Specialist | 8 | `Quickdraw` *(`PT-74`)* | complete |
| **Jedi Consular** | Specialist | 13 | `Force Focus` | complete |
| **Machinist** | Specialist | 10 | `Jury Rig` | ⚠ second feature pending `EQUIPMENT-01` |

**Three features were already in the corpus and needed finding rather than inventing** — `Force Jump`, `Force Immunity`, `Quickdraw`. **Two implement a rule the corpus stated and never gave anyone** — `Quarry` for taking targets alive, `Jury Rig` for repairing a droid other than yourself. **Two are derived from a single ported number** — `Still Standing` from the `d12` and Constitution primary, `Read the Ground` from 12 / 12 / 12.

---

# The question

> **Nothing blocking. Ten of ten are written.**

**The two decisions that would close the most: the chassis reading, which is the only thing making a printed chain count conditional, and `FORCE-POOL-01-v3`'s duplicate formulas, which is new and sits in a document six others depend on.**
