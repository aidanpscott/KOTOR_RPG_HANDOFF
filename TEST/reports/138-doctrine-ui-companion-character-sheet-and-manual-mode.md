# TEST 138 — PT-2607 re-check, the doctrine UI, the companion character-sheet thread, manual mode

**Build.**

```
local HEAD              61e629a  "Reconcile combat's per-fight maps with a
                                  companion's real, current level"
working tree             clean at that sha when archived; git-archived into
                        an isolated scratch copy ($S/app-head3)
pubspec.lock resolves    lodestar  0cbb4336c52d62b96839d69499c8b7ede9bb7d4e
pub-cache checkout       ~/.pub-cache/git/Lodestar-0cbb4336.../ — present,
                        confirmed against the lock before anything ran
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints. The live `KOTOR-RPG-APP` repo picked up genuine, uncommitted,
mid-edit work from Coder partway through this pass (`lib/play/
play_screen.dart` modified, `test/manual_companion_casts_test.dart` new) —
left entirely untouched, consistent with never fixing and never touching
the live tree; everything below ran from the git-archived snapshot only.
`Loom` clean throughout. HANDOFF itself carried one foreign, unrelated
uncommitted change (`BUILD/screens/76-party-selection.png`, a modified
screenshot) — stashed before pulling 40 commits, restored after, left as
found.

**Verdict — all four items confirmed. Zero new defects.** A genuinely
large batch, and everything routed held up, including one real gap I
closed myself (Force-pool exhaustion falling back to a weapon attack,
never previously exercised) and one methodology lesson from re-running my
own TEST-137 fixture against newer mechanics.

---

## 1. PT-2607 — re-confirmed, via a different method than TEST 137's own

My original TEST-137 fixture (a full end-to-end fight) no longer isolates
cleanly on this build: companions now carry a real, spendable Force pool
(`ec5b102`), so the same jediSupport companion that reliably healed itself
in TEST 137 now spends its pool on repeated `force_valor` self-buffs before
ever needing to heal, and the observed heal amount (1) matched neither of
my old predictions. Rather than fight the now-more-complex interaction,
I used the two new `@visibleForTesting` hooks Coder's own fix commit added
specifically for this (`rollPowerAmountForTest`, `combatantForTest`) to
call the exact production arithmetic directly against a real companion:

```
⚠⚠⚠ RE-CHECK — heal's roll uses the CASTER's own Cha/Wis/Force levels,
not the player's — PT-2607, TEST 137 R2
⚠ RE-CHECK: amount=19 derivation="5 +4 cha +4 wis +6 level 19"
All tests passed!
```

19 — the caster's own real stats (Cha 18, Wis 18, level 6, all Force) —
not 3, what the player's stats (Cha 8, Wis 8, no Force levels) would give.
The fix holds.

## 2. The doctrine-changing UI — all three routes, confirmed sharing one state

Coder's own suite (`doctrine_picker_test.dart`, `radial_wheel_test.dart`,
`real_preset_through_the_ui_test.dart`, 14 tests) already proves each
route independently sets the identical `doctrineForTest` value on its own
companion. What none of them do is exercise more than one route against
the *same* companion in one continuous session — so I wrote that:

```
⚠⚠⚠ ONE COMPANION, THREE ROUTES IN SEQUENCE — EACH OVERWRITES THE SAME
UNDERLYING STATE, NOT A SEPARATE COPY OF IT
All tests passed!
```

Sidebar → Jedi Support, then PartyScreen (same still-fielded companion,
not dismissed) → Healer overwrote it, then the radial wheel → Aggressive
overwrote that. Confirms all three routes read and write one shared piece
of state rather than three independent ones that happen to agree in
isolation.

## 3. The companion character-sheet thread — confirmed, one real gap closed

Ran all five of Coder's own dedicated files (13 tests total, one file
name I initially mistyped and re-ran separately — my own error, not a
finding): recruitment seeding, undivided subject-tagged combat XP, the
fully interactive level-up wizard (same steps as the player's own, proven
never to cross-contaminate the player's progress, survives a reload),
Force-pool affordability and spend/persist, Treat's medpack waiver, and
combat correctly reading a leveled-up companion's *current* stats rather
than the frozen blueprint. All pass.

**Force pool running low and falling back to a weapon — not covered by
any existing test, closed here:**

```
⚠⚠⚠ A DEPLETED FORCE POOL — THE COMPANION KEEPS FIGHTING WITH A WEAPON,
NOT HOLDING
⚠ padawan pool before: 12/12
⚠ padawan pool after: 4/11 everCastEver=true everRanDry=true
struckAfterDry=true
All tests passed!
```

A level-1 Jedi Consular (pool 12, `force_valor`/`heal` both cost 8) casts
once, is left with 4 — genuinely below the cost of anything it knows —
and keeps landing real hits on the thug afterward rather than holding.
Confirms `Doctrine.decide`'s own `canCast`-refuses-so-`continue`-to-the-
next-rule mechanism (proven in Lodestar's own suite) actually reaches the
`targeting` attack tail for a real companion with a real, exhausted pool,
not just in the abstract.

⚠ My own first attempt at this test asserted the pool hit exactly `0`,
which it never does — it gets stuck below the cost (`4 < 8`), not driven
to zero. A wrong assertion on my part, caught by reading my own printed
diagnostic before concluding the claim was false.

**Treat**, confirmed by name, standalone:

```
⚠⚠⚠ TREAT STABILIZES A DYING ALLY WITH NO MEDPACK IN THE BAG
⚠⚠⚠ AND A MERELY WOUNDED ALLY — NOT DYING — STILL REFUSES WITH NO
MEDPACK, THE ORDINARY RULE UNCHANGED
All tests passed!
```

Both halves of the routed claim hold: dying is waived, wounded is not.

**Combat XP → real threshold → wizard**, considered and not independently
re-chained: Coder's own suite proves real combat XP lands subject-tagged
(one test) and proves the wizard opens correctly given an XP-crossing
event (a second test, deliberately injecting a realistic amount rather
than grinding the CR table — their own stated reason: *"grinding the
exact CR table to 6000 would test the table, not the door"*). That's a
reasonable, well-justified split rather than a real gap; chaining them
into one continuous test would mostly re-prove the same two already-solid
claims at a much higher cost, so I left it alone.

## 4. Combat manual mode — confirmed, both halves

```
$ flutter test test/manual_companion_moves_test.dart \
    test/manual_companion_strikes_test.dart
All tests passed!   (6 tests)
```

A manual companion's own turn genuinely stops the round for real input,
the player can move them and strike with them on their own turn, ending
the turn advances the round, and hands-off/auto companions are completely
unaffected by any of Slice 1/2's own mechanism — exactly the routed claim,
already fully covered.

---

## Fixtures

All scratch, in `$S/app-head3/test/`, deleted after this pass:

- `tester_own_recheck_roll_power_amount_test.dart` — §1.
- `tester_own_doctrine_cross_route_test.dart` — §2.
- `tester_own_force_exhaustion_switches_to_weapon_test.dart` — §3, the one
  genuinely new coverage this pass adds.

No stray processes belonging to this session at the end of this pass —
one long-running `flutter_tester` process pointed at the live repo's own
`package_config.json` was found via `ps aux`, not touched (not mine —
Coder's own concurrent work, matching the uncommitted `play_screen.dart`
changes found in the live tree).
