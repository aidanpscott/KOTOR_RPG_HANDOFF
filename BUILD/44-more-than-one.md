# 44 · `PT-1453` — more than one, and the class underneath it

**617 green** — Lodestar 285 · Lens 4 · Loom 114 · app 214.
`Lodestar 78782b6` · `Loom 2058b16` · `app a42f9b3`.

**Three slices: the third exit with N1 and N2, the viewport hygiene, and the
stale extract.** The class answer is `§1` and it is the point.

---

## 1 · ⚠⚠ THE CLASS — what else folds a list it has only ever seen one of

**The question is better than the fixes and the answer is not the obvious one.**

### ⚠ It is NOT "untested with more than one". Two of them were tested

**`play_state_test` folded two encounters and asserted `working.length == 2`.**
It passed. **The test locked the growth in as correct**, and nobody asked what
six looked like — the owner's save reached **twenty**.

> **"Tested with two, and two looked fine" is worse than never tested, because
> the suite reports confidence it has not earned.**

**And the format readers are fine** — 2+ `[[contents]]`, 2+ `[[connections]]`
and 2+ `[[arrivals]]` all have tests. **Parsing lists was never the problem.**

### ⚠ The real class is narrower and has three shapes

**1 · A CONSUMER WITH NO PRODUCER.** `projectPlayState` has handled
`character.revived` since it was built and **nothing anywhere emitted it.** So
a character who ended a fight at negative vitality projected as down **for
ever**, `standing` dropped them, and the next fight ended after initiative.
**That is N1**, and `PT-559` had already ruled the behaviour — only the writer
was missing. **A consumer with no producer is invisible until a sequence
exists.**

**2 · A PRODUCER WITH NO GUARD.** `_endFight` was re-entrant: pressing a key
after *"it is over"* re-ended a finished fight and appended another set of
outcomes. **One fight produced six.** Invisible until what it produced was
kept.

**3 · A FOLD WHOSE VALUE AND NARRATION DISAGREE.** `current = v` was always
last-wins; `working.add(...)` was not. **They agreed exactly while a log could
hold one.** That is N2.

### ⚠ Where else each shape lives — measured

| | |
|---|---|
| ⚠ **The test bed has ONE of everything** | 1 creature, 1 connection per area, 1 arrival per area, 1 doctrine, 1 item, 1 conversation, and **`a02` has no creature at all.** Every runtime fold over package content has only ever seen one |
| ⚠ **`[requires] packages` — never tested with two** | `§4` makes the ORDER the precedence, *"written as given, never sorted"*, and **no test has ever had two.** The one thing that would exercise it is a second rules package, which does not exist |
| ⚠ **Multiclass — never tested with two classes** | `classes` is ordered and `PT-723` caps it at three. **Chargen writes one.** The list, its order and its `levels` sum are all folded by code no fixture has stretched |
| ⚠ **`_workingLines()` folds `_here`** | Two creatures in one area **has never been rendered.** It joins with `·` and caps at two lines, so a third would truncate exactly as N2 did |
| **`flagsFrom` / `questsFrom`** | ✓ Set and map comprehensions — **last-wins, correct for many.** They have only ever seen zero, but the shape is right |
| **`composers.single`** | ✓ Would throw on two, and **a refusal above it makes two impossible.** Guarded |

### ⚠ And one more of the same family, found in the owner's saves

**The player's log `subject` is their DISPLAY NAME** — `identity['name']`, so
`"Vess Taran"` — while creatures use a tag. **`PT-1445` already ruled that a
log records the id, never the name**, and this is a permanent entry breaking
it. **Reported, not changed**: re-keying it orphans the player's outcomes in
every existing save, which is a migration and a ruling, not a patch.

---

## 2 · The three symptoms

**⚠ THE THIRD EXIT.** `_endFight` persisted and `_enter` persisted; **leaving
the screen with `esc` went through neither.** Three exits write an outcome now,
and **all three share the re-entrancy guard.** Controlled: with the fix
reverted the test fails on exactly that line.

**⚠ N1's test assertion had to be tightened, and that is itself a finding.** A
second fight now often ends **because the player loses** — the trooper's
authored blaster rifle is **1d12 against 11 vitality**, where the invented
vibroblade was 1d6. So the assertion is *an attack was resolved*, not *the
fight did not end*: N1's signature was ending after initiative **with both
alive and no dice rolled.**

---

## 3 · The viewport hygiene — and one file left lying on purpose

**⚠ MY SIZING WAS WRONG BY 4.5×.** I called it *"23 one-line additions"*; it is
**104 test bodies**. A file-level `setUp` covers a whole file, so it came to one
insertion per file after all — **but the estimate was luck rather than
measurement**, and I had already been told once this session that a number I
had not measured was not a number.

**Verified the `setUp` really changes the surface** — a probe printed
`Size(1280.0, 720.0)` inside a test body — **because a hygiene fix that
silently does nothing is the thing this project keeps finding.**

### ⚠⚠ `subrace_test` is deliberately left lying, and that is the finding

Giving it a real surface turns the Zabrak case **red**: the tap on the subrace
row lands at **y≈616** and does not hit it, the flow never advances, and a
later finder throws `No element`. **Zabrak is both a species and its own
subrace**, so `find.text('Zabrak')` matches two rows — and neither `.first` nor
`.last`, with or without `ensureVisible`, reaches the right one.

> **Those tests pass only because their viewport is wrong.**

**Left visibly rather than silently.** Whether that row is genuinely
unreachable at 1280×720 is a **product** question — it is what a player at that
size would meet — and it is the same shape as the clipped-reply click bug.
**Not diagnosed here.**

---

## 4 · `check_extracts` — ⚠ NOT the equipment re-extraction

**The stale one is `event_kinds.json`.** `equipment.json` re-stamped correctly
and reports current.

**⚠ AND IT IS A REAL LAG, NOT A RE-STAMP — but the lag is in the CODE, not in
the extract.** Two copies of the document exist and have diverged:

    HANDOFF/docs/EVENT-KINDS-01.md    175 lines   2fa60f…  ← what the extract records
    MAIN_WORK/design/EVENT-KINDS-01.md 181 lines  0ec0d3…  ← what the checker reads

**Re-running the extractor produces byte-identical rows** — 50, unchanged —
because the six added lines are prose, not table rows. **So the DATA is not
stale.**

**⚠ What changed is a correction that governs a CHECK, and the check has not
been updated.** The added lines are `PT-1435`:

> ***"a permanent kind that NO PROJECTION folds is the bug… the check compares
> against the UNION of what every projection folds, not `replay`'s switch
> alone."***

**`emitted_kinds_test` still compares against `handledByReplay`** — replay
alone. `projectPlayState` is the second projection and check A does not know it
exists.

> **⚠ SO RE-STAMPING IT WOULD SILENCE THE ONLY SIGNAL POINTING AT AN
> UNIMPLEMENTED CORRECTION. The flag is left up deliberately.**

**And it is the same class as everything above:** a check written when `replay`
was the only projection, still assuming one.
