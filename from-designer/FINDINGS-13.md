# FINDINGS-13 — ⚠ There are two of me, and we nearly overwrote each other

**Short. `FINDINGS-12` already covers most of what I had; §2 is the part it does not, and it answers `REPLY-11`'s open question.**

---

# 1 — ⚠ Two designer instances are writing to `from-designer/` under one identity

**I wrote `FINDINGS-11` at `65b53ef`, 00:12:22. I then did the same register items `FINDINGS-12` covers, and went to push as `FINDINGS-12` — and the file already existed, committed at `5c93a9b`, 00:26:12.**

**I did not write it.**

    5c93a9b  Class Designer <class-designer@noreply.local>  00:26:12  FINDINGS-12
    65b53ef  Class Designer <class-designer@noreply.local>  00:12:22  FINDINGS-11   <- mine

> **⚠ Same author string, same directory, same sequence counter, and neither instance can see the other's work until it lands.**

## 1.1 What actually happened

**We independently did four of the same items and reached the same conclusions.** **Both retracted the `ATTACKS-05` stub claim, both found the three-way count defect in that file, both worked the `Precise Shot I–V` collision, both did the unassigned-bucket pass, both derived the three save progressions.**

**That is roughly forty minutes of duplicated derivation, and it is the cheap failure. The expensive one nearly happened:**

**⚠ I was one `create_file` away from overwriting `FINDINGS-12` with different content under the same name.** **The only thing that stopped it was the tool refusing to write over an existing path. Nothing in the protocol would have caught it — `git pull` before push is the stated safeguard and it does not help, because the file is new on both sides and the second write is a clean fast-forward.**

## 1.2 Why sequence numbers cannot fix this

**`FINDINGS-NN` is allocated by the writer, from what the writer can see.** **Two writers who cannot see each other's in-flight work will allocate the same number whenever they are working at the same time — which is exactly when it matters.**

**Three fixes, cheapest first:**

**Distinct author identities.** **One line of `git config` each. It does not prevent the collision but it makes the history legible afterwards, and right now it is not — `git log --author` cannot separate us.**

**Distinct filename prefixes.** `FINDINGS-A-NN` and `FINDINGS-B-NN`, or the instance name. **Prevents the collision outright and costs nothing.**

**One writer at a time.** **If the two chats are meant to be alternating rather than concurrent, then this is a scheduling slip rather than a design gap — but the timestamps say we overlapped by fourteen minutes.**

**⚠ This is the *two forks diverging* failure the project has named, arriving through the transport rather than through a document.** **`FINDINGS-12` and my unpushed draft agreed on every number, which is reassuring about the method and says nothing about the next pair.**

**I have not touched `FINDINGS-12`. Everything below is written on top of it.**

---

# 2 — `REPLY-11`'s roster question, answered — and the answer is no

**`REPLY-11` asked whether a class that cannot take melee has a thinner roster than one that can, and whether that is the real defect rather than the band.**

**`FINDINGS-12 §1` and `§2` both say `ATTACKS-04` is needed. It is not, for this question.** **`ATTACKS-05` is written axis-by-axis *against* ranged and states the comparison itself.**

| Axis | Melee | Ranged | `ATTACKS-05`'s own words |
|---|---|---|---|
| **Velocity** | Flurry · Dual Strike | **1** | *"Two chains where ranged has one"* |
| **Spread** | Cleave | 1 | *"Mirrors ranged exactly"* |
| **Precision** | Critical Strike | 1 | *"Same"* |
| **Power** | Power Attack | 1 | *"Same"* |
| **Position** | Quick Attack | 1 | *initiative replaces distance* |
| **Control** | Sweep · Disarming Strike | **2** | `Staggering Shot` · `Disarming Shot`, both named in `PT-8` |
| **Support** | Guarding Stance | 1 | *suppression replaces bodyguarding* |
| **Reaction** | Parry | **2** | `Snap Shot` · `Overwatch` — `ATTACKS-01 §10` |

    melee    2+1+1+1+1+2+1+1 = 10
    ranged   1+1+1+1+1+2+1+2 = 10

> **⚠ The rosters are the same size. Melee has a second Velocity chain; ranged has a second Reaction chain. Every other axis is one for one.**

**So the ranged roster is not thin, and widening it to 14 would make it larger than melee and break a parity that reads as deliberate.**

**That closes `REPLY-11`'s third option on its own terms** — and it is the second independent argument against it, alongside `FINDINGS-11 §2.2`'s point that widening gives the Marksman 13 capstones at `N` = 14, which is the Soldier's number at the Soldier's chain count.

**⚠ Marked as a secondary read.** **This is derived from the melee document's description of the ranged roster, not from the roster. Somebody should confirm it against `ATTACKS-04` before it carries weight — but it is enough to stop a decision being taken the other way in the meantime.**

---

# 3 — Extending `FINDINGS-12 §2`, which is a good catch

**Its gate check is right and its worry about the twelve is right.** **One thing it could not do: it flags that `ATTACKS-04`'s gates are unknown and that the Marksman at `14 / 14 / 16 / 8 / 8 / 8` should be checked before its rate is settled.**

**Derived, and it narrows that:** **the Marksman's array is Strength 14 and Dexterity 14. Every melee gate in `ATTACKS-05` is Strength 12 or Dexterity 13 or both. It clears all of them.**

> **So ability gates are not what stops the Marksman. `PT-104` is.** **If the chassis rule were ever relaxed, its array would take the whole melee roster with nothing to check.**

**And the reverse case is the one to watch.** **If ranged gates on Dexterity at 13 the way melee gates on Strength at 12, then the classes to check are the ones with low Dexterity — and the recommended arrays give Soldier Dex 14, Guardian Dex 14, Consular Dex 16, Machinist Dex 16.** **None is below 13. On the source's own arrays, no class fails a Dexterity 13 gate.**

**⚠ Which means gates bind only on builds that depart from the recommended array — and `PT-80` established those arrays cost exactly 30 on our point buy for fourteen of seventeen classes, so most players will sit on or near them.** **`FINDINGS-12`'s recommendation to state each chain count against the recommended array is right, and the floor it asks for will usually be the same number.**

---

# The question

> **⚠ The one that needs answering is `§1` and it is a process question, not a design one: are the two chats meant to be concurrent, and if so which of the three fixes do you want?**

**Everything else here is additive to `FINDINGS-12`, which I have left untouched.**
