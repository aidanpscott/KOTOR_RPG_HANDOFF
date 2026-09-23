# TEST 135 — feat-chain progression, and the Sith schedule

**Build.**

```
local HEAD            d98d894  "Feat-chain progression finally reaches
                                real level-up — PT-2579"
working tree            clean at that sha (archived into an isolated scratch
                        copy, same discipline as TEST 134)
pubspec.lock resolves   lodestar  7cd04110b083d2dbb6b566eba9c0b13777d49f3a
                        lens      32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd
package_config.json     ~/.pub-cache/git/Lodestar-7cd04110.../
                        ~/.pub-cache/git/Lens-32b77e3b.../
built from              git archive d98d894
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints.

**Verdict — both confirmed, both decisively, neither in play.** The GUI is
still not taking input in this environment (checked again today, twice, with
the same control as TEST 134 — see §3). Everything below is independent
headless confirmation: I ran Coder's own tests, then read them closely enough
to see what they didn't cover, then wrote and ran my own fixtures — including
a mutation test that proves my own test would have caught the original bug.

---

## 1. The feat-chain fix — all three routed states, confirmed

The routing asked for three things in one character: a first-tier feat
offering its next link, a full chain offering nothing further, and an
untouched chain still offering its head. Coder's own new door test covers
only the first of these through the real screen (`toughness` alone →
`Improved Toughness` offered). I wrote my own character carrying all three
states at once and drove it through the identical real door — secondary-tap
the portrait, `Level Up`, the real `Abilities` and `Skills` steps, the real
`Feats` tab, no shortcuts:

```dart
feats: [
  {'id': 'toughness'},            // partial — one link held
  {'id': 'cautious'},             // )
  {'id': 'improved_cautious'},    // ) the WHOLE Cautious chain, all
  {'id': 'master_cautious'},      // ) three tiers, held in full
],
// 'Gear Head' never touched at all — the untouched-chain control
```

```
$ flutter test test/tester_own_feat_chain_check_test.dart
⚠⚠⚠ ALL THREE ROUTED STATES, ONE CHARACTER, THE REAL DOOR — TEST 135
All tests passed!
```

Assertions, all in one run:

```
Improved Toughness   found        ← partial chain offers the next link
Toughness             absent      ← the held head does not reappear
Cautious              absent      ← full chain offers nothing — the head
Improved Cautious     absent      ← full chain offers nothing — the middle
Master Cautious       absent      ← full chain offers nothing — the last
Gear Head             found       ← untouched chain still offers its head
```

⚠ **My first attempt was wrong, and worth recording.** I picked level 6→7 for
the transition and the test failed reaching "Level Up" at all — level 6 with
xp exactly at `xpToReach(6)` has no level pending, so the secondary tap opens
Equip, not the sheet (`PT-1134`). My second attempt kept level 6→7 but with
enough xp, and the **Abilities** tab then wasn't found — level 7 grants no
ability point (only every fourth level), so that tab isn't reachable at all,
an unrelated confound. I settled on mirroring Coder's own known-working
transition exactly (Soldier, level 3→4, xp 6000) and changed only the `feats`
field — which is what the run above used, and what passed.

### The mutation — my own test proves it discriminates

I reverted `LevelUpStep.feats`'s call, in my scratch copy only, back to
the pre-fix line:

```dart
heads: widget.chargenData?.buyableAtFirstLevelFor(isDroid: _isDroid) ??
    const [],
```

and reran the same test against nothing else changed:

```
StateError: Bad state: No element
  … scrollUntilVisible(find.text('Improved Toughness'), …)
Some tests failed.
```

`Improved Toughness` never renders under the old call — it can't scroll to
what isn't there — so the test fails loudly rather than silently passing.
Restored the file afterward; a diff against the pre-mutation copy shows no
difference, and `git status` on the real repo's `play_screen.dart` was clean
throughout (the mutation never touched anything but my own scratch tree).

### Coder's own three files, run by me

```
$ flutter test test/the_level_up_door_test.dart test/feat_eligibility_test.dart \
    test/the_grant_schedule_audit_test.dart
All tests passed!   (16 tests)
```

Including the exact real-door case: *"A character who holds the head is
offered the next link — PT-2579, through the real Feats tab."*

## 2. The Sith feat schedule — confirmed through the real parser

⚠ **This fix is content-only** — the commit touching it (`f8a460d`) changes
no app code, only an audit test's pins, because the actual correction lives
in the shelf's own `classes.toml`. I read that file directly first, then
confirmed the same thing through the product's own parser rather than
trusting my reading of the TOML:

```
$ flutter test test/tester_own_sith_schedule_check_test.dart
All tests passed!   (3 tests)
```

```
sith_warrior.featLevels  ==  jedi_guardian.featLevels   exactly
  [1,3,4,6,7,9,10,12,13,15,16,18,19,21,22,24,25,27,28,30]
  len 20 (feats_at_30) · 13 entries ≤20 (feats_at_20)

sith_assassin.featLevels ==  jedi_sentinel.featLevels    exactly
  [1,3,6,7,9,12,13,15,18,19,21,24,25,27,30]
  len 15 (feats_at_30) · 10 entries ≤20 (feats_at_20)
```

Both are **element-for-element identical**, not merely the same length or the
same two headline totals — and both totals are themselves derived from the
array in my assertion (`.length`, `.where((l) => l <= 20).length`) rather than
typed a second time, so a drifted total couldn't pass by coincidence with a
drifted array.

### The control

```
sith_warrior.featLevels  is NOT  jedi_consular.featLevels
```

Sith Warrior is a combat-rate class; Jedi Consular is not — their real
schedules differ. This is what makes the two equality checks above a
finding rather than an assertion that happens to be true of any two classes:
if this control had also passed as equal, the technique would prove nothing.

I did not mutate the shelf file itself for this one — it's the real,
shared `~/.local/share/kotor-rpg/packages`, and the discriminating control
above does the same job a mutation would: it shows the comparison is capable
of failing.

## 3. ⚠ Why this is headless confirmation again, not a live pass

Checked twice today, independently, both with the required control:

```
fresh relaunch, click, wheel, keys      zero pixel change, both times
control: type into a throwaway xterm    landed correctly, both times
```

The display itself was quiet both times — no game process, no `gdb`, load
average under 0.5 on four cores — which rules out the contention I flagged as
a possible cause in TEST 134. This has now reproduced identically across two
separate sessions under different load conditions, which reads less like
transient contention and more like something stable about this build or this
container's input path that I can't fix from here. I'm not spending further
time forcing it without a different angle; happy to try again if the
environment changes, or if a manual check from the user's own hands would
settle it faster than more automated retries.

## Fixtures

Two new test files, mine, in the scratch build only (never touched the live
repo):

* `test/tester_own_feat_chain_check_test.dart` — one character, three chain
  states, the real door, mirroring Coder's own known-working level
  transition so the only variable is the fix under test.
* `test/tester_own_sith_schedule_check_test.dart` — three assertions through
  `ChargenSource.load`, with a discriminating control.

Both deleted from my scratch tree after this pass; nothing was added to the
shared repo or the shared shelf.
