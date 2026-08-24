# FINDINGS-26 — the six ported prestige classes

**`REPLY-25` asked which way *"grants nothing"* breaks before I write the first one. `§1` answers it and the answer is that it does not break.**

**`§2` is a finding that arrived while checking entry levels and it changes what an entry requirement is *for*.**

---

# 1 — `CLASS-ATTACKS-01 §5` is about credits, not feats, and it is already right

**`§5` reads:** *"Prestige classes. Grants nothing. Picks continue from the character's rate."*

**`jwm` has 23 grants in `feat.2da`, `jwa` 25, `sma` 24. That looks like a flat contradiction and it is not.**

**Derived — the counts are inflated by the package every Force class carries:**

| Class | Grants | **Distinctive** | The rest |
|---|---|---|---|
| **Jedi Weaponmaster** | 23 | **7** | weapon and armour proficiencies · `Force Sensitive` · `Jedi Defense` · the Sense tier · `Unarmed Specialist` I–VIII · `Complex Unarmed Anims` |
| **Jedi Watchman** | 25 | **7** | same |
| **Sith Marauder** | 24 | **6** | same |
| **Jedi Master** | 17 | **2** | same |
| **Sith Lord** | 17 | **2** | same |
| **Tech Specialist** | 5 | **0** | five proficiencies and nothing else |

**⚠ And `§5` sits directly under `§4`, which is the *attack credit* table. It is scoped to that section.**

> **`§5` means: a prestige class gives no attack credits at 1st level. It does not mean a prestige class grants no feats.**

**That reading is the only one consistent with the rest of the corpus.** **`PT-89` gives every class four attack credits at 1st level; if a prestige class gave four more, entering one would double a budget the whole chain-count system is built on.** **And `REPLY-10` ruled that restricted chains *are* granted — so `Deflect` and `Inner Strength` are granted, because they are the Weaponmaster's restricted chains.**

**⚠ No rules change needed. One clause of scope needed, because *"grants nothing"* against a column of 23 will be read as a contradiction by the next person who checks.**

**Proposed: *"Grants no attack credits. Restricted feat chains are granted as for any class — `REPLY-10`."***

---

# 2 — ⚠ Splitting into a prestige class beats staying pure, on feats

**Found while checking what entry level to require. `FEAT-SCHEDULE-01` rules that prestige feat columns read from their own class level, so a split character reads **both** columns from row 1.**

**Derived, cumulated over `k2_featgain.2da`:**

    pure Guardian 30                   16 feats
    Guardian 8  / Weaponmaster 22      17
    Guardian 12 / Weaponmaster 18      17
    Guardian 15 / Weaponmaster 15      18   <- optimum
    Guardian 20 / Weaponmaster 10      17
    Guardian 25 / Weaponmaster  5      18   <- also optimum

    pure Consular 30                   11
    Consular 15 / Jedi Master 15       12

> **⚠ Every split beats staying pure, and an even split beats it by two.**

**It is small — 18 against 16 is 12.5% — and it is not the banking exploit `MULTICLASS-01` was built to kill, because it costs nothing to set up and gains little.** **But it is real, it is in the direction that rewards multiclassing, and `MULTICLASS-01 §4` states the opposite intent:** *"Ours charges you slowly, forever. A splitter is continuously behind."*

**On feats, a prestige splitter is continuously *ahead*.**

## 2.1 What it means for entry requirements

**⚠ The source's own entry level was 15. Our optimum is 15.**

> **A requirement set at 15 hands the player the optimal split as the minimum legal one.**

**Three ways to respond and I recommend the third:**

**Fix the schedule** — make prestige columns read from character level. **⚠ No. `FEAT-SCHEDULE-01` closed that deliberately and every prestige feat total in the corpus depends on it.**

**Set entry above 15** so the optimum is not the floor. **⚠ No. It compresses the prestige career into fewer levels than the class needs and 25/5 is also an optimum.**

**Set entry *below* 15 and accept the two feats.** **Entry at 10 means a player who wants the optimum still has to choose it at 15 rather than being handed it, and a player who enters at 10 takes 17 rather than 18.** **The gap stays 12.5% at worst, which is inside the noise of a single class feature, and nothing has to be reopened.**

**⚠ Recorded rather than solved. It is an owner call and it is small.**

---

# 3 — The six, on `PT-138`'s grammar

**Requirements are a minimum character level plus one to three holdings. Entry level 10 throughout, per `§2.1`.**

**⚠ Every requirement below names something the character must *already have been doing*. None is a tax.**

## 3.1 Jedi Weaponmaster

    d10 · Force die 6 · Strength · 16 feats · Middle · saves 12/12/9

**Skills, 4 ported:** Demolitions · Awareness · Persuade · Medicine
**Granted:** `Deflect` · `Inner Strength` I–III · `Increase Melee Damage` I–III

> **Entry: character level 10, Jedi Guardian 6, and `Weapon Focus: Lightsaber`.**

**The Guardian requirement is the class — this is where a Guardian goes.** **`Weapon Focus: Lightsaber` is the cheapest possible statement that you have been using the weapon, and the base Jedi are granted the proficiency but not the Focus, so it is a real purchase.**

**⚠ `Deflect` is the only granted chain in either game that no other class receives.** *The Jedi answer to a blaster; the Sith are given none — `PT-129`.*

## 3.2 Sith Marauder

    d10 · Force die 6 · Strength · 16 feats · Middle · saves 12/12/9

**Skills, 4 ported:** Demolitions · Awareness · Persuade · **Intimidate** *(`PT-131`, `Medicine` → `Intimidate` on the Sith side)*
**Granted:** `Ignore Pain` I–III · `Increase Combat Damage` I–III

> **Entry: character level 10, Sith Warrior 6, and `Weapon Focus: Lightsaber`.**

**The Weaponmaster's mirror, and the pair is the clearest illustration of `PT-129` in the game.** **`Inner Strength` and `Ignore Pain` are the same −5/−10/−15%; `Increase Melee Damage` is melee only and `Increase Combat Damage` covers ranged as well; and the Marauder gets no `Deflect`.**

## 3.3 Jedi Watchman

    d8 · Force die 8 · Dexterity · 15 feats · Middle · saves 12/12/9

**Skills, 6 ported:** Slicing · Stealth · Awareness · Persuade · Security · Medicine
**Granted:** `Sneak Attack` 1d6–7d6 at 1, 4, 7, 10, 13, 16, 19

> **Entry: character level 10, Jedi Sentinel 6, and `Stealth` 8 ranks.**

**⚠ `Stealth` 8 is the one requirement that is a real gate rather than a formality.** **`Sneak Attack` requires `Stealth` 5 to hold at all and caps its dice at ranks ÷ 3, so a Watchman who enters without ranks receives a chain that does nothing.**

**⚠ And this is the third of the three `Sneak Attack` classes.** **`PT-122` set them at three speeds — Smuggler every odd from 1 to 10d6, Watchman every third to 7d6, Sith Assassin every second from 5 to 9d6.** **The Watchman is the slowest and the shallowest and that is correct: it is the only one of the three that is not built on the opening strike.**

## 3.4 Jedi Master

    d6 · Force die 10 · Wisdom · 11 feats · Specialist · saves 12/9/12

**Skills, 4 ported:** Awareness · Persuade · Repair · Medicine
**Granted:** `Regenerate Force Points` · `Light Side Enlightenment`

> **Entry: character level 10, Jedi Consular 6, and `Mysticism` 8 ranks.**

**⚠ `Repair` is a genuine oddity and it is the source's.** **`PT-79` already ruled on the same anomaly for the Consular — *"`Repair` is a deliberate departure from source. K2's Consular is a tinkerer; ours is a scholar"* — and cut it there.** **Cutting it here too would be consistent; keeping it would make the Jedi Master the only Jedi who fixes things. I would cut it and replace with `Mysticism`, and I am flagging rather than doing it because `PT-79` was an owner ruling on the parent class.**

## 3.5 Sith Lord

    d6 · Force die 10 · Wisdom · 11 feats · Specialist · saves 12/9/12

**Skills, 4 ported:** Awareness · Persuade · Repair · **Intimidate**
**Granted:** `Regenerate Force Points` · `Dark Side Corruption`

> **Entry: character level 10, Sith Inquisitor 6, and `Mysticism` 8 ranks.**

**The Jedi Master's mirror, and `Light Side Enlightenment` / `Dark Side Corruption` are the same mechanic pointed in opposite directions — both shift companion alignment.**

**⚠ Both classes break `PT-129`.** **`Regenerate Force Points` is unconditional on the Jedi Master and the two alignment chains are unconditional on both.** **`PT-129` is a rule about *base* classes — the Jedi three each have a conditional chain and the Sith three have none — and the prestige tier does not follow it.** **Recorded so nobody reads the exception as a refutation.**

## 3.6 Tech Specialist

    d6 · Force die 0 · Dexterity · 11 feats · Specialist · saves — see below

**Skills:** **⚠ a function of the entrant** — `CLASS-ROSTER-01 §6`: *"its skills are whichever of `Engineer` and `Machinist` the entrant is missing."*
**Granted:** **nothing. Five proficiencies and no class feature — the only class in either game with none.**

> **Entry: character level 10, and **Engineer 5 or Machinist 5**.**

**⚠ This class has no numbers of its own and I want that stated plainly rather than buried.**

**`FINDINGS-01 §7`, `FINDINGS-08 §1.2` and `PT-98` between them establish it: `k2_classes.2da` row 9 is identical to the Scoundrel's row on every design column, `tec_reg` is byte-identical to `scd_reg` across all fifty rows, and `tec_class` is byte-identical to the Combat Droid's skill list.**

**Its saves point at `CLS_ST_TECHSPEC`, which is not in holdings — so they are authored on `PT-123` like the other four missing tables. Dexterity primary, one job: **6 / 12 / 6**.**

**⚠ I recommended cutting it in `FINDINGS-01 §7` and `REPLY-09` declined, correctly — a duplicate row is weaker evidence than an original and stronger than a placeholder.** **It survives. But it is the one class in the roster whose entire content is *completing another class*, and it has no feature to write because the source gave it none.**

**If it is to be more than a skill-list transfer it needs an authored chain, and that is a design decision nobody has made.**

---

# 4 — Plain-language lines, per `REPLY-25`

**Asked for and worth having early rather than after.**

**Jedi Weaponmaster** — the Guardian who kept going. Turns blaster fire aside better than anyone alive and hits harder for it.
**Sith Marauder** — the Warrior who kept going. Feels less, hits more, and unlike the Jedi he will use a blaster.
**Jedi Watchman** — the Sentinel who went undercover. The slowest of the three stealth-strikers and the only one not built around the opening.
**Jedi Master** — the Consular who became a teacher. Recovers the Force faster than anyone and pulls the people around her toward the light.
**Sith Lord** — the Inquisitor who took command. The same recovery, and the people around him rot.
**Tech Specialist** — ⚠ the one that completes you. Whichever half of the tech pair you are not, you now are. Nothing else.

---

# The question

> **⚠ Two, and neither blocks the six above.**

**Entry level 10 throughout — or another number, given `§2.1`'s finding that 15 is both the source's answer and the optimal split?**

**And `§3.4` — does `PT-79`'s cut of `Repair` from the Consular extend to the Jedi Master and Sith Lord, which inherit it from the same source?**
