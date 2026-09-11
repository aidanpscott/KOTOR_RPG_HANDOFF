# TEST 064 — KOTOR 1 reference pass: the real chargen flow, and there is no
# droid naming to compare against

**Built against:** actual retail **STAR WARS: Knights of the Old Republic**
(Steam AppID `32370`), launched through the Steam client already running on
this machine, via Proton `experimental-11.0-20260910b`. Not a KOTOR_RPG_APP
build — this is the reference game itself, played to observe its own UI
rather than to confirm anything about our engine.

**Instrument:** the machine already had real player progress in
`swkotor/Saves/` (an autosave plus four manual saves, 43MB). Backed up the
entire `Saves/` directory to my scratchpad **before** touching the game, on
the same principle as the NWN install rule — a real save is not mine to
risk. Launched twice: once through full character creation to `Play`
(killed the process at the Endar Spire loading screen, before any gameplay
input that could trigger an autosave), once briefly back to the main menu
only, no further, per the project owner's direct correction mid-session (see
below). Diffed the `Saves/` directory against the backup after each
session: byte-identical both times, only `steam_autocloud.vdf`'s mtime
touched (Steam's own cloud-sync bookkeeping, content unchanged). Nothing
else on the machine was touched — this pass never went near
`KOTOR_RPG_APP`, Loom, or any Tester package.

---

## 1. The character creation flow, start to finish

`Main Menu → New Game` goes straight to chargen — no forced intro movie, no
difficulty prompt first.

1. **`CHARACTER GENERATION — Choose your class`** — one screen combines
   class, gender, and appearance. Six body portraits in a row for the
   current class+gender pairing (this session showed "Male Scoundrel"); a
   description line underneath explaining the class. Clicking a portrait
   selects both the appearance and confirms that class+gender, advancing to
   the next screen. **I did not test whether this screen itself carries
   arrows to cycle among the six class×gender combinations** — the project
   owner confirmed directly, before I could re-check it, that there is no
   droid option anywhere in this flow, which was the only thing a second
   pass would have been checking for; see §2.
2. **`CHARACTER GENERATION — [Class name]`** — a hub-preview screen: headshot
   thumbnail, full-body model, an empty six-attribute table (Strength
   through Charisma, all blank), and two buttons: **`Quick Character`**
   (pre-selected, help text: *"your character will use an optimized
   template. You will only have to choose your character's appearance and
   decide on a name"*) and **`Custom Character`**. I took Custom, to see the
   full screen set.
3. **`CHARACTER GENERATION` numbered hub** — six numbered rows, all reachable
   in any order, each opening its own full-screen sub-panel and returning
   here on OK:
   - **`(1) Portrait`** — a dedicated carousel screen (small thumbnail +
     large rendered head, left/right arrows, gender/variant toggle icons,
     OK/Cancel). Not a popup — same full-panel chrome as every other screen
     in this flow.
   - **`(2) Attributes`** — point-buy grid (remaining points, per-attribute
     cost/modifier, a description pane), `Recommended` / `OK` / `Cancel`.
     A first-use help popup appeared automatically over this screen the
     first time it opened (a genuine modal overlay, dismissed with its own
     `OK`) — noted because it's a real example of what KOTOR 1 actually
     does use popups for, which sharpens the contrast with Name below.
   - **`(3) Skills`** — same point-buy shape, another first-use help popup.
   - **`(4) Feats`** — a feat-icon grid; this class's remaining-feat count
     started at 1, and the game refused to let me leave the panel until I
     used the on-screen `Add Feat` control to spend it (a blocking dialog:
     *"You have gained new feats. You must use 'Add Feat' to select your new
     feats before continuing."*).
   - **`(5) Name`** — see §1a below; this is the screen the ask was really
     about.
   - **`(6) Play`** — the terminal action. Clicking it goes directly to a
     loading screen for the game's opening area; no further chargen screens
     exist after Name.

### 1a. The Name screen itself

Order confirmed: **Portrait is step 1, Name is step 5 of 6** — portrait
first, name second-to-last, Play last. This is the real game's own
ordering, for whatever it's worth as a reference point.

The screen (`CHARACTER GENERATION — Name`) is a **full-screen panel**, the
same chrome and same modal weight as Portrait/Attributes/Skills/Feats — it
is not layered as a popup over another screen, and nothing else is visible
behind it. Contents: a single-line text field, pre-populated on first visit
with an already-generated random name (no click needed to get one); a
**`Random Name`** button below the field that replaces the entire field's
contents with a freshly generated name on each press (confirmed by pressing
it twice — `Denil Sana` then `Bron Lankari`); the field remains directly
editable by typing, cursor visible mid-edit. `OK` / `Cancel` at the bottom.

One incidental observation: typing did not accept a keyboard `Ctrl+A` /
`Delete` to clear the field the way a normal text control would — it just
appended past the existing text, requiring repeated Backspace to actually
clear it. Not something I chased further; noted only because if anyone is
comparing widget behavior, this field does not behave like a stock text
input in every respect. I did not determine an exact character cap; an
18-character concatenation test (`Bron LankariBaseli`, cut off there) is the
only data point I have and I would not treat that as a measured limit.

## 2. Droid naming — does not exist in this game, confirmed directly

I did not find a droid option anywhere in the one chargen pass I completed
(all six portraits in the class/appearance screen were human-appearing, and
neither the class-hub screen nor the numbered-panel hub ever offered a
species or chassis choice). I had queued a second, narrower check —
reopening just the very first "Choose your class" screen to see whether it
carries arrows for cycling into a droid option I might have missed — and
was stopped by the project owner mid-check with a direct statement: **there
is no droid option in the game.** I did not complete that second check
myself; the owner's correction is what closes this, not my own
verification. Recorded as told, not as independently exhausted.

Given that, the follow-on question — whether a droid **companion** (T3-M4,
HK-47) gets any naming/designation screen when recruited later — was never
reachable from chargen and was not chased, since the owner's statement
already answers what this pass was checking for at the character-creation
level, and reaching a droid companion's recruitment is hours of real
gameplay past where this pass stopped.

**So, against the reference design described in the ask** (chassis-prefixed
designation, generate-random control, manual entry, a canon ban list) —
KOTOR 1 has nothing to compare it to. The generate/manual-entry pattern
exists in this game, but only for the one human player-character name field
described in §1a, and it carries no format constraint I could find beyond
whatever the untested length cap is. **This is not a real-game precedent
that can be checked against; it's a design built without one**, which is
worth saying plainly rather than stretching the Name screen's shape into an
answer it doesn't give.

---

## What I did not check

- Whether the class/appearance screen has left/right navigation to cycle
  class+gender combinations — stopped mid-check by the owner's correction
  that the underlying question (droid option) is already answered.
- Any character length limit on the Name field — only the one incidental
  data point above.
- Whether a droid companion is ever named/designated on recruitment later
  in the game — moot per the owner's confirmation, and far past a
  reasonable single-session reach regardless.
- Whether `Quick Character` (the template route I didn't take) reaches Name
  by a different path or order than Custom Character did.

## State

- `swkotor/Saves/` — confirmed byte-identical to the pre-session backup
  after both launches; only `steam_autocloud.vdf`'s mtime touched, content
  unchanged. No new save was written, no existing save was overwritten.
- Nothing in `KOTOR_APP_PROJECT` was touched this pass — no packages, no
  saves, no git state, in either KOTOR-RPG-APP, Lodestar, or Loom.
- Both KOTOR 1 process launches were killed by PID; the first was killed at
  the Endar Spire loading screen (post-chargen, pre-gameplay-input), the
  second at the main menu.
