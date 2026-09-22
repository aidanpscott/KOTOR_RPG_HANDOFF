# TEST 134 — the credits fix, confirmed headlessly, not in play

**Build.**

```
local HEAD            8c86941  "Store, Inventory and the dialogue gate all
                                read the real credits — PT-2566/2570"
working tree           clean at that sha (archived, not the live checkout —
                       Coder has unrelated dirty test files on top of the
                       same commit right now; see §4)
pubspec.lock resolves  lodestar  7cd04110b083d2dbb6b566eba9c0b13777d49f3a
                       lens      32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd
package_config.json    ~/.pub-cache/git/Lodestar-7cd04110.../
                       ~/.pub-cache/git/Lens-32b77e3b.../
built from             git archive 8c86941
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints.

**Verdict — real, but not the confirmation I usually file.** I could not get
a hands-on, pixel-verified play-through of `tester-purse` this pass. The GUI
became genuinely unresponsive to all synthetic input partway through this
session, on a shared display that other work is actively using at the same
time, and I stopped rather than keep fighting it. **What I have instead is
independent, non-mocked confirmation from running the real test suite myself**
— Coder's own new end-to-end test, against my own git-archived build, opening
the real files from the real shelf — plus a static sweep that closes the
question TEST 132 raised about a third reader.

---

## 1. The static sweep — no third reader

```
lib/play/play_screen.dart:1871   creditsAfter(_log, subject: handle, starting: …)      Store
lib/play/play_screen.dart:2289   creditsAfter(_log, …, starting: equipment['credits'])  Inventory
lib/play/play_screen.dart:5706   creditsAfter(_log, …, starting: equipment['credits'])  Dialogue
```

Every remaining use of `equipment?['credits']` in `play_screen.dart` is now
exclusively the `starting:` argument fed into `creditsAfter` — none of the
three sites hands a raw field value to a screen as the displayed total.

```
grep -rn "equipment?\['credits'\]|equipment!\['credits'\]" lib/ | grep -v play_screen.dart
```

returns nothing — no other file in `lib/` reads the field at all.

## 2. Independent confirmation — I ran the real test myself

Coder's new file, `test/the_payment_gate_reads_the_real_credits_test.dart`,
replays TEST 133's own sequence: walk into the merchant, confirm the 400 gate
passes and the 600 gate is hidden, open the store, sell a vibroblade, confirm
Store reads 600, close to the counter node, open the Inventory, confirm 600
there, re-bump the merchant, confirm the 400 gate still passes and the 600
gate now opens.

⚠ **I read it before trusting it.** It opens `tester-purse` through
`sandboxed()`, which snapshots the REAL `~/.local/share/kotor-rpg/packages`
directory (`Locations.desktop()`) into an immutable temp copy — not a mock,
not hand-typed fixture data inside the test file. The merchant, the board,
the conversation and its two payment gates are my own files, read off disk.

I built the app from a clean `git archive` of `8c86941` into my own scratch
copy (not Coder's live, currently-dirty checkout — see §4) and ran the test
myself, headlessly, no GUI involved:

```
$ flutter test test/the_payment_gate_reads_the_real_credits_test.dart
00:01 +0: ⚠⚠⚠ THE DIALOGUE GATE, THE STORE AND THE INVENTORY ALL AGREE —
          TEST 133, PT-2566/2570
00:05 +1: (tearDownAll)
00:05 +1: All tests passed!
```

One test, one assertion chain, and it passed against my own fixture through
my own build.

## 3. The shortfall-wording fix — also run myself

`test/terminal_panel_test.dart` and `test/door_lock_test.dart`, together:

```
$ flutter test test/terminal_panel_test.dart test/door_lock_test.dart
...
⚠⚠⚠ AN OPTION THE PLAYER CANNOT AFFORD IS MARKED, NOT HARDCODED AFFORDABLE
⚠⚠⚠ A FREE REPLY REACHES THE PANEL TOO, NOT ONLY COSTED ONES
...
02:07 +35: All tests passed!
```

`door_lock_test.dart` asserts the exact wording directly, on a bed carrying 2
spikes against a 3-spike cost:

```dart
expect(o.held, 2, reason: '…a stale/hardcoded held count would not track
    this bed's own real supply');
expect(find.textContaining('you have 2 spikes'), findsWidgets);
expect(find.textContaining('you have none'), findsNothing);
```

That is the exact defect TEST 132 filed — a fixed *"you have none"* printed
while the readout two rows below read `Spikes 1`. `TerminalOption` now
carries `held`, and `optionLine` reports the real count.

## 4. ⚠ Why I stopped trying to drive the GUI myself

Partway through this session my window stopped responding to any synthetic
input — clicks, wheel scroll (shift-held and plain), keyboard, and a
click-drag all produced **zero** pixel change, including on a **freshly
relaunched instance never touched before**. I did not conclude this quickly;
I checked the actual candidates before giving up on the live pass:

```
pointer position after a targeted move    correct — reported inside my window
window stacking (raised + activated)      confirmed on top; a full-desktop
                                           screenshot showed my window's own
                                           title bar, no overlap
WM_HINTS / _NET_WM_STATE                  "Client accepts input: True",
                                           _NET_WM_STATE_FOCUSED set
XTEST / X11 session                       present; XDG_SESSION_TYPE=x11
stuck modifier                            explicitly released; no change
CPU contention masking a delayed repaint  waited 3s after a click; still zero
xdotool/X11 input in general              WORKS — typed into a throwaway
                                           xterm and it landed correctly
```

The control in that last row is the one that matters: **the same tool, the
same session, the same moment, worked perfectly on a different window.** The
problem is scoped to this one Flutter window in this one session, not to my
input method or to the display server.

⚠ **And the display was genuinely shared and busy at the time.** A live
`gdb`-attached capture session against `swkotor.exe` (the vanilla game, a
separate investigation) was running when this session started; the
KOTOR-RPG-APP working tree itself had unrelated dirty test files
(`power_target_test.dart`, `powers_test.dart`, a new
`zz_six_tier_shot_test.dart`) from Coder's own in-progress slice; and a
concurrent `flutter test` invocation was running in that same live checkout,
pulling real CPU. None of that reached into my own isolated `git archive`
copy or its build — the archived commit and the packages I compiled are
untouched by any of it — but it is the kind of contention the standing
practice about a shared display warns about, and I chose to stop rather than
keep contesting it.

**What this means for the confirmation:** I did not watch the sale happen on
screen, read the readout with my own eyes, or type into the Notes-style
autofocus check this batch didn't route. What I did do is run the actual
production code, against my own real fixture files, through the actual
automated test harness, myself — which is a real and independent check, just
not the one I usually file. I'm not certain a genuinely fresh window and a
quieter moment on the display wouldn't work fine; I simply didn't spend
further time finding out today.

## What I'd still want, if the display is available later

A hands-on walkthrough of `tester-purse` exactly as in TEST 133 — sell, close
to the counter node, re-bump the merchant, read the three numbers with my own
eyes — remains the more decisive form of confirmation this project's standing
practice asks for, and I'd rather do it than not. Fixture, saves and scripts
are unchanged from TEST 133 and ready.
