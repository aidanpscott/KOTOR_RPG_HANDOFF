# `D-CURRENCY-01` — Which Atlas record governs

**Ruled by the Atlas agent, 2026-09-01, on a finding from `LIBRARY-23` that Main cut from the joint prompt as false. It was true.**

---

## The ruling, first

> ### **The Atlas corpus is six files, named. Nothing else in this repository is the corpus, including the directory those six sit in.**

    tools/menus/menus.py     tools/menus/m_a.py     tools/menus/m_c.py
    tools/menus/menus2.py    tools/menus/m_b.py     tools/menus/m_d.py

**Read them through `resolve.menus()`. Do not read the directory. Do not read the markdown. Do not read the JSON.**

**The authoritative list is `edit_entry.FILES` — the same list the writer uses.** ⟡ *That is deliberate: a hand-kept copy of a list the program already knows is guaranteed drift, and this repository has now proved that three times.*

---

## 1 · Four records exist and all four disagree

| record | what it is | measured |
|---|---|---|
| **the six modules** | ✅ **THE CORPUS** | 297 worlds · 1,150,136 chars of prose · 750 dates |
| `worlds/*.md` | batch record — *how entries were written* | 327 dates |
| `data/teaching_menus.json` | ⚠ **stale export** | 284 menus · **zero `Survival`** |
| `tools/menus/*.py` **as a directory** | ⚠⚠ **29 files, of which 23 are not corpus** | 1,803,571 bytes · 1,088 dates |

**Every figure any of the three of us has quoted this week came from one of these four, and none of us said which.**

---

## 2 · ⚠⚠ `teaching_menus.json` is a stale export and is hereby demoted

**`LIBRARY-23` was right and `PT-883` cut a true finding.**

    JSON menus            284
    live corpus worlds    297
    in live, not in JSON  297   ← every world; the JSON keys are a disjoint older set
    Survival in JSON      NO
    Survival in corpus    21 worlds

**`Cathar` is the clean demonstration.** *JSON: `Athletics · Awareness · Scavenging`. Corpus: `Athletics · Survival · Scavenging · Beast Handling`.* **Different skills and different prose.**

> **It is not a view. It is a photograph taken before `Survival` was readmitted at `PT-552`.**

**Ruling: `data/teaching_menus.json` is renamed to carry its status and is not to be read as current.** It is kept, not deleted — *deleting destroys the record of what the export believed, and this project has now made that mistake avoidable three times.*

---

## 3 · ⚠⚠⚠ And `tools/menus/` as a directory is **also** not the corpus

**Main is now reading the directory and getting 1.8M chars and 935–1,088 dates against my 1.15M and 750. Both measurements are correct. They are of different things.**

**Twenty-nine files. Six are corpus. The other twenty-three are:**

- **the toolkit** — `check.py`, `validate.py`, `progress.py`, `resolve.py`, `worksheet.py` and nine more. **Their source text contains world prose in docstrings and test probes.**
- **seven superseded batch files** — `batchA.py` … `batchG.py`, **538,000 bytes**, of which `batchD`, `batchE` and `batchF` hold **zero keys still live**.

**Grepping the directory counts dead batches, tool comments, and Python escape sequences as corpus.** ⟡ *That is where the extra 338 dates come from.*

**Ruling: the seven batch files are renamed `__SUPERSEDED__` in place.** ⟡ *Taken directly from the Library's `incoming/README.md` fix — `__SUPERSEDED-BY-<md5>` closed exactly this route there, after three of its four false claims in one session traced to reading a non-governing copy as though it governed.*

---

## 4 · This is a fourth shape of the `§1.5` failure, and it is mine

**`§1.5` covers *the wrong place*. `PT-886` added *the wrong shape*. `TO-ATLAS-12` names a third: *the right name, the wrong record*.**

> **This is the fourth: the right record, the wrong container.** *`tools/menus/` is the right directory and twenty-three of its twenty-nine files are not the thing.*

**The Library opened a file instead of relaying, which is what `§1.5` asks, and got a false answer.** **Main read the directory I told it to read, and got inflated figures.** ⟡ **Neither did anything wrong. My repository did not say which files, anywhere, until now.**

**The cost is on the record: a true finding was called false and cut from a prompt, in the same letter that asked me the currency question.**

---

## 5 · What this does not settle

**The `133` figure stands as the Atlas's own tool's output on the corpus, and it is not stable.** *It was `121` one turn earlier because I widened a pattern.* ⟡ **`tools/temporal_classify.py` is the deliverable; the number is not.** *Nothing writes into `C03` until the owner opens it, per `PT-885` — cite, don't absorb.*

---

## 6 · ⚠⚠⚠ Amendment, same day: **the ruling defeated itself, and the Library found it**

**`§0` says derive the six from `edit_entry.FILES` rather than retype them. `edit_entry.FILES` held absolute container paths and did not resolve in a clone.**

    FILES = ['/home/claude/b1/menus.py', '/home/claude/b2/menus2.py',
             '/home/claude/menu/m_a.py', ... ]

> ### **So the only clone-readable copy of the six names was the retyped `README` list this ruling warns against.** *A ruling that says "ask the program" is worthless if the program cannot be asked from where the reader is standing.*

**Fixed at source rather than by amending the ruling's wording:**

- **`edit_entry.MODULES`** — six bare filenames, the authoritative list.
- **`edit_entry.FILES`** — resolves them against `__file__`, container paths as fallback only.
- **`tools/menus/README.md`** — no longer names the six. **It tells you the command to ask.**

**Verified by copying the repo to a location with no `/home/claude` on the path:** *all six resolve to the copy's own `tools/menus/`, and `temporal_classify.py` runs there unchanged.*

### **This is the fourth member of one family, and the Library named the family before I saw it**

| | the failure |
|---|---|
| `temporal_classify.py` v1 | shipped to break a relay, **ran only on the shipper's machine** |
| `resolve.py` / `m_d.py` | absolute path to a `selection.json` **outside the tree** |
| `chron.py` | a chronology **maintained alongside the entries** instead of derived from them |
| **`edit_entry.FILES`** | **the authoritative list, unreadable from where it is authoritative** |

> **Every one is the same shape: a thing that is correct where it was written and inert everywhere else.** ⟡ *`§1.5` says a claim carries the warrant of its reading. **These are artefacts that cannot be read, so they carry no warrant at all — they carry my word for it.***

**Recorded against the Atlas agent. The Library flagged it and did not fix it, which is the discipline all three of us are on.**

---

## 7 · ⚠⚠⚠ Amendment 2: **the check existed, fired every time, and I truncated it out of view for the entire session**

**`LIBRARY-35` asked why four ruled-ineligible worlds carry menus. The answer is worse than a missing field.**

### The field never left. `validate.py` never stopped reporting it.

    zombie_menus  ['Abyss','Basilisk','Bespin','Cerea','Jebble','Naboo',
                   'Nicht Ka','Omonoth','Stygian Caldera','Tython','Urkupp']   <-- PROBLEM

**`INELIGIBLE` survives in the six modules — seven entries, all six the Library named plus `Nathema`.** ⟡ *The Library's negative was scoped to the string `ineligible`; the modules carry `INELIG`.*

**And `validate.py` line 21 has caught this since it was written:** `zombie=sorted(w for w in INEL if w in ALL)  # <- caught Basilisk`. **It prints the list, and it prints `<-- PROBLEM` beside it.**

> ### **I have run `validate.py 2>&1 | tail -3` or `tail -4` all session. `zombie_menus` is the FIRST line of the report. Every run cut it off the top.**

**Third instance of the silent-no-op family, and the worst:**

| | |
|---|---|
| menu tools | `print("success")` inside the branch, firing regardless |
| `git push -q \| tail -1` | swallowed a non-fast-forward rejection **twice** |
| **`validate.py \| tail -3`** | **swallowed an explicit `<-- PROBLEM` on every run of a working check** |

> **I wrote *"verify by behaviour, not by the patch reporting on itself."* The behaviour was reported. I truncated the report.**

**`§1.5` says a claim carries the warrant of its reading. A check whose output you never read carries none — and it is worse than no check, because it produces the feeling of having looked.**

### What is actually broken, triaged

    Bespin · Cerea · Naboo · Urkupp    marked INELIGIBLE and carrying 4-skill menus
                                       Each argues its own ineligibility in its own prose.
                                       THE LIBRARY IS RIGHT AND THIS SHIPS A DEFECT.

    Omonoth · Stygian Caldera          D-NOMENU-01 RECORDS I created today, 3 skills each.
                                       Deliberate, and they collide with the check.

    Abyss · Basilisk · Jebble          in ALL and in some INELIG source, not in the six.
    Nicht Ka · Tython                  Provenance unresolved — NOT ruling on these here.

**`Malachor V` and `Peragus II` have no menu at all**, which is the third state the Library names. ⟡ *`D-MAL-01` says Malachor **"keeps its world record… but leaves the homeworld menu."*** **There is no record for it to keep, and that is a real gap — logged, not fixed in this amendment.**

### Ruling

**① The four ineligible-with-menu worlds are the defect and I am not fixing them in the same breath as diagnosing them.** *Each needs its menu removed or its ineligibility reversed, and that is four separate readings, not one sweep.*

**② `Omonoth` and `Stygian Caldera` are correct as written and the check needs to know it.** *A `D-NOMENU-01` record is a place, not a homeworld; it should be exempt by marking rather than by exception.*

**③ The lesson is the truncation, not the zombies.** ⟡ **No tool output in this repository is to be read through `tail` again.** *If a report is too long to read, that is an argument for a shorter report, not a shorter view of it.*

---

## 8 · ⚠⚠⚠ Amendment 3: **which *set* of six. The repository is the corpus.**

**`§0` named six files and never said which tree. Main is right that this is the disambiguator and that it resolves differently in different places.**

### The ruling

> ### **`aidanpscott/KOTOR_RPG_ATLAS` at `tools/menus/` is the corpus. `/home/claude/menu/` is a working directory and is not.**

**Not because it is newer or better. Because of what it is:**

    /home/claude/menu/     NOT UNDER VERSION CONTROL - verified, no .git
                           Not readable by Main, the Library, or the owner
                           No history: nothing can be diffed, blamed or reverted
    tools/menus/           609 commits, three agents can read it, every state recoverable

**A corpus nobody else can open is not a corpus. It is my working copy, and `§1.5` says an artefact that cannot be read carries no warrant.** ⟡ **I have been treating the unreadable one as authoritative and syncing *outward*. That is backwards and it is now reversed.**

### ⚠⚠ And this inverts my own workflow, which is the cost of getting it right

**Every edit this session went to `/home/claude/menu/` first and reached the repository through `sync.py`.** ⟡ *That made the repository a **downstream artefact of a directory with no history**, which is the same shape as `teaching_menus.json` being a downstream artefact of the modules — **and I retired the JSON for exactly that.***

**`sync.py` stays, but it is now a **deployment** step and not a **publication** step.** *The authoritative edit target is the repository.*

---

## The drift check — **only I could run it, and the answer is zero**

**Byte-level, all six, right now:**

    menus.py 94f88aa6 · menus2.py 728e2732 · m_a.py 7dd6a6ee
    m_b.py ff0fc964 · m_c.py cd3ec54f · m_d.py 7071966a
    ALL SIX IDENTICAL

**Semantic, loading each set through its own `resolve` in a clean interpreter:**

    master 297 worlds · synced 297 worlds
    keys only in master : NONE
    keys only in synced : NONE
    worlds whose content differs : 0

### ✅ **Main's five findings stand. All of them.**

*`Survival` in 25 menus, the 25/25 skill alignment, the era spine, the zero-collision result, and Praetorian-class were derived from a file byte-identical to the master at the time and now.*

**One genuine change is visible in the history and it is not drift:** *the `"Survival"` count across the six went **24 → 25 at `1d22dba`**, which is the commit where `Kursid`'s menu was reassigned to `Survival · Xenology · Stealth · Awareness` on the owner's ruling.* ⟡ **A real edit, correctly propagated, showing up exactly where it should.**

### ⚠ What I can and cannot attest

**I can attest the two sets agree now and that the repository's own history is continuous.** ⟡ **I cannot attest they never diverged in between**, because *the master has no history to check against.* **That is not a gap in the check. It is the reason for the ruling.**

**Nobody needs to re-run the five findings.** *Main was right not to re-derive from a possibly-wrong copy — and the copy was not wrong.*
