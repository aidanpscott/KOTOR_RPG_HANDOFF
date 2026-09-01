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
