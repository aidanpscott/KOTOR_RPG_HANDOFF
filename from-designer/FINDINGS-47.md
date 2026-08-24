# FINDINGS-47 — five owner rulings, and two of them reach systems that do not exist

**⚠ `§3` is the one to read first. The Force-form ruling has no content behind it.**

---

# 1 — `Superior Two-Weapon Fighting` extends to the Gunslinger

**Holders: `Jedi Weaponmaster`, `Sith Marauder`, `Gunslinger`.**

**⚠ I had proposed `Shadow Hunter` as a fourth and the owner named only the Gunslinger. Not adding it.**

**And `ACTION-ECONOMY-01 §7.2`'s *never zero* still needs its exception clause — three classes reach zero now instead of two.**

# 2 — `Repair` cut from the Sith Lord, kept on the Jedi Master

**⚠ This reverses the direction of `PT-79` and I think deliberately.**

**`PT-79` cut `Repair` from the `Jedi Consular` — *"K2's Consular is a tinkerer; ours is a scholar."*** **The `Jedi Master` continues the Consular and now keeps the skill the parent lost.**

> **Which reads: the Order's scholars do not tinker, and the one who has been at it longest does.**

**The Sith Lord's list needs a replacement. Proposed `Mysticism`** — it is his entry requirement at 8 ranks and the only Force class that would not otherwise hold it as a class skill.

    Jedi Master   Awareness · Persuade · Repair · Medicine
    Sith Lord     Awareness · Persuade · Mysticism · Intimidate

---

# 3 — ⚠ Force forms do not exist in this project

**Owner: *"entering a prestige class grants either a lightsaber form or, for Jedi Master and Sith Lord, a **Force form**. Watchman or Marauder gives a choice between the two."***

**Derived, before building on it:**

    feat.2da            245 rows, K2 (has jwm_ and tec_ columns)
    rows with FORM      0
    rows for Shii-Cho, Makashi, Soresu, Ataru, Shien, Niman, Juyo    0
    rows for Potency, Affinity, Mastery                              0
    ATTACKS-06          "Seven forms" — LIGHTSABER only. And: "Lore from
                        Wookieepedia, source_rank 3. MECHANICS AUTHORED."

> **⚠ The seven lightsaber forms are authored, not ported. And there is no Force-form system anywhere in the corpus — not a document, not a feat row, not a mention.**

**KOTOR 2 does have them. Our holdings do not, and `ATTACKS-06` covers the lightsaber side alone.**

## 3.1 What the ruling needs before it can be applied

**The lightsaber half works today.** **`FINDINGS-32 §3` already sets acquisition and this adds a third route: a form on prestige entry.**

**⚠ The Force half is a system that has to be built first.** **Roughly what it would need:**

    how many forms          K2 has four — Focus, Potency, Affinity, Mastery
    what each does          nothing exists; all authored
    exclusion group         one active at a time, as lightsaber forms are
    who grants them         this ruling, plus base-class grants to match FINDINGS-32
    what they cost          a feat, as lightsaber forms do

**That is a `FORCE-FORMS-01` document and it is not a class-workstream deliverable — it is the same shape as `ATTACKS-06`.**

**⚠ I can draft it if it is assigned. I am not drafting it inside a class record, because the last two times something was built beside a missing system — the Pirate's dogfighting and the Sharpshooter's range — the class had to be revisited when the system arrived.**

## 3.2 What I have applied

**Lightsaber forms on prestige entry, for the six martial Force prestige classes.** **`Jedi Master` and `Sith Lord` are marked *pending `FORCE-FORMS-01`*, and `Watchman` and `Marauder` get the choice the ruling describes once there are two things to choose between.**

**⚠ This reverses `FINDINGS-32 §3.4`, where I recommended no form on prestige entry.** **My argument was that the Battlemaster is already the class about holding more forms and granting one would pay it twice. The owner has ruled otherwise and the reversal is recorded rather than argued.**

---

# 4 — The Sith Warrior at `+46%` — is it a problem?

**Short answer: no, and the reason is that the number is a peak rather than an average.**

**It fires only below half vitality. Across a whole fight a Warrior is above half for the early rounds and below it for the late ones, so the realised increase is roughly half the headline.**

    below half, three strikes    39.9 a round     +46%
    across a typical fight       ~33              ~+20%

**⚠ The thing to watch is not the damage. It is the incentive.** **A capstone that pays for being hurt rewards a player for not disengaging, and `DEATH-AND-DIFFICULTY-01` governs what happens when that goes wrong.**

**That is the class working as designed — `FINDINGS-22` built it as the inversion of `Ignore Pain`, which answers being hurt defensively. But it should be adopted knowing it encourages the Warrior to stay in.**

**Keep `+2 / +4 / +6`.**

---

# 5 — An unarmed Velocity chain, and ⚠ a problem underneath it

## 5.1 The chain — `Combination`, for `ATTACKS-07`

**Gated on `Unarmed Specialist IV`, which in practice means the Brawler and the Force classes.**

| Tier | | Effect |
|---|---|---|
| **`Combination`** | 1 | **Strike twice unarmed.** The second strike gains `+2` if the first hit. **Attack −3, Defence −2.** |
| › **`Chain Punch`** | 4 | **Three strikes**, each `+2` if the previous hit. **Attack −2, Defence −1.** |
| ›› **`Rain of Blows`** | 8 | **Three strikes**, each `+2` if the previous hit, and **if all three hit, the target is `Slowed`** until the end of its next turn. |

**⚠ Deliberately not `Flurry` renamed.** **`Flurry` buys back accuracy across its tiers and keeps volume flat. This starts at two strikes and escalates *within the round* — a hit makes the next easier — which is what a boxer does and what a swordsman does not.**

## 5.2 ⚠ And it cannot be priced, because the unarmed ladder outdamages every weapon

**Derived, `ATTACKS-07` against `baseitems.2da` at level 30:**

    unarmed, Unarmed Specialist VIII   8d4   20.0 average
    Lightsaber                         2d8    9.0
    Vibro Double-Blade                 2d8    9.0
    Vibrosword                         2d6    7.0

> **⚠ Unarmed dice are 2.9× a vibrosword at the top of the ladder.** **Three unarmed strikes would be 60 a round before Strength, against Korr's Barrage at 27.3.**

**⚠ This is not created by my chain. It is the ladder, and it is already in the game.**

**A level-30 Brawler punching once already beats a level-30 swordsman swinging once, by a factor of three on the dice — and the Brawler's own capstone ignores armour on top.**

**Two readings and neither is mine to pick:**

**The ladder is the point** — unarmed has no upgrades, no crystals, no reach and no threat range above `20`, so the dice compensate. **⚠ Then a three-strike unarmed chain is unaffordable and `Combination` should cap at two strikes.**

**The ladder is overpriced** — 8d4 was set against a game whose weapons also scaled, and ours do not. **⚠ Then the ladder wants revisiting and `Combination` is fine as written.**

**I recommend the second, and I am flagging rather than acting because `ATTACKS-07` is not mine and the ladder is ported from `feat.2da` rather than authored.**

---

# 6 — The five chain counts, as asked

    Jedi Watchman     12 chains,  9 capstones   Middle
    Sith Marauder     11         10             Middle
    Jedi Master       11          5             Specialist
    Sith Lord         11          5             Specialist
    Tech Specialist    8          7             Specialist

**All inside band, none stranding — `FINDINGS-42`, adopted as `PT-174`.**

---

# The question

> **⚠ `§3` — `FORCE-FORMS-01` does not exist and the ruling needs it. Assign it to me, or to whoever holds `ATTACKS-06`?**

**And `§5.2` — unarmed dice are 2.9× a vibrosword at level 30. That is in the game today, with or without my chain.**
