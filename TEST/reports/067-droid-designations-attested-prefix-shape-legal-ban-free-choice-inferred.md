# TEST 067 — droid designations, all four cases: attested prefix, the
# shape-legal ban list catches what the digit-count rule can't, free choice,
# inferred prefix

**Built against:** `run-app.sh` (always rebuilds). KOTOR-RPG-APP `cc4277f`
(*PT-1729 — the name step asks a droid for a designation*), the commit that
ships this feature — `081ef6b` landed on top of it during/after this session
(board-edge/PT-1640, unrelated). `pubspec.lock`'s `lodestar` pin:
`resolved-ref 95bc648`, matching Lodestar's own current HEAD (*PT-1729: what
a player droid may call itself, as a rule over values*) and
`.dart_tool/package_config.json`'s `rootUri` for the compiled checkout — all
three agree.

App PID `53763`, killed by PID at the end of the session, confirmed gone.
Coder's Loom (`12445`, wrapper `12443`) checked running, untouched, before
and after; a `flutter test` run of Coder's own was visible mid-session
(PIDs `61953`/`62143`) and left alone.

No package edited this session — ran a droid through `companion-fixture`'s
own chargen four times (Cancel/Back out and reselect each time), no save
created, `Play` never reached.

---

## 1. Attested prefix — CONFIRMED

`Droid → Astromech → T3-series` (`designations.toml`: `prefix = "T3-"`,
`digits = 2`, `basis = "attested"`). The Name step:

> *"T3-series units are 'T3-' and two digits."*

pre-populated with a valid generated value, `T3-40`, and **Generate**
replaced the whole field with a second valid one, `T3-89`, on one press —
matches `TEST 064`'s finding for the organic Random Name control
(*"replaces the whole field on each press"*), now confirmed for the droid
control reading the same `randomDesignation`.

## 2. Two ways to be refused, and they're genuinely different checks

**Shape-illegal, caught before the ban list is ever read:** typed `T3-M4`
directly. Refused with *`"After "T3-" come two digits, and nothing else."`* —
the digit-count rule (`designationProblem`'s shape branch, `RegExp(r'^[0-9]+$')`
on the tail) rejects `M4` outright, so `T3-M4`'s presence on `reserved.toml`
is never consulted for this input. The Story button stayed dead the whole
time, correctly.

**Shape-legal, caught only by the ban list:** switched chassis/model to
`Droid → Assassin → HK-24` (`prefix = "HK-"`, `digits = 2`, `basis =
"attested"` — `HK-47`/`HK-50` correctly absent from the model list per
`PT-593`). Pre-populated `HK-87` (valid). Typed `HK-47` directly — shape
passes (`47` is two digits) — and got the other message: *`""HK-47" belongs
to somebody — pick another."`* This is `reserved.toml`'s row, read verbatim
in shape, confirming the task's premise exactly: `T3-M4` never needed the
ban list to be caught, `HK-47` on an `HK-24` unit needed nothing else.

## 3. Free-choice chassis — CONFIRMED genuinely free

`Droid → Battle → War Droid Mark I` (`basis = "free"`, no `prefix` row).
Name step text: *"This chassis has no designation convention in the source,
so the whole of it is yours — letters, digits and hyphens, no spaces."* Field
starts **empty** (nothing to pre-populate from) and no Generate button is
shown at all — matches `identity_screen.dart`'s own comment, *"a droid on a
free-choice chassis is the one case with nothing to generate."* Typed
`Gearhead-7` freely; accepted, Story enabled. Note in passing: `Battle` (and
`Assassin`, `HK-24`) also carry a **Voice** step (Masculine/Feminine/Neutral)
absent for the `Astromech` T3-run — `Battle`'s own chassis text says it ships
a vocabulator, which the Voice step's presence tracks correctly.

## 4. Inferred-prefix model, not required but checked — behaves identically,
## plus one extra sentence

`Droid → Astromech → T1-series` (`prefix = "T1-"`, `digits = 2`, `basis =
"inferred"`). Name step: *"T1-series units are 'T1-' and two digits. **The
prefix is inferred from the line rather than copied from a named unit.**"*
Pre-populated `T1-12`, Generate present and produced a second valid value on
press. Mechanically indistinguishable from the attested `T3-`/`HK-` cases —
`designationProblem`/`randomDesignation` read `prefix`/`digits` the same way
regardless of `basis` — the only difference is that one appended sentence,
present verbatim per `identity_screen.dart`'s `rule.basis == 'inferred'`
branch. No `T1-`-prefixed name appears in `reserved.toml`, so the ban-list
half of this model's check went untested by data (nothing to reject).

---

## What I did not check

- The two remaining "inferred" Astromech rows (`3C-series`, `IT-series`) and
  the three inferred Protocol rows (`3DO-series`, `GE3-series`, `GG-series`)
  — `Protocol` isn't a chargen-selectable chassis at all (species step
  offers only `Astromech`/`Assassin`/`Battle`/`Remote`, matching the
  `Droid 4` count on the species list), so those three are unreachable
  through this screen regardless; `3C-`/`IT-series` behave by the same
  mechanism as `T1-series` and weren't separately driven.
- `R-8009` (`prefix = "R-"`, `digits = 4`, the one four-digit attested case)
  and `HKB-3` (`digits = 1`) — the two attested exceptions to the uniform
  two-digit shape. Confirmed only by reading `designations.toml`/
  `designation.dart`'s own `_count` switch, not by driving either model
  through the Name step.
- `Remote` chassis's own Name step — inferred free-choice from `Battle`'s
  identical `basis = "free"` treatment, not separately driven.
- Whether a designation actually **saves** correctly into a character record
  — never reached `Play`/a save this session; confirmed only that the
  Story button's enabled state (the chargen-internal signal that a value
  passed `designationProblem`) tracks correctly through all four cases.
- Case-insensitivity of the ban/shape checks beyond what was incidentally
  exercised (`HK-47` typed uppercase, matching `reserved.toml`'s own
  casing) — did not try `hk-47` or `t3-m4` lowercase.

## State

- No package files touched. `companion-fixture` confirmed unchanged by
  mtime.
- No saves created this session.
- App PID `53763` killed by PID, confirmed gone. Coder's Loom (`12445`/
  `12443`) checked running, untouched, before and after; Coder's own
  `flutter test` run (PIDs `61953`/`62143`, mid-session) left alone.
