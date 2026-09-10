# BUILD 102 — a wrong owner, two dead paths, and a port

**1,155 green** — Lodestar 446 · Lens 7 · Loom 217 · app 362 · `+11`.
Lodestar `661405c` · Loom `14997f7` · app `7c3a353`. Pins level, gate SENDABLE.

---

# ⚠⚠ 1 · IT IS ONLY THE NAME — AND THAT IS WHY NOTHING COULD SEE IT

**Traced, then proved.** Nothing in the runtime ever looks a creature up by
`owner`:

    the app opens the conversation the PLACEMENT you walked into names
    `owner` becomes `Beat.speaker`, and `dialogue_panel` prints it uppercased
    grep `speaker` across all three repositories — SEVEN sites, all display

**So a wrong `owner` cannot pull the wrong creature's doctrine, equipment or
vitality. It renames the speaker and nothing else** — and `Tester` had already
built the discriminator for exactly this question: `probe-sentinel` carries
`override = 33`, *"a DISTINCTIVE number, so that if a conversation owner ever
leaked the wrong creature's RECORD into a fight, the vitality would say so."*
**It does not leak.** The fight is with the creature you walked into.

> **⚠ And that is precisely why it is invisible: nothing behaves differently, so
> there is nothing for a runtime check to notice. It can only be caught at
> rest.**

## The two members, because absent and present-but-wrong are not one channel

    conversationOwnerUnknown         a tag no area declares  — TEST 026
    conversationOwnerNotTheSpeaker   a REAL tag, and not the one that reaches
                                     this conversation — Tester's case

**`blueprintMissing`/`blueprintUnreadable` and
`targetAreaUnknown`/`targetAreaUnreadable` are the same split, and both were
made because one channel carrying two meanings makes a fault explain itself
falsely.** A missing tag is a stale reference; a real tag is an author pointing
at the wrong creature, and those are not the same sentence to act on.

**Both fire on real shipped packages:**

    endar-spire   "dialogue/trooper-challenge" is owned by
                  "sith-trooper.command-deck.07", and no area places anything
                  by that tag …  did you mean: sith-trooper.command-deck.39
    tester-probe  "dialogue/sentinel-challenge" is owned by
                  "probe-sentinel.probe-room.04", which does not name this
                  conversation. The creatures that do are
                  probe-warden.probe-room.03, .10, probe-warden.probe-slit.02,
                  .05

**⚠ `TEST 026` suggested this member and it was never built** — and `026`'s
finding was still on disk, unfixed, in the bed every suite loads. **It is
repaired**: `trooper-challenge` names `.39` now, and `play_walk_test`'s
*"validate agrees"* case went red until it did, which is the check earning its
keep on the day it shipped.

## ⚠⚠ AND A CORRECT `owner` IS NOT ALWAYS AVAILABLE — a format question, not a typo

**`conversation` is on the BLUEPRINT and `owner` is a PLACEMENT tag.** A
template placed three times has three tags and one owner, so **it can be right
for at most one of them, by construction.** `tester-probe` places `probe-warden`
four times against one `sentinel-challenge`.

**So the check does NOT fire when the owner is one of them.** A check a package
cannot be made to pass is a check that gets turned off — `PT-1600`, one slice
ago. **The format question is named and is not enforced.**

## ⚠ AND THE ROOT IS THAT `owner` IS TYPED

`conversation_tab` offers a **blank text box** labelled `owner`. `PlaceWayDialog`
three panes over offers the areas and the arrivals each one declares, on the
argument that *a value the reader will refuse should not be typeable* — and here
the value the reader accepts is one the VALIDATOR refuses. **A stale tag is the
expected outcome of a blank box, not an accident**, and `PT-1377`'s monotonic
`tag_seq` guarantees the tag changes every time the creature is re-placed.

**Not built this slice** — it is the same port as item 3 and it belongs beside
whatever you rule about the multi-placement question.

---

# ⚠⚠ 2 · A COUNTER DESTROYED BY THE ACT THAT INCREMENTS IT

`Tester` is right and it is worse than two dead branches:

    speak   reachable ONLY when `_fight == null` (`_step` guards it), which is
            exactly when the toll returns free
    a door  spends it, and then `_enter` ABANDONS THE FIGHT THAT HOLDS THE
            COUNTER

**`§5` lists six interactions and the product has an affordance for two** — one
ends the fight when taken, and the other cannot be taken during one. **A pip was
not added either**, and deliberately: `interactionSpent` is the one budget the
strip does not draw, but a pip you can only spend by leaving the room is
`PT-1554` freshly made — *a bright pip is a promise*. **No control was invented
to give the rule something to bite: a stow-your-weapon key nobody would press is
not a caller.**

## ⚠⚠ AND I JUSTIFIED THE SPEAK PATH WITH A CLAIM THE CODE CONTRADICTS

My own comment read *"the app has been starting conversations mid-fight for
nothing since `PT-1437`."* **It has not and it could not.** `_step` guards
`_startTalk` with `_fight == null`, twenty lines above. **Asserted rather than
checked, about the same function**, and `Tester` found by playing what I could
have found by reading.

## ⚠⚠ AND UNDERNEATH THE DEADNESS THERE WAS A LIVE BUG

**A refused door spent your free interaction and moved you nowhere.** `_enter`
reads the destination and leaves you where you are when it cannot be reached —
and `PT-1596` took the toll *before* it looked.

> **`_enter`'s own comment names that defect one clause over**, written about the
> outcome write: *"a refused door would have cost a round and moved nobody."* **I
> added a second toll above the check it had been moved for.** A rule applied to
> one path and not the next, inside the function whose comment names it.

**The toll goes with the travel now** — taken once the destination has opened and
before the fight is given up. Both halves matter: earlier and a refusal charges
for nothing, later and there is no turn left to charge.

**⚠ And its sentence was destroyed by the arrival line inside the same
synchronous call — `PT-1464` a third time.** Appended rather than assigned.

## ⚠ AND THE INSTRUMENT WAS PROVED, TWICE, BECAUSE THE FIRST ONE WAS DEAD

One refused door proves nothing — **the first interaction is silent by design**.
The case uses **two** doors in one turn, and the observable is the ACTION PIP
rather than the line, because under the old order the second refusal *did* cost
the Action and **the sentence saying so was destroyed by `_enter`'s own refusal
message.** With the fix reverted the case goes red on `action 1 of 1`; with it,
green. `free_interaction_test` is new — **`PT-1596` shipped with no case at all,
which is most of why it shipped dead.**

---

# ⚠⚠ 3 · THE ITEM DIALOG, AND THE FIX WAS THREE PANES AWAY

    a closed list                    both had one — the base types
    a dependent field that explains
      its own emptiness              "pick an area first" against a blank gap
    a refusal you can see from
      where you click                `enabled:` against a sentence below the
                                     fold of a scrolling body

**`DialogFrame` gains a pinned `note` slot** — above the verbs, outside the
scroll. **One fix, every dialog**, which is the argument the frame's own
`maxHeight` comment already makes.

- **`Create` is grey until it can write**, recomputed on every keystroke.
- **The reason is on screen from the first frame.** `TEST 022`: *"the path
  prefill is itself invalid, so the dialog opens in a state that will refuse,
  and says so somewhere you cannot see."* It still opens in that state — the
  prefill is a useful stem — **but the reason is there before you touch
  anything**, rather than being earned by a click that appears to do nothing.
- **An empty base-type roster says whose fault it is not.** It drew a heading
  over nothing and then refused for a choice it had never offered.

**⚠ AND A FOURTH THING WAS ALREADY BUILT TOO.** This file's `_field` constructed
a `FocusNode()` **inside `build`** — the exact defect `FieldBox`'s own comment
names — and got away with it only because nothing rebuilt on a keystroke.
**Validating as you type is what would have made it bite**, so the port had to
bring the field with it. A test asserts the refusal is **not** a descendant of
the `SingleChildScrollView`, because the finding was the POSITION and a case
that only checked the sentence exists would have passed on the reported version.

---

# ⚠⚠ AND THE SWEEP OF MY OWN REPORTS

**Grepped 101 build reports for conclusions stated and not applied.** Four found,
two of them real:

    BUILD 92   "does the fenced-example check belong in the gate? YES … and it
               should go in NOW"          → eight slices unapplied; closed at
                                            BUILD 101
    BUILD 96   "they can cite PT-1588 now, and I will change them the next time
               either file is open"       → the condition never triggered.
                                            APPLIED THIS SLICE — area_open.dart
                                            and AREA-FORMAT-01 §3c
    BUILD 33   "[requires] belongs in package properties, and properties does
               not offer it"              → closed at the time, verified
    BUILD 68   "say the word and I will build it"
                                          → awaiting a ruling, not a broken
                                            promise

**⚠ AND THE SHAPE THE SWEEP FOUND IS THE CONDITIONAL DEFERRAL.** *"Next time
that file is open"* and *"one line, next time the palette is open"* are promises
whose trigger nobody watches — **they are not scheduled, they are hoped for.**
`BUILD 93`'s *"the palette's two gestures — one line, next time the palette is
open"* is still open on the same terms, and `BUILD 43`'s viewport-hygiene sweep
was deferred to "its own small slice" that has not come.

> **A deferral with a condition no check evaluates is a `TODO` with better
> prose.**

---

# STILL OPEN

`owner` is typed into a blank box where every comparable field is a pick-list ·
one conversation, one owner, N placements — a format question · `§5` has no
second interaction the product can reach · the palette's two gestures ·
`BUILD 43`'s viewport sweep · and everything carried from `BUILD 100`.
