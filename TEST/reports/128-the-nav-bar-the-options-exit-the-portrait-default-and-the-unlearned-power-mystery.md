# TEST 128 — the nav bar, the Options exit, the portrait default, and the unlearned-power mystery

**Build.** App **`a9438a7`** ("The shared nav bar, and the exit moves onto the
Options list — PT-2525"), tree clean, built from `git archive` of that sha.
The committed lock resolves Lodestar **`46f0fcea`**, and that is the
pub-cache checkout `package_config.json` compiles against. `check_shelf.py`
clean: 29 rules files and 65 standard blueprints.

**Verdict.** Items 2 and 3 confirmed in full. Item 1's position clause
holds; **its refusal clause fails** — Party and Journal drop the tap
silently. And **item 4 is not a defect**: the record does carry its powers,
and the screenshot is the same misreading I made myself in TEST 127.

---

## 1. The nav bar

### Same position on every screen — confirmed

Measured, not eyeballed. The nav strip's bounding box on each screen:

```
EQU   x 1245–1643   y 85–137
INV   x 1258–1643   y 85–137
CHR   x 1258–1643   y 85–137
ABL   x 1258–1643   y 85–137
OPT   x 1258–1659   y 85–137
```

Identical y band and right edge throughout. The small left/right variation
is the *lit* slot's fill being brighter than the unlit borders, not the bar
moving — the seven slots sit at the same x on all five.

### ✗ Party and Journal drop the tap silently

The refusal sentences exist. `play_screen.dart:1351–1353`:

```dart
NavScreen.party   => 'the Party screen is not built yet',
NavScreen.journal => 'the Journal is not built yet',
```

But `nav_bar.dart`'s `_cell` never shows them:

```dart
onTap: why == null ? () => onGo(s) : null,
```

An unavailable slot gets a **null** tap handler, and `why` is used only to
pick a dimmer border colour. Tapping PTY or JRN produced no change and no
message anywhere on screen — I checked the status line, the panel body and
the whole frame.

So they are **not silently absent** — both slots are drawn, visibly dimmer
than the other five — but the tap is silent and the reason never reaches
the player. The field's own comment three lines above is the standard it
fails: *"a disabled row with no reason is a bug a player cannot distinguish
from one."*

⚠ Scope: the strings are built and passed in correctly. This is one missing
render, not a missing decision.

## 2. Escape and Options — confirmed

**The status line reads `esc options`**, replacing `esc to leave`:

```
Whisper   arrows to move · m map · i carrying · esc options
```

**Escape opens OPTIONS**, ten entries: SAVE GAME, LOAD GAME, TABLE RULES,
TURN PACING, DISPLAY, ROLLS & FEEDBACK, SOUND, SESSION, ACCOUNT, LEAVE
SESSION.

**LEAVE SESSION genuinely leaves.** It is the one entry with no "not built"
line — it carries *"end this session and return to the package menu"* and a
red confirm button, and clicking that returned me to the package menu
(Continue / New Game / Load Game / Movies / Music).

**The other nine do nothing, each with a stated reason.** Each has its own
subtitle — *"write the session to disk"*, *"open a saved session"*,
*"difficulty, death handling, rest pacing — a GM's calls, campaign-scoped"*,
*"the bottom is a waiting table, not a distracted player"*, *"theme, text
size, motion — nothing 3D to configure"*, *"a tabletop app should be able to
show its working"*, *"volume and mix"*, *"who is here, and whether it is
publicly listed"*, *"sign-in, friends, sync"*.

⚠ **But the reason beneath them is one shared sentence, word for word:**

```
not built yet — PT-1140 and PT-1148 hold which settings are universal,
per-campaign or per-session, and this screen does not guess
```

For TABLE RULES, TURN PACING, DISPLAY and SOUND that is exactly right. For
**SAVE GAME**, **LOAD GAME** and **ACCOUNT** it is not — writing a session
to disk and signing in are not settings whose scope those two rulings
govern. The clause passes as routed; the reason is generic where three of
the nine need their own.

## 3. The portrait default — confirmed

| character state | secondary-tap opens |
|---|---|
| no level waiting | **EQUIP** (`head` · `mask (Equipped)`) |
| level-up pending (`unspent`) | **the Character Sheet** (`Whisper · Jedi Consular · level 12`) |

Both branches, exactly as `_openPortrait` describes them.

⚠ **"Tapping" is the SECONDARY tap**, and it is worth writing down because I
got it wrong first. A primary tap *selects* — the status line reads
`Whisper selected` and the card lights gold. `party_sidebar.dart:404` wires
`onTap` to `onSelect` and `:408` wires `onSecondaryTap` to `onOpen`. Both
behaviours are right; anyone testing the clause with a left click will
conclude it fails.

**A companion shows their own state, never the player's.** Secondary-tapping
the companion's portrait:

```
EQUIP · implant
no equipment is recorded for Second Guard — a companion is a blueprint in
the roster and carries none
you are carrying nothing for this slot
```

All twelve lattice cells empty, and **none of the player's four worn items**
(mask, clothing, belt, blaster-pistol) appears anywhere on it. A real empty
state that names the companion.

## 4. The mystery — it is not a defect, and I made the same mistake

**The screenshot is consistent with a correct build.** The arithmetic:

* The Powers grid renders **all 106 shelf powers**, by `PT-1250`'s rule that
  *"an unlearned power is present and anonymous"*.
* An unlearned power renders as `?` in the tile, `UNKNOWN FORCE POWER` in
  the title and `--` in all three cost rows — deliberately.
  `abilities_screen.dart:534` documents it, `:542` implements
  `p.known ? p.name : 'UNKNOWN FORCE POWER'`, `:604` dashes the costs on
  the same condition.
* **Whisper knows four powers.** So **102 of the 106 tiles correctly show
  `?`**, and the four learned ones sit at shelf indices 31, 32, 35 and 46 —
  scattered across two rows in the middle of the grid.

A screenshot of that reads as *"every power is unlearned"* to anyone not
counting. **That is precisely the misreading I filed in TEST 127 and
retracted in TEST 127's amendment** — I sampled three tiles, all of them
among the 102, and concluded the screen was broken.

**And the record does carry the events.** Decoded from every save I hold:

| save | character | `character.power-taken` |
|---|---|---|
| t119-wipe | Whisper | **4** |
| t123-bare | Whisper | **4** |
| t124-equip | Whisper | **5** |
| t113-sphere | Bench Caster | 9 |
| t115-deflectonly | Bench Caster | 1 |
| t118-a | Pilgrim | 4 |
| t111-f, t112-shaken, t116-sonicmine | other benches | 0 |

The three zero-power saves are `Fitting Room Volunteer` (level 1),
`Bench Scout` (level 6) and `Rocketeer` (level 10) — none of them is
Whisper, none is level 12, none has force 159.

**Positively verified on this build family**, which is the control the
TEST 127 version lacked:

```
Force Scream        known, priced     "Force Scream"         8 · 0 · 8
Crush Opposition II known, unpriced   "Crush Opposition II"  -- · -- · --
any of the other 102                  UNKNOWN FORCE POWER    -- · -- · --
```

### What I cannot reconcile, stated plainly

Coder reports the record *"genuinely carries no powerTaken events"*. **That
is not true of any Whisper save I currently hold** — all three carry four or
five. Either a different record was inspected, or one of mine was read at a
moment my generator had rewritten it (`mk119`/`mk123`/`mk124` delete and
recreate their saves on every run, so a save inspected an hour apart is not
the same file).

**The discriminator, if the screenshot is still to hand:** the four learned
powers are the tiles with **no `?` in them**. If the grid in the screenshot
has four blank tiles among the 106, it is one of my saves and the behaviour
is correct. If every single tile carries a `?`, it is a record with no
powers and not one of mine.

⚠ And one honest note on my own contribution to this: the reason this
became a mystery at all is that TEST 127 filed the 102-of-106 case as a
defect. Coder's three guards are real work spent on a report of mine that
was wrong.

## Fixture

`tester-mind`. `mk124.py` now also writes a `party.joined` event —
`ally.pc.01` from `characters/ally` — so the portrait rules and the Equip
screen can be read for somebody who is **not** the player, which is the only
way to test the companion clause.
