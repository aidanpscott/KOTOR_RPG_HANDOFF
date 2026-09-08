# STUDY 18 — judgement

Records in `RECORDS.md`, cited by number.

---

## F18.01 · ⚠⚠ Their condition is not a predicate. Ours is. **That is the wall, and it is not a difficulty — it is a category difference**

`ENGINE-SPEC-03 §2` adopts *"THE BIOWARE MODEL, UNCHANGED"* and `§4b` describes
our gate as **a declared predicate set with a price**. A predicate is a
question. **`Active` is not a question — it is a procedure that returns a
number**, and nothing in the format constrains what else it does on the way.

**Eleven of eleven opening gates in `bastila.dlg` write to global state while
deciding** (`R18.08`). They read a zone number, and on returning true set a
"done" boolean and reset the zone number. **The evaluation IS the bookkeeping.**

**⚠ Two consequences that an importer cannot paper over:**

- **Evaluating twice is not the same as evaluating once.** Our engine may
  re-evaluate a gate freely — to render the option list, to hide an unavailable
  option (`§4c`), to answer *"why is this shut"*. **Theirs may not.** A gate
  that must be evaluated exactly once, at a moment the format does not name, is
  not a gate.
- **`TRACE-95`'s negative gets its explanation.** The format has no concept of a
  second visit **because the second-visit machinery is inside the conditional**,
  hand-built out of globals. `101PER_Atton_Intro_1` through `_4` is that pattern
  in its ugliest form; `k_pdan_bastila01` is the same pattern hidden inside a
  function that claims to be a test.

**This is corpus-wide only in part** — 6.8% of K1's opening gates and 0.4% of
in-tree gates provably mutate (`R18.07`). **The number is a floor**, because
47% of K1's gates cannot be read at all (`F18.02`). **And 6.8% is fatal
regardless of how small it sounds:** an importer cannot skip the gates it
cannot safely port and call the result the same conversation.

---

## F18.02 · ⚠ Half of K1's conditions cannot be read, so the cost of an import is **not merely large — it is unbounded below**

**Both games ship script source**, which the brief did not assume and which is
worth stating plainly: **their conditions are readable, for 52.9% of K1's use
sites and 77.5% of K2's** (`R18.07`). The premise *"script references into a
compiled engine"* is **half right for K1 and mostly wrong for K2.**

**But the other half is the problem.** 5,501 K1 use sites and 2,809 K2 use
sites resolve to a compiled `.ncs` with **no `.nss` shipped**. For those, an
importer has three options and all three are bad:

- **decompile** — a research project, and the output is engine calls, not gates;
- **drop the gate** — the option is then always available, which changes the
  conversation;
- **stub it true or false** — which changes it in a specific, silent direction.

**⚠ And there is no way to tell which of the unreadable ones mutate.** The
measured 6.8% is computed over the readable half only. **The honest statement
is that between 6.8% and 60.5% of K1's opening gates are not predicates, and
the format cannot tell you which.**

---

## F18.03 · ⚠⚠ An import that brings the text and drops the conditions is **a transcript, not an import**, and it should be called that

The brief asked for this to be named. **Naming it:**

| what you get | what it is |
|---|---|
| nodes, links, `Index`, alternation, `Text` | **the transcript** — the words, in order, with the shape |
| `Active` semantics, `Script` actions, globals | **the conversation** — what makes it respond to you |

**A transcript is not worthless.** 482,848 words in K1 and 433,707 in K2
(`R18.01`), already in a tree, already alternating, already with 27.7% of NPC
nodes carrying real choices. **As a corpus to study, or a shape to test an
engine against, that is real.**

**But it is not content you can ship**, for three separate reasons, any one of
which is sufficient:

- **It would not work.** 67.9% of K1's NPC nodes offer exactly one reply and
  59.0% of player nodes have no text (`R18.06`). **Most of the tree is
  plumbing whose only job is to route** — and routing is exactly the part that
  lives in the conditions you dropped. Strip the gates and a large fraction of
  the tree collapses into "always take the first link."
- **It is not ours.** The text is LucasArts/BioWare/Obsidian copyright, and
  `ASSET-REPLACEMENT-01` already governs prototype material that never ships.
  **Dialogue is not in a different position from art.**
- **It contradicts what we are building.** `§4c`'s bracket vocabulary is
  rendered **from the gate field**. Import text with brackets typed into it and
  **you have re-imported the 62% drift the design exists to eliminate**
  (`F18.05`).

> **⚠ So the answer to *"could we import their conversations wholesale"* is:
> the STRUCTURE ports almost exactly, the TEXT ports and must not, and the
> CONDITIONS do not port at all.**

---

## F18.04 · The structure ports **better than expected**, and that is the genuine finding

`ENGINE-SPEC-03 §2` did not merely take inspiration — **it took the model.**
Walking a real `.dlg` against it (`R18.08`) finds the mapping is near-total on
the structural half:

| theirs | ours | |
|---|---|---|
| `StartingList` / `EntryList` / `ReplyList` | same three, named the same | **exact** |
| link = `Index` + `Active` | `§2` states exactly this | **exact** |
| walk in array order, first pass wins | `§2` states exactly this | **exact** |
| `Param1–5` + `Not` | `§2` takes it by name | **exact** |
| `Active2` + `Logic` (AND/OR, one level) | `all_of`/`any_of`, **nestable arbitrarily deep** | **ours is strictly richer** |
| `Text` | authored line | **exact**, minus the bracket convention |
| `Speaker` override, 23–25% of entries | **no counterpart named** | **a real gap in OUR document** |
| `IsChild`, 30–34% of links | **no counterpart named** | **a real gap in OUR document** |
| `Quest` / `QuestEntry`, 1.6% | `QUEST-MODEL-01` exists separately | undetermined |
| `Emotion`, `FacialAnim`, `AnimList`, six camera fields, four fade fields | **no counterpart, by ruling** | `PT-1319` — a character is a portrait, nothing animates |
| `VO_ResRef`, `Sound`, `StuntList`, `CameraModel` | no counterpart | production machinery for a game with 3D scenes |

**⚠ Roughly half of their field set is presentation for a genre we ruled out.**
Of K2's 46–50 node fields, the ones that carry meaning rather than staging are
about eight. `PT-1319` did not know it was deleting half a file format; it was.

**⚠ And two things our own document does not have that a real conversation
needs.** `Speaker` and `IsChild` are used on a quarter and a third of the
corpus respectively. **They are not exotic.** Recorded as gaps in
`ENGINE-SPEC-03`, not as arguments for importing.

---

## F18.05 · ⚠ Is dialogue the item shape? **No — with one exception that is exactly the item shape**

`PT-1409`'s lesson is that the item import *already happened and it was a
conversion*: `ITEMS-01..09` hold converted stats and re-importing would
overwrite seven rulings.

**Dialogue is genuinely untouched ground** (`R18.11`). The TLKs are held raw
and are used for **item and creature names**. No `.dlg` has been read into any
document. Nineteen extracted JSON files, none of them dialogue.

**⚠ The exception is the bracket vocabulary, and it is the item shape exactly.**
`TRACE-12` converted 2,509 bracketed lines / 256 distinct strings / ~25
concepts into **eight checks, one manner tag, and one retirement.** Rulings
sit on top of it:

- `PT-1104` — keep all eight, do not treat KOTOR's distribution as a target;
- `THREATEN → INTIMIDATE` run as a real check, *"KOTOR never did… OURS";*
- `PT-1306`/`PT-1307` — the colours and the removal of numbers;
- `§4c` — rendered from the gate field, so the drift is structurally impossible.

**An import that brought reply text in verbatim would bring the 256 strings
back with it**, and every one of those rulings would be silently overwritten by
literal typed text. **That is `PT-1409`'s failure mode precisely: a conversion
that already happened, re-run from the source, discarding the judgement.**

---

## F18.06 · ⚠ `ENGINE-SPEC-03 §4c` contradicts itself in place. **Reported, not resolved**

`§4c` states `PT-1307`'s ruling —

> **NO NUMBERS ANYWHERE. `[Persuade]`, `[Slicing]`, and you roll.**
> **UNAVAILABLE OPTIONS ARE HIDDEN, NOT GREYED.**

— and then, **further down the same section**, carries the superseded
`PT-1306` block still written as live:

> **⚠ REVERSED: THE DC RENDERS ON THE OPTION, AS `DC 14`, NOT BEHIND A CLICK.**

with a mock-up showing `[Persuade DC 14]` and `[Slicing DC 18]` **greyed**.
**Both of those contradict the ruling printed above them**, on both counts —
the number and the greying.

**The `PT-1306` text is not marked as superseded.** A reader arriving at `§4c`
cold gets two incompatible specifications of the same element and no ordering
between them. **Superseding an owner ruling belongs to the owner; this is
reported and left.**

---

## F18.07 · A correction to the brief's own citation

**The three colours are not `PT-1305`.** `PT-1305` is the character brain being
queued and `RULES-02 §3`'s fact shape. **The colours are settled at `PT-1306`
and simplified at `PT-1307`** (`R18.10`).

**And it is four, not three, once a check has resolved:** amber passed, **coral
failed**, grey manner, teal background — plus `dim` for an act like `[Leave.]`.
`§4c`: *"the colour carries through unchanged; only failure changes it."*

---

## F18.08 · ⚠ The one thing worth taking from the `.dlg` format, and it is not text

**K2's parameterised conditional is the good idea**, and `ENGINE-SPEC-03 §2`
already took it — but the *measurement* is new here and it is the argument.

    K1  2,309 distinct condition scripts for 11,716 use sites
    K2    493 distinct condition scripts for 12,541 use sites

**K2 does more gating with a fifth of the scripts**, because `c_global_eq` with
parameters replaces two thousand bespoke ones. `c_global_eq` alone covers 1,708
sites (`R18.07`).

**⚠ And that is also why K2 is 77.5% readable where K1 is 52.9%.** A small
closed set of generic conditionals is a set you can read once and then
understand every call site of. **A declared gate vocabulary is not just tidier
than 2,309 scripts — it is the difference between a format you can inspect and
one you cannot.**

**We already have the better version of this**, and it is worth saying which
part is better: `§4b.1`'s `all_of`/`any_of` **nests arbitrarily deep**, where
K2's `Logic` field joins exactly two conditions with one operator.
`TRACE-12` found KOTOR's typed convention had *"no way to express that
difference"* — **and neither does its structured field.**

---

## F18.09 · What I could not determine, stated as needs

- **Whether the unreadable 47% mutate.** Needs decompilation, which is a
  separate project and may not be worth it. **Until then every purity figure in
  `R18.07` is a lower bound and should be quoted as one.**
- **Whether our dialogue file format should exist yet.** `PACKAGE-FORMAT-01`
  names a `dialogue/` folder and nothing inside it (`R18.09`). **This study
  answers what it must NOT be constrained by — a `.dlg` importer — but it does
  not author the format, and nothing here should be read as having done so.**
- **`Speaker` and `IsChild`.** Both are heavily used in the source and have no
  counterpart in our documents. **Named as gaps. Not proposed as fields** —
  what a second speaker inside one conversation means for a design where a
  character is a portrait is a design question, not a format one.
