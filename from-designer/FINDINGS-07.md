# FINDINGS-07 — Smuggler, Engineer, and initiative closed

**Chain counts were re-derived in `FINDINGS-06`, pushed before `REPLY-07` was written. Smuggler 8, Engineer 11 conditional. Not repeated here.**

**One new defect of the same family as `Force Focus`: a ruling that never reached the library.**

---

# 1 — The Smuggler

## 1.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Specialist** | **Derived.** `scd_reg` over `k2_featgain.2da` rows 1–30 gives 11 |
| **Hit die** | **d6** | **Ported.** `k2_classes.2da` row 2 |
| **Base attack** | **Full** | **Ported**, uninformative. *K1 gave `CLS_ATK_2`; K2 gives everyone `CLS_ATK_1` — `PT-72`* |
| **Saves** | **Fort weak, Reflex strong, Will weak — 6 / 12 / 6** | **Derived.** `cls_st_scndrl.2da` |
| **Skill base** | **7** | **Authored.** ⚠ `PT-78` records it as outside its own band — Specialist is 3–6 — and unresolved |
| **Class skills** | **11** — Alertness · Appraise · Awareness · Slicing · Demolitions · Persuade · Pilot · Security · Sleight of Hand · Stealth · Streetwise | **Authored** |
| **Feats at 30** | **11** | **Derived** |
| **Attack picks at 30** | **18**, `T` = 22 | **Derived** |
| **Chains entered** | **8** | **Authored.** `FINDINGS-06 §3` |
| **Recommended opening** | `Precise Shot` · `Sneak Attack`\* | *\*a feat rider, not a credit — `PT-29`* |
| **Restricted chains** | `Killer's Instinct` · `Smuggler's Luck` · **`Quickdraw`** | **See §1.2** |

**Source grants, derived from `scd_granted`:** `CRITICAL_STRIKE` 1 · `SNIPER_SHOT` 1 · `SCOUNDRELS_LUCK` 1 · `SNEAK_ATTACK_1D6`–`10D6` at every odd level 1–19 · light armour and three weapon proficiencies.

## 1.2 ⚠ `Quickdraw` was ruled and never reached the library

**Grepped: `Quickdraw` appears in `PLAYTEST-RULINGS-01` and in no other document.**

**`PT-74` is explicit — *"A `Smuggler` class feat"* — and gives it in full: one attack, once per encounter, when someone you can see turns hostile.** **`FEATS-LIBRARY-01`'s Smuggler section holds two chains and this is not one of them.**

> **Same family as `Force Focus`: the decision was made, the reasoning was written down, and the document a reader consults does not have it.**

**⚠ And it is the Smuggler's class feature.** **I was asked for *what the class does that no other class can* and the answer already exists — it was ruled in `PT-74`, argued from Han and Greedo, and correctly rejected a flat initiative bonus in favour of a conditional one. I have nothing better to propose and would not try.**

**The action is to write it into `FEATS-LIBRARY-01 §5` under `## Smuggler`, single tier, with `PT-74`'s condition intact.**

## 1.3 `Smuggler's Luck` is one tier and the source has three

**Derived, `feat.2da`:**

    SCOUNDRELS_LUCK            scd_granted 1   successor 105
    IMPROVED_SCOUNDRELS_LUCK   prereq 104      successor 106
    MASTER_SCOUNDRELS_LUCK     prereq 104

**`FEATS-LIBRARY-01` line 245 carries one tier: `Defence +2 + (2 × [(level+1)/6])` in combat.**

**Two things to decide and they are separable.**

**The correction:** **restore the missing two tiers. That is a straight port and needs no argument.**

**The question:** **what the three tiers should do.** **As printed it is a flat Defence bonus that scales on its own — a passive the player never interacts with.** **By the standing constraint that is a mechanic which is balanced and produces no recognisable moment, and the class it belongs to is the one whose whole character is *getting away with it*.**

**Proposal, authored — reshape the chain into a spendable reroll:**

| Tier | | Effect |
|---|---|---|
| **`Smuggler's Luck`** | 1 | **Once per encounter, after a d20 is rolled and before it resolves, reroll it.** Yours, or one made against you. **Take the second result.** |
| › **`Long Odds`** | 4 | **Twice per encounter.** |
| ›› **`Never Tell Me the Odds`** | 8 | **Twice per encounter, and one of them may be given to an ally.** |

**Priced.** **A reroll of a failed d20 is worth roughly `+3` to `+4` on that roll, once or twice a fight.** **`Conditioning` gives `+1` to every save permanently for one feat; this is a larger effect on far fewer rolls.**

**Not dominant:** **it changes one die. It cannot be stacked, it does not scale with level, and the capstone's third use is spent on somebody else.**

**⚠ It is a departure from source on flavour and I am flagging it as one.** **The faithful option is to restore three tiers of the Defence bonus, which is one line and no argument. I am proposing the reroll because the Defence version is exactly the failure mode the constraint names, and because *"never tell me the odds"* is the only place in this class where the mechanic and the fiction are the same sentence.**

---

# 2 — The Engineer

## 2.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Middle** | **Derived.** `drx_reg` gives 16 at 30 |
| **Hit die** | **d8** | **Ported.** `k2_classes.2da` row 7 |
| **Base attack** | **Full** | **Ported**, uninformative |
| **Saves** | **Reflex strong. ⚠ Fortitude and Will unstated** | **§2.2** |
| **Skill base** | **4** | **Authored.** `PT-94` — K2 gives `drx` 1; 4 is K1's |
| **Class skills** | **7** — Slicing · Security · Science · Appraise · Awareness · Alertness · Pilot | **Authored.** `PT-83` |
| **Feats at 30** | **16** | **Derived** |
| **Attack picks at 30** | **27**, `T` = 31 | **Derived** |
| **Chains entered** | **11** *(the floor)* | **Authored, conditional** — `FINDINGS-06 §4` |
| **Recommended opening** | `Covering Fire` | |
| **Restricted chains** | **none exist** | **§2.3** |

**Source grants, derived from `drx_granted`:** `WEAPON_PROF_BLASTER` 1 · `BLASTER_INTEGRATION` 1 · `LOGIC_UPGRADE_COMBAT` 1 · `DROID_INTERFACE` 1 · `DROID_UPGRADE` 1 / 7 / 13.

## 2.2 ⚠ The Engineer's other two saves do not exist

**`PLAYTEST-RULINGS-01 B2` gives *"Engineer — Reflex"* and nothing else. `cls_st_ex_drd.2da` is not in holdings.**

**Same gap as the Bounty Hunter's, one column narrower. `PREGENS-01` builds T4-K9 at Fort `+2` and Will `+6`, which is weak / weak at level 8 — so the sheet assumes 6 / 12 / 6, total 24.**

**Proposal, authored: Fort weak, Reflex strong, Will strong — 6 / 12 / 12, total 30.**

**Reasoning: the Engineer is the Smuggler's structural twin on the other side of the mental stats.** **Both are `d8`-or-under support classes with strong Reflex; the Smuggler's case is nerve and the Engineer's is a mind that does not stop working under pressure.** **A strong Will is also the only defensive thing that distinguishes it from the Machinist, which is otherwise the same character with hands.**

**⚠ Against it: this contradicts the pregen, which would move from 24 to 30 and gain `+6` Will at level 20.** **If the owner prefers the sheet, 6 / 12 / 6 is the alternative and the Engineer becomes the third class at 24 alongside the Soldier and the Smuggler.** **Either is defensible; what is not defensible is leaving two of three columns unstated in a shipped class.**

## 2.3 What the Engineer does that no other class can

**Three derived facts point one way.**

**One — the source grants it `DROID_INTERFACE` at 1st level and grants that to no other class.** *`FEATS-LIBRARY-01` files it under **All droids — the chassis**, which is where the source puts it too — but `drx` is the only class column that carries it.*

**Two — `Slicing`, `Security` and `Science` are its own three skills under `PT-83`, and `Slicing` is the Engineer's alone among non-Jedi.**

**Three — `SKILL-RESOLUTION-01` already rules the case and nothing implements it:** *"a slicer takes control of an enemy droid mid-fight. All of it runs."* **It is listed as permitted between NPCs and forbidden against a player-controlled character, which is a complete permission structure for an ability that does not exist.**

> **The corpus has granted the Engineer the interface, the skill, and the ruling that it works. It has never given anyone a way to do it.**

### The proposal — `Field Override`

**Engineer-only feat chain, 1 / 4 / 8.**

| Tier | | Effect |
|---|---|---|
| **`Field Override`** | 1 | **Declare it in place of an attack.** Opposed `Slicing` against an enemy droid's **Will save**, within 20 m and in line of sight. **On a success it loses its next turn.** You make no attack this round. |
| › **`Subverted`** | 4 | On a success it instead **takes one action of your choosing on your initiative**, that turn only. |
| ›› **`Turned`** | 8 | As above, and it **remains under your control** until it takes damage from your party, you use the chain again, or the encounter ends. **One droid at a time.** |

**Uses only machinery that exists.** **The declaration economy — `ATTACKS-01 §2`. Opposed rolls against a save — `SKILL-RESOLUTION-01 §6`, which already pairs `Intimidate` with Will. The player-protection rule — the same section, which already forbids slicing a player-controlled droid.**

**Priced.** **The Engineer gives up the least of any class when it gives up its attack: `Covering Fire` and no ability modifier on ranged damage — `EQUIPMENT-01 §1`.** **That is deliberate. The class that cannot fight gets something to do instead of fighting badly.**

**Not dominant:** **it does nothing against organics, which is most of the game.** **Against a droid encounter it is decisive, which is the same shape as `Read the Ground` — a hard counter to one narrow category — and `SKILL-RESOLUTION-01 §4.1`'s own argument covers it: *two things that fail differently is worth more than one that is simply better.***

**⚠ The capstone needs a ceiling and I have given it one.** **Without *"one droid at a time"*, an Engineer in a droid-heavy encounter accumulates a second party. With it, the strongest case is turning the single most dangerous machine on the field — which is the moment, and it is HK-47 on Tatooine.**

**⚠ One thing I have not resolved.** **A turned droid acting on the Engineer's initiative gets a declaration of its own, and `ATTACKS-01 §2` gives each character one per round. I read that as the droid's, not the Engineer's, but nothing states whether a controlled character's declaration is separate. One line, and it is the same question `Battle Meditation` and the domination powers will raise.**

---

# 3 — Initiative, and I recommend closing it as answered

**`ACTION-ECONOMY-01 §9` and `§17` both carry *class initiative modifiers* as open, with the note *"the Smuggler was to own an initiative feat."***

> **`PT-74` already answered it, and answered it by refusing.**

**Its reasoning, which I would not improve on:** *"A flat initiative bonus is a different feat and every class wants it."* **`Quickdraw` was written specifically to be the conditional version — useless in an ambush, useless at range, useless against something that was always going to attack you.**

**Recommendation, authored: no class modifies initiative. Close `§17`'s line and strike the reservation in `§9`.**

**Three supports:**

**The Smuggler's slot is filled** — `PT-74`, and by a feat that deliberately is not an initiative bonus.

**The Scout does not need one.** **Its claim was never speed, it was not being ambushed — and `§9` already resolves surprise as the ambusher's `Stealth` against *the better of* the defender's `Awareness` or `Alertness`.** **Both are Scout class skills, and no other class holds both with eleven class skills to fund them.** **The Scout is already the hardest party member to surprise, by a rule that exists, with no new mechanic.**

**And a class initiative modifier fails the standing constraint on its face.** **`+2` to a once-per-encounter roll produces no moment anyone describes afterwards, and every class would want it, which is the definition of a bonus that says nothing about who you are.**

**⚠ What this leaves genuinely open is `§9`'s own finding, and it is not a class question:** **S6 ran four ambushes and surprise changed nothing in any of them.** **That is a surprise-rule problem, not an initiative-modifier problem, and it belongs to whoever owns `ACTION-ECONOMY-01`.**

---

# The question

> **Nothing blocking. The chassis reading remains with the owner; `FINDINGS-06 §4` shows one branch leaves the Marksman with no legal chain count.**

**Four small decisions open on my side: the Bounty Hunter's saves, the Engineer's saves, whether `Smuggler's Luck` is restored faithfully or reshaped, and whether the bands widen to 6.**
