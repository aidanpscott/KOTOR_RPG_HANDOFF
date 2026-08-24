# FINDINGS-75 — ⚠ The seven entry requirements were never missing. They were never written down.

**`REPLY-56` and `REPLY-57` both list seven standard prestige classes with no entry requirement. All seven have had one since they were drafted.**

---

# 1 — They are in `from-designer/`, not in `docs/`

**Derived — every `Entry:` line I have pushed, deduplicated:**

    Commando        level 10, Soldier 6, Weapon Specialization in the chosen family
    Gunslinger      level 10, Smuggler 6 or Pirate 6, Master Two-Weapon Fighting
    Sharpshooter    level 10, Scout 6 / Marksman 6 / Bounty Hunter 6,
                    Weapon Specialization: Blaster Rifle
    Shadow Hunter   level 10, Agent 6 or Smuggler 6, Stealth 8
    Beast Master    level 10, Scout 6 or Explorer 6, Beast Handling 8
    Scoundrel       level 10, Smuggler 6 or Agent 6, Stealth 8
    Officer         level 10, Soldier 6, Persuade 8

    Juggernaut      level 10, Soldier 6, Heavy Armour Proficiency
    Droid Master    level 10, Engineer 6 or Machinist 6, Repair 8
    Operative       level 10, Agent 6, Stealth 8
    Tech Specialist level 10, Engineer 5 or Machinist 5

**Eleven of eleven standard prestige classes. ⚠ `REPLY-57` says four of eleven got filled in; the true figure is eleven of eleven, and seven of them never left `from-designer/`.**

## 1.1 ⚠ This is `check_landed.py`'s exact failure mode, and the check could not see it

**`FINDINGS-59` built the check on a simple rule: a ruling is landed when its ID is cited in the document it governs.**

**⚠ These were never given an ID.** **They were written inside class records — one line each, in a table, alongside the dice and the saves — and adopted as part of the class rather than as rulings of their own.**

> **The check finds rulings that did not reach a document. It cannot find content that was never a ruling.**

**`REPLY-51` named this gap and I said in `FINDINGS-60 §3` that no script could close it:** *"a decision with no ID and no contradiction leaves no artefact."*

**⚠ That was right, and this is the artefact it produces instead — the same content asked for twice, one exchange apart, by someone who had adopted the classes containing it.**

## 1.2 ⚠ And there is no document for them to land in

**Grepped `MULTICLASS-01`. It holds the *mechanism* — `§2.2` *"there is no entry credit"*, `§106` on when credit applies — and no class's requirements.**

**`CLASS-ROSTER-01` names the classes. `CLASS-ATTACKS-01` holds rates and chains. `FEATS-LIBRARY-01` holds feats.**

> **Nowhere in the corpus is the place where *what you need to enter a prestige class* lives.**

**⚠ Which is why they never landed. They had no destination, and eleven separate class records is not a destination — it is eleven places to look.**

---

# 2 — The fix is a document, and it is small

**A `PRESTIGE-ENTRY-01` holding nineteen rows: eleven standard, six Force, and the two `PT-215` cut as ranks recorded as cut.**

**⚠ Every row already exists. This is a transcription, not a design task, and it is the last thing between the prestige tier and being checkable.**

**And it gives check 21 and `check_landed` something to test against, which eleven scattered class records never could.**

---

# 3 — The Force six, for the same document

**Under `PT-214` and `PT-215`:**

    Jedi Weaponmaster   any Jedi base 6, Weapon Focus: Lightsaber
    Jedi Watchman       any Jedi base 6, Stealth 8
    Jedi Sage           any Jedi base 6, Mysticism 8
    Sith Marauder       any Sith base 6, Weapon Focus: Lightsaber
    Sith Battlemaster   any Sith base 6, Weapon Focus: Lightsaber
    Sith Sorcerer       any Sith base 6, Mysticism 8

**⚠ `Marauder` and `Battlemaster` share an entry exactly.** **Both are `any Sith base 6` plus `Weapon Focus: Lightsaber`, so the gate sorts neither from the other.**

**Not a defect — `PT-214`'s principle is that the holding sorts, and these two are genuinely the same door into two different rooms. Recorded because it is the only duplicate pair in nineteen.**

---

# 4 — On the `Officer` carrying leadership alone

**`REPLY-57`: it is now the only class doing it, so build it accordingly.**

**⚠ `Give the Order` as drafted is one ability: spend your declaration, an ally attacks now.** **That was priced as one leadership feature among three. As the only one, it is thin.**

**I have not changed it — the owner's next items are starting attacks and first-level multiclass benefits, and `Officer` was not named. Flagged as due for a second look.**

---

# The question

> **⚠ `§2` — a `PRESTIGE-ENTRY-01`? Every row exists; there is nowhere to put them, which is why they were asked for twice.**

**And `§4` — does the `Officer` get a second look now that it carries leadership alone?**
