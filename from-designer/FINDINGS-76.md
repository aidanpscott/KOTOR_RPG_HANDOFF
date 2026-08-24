# FINDINGS-76 — ⚠ `PT-215` orphaned `Inspire Followers`. The Officer inherits it.

**Owner: remake it as an Officer ability, and note the Exile question for the agenda.**

---

# 1 — ⚠ It has a prerequisite that no longer exists

**`FORCE-POWERS-01 §78`–`80`, ported verbatim:**

    Inspire Followers I     Light · tier 1 · cost 8 · DC −1 · requires JEDI MASTER
                            every party member +1 hit, +1 damage, +1 Will. 45 s. Not droids.
    Inspire Followers II    +2 · requires level 5 Jedi Master
    Inspire Followers III   +3 · requires level 9 Jedi Master

> **⚠ `PT-215` cut `Jedi Master` as a class. Three ported Force powers now require a class that does not exist.**

**And `Force Breach` and `Force Suppression` both name it — `§38` and `§61` — so two more powers reference a chain whose gate is gone.**

**⚠ The owner's instinct is better founded than the reasoning given for it. Moving `Inspire Followers` to the Officer is not a flavour choice; it is the repair for a break `PT-215` made and nobody caught.**

## 1.1 And the feat rows were cut in the source

**`feat.2da`: `XXXX_INSPIRE_FOLLOWERS_I` through `V`.** **The `XXXX_` prefix is the same disabled-row convention as `XXXX_FORCE_FOCUS_ALTER` — `PT-183`.**

> **The feat version was cut and the power version shipped. So there is no feat to port, and the Officer's version is authored from the power.**

---

# 2 — The Officer, rebuilt

**⚠ `Give the Order` was priced as one leadership feature among three. `PT-215` left it carrying the whole idea, and `REPLY-57` says build it accordingly.**

**Merged into one chain rather than bolted together — a class has one feature.**

| Tier | | Effect |
|---|---|---|
| **`Give the Order`** | 1 | **Spend your declaration.** Every ally who can hear you gains **`+1` attack, `+1` damage and `+1` Will** until the encounter ends. |
| › **`On My Mark`** | 4 | **`+2`**, and **one ally may immediately make one attack.** |
| ›› **`Command Presence`** | 8 | **`+3`**, and the immediate attack applies to **two** allies. |

**⚠ *Until the encounter ends* rather than 45 seconds.** **`ACTION-ECONOMY-01` has no seconds. The Consular's chain already uses encounter duration and this matches it.**

**One declaration, once, then the Officer fights normally.**

## 2.1 ⚠ Priced, and it is the largest party-wide effect in the game

    3 allies × ~3 attacks × +3 damage    +27 damage a round across the party
    plus +3 to hit on every one of those attacks
    plus +3 Will to everybody

**⚠ And the Officer contributes none of it himself.** **That is the class — `d10`, 13 chains, no personal damage feature — but the number should be seen before it is adopted.**

**Two dials if it is too much: **`+1 / +2 / +3` → `+1 / +1 / +2`**, or **allies within a stated distance** rather than everyone who can hear.**

**⚠ I would keep it.** **The source figure is `+3` and it was balanced against a party of three in a game where the buff also cost 8 Force points and 45 seconds. Ours costs a whole round and the class's entire identity.**

## 2.2 One departure from the source, deliberately

**The power says *"does not affect droids."*** **⚠ `PT-210` ruled the sharing principle: *share what is training, withhold what is instinct or anatomy*.**

> **An order is training. A droid follows orders better than anyone.**

**So the Officer's version **does** affect droids, and the exclusion was a Force-morale artefact rather than a rule about orders.**

---

# 3 — For the agenda: `Inspire Followers` as an Exile-unique power

**Owner: note it with the relevant information.**

    what        Inspire Followers I–VI, Light side
    where       FORCE-POWERS-01 §78–80 hold I–III; Force Breach §38 refers to
                "all six tiers", so III–VI are referenced and not written
    source      feat.2da rows XXXX_INSPIRE_FOLLOWERS_I–V — cut rows, feat version
                disabled, power version shipped
    the gate    "requires Jedi Master" — ⚠ a class PT-215 removed
    the case    in KOTOR 2 it belongs to the Exile, whose Force bond with the
                party is the mechanic the power expresses
    depends on  whether the campaign models the Exile's bond at all; nothing in
                the corpus does
    ⚠ note      Force Breach and Force Suppression both reference the chain, so
                cutting it entirely would leave two powers naming nothing

---

# 4 — The two open items from `FINDINGS-74 §4`

**⚠ The `1 / 5 / 10` gating.** **`ATTACKS-05 §69`–`71` still reads `2 / 4 / 10`. The owner ruled the change; `PT-193`'s restore used the original figures. One edit, and it is not mine to make.**

**⚠ The `Sith Assassin`.** **`Vanish` survives; its `9d6`-against-`10d6`-against-`7d6` distinction does not. Its stealth damage now equals any class that spends one tree.** **It still holds `Killer's Instinct`, which three other classes also hold. Reported again because nothing has moved on it.**

---

# The question

> **⚠ `§1` — three ported powers require `Jedi Master`, which no longer exists. Moving the chain to the Officer fixes one; `Force Breach` and `Force Suppression` still name it.**

**And `§2.1` — `+3` party-wide is the largest effect in the game. Keep, or halve?**
