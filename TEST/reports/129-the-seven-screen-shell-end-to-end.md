# TEST 129 — the seven-screen shell, end to end

**Build.** App **`c87a05b`** ("The sidebar portrait is square too — PT-2536"),
tree clean, built from `git archive` of that sha. The committed lock resolves
Lodestar **`29c636b7`** — it has MOVED from `46f0fcea`, which every report up
to TEST 128 declared — and `29c636b7` is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules files
and 65 standard blueprints.

**Verdict.** The shell holds. Items 1, 3, 6 and 7 pass in full, and item 2
passes every clause you named. **Six real defects**, two of them severe:

* **16 of the engine's 21 conditions are listed under GOOD EFFECTS**, including
  `paralysed`, `helpless` and `prone` — §4.
* **A note cannot be typed.** The field is never focusable — §5.
* A dismissed companion is listed by its raw tag, and re-adding one produces a
  phantom until the next room load — §2.
* Escape does nothing on Journal, Messages, Notes or Party Selection — §6.
* `character.levelled` reads *"A level is waiting"* for levels already taken —
  §4.

⚠ And one correction to a premise in the routing: *"Good Effects will
legitimately be empty"* is **not true on this build** — see §4.

---

## 1. The shell — confirmed

### The bar is in the same place on all seven

Measured on each screen, not eyeballed. The slot boxes' own top border row:

```
              top border   slots                    x span        pitch
EQU   y 85    1245-1297 …  seven                    1245-1659     60/61
INV   y 85    identical                             1245-1659     60/61
CHR   y 85    identical                             1245-1659     60/61
ABL   y 85    identical                             1245-1659     60/61
PTY   y 85    identical                             1245-1659     60/61
JRN   y 85    identical                             1245-1659     60/61
OPT   y 85    identical                             1245-1660     60/61
```

Every slot is 52 or 53 wide on a 60/61 pitch, and the band is `y 85-137`
throughout. The one-pixel variations are the lit slot's brighter border
widening its own run by a pixel, not the bar moving.

### Nothing is dim, and all seven open their own screen

On each screen the six unlit slots measure **border 23, text 312**, and the lit
one **border 170, fill 76, text 586** — so no slot is drawn as unavailable.
That matches the source: `play_screen.dart:1365` now passes
`unavailable: (_) => null`.

Each click lit its own slot and opened its own screen — `EQUIP` · `INVENTORY`
(with the seven-category filter strip) · the character sheet (`Whisper · Jedi
Consular · level 12`) · `ABILITIES` · `PARTY SELECTION` · `JOURNAL` ·
`OPTIONS`. No silent absence, nothing unreachable through the bar.

⚠ **PT-2530's refusal path is now unexercised.** Every slot is built, so
`onRefused` never fires. The fix from TEST 128 is in the code
(`nav_bar.dart:154`, `onTap: why == null ? () => onGo(s) : () => onRefused(s,
why)`) and I could not reach it — no slot refuses anything.

### ⚠ Four of the seven cannot be reached from the board

The board draws **no nav bar** — its own verb line is
`arrows to move · m map · i carrying · esc options`. And `_journal = true` and
`_party = true` appear at **exactly one call site each** in all 14,843 lines of
`play_screen.dart` (`:1390`, `:1392`), both inside the nav bar's `onGo`. There
is no keyboard shortcut for either, where the bag has `i`, Abilities has `v`
and the map has `m`.

So Journal, Messages, Notes and Party Selection are reachable only by first
opening one of the other screens — secondary-tapping a portrait, or `i`/`v`/
`esc` — and then using its bar. Not a defect against the clause as routed
(all seven slots ARE reachable), but `PT-1249` calls the bar *"persistent
furniture on every in-game screen"* and the board is the screen a player is on
most.

### ⚠ A stale comment, eight lines above the one that corrects it

`play_screen.dart:1352-1354` still reads:

```dart
/// ⚠ THREE OF THE SEVEN ARE NOT BUILT and say so rather than ignoring the
/// tap — `PT-1380`. Party and Journal have no screen at all;
```

and `:1361-1363`, inside the same widget, reads *"ALL SEVEN ARE BUILT NOW —
`PT-2533`"*. The second is right.

## 2. Party selection

### Portraits — confirmed, square, and with room

Measured off the render:

| | box | shape test | verdict |
|---|---|---|---|
| Party Selection | **120 × 120** | top row 89 wide vs middle 120 | rounded square, r ≈ 15 |
| Party sidebar | **48 × 48** | top row 32 wide vs middle 48 | rounded square, r ≈ 8 |

A circle's topmost row would be one to three pixels wide. Neither is a circle,
so `PT-2535`/`PT-2536` both landed and the two surfaces now agree.

**The row has real clearance.** Row boxes measured `y 224-372`, `387-536`,
`550-699` — **149 to 150 tall** around a 120 portrait, so 15px above and below.
Not cramped. Portrait fill `(10,34,26)` inside border `(204,204,178)`.

### A full party blocks an add and never a remove — confirmed by doing it

Ten companions on the roster, three fielded (`companionCap()` is 3).

```
before   PARTY IS FULL — 3 of 3        (amber)
         Second Guard / Bruiser / Guard   IN FIELD, REMOVE live
         the other seven                  ADD dim + "the party is full —
                                          send somebody home first"

REMOVE on Second Guard, from the full party — it worked

after    1 of 3 slots available        (no longer amber)
         every ADD bright, every refusal line gone
```

So the refusal is real, it is stated on the row rather than dropped, and it
lifts the moment a slot frees. The remove was taken **while the party was
full**, which is the half of the clause that the obvious implementation breaks.

### Scrolling — confirmed

Ten rows in a panel that holds three and a half. The scrollbar thumb measures
**x 1744-1751, y 223-431** (209px in a ~590 track) at RGB `(92,86,68)` —
`C.textLabel`, the colour `PT-2535` changed it to, and visible against the
panel. Six wheel notches moved it to `y 565-775` and brought
`dr-bare.pc`, `dr-battle.pc`, `dr-remote.pc`, `dr-x.pc` into view.

### ✗ A dismissed companion is listed by its raw tag

Not a fixture artefact — **the same row changed within the test**:

```
dismissed, still in the room     Second Guard      ← name intact
quit and Continue                ally.pc           ← the tag
re-added, then reloaded again    Second Guard      ← name back
```

`play_screen.dart:1680` reads `_nameOf[r.tag] ?? _thingNameFor(r.tag) ?? r.tag`.
`_nameOf` is **cleared and rebuilt from the room's placements on every load**
(`:3562`), and `_thingNameFor` (`:1639`) reads the sidebar — the fielded party.
A companion who is neither placed nor fielded has no name source and falls to
the tag.

That is the exact state the screen exists for: `rosterIn`'s own comment says it
remembers a dismissed companion *"precisely so they can be offered back"*, and
`RosterEntry.from` carries the blueprint path — `characters/ally`, the file
whose `name` is "Second Guard" — which nothing on this path reads.

All seven of my dismissed companions showed as `frail.pc`, `dr-assas.pc`,
`dr-astro.pc`, `dr-bare.pc`, `dr-battle.pc`, `dr-remote.pc`, `dr-x.pc`.

### ✗ A re-added companion is a phantom until the next room load

Tapping ADD on the dismissed `ally.pc`:

```
sidebar        ally.pc
               in the fight, and the round does not hol…
               0 of 0
Party row      ally.pc   IN FIELD   REMOVE dimmed
               down — not until this fight is over
count          PARTY IS FULL — 3 of 3
```

**No fight was running** — the board's verb line was the exploration one and
the status line read `nothing is threatening you`. The subtitle is
`party_sidebar.dart:600`'s `if (!row.present)`: they are in the party and not
on the board, because the room was loaded before they rejoined and nothing
places them after. 0 of 0 then makes `_isDown` true, so
`play_screen.dart:1688` refuses the remove, and the slot cannot be freed.

⚠ **Scoped: it is transient.** A reload places them and they come back at
400 of 400, correctly named. So it is one room's worth of a consumed slot and
a companion who is in the party but nowhere, not a permanent lock — but ADD on
this screen is the one control that reaches it.

## 3. Journal — confirmed, and the sorts are genuinely four

Coder's `quest-bed` is a good bed and I used it as built. **⚠ I dropped one
flag** (`cache.found`) so four quests are active at once rather than three —
with three, the name and planet orders coincide and a planet button that fell
through to name would have passed.

All four orders differ from each other:

| sort | order | key shown on the row |
|---|---|---|
| **time** | Debt · Echo · Cache · Alibi | — (log order) |
| **name** | Debt · Alibi · Cache · Echo | — |
| **priority** | Alibi · Echo · Cache · Debt | highest · high · medium · lowest |
| **planet** | Debt · Cache · Alibi · Echo | Nar Shaddaa · Onderon · Onderon · **no world** |

Every key is annotated on the row, so a reader can see what it sorted by.
**The planetless quest sorts last**, not first. **The two Onderon quests
tie-break by first-reached** (Cache's flag preceded Alibi's) — the documented
stable-on-`firstAt` behaviour, visible because they tie.

**Entries accumulate.** `A Doctor's Alibi` showed both reached lines in
declaration order and neither of its two unreached `end` lines.

**Completed is its own list.** With `cache.found` set, `The Hidden Cache` left
Active and appeared under Completed — an `end` entry finishing a quest with no
`quest.concluded` event.

**✗ Nothing unreached appeared.** `an-unreached-quest` — shipped by the package,
never flagged — is absent from all four sorts and from both tabs. Coder built
that control in deliberately and it holds.

**The empty state names the reason**, on a package with no quests at all:
`no quests underway — one begins when something in the world starts it`.

## 4. Messages

### The four panes — confirmed

`FILTER │ FEEDBACK DIALOG COMBAT EFFECTS`. ⚠ The labels are **FEEDBACK** and
**DIALOG**, not "Messages" and "Dialogue"; the screen's own title is MESSAGES.
All four switch and each draws its own body — FEEDBACK carried real lines,
DIALOG and COMBAT read `nothing here yet`, EFFECTS draws two headed columns.

### Two columns — confirmed

`GOOD EFFECTS` at the left edge and `BAD EFFECTS` at x ≈ 660 of the panel, same
row. Not a stacked list.

### ✗✗ BUT SIXTEEN OF TWENTY-ONE CONDITIONS ARE FILED AS *GOOD*

⚠ **The routed premise is wrong on this build.** *"Good Effects will
legitimately be empty"* is not what happens: it fills with penalties.

A matched pair, on the same bench, same character, same mechanism — a
`does = "condition"` hazard with `dc = 99` and `rounds = 30`, one square from
the spawn. The only thing that differs is the condition's **name**:

| board | landed | column |
|---|---|---|
| `a0334` | `shaken for 30 rounds` | **GOOD EFFECTS** — "shaken — 30 round(s) left" |
| `a0330` | `slowed for 30 rounds` | **BAD EFFECTS** — "slowed — 30 round(s) left" |

`play_screen.dart:_activeEffects`:

```dart
final bad = <String>{};
for (final p in widget.powers) {
  final c = p.condition;
  if (c != null && p.affects == 'enemy') bad.add(c);
}
… bad.contains(c.name) ? EffectSide.bad : EffectSide.good
```

**The `bad` set is built from the Force-powers roster and nothing else**, and
the fall-through side is `good`. Across all 106 rows of `powers.toml` only five
conditions are named by an enemy-affecting power — `blinded`, `cowering`,
`held`, `slowed`, `stunned`. `conditionNames` in `conditions.dart:36` has
**21**. So sixteen are shown to the player as beneficial:

```
shaken  panicked  sickened  nauseated  fatigued  exhausted  dazed
prone   flat-footed  deafened  entangled  grappled  helpless
staggered  disabled  paralysed
```

A condition from a hazard, a weapon's on-hit property or an item can never be
in that set, because only powers are read. `paralysed` and `helpless` read as
good news.

⚠ The comment above the function says the empty good column *"is a finding and
not a bug"* because all 19 condition-applying POWERS are `affects = "enemy"`.
That is true of powers and is the wrong question: the classifier is asked about
every condition, from every source.

### ⚠ `character.levelled` reads as a level that is waiting

`play_screen.dart:1618-1620` renders `CharacterEventKind.levelled` as
`A level is waiting — N.` — but that event records a level **taken**
(`_classesNow` adds a class level per event, `_levelsTakenThisSession` counts
them). A level-6 character with nothing pending shows five of them:

```
A level is waiting — 2.
A level is waiting — 3.
A level is waiting — 4.
A level is waiting — 5.
A level is waiting — 6.
```

`_hasLevelWaiting` correctly said no level was waiting at the same moment — the
sheet and the portrait default both agreed. It is the sentence, not the state.

## 5. Notes

### ✗ A note cannot be written

The field takes no input. Tried, on a freshly opened screen each time:

```
click in the field, settle 2s, type      nothing
click exactly on the existing text, type nothing
Tab, then type                           nothing
open the screen and type immediately     nothing
ctrl+a then BackSpace                    nothing — not even a deletion
```

The source says why. `notes_screen.dart:107` is a raw **`EditableText`**, not a
`TextField`:

```dart
child: EditableText(
  key: const ValueKey('notes-field'),
  controller: _c,
  focusNode: _focus,
```

`requestFocus` appears **zero times** in the file, there is no `autofocus`, and
the only `GestureDetector` in it (`:152`) is the SAVE/◂ JOURNAL button builder.
A bare `EditableText` does not take focus from a tap — that behaviour is what
`TextField`'s selection gesture detector adds. Nothing can ever focus it.

⚠ **Two characters did land, once.** On my very first attempt the note came out
as `Y9` — characters 12 and 13 of what I typed — and I could not reproduce it
in six later attempts by any route. I cannot explain it and I am not going to
invent a reason; the reproducible state is that the field is dead.

### The privacy guarantee — confirmed three ways, and it holds

Verified against the two-character note that did land, so this is a real
`note.written` and not an absent one.

**The text is not in the save.** Decoded `t129-quest.sav`:

```
{"kind":"note.written","payload":{"chars":2}}
```

and searching the whole decompressed body for the note's own text — `Y9` —
and for every string I attempted to type returns **nothing**. The event proves
the path ran; the absence proves it carried no text.

**A package cannot write into it.** Run against the real parser
(`openConversation`), not a reimplementation:

```
effect kind = "note.written"   ✗ effectNamesEngineKind
                                 "`note.written` is written by the engine,
                                  never by an author (§5)."
link gate  { note = "doctor" }  ✗ unknownGateKey
                                 "`note` is not a gate term. The grammar is
                                  closed (§4) — the terms are alignment,
                                  all_of, any_of, attitude, background, dc,
                                  flag, not, opposed, opposed_by, party,
                                  payment, quest, skill, species, status."
link gate  { flag = "alibi.riiken" }   ✓ loads      ← the control
```

The control matters: without it the refusal could have been about the link
shape rather than the term.

⚠ **And one way I nearly broke it by accident.** My first probe wrote the gate
as `[npc.reply.gate]` — a table `_gate` is never reached from — and the file
**loaded silently**. A gate in a place the parser does not read is ignored, not
refused. That is not the privacy hole it looked like, but a gate authored in
the wrong table does nothing and says nothing.

## 6. Options

### Escape — confirmed from the board, and it is a chain

Measured pre and post on each screen:

| what is open | Escape |
|---|---|
| the board | **opens OPTIONS** ✓ |
| Equip | closes it to the board ✓ |
| Inventory | closes it to the board ✓ |
| **Journal** | **nothing** ✗ |
| **Messages** | **nothing** ✗ |
| **Notes** | **nothing** ✗ |
| **Party Selection** | **nothing** ✗ |

The chain at `play_screen.dart:13931` closes `_sheet`, `_bag`, `_equip`,
`_abilities`, `_settings`, `_map` in that order and only then falls through to
the board handler that opens Options — correct, and `PT-2465` says so.
**`_journal`, `_messages`, `_notes` and `_party` are not in it**, and they also
do not reach the board handler, so Escape is inert on the four newest screens.
The chain's own closing comment is the standard it misses: *"a new overlay that
sat outside it would let `esc` leave the board with a full-screen panel still
drawn over it."*

### The nine reasons — confirmed, and the three you named are correct

```
SAVE GAME     write the session to disk
              not built yet — the save format and its list exist,
              this door into them does not
LOAD GAME     open a saved session
              not built yet — Load Game is on the package menu today, not here
ACCOUNT       sign-in, friends, sync
              not built yet — there are no accounts to sign in to,
              so there is nothing here to configure
```

None of the three cites `PT-1140`/`PT-1148`. The other six —
TABLE RULES, TURN PACING, DISPLAY, ROLLS & FEEDBACK, SOUND, SESSION — all do,
and all six are settings whose scope those rulings govern. Both halves read.

### LEAVE SESSION — confirmed

`end this session and return to the package menu`, a red confirm, and clicking
it returned me to the package menu with `reading saves…` running. It is the one
entry with no "not built" line.

## 7. The portrait default — confirmed

| state | secondary tap opens |
|---|---|
| no level waiting | **EQUIP** (`body` · `clothing (Equipped)`) |
| level waiting (`t123-unspent`, xp 80000 at level 12) | **the Character Sheet**, with `Auto Level Up` and `Level Up` |

**Primary selects.** Primary-tapping the same portrait put `Whisper selected`
on the status line and opened nothing.

⚠ **The big circle on the sheet is not a portrait.** It measures as a true
circle — width 66 → 131 → 78 down its height — and it is
`character_screen.dart:558`'s `shape: BoxShape.circle`, the **model viewport**
`PT-1249` describes as *"overlaid on the model itself"*. The sheet's actual
portrait is the 22-unit header chip beside the name, and `:416` gives it
`BorderRadius.circular(M.radiusCell * s)` — a rounded square, the same
treatment as the other two. **All three portraits agree.** Only the comment
above it (`:408-410`, *"currently: a filled circle"*) has not caught up.

## Fixtures

`mk129.py`, two beds:

* **`party`** — `tester-mind` on `m01-guard`, ten companions off ten
  distinctly-named blueprints with three fielded. Ten rows is more than the
  panel holds and three is `cap`, so the scrollbar and the full-party refusal
  are both live, and REMOVE on the three is the clause's other half.
* **`quest`** / **`quest4`** — `quest-bed`, flags ordered so the four sorts
  give four different orders. `quest4` drops `cache.found` to keep four quests
  active; with three, name and planet coincide.

`mk112.py shaken` and `mk112.py slowed` — Coder's condition benches, used
unchanged. Each puts one unavoidable hazard one square from the spawn, which is
a matched pair by construction: same mechanism, different condition name.

`probe/note_effect.dlg`, `probe/note_gate.dlg`, `probe/flag_gate.dlg` and
`tool/probe_notes.dart` — run against `openConversation` itself.

⚠ **One note on my own method.** I overwrote two screenshots by reusing
`s0`/`s1` across runs and briefly mis-read one of them as evidence about a
screen it was not. Everything above was re-taken under unique names.
