# K2 Save/Load — read-only capture, 2026-10-04 (PT-2729)

Taken in a live K2 session (Steam build with the Cloud Save checkbox), 1920x1080, nothing saved, deleted or overwritten. Account saves: Onjo Trigit (slots 8, 4, 2 x5, Auto Save) and Palyn Morusk (slot 9 "DROID ARMOR").

| Shot | State |
|---|---|
| 00-main-menu | Main menu: New Game, Load Game, Movies, Music, Options, Quit, More Games |
| 01 | Main-menu Load Game, FIRST view: the list opens on the OTHER character (Palyn Morusk, one row `[MODDED] 9 : DROID ARMOR`, Oct 02 2026 - 17:59:46; area bar `EBON HAWK`, `INTERIOR`, a droid portrait), not the one last played |
| 02, 03 | Main-menu Load Game on Onjo's list: first row selected, then a lower row selected |
| 10 | In-game Options menu: Save Game ("Save the current game"), Load Game, Gameplay, Feedback, Auto-Pause, Graphics, Sound, Exit Game |
| 11 | In-game Save Game: first row **New Slot**, then the saves; Delete disabled; Auto Save row absent from this list |
| 12 | Save Game with an existing row selected (Delete now enabled) |
| 13 | In-game Load Game: same rows plus **[Modded] Auto Save** last |
| 14 | Exit Game box: "Do you really want to quit? Your progress will not be saved." OK / Cancel |

Read off the pictures (not yet cited to a `.gui`/StrRef; the next pass does that):
- Rows are two lines, centred: `[MODDED] 8 : PT-2715 EQUIPPED` over `SEP 30, 2026 - 16:15:57` (small caps). **K2 itself prints `[Modded]` left of the slot number**, same font and colour as the rest of the row.
- Right pane: character name bar (top), thumbnail of the saved view, area bar (bottom, `PERAGUS`), the module/level text under it (`ADMINISTRATION LEVEL`), `TIME: 0H 7M`, three portrait boxes (the party; the leader is in the middle one).
- Buttons: Load list `CANCEL | LOAD | DELETE | SWITCH CHARACTERS`; Save list `CANCEL | SAVE | DELETE | SWITCH CHARACTERS`. A `CLOUD SAVE` checkbox sits top-left of both lists.
- The list belongs to ONE CHARACTER; the main-menu Load opened on a different character (Palyn Morusk) than the one last played, and Switch Characters moves between them.
- New Slot's pane: character name, empty thumbnail frame with `NEW SLOT` centred, `TIME: 0H 0M`, empty portraits.

NOT captured, on purpose: the naming entry, the overwrite prompt, the delete prompt, saving/loading in progress, quicksave and the "cannot save here" refusals. Each needs a Save, Delete or confirm press (or a special area) and K2 is read-only for us. These go to the owner as open questions.
