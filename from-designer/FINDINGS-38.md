# FINDINGS-38 — Sharpshooter and Droid Master

**Two of the five remaining. `§1.1` is a gap the Sharpshooter walked into; `§2` is built on `REPLY-33`'s 5e shape.**

---

# 1 — Sharpshooter

**Owner distinction, `CLASS-ROSTER-01 §6`:** *"`Gunslinger` is pistols. `Sharpshooter` is rifles."*

## 1.1 ⚠ There are no range rules, so *rifles* cannot mean what it should

**Grepped `ACTION-ECONOMY-01` and `ATTACKS-01` for maximum range, range penalties, short and long range. Nothing.**

**The only ranges in the corpus are two numbers on `PREGENS-01`'s equipment lines** — **blaster rifle 28 m, blaster pistol 23 m** — **and nothing consumes them.**

> **⚠ There is no penalty for shooting at distance, no maximum beyond which you cannot, and no benefit to being far away.** **A rifle's 28 metres is a fact about the weapon that changes nothing.**

**Two rules do reference range and both assume a system that is not written.** **`FEATS-LIBRARY-01`'s `Master Spotter` — *"within half their weapon's maximum range"* — and `Close Combat`, which gives *"+1 attack at short range"* without defining short range.**

**So a Sharpshooter built on *outranging people* is a class built on nothing, the same way the Pirate's dogfighting was.** **`FINDINGS-27 §3.5` flagged that; this is the second instance and it is a smaller gap than ship rules.**

**⚠ I have built the class on what rifles *do* have — one shot, lined up — rather than on distance. If range rules arrive, the class should be revisited.**

## 1.2 The record

    Middle · d8 · Dexterity · 16 feats · saves 6/12/12 · skill base 4
    13 chains, 9 capstones · picks 27, T = 31
    Skills 6   Awareness · Alertness · Stealth · Demolitions · Athletics · Scavenging

> **Entry: character level 10, **Scout 6, Marksman 6 or Bounty Hunter 6**, and `Weapon Specialization: Blaster Rifle`.**

**⚠ The specialization requirement mirrors the Commando's and does the same work.** **You enter holding the top of the rifle ladder, and `ACTION-ECONOMY-01 §18.2` grants rifle proficiency to the Soldier, Scout and Marksman but not the Focus or Specialization — so it is three feats of real investment, not a formality.**

## 1.3 Feature — `One Shot`

| Tier | | Effect |
|---|---|---|
| **`One Shot`** | 1 | **Spend your declaration taking aim and make no attack.** Until the start of your next turn your next single attack with a rifle **cannot miss on anything but a natural 1**, and its threat range widens by one. |
| › **`Settled`** | 4 | As above, and **the aimed shot ignores the target's cover.** |
| ›› **`Called Shot`** | 8 | As above, and **a threat confirmed on the aimed shot needs no confirmation roll.** |

**Priced.** **It costs a full round — the same price the `Soldier`'s `Hold the Line` pays and the largest price in the system, because `ATTACKS-01 §2` makes the declaration the whole turn.**

**Against `Barrage` at 27.3 damage a round over two rounds, an aimed rifle shot is one hit of about 4.5 plus riders. ⚠ The chain is not about damage.** **It is about the shot landing — which matters against high Defence, against cover, and for anything that rides on a hit.**

**⚠ And it stacks with `Sneak Attack` and `Killer's Instinct` by design.** **A Sharpshooter who also holds stealth dice converts a guaranteed hit into a guaranteed alpha strike, which is what a sniper is. It is two feat chains and a wasted round to set up, and it fires once per approach — `ACTION-ECONOMY-01 §19.5`.**

**Not dominant:** **useless in a scrum, useless against anything already adjacent, and it gives up a whole round every time.** **A Sharpshooter who aims every round attacks half as often as anyone else.**

---

# 2 — Droid Master

**Built on `REPLY-33`'s shape, which is 5e's answer to the necromancer.**

## 2.1 The record

    Middle · d8 · Intelligence · 15 feats · saves 6/12/12 · skill base 5
    11 chains, 10 capstones · picks 27, T = 31
    Skills 8   Repair · Slicing · Security · Science · Appraise · Awareness · Alertness · Pilot

> **Entry: character level 10, **Engineer 6 or Machinist 6**, and `Repair` 8 ranks.**

**⚠ `Intelligence` primary, so `PT-133`'s extension is load-bearing here** — Will strong. **The Explorer was the first Intelligence class; this is the second, and the rule that covers it is four exchanges old.**

**Chain count at the `Middle` floor deliberately.** **A class whose combat contribution is several other characters does not need trees of its own.**

## 2.2 Feature — `Command Protocol`

| Tier | | Effect |
|---|---|---|
| **`Command Protocol`** | 1 | **You hold **two** droids.** Each is a henchman under `PT-145` with its own turn. **⚠ You may issue one order to all of them at once as a Bonus action, and an order persists until its task is complete.** A droid with no order **takes cover and moves only to avoid harm.** |
| › **`Squad Doctrine`** | 4 | **Three droids**, and an order may name two different tasks split among them. |
| ›› **`Master and Servants`** | 8 | **Four droids**, and **once per encounter you may issue an order as a free action** rather than a Bonus. |

**⚠ Cap is four, stated in the class rather than left to a GM.** **`REPLY-31` asked for a hard cap and this is it: two, three, four at tiers 1, 4 and 8.**

## 2.3 ⚠ The decision cost is the design, not the turn count

**`REPLY-31` worried that a henchman with its own turn means an army of turns.** **`REPLY-33`'s reading is the answer and it is worth stating in the class text rather than the ruling:**

> **The problem was never the turns. It was the decisions.** **Four droids sharing one order with a stated default resolve fast. Four droids each making a choice is what ends an evening.**

**One order, all droids. Orders persist. Silence has a default.** **Decision cost is one per round regardless of how many droids are on the field.**

## 2.4 ⚠ The scaling axis, because 5e's version is a trap

**`REPLY-33`'s warning is the important half: 5e's necromancer *"gives a false sense of security in numbers, but those numbers are straw figures."*** **The minions do not scale and the class hollows out.**

**`PT-153` supplies the fix and it is already ruled:** *"a Droid Master's droids are built, commanded, permanent until destroyed, and replaceable. A destroyed droid is not a loss. It is a rebuild."*

> **So the sink is upgrades, not headcount.**

**Proposal: a Droid Master's droids advance with them.** **Each droid is built at a level equal to half the Droid Master's, rounded down, and rebuilding one after destruction takes downtime rather than a resource.**

**⚠ Which means the cap of four is a *breadth* cap and the level is the *depth* dial — the same shape as chain counts.** **A Droid Master at 20 fields four droids at level 10 rather than four at level 3, and the class does not hollow out.**

**And it uses `DROID-SKILLS-01`'s existing chassis list — `Astromech`, `Assassin`, `Battle`, `Remote` — which carries `PT-114`'s eleven-chain access limit and `PT-92`'s Force restriction with it.** **No new machinery.**

## 2.5 Against the Engineer, measured

    Engineer        one droid    the enemy's    one encounter    Field Override
    Droid Master    up to four   yours          permanent        Command Protocol

**Different count, different ownership, different duration.** **⚠ And the Engineer's is a declaration spent in combat where the Droid Master's is built in downtime, so the two never compete for the same action.**

---

# 3 — Plain-language lines

**Sharpshooter** — spends a whole round doing nothing so the next shot cannot miss.
**Droid Master** — brings four droids, tells them all the same thing, and rebuilds them when they break.

---

# The question

> **⚠ `§1.1` — there are no range rules, so *rifles* currently means only *the weapon you hold*. Is that a gap someone should fill, or does the Sharpshooter stand on `One Shot` alone?**

**`Officer` is next, then `Scoundrel` and `Vanguard` in the owner's order.**
