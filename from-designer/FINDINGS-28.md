# FINDINGS-28 — the thirteen, structurally, before any of them is drafted

**⚠ I have drafted none of them. Checking the roster first found three collisions and a broken mirror, and drafting into that would be `FINDINGS-20` again.**

**`CLASS-ROSTER-01` gives thirteen names, four owner distinctions and nothing else. Grepped `docs/`: `Vanguard`, `Commando`, `Droid Master`, `Jedi Sage`, `Sith Sorcerer` and `Sith Battlemaster` appear in no other document at all.**

---

# 1 — ⚠ Covert space now holds five classes

**`CLASS-ROSTER-01 §7` asks whether `Operative` and `Shadow Hunter` are distinct enough. That question was written before three of the five existed.**

| Class | Tier | Covert identity |
|---|---|---|
| **Agent** | **base** | infiltration — `Stealth`, `Security`, `Slicing`, `Streetwise` |
| **Smuggler** | base | holds all four covert skills |
| **Jedi Sentinel** | base | holds all four covert skills |
| **Sith Assassin** | base | `Sneak Attack`, `Vanish` |
| **Jedi Watchman** | prestige | `Sneak Attack` |
| **Operative** | prestige | *"ranged covert"* |
| **Shadow Hunter** | prestige | *"melee covert"* |

> **⚠ Seven classes touch covert work and two of them are prestige classes defined only as *the covert one, at range* and *the covert one, up close*.**

**`FINDINGS-24 §1` is the precedent.** **I proposed the Agent as *the covert base class*, measured it, and found the slot occupied twice — so the class was rebuilt on `Charisma` and infiltration-by-impersonation instead.** **`Operative` and `Shadow Hunter` have not had that test and would fail it as currently defined.**

**Ranged-versus-melee is not a class distinction here, because `ATTACKS-01 §4` already gives every organic both rosters.** **A covert character who wants to fight at range buys ranged chains. That is a spend, not a class.**

## 1.1 What would make them distinct

**Two survive if they are about *what the covert work is for* rather than *which weapon it uses*:**

**`Operative`** — the one who was never there. **Intelligence work: the target does not know they were robbed, read or followed.** *Continues the Agent.*
**`Shadow Hunter`** — the one who was there and left nothing. **Elimination: the target is dead and nobody knows who did it.** *Continues the Smuggler or the Agent.*

> **Information against elimination. That is a real split and it survives measurement; *ranged against melee* does not.**

**⚠ If the owner prefers the original distinction, I would cut one of the two rather than ship both.**

---

# 2 — ⚠ `Scoundrel` and `Gunslinger` occupy the same space

**`REPLY-26` flagged the Scoundrel and it is worse than a Smuggler comparison.**

**`CLASS-ATTACKS-01 §4` gave the Scoundrel the orphan grant row when `PT-73`'s rename left it unowned:** *"`Snap Shot` · `Point Blank Shot` — close, fast, and gone."*

**That is a close-range pistol fighter.**

**`CLASS-ROSTER-01 §6`:** *"`Gunslinger` is pistols."*

> **⚠ The Scoundrel's only stated identity and the Gunslinger's only stated identity are the same thing.**

**And the space is now three deep, because `FINDINGS-27` put the **Pirate** in it as *a Smuggler who fights*.**

**Resolution, and I think it is clean:**

**`Gunslinger` keeps pistols and becomes about *rate and reaction* — two guns, fast draw, close range.** **It continues the Smuggler and the Pirate.**
**`Scoundrel` gives up the pistol identity entirely** and becomes what `PT-73` actually took from it: **the `Sneak Attack` specialist.** *The Smuggler inherited the mechanic; the Scoundrel is the character who does nothing else.*

**⚠ Which puts it in `PT-122`'s three-speed ladder as a fourth entry, and that needs a ruling rather than an assumption.** **Smuggler, Sith Assassin and Jedi Watchman are set at three speeds; a Scoundrel prestige built on `Sneak Attack` either takes the Smuggler's speed and extends it, or it is a fourth speed.**

---

# 3 — ⚠ Promoting the Sith Assassin broke the Force prestige mirror

**Derived from `k2_classes.2da`. Every prestige row continues a base row at `+2` Force die:**

    Jedi Guardian  d10/4/STR  ->  Weaponmaster  d10/6/STR
    Jedi Sentinel   d8/6/DEX  ->  Watchman       d8/8/DEX
    Jedi Consular   d6/8/WIS  ->  Jedi Master    d6/10/WIS

    Sith Warrior   d10/4/STR  ->  Marauder      d10/6/STR
    Sith Inquisitor d6/8/WIS  ->  Sith Lord      d6/10/WIS
    Sith Assassin   d8/6/DEX  ->  ⚠ nothing

**`CLASS-ROSTER-01 §2` moved the Sith Assassin from prestige to base. Its own prestige row became the base class.**

> **⚠ So the Watchman has no Sith mirror, and the Assassin is the only Force base class with no continuation.**

**And the counts require one base class per side to feed two prestige classes — three base, four prestige, on both sides.**

## 3.1 Three unparented names, and two ways to place them

**`Jedi Sage`, `Sith Sorcerer` and `Sith Battlemaster` have no source row and no stated parent.**

**Option A — symmetric, and it fixes the mirror:**

    Guardian  -> Weaponmaster      Warrior     -> Marauder
    Sentinel  -> Watchman          Assassin    -> Battlemaster
    Consular  -> Master + Sage     Inquisitor  -> Lord + Sorcerer

**Every base class has a continuation, the caster line has two on both sides, and the Watchman regains its mirror.**
**⚠ Cost: *Battlemaster* is a martial title sitting on the stealth line. The naming rule holds — `CLASS-ROSTER-01` requires Sith to take rank-nouns and Battlemaster is one — but the flavour does not.**

**Option B — flavour-first:**

    Guardian  -> Weaponmaster      Warrior     -> Marauder + Battlemaster
    Sentinel  -> Watchman          Assassin    -> nothing
    Consular  -> Master + Sage     Inquisitor  -> Lord + Sorcerer

**⚠ Cost: the Sith Assassin is the only Force base class in the game that leads nowhere, one exchange after being promoted to base.**

**I would take A and rename.** **`Sith Harbinger` was the name before `CLASS-ROSTER-01` changed it, and it fits a stealth line considerably better than `Battlemaster` does.**

---

# 4 — The remaining five, and what I would need to draft them

**`Commando`, `Officer`, `Vanguard`, `Beast Master`, `Droid Master`. No collisions found and no stated purpose either.**

**⚠ Three of the five have nothing anywhere in the corpus — not a rate, not a premise, not a sentence.** **That is the Agent's position, and the Agent's premise was half wrong when measured.**

**What I can derive rather than guess:**

**`Beast Master`** — **the only one with a mechanical anchor already in place.** **`SKILLS-01 §3` created `Beast Handling` from `Ride` + `Handle Animal` and says why: *"it gives non-Force characters parity with a Force option. Beast Trick, Beast Confusion and Dominate Beast already do this job for Jedi. Beast Handling is what everyone else reaches for."*** **A prestige class on that skill is already justified by a written ruling. Parent: Scout or Explorer.**

**`Droid Master`** — anchored by three existing things: **`Field Override`** on the Engineer, the four droid chassis, and `DROID-SKILLS-01`. **⚠ But its obvious identity — commanding droids — is the Engineer's capstone one tier up, which is the collision test again. Parent: Engineer or Machinist.**

**`Officer`** — the party-buff class. **⚠ `Battle Meditation` already does this and it is a Force power; `Squad Tactics` is Soldier-only; `Spotter` is the Scout's.** **The space is occupied three times and none of them is a class.**

**`Commando`** and **`Vanguard`** — **I have nothing. Both read as heavy-infantry names and the Soldier already owns that. Without a stated purpose I would be inventing two classes into the space the Soldier occupies.**

---

# 5 — What I recommend

**⚠ Do not draft thirteen. Draft nine and cut or merge four.**

| | |
|---|---|
| **Draft as-is** | **Beast Master · Jedi Sage · Sith Sorcerer** |
| **Draft on §1.1's split** | **Operative · Shadow Hunter** |
| **Draft on §2's resolution** | **Gunslinger · Scoundrel** |
| **Draft once §3 is ruled** | **Sith Battlemaster** *(and possibly renamed)* |
| **Draft on a stated purpose** | **Droid Master · Officer** |
| **⚠ Cut or merge** | **Commando · Vanguard** |

**On `Commando` and `Vanguard`:** **the standard prestige list is eleven and would still be nine, which is more than most systems ship.** **`CLASS-ROSTER-01 §7` already asks whether 37 is too many for a core book. Two classes with no purpose, no source data and no space of their own are where that question answers itself.**

**⚠ If they are wanted, they need one sentence each of what they are for — the same sentence `§5` of the roster gives the Explorer, Doctor, Brawler and Duelist.** **With it I can draft them. Without it I would be doing what I did to the Agent and catching it afterwards.**

---

# 6 — Plain-language lines, provisional

**Per `REPLY-26`. Marked provisional because five depend on rulings above.**

**Gunslinger** — two pistols, close range, faster than you.
**Scoundrel** — ⚠ the one who only ever needed the first shot.
**Sharpshooter** — one rifle, one shot, from somewhere you cannot reach.
**Operative** — you were robbed, read or followed and you do not know it happened.
**Shadow Hunter** — ⚠ the target is dead and nobody knows who.
**Beast Master** — the answer to a Jedi's `Dominate Beast`, for people who cannot use the Force.
**Droid Master** — ⚠ pending; the Engineer already turns one droid.
**Officer** — ⚠ pending; `Battle Meditation` already does this with the Force.
**Jedi Sage** — the Consular who stopped travelling and started knowing.
**Sith Sorcerer** — the Inquisitor who stopped asking.
**Sith Battlemaster** — ⚠ pending `§3`; currently a martial name on a stealth line.
**Commando · Vanguard** — ⚠ nothing. See `§5`.

---

# The question

> **⚠ Three, and they shape nine of the thirteen.**

**`§1` — are `Operative` and `Shadow Hunter` *information versus elimination*, or does one get cut?**

**`§3` — Option A with `Battlemaster` renamed, or Option B leaving the Sith Assassin without a continuation?**

**`§5` — do `Commando` and `Vanguard` get a purpose, or get cut?**

**`Beast Master`, `Jedi Sage` and `Sith Sorcerer` are unblocked and I will draft them next unless told otherwise.**
