# 18 · The two checks — emitted against declared, declared against handled

**`MAIN_WORK` `5510cbf` · `Lodestar` `d08c2f` · `KOTOR-RPG-APP` `3d0be11`.**
180 app tests, 115 Lodestar tests, analyze clean. **All three checks are in,
including the cheap one.**

---

## ⚠ Where the declared list lives — extracted, and here is the argument

**Both checks are about DRIFT between `EVENT-KINDS-01` and code.** A kind
emitted and never declared; a kind declared and silently ignored.

> **⚠ IF THE CODE OWNED THE LIST THERE WOULD BE NO DRIFT TO DETECT.** The check
> would say *"the app emits what Lodestar declares"* — a much weaker sentence
> than *"the app emits what the vocabulary declares"* — and `EVENT-KINDS-01`
> would become decoration. **A check comparing code to code cannot catch a
> document changing.**

**And this project's characteristic failure is exactly that.** `PT-1417` moved
`character.moved` and `area.entered`/`.left` from `session` to `campaign`
**three days ago**, and nothing in either repository could have known. Extracting
puts the vocabulary under `check_extracts.py`, which is how every other rule
already reaches the code.

**So: `design/EVENT-KINDS-01.md` → `data/extracted/event_kinds.json` →
`base-rules/rules/event_kinds.toml`**, read by both repos.

**The cost is the moving parts you named** — an extractor, a kind in
`gen_base_rules.py`, a file on the shelf. **They are the same moving parts
every other rule already has**, which is the second half of the argument: this
is not new machinery, it is the existing machinery applied to one more
document.

**⚠ A row is not a kind.** Six rows name two or three in `a.b / .c` shorthand.
**24 rows carry 36 kinds**, and a reader counting rows is twelve short.

---

## ⚠ A — every kind the code emits is declared, and it failed on the first run

**In the app, because the app is what emits.** Chargen decides when a species
was chosen; Lodestar only folds.

> **⚠ FOURTEEN OF THE FIFTEEN KINDS THIS BUILD EMITS ARE NOT IN
> `EVENT-KINDS-01`.** `PT-1415`'s thirteen creation kinds plus `step-reopened`.
> **Only `character.created` is declared.**

**That is the check working, and it is now a fact the build asserts rather than
a paragraph in a report.** They are named as an exception list — which is `§4`'s
*"should say so"* in a form that can be run:

- **Every entry is owed to the document.** The list is the debt, written down.
- **The day a fifteenth appears** without being added to either the vocabulary
  or that list, **the check fails.**
- **And the other direction is checked**: an exception list that outlives its
  exception is permission nobody is using any more.

**Plus `emitted == handledByReplay`** — which catches the next person adding a
constant and forgetting one of the two halves.

---

## ⚠ B — every declared kind is handled, and the fix is the report

**The worse half.** The kind exists, the event is written, the file
round-trips, `PT-1265`'s guarantee passes — **and the character comes back
missing something.**

**⚠ Replay cannot simply refuse an unknown kind.** A log may legitimately carry
play events this projection has no opinion about — `character.damaged`,
`area.entered`. Refusing would break every save the moment combat is built.

**So the fix is not the test. It is `replayDetailed`**, which returns the record
**and every kind it had no case for**, in the order first met. `replay()` is
that with the report dropped. **One switch**, so what is handled and what is
reported as ignored cannot drift apart.

The test then asserts two things: **no declared creation kind is unhandled**,
and **a play event in a log is named rather than vanishing**.

> **`handledByReplay` is declared as data**, not left implicit in the `switch`,
> so a check can compare it to the vocabulary without reading source.

---

## ⚠ C — every declared kind has a lifetime. It was cheap, and it is in

**36 of 36 have one**, and the set is exactly `PLAY-STATE-01 §2`'s four:
`permanent · campaign · session · transient`.

    campaign   19      permanent   5
    transient   9      session     3

**A kind with no lifetime is a kind nobody has decided persists** — and
`SAVE-LOAD-01 §4` gives lifetimes their job: *"they decide what is written in
the first place."* `PT-1417` was a lifetime set wrong, and it took a player
walking between two areas to find it.

---

## And one thing found in passing

**`check_extracts.py` caught `chassis.json` and `first_level_feats.json` going
stale** against `CHARGEN-DATA-01` while this batch was running — the owner had
edited it. Both re-run; `current 35, stale 0`.

`base-rules` is now **22 kinds / 2,533 records**.

---

## What was NOT built

**No new kinds were added to `EVENT-KINDS-01`.** The fourteen are owed and the
check names them; **writing them into the document is the owner's**, and doing
it here would be resolving a reading into a ruling.

**Nothing scrapes source.** The emitted list is written out by hand in the test,
deliberately: a scraper would pass the day someone emits a kind from a place the
scraper does not look, and the `emitted == handledByReplay` assertion is what
catches a forgotten entry instead.
