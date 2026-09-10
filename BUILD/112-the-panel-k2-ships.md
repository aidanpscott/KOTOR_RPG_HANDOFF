# BUILD 112 — the panel K2 ships, and a tool written twice

`PT-1642`, all three parts answered and built.

---

## 1 · ⚠⚠ THE RESEARCH, BECAUSE IT DECIDED THE BUILD

The owner asked what KOTOR's death screen does so the loss condition would be
**read rather than invented**. Read out of both installed games.

**K2 ships `gameover_p.gui`; K1 ships no such resource** — checked its 26 BIFs,
`patch.erf` and `Override/`. A modal 290×163 panel, message, then three
full-width stacked buttons:

| control | strref | text |
|---|---|---|
| `LBL_MESSAGE` | 42351 | `Your entire party has been killed.` |
| `BTN_LASTSAVE` | 49467 | `Load Last Saved Game` |
| `BTN_LOADGAME` | 49468 | `Go to Load Game List` |
| `BTN_QUIT` | 49466 | `Main Menu` |

⚠⚠ **NO CONTINUE, NO RESUME, NO SAVE.** Every exit either loads an earlier
state or leaves. **That is what settled the question** — a wipe is not a status
line you walk away from, and before this the app let you keep walking.

**K1 is the same fact without the panel** — the same strref number carrying the
instruction inside it: *"Your entire party has been killed.\nReturn to Main
Menu."* No buttons to put it on.

⚠⚠ **AND K2 STATES OUR RULE VERBATIM, AS A TUTORIAL STRING** — `41883`:
*"Party members who go down in combat will be revived at the end of the battle.
If your entire party goes down the game is over."* **`PT-1633` was ruled from
the owner's intent before anybody read that string.** Independent confirmation
of a rule we derived, not a source we derived it from.

Filed to `Scholar` as `STUDY/requests/001`, with the scoped negative I did not
check: whether either game's scripts can raise the panel.

## 2 · ⚠⚠ READING 1, AND THE ARGUMENT WAS NOT THE ONE I OFFERED

I argued from my own standing ruling about the save path. The owner's argument
is better and is the one recorded: **`PT-1496` — their answers transfer and
their constraints do not.** KOTOR has snapshot saves and therefore nowhere to
record a death that outlives the run. **They did not decide not to record it;
they had nowhere to record it.** `PT-1411` makes the log what persists, so
refusing to write the wipe would leave the log **silent about the most
important moment in the campaign** — `PT-1611`'s defect inverted, a cause
deliberately discarded.

So: the `died` stands, and `Continue` shows the panel instead of loading you
in. Nothing in the save path changed.

## 3 · What was built

* `play/game_over.dart` — K2's panel, its order, its wording. The rule is said
  in the game's own terms rather than cited (`PT-1479`).
* **The keyboard is swallowed while wiped**, not ignored — a key that still
  walked you around behind the panel would be the Continue K2 refuses to offer.
* **The panel is over the board, not instead of it.** K2 dims the room and
  draws the box on top: you are being told what happened to the thing you can
  still see.
* `_Where.gameOver` — **one widget, two ways in**: a fight that ended in
  defeat, and a save that records one. Two panels would be two wordings of one
  fact, which is the defect this pair of slices removed from `outOfReach`.

### ⚠⚠ AND THE ONE BUTTON OUR FORMAT CHANGES THE MEANING OF

The owner asked for this explicitly and the answer is worse than I expected.

K2's *"Load Last Saved Game"* rewinds to a **snapshot taken before the death**:
the defeat is in memory and the file predates it.

**Ours is an append-only log and `_append` writes it in place.** Every crossing
goes straight into the save you loaded — so **the wipe overwrites the very file
that button would open.** The newest save for the package is the one that now
records the defeat, and loading it lands back on the panel.

⚠ **So the button is offered only when it leads somewhere else, and today that
is almost never.** It needs a save for this package that is not the one in
hand, and with one save per run there is none. It is **absent with its reason
printed** rather than present and inert — the same absence-with-a-reason the
palette draws.

⚠⚠ **AND THE GAP IT REVEALS IS NOT MINE TO CLOSE: we have no autosave slot.**
K2's button works because K2 writes autosaves the death does not touch. Ours
cannot rewind because there is nothing to rewind to. **That is a product
question and it is in `STATE.md`, not invented here.**

⚠ **One rule, two callers.** `_canLoadLastSave` and `_whyNoLastSave` are read
by the play screen's panel and by the `gameOver` route both. Two copies of that
test would be the pair a rule gets applied to one of, in the slice that removed
exactly that.

### ⚠⚠ AND AN EXISTING TEST CAUGHT THE RULING

`whole_loop_test`'s *"Load Game LISTS THEM"* has asserted the character's name
on the play screen since `PT-1518`. **Kaeda Vos loses that fight** — the
fixture's log ends `character.dying, character.died` — so opening it now gives
the panel. **The check did its job on a change made three files away**, and the
case was updated to assert the ruling rather than narrowed around it.

⚠ **The row above still names her.** A listing describes the SAVE — who, what
level, where — and is not a claim about whether that character is on their
feet. Two facts, both shown.

## 4 · ⚠⚠ A TOOL WRITTEN TWICE, AND A TYPE MAP NOBODY VERIFIED

`Scholar` needed a KEY/BIF reader for `STUDY 19`, grepped all six repos, found
none, wrote one, **and filed it inside its own study folder.** I ran the same
search for this research, got the same answer, and wrote the same tool.

> **Owner, ruled: a tool goes in `scripts/`, not in a study folder.**

**`Scholar`'s was the better reader and is the one that survived** — the class
API, the NWN:EE path resolution, the case-insensitive fallback and the
streaming read are all theirs. Mine contributed the corrected `GUI` code.

⚠⚠ **AND `STUDY 23 §5`'s CORRECTION WAS NEVER APPLIED TO THE FILE.** Its own
note — *"the table in `keybif.py` had 2009 as `utc` and 2010 as `nss`, and 2027
is `.utc`"* — was right, and the file still carried the wrong map. **A
conclusion stated in a report and never applied.**

⚠⚠ **AND THE SAME WRONG MAP WAS IN `archive.py`, SIX CODES OF NINE**, under a
comment reading *"the type codes below were verified by reading contents, not
assumed from a table."* **A clause asserted rather than checked, in the comment
that warns against exactly that.** Consistently shifted — every code named the
type belonging to a different code:

    2009 said utc · is nss      2032 said utw · is utt
    2027 said utp · is utc      2035 said utt · is uts
    2040 said uts · is ute      2044 said ute · is utp

⚠ **NOTHING SHIPPED THROUGH IT.** All 506 extracted `.utc` and 1,550 `.uti` in
`data/` carry the magic their extension claims, **checked file by file**. It
was latent: the next caller of `extract(..., 'utc')` would have written 1,774
script sources into `data/creatures/`. `2025` (uti) and `2023` (git) were
right, which is why it was never noticed.

**Every code is verified now** — one resource of each type pulled and its magic
read. Both files share one map, and the two that carry no magic (`tga`, `mdl`)
say so rather than being asserted.

### The check, so the ruling bites

`check_tools_in_scripts.py`, **blocking**. A ratchet, not an inventory: a NEW
tool in a study folder fails **and so does a healed one**, so the list cannot
rot into an allowance nobody prunes.

⚠ **It found three more the moment it ran** — `dfm.py` and `pe.py` live in
`code/`, not `tools/`, and my hand count had missed them. Nine remain, each
excused with a reason and `Scholar`'s to move. ⚠ **One of them is
`parse2da.py`, which ALSO exists in `scripts/`** — a second duplicate of one
reader, found by the check written for the first.

`d2.py` imported the reader I removed; **its import was repaired in the same
commit** rather than left broken. One line, and nothing else in `Scholar`'s
directory was touched.

## 5 · Recorded, not built

* ⚠ **`PT-1635` is wrong where it repeated me.** `BUILD 110`'s second-State
  conclusion is withdrawn: the unmodified build also creates three States,
  properly paired, and the failing sequence is an ordinary quit-and-reload the
  test drives.
* ⚠ **The `_append` race is blocked on the same question**, and the named
  probe — print `_said` inside the walk loop — is the next thing, not a third
  remedy.
* ⚠ **A hanging test is worse than a failing one.** Real `File` futures never
  complete under `testWidgets`' `FakeAsync`; the case does not fail, it hangs,
  and nothing tells you which case it was.
