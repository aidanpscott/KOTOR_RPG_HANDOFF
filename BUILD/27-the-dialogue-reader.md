# 27 · The dialogue reader, the validator, and a real `.dlg` converted

**232 Lodestar tests · 198 app · 101 Loom.** All three analyze clean.
**38 of the Lodestar tests are new.**

    Lodestar/lib/src/dialogue.dart          the reader and the validator
    Lodestar/test/dialogue_test.dart        27 cases
    Lodestar/test/dialogue_conversion_test.dart   11 cases
    Lodestar/test/fixtures/converted-bastila.toml a real .dlg, structure only
    Lodestar/test/fixtures/trooper-challenge.toml §9's own worked example
    MAIN_WORK/scripts/convert_dlg.py        the converter

---

## 1 · The reader refuses; the validator reports

**Two layers, and the split is principled rather than convenient.**

**The reader refuses a file that is not a conversation** — bad TOML, no
`[conversation]`, no `owner`, a line with no `say`, two lines sharing an id,
**an unknown gate key at any nesting depth**, a link carrying anything but `to`
and `gate`, an effect naming an engine-written kind, and **a link naming an id
that is not in the list it must be in.**

**⚠ The alternation is the reader's job, not the validator's.** `§1` says a
crossed link *"names an id that is not in the list it must be in"* — **so it is
the same failure as naming nothing**, and it is one enum value rather than two.

**⚠ And the closed grammar is enforced where it matters — at depth.** A gate
three levels down carrying `call = "x"` is refused exactly like one at the top.
A surface check would have been the shrug `§4` warns about.

**The validator reports a conversation that loads and is still wrong:** no way
in, unreachable nodes, a dead link, a `skill` not in `SKILLS-01`, an `effect`
kind not in `EVENT-KINDS-01`.

**⚠ And it says what it could NOT check** — same shape as
`record_validate.dart`. Given no skill list and no event-kind list it returns
two `unchecked` lines rather than an empty problem list, **so "clean" can never
mean "nothing was looked at."** Speaker tags are permanently unchecked: `§11`
records that no rule covers a `by` naming a tag that is not in the area.

---

## 2 · ⚠⚠ The validator found a contradiction rather than a bug

**Reported, not resolved.**

`ENGINE-SPEC-03 §2` says of every link: *"walk links in order, run each
`Active`, take the first that passes."* **Built literally, that check flagged
every multi-option node in both shipped games as broken.**

    PICK ONE    start · a player line's `then`     which one fires
    SHOW ALL    an NPC line's `replies`            the options in front of you

**`§4c` is the evidence and it is not a preference.** It designs an option
**list** — `[Persuade]` amber beside `[Lie]` grey beside `[Zabrak]` teal — and
rules **unavailable options are HIDDEN, not greyed.** *Hiding what fails is
only meaningful if everything that passes is shown.* And `STUDY 18` measured
the shape: **27.7% of K1's NPC nodes offer more than one reply, up to seven.**

**The build takes the reading that makes `§4c` possible** and the ordering
check runs only on the pick-one lists. **An owner ruling closes it; this does
not.**

---

## 3 · ⚠ And it corrected the format document, twice, on its own example

- **`§9`'s worked example had no `start`.** It could not begin. **And `§1` had
  never documented `start` at all** — `[conversation]` was shown with `id` and
  `owner` and the entry points were never specified. `§1` now specifies them.
- **Two of `§9`'s option lists tripped the ordering check**, which is what
  surfaced `§2`.

**Both are recorded in `§12` rather than quietly fixed.** A format document
that omits a required field is exactly the failure the validator was built for,
**and the first thing it found was that.**

---

## 4 · A real `.dlg`, converted — and what does not survive

**`convert_dlg.py` reads a real KOTOR companion conversation and writes
`DIALOGUE-FORMAT-01`.** `TRACE-112` governs what may come: **the structure
ports almost exactly, the text ports and must not, the conditions do not port
at all.**

**⚠ It ships nothing.** Every `say` is invented from the node's position and
every condition is dropped. It is a test fixture, and it says so on its first
line — the same standing as the throwaway test package.

**The format held it, node for node:**

    26 NPC nodes · 35 player nodes · 58 links · 11 ways in
    alternation valid throughout
    the speaker override carried — a second character speaks on 3 of 26 lines

**⚠ WHAT DID NOT SURVIVE, counted:**

```
recorded voice line                                        60
silent node — no Text at all                               20
link condition                                             12
IsChild                                                     8
Listener                                                    4
animation list                                              2
node action script                                          2
```

**⚠ And the one that is not a deletion but a consequence: the eleven ways in
became one.** The source opened eleven different ways, each behind its own
condition — **and `STUDY 18` found all eleven of those conditions writing to
global state while deciding.** Drop them, and `start` is a pick-one list of
eleven ungated links. **Ten are dead.** That is the cost of an import in one
number, on a real conversation.

**⚠ Two limits are the format's own, not the conversion's:**

- **There is no silent node.** `§3` makes `say` required, and **20 of 35 player
  nodes in this conversation have no text at all** — they are routing devices.
  **The converter had to invent a line for every one of them.** Corpus-wide
  that is 59.0% of K1's player nodes.
- **Reachability in the graph is not reachability in play.** Not one node is
  orphaned — every node is reachable from *some* start — while the ordering
  check says most of the conversation cannot be got to. **Two different
  questions, and only running both tells you anything.**

---

## 5 · Not built

No editor, no screen, no runtime. Nothing renders a conversation and nothing
plays one. The reader and validator are called by tests and by nothing else.
