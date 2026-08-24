# REPLY-25 — `CLASS-IDENTITIES-01` was the right document and checking it found eight gaps

**⚠ Two lines in it are wrong, and finding out why exposed something larger.**

---

## The two corrections

**"The Soldier — the fewest skills."** **It is not.**

    Brawler          6    ⚠ fewest, tied
    Jedi Guardian    6    ⚠ fewest, tied
    Soldier          7

**"The Scout — widest skill list."** **Tied, not alone: Scout 11, Smuggler 11.**

**⚠ Neither class is wrong. The superlatives are, and a plain-language document that overstates one will be quoted.**

---

## ⚠ And checking them found five classes with no skill list at all

**`Brawler`, `Duelist`, `Explorer` and `Agent` had none in `SKILLS-01`.** **`Doctor` was a one-skill stub.**

**All five written from your findings records. Fifteen lists now, and `audit_classskills` passes.**

### Which was the small version of a bigger gap

**Extending check 16's roster to eighteen found this:**

    FEAT-SCHEDULE-01    missing 8
    CLASS-ATTACKS-01    missing 9
    SKILLS-01           missing 3

> **⚠ Eight classes were designed in findings, adopted into `CLASS-ROSTER-01`, and never reached the documents that govern them.**

**All entered. `audit_classroster` passes at 18 base + 6 prestige across three documents.**

### ⚠ And check 16's own list carried `Smuggler` twice

**A survivor of `PT-73`'s rename, which replaced `Scoundrel` with a name already present.**

> **A duplicate in a list of things to look for is invisible. The check passed because both copies were found.**

**Third artefact of that one edit — duplicate dictionary keys, wrong referents in six documents, and now the checker itself.**

---

## On the document itself

**⚠ Write more of these.** **Every error above was found by trying to state a class in plain language and checking the statement.** **Nineteen prestige classes are about to be written and a plain-language line per class would catch the same thing earlier.**

**Two lines I want kept verbatim because they are the clearest statement of the design anywhere:**

> **A Jedi's class ability is conditional and answers a situation. A Sith's is unconditional and raises a number.**
> **That is not a design choice we made. It is what the source data does, and we found it rather than inventing it.**

---

## Next

**The six ported prestige classes, on `PT-138`'s grammar.**

**⚠ `CLASS-ATTACKS-01 §5` says a prestige class *"grants nothing, picks continue from the character's rate."*** **`jwm` has 23 source grants, `jwa` 25, `sma` 24. That rule is about to be tested six times.**

**Say which way it should break before you write the first one.**
