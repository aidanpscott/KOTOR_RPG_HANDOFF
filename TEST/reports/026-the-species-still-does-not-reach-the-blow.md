# 026 · The species still does not reach the blow — and a shipped conversation names a creature that is not there

**From `Tester`. Unrequested number.** `PT-1512` followed: packages, saves and
console backed up before anything was touched.

**Built and tested against:**

    Lodestar 61e2849 · Lens 6b55219 · Loom cf4f5ad · app f453601

**⚠⚠ CONTAMINATION DECLARED, TWICE, AND IT MATTERS FOR EVERY CLAIM BELOW.**

- **08:10** — I found `Loom` **dirty**, five files touched between 08:05 and
  08:10, a conversation wizard being written that minute. **I did not build it**;
  I ran the app instead and came back.
- **08:44** — `Loom` was clean at `cf4f5ad`, three slices further on than the
  brief describes. **That is what I built and used.**
- **09:1x** — while I was finishing, the tree moved again. At the time of
  writing HEAD is **Lodestar `8534402` · Loom `d0f2b87` (12 dirty) · app
  `2c298f8`**.

> **⚠ So every finding here is against `app f453601` and `Loom cf4f5ad`. If a
> fix landed in `2c298f8` or `d0f2b87` this morning, I have not seen it.**

1280×720 throughout.

---

# ⚠⚠ 1 · `PT-1533` HAS NOT LANDED IN PLAY. The fix is in the binary and the map it needs is empty

**You asked me to swing the vibroblade again and said the number should be +4.
It is +2. It is the same number `025` filed.**

## The proof, and it is stronger than `025`'s

Built the same character: **Gamorrean Duelist, `Grukk Ironjaw`**.

    bought STR 14   species +4   →  sheet says STR 18   →  modifier should be +4
    bought DEX 14   species −2   →  sheet says DEX 12   →  modifier should be +1

**Four strike lines and two defence lines, fresh chargen and reloaded save:**

    Vibroblade · rolled 18 — d20 16 + attack 0 + Strength 2 · needed 13 — hit
    Vibroblade · rolled 19 — d20 17 + attack 0 + Strength 2 · needed 13 — hit
    Vibroblade · rolled 16 — d20 14 + attack 0 + Strength 2 · needed 13 — hit
    defence base 10 + Dexterity 2 = 12
    defence base 10 + Dexterity 2 = 12          ⚠ on a LOADED save

> **⚠⚠ TWO ABILITIES WHOSE ADJUSTED MODIFIERS DIFFER (+4 and +1) BOTH RENDER AS
> +2 — WHICH IS THEIR SHARED BOUGHT VALUE OF 14.**

**That is the proof and it is not a coincidence.** `025` had one number; this has
two that must differ and do not.

## ⚠ It is not the record, and it is not the fix

**The record is correct.** From the save this run wrote —
`grukk-ironjaw.sav`, gzip magic at byte 83, format 02:

    character.species-set   {"id": "gamorrean", "subrace": null, ...}
    character.ability-set   {"ability": "str", "score": 14}

**`CHARACTER-RECORD-01` exactly: the bought score, and a species that is named.**

**The fix is in the binary.** `PT-1533` landed at app `7a2fa73`; I built
`f453601`, six commits later. `_ability()` in `play_screen.dart:1537` reads

    (abilities[key] ?? 10) + (widget.abilityAdjustments[key] ?? 0)

**which is right.** And `main.dart:387` wires `abilityAdjustments` from
`adjustmentsFor(chargen.speciesChoices, character.species)`.

> **⚠ So the READING is that `abilityAdjustments` arrives EMPTY.** Its own doc
> comment says *"Empty for a species with none, and for a screen built without
> chargen data."* **I did not isolate which of `adjustmentsFor`'s two inputs
> fails — that is the fixer's half, not mine.**

## ⚠ And it is on BOTH paths

**Fresh chargen and `Continue` from a save give the same `Dexterity 2`.** It is
not a chargen→play handoff problem.

**⚠ And it is not my package.** `ChargenSource.load()` runs once at app start,
so the species data is global; `tester-probe`'s empty `[requires]` cannot be the
cause.

---

# ⚠⚠ 2 · A SHIPPED CONVERSATION NAMES A CREATURE THAT IS NOT IN THE AREA

**This is the one I would fix first, and it is not in `tester-probe`.**

    endar-spire/dialogue/trooper-challenge.toml   owner = "sith-trooper.command-deck.07"
    endar-spire/areas/a01-command-deck.toml       tag   = "sith-trooper.command-deck.39"
                                                  tag_seq = 39

**`.07` is not in that area. The only creature in it is `.39`.**

`DIALOGUE-FORMAT-01 §1`: *"**`owner` is a placement tag, not a blueprint path** —
`PT-1331`, a tag names ONE placed thing. **It is the default speaker for every
NPC line and the only thing the file says about who you are talking to.**"*

> **⚠⚠ SO THE TROOPER CANNOT TALK, AND
> `RUNNING-ON-THIS-MACHINE.md` LISTS "the trooper talks before it shoots" AS
> WORKING SCAFFOLDING.**

## ⚠⚠ The mechanism, and it is structural rather than a typo

**`tag_seq = 39` is the story.** `PT-1377` made the counter **monotonic** — I
proved it working in `§5` below — so **deleting and re-placing a creature always
gives it a new tag.** The trooper has been re-placed; the conversation still
names the tag it had at the time.

> **A conversation's `owner` is a permanent reference to a thing whose identity
> is designed to change every time an author re-places it. Nothing updates the
> reference and nothing checks it.**

## ⚠⚠ And NOTHING VALIDATES IT — checked, not assumed

**`Lodestar/lib/src/package_validate.dart` — the whole enum, twelve members:**

    blueprintMissing · equipmentMissing · referenceMissing · areaFileMissing
    areaUnreadable · targetAreaUnknown · targetAreaUnreadable
    landingPointUndeclared · duplicateArrivalName · entryUndeclared
    entryAreaUnknown · requiredFieldMissing

**None is about a conversation.** And **`grep owner package_validate.dart`
returns nothing** — the validator never reads the field.

**Loom's `Verify` on `tester-probe` reports 5 problems and names every one; a
dangling conversation owner is not among the classes it can report.**

## ⚠ The failure in play is silent

Walking into the creature **starts a fight**, with no message anywhere that a
conversation was skipped or that its owner did not resolve. Compare the
placement alert, which names tags and reasons in the same bar.

**⚠ Suggested shape, since `§9` and `PT-1331` already decide the hard part:** a
thirteenth member — *a conversation names an owner no area declares* — reported
the way `blueprintMissing` already is, naming the conversation, the tag, and the
area it looked in.

---

# ⚠⚠ 3 · TWO SURFACES DISAGREE ABOUT ONE FILE — 2 against 3

**I hand-added a third unclassifiable placement to `a01-probe-room`:**

    [[contents]]
    tag  = "mystery.probe-room.11"
    from = "widgets/probe-thing"
    at   = [0, 0]

**Loom's `Verify` names all three:**

> *"mystery.probe-room.11" in "a01-probe-room" is placed from
> "widgets/probe-thing", and there is no blueprint there. **It will be drawn and
> will not be present.**"*

**The app's alert bar says two:**

> ⚠ **2 drawn and not present** — probe-sentinel.probe-room.01 — not a creature
> path, expected "characters/…" · probe-warden.probe-room.02 — …

**And the board draws three** — I counted the placeholder rings, and moved the
player off `0,0` to confirm the third is under it.

> **⚠ The two that are named begin `blueprints/characters/`. The one that is not
> begins `widgets/`. The app appears to report only paths it recognises as
> *meant* to be creatures, and to drop a path it cannot classify at all — which
> is the one an author most needs told about.**

**`PT-1553`'s own rule, one layer down:** *a thing you cannot classify must still
be selectable.* **Loom obeys it. The app does not report it.**

---

# 4 · The four rulings that DID land

## ✅ `PT-1540` / `PT-1537` — the turn waits, and I finally saw the pip go grey

**My two-report-old negative closes, and it closes on a frame.**

    before the swing    ◆ 10 move   ● action   ▪ gear      all bright
    swing (arrow into it)
    after the swing     ◆ 10 move   ● action   ▪ gear      ⚠ ACTION GREY
                        "space to end your turn"           the turn is still mine
    space               enemy answers on my key
    new round           ● action bright again

**The control half is what made it observable**: the first fight ended in one
blow and the strip vanished with the encounter, exactly as `BUILD 84` says. The
second enemy survived at 4 of 8 and the grey pip held on screen.

**⚠ And the three pips are three SHAPES** — diamond, circle, square — so the
identity does not rest on colour.

## ✅ `PT-1534` — a zero term is shown when the weapon uses it

    probe-sentinel.probe-room.04: unarmed · rolled 17 — d20 16 + attack 1 + Strength 0

**`Strength 0` is printed** because unarmed uses Strength. Seen on four enemy
lines.

## ✅ `PT-1517` — the reaction pip is absent, not grey

**There is no reaction row at all**, on any of the three fights. Absent, as
ruled.

**⚠ And the same principle shows up in chargen**: at `0 of 30` ability points
**every `+` button vanishes** while the `−` buttons remain.

## ✅ `PT-1550` — a hidden placement, all four halves

Hand-added `hidden = true` to a new placement at `3,4`, and:

- **not drawn** — the square is empty in the app, on a fresh load and after a
  reload
- **holds its square** — walking into it stopped me at `3,3`
- **findable by contact** — *"something was waiting there — probe-warden"*, and
  the token appeared
- **the hand edit survived** — Loom read it, and see `§5`

**⚠ Two things worth deciding rather than defects:**

1. **The reveal does not persist.** Reload and it is hidden again. `PT-1550`
   says *not a perception system*, so this may be right — but it means a player
   who finds it, leaves and returns finds it again.
2. **The message names the BLUEPRINT** (`probe-warden`) where the placement
   alert in the same bar names **tags** (`probe-warden.probe-room.02`). Two
   identities, one bar.

---

# 5 · The Loom rebuild — used, and it holds

**Slices one to three, `cf4f5ad`.** The brief described slice one; three had
shipped by the time I built.

## ✅ The tree agrees with the board, and it agreed every time

- Selecting a tree row **highlights the token** and **opens a property sheet**.
- Placing a creature **appended a row, selected it, highlighted the board square
  and named it in the sheet — all at once.**
- Deleting it **removed the row, cleared the board and closed the sheet.**

**⚠ "Does a tag you just made appear where you are looking?" — yes.** It appears
in the tree, auto-selected, in **file order** at the end of its group, which is
`BUILD 85`'s reasoning working as intended.

## ✅ The `⚠ unknown kind` group works and is the sharpest thing in the slice

All three unclassifiable placements are grouped, drawn in alert, and
**selectable** — including the one the app does not report (`§3`).

## ✅ `PT-1493`'s writer bug is fixed

A placement Loom wrote reads `from = "characters/probe-sentinel"` — **the
correct prefix.** My old finding is closed.

## ✅⚠ `PT-1377` PROVEN END TO END — a retired tag is retired forever

    placed          tag_seq 11 → 12    probe-sentinel.probe-room.12
    deleted         tag_seq stays 12   the entry is gone
    placed again    tag_seq 12 → 13    probe-sentinel.probe-room.13   ⚠ NOT .12

**The defect I escalated at `PT-1377` is closed and I have now watched it not
happen.**

## ✅⚠ The placement writer is byte-faithful, which is what `BUILD 83` was worried about

`BUILD 83`: *"The moment that changes is the moment Loom gains an edit-in-place
path."* **It has, and it is careful.** Toggling `hidden` off produced:

    @@ -58,7 +58,6 @@
     tag    = "probe-warden.probe-room.10"
     from   = "characters/probe-warden"
     at     = [3, 4]
    -hidden = true

**One line. My hand-written column alignment survived, the `mystery` entry below
it survived, and toggling back on returned the file BYTE-IDENTICAL.**

---

# ⚠⚠ 6 · THE CONTROL MOVES 24 PIXELS WHEN YOU USE IT — `PT-1439` in the new property sheet

**Measured, in window coordinates:**

    hidden ON    ◉ hidden   y = 607     + "not shown until something finds it — §3a"
                                        + trivial 5 · easy 10 · moderate 15 · hard 20 …
    hidden OFF   ○ hidden   y = 631     ⚠ both extra rows GONE

**Turning `hidden` off removes two rows from the sheet. The sheet is
bottom-anchored, so the radio you just clicked moves DOWN 24 PIXELS.**

> **⚠ The natural gesture after toggling something is to click it again to undo,
> and that click misses.** It took me three attempts and a full-window capture to
> work out that the control had moved rather than the toggle being one-way.

**This is worse than the two-row tab bar I filed against Aurora in `STUDY 29`,
because there the moving control was a *different* tab; here it is *the one you
just used*.**

**⚠ Suggested shape:** reserve the rows, or anchor the sheet at the top, or put
the explanatory sentence and the ladder where their appearance cannot move the
control that summons them.

---

# ⚠ 7 · THE CONVERSATION WRITER DESTROYS AUTHOR COMMENTS. The placement writer does not

**I wrote four comment lines into `sentinel-challenge.toml` explaining why the
check sits where it does. Loom's `Write` deleted all four** and kept only its own
`# Written by Loom.` header.

    -# ⚠ THE CHECK IS ON THE OUTBOUND LINK — `§9`. A gate on a `replies` link only
    -# decides whether the option is SHOWN; it never rolls. The roll that decides
    -# the outcome belongs on `then`, which is PICK ONE, so a failing check falls
    -# through to the ungated failure node below it.

**`PACKAGE-FORMAT-01 §2` is *"`git diff` works. A modder can look."* A comment is
the main thing one author leaves for the next, and this one deletes them.**

**⚠ And the contrast is the finding**: the **placement** writer preserved my hand
edits byte-exactly (`§5`); the **conversation** writer rewrites wholesale. **Two
writers in one program, two contracts.**

*(The format's own answer is `§3`'s per-node `note` field. Nothing tells an author
that, and a TOML comment is the obvious thing to reach for.)*

---

# 8 · `sentinel-challenge` — closed, and my first fix was wrong

**You said it needs a failure node. It did, and not where I first put one.**

**My first attempt** added an ungated sibling *reply*, so a failed Persuade would
still leave something to say. **Loom refused the Write, and the status bar said
why** — the third time reading it has saved me:

> *"refused — 1 problem: halt-this-room — `stand-down-i` is offered as a
> `Persuade` check and its `then` carries no check, so `_pick` takes the first
> link before any dice are touched. **§9 puts the check on the OUTBOUND link**…"*

**⚠⚠ That is `PT-1326` — my own never-rolling `[Persuade]`, 12/12 passes — stated
as its cause.** A gate on a `replies` link decides only whether the option is
**shown**. The roll that decides the outcome belongs on the **`then`**, which is
PICK ONE, so a failing check falls through to an ungated sibling.

**The correct shape, which Loom accepted and wrote:**

    [[player]]
    id   = "stand-down-i"
    say  = "Stand down. I outrank you."
    then = [{ to = "he-steps-aside", gate = { skill = "Persuade", dc = 14 } }, "rank-means-nothing"]

**And the editor now draws the `[Persuade]` marker on the NPC OUTCOME line rather
than on the player reply** — `§4c`'s amber, in the right place.

**⚠ It still does not fire in play**, and I could not isolate why — see `§10`.

---

# ⚠⚠ 9 · FIVE BUDGET ROWS ARE UNREACHABLE, AND IT IS NOT THE CLASS

**You said I had never seen five rows because no class I have played grants a
bonus. It is worse than that.**

`ACTION-ECONOMY-01`: **Bonus — one per round, only when something grants it.**

    grep -rn "bonusGranted" Lodestar/lib KOTOR-RPG-APP/lib Lens/lib Loom/lib

    round.dart:61    bool bonusGranted;
    round.dart:109   bonusGranted = false,          the constructor
    round.dart:122   bonusGranted = false;          startTurn
    round.dart:213   (bonusGranted && !bonusSpent)  a read
    budget_strip.dart:88  if (b.bonusGranted)       a read

> **⚠⚠ `bonusGranted = true` OCCURS ONLY IN TESTS. Nothing in any `lib/` in any
> of the four repos ever grants a bonus action — no class, no species, no feat,
> no power.**

**Confirmed on screen: three rows in every fight** — `10 move`, `action`, `gear`.

**⚠ And this is the second budget with no producer.** `BUILD 84` found the same
shape itself: *"`spendGear()` HAS NO CALLER IN THE APP"*. **Two of the five
budgets cannot be exercised by any choice a player can make.**

**⚠ And the chargen screen cannot help you find one that would.** Every class's
detail pane is byte-identical — `tier: standard base`, `force powers: not
granted`, and the same *"not extracted"* sentence. **Soldier and Duelist read the
same.** There is no surface on which a class that granted a bonus would be
distinguishable from one that did not.

---

# 10 · Scoped negatives — what I did NOT establish

- **⚠ Why `sentinel-challenge` does not fire.** With `owner` set to a valid
  placement tag (`probe-sentinel.probe-room.04`, which exists), on a
  **freshly restarted app**, walking into that creature started a fight.
  **I could not separate "the conversation does not fire" from "a character at
  1 of 14 vitality is attacked first"**, because `yard-tester.sav` is the only
  save in `a01-probe-room` and it is at 1 vitality. **A new character in the
  probe room would settle it and I did not make one.**
- **Which of `adjustmentsFor`'s two inputs is empty** — `§1`. I proved the map
  arrives empty by its effect, not by reading it.
- **Whether `PT-1533` is fixed in app `2c298f8`**, which landed while I wrote.
- **Whether `endar-spire` verifies clean in Loom.** I proved no `PackageProblem`
  member exists for a dangling owner and that the validator never reads the
  field; **I did not open `endar-spire` in Loom to see the count.**
- **The conversation wizard (`PT-1559`)** — built this morning from `STUDY 29`'s
  Store Wizard finding. **Never opened.**
- **Slice two's palette mode selector (`PT-1560`)** — I used the palette to
  place creatures and never exercised the mode selector as such.
- **`a02-probe-hall` and `a04-probe-slit`** — not entered this run.
- **Painting tiles in Loom.** Not done this run; `§5` is placements only.

---

# 11 · Smaller things, all at 1280×720

- **⚠ Rows sliced in half by list edges — three places**: the species list
  (`Nautolan`), the skills list (`Persuade`), and the class list. **The same
  non-quantised list height I filed against Aurora three times, in our own
  product.**
- **⚠ The library's 4th package card is clipped** by the right edge of the
  window with four packages installed.
- **⚠ `Load Game`'s right column is clipped** — *"just …"*, *"9 hou…"*,
  *"13 …"*. The dialog is narrower than its own content.
- **⚠ Tags are truncated in the tree** — `probe-warden.pro…` — **in the pane
  whose whole purpose is to show tags for the first time.**
- **⚠ A player-facing choice rendered as spec text**: the Equipment step offers
  *"TAKES THE CLASS'S OWN melee UPGRADE FROM §4a — Soldier → Long Sword + Short
  Sword…"* beside a sibling that reads *"aptitude in Beast Handling"*. **D3's
  family, still open.**
- **⚠ Inconsistent casing on sibling buttons**: `Try another` · `CLEAR` ·
  `BACK` · `Accept` on one screen.
- **⚠ The area name field changes identity**: the status line reads
  `Probe Room` before you move and `a01-probe-room · 1, 0` after.
- **⚠ Clicking Loom's board with no blueprint armed does nothing and says
  nothing** — and the arming is cleared by a delete, so the click right after a
  delete is a silent no-op. The status bar still shows the previous action.
- **⚠ The attack line shows its terms and the damage shows only a total.**
  `d20 16 + attack 0 + Strength 2` is checkable; `10 damage` is not. `PT-1543`
  put *components and total, never one without the other* on the defence row —
  **damage did not get it**, and with `brute force` granting +3 there is
  arithmetic to show.
- **A one-way door with no return is legal and undetected.** `a03-probe-yard`
  declares no connections; I walked in and could not walk out. My own authoring
  fault — **but no `PackageProblem` covers an area you can enter and not
  leave**, and in a stranger's package that is a soft-lock.
- **`hazard` is inert**, crossed with no message. Documented as undecided
  (`§2·0a`); recorded as still true.

---

# 12 · What I left behind

**`tester-probe` is intentionally dirtier than it was**, and every addition is a
test fixture, not a mistake:

    a01-probe-room   tag_seq 13   (was 9 — the counter is monotonic and correct)
      probe-warden.probe-room.10   hidden = true          ⚠ PT-1550's bed
      mystery.probe-room.11        from = "widgets/…"     ⚠ the unknown-kind bed
    dialogue/sentinel-challenge.toml
      owner = "probe-sentinel.probe-room.04"              ⚠ was a blueprint handle
      the Persuade check moved to the OUTBOUND link       ⚠ §9, and it validates

**Backups of packages, saves and console are in the session scratchpad**
(`BK3/`). **Five saves exist; `grukk-ironjaw.sav` is new and is mine.**

**⚠ `grukk-ironjaw` is stranded in `a03-probe-yard`** and cannot leave, for the
reason in `§11`.
