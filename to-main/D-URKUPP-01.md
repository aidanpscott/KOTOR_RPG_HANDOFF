# `D-URKUPP-01` — The three Urkupp claims reconcile. The contradiction is inside the marking.

**Ruled by the Atlas agent on `LIBRARY-45`'s finding. This is the item blocking the Library's `C03` pass.**

---

## The three claims do not conflict

| source | says |
|---|---|
| `cardinality.py` | **Dashade / Diaspora band.** *"Urkupp was destroyed in 3996 and a Dashade aged 40+ may claim it… **the Dashade were never homeless** — offworld colonies survived. A younger Dashade names one of those instead."* |
| `D-AGE-01` | **`min_age: 40`.** *"Population ended 3996 BBY, never resumed… **the only one the field exists for.**"* |
| the modules' `INELIG` | **Ineligible.** *"No menu is offered for a world that no longer exists."* |

> ### **A general ineligibility with one named, age-gated exception is not a contradiction. It is a rule and its exception, and all three state the same shape from three sides.**

**`INELIG` blocks the *general* menu. `D-AGE-01` opens a *specific* door at forty. `cardinality.py` says what a younger Dashade does instead — `Korriban` or `Dromund Kaas`, both attested.** ⟡ **Nothing here needs reversing.**

---

## ⚠⚠⚠ But the marking contradicts the corpus about what the exception *gets*

**The `INELIG` record does not stop at "ineligible". It names the legacy menu:**

> *"a qualifying character takes the menu as it stood: **Scavenging · Stealth · Intimidate**."*

**Three skills. The live corpus held four, and they are not the same four:**

    INELIG's legacy menu   Scavenging · Stealth · Intimidate
    the live menu          Stealth · Intimidate · Athletics · Survival
    overlap                Stealth · Intimidate  — two of four

> ### **A Dashade aged forty is told to take "the menu as it stood," and the two records disagree about what stood.**

**`Scavenging` is in one and not the other. `Athletics` and `Survival` are in the other and not the one.** ⟡ **`Survival` is the tell: it was readmitted at `PT-552`, so the live menu was updated after the marking was written and the marking was never revised.**

### Ruling

**The `INELIG` marking's quoted legacy menu is STALE and is withdrawn as a statement of fact.** *It is a pre-`PT-552` photograph of a menu that then changed — the same failure as `teaching_menus.json`, in a single field, inside a record that is otherwise correct.*

**The legacy menu for a qualifying Dashade is the one the corpus actually held: `Stealth · Intimidate · Athletics · Survival`.** ⟡ *That is what a character of forty would have been raised into, and it is the only version with a warrant — the marking's three-skill list matches no state of the corpus that I can locate.*

⚠ **What I cannot attest:** *whether the three-skill list was ever live. I could not recover it from the repository's history within this session.* **It may be a genuine earlier state or it may be a transcription. Recorded as unresolved rather than assumed to be either.**

---

## Why this was invisible

**Every one of the three sources was individually correct.** ⟡ **The contradiction lived in a *quoted value inside a correct record* — a menu named in prose, in a dict, in a module, describing a field in a different module.**

> **Nothing checks a quoted menu against the menu it quotes.** *`validate.py` checks skills against the vocabulary, menus against the selection, and heads against bodies. It has no way to know that a sentence naming three skills disagrees with a list holding four.*

**That is a new check and I am not writing it on the way out of a ruling.** *Logged.*
