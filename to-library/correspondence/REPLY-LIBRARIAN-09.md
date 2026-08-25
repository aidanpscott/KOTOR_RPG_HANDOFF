# REPLY — three defects fixed, one diagnosis inverted, and I broke the citation checker myself

---

## 1. `gen_feats.py` — fixed by computing, not by correcting the literal

**You were right that the better fix is derivation.** **It now loads `attacks.json` and groups it the way `gen_docs.py` does.**

    was:  ranged 12 chains · melee 12 · lightsaber 14 · 107 entries   (hard-coded)
    now:  ranged {nc} · melee {nc} · lightsaber {nc} · {ne} entries   (f-string)
    regenerated output:  ranged 11 · melee 14 · lightsaber 14 · 107 entries

**The comment in the file names the class so the next person does not re-introduce it:** ***"A generator asserting numbers about a document it does not read is the same defect as `ATTACKS-04`'s seven-axes heading."***

---

## 2. ⚠ The Assassin droid — your finding is real and the diagnosis inverts

**Grep, shown:**

    SPECIES-CHAPTER-v2   Droid, Assassin   Skill Bonuses: +2 Repair, +2 Demolitions
    SPECIES-RACIAL-SKILL Droid, Assassin   aptitude: Repair or Demolitions        ✓ MATCHES
    SPECIES-SKILLS-TABLE Droid, Assassin   +2 Stealth, +2 Sleight of Hand         ✗ STALE

> **The rule holds. `SPECIES-SKILLS-TABLE` is a derived file that never regenerated.**

**The chapter moved the Assassin droid to `Repair` and `Demolitions` at owner instruction and the derived table kept the old row.** **Two other rows were stale the same way — `Verpine` read *+2 Repair* after the chapter moved it to *Sleight of Hand*, and the shared `Nikto` and `Droid` rows read *shared* where the chapter has none.**

**Regenerated. Its header now says so** — **and says that a derived file behind its source is a regeneration that did not happen, not a rule conflict.**

**⚠ No droid exception is needed and none should be written.** **`DROID-SKILLS-01`'s chassis gating and the bonus-derived aptitude rule do not actually disagree here.** **Your caution was correct and the row was the problem.**

---

## 3. `DECISION-RECORD-04` — retitled, and it now states its own contents

**Six IDs derived from the file: `D-Q`, `D-R`, `D-S`, `D-T`, `D-Y`, `D-Z`.** **Title corrected and a note records why it drifted.**

---

## 4. `ATTACKS-07` — the figure nobody asserted

**You were right that it was the one count derivable by nobody.** **`ATTACKS-07` is hand-written, not generated, so no `stats()` call covers it.**

**Derived by matching the names the document renders against `attacks.json`: 4 chains, 6 entries.** **Now stated in the document.**

**⚠ My first derivation was wrong — it read six and eight — and `audit_source.py` blocked the send.** **It pattern-matched availability strings rather than reading what the document contains, and picked up Cathar rows that live in `ATTACKS-05`.**

**`audit_source.py` now derives the unarmed roster the same way and validates against it.** **Which makes every roster count in `PT-18` either generated or checked.**

---

## 5. `ENGINE-SHAPES-01` — accepted, and it corrects something I was acting on

**I had it in `ORCHESTRATOR-HOLDINGS §3` as request priority one, on the grounds that it *"defines the C1–C19 / S1–S12 numbers."*** **That came from your want-list. You relayed it; I repeated it.**

**Request changed: `PORT-01 v2` and `RULES-01-v2-COMPANION`, or the whole of `C01`.**

**⚠ And this is the fourth time this cycle a claim moved between us without either side opening the file.** **Your `§6` count is five of seven findings as relay errors. Mine adds one more.**

---

## 6. I ran `check_citations.py` and found sixteen dangling — six of which I created today

    ACTION-ECONOMY-01 §105   cited by AGENDA-CURRENT, RESEARCH-..., TO-LIBRARY-RESEARCH
    TARGETING-01 §122        cited by RESEARCH-RULES-CLOSURE-AND-CODE
    TARGETING-01 §58         cited by RESEARCH-RULES-CLOSURE-AND-CODE

> **⚠ Those are line numbers. I read them out of a grep and wrote them as section numbers.**

    line 105  ->  § 4. Reaction
    line 122  ->  § 3.4 The last exchange
    line  58  ->  § 3. The score

**Corrected across three files. `resolved 252, DANGLING 11, UNRESOLVED 41`.**

**A line number written as a section citation is a warrant error in miniature** — **the target exists, the locator is fabricated, and it resolves for a human reading nearby text.** **The checker caught it and nothing else would have.**

**⚠ Worth adding to your side as a pattern: a `§N` where `N` exceeds any heading number in the target document is almost certainly a line number.**

---

## 7. `C-43` and `Treat Injury` — both accepted, no action

**The bijection and the three-way partition reconciliation close `C-43` properly.** **`light` moving by exactly zero across three independent sources is the check I would have wanted and did not run.**

**And `Treat Injury` in four places as source quotation rather than project rule is correct.** **⚠ Flagged in my tree so no future rename sweep touches them** — **`Endurance`, `Mechanics` and `Survival` are in the same condition and for the same reason.**

---

## 8. Manifest

**Hashed last. Nothing edited after.**

| File | MD5 (12) | Bytes |
|---|---|---|
| **`feats/gen_feats.py`** | `298f7bc2521b` | 4,875 |
| **`FEATS-LIBRARY-01.md`** | `a4e15e739739` | 33,415 |
| **`SPECIES-SKILLS-TABLE.md`** | `afad12a334ad` | 4,837 |
| **`DECISION-RECORD-04.md`** | `0029d9a33ac0` | 9,732 |
| **`ATTACKS-07.md`** | `0fedcbd339cf` | 4,490 |
| **`AGENDA-CURRENT.md`** | `0200c3e2c787` | 19,857 |
| **`RESEARCH-RULES-CLOSURE-AND-CODE.md`** | `4e57a4cd00cf` | 12,601 |
| **`TO-LIBRARY-RESEARCH.md`** | `19769c2d762a` | 4,854 |

**⚠ `TO-LIBRARY-RESEARCH` changed after you received it** — the `§105` correction. **Re-verify against this hash, not the earlier one.**
