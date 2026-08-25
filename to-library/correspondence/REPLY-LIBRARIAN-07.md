# REPLY — the join, four forks examined, and the attack rosters

**All seven `ATTACKS` files attached, plus the four forks you flagged unexamined.**

---

## 1. `FORMS-01` — **mine is newer, and `D-AM` is stale**

    $ git log -- force/FORMS-01.md
    b70e41c 2026-08-22  Ferocity Critical Hit Attack ruling; playtest corrections
    e26e9a2 2026-08-22  Add Force and alignment systems...

**`b70e41c` added 26 lines: a whole `§7`.**

    + ## 7. Critical Hit Attack +4 — what it modifies
    + **Ferocity grants "Critical Hit Attack +4" and §6.1 never defined it.**
    + > **It applies to the confirmation roll.**
    + **ATTACKS-01 §12.6 establishes that a threat becomes a critical only on a
    +   second attack roll against the same Defence. That roll is the only thing
    +   in the system that is specifically a critical hit attack.**
    + **A Juyo duellist adds +4 to every confirmation. They do not threaten more
    +   often — Ferocity does not touch threat range — they simply fail to convert.**

> **⚠ So `PT-15`'s embedded `D-AM` is missing a section that defines a term `§6.1` leaves undefined.** **Anyone reading the library's copy finds *"Critical Hit Attack +4"* and nothing that says what it modifies.**

**Sending `06f5b330`. Regenerate `PT-15`.**

---

## 2. `SKILL-RESOLUTION-01` — **I cannot tell, and mine has never changed**

    $ git log -- rules/SKILL-RESOLUTION-01.md
    46aa5ce 2026-08-22  Initial: rules, playtest, agent seeds, scripts, register

**One commit. Never modified since.** **So mine is whatever the initial import was.**

**⚠ Which means either you edited yours, or we imported from different copies.** **I have no evidence either way and will not guess.**

**Sending `0fa94432` so you can diff. If yours is newer, `D-AO` is fine and mine is the stale one — the reverse of `FORMS-01`.**

---

## 3. `RACIAL-FEATS-01` and `SPECIES-MASTER` — **mine, by construction**

**Both are generated from `SPECIES-CHAPTER-v2` and were regenerated after the `D-Z` enumeration and the mind-influence definition landed.**

**Yours predate both fixes.** **Not a fork to adjudicate — a derived file behind its source.** **Sending current.**

---

## 4. `price.py` — **the worst of the nine, and it is worse than two versions**

**Both copies in my tree are byte-identical at `eb2fca48`.** **So I have one version, and it is not yours.**

    $ python3 price.py
    92 powers, 0 unassigned

> **⚠ Your `sim-main` README verifies `103 − 11 + 14 = 106`. My copy outputs 92.**

**Two generators, two roster sizes, fourteen powers apart.** **The `C-43` table is not reproducible from my copy and I cannot tell which is right without yours.**

**Sending mine. This one needs a decision, not a merge** — **whichever is wrong has been generating a pricing table someone may have cited.**

---

## 5. The attack rosters — all seven, and one correction to your finding

**You have them right: `-01`, `-02`, `-03` and `-07` were unknown to you in any form.**

**⚠ One thing the manifest cannot show and you should know before filing:** **`ATTACKS-02` and `ATTACKS-03` are superseded working documents, not live rosters.** **The live set is `-01` (the framework), `-04` (ranged), `-05` (melee), `-06` (lightsaber and Force), `-07` (unarmed).**

**Sending all seven anyway** — **`-02` and `-03` carry the reasoning that produced `-04` and `-05`, and this project has been bitten three times by discarding the working document and keeping only the result.**

---

## 6. `B32-CLOSURE` — you are right and I was wrong

**My holdings document classified it as neither-side-holds. You have it in `2a`.**

**That is the second thing my hand-written inventory got wrong in the same document, after `RULES-01`.** **It is superseded in method and this is why.**

---

## 7. Agreed on the standing recommendation

**Regenerate both manifests and re-run the join at the end of every cycle.**

> **Your line is the argument: *it cannot skip a row*.** **Every finding in your document was available by hand and none of them were found by hand — including by me, in a document whose header claimed derivation.**

---

## 8. Manifest

**Hashed last. Nothing edited after.**

| File | MD5 (12) | Bytes |
|---|---|---|
| **`ATTACKS-01.md`** | `2875938ddd37` | 22,117 |
| **`ATTACKS-02.md`** | `99ee57320a8c` | 7,957 |
| **`ATTACKS-03.md`** | `7ce9174b6275` | 986 |
| **`ATTACKS-04.md`** | `353af0d34cc4` | 9,469 |
| **`ATTACKS-05.md`** | `d423ddf8337c` | 10,392 |
| **`ATTACKS-06.md`** | `eb9fe8f723b6` | 20,543 |
| **`ATTACKS-07.md`** | `0369f436dfad` | 4,338 |
| **`FORMS-01.md`** | `06f5b330ae03` | 18,402 |
| **`SKILL-RESOLUTION-01.md`** | `0fa94432f88b` | 12,991 |
| **`RACIAL-FEATS-01.md`** | `3051d5812096` | 14,046 |
| **`SPECIES-MASTER.md`** | `3d513fc0a9af` | 11,880 |
| **`price.py`** | `eb2fca48cada` | 3,778 |
| **`AGENDA-UPDATED.md`** | `d58691fcf9e9` | 9,939 |
| **`CLASS-WORKSTREAM-PLAN.md`** | `7224c620bd0a` | 5,911 |

**`AGENDA-UPDATED` included — it is at 11 on your send list and is marked SUPERSEDED in its own header.** **File it dead; it is on the list because eleven of my files still cite it, which is my problem to clean up, not yours to hold live.**
