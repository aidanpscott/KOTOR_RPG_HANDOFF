# TEST 136 — the Loom trigger/effect system, both layers

**Build.**

```
Loom            local HEAD    cb6e722, working tree clean, built via
                              `git archive cb6e722` into an isolated scratch
                              copy ($S/loom-head)
KOTOR-RPG-APP   local HEAD    460063b, working tree clean, built via
                              `git archive 460063b` into an isolated scratch
                              copy ($S/app-head)
pubspec.lock    resolves      lodestar  0f267bd5e1bc7cc75bfec474aedc7e15942933f6
package_config  agrees        ~/.pub-cache/git/Lodestar-0f267bd5.../
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints. Both live repos (`KOTOR-RPG-APP`, `Loom`) confirmed clean via
`git status --short` throughout — nothing in this pass ever touched them; all
work happened in the two `$S/*-head` scratch archives and one new package on
the real shelf (`tester-effects`, kept — see Fixtures).

**Two corrections to the routing before anything else.** `EVENT-KINDS-01`
(via Loom's own `askableEffectsList`, `wizard.dart:159-193`) declares
**15** kinds, not 10, across **7** categories (Combat, Story, World, Access,
Items, Presentation, Security). There is no `door.locked` kind — only
`door.unlocked` exists; the other nine unnamed kinds are `quest.flag-set`,
`quest.concluded`, `store.opened`, `camera.shown`, `encounter.began`, plus
the six the routing did name. Neither correction changes what got confirmed
below.

**Verdict — two real defects confirmed, both empirically; two of the
routing's "real consumer" claims were wrong before I ever opened the app.**

---

## 1. Loom's own picker — confirmed, all three claims

```
$ flutter test test/tester_own_effect_picker_fields_test.dart
⚠⚠⚠ EACH KIND'S FIELD FORM MATCHES fieldsForEffect, KIND BY KIND
⚠⚠⚠ item.acquired/item.lost NEVER ASK FOR subject, DOOR/CONTAINER DO
⚠⚠⚠ THE ZERO-FIELD NOTE APPEARS FOR EVERY PARAMETERLESS KIND
All tests passed!   (3 tests)
```

- Every one of the 15 kinds renders exactly the field labels
  `fieldsForEffect(kind)` says it should — no more, no fewer — read directly
  off the real widget after selecting each kind in turn, not just off the
  static description/category text Coder's own test already covered.
- `item.acquired`/`item.lost` never show a `subject` box. The control
  matters here: `door.unlocked`/`container.opened` need the *same* field and
  are *not* auto-filled, and both correctly do show it — so the absence for
  item.* is the wizard's `effectAutoFields` doing its job, not a form that
  never asks for anything.
- The zero-field note ("the kind alone is the whole effect — nothing to fill
  in.") appears for every parameterless kind, `encounter.began` through the
  four Security kinds.

Security category, and all four tier-two kinds inside it
(`droid.reprogrammed`, `turret.disabled`, `forcefield.toggled`,
`alarm.raised`), confirmed present and correctly organized as part of the
same run.

## 2. door.unlocked — ⚠⚠⚠ CONFIRMED DEFECT: writes to the log, does nothing live

Authored through the real wizard shape, on a real door, played through the
real screen:

```
$ flutter test test/tester_own_trigger_effects_play_test.dart
⚠⚠⚠ DOOR.UNLOCKED — REAL, OBSERVABLE EFFECT [E]
⚠ FINDING: ⚠⚠⚠ door.unlocked landed (in the log) but the target STILL
  offers "Open Lock" live — the menu did not update
⚠ FINDING: door.unlocked: the player did NOT pass through live — walking
  is still blocked, consistent with `_unlocked` never updating
```

Root cause, read from `play_screen.dart` directly and confirmed by
exhaustive grep: `_unlocked` (`late final Set<String> _unlocked = {
...unlockedIn(_log)}`, line 5301) is a **live, mutable Set** that both the
"Open Lock" context-menu check (`_shutTo`, line 5269) and the walk-gate read
directly. The *only* two call sites anywhere in the file that ever add to
it are inside `_wroteUnlocked` (line 5306), reached exclusively from the
direct "Open Lock" skill-check interaction (lines 4671, 4864). The dialogue
effect path — `_pick` → `_landed` (lines 6173-6216, 5983-5988) — appends the
event to `_log` and persists it (so it genuinely reaches the save), but
`_landed` has no analogous call for `door.unlocked`/`container.opened`,
unlike `store.opened`, which *does* get a special-case reaction right next
to it in `_pick` (lines 6183-6192). The mechanism that would wire a dialogue
effect into `_unlocked` was built for one kind and never extended to these
two.

Practical consequence: a door or container unlocked through a dialogue
reply stays functionally locked — same menu, same walk-block — for the rest
of that play session. The event is real and would seed `_unlocked` correctly
on the *next* load (that half is read from the doc comment at line 5289-5300
and the `_persist` call, not independently re-verified through an actual
save/reload in this pass — stated as a source-backed claim, not an
empirical one).

## 3. container.opened — ⚠⚠⚠ CONFIRMED, same defect, same code path

```
⚠⚠⚠ CONTAINER.OPENED — REAL, OBSERVABLE EFFECT [E]
⚠ FINDING: ⚠⚠⚠ container.opened landed (in the log) but the target STILL
  offers "Open Lock" live — the menu did not update
⚠ FINDING: container.opened: the player did NOT pass through live —
  walking is still blocked, consistent with `_unlocked` never updating
```

Identical result, on a footlocker, from its own fresh conversation (not a
re-bump of the door's — see the footnote in Fixtures on why each lock gets
its own board). `container.opened` shares the exact same `_unlocked` Set and
the exact same missing wiring, so this isn't a second, independent defect —
it's the same one, confirmed twice rather than assumed by symmetry.

## 4. item.acquired/item.lost — ⚠⚠⚠ CONFIRMED SEVERE DEFECT: the wizard's own "you" never lands

This was the finding I went in suspecting from static reading alone, and
built a matched control specifically to settle empirically rather than
report from source-reading:

```
⚠⚠⚠ item.acquired/item.lost — THE WIZARD'S OWN "you" AGAINST A REAL NAME
All tests passed!
```

Two identical `item.acquired` effects, same item, same reply shape — the
only difference is the `subject` value:

```
subject: "you"           (exactly what Loom's own effectAutoFields writes)
subject: "Vess Taran"    (the real character's own identity name)
```

The control landed: after the named-subject reply, the vibroblade is in the
inventory. The wizard's own shape did not: after the "you"-subject reply,
it never arrives. Root cause, confirmed via grep of `dialogue_run.dart` and
`remains.dart` (zero hits for the literal string `'you'` anywhere in
Lodestar): `carriedBy`/`creditsAfter` fold by `subject == handle`, and
`_playerCombatant()` in `play_screen.dart` sets `handle` to the character's
own `identity['name']`, never the literal string `'you'`. Nothing anywhere
substitutes one for the other. Since Loom's wizard is the *only* way an
author reaches this kind, and it hard-codes `subject: 'you'`
(`effectAutoFields`, `wizard.dart`), **item.acquired/item.lost authored
through the real tool is a silent no-op against any real player, always.**

A comment in KOTOR-RPG-APP's own `test/door_lock_test.dart` already carries
this exact lesson on a test fixture (`'subject': 'Vess Taran'`, with a note
that `'you'` was only ever right when the bed had no character at all) —
this defect was one hop from being caught before, on the same subject-value
question, in a different file.

## 5. map.revealed / log.written — routing's premise was wrong, not a defect

The routing asked me to confirm these "actually clear fog of war" and are
"readable in-game." Both are inert, and were already known to be inert
*before* I opened either app — Lodestar's own `ledger.dart` says so in its
own doc comments ("no fold yet" for `map.revealed`, "no fold or reading
surface yet" for `log.written`), and grepping all of KOTOR-RPG-APP's `lib/`
turns up zero consumers for either kind outside the wizard's own
declaration. Played through anyway, for a real scoped negative rather than
trusting the source alone:

```
⚠⚠⚠ map.revealed AND log.written — AUTHORABLE AND INERT, SCOPED
All tests passed!
```

Both replies land without crashing and the conversation continues normally
— same expectation the routing itself set for the four tier-two Security
kinds, just true here for two kinds the routing called tier-one with real
consumers. Scoped: what I can say is nothing on the play screen changes and
nothing in `lib/` reads either kind back; I can't rule out a consumer that
doesn't exist in this codebase at all.

## 6. The GUI input blocker — still broken, now on a third binary

Not retried this session — already reproduced twice on two different apps
(KOTOR-RPG-APP, Loom) across TEST 134/135 with the required xterm control,
and stable/non-transient is the standing read at this point. All
confirmation above is headless, through the real widget tree and real
parser, not through a live launch.

---

## Fixtures

New package on the real shelf, kept (not scratch, since it's a package like
any other and both apps' tests need to open it by path):

```
~/.local/share/kotor-rpg/packages/tester-effects/
  package.toml
  areas/a01-hall.area, a02-through.area
  blueprints/characters/rigger.toml
  blueprints/items/weapons/vibroblade.item
  dialogue/rigger.toml   — nine replies, one per tier-one effect kind
                           (plus the item.acquired "you" vs "Vess Taran"
                           control pair)
```

Validated clean through the real parser (`openConversation`, `openArea`)
before any widget test touched it — zero problems, all payloads read back
correctly.

Two new test files, scratch only, deleted after this pass:

- `test/tester_own_effect_picker_fields_test.dart` (Loom) — 3 tests, §1.
- `test/tester_own_trigger_effects_play_test.dart` (KOTOR-RPG-APP) — 4
  tests, §2-5. ⚠ Each lock gets its own fresh board rather than re-bumping
  the same NPC twice in one conversation — a second `bump()` after
  `[Leave]` timed out `pumpUntil`'s own 60s backstop waiting for the
  greeting text to reappear, almost certainly because the conversation
  doesn't reopen on the same node on a repeat visit. That's a fixture
  confound, not a finding, and splitting the board sidesteps it rather than
  explaining it.

No stray processes left running — checked via `ps aux` for `flutter`/`dart`
at the end of this pass, none found.
