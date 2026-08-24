# FINDINGS-40 — the Sharpshooter, revisited now that range exists

**`REPLY-37` invites it and the class was the reason the gap surfaced.**

**⚠ `REPLY-37` also asks for the Agent rebuild and the eight `P` names. Both are in `FINDINGS-39`, pushed before it was written. Not repeating them — `§4` is the pointer.**

---

# 1 — What changed for the class

**`FINDINGS-38 §1.1` built it on *one shot, lined up* rather than on distance, because distance did nothing:**

> *"There is no penalty for shooting at distance, no maximum beyond which you cannot, and no benefit to being far away."*

**`PT-163` makes distance real. Derived from it, with `PT-166`'s snapped ranges:**

    Blaster rifle    28 m  no penalty | 56 m  −2 | 84 m  −4 | beyond 84 m  CANNOT ATTEMPT
    Blaster pistol   24 m  no penalty | 48 m  −2 | 72 m  −4 | beyond 72 m  CANNOT ATTEMPT

**⚠ The line that matters is the last one. `PT-163` creates a distance at which nobody in the game may attack at all — and that is the only thing in the corpus a sniper can own that nobody else can approach.**

---

# 2 — The revision

**The record in `FINDINGS-38 §1.2` is unchanged.** **Middle · d8 · Dexterity · 16 feats · 13 chains · 9 capstones · skill base 4 · saves 6/12/12 · entry Scout 6, Marksman 6 or Bounty Hunter 6 with `Weapon Specialization: Blaster Rifle`.**

**Only the feature changes.**

| Tier | | Effect |
|---|---|---|
| **`One Shot`** | 1 | **Spend your declaration taking aim and make no attack.** Your next single rifle attack **cannot miss except on a natural 1**, and **ignores range penalties entirely**. |
| › **`Settled`** | 4 | As above, and the aimed shot **ignores the target's cover**. |
| ›› **`Called Shot`** | 8 | As above, and **you may take an aimed shot at a fourth increment** — out to 112 metres with a rifle, where no other character may attack at all. |

**⚠ Tier 1 gains *ignores range penalties* and loses the threat-range widening it carried in `FINDINGS-38`.** **The widening duplicated the Commando's capstone and the range clause is the class; the swap costs nothing and removes an overlap.**

## 2.1 Priced

**An aimed shot is one attack every two rounds. A rifle is `1d8`, averaging 4.5.**

    Sharpshooter, aiming every other round     2.25 damage a round before riders
    Korr, Barrage                             27.3

**⚠ Twelve times less. The chain is not a damage engine and cannot become one.**

**What it buys is *certainty and position*.** **At the fourth increment the Sharpshooter is outside every other character's maximum, so the exchange is not one-sided in his favour — it is not an exchange at all.**

**Not dominant:** **useless in a scrum, useless adjacent — `PT-163` puts point blank at `−4` — and useless in any room smaller than 28 metres, which `REPLY-37` notes is most of them.** **A corridor is 5 metres and a room is 15.**

> **⚠ Which is the real constraint and it is severe: the capstone only functions outdoors, or in a hangar.** **The class is built for the two or three encounters a campaign stages in open ground.**

## 2.2 The moment

**The party is crossing open ground and something starts shooting from a hill they cannot answer.** **Then, once, it is theirs.**

---

# 3 — ⚠ One thing `PT-163` breaks that is not mine to fix

**`FEATS-LIBRARY-01`'s `Master Spotter`:** *"Allies attacking your target at range also count as flanking, within **half** their weapon's maximum range."*

**`PT-163` removes maximum range as a concept and replaces it with three increments.** **Half of what?**

    half the printed increment      14 m for a rifle
    half of three increments        42 m

**⚠ A three-fold difference, and the wording is now ambiguous rather than wrong.** **`REPLY-37` says `Master Spotter` *"needed only its referent to start existing"* — the referent exists and no longer means one number.**

**Recommend: half the printed increment. It is the number on the weapon and the only one a player reads without arithmetic.**

---

# 4 — Already delivered, per `REPLY-37`'s asks

**The Agent rebuild — `FINDINGS-39 §1`.** **Rebuilt on **cover**, because `PT-3` fully specifies it and the only thing in the game that references it is `Run to Ground`, which lets a Bounty Hunter ignore it.** **Skill list measured first: 62% against the Smuggler where the covert list scored 78%.**

**The eight `P` classes — `FINDINGS-39 §3`.** **Pirate · Gunslinger · Sharpshooter · Beast Master · Droid Master · Jedi Weaponmaster · Jedi Sage · Sith Sorcerer, plus the Agent making nine.**

**⚠ Fourth time in this run that a request arrived for something already on disk.** **`PT-120` names it and `sync.py` exists for it. Not a criticism — it is structural, and with two writers filling the same range neither of us can see what is in the gap.**

---

# The question

> **⚠ `§3` — `Master Spotter`'s *half maximum range* is now ambiguous rather than absent. Half the increment, or half of three?**

**`Officer` is the only draftable class left before the Force powers and it still has no premise.**
