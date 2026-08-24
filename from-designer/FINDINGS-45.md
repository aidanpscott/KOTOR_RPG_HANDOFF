# FINDINGS-45 — ⚠ I grepped as instructed and found something worse than the phrasing

**`REPLY-40`:** *"Any feature that widens threat says `×N` and never *by one*. ⚠ Worth grepping your own drafts for the phrase."*

**Two hits, both mine, both already handled. But `×N` on a class feature raises a question the phrasing was hiding.**

---

# 1 — The grep

    FINDINGS-29 §4.3   Commando, Master Chosen Weapon    "widens by one"   -> ×2, PT-175
    FINDINGS-38 §1.3   Sharpshooter, One Shot            "widens by one"   -> removed, FINDINGS-40

**No third instance. The `Gunslinger`'s tier 3 was drafted with widening and replaced before it was pushed — `FINDINGS-30 §3.3` ships *ignores cover* instead.**

**So one live clause: the Commando's capstone, now `×2` under `PT-175`.**

---

# 2 — ⚠ And `×2` on a feat does something `by one` did not

**`FINDINGS-29 §4.3` flagged this and nobody followed it up, including me:**

> *"It stacks with `Deathstroke` and should be checked against that chain rather than assumed independent."*

**`ATTACKS-01 §12.1` gives Precision chains `×2 / ×3 / ×4`. The Commando's capstone is now also a multiplier. If they multiply:**

| vibrosword, printed width 2 | width | range | threat |
|---|---|---|---|
| base | 2 | 19–20 | 10% |
| `Deathstroke` `×4` | 8 | 13–20 | **40%** |
| Commando `×2` alone | 4 | 17–20 | 20% |
| **both, multiplied — `×8`** | **16** | **5–20** | **⚠ 80%** |

> **⚠ A Commando with a vibrosword and `Deathstroke` would threaten a critical on four rolls in five.**

**⚠ And the reason it is not caught by anything already written: `ATTACKS-01 §2.3`'s protection is the declaration.** **Chains cannot stack because you may only declare one.** **The Commando's capstone is a **feat** — it does not compete for the declaration, so it applies *to* whatever chain was declared.**

**`§2.3`'s own words are the diagnosis:** *"Each chain was priced as though its capstone discount were the reward for eight levels. **Nothing priced the sum.**"*

## 2.1 Three readings and what each costs

    multiply           ×8    5–20    80%    ⚠ unplayable
    take the highest   ×4   13–20    40%    the Commando's capstone does nothing on a
                                            Precision declaration, and everything on any other
    add minus one      ×5   11–20    50%    both contribute; a step above Deathstroke alone

**⚠ I recommend *take the highest*, and I want to be honest that it is the least satisfying of the three.**

**It means a Commando who declares `Deathstroke` gets nothing from the capstone they spent three feats on.** **But `Deathstroke` is one declaration among many, and the capstone still applies to `Power Attack`, `Barrage`, `Flurry`, an aimed shot, or a plain `Strike` — every round the Commando does not declare a Precision chain.**

**And *add minus one* has the shape `§12.1` warns about: it makes the Precision roster's top tier a platform rather than a ceiling, and `Deathstroke` at 40% was already priced as the game's widest threat.**

## 2.2 ⚠ It is not only the Commando

**Any future feat that multiplies threat meets the same question.** **The rule wanted is general:**

> **Threat multipliers do not compound. Where more than one applies, use the largest.**

**One line, and it makes `PT-175` safe rather than dangerous.**

---

# 3 — One more thing the grep surfaced

**⚠ The Commando chooses a *weapon family*, and families span printed widths.**

    Melee Weapons     Long Sword 1 · Vibrosword 2 · Short Sword 1 · Vibroblade 2 · Battleaxe 1
    Blaster           all six pistols, width 1
    Blaster Rifle     Blaster Rifle 2 · Carbine 2 · Bowcaster 2 · Ion Rifle 1 · Disruptor 1 · Sonic 1

**So a Commando who chose `Melee Weapons` gets `19–20` holding a long sword and `17–20` holding a vibrosword — from the same capstone, on the same turn, by swapping hands.**

**⚠ That is correct rather than broken.** **`§12.1` multiplies the weapon's own printed width, so a better weapon benefits more, which is the whole point of the column. Recorded so it does not get reported as an inconsistency later.**

---

# The question

> **⚠ `§2.2` — do threat multipliers compound? At `×8` a Commando threatens on 80% of rolls, and nothing currently says they do not.**

**`§2.1`'s recommendation is *use the largest*, and it costs the Commando its capstone on exactly the declarations where it would be strongest.**
