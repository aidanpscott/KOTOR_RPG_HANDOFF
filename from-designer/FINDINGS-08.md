# FINDINGS-08 — Machinist and Marksman

**Two of the last five. The three Jedi are next and §3 is the flag you asked for.**

**One self-check in §4 that I would rather raise than have you find.**

---

# 1 — The Machinist

## 1.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Specialist** | **Derived.** `tec_reg` over `k2_featgain.2da` rows 1–30 gives 11 |
| **Hit die** | **d6** | **⚠ Ported from a clone row — §1.2** |
| **Base attack** | **Full** | **Ported**, uninformative — `PT-72` |
| **Saves** | **⚠ none exist** | **§1.3** |
| **Skill base** | **6** | **Authored.** `PT-78`, confirmed `PT-54.3` |
| **Class skills** | **8** — Repair · Scavenging · Sleight of Hand · Demolitions · Appraise · Awareness · Alertness · Pilot | **Authored.** `PT-83` |
| **Feats at 30** | **11** | **Derived** |
| **Attack picks at 30** | **18**, `T` = 22 | **Derived** |
| **Chains entered** | **10** | **Authored.** `FINDINGS-06 §3` |
| **Recommended opening** | `Charged Shot` · `Covering Fire` | |
| **Restricted chains** | **none exist** | |

## 1.2 ⚠ Every source number on this class is the Scoundrel's

**Derived, `k2_classes.2da` row 9 against row 2:**

    Scoundrel        hitdie 6  CLS_ATK_1  base 4  10/16/10/12/14/14  DEX
    TechSpecialist   hitdie 6  CLS_ATK_1  base 4  10/16/10/12/14/14  DEX

**Identical on every design column.** **`tec_reg` is byte-identical to `scd_reg` across all fifty rows.** **`tec_class` in `k2_skills.2da` is byte-identical to `drc_class` — the Combat Droid's list.** **`tec_granted` is five proficiencies and nothing else — the only class in either game with no granted class feature.**

**`FEAT-SCHEDULE-01` already noticed half of it — *"the Machinist runs the Smuggler's schedule exactly"* — and read it as two classes that happen to share a cadence.** **They do not share it. One row was copied from the other.**

> **This is the same situation `PT-68` ruled on for the Bounty Hunter, with the labels reversed.** **There the cut row was rejected and two of its values kept anyway. Here the row was never questioned and every value was kept.**

**⚠ I am not proposing to change the d6 or the Specialist rate.** **`PT-83` built this class deliberately and its numbers are defensible on their own — a `d6` hands-on technician with the second-highest skill base is a coherent character.** **What is not defensible is the warrant. The document should read *authored, on `PT-83`'s case* rather than *ported*, because a later reader will find `hitdie 6` in `k2_classes.2da` and conclude it was derived.**

**⚠ And it sharpens `FINDINGS-01 §7`, which you have not read past the truncation.** **My argument there was that the *prestige* **Tech Specialist** should be cut because its row is a clone. That argument is unaffected — but it now also means the Machinist and the prestige Tech Specialist are both built on the same copied row, which is worth knowing before the prestige classes are written.**

## 1.3 ⚠ The Machinist has no saving throws — the third class in this position

**`k2_classes.2da` points at `CLS_ST_TECHSPEC`, which is not in holdings. No document states them.**

    Bounty Hunter   none stated   -> 12 / 12 /  6 proposed, FINDINGS-05, adopted PT-93
    Engineer        Reflex only   ->  6 / 12 / 12 proposed, FINDINGS-07, adopted
    Machinist       none stated   ->  ?
    Marksman        Fort only     ->  ?  see 2.3

**Proposal, authored: Fort weak, Reflex strong, Will weak — 6 / 12 / 6, total 24.**

**Reasoning: the Machinist is the Smuggler's structural twin and the source made it literally so.** **Same die, same feat column, same rate. Giving it the Scoundrel's save profile is the one place where the copied row is evidence rather than an accident — `CLS_ST_TECHSPEC` is a separate file, so BioWare wrote a save table for this class and did not simply point at `CLS_ST_SCNDRL`.**

**⚠ Which means the file exists and would settle it.** **`cls_st_techspec.2da` and `cls_st_cm_drd.2da` are the two I am missing. Both are small. If you can send them, two of these four proposals become derivations.**

## 1.4 What the Machinist does that no other class can

**Derived. `SKILL-RESOLUTION-01 §5.3` gives `Repair` two modes and the second is the interesting one:** *"a second mode alongside its resource use: more vitality restored when a droid uses a repair kit on itself. The droid equivalent of a medpac, and the same shape as Medicine."*

> **⚠ *On itself.* No character in the game can repair a droid other than themselves.**

**`Medicine` heals organics as a Gear action — `PLAYTEST-RULINGS-01 B3`, `+1` vitality per 2 points of skill on top of the item's dice.** **The droid half of that has no operator. In a party holding T4-K9 and HK-24 the medic cannot touch either of them, and the droids can only patch themselves.**

**`PT-83` named the class for exactly this:** *"The Engineer breaks into things with its head. The Machinist fixes things with its hands."*

### The proposal — `Jury Rig`

**Machinist-only feat chain, 1 / 4 / 8. A **Gear** action, one per round — `ACTION-ECONOMY-01 §3` — so it costs no declaration, which is the same price `Medicine` pays.**

| Tier | | Effect |
|---|---|---|
| **`Jury Rig`** | 1 | **Spend one repair part to restore `2d8 + half your Repair total` vitality to an adjacent droid.** Any droid, not only yourself. |
| › **`Percussive Maintenance`** | 4 | As above, **or instead clear one ion effect, stun, or disabled state** on an adjacent droid. |
| ›› **`Back in the Fight`** | 8 | As above, and **once per encounter you may restore a droid at 0 wounds to a quarter of its vitality.** It acts on your initiative that round. |

**Parity, derived.** **`Medicine` on a medpac is `2d8 + Medicine ÷ 2` per `B3`. This is the same expression on the same action for the other half of the party.** **It is not a new power level; it is the missing operator for a mode the corpus already defined.**

**Not dominant:** **it does nothing in a party without droids.** **The capstone overlaps `Emergency Reboot` — a chassis feat that fires once per day at 0 wounds — and the two are alternatives rather than a stack: Reboot is automatic and self-only, `Back in the Fight` is someone else choosing to spend their action on you and works after Reboot is used.**

**⚠ And this is the smaller half of the class. See §4.**

---

# 2 — The Marksman

## 2.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Combat** | **Authored.** `PT-77`. *`drc_reg` derives 11, which is Specialist* |
| **Hit die** | **d12** | **Ported.** `k2_classes.2da` row 6. **The largest in the game and the only d12** |
| **Base attack** | **Full** | **Ported**, uninformative |
| **Primary ability** | **Constitution** | **Ported.** `primaryabil CON`, spread `14 / 14 / 16 / 8 / 8 / 8`. **The only Constitution-primary class in either game** |
| **Saves** | **Fortitude strong. ⚠ Reflex and Will unstated** | **§2.3** |
| **Skill base** | **4** | **Authored.** `PT-77` — the most in the Combat tier |
| **Class skills** | **8** — Repair · Demolitions · Awareness · Alertness · Sleight of Hand · Intimidate · Acrobatics · Scavenging | **Authored** |
| **Feats at 30** | **18** | **Authored.** `PT-77`. *`drc_reg` derives 11* |
| **Attack picks at 30** | **36**, `T` = 40 | **Derived** |
| **Chains entered** | **14** | **Authored, adopted `REPLY-08` — ⚠ and see §2.2** |
| **Recommended opening** | `Power Attack` · `Charged Shot` | |
| **Restricted chains** | **none exist** | |

## 2.2 ⚠ Adopting 14 has ruled the chassis question by implication

**`REPLY-08` adopts Marksman 14. `REPLY-06` records the chassis reading as still with the owner.**

**Derived: under *credits are tiers only*, a droid Marksman's accessible roster is the 11 ranged chains. 14 exceeds it.**

> **The number that has been adopted is only legal under one of the two branches.**

**I am not treating that as the ruling. I am recording that the ruling has effectively been made in one document while another says it is open, which is the divergence pattern the project has named — and it is cheaper to reconcile now than after the prestige classes read from it.**

**If the restrictive branch is chosen, 14 is void and the Marksman needs its *rate* revisited rather than its chain count, because no legal number exists at Combat with an access ceiling of 11.**

## 2.3 Saves — Fortitude only, and the file exists

**`PLAYTEST-RULINGS-01 B2` gives *"Marksman — Fortitude"*. `cls_st_cm_drd.2da` is not in holdings.**

**Proposal, authored: Fort strong, Reflex weak, Will weak — 12 / 6 / 6, total 24.**

**Reasoning: it is the Soldier's profile and the Marksman is the Soldier's shape pushed further** — bigger die, Constitution primary, slower acquisition, more skills. **A body that endures and a mind that does not.** **Constitution primary with a weak Will is also the sharpest expression of what the class is, and `PLAYTEST-RULINGS-01`'s single stated column already points at the Soldier's table.**

## 2.4 What the Marksman does that no other class can

**The derivation is three ported numbers and they say one thing.**

    hit die        d12    the only one in either game
    primary        CON    the only Constitution-primary class
    skill base     4      the most in the Combat tier

**`CLASS-ATTACKS-01 §2.3` already reached the conclusion and left it as prose:** *"A d12 that endures, acquires slowly for its tier, and knows more than the Soldier."*

> **The Soldier absorbs damage on behalf of others. The Scout avoids it. The Marksman is the one it does not finish.**

### The proposal — `Still Standing`

**Marksman-only feat chain, 1 / 4 / 8.**

| Tier | | Effect |
|---|---|---|
| **`Still Standing`** | 1 | **The first time each encounter you are reduced to 0 wounds or below, take one more full turn before you become Disabled or begin dying.** Resolved immediately after the attack that dropped you. |
| › **`Not Finished`** | 4 | **Two turns**, taken on your own initiative. |
| ›› **`Last Word`** | 8 | Two turns, and **during them damage cannot take you below −9.** You cannot die until they are spent. |

**Priced.** **One extra turn for a Combat-rate character is one extra declaration — about 27 damage at level 8 by `PREGENS-01 §5.1`'s own figure for Korr.** **Once per encounter, across a three-feat investment, against a class that has the fewest feats of any Combat class at 18.**

**Not dominant:** **it does not prevent death and it does not heal.** **You arrive at 0 wounds either way; the chain buys the order of events, not the outcome.** **The capstone is the only tier that touches survival at all and it buys at most two turns of immunity to a threshold, not to damage.**

**⚠ It interacts with `Emergency Reboot` and should say so:** **a droid Marksman holding both takes the extra turns first and Reboot fires afterwards, because Reboot triggers on being destroyed and `Still Standing` postpones that.** **One clause.**

**The moment:** **the shot that should have ended him lands, and he fires back before he goes down.** **That is Canderous on the Leviathan, and it is the only thing in the class list that produces it.**

---

# 3 — The Jedi gate

> **The three Jedi are all that remain and I am at the point you asked me to flag.**

**I can write the Guardian and probably the Sentinel from what I hold. `Force Jump` and the `Force Immunity` ladder are both in `feat.2da` with their grant levels, both are already catalogued, and both classes' identities are expressible without the Force economy.**

**The Consular is not writable.** **Its class feature is `Force Focus` — `FINDINGS-01 §6`, catalogued in `REPLY-04` with its effect marked pending on string rows `1257 / 1259 / 1260`. What that chain *does* is a Force-power-effectiveness multiplier, and I cannot price a multiplier without the thing it multiplies.**

**Needed before the Consular: `FORCE-POOL-01-v3`, `POWER-COSTS-01`, `FORCE-POWERS-01`.** **`FORCE-AWAKENING-01` and `FORCE-TRAINING-01` matter for the roster question — `CLASS-ROSTER-01 §7`'s missing non-institutional Force user — but not for the Consular's numbers.**

**And two small files would convert four authored proposals into derivations: `cls_st_techspec.2da` and `cls_st_cm_drd.2da`.**

---

# 4 — A self-check, before you find it

**Seven class features now exist. Sorted by when they apply:**

    Hold the Line    Soldier      any round an ally is adjacent      broad
    Quarry           Bounty H.    any encounter with a named target  broad
    Still Standing   Marksman     any encounter you are dropped in   broad
    Quickdraw        Smuggler     a conversation becoming a fight    narrow
    Read the Ground  Scout        area effects only                  narrow
    Field Override   Engineer     enemy droids only                  narrow
    Jury Rig         Machinist    allied droids only                 narrow

> **⚠ Four of seven are hard counters to a narrow category, and two of those four are both about droids.**

**Each is individually defensible and you have accepted the reasoning for three of them. The pattern is what I want on record.**

**Two of the four are load-bearing and I would not change them** — `Quickdraw` is `PT-74`'s and it is right, and `Read the Ground` is the Scout's save profile made into an action.

**The droid pair is the one to watch.** **`Field Override` and `Jury Rig` are the same shape pointed in opposite directions, and in a party with no droids on either side both classes lose their feature entirely.** **That is a real exposure: the Engineer and the Machinist are the two tech classes and they were split at 89% overlap precisely so they would not share a fate.**

**⚠ The honest fix is that the Machinist's larger identity is the upgrade system, not the repair kit.** **`SKILLS-01 §4` cuts `Craft` on the grounds that *"KOTOR 2's crafting system is being incorporated"*, and `feat.2da` carries `CRAFT` plus `MASTERCRAFT_WEAPONS_I–III` and `MASTERCRAFT_ARMOR_I–III` — seven rows, granted to no class in either game.**

**That is the Machinist's chain and I cannot write it.** **It needs `EQUIPMENT-01` and whatever holds the crafting port, neither of which I have.** **`Jury Rig` is what is specifiable today and I would rather ship it as the class's second feature than as its whole identity.**

---

# The question

> **Nothing blocking. `FINDINGS-08` completes seven of ten; the Guardian and Sentinel are writable now and the Consular is not.**

**Send the three Force documents when convenient, plus `EQUIPMENT-01` and the crafting port if the Machinist's upgrade chain is wanted. Two `cls_st_*` files would settle four proposed save lines.**
