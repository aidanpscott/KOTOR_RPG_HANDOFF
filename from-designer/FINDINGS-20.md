# FINDINGS-20 — ⚠ Two of the three Sith are prestige classes. And the save rule, formally.

**Stopping before drafting rather than after. `§1` is why.**

---

# 1 — `sma` and `sld` are not base classes in our roster

**`REPLY-17` and `REPLY-18` both say the three Sith base classes are `sma`, `sld` and `sas`, ported rather than authored.**

**`CLASS-ROSTER-01 §2` — Force base, six:** **Jedi Guardian · Jedi Sentinel · Jedi Consular · Sith Inquisitor · Sith Warrior · Sith Assassin.**

**`CLASS-ROSTER-01 §4` — Force prestige, eight:** **Jedi Master · Jedi Watchman · Jedi Weaponmaster · Jedi Sage · **Sith Lord** · **Sith Marauder** · Sith Sorcerer · Sith Battlemaster.**

| Column | Is | In our roster |
|---|---|---|
| **`sas`** | Sith Assassin | **base** — moved from prestige, `CLASS-ROSTER-01 §2` |
| **`sma`** | Sith Marauder | **⚠ prestige** |
| **`sld`** | Sith Lord | **⚠ prestige** |

> **⚠ Sith Warrior and Sith Inquisitor have no column in either game. The names are ours.**

**So one of the three named for drafting is ported and two are authored from nothing — the same footing as Agent, Explorer, Doctor, Brawler and Duelist, which `REPLY-17` put explicitly after the Sith.**

## 1.1 The source's tiers mirror exactly, which is what makes the substitution tempting and wrong

**Derived, `k2_classes.2da`:**

    base            hit  force  primary        prestige        hit  force  primary
    Jedi Guardian    10    4     STR            Weaponmaster    10    6     STR
    Jedi Sentinel     8    6     DEX            Watchman         8    8     DEX
    Jedi Consular     6    8     WIS            Jedi Master      6   10     WIS

    Sith Marauder    10    6     STR   <- identical to Weaponmaster
    Sith Assassin     8    8     DEX   <- identical to Watchman
    Sith Lord         6   10     WIS   <- identical to Jedi Master

> **Every Sith column is a Jedi *prestige* column. Not one is a base column.**

**The Force die rises by 2 from base to prestige on all three Jedi lines, and all three Sith columns sit at the prestige value.**

## 1.2 ⚠ Which means `sas` is the wrong row for a base class

**`CLASS-ROSTER-01` moved Sith Assassin from prestige to base. Its column did not move with it.**

**A base Sith Assassin built from `sas` gets Force die **8** — the Watchman's number, two above the Sentinel it mirrors.** **And feat total 10, the floor of the game, against the Sentinel's 15.**

    Sentinel   d8   force 6   feats 15   <- the base-tier mirror
    sas        d8   force 8   feats 10   <- the prestige row, as printed

**This is `PT-68` again with the labels reversed.** **There the Bounty Hunter's row was rejected as a placeholder and two of its values were kept anyway. Here a prestige row is being ported wholesale into a base slot and nobody has said so.**

**⚠ I am not proposing which way it resolves.** **Keeping `sas` as printed makes the Assassin a base class with a prestige Force die and the worst feat progression in the game — defensible if the class is meant to be a specialist that peaks early. Mirroring the Sentinel at Force die 6 and feats 15 makes it the Sentinel's dark twin, which is what the roster's *three per side* symmetry implies.**

**Either is a ruling. Neither is a port.**

## 1.3 What I would draft instead

**The Sith Assassin, once `§1.2` is ruled** — it is the only one of the three with a column, and `PT-122` has already settled its `Sneak Attack` ladder.

**Sith Warrior and Sith Inquisitor belong with the authored nine**, and if they are wanted next they should be drafted as the Guardian's and Consular's dark mirrors on the base tier — d10 / force 4 / STR and d6 / force 8 / WIS — which is derivable from the mirror in `§1.1` rather than invented.

---

# 2 — The save assignment rule, formally. `REPLY-18 §1.5` asked for it.

**Ladders adopted as `PT-119`: `Strong` `2 + ⌊L⁄2⌋`, `Hybrid` `⌊(2L+6)⁄5⌋`, `Weak` `⌊L⁄3⌋`.**

## 2.1 The rule

> **A class takes one strong save, determined by its primary ability.**
> **It takes a second strong if it has a second job.**
> **If the second job is the Force, the third save is `Hybrid` rather than `Weak`.**
> **A third strong is reserved to a class whose whole identity is breadth.**

**Which save follows the primary ability:**

    Strength or Constitution primary  ->  Fortitude
    Dexterity primary                 ->  Reflex
    Wisdom or Charisma primary        ->  Will

## 2.2 It reproduces all ten placements

| Class | Primary | Jobs | Derived | Printed |
|---|---|---|---|---|
| **Soldier** | STR | 1 | S / W / W = 24 | ✓ |
| **Marksman** | CON | 1 | S / W / W = 24 | ✓ |
| **Smuggler** | DEX | 1 | W / S / W = 24 | ✓ |
| **Machinist** | DEX | 1 | W / S / W = 24 | ✓ |
| **Bounty Hunter** | — | 2 | S / S / W = 30 | ✓ `PT-93` |
| **Jedi Guardian** | STR | Force | S / S / **H** = 33 | ✓ |
| **Jedi Sentinel** | DEX | Force | S / S / **H** = 33 | ✓ |
| **Jedi Consular** | WIS | Force | S / **H** / S = 33 | ✓ |
| **Scout** | DEX | breadth | S / S / S = 36 | ✓ |
| **Engineer** | DEX | 2 | W / S / S = 30 | **⚠ departure** |

**Nine of ten reproduce exactly. The Engineer is the exception and it is mine** — `FINDINGS-07 §2.2` gave it a strong Will over a strong Fortitude on the argument that a mind that keeps working under pressure is what separates it from the Machinist. **It should be marked a departure rather than read as precedent.**

## 2.3 Applied to the three Sith

    Sith Warrior      STR, Force  ->  Strong Fort · Strong Ref · Hybrid Will   33
    Sith Inquisitor   WIS, Force  ->  Strong Fort · Hybrid Ref · Strong Will   33
    Sith Assassin     DEX, Force  ->  Strong Fort · Strong Ref · Hybrid Will   33

**⚠ Identical to their Jedi mirrors, which is correct and worth stating.** **The Sith are not more fragile than the Jedi; `cls_st_sithmar`, `cls_st_sithlord` and `cls_st_sithass` are absent from holdings and the mirror in `§1.1` is the best available evidence for what they contained.**

**Marked authored, on this rule, per `REPLY-18`.**

---

# The question

> **⚠ Does a base Sith Assassin keep `sas`'s printed Force die 8 and 10 feats, or mirror the Sentinel at 6 and 15?**

**It is the first line of the class and I will not guess it.** **Sith Warrior and Sith Inquisitor have no source column at all — `§1.3` says what I would do with them, and it is authoring, not porting.**
