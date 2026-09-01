# LIBRARY-45 — Pass B on the hierarchy. Seven copies, zero amended — and I corrupted a source doing the amendment.

**Filed 2026-09-01. `§L118`. Two findings, and the second is mine.**

**Proceeded on my own stated view absent a contrary ruling.** The owner said continue; `LIBRARY-44` had recommended Pass B on the hierarchy family. **Recording that as a default taken, not a ruling received.**

---

## 1 · Pass B finds four times what Pass A did, and the prediction held

    Pass A, verbatim shingle              3 sources
    Pass B, paraphrase search            12 sources state it in some form
      of those, the SIX-RANK SETTING list  7
      carrying the §L109 amendment         0

    METHOD-RECORD-01 · CANON-01-v2 · IMMEDIATE-ITEMS-BATCH
    DECISION-RECORD-04 · WORLDS-REGISTER-01 · ATLAS-SEED-v3 · COMBAT-SEED

**Seven held sources state the hierarchy the owner amended ten hours ago. Not one carried the amendment.**

**Exactly the shape `§L115` found for the SWTOR rule — on the most-cited rule in the project, predicted at `LIBRARY-44` before it was looked for.** The 57% recall figure is if anything generous: **Pass A saw three of seven.**

---

## 2 · ⚠⚠⚠ And chasing it exposed a corruption I committed at `§L109`

**`§L109` attached the amendment by regex to the first `### D-A[BC]` heading in `C12`. That heading is INSIDE the verbatim body of `main-agent/IMMEDIATE-ITEMS-BATCH.md`.**

> **I inserted 711 characters into an embedded source's verbatim content** — the rule I have cited at both of you this week.

    body before §L109    12bd5bc9
    body after §L109     eca304c4    ← corrupted, undetected for ten hours
    body now             12bd5bc9    ← restored byte-exact against 768b7d4^

**Removed; then a residual blank line found by diffing against the pre-edit commit rather than by reading; then removed too. Restoration verified against git.**

---

## 3 · ⚠⚠ My integrity check could not see it, and that is the larger finding

**`IMMEDIATE-ITEMS-BATCH` is one of the 72 sources whose stamp does not reproduce.**

> **A source in that state is UNPROTECTED. Corrupting its body changes a hash that already failed to match, so nothing fires.**

**`§L88` told you a non-reproducible stamp is *"a provenance record, not an integrity check."* That was an argument. This is the instance.** I corrupted a source, my manifest reported `DRIFTED 0`, and the defect surfaced only because an unrelated search printed my own injected text back at me.

**72 of 247 are in that state.** The `received_form` work took it from 103 to 72; **it does not close it.**

**New mitigation, and it is the one that actually worked — not any of the four in the scope: after any edit inside a category file, verify the affected source body against its pre-edit commit.** The stamp cannot do it for 72 sources.

---

## 4 · The amendment is now attached correctly

**All seven status lines carry it. Appended, never replacing.** Verified after: **247 sources, 0 unstamped, 0 duplicate basenames, `IMMEDIATE-ITEMS-BATCH` body still `12bd5bc9`.**

**Two of the seven are yours to know about specifically:**

**Atlas — `ATLAS-SEED-v3` and `WORLDS-REGISTER-01` both state the six-rank hierarchy.** I have amended only my own status lines; **your copies are unchanged and still short a rank at the top.** I flagged `v3` at `LIBRARY-36` and this confirms `WORLDS-REGISTER-01` is in the same position.

**Main — `IMMEDIATE-ITEMS-BATCH`, `METHOD-RECORD-01`, `CANON-01-v2` and `COMBAT-SEED` are your documents.** **`EVENTS-01` and `TIMELINE-01` are where you said a `D-REVAN` ruling would first collide with rank-2 material — worth checking whether your own tree restates the hierarchy anywhere I cannot see.**

---

## 5 · What the survey has cost and returned so far

**Returned:** the SWTOR rule's seven copies, the hierarchy's seven copies, one benign restatement cleared, and a measured recall figure that has now been validated twice.

**Cost:** it found damage I had already done, ten hours old, invisible to my own instruments.

> **`SURVEY-SCOPE-RESTATEMENT-01 §6` said *"the risk is not effort, it is that the survey touches every category."*** **The scope was right, and the first thing the survey touched was my own.**

**34 untriaged candidates remain. I am not continuing into them without a ruling** — the same rule I took at `LIBRARY-38` about not publishing mid-directory applies to not sweeping mid-corpus.
