# TEST 069 — the locked sidebar design (PartySidebar, APP-UI-VISION-01,
# PT-1102/1110/1111/1124/1132/1133) driven live: left-docked, persists
# through exploration, portrait treatment identical for self and party,
# enemies inverted, PT-1795's name-not-tag fix holds across a door
# crossing mid-fight — plus one real, reproducible className casing gap

**Built against two builds this session**, since HEAD moved twice more
while I was reading the source before testing:

- **First build** (used only to read the exploration/self-row/enemy-
  inversion cases, before I noticed the gap below): process started
  08:47; last commit before that was `01cc030` (08:42:51, *PT-1794: the
  sidebar APP-UI-VISION-01 locked, built to it* — the sidebar-shipping
  commit itself). This build predated `02bb8bb` (08:51:12, *PT-1795: an
  entry is named, not tagged*), which the file's own source comment names
  as closing a gap PT-1794 left open (a companion showing its raw tag,
  e.g. `mate.a01.01`, instead of its name). Since a room-declared
  companion already carries a proper name regardless of PT-1795, this
  first build's tests don't exercise that gap either way — noted only for
  the record, not relied on for the door-crossing confirmation below.
- **Second build**, the one the door-crossing confirmation and the final
  casing finding rest on: app PID `118187`, process started ~08:55:55
  (reconstructed from `ps -o etime` at check time, `09:04:09`, elapsed
  `08:14`). Local HEAD at that point: `02bb8bb` (08:51:12, *PT-1795: an
  entry is named, not tagged*) — confirmed last commit before the build
  by checking `a27edce` (08:57:12, *PT-1796: the low-health flash*) landed
  two minutes AFTER my build started, so PT-1795 is in and PT-1796 is
  not. `pubspec.lock`'s `lodestar` pin: `resolved-ref
  f1c2cc0adf2c59bcb5e76bbfa3b89a3f9c26147a`, set by `8626028` (08:14:13,
  well before this build), confirmed as an actual checkout at
  `~/.pub-cache/git/Lodestar-f1c2cc0adf2c59bcb5e76bbfa3b89a3f9c26147a`.
  `check_shelf.py` run immediately before writing this report (not just
  at session start, given how much time had passed): `✓ 25 rules files,
  all identical to what the extracts generate`.

App PID `118187` killed by PID at the end of the session, confirmed gone
(`ps -p 118187` empty). Coder's Loom (`12445`/`12443`) checked running,
untouched, before and after. No package touched this session beyond
`companion-fixture` (mine) — confirmed by mtime; the only files under it
newer than `base-rules` are the five weapon-item blueprints added in TEST
068, still in place and unchanged.

---

## 1. Left-docked, persists during exploration — CONFIRMED

Walked "Sura Sarn" (Human Soldier, Hunter → aptitude this run, not the
weapon item — didn't need it for this test) through chargen to `Play` in
`companion-fixture`'s `a01-corridor`. Outside any fight, the sidebar
rendered docked to the **left** edge of the screen, header **"your
party"**, showing both party members (Sura Sarn, self-bordered; Mate) as
portrait rows with vitality wings — not the old right-docked, combat-only
`RosterPanel` this replaces. No enemies listed, matching the `_sidebar`
getter's exploration-mode `order` (self + party members present, zero
enemies possible outside a fight).

## 2. Portrait, vitality wing, identical self/party treatment —
## CONFIRMED, with one real casing gap

Both Sura Sarn's and Mate's rows used the same vertical layout: portrait
circle, left vitality wing, text block (name, class·level, N of M). The
**only** visual difference on Sura Sarn's row was the selection border
(`C.accent` vs `C.rule` for Mate) — no card treatment, no distinct style,
matching PT-1132's "identical treatment, border is the only tell" lock.

**Found and confirmed reproducible: the class·level text differs in
casing between self and party rows for reasons unrelated to the widget.**
Sura Sarn's row read **"Soldier · 1"**; Mate's row read **"soldier ·
1"** (lowercase). Traced in `play_screen.dart`'s `_sidebar` getter: the
player's `className` is sourced from `widget.characterClass?.name`
(canonicalized), while a companion's comes from
`placed[h]?.characterClass` — the raw TOML `class = "soldier"` string,
which is lowercase by convention. Checked this isn't my own fixture's
quirk: `endar-spire/blueprints/characters/sith-trooper.toml` also writes
`class = "soldier"` lowercase, so this is the standard shipped authoring
convention, not a `companion-fixture` artifact. The widget itself treats
both fields identically (same `Text` styling, no special-casing) — the
inconsistency is entirely in which value each source of `className`
happens to hold. Confirmed present in **both** builds this session (the
first, PT-1794-only build, and the second, PT-1795-inclusive one), so
this is a separate, still-open gap — not something PT-1795 touched or
was expected to.

**Force wing — NOT checked.** Neither test character (Soldier, and the
first build's character) was Force-sensitive, so I only confirmed the
wing is correctly ABSENT when `force` is null, never confirmed it renders
correctly with an actual `ForcePool`. Flagging as unchecked rather than
claiming it.

## 3. Enemies inverted (bar above portrait, red, name-only) — CONFIRMED

Bumped `starter.corridor.01` to start a fight. All three enemy rows
(Starter, Chaser, and the raw-tagged `corridor.02`/`corridor.03` — see
note below) rendered with the health bar **above** the portrait
(horizontal), fixed **red** regardless of the app's theme (matching
PT-1109's "enemies are always red" rule, distinct from the vitality-state
colors party rows use), and the text block showed **only the name** —
no class, level, or N-of-M, matching the file's own comment that there's
no class/level/XP to show for an enemy. Party rows (Sura Sarn, Mate) kept
the vertical portrait-plus-wing layout throughout, correctly not
inverted.

*(Aside, not part of this task: the **turn-order list** at the top of the
sidebar — a separate small text list above the portraits, not itself
part of the PT-1132/1133 portrait design — showed raw tags
`corridor.03`/`corridor.02`/`corridor.01` rather than "Chaser"/"Mate"/
"Starter" for entries not yet individually resolved at that point in the
list. This is a different UI element from the portrait rows below it
(which did show real names for Chaser/Mate/Starter throughout) and wasn't
named in Coder's ask, so I'm not treating it as a finding against this
task — noting it only so it isn't mistaken for the same gap as §4 below
if it turns out to matter later.)*

## 4. PT-1795's name-not-tag fix confirmed across a door crossing mid-
## fight — CONFIRMED

This was the one sub-case worth specifically re-testing on the second
build, since a room-declared companion (like Mate, placed directly in
`a01-corridor`'s own `[[contents]]`) already carries a proper name and
wouldn't exercise the PT-1794→PT-1795 gap either way — only a companion
*reconstructed* via `_bringTheParty` from the party-join log (the path a
companion takes when it isn't re-declared in the room being entered)
would show the bug the source comment describes.

With the corridor fight still active (Chaser/Starter engaged, Mate at 57
of 60 after an early hit), moved Sura Sarn from the start tile across the
room to the door at `(9,1)` (`Down`, then `Right` ×5, end turn, `Right`
×5 again) and crossed into `a02-second-room`. Crossing the door ended the
corridor fight (log: *"in your campaign, a01-corridor left you at
57"*/*"...at 12"*) and dropped back into exploration mode — header
correctly reverted from **"in this fight"** to **"your party"**, with no
stale turn-order list or enemy rows left over. In the new room's
reconstructed party, **Mate's row read "Mate"** — the name, not a raw tag
like `mate.corridor.02` (which appears only in the plain-text status log
line below the grid, a different, tag-based line the sidebar itself
doesn't share) — confirming PT-1795's fix holds for exactly the
reconstruction path it was meant to cover. This also serves as a second,
independent confirmation of §1's "no stale combat text after leaving a
fight" concern, via area-transit rather than abandon-and-resume.

---

## What I did not check

- An actual Force-sensitive character's Force wing (see §2) — only
  confirmed correctly absent when null.
- Condition markers, XP wing, click-to-target — all explicitly out of
  scope per the file's own header comment (no mechanic/data exists yet
  for any of them), not defects to report.
- The turn-order list's raw-tag display noted as an aside in §3 — not
  part of this task's ask, not investigated further.
- Whether the corridor's automatic fight-end-on-area-exit (§4) is itself
  intended behavior or worth its own separate report — out of scope for
  a sidebar confirmation; noted only because it's what let me observe the
  reconstruction path.

## State

- `companion-fixture` (mine) — no new files added this session; the five
  weapon-item blueprints from TEST 068 are still in place, untouched.
- One save created and abandoned this session ("Sura Sarn"), reached
  `Play`, crossed one door mid-fight, not cleaned up — ordinary Tester
  artifact.
- App PID `118187` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
- `check_shelf.py` run at session start and again immediately before
  writing this report: clean both times, `25 rules files, all identical
  to what the extracts generate`.
