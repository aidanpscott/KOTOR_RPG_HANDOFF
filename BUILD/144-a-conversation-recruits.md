# BUILD 144 — a conversation recruits, and my own wiring failed the test I wrote to catch it

---

## 1 · ⚠⚠ `PT-1745` — RECRUITMENT IS A CONVERSATION EFFECT, AS RULED

> *"Dialogue lines already support `effect = [{kind = …}]` with existing kinds
> (`quest.flag-set`, `item.lost`) — add a `party.joined` kind that plugs into
> that same machinery. Matches how the source games actually do it (every
> companion joins via a conversation moment), and needs no new UI."*

**The writing half needed nothing.** `dialogue_run` already builds

    CharacterEvent(e['kind'] as String, step: 'play', payload: {...e}..remove('kind'))

at both the `begin` and `choose` sites — **every key an author writes is
carried through already** — and `party.joined` has been a declared `campaign`
kind in `EVENT-KINDS-01` and the shelf's `event_kinds.toml` all along. An
author could have authored this before anything could act on it.

**What was missing was the board noticing without leaving the room.**
`combatantsIn` reads a placement's `role`, and it runs **on entry** — so a
creature recruited mid-conversation stayed an enemy until you walked out and
back. Added:

* `combatantsIn(sides:)` — a map the **log** supplies, and the log's role wins
  over the placement's.
* `_sidesFromLog()` — folds `partyIn` into that map.
* `_sidesChanged(fresh)` — rebuilds **only** the creatures whose side actually
  moved, through the same reader, clears them from `_hostile`, and says
  *"… is with you now"*.

Two cases, both on a board where the author placed the creature with **no
`role` at all** — an enemy, asserted as the control before anything is said.

## 2 · ⚠⚠ AND THE SECOND CASE FOUND THE DEFECT THE FIRST COULD NOT — IN MY OWN WIRING

I wrote the first case for the opening line and it passed. Then I read my own
comment — *"two paths carry effects and wiring one is the shape this corpus has
a name for"* — and wrote the second case for a **reply**.

It failed. Not on the conversation, not on the effect: the log **had**
`party.joined` and the board said **nothing**.

**`_pick` called `_sidesChanged` BEFORE the `setState` that appends to
`_log`.** `_sidesChanged` folds `_log`; at the moment it ran, the join was not
in it, so the map was stale, nothing had moved, and it returned having changed
nobody. **The opening line worked only because that site happened to append
first.**

And the count was worse than two. **Four** sites in the dialogue path carry an
author's effects — an opening line, a reply, an interrupt (`PT-1664`), and a
beat advancing — and I had wired **two**. That is *a rule applied to one path
and not the next*, committed by the person who keeps naming it.

The repair is not four copies. One `_landed(events)`:

    void _landed(List<CharacterEvent> events) {
      _log.addAll(events);
      _persist(events);
      unawaited(_sidesChanged(events));   // ⚠ AFTER THE APPEND, ALWAYS
    }

All four sites call it. **The order is not a detail, so it is not left to each
caller.**

> ⚠ The case is mutation-checked in the other direction too: severing the begin
> hook kills the first case. `PT-1661` — a guard is not a guard until it has
> been seen to fail.

## 3 · ⚠ TWO OF THE THREE THINGS THAT COST ME TIME WERE FIXTURE FAULTS, AND ONE WAS ON SCREEN

**The conversation would not open.** The screen said, and had been saying:

    this conversation will not load — There is no conversation here.

I had written the fixture to `blueprints/conversations/join.toml`.
`package_validate` is explicit about this and has been since `PT-1441`: a
`doctrine` is a path **under `blueprints/`**, a `conversation` is a path **from
the package root**, *"checking them with one root would have reported every
conversation missing."* The refusal was correct and I had not read it.

> **That is the third time this month the answer was in the status bar.**

**An `npc` node offers `replies`, not `reply`.** My typo produced a
conversation with one line and no options. I went looking for the missing
refusal — and [dialogue.dart:511](Lodestar/lib/src/dialogue.dart#L511) already
says it: only `§4`'s **gate** keys are a closed grammar; *"an unknown key in
the head is ignored"*, deliberately and in writing. **Not a gap. I checked
before filing it as one.**

**And `PlayScreen.campaignKinds` DEFAULTS TO `const {}`.** A bed that omits it
gets `onAppend` called for nothing at all, which reads exactly like *the effect
never fired*. The shipped app fills it from the shelf; `roster_panel_test` and
`looting_test` already carry the line. Mine now does too, with the reason
written down.

## 4 · ⚠ THE `whole_loop` FLAKE, REPORTED AS UNRESOLVED AND NOT AS DIAGNOSED

One full app run failed two `whole_loop_test` cases — *"Load Game LISTS THEM"*
and *"THE WHOLE LOOP — and it survives a restart"*. The file passes **in
isolation** and passed **two subsequent full runs**. **I did not capture the
failure message**, so I have a sighting and not a cause.

What it does narrow: **that file is already on `copiedShelf`.** So `copiedShelf`
is not sufficient for it, and the `BUILD 142` fix does not cover this. A
hypothesis I have **not** confirmed: `copiedShelf` still `listSync`s and copies
**the live shelf** at copy time, so it removes the lazy-tile and extra-package
exposure but **not** a partial file being written underneath it.

**Filed as open. Evidence-fits is not confirmed.**

---

## What ran

    Lodestar   644 tests   exit 0
    Loom       261 tests   exit 0
    app        (full)      exit 0 on two of three runs — see §4
    companion_test          10 tests, exit 0
    flutter analyze lib/    clean, Lodestar and app
    flutter build linux     built

Exit codes read from `$?` directly, never through a pipe.

## Heads

    Lodestar        ea486f7   (unchanged)
    Loom            948f536   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   d875bfb
