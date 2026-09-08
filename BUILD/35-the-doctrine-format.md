# 35 · The doctrine format, and a check instead of an errand

**270 Lodestar · 206 app · 111 Loom · 4 Lens.** All analyze clean.
**`DOCTRINE-FORMAT-01` is in `docs/`.**

---

## 1 · The format, derived from the code

**`ENGINE-SPEC-04 §6` does not carry the shape.** `PT-1423` built the decision
procedure and **`doctrine.dart` is the only place the four answers are written
down**, so the document describes what already runs.

**The file reads in the order the engine asks:**

    [doctrine]   name · goal · want_range      1st and 4th question
    [break_off]  when · fraction                2nd — a doctrine that is
                                                leaving does not pick who
    [[never]]    the exclusions                 3rd
    [[prefer]]   the preferences, in order

## 2 · ⚠⚠ The distinction survives by construction, not by care

> **`PT-1423`: *"never is not a preference that lost."*** Exclusions apply
> before every preference, so the hull is not chosen **even when it is the only
> thing left** — and `none:all-excluded` is a decision that says which kind.

**Four things make it unloseable, and none of them is a convention:**

- **Two sections.** `[[never]]` and `[[prefer]]` are different lists.
- **`never` is not a value `prefer.rule` accepts.** Writing one there is a load
  failure that says why.
- **The reader puts exclusions first in the rule list whatever order the file
  puts them in.**
- **The dialog has TWO VERBS**, not one *add rule* with a kind beside it —
  because that is the shape that lets an author put an exclusion last.

**⚠ A `match` is DATA, because a file cannot carry a closure.** `Never` and
`Prefer` hold `bool Function(Combatant)`; the vocabulary is **closed** —
`role`, `handle`, `handle_starts`, `below` — and **an unknown key is a load
failure**, exactly as `DIALOGUE-FORMAT-01 §4`'s gate.

**⚠ AND THE WRITER TAKES DATA, NOT A `Doctrine`.** A writer accepting one would
**silently drop every match**, since it cannot read a closure back out.
**The type it cannot write correctly is a type it does not accept** — there is
no `render(Doctrine)` to call.

---

## 3 · `PT-1423`'s layer has an authored caller for the first time

**The bed's trooper carries `doctrines/sith-line`, made by clicking**, and the
play screen loads it. **`plainAggression` is the fallback for a creature that
names none** — still scaffolding when it is used, no longer the only answer.

**⚠ And a creature naming a doctrine that will not load says so loudly.** A
fault in the package is not a reason to fall back quietly.

**The authored one behaves:** the beast is excluded even when it is all there
is (`none:all-excluded`), and the wounded is chosen over the whole one.

---

## 4 · ⚠⚠ The audit is a check now

**`BUILD/33` found five fields by looking once. `BUILD/34` closed four and a
second look found a sixth.** A thing found by looking, and found again after
fixing, **is a check.**

**`test/loom_can_write_test.dart`, and it is `check_extracts.py`'s shape:**
that compares a recorded digest to what is on disk; **this compares what the
readers read — SCRAPED FROM THEIR OWN SOURCE — to what Loom declares it can
write.**

> **⚠ The reader side is scraped and only the writer side is declared.** A
> hand-kept list of reader fields would go stale **the moment a reader gained
> one**, which is exactly the failure being checked for.

**Each excuse carries its reason, and an excuse nobody is using fails the
test** — *"an exception list that outlives its exception is permission nobody
is using any more."*

**⚠ It caught two stale excuses on its first run.** `chassis` and `subrace`
were excused and **no reader here reads them** — they are `CHARACTER-RECORD`
fields, not blueprint ones. **The check found its own stale exception list on
the day it was written.**

**What it excuses now: one.** `reaction` — `PT-1441` rules it **inline with no
file** and nothing in Loom offers the `on`/`then` pair yet. **The next one.**

---

## 5 · ⚠ Three things found on the way

- **⚠ `blueprintKinds` was nine and is ten**, and `PACKAGE-FORMAT-01 §3`'s
  layout comment still reads *"the nine categories"* above **ten folders.**
  Same class as `PT-1252`'s eleven-slots-twelve-positions. **Reported.**
- **⚠ The tenth kind pushed the last one below the fold.** Both panes are
  `ListView`s; **a pane that fitted nine categories does not fit ten.** Not
  missing, not built. **Reported, not restyled.**
- **⚠ `below` is a break-off rule AND a match term** — the *format* uses the
  word twice. A person reads the row label; **anything addressing a control by
  its words cannot.** The chips carry their row in their key.

---

## 6 · Not done

**`reaction`** — inline, and the pair is unbuilt. **`goal` is inert** —
`§6` records it: it is carried into the decision and **nothing reads it.**
**`want_range` has no caller.** **Not the side panel.**
