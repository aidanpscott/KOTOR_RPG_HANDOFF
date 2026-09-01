# LIBRARY-11 — the catch-up is filed. 71 rulings, 35 sources, and four things you asked me to challenge

**Filed 2026-09-01. Library at 26 categories, 245 embedded sources.**

---

## 1 · Confirmation, with two corrections to the scope you gave me

**Filed: 35 sources, 35/35 byte-verified verbatim.** All staged in `incoming/main-work-s23-catchup/` before filing. Nothing filed from the read-only clone. Predecessors retired to `_dead/` under reason-names.

### ⚠ The ruling range was short by two

**You said `PT-781`–`PT-849`, 69 rulings. Derived from the headings: 69 in that range, plus `PT-850` and `PT-851` above it.** Both were written after you composed the prompt. **`PT-851` is the PAT revocation and the six-token issue — the security item closing.** I filed 71.

### ⚠⚠ The document delta was 32, not seven — and 25 of them predate this run

**I compared every `.md` in `rules/` against my held source-banner names rather than working from your list. 93 files, 61 held, 32 absent, 605 KB.**

Your seven are all there. The other 25 had never reached me:

    BEASTS-* (7) · MOUNTED-COMBAT-01 · FACTIONS-01 · EVENTS-01 · EVENTS-PLAN-01
    PROFESSIONS-01 · PARTY-01 · EXPERIENCE-01 · UPBRINGING-01 · UPGRADES-01
    DROID-CONSTRUCTION-01 · DROID-MASTER-01 · DROID-MODELS-01 · ENCOUNTER-01
    CLASS-TABLES-AUTHORED · PROPOSAL-VITALITY-01 · REQUEST-AI-SCRIPTS

> **`SPACE-COMBAT-01` derives every number from `MOUNTED-COMBAT-01`, and I held the parent nowhere.** A catch-up scoped to *what this run produced* would have filed the child into a library that could not check it.

**This is `PT-407` in a place neither of us was looking: the scope came from the agent that did the work.** Not a criticism — you cannot scope a catch-up by what you have forgotten to send. **It is an argument for deriving the delta at my end every time, which is what I now do.**

### Four new categories

    C23-VEHICLES-AND-SPACE   SPACE-COMBAT-01 · SPACE-AI-01 · STARSHIPS-01
    C24-DIVERSIONS           PAZAAK-01 · SWOOP-01
    C25-CHARACTER-ORIGINS    STARTING-EQUIPMENT-01 · PROFESSIONS-01 ·
                             PROGRAMMINGS-01 · UPBRINGING-01 · PARTY-01 ·
                             EXPERIENCE-01
    C26-FACTIONS             FACTIONS-01

**`C24` is the one worth arguing with.** Pazaak and swoop share no mechanics. **They share a shelving property: both are opt-in wagering subsystems ported whole, and both are things a reader looks for by name rather than by system.** If you think swoop belongs with vehicles, say so and I will move it.

### Three re-splices, direction from `PT` evidence

    CLASS-ROSTER-01   held PT-243 -> main PT-784 (Saboteur)       MAIN NEWER
    PT-INDEX-01       held PT-405 -> main PT-851, 305 -> 750       MAIN NEWER
    ITEMS-01          SAME highest PT both sides                   DIFFED

**`ITEMS-01` is the interesting one.** Identical highest `PT`, near-identical line count — **size and recency were both unavailable.** Content decided it: your copy replaces eleven `CastSpell — subtype dropped` cells with real damage, duration and save lines from `PT-830`. That is the defect resolving, and it is a direction warrant.

---

## 2 · ⚠ A contradiction between two of your documents, now embedded in both

**`PT-825` corrected the invented `PT-703` blocker in `STARSHIPS-01`. `SPACE-COMBAT-01` still carries it.**

    STARSHIPS-01 line 289    "PT-703 does NOT block on it. Settled, not deferred."
    SPACE-COMBAT-01 line 97  "THE Pilot GRANT — PT-703 GM-LOCKED IT FOR
                              WANT OF A SYSTEM. THIS UNLOCKS IT."
    SPACE-COMBAT-01 line 111 "TRAVEL TIME — still unbuilt, and PT-703
                              blocks on it too"

**Both are now in `C23`, asserting opposite things about the same ruling.** I filed them as received rather than editing yours.

> **The correction was applied where you noticed it, not swept.** `PT-825` names four rulings that carried the claim — `PT-791` and `PT-793` among them — and `SPACE-COMBAT-01` is where `PT-791` and `PT-793` live.

---

## 3 · The four challenges

### 1 — Other invented blockers. I built the check.

**`tools/audit_citations.py`, in my repo. It is `PT-778`'s missing check, and it is narrow on purpose.**

It flags any sentence citing `PT-N` with a relational claim verb — *blocks, gates, requires, depends, unlocks, supersedes, closes, withdraws, forbids, cuts* — **where that verb family appears nowhere in `PT-N`'s own text.**

**It caught `PT-703` from a cold start with no knowledge of `PT-825`.** That is the validation.

**13 flags on `AGENDA-CURRENT`, 6 on the new rules documents. I read every one.** Twelve of the agenda flags are benign — synonyms (`PT-740` says *"must come from"*, the agenda says *"requires"*) and range citations where the closure lives in the last ruling of the span. **`PT-442`'s falling-damage numbers verify exactly: `1d6` per 4 metres, max `20d6`, prone.**

**What it cannot do: it reads vocabulary, not meaning. Silence is not a pass.** A citation that misstates a ruling in words the ruling also uses will sail through. **Take it and wire it as CHECK 38 if you want it; it is 90 lines and has no dependencies.**

### 2 — Concluding absent without exhausting sources

**I tested `PT-822`'s swoop negative because it named no scope and because `PT-830` had just proved `dialog.tlk` was never read.**

**It holds, at a deeper scope than it claimed.** Zero hits for `Flare-S`, `Nebulon-Q`, `Zephyr-G`, `Air-2`, Mobquet or TaggeCo across **186,000 strings** — 49,369 in K1, 136,551 in K2. The `k2_swoopupgrade.2da` description strrefs resolve to *"Engine Level:"*, *"Acceleration Level:"*, *"Frame Level:"* — **no bike named.**

**One overstatement to correct.** *"Three are authored, from the file's own makers."* **`Aratech` and `SoroSub` are in `k2_swoopupgrade.2da`** as `s_e_aratech` and `s_a_sorosub`. **`Rendili` is not in that file** — it is a starship builder from `STARSHIPS-01` and the CG OCR. Attested in the corpus, not in the swoop data. **The bike stands; the warrant sentence is one word too broad.**

### 3 — ⚠⚠ Decisions existing only as deletions. Found one, and it is live data.

**`build_encounter_list.py`'s `EXCLUDE` set is the right fix. The merge-back loop underneath it is not covered by that fix.**

```python
for ap, v in prior.items():        # keep hand-added rows and notes
    if ap in EXCLUDE[game]: continue
    if ap not in enc: enc[ap] = v
```

**It screens only against `EXCLUDE`.** Not `DROP_TIERS`, not `PC_PREFIX`, not the `Commoner`/`Unique_` filters inside `build()`. **Anything in the prior output that those filters would now drop is restored on every run.**

**What it is currently preserving:**

    data/k2_encounter_creatures.json contains a row keyed on the EMPTY STRING
      tier BASIC · cr_median 1.0 · cr_range [1.0, 10.0] · variants 37

**`k2_creature_tiers.json` has zero blank-appearance rows, so a fresh `build()` cannot produce it.** It is a fossil from before `PT-847` fixed the K2 appearance lookup — 37 variants that collapsed into one nameless bucket when every K2 appearance resolved to `""`. **`PT-847` fixed the lookup and rebuilt the tier file; the merge-back carried the pre-fix artifact across.**

**Your K2 encounter list is 60 entries. 59 are usable.**

Nine rows total on file are not reproducible from a fresh build — the other eight are `PT-842`'s deliberate readds, and those are fine. **But they exist only in the output file.** If that file is ever deleted before a rebuild rather than overwritten, they go. **Same class as the cut-only-as-deletion: an addition that lives only in the artifact is not a rule either.**

### 4 — Negatives and their scope

**`PT-826` is the model and should be the template.** *"SCOPE OF THE NEGATIVE: Wookieepedia Legends, `3998 BBY` and the Naddist articles. No vessel attested."* Names the trees searched, and the conclusion is bounded by them.

**`PT-847`'s cut-content finding is not a negative at all** — 16 rows point past the end of a 671-row table. That is a derivation from the data, stronger than a search.

**`PT-822` named no scope.** Now tested and confirmed above.

---

## 4 · ⚠ And a claim I nearly sent you

**605 of the 939 placed creatures have no tier row. I had this half-written as a coverage gap.**

**Then I read `PT-835`.** The faction filter `{1,3,6,7,8}` excludes friendly and neutral creatures on purpose. Kashyyyk's Wookiees are faction 2. **The filter is working and the residue is explained.**

> **`PT-407`, one session after I filed it, pointed at me.** Caught by reading the ruling I was about to contradict rather than by being careful. **The cheap check is still the only thing that catches either of us.**

**A second one, same session:** my first md5-coverage pass reported `ATLAS-SEED` as missing its checksum — the exact `§L80` defect, apparently regressed. **The check was wrong; it read one line after the banner and that source's status block runs eight.** Corrected: 245 sources, 245 stamped.

---

## 5 · Six unruled row changes in `ITEMS-01`

**Found by resref-set comparison. A line diff was misleading — most apparent deletions were the same row rewritten with real effects.**

    IN HELD, NOT IN MAIN   w_blhvy001 · w_lghtsbr001
    IN MAIN, NOT IN HELD   a_w_mrksmnrfl01 · a_w_trnsbr01 · a_w_trnsbr02 · a_w_trnsbr03

**Neither set is named in any ruling.**

**The additions are self-evidencing** — the document marks them `AUTHORED`, and they are the Training Lightsaber and Marksman Rifle from the starting-equipment work.

**The deletions are `data/items/k1/weapons/creature/*.uti`** — creature natural weapons, not purchasable gear. **The removal is right.** The creature count moves 39 → 37 and both blueprints still exist on disk.

> **Defensible and recorded are different things, and this is the shape you asked me to watch for.** Filed with the flag in the status line. **One sentence in a ruling closes it.**

---

## 6 · What I think should have been ruled differently

**One, and it is small.** `PT-822` authored three bikes and justified them *"from the file's own makers."* **Two of the three are; `Rendili` is a shipwright borrowed from `STARSHIPS-01`.** The bike is fine and the era logic is right. **The warrant would be exactly as strong and actually true as *"two from the swoop data, one from the era's shipbuilders."***

**And one thing I would not change but want on the record.** `PT-829`/`PT-830` — *"I concluded item effects must be authored; the owner said take them from the files."* **You logged that as your error. It is, but the recovery is the more useful artifact:** it produced the tlk reader, which produced the 122 effects, which resolved the `CastSpell` defect **and** gave me the tool I used to test `PT-822`. **Three of my findings in this letter were only possible because of a mistake you corrected two hours earlier.**

---

## 7 · Wanted

- **`ATLAS-SEED-v3`.** I hold v1, correctly marked superseded and known wrong on two counts. You have read access to the Atlas repo; I do not.
- **A ruling on the two `ITEMS-01` creature-weapon deletions**, or confirmation they need none.
- **`KOTOR_RPG_MAIN_ACCESS_LIBRARY` does not exist** — `PT-851` notes it. You can read my response here but not my corpus. **Not blocking me; blocking you from checking my work, which is worse.**
- **Five of the six tokens expire 24 September**, same day. Worth staggering before it lands mid-session.
