# 001 · Saves, and the package they belong to — REPORT

**From `Tester`. Answers `requests/001`.** Walked on the real machine, real
folder, real display (`:0`), on a **rebuilt** app binary — see ⚠ below.

Tested against `Lodestar f7fe50d · Lens 04e4061 · Loom b2308e1 · app 3d97d52`.

---

## ⚠ READ THIS FIRST — the binary on disk was STALE and would have faked a pass

`run-app.sh` only builds when the binary is **missing**:

    [ -x build/.../kotor_rpg_app ] || flutter build linux --debug

The bundled binary was `21:31`. `lib/chargen/hub.dart` was `22:10` and
`lib/saves/save_store.dart` was `22:11` — **the two files carrying `PT-1445`
and `PT-1443`'s save work.** Following the request literally (`./run-app.sh`)
runs **pre-fix code**, and every claim below would have been tested against the
wrong build.

**I rebuilt before testing.** Everything in this report is against a binary
built from `3d97d52`.

**This is not a claim failure — it is a hazard in the runner**, and it will
recur on the next slice.

---

## Numbered against your claims

| # | claim | verdict |
|---|---|---|
| 1 | Each package offers only its own saves | ✓ **TRUE — attacked hardest, held** |
| 2 | `base-rules` offers no New Game/Continue/Load, and says why | ✓ **TRUE** |
| 3 | `Continue` on `base-rules` does not red-screen | ✓ **TRUE** |
| 4 | `Back` from the hub does not drop you into a game | ✓ **TRUE** |
| 5 | Entry screen reads `Select Premade Character` | ✓ **TRUE** |
| 6 | A save survives a full quit — the character, **and the wound** | ⚠ **HALF FALSE** |

### 1 · Cross-package isolation — held under the hardest attack I could build

You asked for this one to be attacked, so I did not test it with two saves. **I
built a third package and got three saves across three packages**, then asked
each package what it had:

| package | saves on disk | offered |
|---|---|---|
| `base-rules` | 3 | **none** ("no saves") |
| `endar-spire` | 3 | **2** — `kaeda-vos.sav`, `vess-taran.sav` |
| `taris-undercity` | 3 | **none** ("no saves") |
| `tester-probe` (mine) | 3 | **1** — `probe-walker.sav` only |

`Load Game` opened in `tester-probe` lists **only** `probe-walker.sav`. Claim 1
survives.

**⚠ But the migration allowance is dead code, and your own comment says how to
check.** `save_store.dart` reads both id and display name, and says: *"WHEN IT
CAN GO: … a save qualifies if its `package` is not an id in the library. Keep
it until someone has checked the folder."* **I checked the folder.** Both
pre-existing saves decompress to `package: "endar-spire"` — the **id**:

    kaeda-vos.sav  → package field: endar-spire
    vess-taran.sav → package field: endar-spire

**No save on this machine exercises the `packageName` branch.** By your own
stated criterion it can go. (`kaeda-vos.sav` is `22:14`, so it already postdates
`PT-1445` — it is not the old-format save it looks like.)

### 6 · The character survives. The wound does not. — ⚠ DEFECT

**Repro, exactly:**

1. `Endar Spire` → `Continue` (Vess Taran, full health, no working line)
2. Walk to `6,3`, press `Down` into the trooper → conversation
3. Choose **"Stand aside."** → fight
4. Press `Down` once. Log: *"…needed 10 — hit · **1 left**"*
5. Walk away (`Left` ×3), `esc` to leave the area — this ends the encounter
6. **Quit the app** (window close), reopen, `Endar Spire` → `Continue`

**Expected per claim 6:** Vess Taran at 1 of 11.
**Actual:** no working line at all — i.e. **full health**. The trooper is
whole again too.

**Mechanism, and it is already written down in the code** —
`play_screen.dart:109`: *"⚠ IN MEMORY FOR THIS SESSION ONLY. Nothing appends it
to the save yet."* The only writer is `onPlay` at the hub. I confirmed it at the
byte level: `vess-taran.sav` stayed `f5e78ff6…`, size 677, mtime `22:44:49`
across the walk, the conversation, the fight and leaving the area.

**So the wound cannot survive a quit, because nothing about play is ever
appended to the save.** The claim overstates what is built. Whether the fix is
the claim or the feature is yours and the owner's — but claim 6 must not stand
as written.

---

## DEFECT

**D1 · The hub tells the player nothing is saved, directly above the button
that saves.** On the hub, with all eight steps done and `Play` unlocked, the
panel reads:

> *"Every step is built, so Play unlocks once all of them are done. It does not
> lead anywhere yet: your character is not written down and nothing is saved."*

Pressing `Play` **does** write the save — I watched `vess-taran.sav` appear.
⚠ **This is the sentence that produced `PT-1443`'s "nothing saves at all".** A
player who reads it and then reports that saving is broken is reading the
screen correctly. Repro: any package, complete all steps, look at the hub before
pressing `Play`.

**D2 · The dialogue screen shows a TAG where a name belongs — and the wrong
tag.** Talking to the trooper, the speaker line reads:

    SITH-TROOPER.COMMAND-DECK.07

The blueprint carries `name = "Sith Trooper"`, which is never consulted.
`dialogue_run.dart:361,393`: `speaker: line.by ?? conversation.owner` — and
`owner` is a tag.

⚠ **And it does not even match the creature you are talking to.** The dialogue
declares `owner = "sith-trooper.command-deck.07"`; the area places the trooper
as `tag = "sith-trooper.command-deck.39"`. The conversation opens anyway, so
`owner` is enforced by nothing. **The player is shown `.07` in conversation and
`.39` two seconds later in the fight log — two different names for one
creature, neither of them its name.**

**D3 · Raw spec text is rendered as a player-facing choice.** At `Equipment`,
the first profession-grant option is labelled:

> **TAKES THE CLASS'S OWN melee UPGRADE FROM §4a —  Soldier → Long Sword +
> Short Sword or a Double-Bladed Sword; Scout → Double-Bladed Sword; Duelist →
> Vibrosword + Vibroblade**

A player sees a section reference and the mappings for two classes they did not
pick. Repro: any Soldier, `Backstory` → `Hunter`, then `Equipment`.

**D4 · Back from `PRE-HUB COMPLETE` silently discards your species.** Press
`Back` on the boundary screen and `SPECIES` reopens with the selection reset to
**Aqualish** (the first row) and `Accept` disabled — the `Human` choice is gone
with no warning. ⚠ **Scoped:** I confirmed **species** is discarded. I could
**not** determine whether **class** is discarded, because `Soldier` is the first
row of the class list and a retained `Soldier` is indistinguishable from a reset
one. To settle it, pick a non-first class and repeat.

**D5 · Two contradictory health numbers on screen during a fight.** Mid-fight
the status bar reads `Vess Taran: 11 of 11` while the line under it reads
`hit · 7 left`. The bar is `projectPlayState` folding the log; the log
deliberately carries no blows (`character.damaged` is transient), so the bar
**cannot** move until `encounter.ended`. Both halves are working as designed —
**the defect is showing them side by side.** They reconcile the moment the
fight ends. ⚠ It fooled me for two screenshots, so it will fool a player.

**D6 · "left you at" is printed for the NPC too.** After the fight:

    sith-trooper.command-deck.39: 14 of 18 — encounter a01-command-deck left you at 14

**D7 · Overlapping text at the foot of the play screen.** The fight-log line and
the `Vess Taran · arrows to move · esc to leave` line are drawn over each other
at 1280×720 — *"…needed 10 — hit · 7 left"* runs underneath *"Vess Taran"*.
Legible only because both are dim. See capture `46-fighting`.

**D8 · Loom: the entry-area chooser sits below the fold with no cue.** In
`PACKAGE PROPERTIES` at the default window size, the section renders as the
heading *entry area*, the hint *where a new game begins*, and then nothing —
`Cancel`/`Save` follow. The radio list **and** the warning *"Nothing is set, so
a new game has nowhere to begin"* are reachable only by scrolling, and there is
no scrollbar or affordance. `Save` is enabled without it.
⚠ **This is `BUILD 34`'s rule again** — *anything you can click must be laid out
where it can be seen* — a fourth instance. Repro: new package, add one area,
open properties at 1280×720.

---

## UNDECIDED — for the owner, not for `Coder`

**U1 · A character at negative vitality walks around normally.** I lost the
fight and dropped to **-5 of 11**. The screen printed `-5 of 11`, kept the
normal marker, kept offering *arrows to move*, and **I moved** (6,3 → 4,3). No
death, no down state, nothing said. `STATE.md` already flags *`down → dead` in
one blow* as the last unmade ruling; **this is what it looks like from the
chair.** Filing as the question, not the bug.

**U2 · Droid-only feats are offered to an organic, and the format cannot say
otherwise.** As a **Human** Soldier the `Feats` step offered `Droid Upgrade 1`,
whose own description reads *"**An organic cannot hold it.**"* (citing
`PT-583`), and `Droid Interface`, `Droid Upgrade 4`, `Emergency Reboot`.

⚠ **This is a missing format, not a screen bug.** A feat record carries only
`id · name · chain · is_chain_head · section · availability · effect ·
description · level` — **there is no field for who may take a feat.** Two feats
state the restriction in prose only, both `availability = "selectable"`:

    Plating Proficiency: Light   selectable
    Droid Upgrade 1              selectable

`STATE.md` lists *feat prerequisites* among the three rules that cannot be
checked; **this is the same hole seen from the offer side rather than the
validation side.** Nothing can enforce it until the format carries it.

**U3 · A package gets `base-rules` without declaring it.** `tester-probe` has
`[requires] packages = []` and full chargen — 271 worlds, every class — because
`ChargenSource.load(where)` reads the shelf, not the opened package. Legitimate
for now; worth a ruling before a second rules package exists.

---

## AS DESIGNED — looked wrong, is not. Filed because it fooled me.

**A1 · "271 worlds" against `STATE.md`'s "301 worlds".** Not a mismatch:
`worlds.toml` holds 301 rows and exactly **271** are `menu_status = "complete"`
(13 unfinished, 12 none, 5 ineligible). The screen offers the complete ones.
Both numbers are right and they count different things.

**A2 · The library row looks clipped at four packages.** The fourth card is cut
at the right edge and the import `+` tile is pushed off-screen — **but the row
scrolls horizontally** and the card is fully reachable. `Import` also has a
button top-right. **Not a defect.** I nearly filed it.

**A3 · Continue lands you at the entry area, not where you stood.** Exactly as
your *undecided* section says. Noting only that it is confirmed.

**A4 · Standing on the `aft` green square does nothing.** It is an **arrival
point**, not the door; the door is the amber marker at `7,2`. Correct, and I
misread it for a minute.

---

## ⚠ Scoped negatives — what I checked, and where

**Suites: I did not run any.** You said 591 green and hermetic; I took it.
**But I did verify the hermetic claim as a side-effect** — while another
process was running `flutter test` in `Loom`, I md5'd all 34 files under
`~/.local/share/kotor-rpg/` before and after: **byte-identical.** Your `BUILD 39`
sandbox holds, measured rather than assumed.

**No existing package was damaged.** `base-rules`, `endar-spire` and
`taris-undercity` are md5-identical to a baseline I took at `22:29` before
touching anything.

**No exceptions.** I grepped all four run logs for
`exception|error|overflow|assert|failed|RenderFlex`. The only hits are two
GTK/GDK teardown warnings at `22:50:13`, which is the instant I closed the
window. **No Dart exception and no RenderFlex overflow anywhere in the session.**

### What I did NOT check

- **Steps 3 and 5 of your journey as written.** I never made a character in
  `Taris Undercity`. I attacked claim 1 with a **fourth** package instead
  (three packages holding saves rather than two). `Taris Undercity` was checked
  only in the "no saves" direction.
- **`Load Game` distinguishability with two saves in one package** — your
  second stated gap. `endar-spire` has two and they list as `kaeda-vos.sav` /
  `vess-taran.sav`, which **are** distinguishable — but only because the file
  is named for the character. **I did not test two characters with the same
  name**, which is where `one file per character per campaign` would collide.
- **The `[Bribe · 50 credits]` path, the typed "say something…" box, and the
  other five dialogue options.** I took `Stand aside.` only.
- **`Movies`, `Music`, `Options`, `Characters`, `Profile`, `Import`.**
- **A droid character.** Organic only, so the whole droid chargen branch —
  chassis, model, droid skills — is untested by me.
- **Any window size other than 1280×720.** D7 and D8 are size-sensitive and I
  cannot say how they behave elsewhere.
- **Loom beyond package/area/properties.** I did not paint a tile, place a
  creature, or use the conversation or doctrine editors.

---

## What I tried that found nothing

- **Pressing disabled `Continue` on `base-rules` by mouse AND by keyboard**
  (`Return` with focus defaulted to `Continue`). No red screen, no state
  change, nothing in the log. Claim 3 is solid from both input paths.
- **Walking the two-area round trip twice** — `aft` → door at `7,2` →
  `Starboard Hold` *"arrived at north"* → back → *"arrived at aft"*. The board
  re-fits from 12×8 to 10×6 and back. Clean.
- **A one-area package with no arrivals at all** (`tester-probe`). The player
  spawns at `0,0` and walks. No crash, no empty-list failure.
- **Scrolling the library row** — reachable, see A2.

---

## ⚠ Data safety — what I left in the owner's real folder

I used the real folder as instructed, so these are real. **I deleted nothing
and I fixed nothing.**

| added | what |
|---|---|
| `saves/vess-taran.sav` | Human Soldier, `Endar Spire`, `22:44` |
| `saves/probe-walker.sav` | Human Soldier, `Tester Probe`, `23:01` |
| `packages/tester-probe/` | **a package I made in Loom**, 2 files, `22:54` |

**`tester-probe` is mine, not the owner's** — a 6×5 room called `Probe Room`,
made only to test the Loom→app seam. **Delete it and both `.sav` files to
reset.** I left them because deleting from the live shelf is not my call.

---

## The two-program seam — it works, live

Authored in Loom → appeared in the app **without restarting it**:

`New package` *Tester Probe* (id auto-derives to `tester-probe`) → `New area`
*Probe Room* 6×5 (file auto-derives to `a01-probe-room`) → properties: authors,
summary, entry area → `Save`. Written to
`~/.local/share/kotor-rpg/packages/tester-probe/` as two TOML files.

In the already-running app: `esc` → `Exit to Library` → **"4 packages
installed"**, *Tester Probe* on the shelf with its summary and author. Opened
it, `New Game` **live** (it has an entry), ran all nine steps, pressed `Play` —
and stood in the 6×5 room I had drawn, `Probe Room`, `a01-probe-room · 1, 1`.

Loom's `VERIFY` also earned its keep: on creation it said *"The manifest
declares no authors and no summary, which `PACKAGE-FORMAT-01 §4·1` requires"*
and named where to fix it, and the tree said *"no entry area — a new game
cannot begin"* until I set one.

---

## On your three stated gaps

**"Does a disabled `Continue` read as 'not yet' or as 'broken'?"** — **Not
yet.** The line *"this package declares no [entry] area — it supplies rules,
not a place to play"* lands. Three greyed rows with no explanation would read as
broken; with that line it reads as a deliberate kind of package. ⚠ **The one
thing missing is that it names a TOML section (`[entry]`) at a player.**

**"Are two saves distinguishable?"** — In this folder yes, but **only because
the filename is the character's name**. The panel shows `kaeda-vos.sav` and
`rules 0.1.0` — no time, no character, no package, and the `.sav` extension is
shown to the player. `PT-1443`'s *"these two saves look identical"* would
return the moment two characters share a name.

**"Does `Back` feel like back?"** — Yes. It goes to `PRE-HUB COMPLETE`, which
is visibly the screen you came from. **The surprise is not where it goes, it is
D4** — that it throws your species away when it gets there.
