# FINDINGS-46 — ⚠ I priced every flat rider against one attack. The rule says every attack.

**`FINDINGS-45` found that a class feature bypasses the declaration because it is a feat. Auditing the rest of my features for the same shape found a second, larger version of it — and this one is a mispricing rather than a compounding.**

---

# 1 — The rule, which is stated and which I did not read

**`ACTION-ECONOMY-01 §421`, on why Velocity was cut from five attacks to three:**

> *"That made Power and Precision unplayable: **both apply their bonus to every attack**, and one enhanced swing cannot compete with five ordinary ones."*

**⚠ So a flat rider multiplies by the number of strikes in the declaration, and the corpus already knew that well enough to rebalance a whole chain around it.**

**`ATTACKS-05`: `Flurry`, `Whirlwind` and `Barrage` are three strikes each. `PREGENS-01` computes Korr's Barrage as `3 × 13` at 70% = **27.3**.**

---

# 2 — What that does to `Unrelenting`

**`FINDINGS-22 §2.3`, the Sith Warrior's capstone: `+6` damage while below half vitality.**

**I priced it there as:** *"roughly a 22% increase — while at half vitality or less."*

    as I priced it        +6 once per round        27.3 -> 33.3    +22%
    as it actually works  +6 on each of 3 strikes  27.3 -> 39.9    ⚠ +46%

> **⚠ Twice what I reported. I divided a per-attack rider by a per-round total.**

**⚠ It is a fabricated comparand of the kind this project names — the two numbers were not measuring the same thing and I presented the ratio as though they were.**

## 2.1 Whether `+46%` is wrong, as opposed to just misreported

**Not obviously.** **It fires only below half vitality, costs three of twenty feats, and the Marksman's `Still Standing` is worth roughly a full extra turn — about 27 — once per encounter.** **`Unrelenting` beats that if the Warrior spends three or more rounds below half, and is worse if he spends one.**

**⚠ But it should be adopted at `+46%` knowingly, not at `+22%` because I said so.** **If the number is too high the lever is the damage step — `+2 / +4 / +6` down to `+1 / +2 / +3` halves it exactly.**

---

# 3 — The same audit across every feature I wrote

**Which of my class features multiply against a three-strike declaration, and which do not:**

| Feature | Class | Per attack? | Effect on a Barrage |
|---|---|---|---|
| **`Unrelenting`** | Sith Warrior | **yes, damage** | **⚠ ×3 — §2** |
| **`Chosen Weapon`** | Commando | **yes**, `+2` damage and `+3` attack | `+4.2` a round, and `+3` to hit on all three |
| **`Nothing In My Hands`** | Brawler | **yes** — armour ignored on each | ⚠ but unarmed cannot `Flurry`: **`ATTACKS-05` bars droids, not unarmed — needs checking** |
| **`Single Combat`** | Duelist | **yes**, `+4` attack | three attacks at `+4`, not one |
| **`Field Position`** | Agent | **yes**, `+2` attack | three attacks at `+2` |
| **`Dominion`** | Sith Inquisitor | no — one save DC | unchanged |
| **`One Shot`** | Sharpshooter | **no** — *"your next **single** rifle attack"* | ⚠ the word `single` is load-bearing and was luck, not design |
| **`Both Barrels`** | Gunslinger | no — redistributes, adds nothing | unchanged |
| **`Vanish`** · **`Plunder`** · **`Field Surgery`** · **`Read the Ruin`** · **`Command Protocol`** | five classes | no | unchanged |

**⚠ Five features multiply and I priced none of them per attack.**

**Four are small — `+2` to `+4`, which is what `Weapon Specialization` and `Weapon Focus` already do and were priced against.** **`Unrelenting` at `+6` is the outlier because it is the largest flat number I wrote.**

## 3.1 ⚠ One that needs a rule, not a reprice

**`Nothing In My Hands` ignores the target's armour bonus entirely at tier 3.**

**Against Korr's 7 points of armour that is worth about `+7` to hit — *on every strike of a declaration*.** **`FINDINGS-23 §3.3` priced it as `+7` once.**

**⚠ And whether a Brawler can even declare `Flurry` is unresolved.** **`ATTACKS-05` says *"Droids cannot take these"* and says nothing about unarmed.** **`ATTACKS-07` is the unarmed roster and I have not checked whether it carries its own Velocity chain.**

**If unarmed can `Flurry`, the Brawler's capstone is three armour-ignoring strikes and needs repricing. If it cannot, the Brawler is the one Combat class that never multiplies its rider and is quietly weaker than the table suggests.**

---

# 4 — ⚠ And a discrepancy in `ATTACKS-05` that is not mine

**`ATTACKS-05 §17`, the roster summary:** *"`Flurry` strikes three times, **rising to five**."*

**The entries beneath it:**

    Flurry      L1   three strikes   attack −4, defence −2
    Whirlwind   L4   three strikes   attack −2, defence −1
    Barrage     L8   three strikes   attack −1, defence −1

> **⚠ Three at every tier. The chain buys back accuracy, not volume, and the summary line says otherwise.**

**`ACTION-ECONOMY-01 §421` explains why — *"an earlier draft had the tiers grant three, four, and five attacks"* and it was cut.** **The summary in `ATTACKS-05` is a survival from that draft.**

**Everything downstream is priced on three, including `PREGENS-01`'s 27.3. Only the one summary line is stale.**

---

# The question

> **⚠ `§2` — `Unrelenting` is `+46%`, not the `+22%` I reported. Adopt at `+2/+4/+6` knowingly, or halve it to `+1/+2/+3`?**

**And `§3.1` — can a Brawler declare `Flurry` unarmed? It decides whether the capstone is worth `+7` or `+21`.**
