# FINDINGS-73 — ⚠ The Watchman's column is empty. There is no feature in the game files.

**Owner asked whether one exists. Derived, `feat.2da`, `jwa_granted` with proficiencies, the universal Force package and the `Sneak Attack` ladder stripped:**

    jwa   (nothing)
    sma   Ignore Pain I–III · Increase Combat Damage I–III
    jsn   Force Immunity: Fear · Stun · Paralysis

> **⚠ Zero distinctive grants. The Sith Marauder has six and the Jedi Sentinel three.**

**So the Watchman was never *stripped* by `PT-193`. Its entire distinctive content in KOTOR 2 **was** `Sneak Attack`, and when that became an attack tree anyone could buy, the class became an empty column.**

**The feature has to be authored. `§2` is what I would author and `§1` is why.**

---

# 1 — The unclaimed space, derived

**⚠ Five features already occupy *what happens around a stealth strike*:** `Vanish` · `Nobody Saw Him Leave` · `No Firing Position` · `Nowhere To Stand` · `Field Position`. **A sixth would be the sixth.**

**But grepping the whole corpus for the *inverse* returns almost nothing:**

    ACTION-ECONOMY-01 §47     Scan — an Awareness or Alertness check to find
                              what you have missed: a hidden enemy, a trap, a way out
    SKILL-RESOLUTION-01 §22   "Stealth and Awareness are a contested pair"

> **⚠ Five classes hide. One action finds. And no class in the roster is built on finding.**

**`Jedi Sense` is not it** — `FEATS-LIBRARY-01 §456` makes it a flat Defence bonus, *"awareness of danger"* in name only.

**⚠ And it is the Watchman's own job description.** **The class watches a sector for years and reports what is moving in it. `FINDINGS-26 §3.3` gave it `Slicing`, `Stealth`, `Awareness`, `Persuade`, `Security`, `Medicine` — the only Force class holding both halves of the contested pair.**

---

# 2 — `What Moves in the Dark`

**Jedi Watchman, granted at 1 / 4 / 8.**

| Tier | | Effect |
|---|---|---|
| **`What Moves in the Dark`** | 1 | **You may `Scan` as a free action once per round**, and you use the better of `Awareness` or `Alertness` for it. |
| › **`Nothing Hides From Me`** | 4 | **Anything you find with a `Scan` is found by your whole party** until the end of your next turn. |
| ›› **`The Watch Is Kept`** | 8 | **An enemy that is Hidden from you when combat begins is not**, and **you may not be made unaware by anything short of losing consciousness.** |

**⚠ The capstone is the class's own parent chain finished.** **`Force Immunity` runs Fear → Stun → Paralysis; two of those three are ways to be made *unaware* under `ACTION-ECONOMY-01 §19.5`. The Sentinel becomes immune to the conditions; the Watchman becomes immune to their consequence.**

## 2.1 Priced

**⚠ It grants no attack, no damage and no Defence at any tier. It is entirely counter-play, and its value is exactly the strength of the thing it counters.**

    against a Scoundrel at Master Sneak Attack + Killer's Instinct   31.1 a round denied
    against an Operative's No Firing Position                        the position is found
    against a party with no stealth opposition                       nothing

**Which is the right shape for a counter — it does nothing until someone brings the thing it answers, and then it does a great deal.**

**⚠ And it is the first feature in the roster whose worth depends on the *campaign* rather than the encounter.** **A gamemaster who never uses hidden enemies makes this class inert, the way no ship rules make the Pirate half a class.** **Stated rather than hidden.**

**One line:** *Nothing gets the drop on you, and nothing gets the drop on anyone standing near you.*

---

# 3 — ⚠ What I did not do

**I did not give it a stealth feature.** **The obvious move — a sixth thing that happens around a stealth strike — would have made the Watchman the fourth class doing what the Assassin, Scoundrel and Shadow Hunter already do, and `PT-83`'s overlap test exists for exactly that.**

**And I did not port anything, because there was nothing to port.**

**⚠ `PT-212`'s reasoning applies here too:** **faithfulness to an empty column is faithfulness to a class that did not work.** **The KOTOR 2 Watchman was `Sneak Attack` and a Defence bonus.**

---

# The question

> **⚠ `What Moves in the Dark` — or should the Watchman be built on stealth after all, accepting it as the fourth class in that space?**

**`§2.1`'s caveat is the one to weigh: a counter-class is only as good as the campaign that needs countering.**
