# TEST 140 — input was never the app, a full visual pass, and two real defects

**Build.**

```
local HEAD              1339b99  "Extract the remaining PT-2675 sweep —
                                  22 more real K2 assets"
pubspec.lock resolves    lodestar  15780d939801e4d651feff5b8a149d912d407177
pub-cache checkout       ~/.pub-cache/git/Lodestar-15780d93.../ — present,
                        confirmed against the committed lock
```

Archived from `git archive HEAD`, not the working tree. The `linux/`
platform directory is gitignored and absent from a fresh archive; rebuilt
it with `flutter create --platforms=linux .` before every build this pass,
deleting the stray `test/widget_test.dart` it drops each time.

**Verdict — the live visual pass MAIN asked for (doctrine picker, radial
wheel, cover tiles, B1 cycle, manual casting) is confirmed working. Getting
there took most of this pass: mouse input in this session's environment
looked dead for long stretches, and the cause was never the app.** It was
one `xdotool` usage bug, root-caused and fixed mid-session (below). Once
fixed, the pass surfaced two real, filed defects (PT-2687, PT-2688) plus
three smaller findings worth recording even though they aren't new bugs.

---

## 0. The input problem — root cause, not a workaround

`xdotool click --window <id>` sends the click via `XSendEvent`, which
`xev` shows as `synthetic YES`. GTK/GDK — the Flutter Linux embedder sits
on top of it — deliberately ignores synthetic X events for input: any
client can send one to any window, so accepting them as real input would
let one app fake clicks into another's. The X server delivered the event
every time; Flutter never saw it. Screenshots always looked correct
because `import -window` reads a window's content directly, bypassing
input entirely — which is exactly why this was so easy to misread as the
*app* not responding.

Real pointer motion kept working the whole time because `xdotool mousemove
--window <id>` warps the actual hardware pointer via XTEST — genuine input,
not synthetic. The fix: keep the `mousemove --window` warp, then drop
`--window` from the click/keypress itself. A bare `xdotool click 1` or
`xdotool key <k>` fires via XTEST at the pointer's current position or
whatever has focus, indistinguishable from real hardware input.

Checked this wasn't wishful thinking before trusting it: the Skills-step
"+" stepper that stalled a large part of this pass under the old click
pattern is exactly the button Coder's own `skills_test.dart` already taps
via `tester.tap()` — Flutter's own gesture path, not X11 — and it passed,
freshly re-run. The button was never broken.

This is almost certainly the same root cause behind the TEST 134/135
keyboard-input findings earlier in this project. Worth re-testing `xdotool
key`/`type` the same way next time keyboard input looks dead in this kind
of environment, before concluding it's an environment limitation.

## 1. B1 cycle button — confirmed

MANUAL → HANDS OFF → AUTO, full cycle, on the party sidebar. Screenshotted
at each state.

## 2. Doctrine picker — confirmed, both surfaces

**Sidebar flat list.** Opens on "Change Doctrine," shows the eligible set,
applies the selection — status bar updates to `<tag> — <doctrine>` on
pick, confirmed for both a Force class (Guardian: Aggressive / Jedi
Support / Healer, all enabled) and a non-Force one (Grunt: same three
listed, Jedi Support and Healer shown disabled with the reason printed
inline — *"requires a Force-sensitive class"*).

**Radial wheel.** Right-click ("secondary tap") on a party member's own
token opens it — found via `_openMenu`'s own comment (`PT-2617`): *"A
COMPANION'S OWN TOKEN OPENS THE RADIAL WHEEL INSTEAD."* Renders as a ring
of four round buttons — Wait here / Dismiss from party / Trade / Change
Doctrine — not a pie, exactly as routed. Hover highlight confirmed live.
"Change Doctrine" cascades into a second ring, same four position slots,
now holding the doctrine set (Aggressive / Healer / Jedi Support).
Selection applies — status bar confirms `guardian.v01.01 — Jedi Support`.

## 3. Cover tiles — confirmed rendering; live numeric bonus not reached

`halfCover`/`threeQuarterCover`/`wall` all render as visually distinct
shapes on the board (screenshotted against a real authored area TOML).
The live Defence bonus while standing on one, during a real fight, was not
reached this pass — every fight I got into clustered participants away
from the tiles authored into this small test hall before I could check the
number. Not an open question about correctness: TEST 139 already proved
the mechanic itself, headlessly, through `myDefenceTermsForTest`. Left for
a next pass to re-confirm live.

## 4. Manual companion casting — confirmed, after a wrong first conclusion

**First conclusion, wrong, corrected the same pass:** I initially reported
there was no way to trigger a manual companion's combat action at all —
clicking a companion's own token opened only the out-of-combat wheel,
clicking an enemy while a companion was "selected" produced *"walk into
them to act — choose an action first to aim at somebody,"* and arrow keys
during a companion's turn moved the **player's** token, not the
companion's. I concluded the trigger didn't exist.

It does. Every combatant's own turn — including a MANUAL companion's —
exposes a letter-key action menu: `f powers · c scan · d disengage ·
s hide · h hurry · t treat · r repair · o throw · g gear · space to end
your turn`. I'd only seen the hint bar render during the *player's* own
turn and never tried a letter key during a companion's. Pressed `f`
during Grunt's manual turn: *"Grunt knows no Force powers"* — correct,
Grunt is a Soldier. Same key during Guardian's turn: *"Guardian knows no
Force powers"* too — both honest, correct refusals to a real keypress,
not silence. The UI is built and works.

**A real, separate finding underneath the correction:** Guardian is
authored as a level 6 Jedi Consular in this package's own
`blueprints/characters/guardian.toml` and still knows nothing. Checked
`character_open.dart` — the parser for that whole file format — line by
line for anything power-related. There is none. A companion placed via an
area's `[[contents]]` (the mechanism a package author uses to hand the
player a henchman without going through a story recruitment) can be given
a class, levels, abilities, equipment, skills — never a power, regardless
of class. Whether real shipped companions who cast powers reach the party
through a different path (the recruitment ledger, which does carry
`character.power-taken` — that's how TEST 139's own Aid test built its
companion) is not something I checked this pass. Worth Coder or MAIN
confirming: can a package author give an area-placed henchman any Force
power at all, through any authored format, today? If not, Jedi
Support/Healer doctrines and manual casting are both structurally
unreachable for that whole class of companion, independent of the UI
question above.

## 5. Custom doctrines (`[protects]`, `blueprints/doctrines/*.toml`) — not
   reachable from the in-game picker; not confirmed applied either

Authored a real one to check the `Protects` rule properly, rather than
guess at it from the engine source alone:

```toml
# blueprints/doctrines/guard-grunt.toml
[doctrine]
name = "Guard Grunt"
goal = "protect the wounded soldier"

[protects]
match = { handle = "grunt.v01.01" }
because = "grunt"
```

Referenced it from Guardian's own blueprint (`[attachments] doctrine =
"doctrines/guard-grunt"` — the field `character_open.dart` actually reads)
and loaded a fresh save that had never entered the area before, so
Guardian would be created from the updated blueprint rather than a
cached one. `check_shelf.py`-style package loading reported no new
problems for this package, so the file parses. **The picker still only
ever showed the same three built-in presets — Aggressive / Jedi Support /
Healer — never "Guard Grunt."**

Ran out of pass time before I could settle the more important question
this raises: is the doctrine silently **applied** anyway at creation
despite never appearing as a choice (which would make this a picker-only,
cosmetic gap), or does `[attachments].doctrine` not take effect for a
party member at all (which would mean `Protects` is currently unreachable
in play by any authoring path)? I got as far as starting a fight to watch
for a `protects:grunt` retaliation line and didn't get a clean read before
the pass ended. Left open, not filed as a defect — I don't have enough to
tell which it is yet.

## 6. PT-2687 — a joined companion's data overwrites the player's own
   character sheet

Filed and pushed mid-pass (`f4f77ea9`). Full mechanism: the save format
writes one combined event log holding the player's own events *and* every
companion's full creation log, each event tagged with a `subject` field.
`play_screen.dart`'s `_classesNow()` (~line 3202) builds the player's own
class summary from `widget.character.classes` with no filter on `subject`
at all, so a joined companion's `class-added`/`levelled` events land in
the same tally as the player's. My own single-class, level 5 Soldier
displayed as "Soldier 9 / Jedi Consular 6" — exactly my Soldier 5 + Grunt's
Soldier 4 + Guardian's Jedi Consular 6, both joined companions in the same
save. The full character sheet (CHR tab) was worse: my own ability scores
displayed as Grunt's exact numbers (STR 12/DEX 10/CON 12/INT 10/WIS 10/CHA
10) and "level 4" instead of what I authored — last-write-wins across the
whole combined log, no subject filter, so the last-joined companion's
events silently overwrite the player's display. Reproduced three separate
ways: the sidebar line, the full sheet, and the live combat log's own
party-status line — independent of the equipment defect below, confirmed
by re-authoring the same character with no armour at all and watching the
contamination persist unchanged.

## 7. PT-2688 — the real item-loading defect is systemic, not one item

Isolated deliberately rather than assumed identical to PT-2687 because
they co-occurred: the CHR sheet refused to open `items/armour/clothing`
(*"There is no item here"*) even though `resolveStartingArmour` named it
with confidence, no refusal returned. Re-authored the same character with
no armour authored at all; Defence then computed cleanly (`base 10`, no
error) — rules out the contamination bug as the cause of that specific
error. Then, in a real fight, the same shape hit the **weapon**: the
combat log's own line reads `equips 'items/weapons/blaster-rifle', which
will not open: There is no item here` — `resolveStartingWeapon` also named
that path with confidence. Two different resolvers, two item categories,
same failure: whatever these resolvers hand back as a path is not
reliably what the runtime item loader can open. Filed and pushed
(`d54c9ec8`), routed to Coder as severe.

## 8. Two things worth recording that are neither bugs nor open questions

- **Click-to-target for a combat action is explicitly unruled**, not
  missed by me. `play_screen.dart`'s `_walkTo`, at the exact line that
  produces *"walk into them to act,"* states plainly (`PT-1108`/`PT-1425`/
  `PT-1443`) that clicking a creature is deliberately not an attack
  trigger — the intended flow is action-first, then a target picker that
  the comment itself calls *"still unruled."* Bump-to-attack via arrow
  keys is the only affordance today, and it is wired to the player only.
- **"Leave Session" autosaves the live character back over whatever file
  it was loaded from.** Overwrote one of my own hand-authored test saves
  mid-pass with the corrupted live state I was trying to isolate away
  from. Not a defect — worth remembering when hand-authoring saves for
  future testing: use a fresh filename per revision, or expect the file to
  change under you on exit.

---

## Fixtures

- `~/.local/share/kotor-rpg/packages/tester-visual/` — a real shelf
  package built this pass: a 12×4 hall (`v01-hall.toml`) with an authored
  `halfCover`/`threeQuarterCover`/wall row, three character blueprints
  (`guardian` — Jedi Consular, `grunt` — Soldier, `hostile` — Soldier,
  enemy), and one custom doctrine (`guard-grunt.toml`, §5 above). Left in
  place; useful for a next pass to pick up where this one stopped,
  including re-confirming the live cover bonus and settling the open
  `Protects` question.
- `tool/author_tester_visual_save.dart` — a real, reusable authoring
  script in the app repo's own `tool/`, alongside the existing
  `author_gate_and_grant_save.dart` precedent it follows: builds a player
  character through the real `ChargenSource`/`resolveStartingWeapon`/
  `resolveStartingArmour`/`levelUpTo` calls rather than a hand-rolled
  header or guessed item paths, then reads the save back to confirm.
  Written to work around the Skills-step click issue before its root
  cause (§0) was found; kept because it's a real, working tool now that
  the cause turned out to be elsewhere — a legitimate way to get a
  chargen-skipping test character into a real area without touching
  chargen at all. Was untracked in the live repo; committing it with this
  report.

No stray processes: every launched instance this pass was killed by its
own recorded PID, never by name or pattern — the display was shared with
Coder for the input-diagnosis portion, confirmed via `xdotool
getwindowpid` cross-checks before ever screenshotting or clicking.
