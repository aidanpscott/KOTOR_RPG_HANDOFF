# FINDINGS-05 — Bounty Hunter and Scout

**Two classes in full. One new gap found on the way — the Bounty Hunter has no saving throws, anywhere.**

**⚠ And one line in the fixed `watch.py`: `ls()` reads `to-designer/` and the print stats `from-designer/f`. On your side those agree. On mine they do not, and my next watch would raise `FileNotFoundError` on `REPLY-06.md`. I am running a corrected copy outside the tree.**

---

# 1 — The Bounty Hunter

## 1.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Middle** | **Authored.** `PT-68`, from an authored feat total — see §1.2 |
| **Hit die** | **d10** | **⚠ Authored, and see §1.2** |
| **Base attack** | **Full** | **Authored.** *Carries no information either way — `PT-72`* |
| **Saves** | **— nothing exists —** | **⚠ Gap. §1.3** |
| **Skill base** | **4** | **Authored.** `PT-68` |
| **Class skills** | **9** — Alertness · Athletics · Awareness · Demolitions · Intimidate · Pilot · Scavenging · Stealth · Streetwise | **Authored.** `SKILLS-01 §9.2` |
| **Feats at 30** | **16** | **⚠ Authored.** No `bh` column exists in either `featgain` table |
| **Attack picks at 30** | **27** | **Derived** from the rate |
| **Chains entered** | **10** | **Authored.** `FINDINGS-02 §3` |
| **Grants** | `Rapid Fire` · `Snap Shot` · `Strike` · `Shoot` | **Authored.** `CLASS-ATTACKS-01 §4` |
| **Restricted chain** | `Weapon Proficiency: Wrist-Mounted` → Focus → Specialization | **Ported + authored.** `WEAPON_PROF_WRIST_MOUNTED` is a real `feat.2da` row; the Focus and Specialization tiers are marked authored in `FEATS-LIBRARY-01` |

## 1.2 ⚠ Every number in this class is authored, and two came from a row we rejected

**`PT-68` ruled `BountyHunter(CUT!!!)` *"a placeholder, not a design"* and declined it as evidence. Correctly.**

**But `k2_classes.2da` row 10 reads `hitdie 10`, `CLS_ATK_1`, `featstable SOL`, `savingthrowtable CLS_ST_SOLDIER`, `skillpointbase 1`.** **`PT-68` rejected the row and kept two of its five design values — the d10 and the full BAB — while replacing the other three.**

> **The full BAB is harmless: `PT-72` established the column carries no information, so keeping it asserts nothing.** **The d10 is not harmless. It is the second-highest hit die in the game and its only warrant is a row we ruled inadmissible.**

**I am not proposing to change it.** **d10 is right for the class and `PT-68`'s reasoning stands on its own — full BAB, d10, `Middle` picks, twice the Soldier's skills.** **But the document should say *authored* where it currently reads as ported, because a later reader will find `hitdie 10` in the source and conclude it was derived.**

**The feat total is the same shape.** **16 is the Scout's number, borrowed. There is no Bounty Hunter column to derive from.**

## 1.3 ⚠ New gap — the Bounty Hunter has no saving throws

**Grepped `docs/`: no Bounty Hunter save progression exists in any document.**

**The source row points at `CLS_ST_SOLDIER` — Fort strong, Ref and Will weak, 12 / 6 / 6 at 20.** **That is the placeholder we rejected, so it cannot be ported without reversing `PT-68`.**

**Proposal, authored: Fort strong, Reflex strong, Will weak — 12 / 12 / 6 at 20, total 30.**

**Derived comparison:**

    Scout       12 / 12 / 12  = 36
    Guardian    12 / 12 /  9  = 33
    Bounty Hunter  12 / 12 / 6 = 30   proposed
    Soldier     12 /  6 /  6  = 24
    Smuggler     6 / 12 /  6  = 24

**The reasoning is the class's own case.** **`PT-68` built it as *"hits as often and as hard as a Soldier, carries a Scout's bag of tricks."*** **Fort and Reflex is exactly that split — the Soldier's body and the Scout's feet.** **Will stays weak because nothing in the class is about resolve, and because 33 would put it level with a Jedi.**

**⚠ It sits above the Soldier at 30 to 24.** **That is intentional and it is the price of the Soldier's twelve capstones. If the owner reads it as too much, the lever is Reflex down to the hybrid 9, giving 27.**

## 1.4 What the Bounty Hunter does that no other class can

**`CLASS-ATTACKS-01 §4` already states the intent and nothing implements it:** *"Takes targets alive and moving."*

**Grepped `docs/`: no rule for non-lethal damage, subdual, or capture exists anywhere in the corpus.** **`ATTACKS-01 §12.4` gives the window — 0 wounds is Disabled and a legal target, −1 to −9 is dying, −10 is dead — and nothing lets a player aim for it.**

> **Every bounty in KOTOR is *alive if possible*. The mechanic for it does not exist, and the class named after it is the one that should own it.**

### The proposal — `Quarry`

**A Bounty Hunter-only feat chain, 1 / 4 / 8, in `FEATS-LIBRARY-01 §5`'s existing per-class slot.**

| Tier | | Effect |
|---|---|---|
| **`Quarry`** | 1 | **Name one target you can see. Free, once per encounter.** You know its exact current wounds and vitality. **Your attacks against it may be declared non-lethal at no penalty** — a quarry you reduce to 0 wounds is **Disabled and stable** rather than dying. |
| › **`Run to Ground`** | 4 | As above, and **+2 attack against your quarry**, which gains no benefit from cover against you. |
| ›› **`No Escape`** | 8 | As above at **+4**, and **once per encounter you may spend a reaction to move your full speed toward your quarry** when it moves away from you. |

**Priced against the one thing in the corpus that does the same job.** **`Squad Tactics` is Soldier-only and reaches `+6` against any target an ally is also attacking. `Quarry` reaches `+4` against one named target and costs a naming action.** **Strictly weaker on the attack axis, deliberately — the attack bonus is not what the chain is for.**

**Not dominant:** **it does nothing against a second enemy, nothing in a fight against four troopers, and the capstone spends a reaction from `ATTACKS-01 §10`'s single pool.** **Against a boss it is a flat `+4` for a feat, which is in line.**

**The moment:** **the fight ends with the target on the floor and breathing, and the party decides what to do with them.** **No other class can produce that outcome at all, and it is the single most characteristic thing the fiction asks of this class.**

**⚠ One rule this creates.** **Non-lethal damage does not exist yet. Minimum statement: *a non-lethal attack resolves identically and a target reduced to 0 wounds by it is Disabled and stable rather than dying.* One line, and it only ever applies to a character holding `Quarry`.**

---

# 2 — The Scout

## 2.1 The record

| | | Warrant |
|---|---|---|
| **Rate** | **Middle** | **Derived.** `sct_reg` cumulated over `k2_featgain.2da` rows 1–30 gives 16 |
| **Hit die** | **d8** | **Ported.** `k2_classes.2da` row 1 |
| **Base attack** | **Full** | **Ported**, and uninformative — `PT-72`. *K1 gave it `CLS_ATK_2`; K2 gives everyone `CLS_ATK_1`* |
| **Saves** | **Fort, Reflex and Will all strong — 12 / 12 / 12** | **Derived.** `cls_st_scout.2da`, every row |
| **Skill base** | **5** | **Authored.** `PT-78`. *Source is 3* |
| **Class skills** | **11** — Alertness · Acrobatics · Awareness · Beast Handling · Botany · Slicing · Demolitions · Pilot · Repair · Scavenging · Swim | **Authored.** `SKILLS-01 §9.2` |
| **Feats at 30** | **16** | **Derived** |
| **Attack picks at 30** | **27** | **Derived** |
| **Chains entered** | **13** | **Authored.** The top of `Middle` |
| **Grants** | `Rapid Fire` · `Precise Shot` · `Strike` · `Shoot` | **Ported.** *The source grants `RAPID_SHOT` and the `TARGETING` ladder* |
| **Restricted chains** | `Targeting 1–8` · `Uncanny Dodge 1–2` | **Ported.** `sct_granted`, levels 1/5/9/13/17/21/25/29 and 4/7 |

## 2.2 ⚠ The Scout is the most heavily granted class in the source and we carry a third of it

**Derived, `sct_granted` in `feat.2da`, everything above proficiencies:**

    FLURRY            1        UNCANNY_DODGE_1   4      TARGETING_1..8   1,5,9,13,17,21,25,29
    RAPID_SHOT        1        UNCANNY_DODGE_2   7      PRECISE_SHOT_I..V  4,8,12,16,20
    CLOSE_COMBAT      1        EVASION           6

**Eight distinct grants and two eight-step ladders.** **No other class in either game comes close — the Soldier has three proficiency groups and two attack chains.**

**`FEATS-LIBRARY-01` holds `Targeting` and `Uncanny Dodge`. It does not record that the Scout is granted `Evasion` at 6, `Close Combat` at 1, or `Flurry` at 1.**

> **⚠ `Evasion` is the one that matters. It sits in `FEATS-LIBRARY-01`'s **Organics only** block as a feat anyone may buy — and `SKILLS-01 §12.4` calls it *"the Scout's damage-avoidance feat"* while the library does not restrict it to the Scout or grant it to them.**

**Recommendation, authored: grant `Evasion` to the Scout at 6th level and leave it purchasable by others.** **That matches the source exactly — a grant is not a lock — and it costs nothing to state.**

**`Close Combat` and `Flurry` at 1st level are a harder call and I am not proposing them.** **Both are now attack chains rather than feats, and granting two more would put the Scout at four granted chains and `T` = 31, which breaks the band arithmetic it was assigned under. Recorded so it is not rediscovered.**

## 2.3 What the Scout does that no other class can

**The derivation is one number.** **12 / 12 / 12 at level 20 is 36 save points against the Soldier's 24 and the Jedi's 33.** **It is the largest defensive gap in the class table and it is the only all-strong progression in either game.**

**Add the two grants that scale with it — `Uncanny Dodge` at 4 and 7, `Evasion` at 6 — and the class the source built is not a ranged specialist. It is the one who walks into the room first and comes back out.**

> **The Soldier absorbs. The Scout avoids.** **`Hold the Line` moves damage onto the biggest pool; the Scout's feature should stop it landing at all.**

### The proposal — `Read the Ground`

**Scout-only feat chain, 1 / 4 / 8.**

| Tier | | Effect |
|---|---|---|
| **`Read the Ground`** | 1 | **When you succeed on a Reflex save against an effect with an area, one ally in that area may use your result in place of their own.** Declared after your roll, before theirs. |
| › **`Called It`** | 4 | **Two allies.** |
| ›› **`Nobody Steps On It`** | 8 | **Two allies**, and **when `Evasion` reduces your damage to none, each of them takes half instead of full.** |

**Priced.** **The only area effects on the pregen sheets are grenades — Vess carries two frag. A trooper's grenade against Korr at Reflex `+5` lands about 8 on a failure.** **At tier 1 the Scout converts one ally's failure into a success roughly a third of the time; expected value is under 3 a round and it fires only when someone throws something.**

**Not dominant:** **it does nothing against weapons, which is almost every attack in the game.** **It is a hard counter to one narrow category, which is what a save specialist should be, and `SKILL-RESOLUTION-01 §4.1`'s own argument applies — *two things that fail differently is worth more than one that is simply better*.**

**The moment:** **the grenade lands, the Scout shouts, and the party doesn't die.** **It is the reason you brought a Scout, and it happens two or three times a campaign rather than every round.**

**⚠ Where the other half of the Scout belongs.** **The reconnaissance half — going first, not being surprised — is initiative, and `ACTION-ECONOMY-01 §17` lists *class initiative modifiers* as open and assigned to this workstream, noting *"the Smuggler was to own an initiative feat."*** **The Scout has a better claim than the Smuggler and the two should be settled together rather than one at a time. Flagged, not proposed.**

---

# 3 — Marksman and Engineer, as far as they go

**Both records are complete except the chain count, which waits on the chassis ruling in `REPLY-05`.**

**Marksman:** Combat · d12 *(ported, `k2_classes` `drc`)* · full BAB · **Fort strong** *(`CLS_ST_CM_DRD`, not in holdings — inferred from `PLAYTEST-RULINGS-01 B2`, marked as such)* · skill base 4 *(authored, `PT-77`)* · 8 class skills · **feats 18 authored**, `drc_reg` derives 11 · picks 36 · grants `Power Attack` · `Charged Shot` · `Strike` · `Shoot`.

**Engineer:** Middle · d8 *(ported, `drx`)* · **Reflex strong** *(`PLAYTEST-RULINGS-01 B2`)* · skill base 4 · 7 class skills · feats 16 *(derived, `drx_reg`)* · picks 27 · grants `Covering Fire` · `Strike` · `Shoot`.

**⚠ The Engineer's skill base of 4 is `k1_classes.2da`'s value, not K2's.** **K2 gives `drx` `skillpointbase` 1. `PT-55` rules K2 the source for class data, and `PREGENS-01 §8` calls 4 *"the real `skillpointbase`"* — which is true of the other game.** **The number is probably right; the warrant is K1 and the document says derived.** **Same shape as `SKILLS-01 §9.3`, smaller stakes.**

**Neither has a class feature yet. I would rather write both once the chassis question is answered, because for the Marksman it decides whether the class is a gunline or a heavy, and that is the feature.**

---

# The question

> **Nothing blocking. The chassis ruling in `REPLY-05` is with the owner and it is the only thing outstanding on my side.**

**Bounty Hunter saves are the one new decision above: 12 / 12 / 6 proposed, authored, lever stated.**
