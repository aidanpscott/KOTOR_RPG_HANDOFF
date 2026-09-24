# TEST 137 — the two TEST-136 fixes, Track A, B1, Jedi Support, and PT-2598

**Build.**

```
local HEAD              8a1e274  "Jedi Support: resolution + app wiring,
                                  and a dead revive rule fixed —
                                  PT-1141/PT-2604"
working tree             clean at that sha (git-archived into an isolated
                         scratch copy, $S/app-head2)
pubspec.lock resolves    lodestar  a048c495be7ed132033f2ef5980d43369a1a2d48
pub-cache checkout       ~/.pub-cache/git/Lodestar-a048c495.../  — present,
                         confirmed against the lock before anything ran
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints. Both live repos (`KOTOR-RPG-APP`, `Loom`) confirmed clean via
`git status --short` throughout and at the end of this pass; every test
below ran from `$S/app-head2`, never the live tree.

**Verdict — four of five items confirmed clean, and one severe, new,
previously-unconfirmed defect found.** Items 1, 2 and 3 (the two TEST-136
fixes, Track A, B1) are correct — for item 3 I found and closed a real gap
in Coder's own coverage (HANDS OFF was never independently exercised as its
own end state) rather than a defect. Item 4 (Jedi Support) is NOT correct:
a doctrine-cast Heal uses the player's own stats instead of the actual
caster's, confirmed empirically, not just from source. Item 5 (PT-2598)
confirmed clean.

---

## 1. The two TEST-136 fixes — both now live, not just logged

Rewrote my own TEST-136 fixture test (`tester-effects`, still on the real
shelf) to read the real written event's own `subject` field via `onAppend`
capture rather than screen text — Coder's own fix commit (`45c2505`) flagged
that inventory-row text was an unreliable thing to grep for ("the same word
showed up regardless of whether the bag actually held one"), which was a
real weakness in my own TEST-136 methodology worth correcting here rather
than repeating.

```
⚠⚠⚠ DOOR.UNLOCKED — NOW LIVE, NOT JUST LOGGED (R2)
⚠⚠⚠ CONTAINER.OPENED — NOW LIVE, NOT JUST LOGGED (R2)
⚠⚠⚠ item.acquired/item.lost — THE WIZARD'S OWN "you" NOW RESOLVES (R2)
⚠⚠⚠ map.revealed AND log.written — AUTHORABLE AND INERT, SCOPED
All tests passed!   (4 tests)
```

- **door.unlocked**: the written event carries `door.effects.02`, the
  "Open Lock" menu is gone afterward, and the player actually walks through
  — all three, in the same session, no reload.
- **container.opened**: the written event carries `footlocker.effects.03`
  and the menu updates. ⚠ Dropped the walk-through check for this one — a
  footlocker isn't a path a player walks *through*, and my first attempt at
  this check failed with both readings empty because the isolated
  container-only board's door (two tiles further, never unlocked in that
  board) blocked the walk, not the footlocker. A test-design mistake on my
  part, not a finding.
- **item.acquired**: the wizard's literal `subject: "you"` now resolves to
  the real character's own handle — the control (`subject: "Vess Taran"`)
  and the wizard's own shape both land the vibroblade in
  `carriedBy([...wrote], subject: 'Vess Taran')` now.

Matches `_resolveYou`'s fix in `45c2505` exactly (rewrites `'you'` at
`_landed`, the one choke point every dialogue effect passes through) and
`_landed`'s new `_unlocked.add` loop for `doorUnlocked`/`containerOpened`.

## 2. Track A — confirmed via Coder's own suite, all 7 sub-claims

`open_portrait_switches_control_test.dart`'s seven tests all pass in this
build, each using real `@visibleForTesting` hooks built for exactly this
purpose (`activeForTest`, `activeTagForTest`, `atForTest`,
`placementSquareForTest`) rather than screen-text proxies:

```
⚠⚠⚠ THE PLAYER IS ACTIVE BY DEFAULT, AND A NON-ACTIVE PORTRAIT SWITCHES...
⚠⚠⚠ ARROW KEYS MOVE WHOEVER IS ACTIVE, AND THE PLAYER FOLLOWS...
⚠⚠⚠ SWITCHING IS EXPLORATION ONLY — A PORTRAIT MID-FIGHT KEEPS TODAY'S...
⚠⚠⚠ A FIGHT STARTED BY THE ACTIVE COMPANION OVERRIDES CONTROL BACK...
⚠⚠⚠ A DIALOGUE EFFECT'S `you` RESOLVES TO THE ACTIVE CHARACTER, NOT...
⚠⚠⚠ DISMISSING THE ACTIVE COMPANION RETURNS CONTROL TO THE PLAYER...
⚠⚠⚠ LEAVING THE AREA RETURNS CONTROL TO THE PLAYER...
```

I did not duplicate a fresh fixture for every one of these — the coverage
here is unusually thorough already (mutation-tested per the commit message,
each claim pinned to its own dedicated test hook rather than inferred from
UI text), and I used my own remaining time on the two areas that actually
had gaps (§1's methodology fix, and §3/§4 below). I did independently use
Track A myself as *infrastructure* for the Jedi Support check in §4 — a
different companion, a different bed, switching control to make it the one
that initiates contact — which exercises the portrait-switch and
active-movement mechanism for real, under conditions Coder's own fixture
never tried.

## 3. B1 — control modes confirmed, and a real gap in Coder's own coverage closed

Coder's own `companion_control_mode_test.dart` proves the default, the
cycle button's three-step rotation, MANUAL holding honestly, and AUTO
fighting — all pass. But every place `HANDS OFF` appears anywhere in the
whole suite either passes through it on the way to AUTO or uses it as
`jediSupport`'s own mode without ever independently asserting a plain
HANDS OFF companion actually swings on its own, as its own end state. The
commit's own claim — *"hands-off and auto both run exactly what every
companion already ran... no behaviour changes for either mode"* — was
therefore real but not independently exercised for HANDS OFF specifically.
Closed it:

```
⚠⚠⚠ HANDS OFF, ON ITS OWN — NOT MANUAL, NOT PROVEN ONLY VIA AUTO — ALSO
FIGHTS
All tests passed!
```

One tap from MANUAL (stopping at HANDS OFF, never advancing to AUTO), a
companion set that way struck a real target within 12 rounds under the
seeded dice, and never showed the manual-hold message. Confirms the claim
rather than assuming it by symmetry with AUTO.

## 4. ⚠⚠⚠ Jedi Support — SEVERE, NEW, CONFIRMED: the heal uses the PLAYER'S numbers, not the caster's

Coder's own `jedi_support_test.dart` proves `jediSupport` fires and
*something* heals — it checks vitality rose, never checks the amount is
right for who actually cast it. Reading `_rollPowerAmount` first
(`play_screen.dart`): its ability-modifier term reads `_me?.modifierOf(ab)`
and its Force-level term reads `widget.character?.classes` and
`_forceLevels()` — both **unconditionally the player's own combatant and
record**, with no caster parameter anywhere. `_useSupportPower` passes a
real companion `caster` into `_applyPower`, but `_applyPower`/
`_rollPowerAmount` never receive it and still read `_me`.

`heal`'s own formula (`base-rules/rules/powers.toml`): `5 + Charisma
modifier + Wisdom modifier + Force levels`. I gave the player a Soldier
(grants no Force) with Charisma 8 / Wisdom 8 (both `-1`) — predicting
**3** if the defect is real — and a companion caster a level-6 Jedi
Consular with Charisma 18 / Wisdom 18 (both `+4`) — predicting **19** if
the cast correctly used the caster's own numbers.

```
⚠⚠⚠ A DOCTRINE-CAST HEAL'S AMOUNT — THE CASTER'S OWN NUMBERS, OR THE
PLAYER'S — TEST 137
Expected: <19>
  Actual: <3>
```

**The healed amount was 3 — the player-derived prediction, exactly.**
Confirmed twice (the number matched precisely both times the fixture
finally isolated a clean, unconfounded hit-then-heal cycle). A doctrine-cast
Heal from any companion whose Charisma, Wisdom, class or level differs from
the player's own lands the WRONG amount, silently, always — the same shape
as TEST 136's `item.acquired` "you" defect: a mechanism built generically
that quietly defaults to the wrong character.

⚠ **Two fixture problems on the way to this result, recorded because they
cost real time and are worth knowing about for anyone building a similar
bed:** first attempt had the player one tile from the thug and the thug
attacked the player exclusively for 60 rounds regardless of who "started"
the fight, discovered only by adding `Vess Taran` to the tracked-vitality
diagnostic (the player's own handle is a real key in `vitalityForTest`,
same as any other combatant — I hadn't checked it). Second attempt switched
control to the companion (Track A) and had it make contact instead, which
did not change the thug's target at all — the player was still the one
being hit. What actually worked was moving the player nine tiles away, out
of the thug's reach entirely, leaving the companion as the only reachable
target.

**This has not been flagged to Coder yet — TEST reports findings, MAIN
routes them.**

## 5. PT-2598 — the two named items, confirmed

**Abilities' empty-list reason** — through a real `PlayScreen` built with
no `chargenData` at all (not a synthetic null passed to the widget
directly):

```
⚠⚠⚠ NO chargenData — THE REASON SHOWS, ON ALL THREE TABS, NOT A SILENT
EMPTY LIST
All tests passed!
```

The reason text (`"rules data could not be loaded — skills, feats and
powers cannot be listed here"`) appears on SKILLS (the default tab), and
survives switching to POWERS and to FEATS — confirming `play_screen.dart`
actually constructs and passes `unavailableReason` through the real board,
not just that `AbilitiesScreen` renders it when handed one directly (which
is what Coder's own `the_abilities_screen_test.dart` already covers).

**Level Up / Character Sheet overlap** — Coder's own new regression test
(`a_portrait_opens_its_own_screen_test.dart`) proves the sheet closes when
Level Up opens and that escape does neither ambiguous thing, through the
real board. I did not duplicate it; the hands-on look the routing offered
as optional was skipped for the same reason as always — see §6.

## 6. The GUI input blocker — not retried

Reproduced and stable across TEST 134/135/136; not worth another attempt
without a changed environment. Everything above is headless, through the
real widget tree.

---

## Fixtures

All scratch, in `$S/app-head2/test/`, deleted after this pass; nothing
added to the live repo or the shelf beyond the `tester-effects` package
that was already there from TEST 136:

- `tester_own_trigger_effects_play_test.dart` — rewritten for §1, 4 tests.
- `tester_own_hands_off_fights_test.dart` — §3, 1 test.
- `tester_own_jedi_support_numbers_test.dart` — §4, 1 test (the severe
  finding).
- `tester_own_abilities_reason_test.dart` — §5, 1 test.

No stray processes at the end of this pass — checked via `ps aux` for
`flutter`/`dart`, none found.
