# REQUEST 001 → Scholar — the death screen, and nine tools that need moving

**From `Coder`, `BUILD 112`, `PT-1642`.** ⚠ `PT-1446` gives `STUDY/` to you;
`requests/` is mine, the way `TEST/requests/` is mine inside `Tester`'s
directory. **Nothing outside this folder was touched except one import** — see
§3.

---

## 1 · ⚠⚠ THE FINDING IS ALREADY MADE. This is a hand-over, not a question.

The owner asked what KOTOR's death screen does, so that our loss condition
would be **read rather than invented**. I read it out of both installed games.
**It is a build fact that turned out to be a source-game fact**, which is
yours — so here it is, in full, so nobody derives it twice.

### K2 ships a panel; K1 ships none

`gameover_p.gui` (PC) and `gameover_x.gui` (Xbox) in K2's `chitin.key`.
**K1 has no such resource** — checked its 26 BIFs, `patch.erf` and `Override/`.

Modal `TGuiPanel`, 290×163 at (174,171). Message label, then three full-width
stacked buttons, in this order:

| control | strref | K2 text |
|---|---|---|
| `LBL_MESSAGE` | 42351 | `Your entire party has been killed.` |
| `BTN_LASTSAVE` | 49467 | `Load Last Saved Game` |
| `BTN_LOADGAME` | 49468 | `Go to Load Game List` |
| `BTN_QUIT` | 49466 | `Main Menu` |

`gameover_x` is the same panel with `LBL_A`/`LBL_B`/`LBL_X` glyph slots beside
the three rows — the Xbox twin, same order, same geometry.

⚠⚠ **THERE IS NO CONTINUE, NO RESUME AND NO SAVE.** Every exit either loads an
earlier state or leaves the game.

### K1 is the same fact without the panel

**The same strref number**, carrying the instruction inside the message because
there were no buttons to put it on:

    42351  "Your entire party has been killed.\nReturn to Main Menu."

⚠ **So the number was reserved before the panel existed and K2 shortened the
string when it built one.** That is worth a record: the two games disagree in
UI and agree in fact.

### ⚠⚠ AND K2 STATES OUR RULE VERBATIM — strref 41883

> *"One of your party is down! Party members who go down in combat will be
> revived at the end of the battle. **If your entire party goes down the game
> is over.**"*

It is a **feedback/tutorial string** — the game teaches the player the rule.

⚠ **`PT-1633` was ruled from the owner's intent before anybody read that
string**, and `PT-559` before it. The owner calls this the find of the slice
and I agree: it is independent confirmation of a rule we derived, not a source
we derived it from.

## 2 · What I am asking for

1. **Turn this into a proper `STUDY` record** in your template. It belongs
   beside `STUDY 23 — the dying band, and what a dead creature leaves behind`,
   which established that KOTOR has **no dying band at all**; this is what
   happens at the other end of the same rule.
2. ⚠ **The scoped negative I did NOT check**: whether either game's *scripts*
   can trigger the panel, and whether `k_sup_*`/`nwscript.nss` expose party
   defeat at all. `STUDY 23` already read `nwscript.nss` whole, so you are one
   grep from an answer I could not justify spending a build slice on.
3. ⚠ **And one thing K2 cannot answer**, recorded so it is not mistaken for a
   gap in the research: KOTOR has snapshot saves, so *"what does the save keep
   after a death"* never arises there. `PT-1496` governs — **their answers
   transfer and their constraints do not.** The owner ruled it separately
   (`PT-1642`, reading 1): the `died` stands and `Continue` shows the panel.

## 3 · ⚠⚠ NINE TOOLS, AND ONE OF THEM I WROTE TWICE

You needed a KEY/BIF reader for `STUDY 19`, grepped all six repos, found none,
wrote one, and filed it at `STUDY/19-input-and-combat/tools/keybif.py`. **I ran
the same search for this research, got the same answer, and wrote the same
tool.**

> **Owner, ruled: a tool goes in `scripts/`, not in a study folder.** A tool
> filed inside the study that needed it is a tool the next agent cannot find —
> `PT-1498`'s docs mirror and `PT-1532`'s STUDY README, a third time.

**Yours was the better reader** and it is the one that survived, at
`MAIN_WORK/scripts/keybif.py`: the class API, the NWN:EE `data/` path
resolution, the case-insensitive fallback and the streaming read are all
yours. I contributed the corrected `GUI` code and the verified type map.

⚠⚠ **AND `STUDY 23 §5`'s CORRECTION WAS NEVER APPLIED TO THE FILE.** Your own
note — *"the table in `keybif.py` had 2009 as `utc` and 2010 as `nss`, and 2027
is `.utc`"* — was right, and the file still carried the wrong map. **A
conclusion stated in a report and never applied**, which is a shape this corpus
has named. It is fixed, and every code is now verified by pulling one resource
of that type and reading its magic bytes rather than remembered.

⚠ **The same wrong map was in `MAIN_WORK/scripts/archive.py`, six of nine
codes**, under a comment claiming *"the type codes below were verified by
reading contents, not assumed from a table."* Both files now share one map.
**Nothing shipped through it** — all 506 extracted `.utc` and 1,550 `.uti`
carry the magic their extension claims, checked file by file — so it was
latent: the next caller of `extract(..., 'utc')` would have written 1,774
script sources into `data/creatures/`.

### What I changed in your directory, and it is one line

`STUDY/19-input-and-combat/tools/d2.py` did `from keybif import KeyIndex`.
Removing the reader would have left it broken, so **its import now points at
`MAIN_WORK/scripts/`** and nothing else in it changed. It still runs.

### ⚠ Nine still to move, and they are yours

`scripts/check_tools_in_scripts.py` is in the gate as **blocking**, with all
nine named and excused with a reason. It is a ratchet, not an inventory: a NEW
tool in a study folder fails, **and so does a healed one** — move a file
without dropping its excuse and the gate goes red, so the list cannot rot into
an allowance nobody prunes.

    STUDY/12-toolset-ui/code/dfm.py            ⚠ in code/, not tools/
    STUDY/12-toolset-ui/code/pe.py             ⚠ in code/, not tools/
    STUDY/19-input-and-combat/tools/bg3stats.py
    STUDY/19-input-and-combat/tools/cols.py
    STUDY/19-input-and-combat/tools/d2.py
    STUDY/19-input-and-combat/tools/lspk.py
    STUDY/19-input-and-combat/tools/lspk_header.py
    STUDY/19-input-and-combat/tools/lz4block.py
    STUDY/19-input-and-combat/tools/parse2da.py   ⚠⚠ AND scripts/parse2da.py
                                                  ALSO EXISTS — a second
                                                  duplicate of one reader,
                                                  found by the check written
                                                  for the first.

⚠ **The two in `code/` are why the first count was seven.** I listed `tools/`
folders by hand and the check found three more the moment it ran — which is the
argument for the check rather than for the list.

## 4 · What I did not check

* **Neither game was launched.** Every claim here is from files.
* **K2's `gameover` panel was read, not watched.** What DISMISSES it, whether it
  fades, and whether a script can raise it are unknown.
* **No other language's `dialog.tlk` was read.** The strrefs are English.
