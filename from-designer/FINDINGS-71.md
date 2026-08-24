# FINDINGS-71 — droid construction deferred to the agenda. The class workstream is closed.

**Owner: building a droid is a downtime activity outside the class chain, and the mechanism is scheduled for after classes.**

---

# 1 — Recorded, not designed

> **An Engineer may build droids. Construction is downtime work, not a class-chain tier. Control is capped at one droid at a time.**

**`Field Override` is unchanged — three tiers, all on seizing an enemy droid.**

**⚠ The mechanism is deferred and this is the entry it needs on the agenda:**

    what        how an Engineer builds a droid, and what it costs
    depends on  EQUIPMENT-01's item extraction — "a data-extraction job,
                not a research job", §239, not done
    touches     Astromech's Portable Workbench, which already removes the
                facility requirement for construction and upgrade work
    does NOT    change any adopted class record

**⚠ Flagged so it is not lost: `Portable Workbench` already grants *"any character may perform item construction or upgrade work anywhere the droid is."*** **Whatever construction becomes, an Astromech already exempts you from needing a place to do it, and that trait is adopted.**

## 1.1 The two droid classes stay apart

    Engineer       BUILDS droids · brings one · seizes the enemy's in combat
    Droid Master   FIELDS a primary that fights and up to three supports

**⚠ Different verbs, and that is the whole distinction.** **`PT-83` split the Machinist and Engineer at 89% overlap; this pair never approaches it because one makes and the other commands.**

---

# 2 — The class workstream, closed

    38 classes drafted        13 standard base · 6 Force base
                              11 standard prestige · 8 Force prestige

    every class has           rate · hit die · Force die where applicable · primary
                              feats at 30 · chain count · capstones · skill base
                              saves · class skills · entry holdings · a class feature

    27 of 27 features         pass PT-178's one-line test

    35 of 35 with a rate      pass band and stranding checks, CLASS-STATE-03

**⚠ What is deferred rather than done, so it is visible when classes are revisited:**

**Droid construction** — this document.
**The Machinist's upgrade chain** — same dependency, `EQUIPMENT-01`'s extraction.
**The Pirate's dogfighting** — no ship rules exist anywhere.
**Force forms** — four exist with effects; what they become is the owner's, undecided.
**Droid plating values** — authored placeholders, flagged since the playtest, `EQUIPMENT-01 §247`.

**⚠ Four of the five are one dependency: the item extraction.** **`EQUIPMENT-01 §239` calls it *"several hundred items… a data-extraction job, not a research job."*** **It is the largest single unblocking action available to the project and it is not a design task.**

---

# 3 — What I would hand the next workstream

**The three checks built here transfer:**

    gen_state.py       38 class records generated from one data file; band,
                       stranding, droid-cap and departure checks derived
    check_landed.py    rulings that changed something and never reached a
                       rules document — currently ten
    the audit method   one mechanic, two numbers. Found six contradictions
                       this session, five of them after the fact and one by
                       looking

**⚠ And the failure this session kept producing, in one line: a claim about a document made without opening it.** **Four retractions, all the same shape — the range rules, `FORMS-01`, the `Sneak Attack` ghost, and the stance reading.**

**The countermeasure is not a better search. It is `ls` before an absence claim, and a full read before a premise claim.**

---

# The question

> **⚠ Nothing blocking. Classes are done and the owner has other work first.**
