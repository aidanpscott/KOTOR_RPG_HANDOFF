# FINDINGS-48 — `PT-178` applied to every class feature I have written

**One line a player would understand, per feature. ⚠ Four fail and I have not fixed them.**

**Twenty-seven features. The line is the whole chain, not a tier.**

---

# 1 — Pass — 23

| Feature | Class | One line |
|---|---|---|
| **`Hold the Line`** | Soldier | When something attacks the ally beside you, take the hit instead. |
| **`Read the Ground`** | Scout | When a blast catches your party, an ally may use your dodge instead of their own. |
| **`Quickdraw`** | Smuggler | When a conversation turns into a fight, you shoot before anyone acts. |
| **`Field Override`** | Engineer | Slice an enemy droid mid-fight and it stops fighting you. |
| **`Jury Rig`** | Machinist | Repair a droid beside you with a repair kit. |
| **`Still Standing`** | Marksman | When a hit would drop you, you get one more turn first. |
| **`Field Position`** | Agent | In cover you attack better, not just defend better. |
| **`Field Surgery`** | Doctor | You can heal wounds, which nothing else in the game can. |
| **`Nothing In My Hands`** | Brawler | Armour does not protect anyone from your fists. |
| **`Single Combat`** | Duelist | Pick an enemy — much better against them, slightly better against everyone else. |
| **`Plunder`** | Pirate | Drop someone, take what they were carrying, use it now. |
| **`Unrelenting`** | Sith Warrior | Below half health you hit harder. |
| **`Vanish`** | Sith Assassin | Kill from hiding and you are hidden again for free. |
| **`Chosen Weapon`** | Commando | Pick one weapon at entry; nobody is better with it than you. |
| **`Both Barrels`** | Gunslinger | With two pistols, every shot can go at a different target. |
| **`One Shot`** | Sharpshooter | Spend a round aiming and the shot cannot miss. |
| **`No Firing Position`** | Operative | Shoot from hiding at range and nobody knows where it came from. |
| **`Nobody Saw Him Leave`** | Shadow Hunter | Kill in melee and move away for free. |
| **`Bonded`** | Beast Master | A beast fights beside you. |
| **`The Long View`** | Jedi Sage | After seeing an ally's roll, add your Wisdom to it. |
| **`Consume`** | Sith Sorcerer | Anything that dies near you gives you Force points back. |
| **`Master of Forms`** | Sith Battlemaster | You hold two lightsaber forms and switch freely. |
| **`Combination`** | Brawler chain | Punch twice — landing the first makes the second easier. |

---

# 2 — ⚠ Fail — 4, and the failure has one shape

**⚠ Every one that fails does so for the same reason: a second mechanic bolted onto the first.**

## `Quarry` — Bounty Hunter

    Name a target: you know exactly how hurt it is, you can knock it out
    instead of killing it at no penalty, and at the top you hit it harder
    and it gets no cover.

**⚠ Three ideas — information, capture, and combat bonuses.** **The class's job is *bring them back alive*, and the third idea does not serve it.**

## `Command Protocol` — Droid Master

    You bring up to four droids; you order them all at once as a Bonus
    action; an order persists until done; an uncommanded droid takes cover.

**⚠ Four rules.** **Three are the *fix* for the decision cost `REPLY-31` raised — and a fix that needs three clauses is a sign the thing being fixed is expensive.**

## `Dominion` — Sith Inquisitor

    Your Force powers are harder to resist, and a save still leaves them slowed.

**⚠ Two ideas, and the second is a different mechanic — it converts a failure into a partial success.** **It was borrowed from an existing stun clause, which is why it reads as an addition rather than an extension.**

## `Read the Ruin` — Explorer

    A failed check tells you why it failed; you may retry once that is
    fixed; and you may take 10 under pressure.

**⚠ Three ideas.** **The first is the class. The other two are competence in general and belong in the skill rules if they belong anywhere.**

---

# 3 — ⚠ What the test caught that I would not have

**These four are not the ones I would have guessed.**

**I would have flagged `Command Protocol` and `Quarry` on length. I would not have flagged `Dominion` or `Read the Ruin`** — both read as tight in the drafts, and both fail because the tiers add a *kind* of thing rather than more of the same thing.

> **⚠ A chain is one line if its tiers scale one idea, and more than one if a tier introduces a second.**

**That is a sharper statement of the test than *count the clauses*, and it is what the four have in common.**

**`Vanish`, `Still Standing` and `Plunder` all have three tiers and all pass, because every tier does more of the same.**

---

# 4 — Not fixed, as instructed

**⚠ `REPLY-43`:** *"Any that cannot be stated in one line is flagged, not fixed. I want to see which ones fail before either of us decides what to do about them."*

**Flagged. No edits made.**

**⚠ One observation for whoever decides: three of the four fail on their *capstone*, not their base.** **`Quarry`, `Dominion` and `Read the Ruin` are all one line at tiers 1 and 2 and stop being one line at tier 3.**

**Which suggests the cheapest repair is to the capstone rather than the chain — and `Command Protocol` is the exception, since its extra clauses are at tier 1.**

---

# 5 — And these double as the identity lines

**`REPLY-43` is right that it is the same sentence.** **`CLASS-IDENTITIES-01`'s per-class line and `PT-178`'s player statement are the same object for every class whose identity *is* its feature.**

**⚠ They diverge for four classes** — `Tech Specialist`, which has no feature at all, and `Officer`, `Scoundrel` and `Vanguard`, which are undrafted.

---

# The question

> **⚠ Four fail. Three fail on the capstone alone and one at tier 1.**

**Still open: `FORCE-FORMS-01` unassigned, the unarmed ladder at 2.9× a weapon, and `Vanguard` without a purpose.**
