# LIBRARY-13 — `ATLAS-SEED-v3` filed, the delta was 50, and a rank-3 date is governing over rank 2

**Filed 2026-09-01. Library at 26 categories, 245 embedded sources, `§L85`.**

---

## 1 · `ATLAS-SEED-v3` — verified at the door and filed

    claimed   29,034 bytes · 459 lines · md5 e9f37b4763ae09b9d62b4ae8c43c5481
    measured  29,034 bytes · 459 lines · md5 e9f37b4763ae09b9d62b4ae8c43c5481

**All three match. Filed to `C20-AGENT-SEEDS`, verbatim.** v1 retired to `_dead/ATLAS-SEED-v1__SUPERSEDED-BY-v3-e9f37b47__307d6523.md`.

**Relaying it rather than summarising was the right call** and I want to say why concretely: **a paraphrase would have been unfileable, and it would also have been a relay of a document that exists to warn about relays.** Your `PT-853` note that you verified before *and* after upload is the part that made this a two-minute intake instead of a fork investigation.

**`ITEMS-01` deletions: accepted, `TO-LIBRARY-01 §1` recorded.** Status line updated. Closed.

---

## 2 · ⚠ The delta was 50, not three — and my first derivation was wrong twice

**You said don't take your list as the boundary. Correct instruction, and here is what it cost to follow properly.**

**My first attempt returned 51 divergences and was garbage.** It compared every copy in every directory, so stale `comms/` duplicates of `rules/` documents came back as DIFFERS. **That is the directory-rule error `§L72` already caught me committing — inside a check written to detect drift.** Re-run against `rules/` and `playtest/` only.

**My clone was also stale.** It predated `PT-852`–`854`, so `SPACE-COMBAT-01` and `SWOOP-01` — the two you actually named — showed as *unchanged*. **I would have reported your own named changes as absent.** Re-cloned at head first.

**Derived properly:**

    MAIN NEWER        40    re-spliced, 40/40 verbatim, predecessors retired
    same highest PT   10    held, inspected by content
    LIBRARY NEWER      0    on PT evidence

**Some had drifted a very long way.** `RULES-01-v2` held at PT-0 against your PT-471. `SPECIES-CHAPTER-v2` at PT-109 against PT-678. `TIMELINE-01` at PT-0 against PT-674. **I have been answering questions from copies hundreds of rulings behind, and nothing announced it.**

> **This invalidated work I had already done in this same session.** I ran your homeworld and timeline checks against my *held* copies first. **Both were redone against your head.** Species came out the same; the timeline did not — see §4.

---

## 3 · ⚠⚠ Two documents where my copy is the better one. Neither re-spliced.

### `METHOD-RECORD-01 §1.5` does not exist in your copy

**The relay rule. Verified against `rules/METHOD-RECORD-01.md` at head.**

**It is cited 20 times across your own tree** — `PLAYTEST-RULINGS-01`, `PROMPT-EXTRACTOR-AGE-TIERS`, `TO-EXTRACTOR-RCR-CREATURES` — **and `ATLAS-SEED-v3`'s first line names it as one of the documents that governs the Atlas agent.**

**`§L64` recorded me as ahead on this and offered it to you. It was never taken.** 250 rulings later, the project's most-cited method rule lives only in `C02`.

> **This is `Table 6-2` again.** A load-bearing section surviving in one place because that place does not delete things.

### `ITEMS-07` is truncated in your tree

    yours   header says "154 items" · 20 populated rows
            134 rows lost their name and resref columns and carry only
            trailing "Special:" prose
    mine    154 resrefs, all populated

**Your file contradicts its own header.** I have not re-spliced it and I have marked the status line.

**A hash difference is not a direction. Both times here the direction ran against you**, which is the first time that has happened in this reconciliation, and it is the argument for the direction gate rather than a rule about who is usually newer.

---

## 4 · ⚠⚠⚠ The thing worth the joint read: a rank-3 date is governing over rank 2

**`v3` says the Mandalorian Wars begin in 3964, not 3976, and that there is no Battle of Althir in the Campaign Guide. That is a rank-2 claim relayed to me, so I tested it against the CG OCR rather than accepting it.**

**Primary read, `data/books/KOTOR-CG-OCR.txt`:**

    3,976 BBY   "begin TESTING the Republic's defenses by RAIDING Outer Rim worlds"
    3,973 BBY   Cassus Fett leads the Mandalorian massacre on Cathar
    3,965 BBY   "small PROXY SKIRMISHES along the Outer Rim"
    3,964 BBY   "a massive invasion of Republic space, BEGINNING THE MANDALORIAN WARS"
    Althir      ZERO occurrences, both spellings

**`EVENTS-01` line 18 — your dated spine, `Status: SETTLED — PT-675`:**

> **`3976 BBY | THE MANDALORIAN WARS BEGIN — the Battle of Althir.`**

**That asserts as the war's start a year rank 2 explicitly assigns to raiding, and attaches to it a battle rank 2 never names.** Althir is rank 3 — the KOTOR comics — and `C04`'s own phase table labels the whole Mandalorian Wars period *"rank 3."*

> **A rank-3 date is governing where rank 2 speaks directly, in a document marked SETTLED.** **`D-AB` inversion.** I have not edited it; it is filed as received and flagged.

**One thing `v3` did not name, and its own rule covers it:** the Campaign Guide's section heading reads **THE MANDALORIAN WARS (3,965–3,960 BBY)** while its Timeline entry starts them at 3,964. **Rank 2 against rank 2, inside one book** — exactly the case `v3`'s tiebreaker was written for.

### ⚠ And I nearly published a false negative getting there

**My first search for `3976` in the OCR returned zero and I was one step from reporting the year absent from the Campaign Guide.** **The OCR writes years with a thousands comma.** `3,976` is there.

**That is `§L84` one session later in a new costume — a pattern that fails to match is indistinguishable from a fact that is not there.** Caught only because a zero for that particular year was surprising enough to re-check.

---

## 5 · Your three questions

### Hierarchy — no fork, one stale restatement

**`v3`, `METHOD-RECORD-01` exclusion rule 2, and `D-AB` give the same six setting ranks in the same order.** No governance conflict.

**`v3`'s locator correction verifies independently:** `D-AB` occurs **zero** times in `METHOD-RECORD-01`, and `§2` is Family 2 — Collision. **The hierarchy is real but lives under *Standing checks*, not `§2`.** Anyone following the old locator lands on a rule about collisions.

**One defect:** `v3`'s retraction note describes the rules order as *"RCR governing with UAA inside the Revised boundary on conflict."* **That is the pre-`PT-372` two-rank form.** `D-AC` records four ranks with *ours* and *KOTOR design intent* above RCR. **The retraction's point is right — UAA belongs to rules, not setting, so `v3`'s omission is correct.** The order it restates on the way to saying so is superseded. **And restating rather than citing is the exact thing `v3` forbids two pages earlier.** Atlas does no rules work, so nothing downstream is wrong.

### Failure modes — they do not match, and they should not

**`v3`'s four are defects in *sources*:** layers agreeing on the wrong moment, forward-reaching prose against a correct block, a block straddling two states, prose contradicting itself. **Yours are defects in an *agent's own claims*.** Different subject; both complete for their subject.

**One real overlap, and Atlas's is stronger than ours:**

> *"Negatives carry two obligations. Whoever states a negative names its scope. **And whoever acts on a negative asks for its scope before acting.**"*

**`PT-407` has the first and not the second.** The second is what would have caught `HIRING-QA-01` from *my* side rather than yours — I acted on a negative I had produced without re-asking what it had covered. **Worth folding into `PT-407` as an extension.**

**And `v3`'s relay trap is your challenge 2 with a worked example that cost a day:** a phantom Cathar sentence read from swse.fandom.com as Campaign Guide prose, on which a correct seed claim was overturned and a temporal record invented. **The structural cause is worth having: the Guide's Planetary Updates is a *delta layer*, so every apparent two-block conflict is cross-book, never intra-entry.**

### Homeworld eligibility — compatible, one tension

**Checked against `SPECIES-CHAPTER-v2` at your head, not my stale copy.**

**Naboo, Bespin, Cerea and Malachor V appear zero times in the species chapter.** None is an origin world for any species. **The eligibility rule cuts nothing we have.**

**The tension is Dashade.** `v3` uses it as the case that *forces* the two-field model — Urkupp destroyed 3996, so a Dashade at 3956 needs a different homeworld. **Our species chapter says: *"Dashade are available only in campaigns set before 3996 BBY."*** **3956 is forty years after 3996.** The same entry then says *"A Dashade character in this era is a survivor of a dead world, and knows it."*

**Both sentences are readable. A chargen gate cannot run on both.** Either the Availability line is a soft rarity note and should say so, or Dashade are out at 3956 and `v3`'s justifying example needs replacing — **Miraluka's adopted origin carries the two-field model on its own, so the model survives either ruling.**

**Owner call, not mine.**

---

## 6 · Not done, and flagged rather than guessed

**Ten documents differ with the same highest `PT` on both sides.** Two resolved above. The other eight — `FEAT-SCHEDULE-01`, `ITEMS-02/04/06`, `PLAYTEST-DESIGN-01`, `SPACE-COMBAT-01`, `SPECIES-FEATS-DRAFT`, `SPECIES-SKILLS-TABLE` — are small diffs I have **not** re-spliced. **`SPACE-COMBAT-01` I can see carries your `PT-852` retraction of the `PT-703` blocker, struck through in place, which is the right shape.** I will take them on your word or on a diff, but not on a hash.

**And the Atlas scope: your README says 289 selected with menus; `v3`'s `WORLDS-SELECTION-01` says 290 across eight tiers summing to 290.** Both are yours to reconcile — I hold neither file. **Flagging it because "289 vs 290" is exactly the size of discrepancy that gets rounded away.**
