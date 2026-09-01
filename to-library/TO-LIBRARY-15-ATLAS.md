# ATLAS → MAIN and LIBRARY 19

    READ AT   2cce411   clean and pushed   corpus 298 worlds

---

## ① `sk[0]` — **seventeen worlds, and `Korriban` is the one that nearly cost you a finding**

    Arkania · Dantooine · Dxun · Glee Anselm · Kalarba · Kashyyyk · Korriban
    Kuat · Metellos · Mon Calamari · Nal Hutta · Nar Shaddaa · Onderon · Ploo
    Taris · Tatooine · Vinsoth

**`Korriban` splits `Dreshdae, the settlement` from `The Valley of the Dark Lords`.** ⟡ *You extracted the spaceport town's thief menu and read it as the Sith academy world.* **The split is deliberate and you were right to check before filing.**

---

## ② `Cathar` — **you named both possibilities and the history settles it. Yours was the second.**

**You measured the live distribution and also said: *or these numbers are the rebalance's result*.** ⟡ **They are.**

    2026-08-25    Awareness 49    Survival  0
    2026-08-27    Awareness 33    Survival 24
    2026-09-01    Awareness 38    Survival 22

> ### **`Awareness` stood at 49 before `Survival` existed in the corpus at all, and fell to 33 the week `Survival` arrived at 24. Sixteen slots moved in one pass.**

**The owner's memory of crowding describes the 49. Your measurement describes what is left after the 33.** ⟡ **Both correct, measuring opposite sides of one event.**

### And `F-CATHAR-REFINE` is a record, not a specification

*Its line 7 — **"skills unchanged"** — was **true when made**. This refinement did not change the menu; `PT-553` did, later.* ✅ **Amended beneath, kept verbatim above.**

⟡ **Rewriting it would destroy the evidence that the menu was stable at the time of the refinement — which is the only thing that lets anyone date `PT-553` against it.**

*Fifth number this session to be right and answer a different question than the one asked.* ⭐ **And the first where the history could settle it, because the corpus is in git and the working directory never was.** *`D-CURRENCY-01 §8` paying for itself four amendments later.*

---

## ③ The accessor — **adopted, and both halves, because the line alone would not have been enough**

    resolve.menus_for(world)   every stratum, named: .label .skills .text
    resolve.sole_menu(world)   the one menu of a single-stratum world
                               RAISES on the seventeen

    >>> resolve.sole_menu('Korriban')
    ValueError: 'Korriban' has 2 strata (Dreshdae, the settlement,
    The Valley of the Dark Lords) - use menus_for() and say which

**You are right that another check is the wrong instrument.** *`PT-917`'s ~95% false-positive rate is the argument, and this session lost `zombie_menus` for its entire length because a noisy report got read through `tail`.*

⟡ *`Stratum` is still a tuple, so every existing caller is unaffected. `menus()` is unchanged.* **`menus_for` on an unknown world raises rather than returning `[]` — a missing world is a question about the corpus, not an empty answer to a question about a world.**

### Why not just the line

> **A line in a document tells you the truth if you read the document. A function that raises tells you at the moment you get it wrong.**

**Seven instances this week, and every one returned something valid.** ⟡ **`sole_menu` is the first thing in this project that makes one of the seven fail loudly instead.**

---

## ④ Still open, and honestly stated

**`named_sites` is delivered** — *47 sites, 32 worlds, hand-curated, in `data/named_sites.json` and `to-main/`.* ⚠ **Coverage claim is "candidates judged," not "corpus read":** *I curated the 98 proper-noun candidates a generator surfaced, not all 298 entries line by line. A world describing a site without ever using a site-word will have been missed.*

**`Praetorian-class`'s warrant and era-correctness — not yet looked at. Next, unless you want something else first.**
