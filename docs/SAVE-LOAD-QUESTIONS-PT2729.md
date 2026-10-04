# Save / Load — what K2 does, what we do, what I propose (PT-2729, step 2)

*For the owner to rule on. Everything under "K2 does" was read off the real game on 2026-10-04 (screenshots in `BUILD/screens/pt2729-saveload/k2/`, described in that folder's README). Nothing under "we do" is new: it is how the app works today.*

**The short version:** K2 keeps a numbered list of saves per character and you save by hand into it. Our app already writes everything you do to one file per character as you play, so a "save" for us is a **bookmark** into that record, not a copy of it. I propose we draw K2's screens exactly, and let each K2 button do the closest honest thing in our model. Six questions need your ruling; each has a recommended answer.

---

## 1. Slots — how saves are numbered and listed

| | |
|---|---|
| **K2 does** | One list per character. Each row reads `[Modded] 10 : ZTEMP` over the date and time. The number is the next free one across **all** characters (Palyn Morusk's save is 9, so Onjo's next was 10). The list is newest first. Saving shows a **New Slot** row at the top; picking it asks for a name. Picking an existing row asks *"Are you sure you want to overwrite the save game?"* (OK / Cancel). **Delete** asks *"Are you sure you want to delete the save game?"* (OK / Cancel). |
| **We do** | One file per character per campaign, and it is written automatically as you play. There is no Save screen and no slots yet; the Load screen lists characters, not saves. |
| **I propose** | Build K2's list and prompts word for word. A manual save is a **named bookmark** into the character's record (cheap, instant). Numbers are global like K2's. **Delete** removes the bookmark only; the record itself is never lost. **Loading a bookmark rewinds to that point** (and says so in the record, as already designed). |
| **Your call** | Numbers global across characters like K2 (my recommendation), or per character? |

## 2. Autosave

| | |
|---|---|
| **K2 does** | A checkbox, **AUTOSAVE**, in Gameplay options (ticked). It keeps one row called **Auto Save** with no number. That row appears in the **Load** list (last, because it is the oldest) but **not** in the Save list. |
| **We do** | Every action is written to disk the moment it happens. That is stronger than an autosave, and it can't be switched off. |
| **I propose** | Keep writing continuously. Show one **Auto Save** row in the Load list, in K2's place and style, meaning "where you left off"; loading it does what **Continue** does. No checkbox, because there is nothing to turn off. |
| **Your call** | OK to have no Autosave checkbox (my recommendation), or add one that is always ticked and greyed? |

## 3. Quicksave

| | |
|---|---|
| **K2 does** | **F4** quick-saves, **F5** quick-loads. Pressing F4 shows a **full-screen "Saving" picture** (the game's loading art, a progress bar, a tip line) for a few seconds, then returns to play. It uses one slot, called **Quick Save** with **no number**, overwritten every time; it sits first in the list because it is the newest. |
| **We do** | Nothing. |
| **I propose** | The same keys and the same single **Quick Save** bookmark, overwritten each time, drawn as an unnumbered row. Show K2's full-screen Saving picture, briefly, so it feels the same, even though ours finishes at once. F5 loads it (and says "no quick save" if none). |
| **Your call** | Keep the full-screen Saving picture (my recommendation, for 1:1), or skip it because our save is instant? |

## 4. Main-menu Load Game against Continue

| | |
|---|---|
| **K2 does** | The main menu has **Load Game** and no Continue. Load Game opens on **one character's** list. When I opened it, it showed Palyn Morusk (the other character), not Onjo, the one last played. A **Switch Characters** button cycles to the other characters' lists. A **Cloud Save** tick box sits at the top left of every list. |
| **We do** | The package menu has **Continue** (opens the most recent character) and **Load Game** (a list of characters). |
| **I propose** | Keep **Continue**, because it is a kindness K2 doesn't have and costs nothing. Make **Load Game** K2's screen: it opens on the **most recent** character's list (better than K2's arbitrary pick), **Switch Characters** moves between characters. Draw the **Cloud Save** box? No: we have no cloud saves, so I'd leave it out and say so in the parity table. (This also lands the "Go to Load Game List" button on the defeat panel on the real list.) |
| **Your call** | Keep Continue beside K2's Load (my recommendation)? Leave the Cloud Save tick out? |

## 5. The thumbnail and the save's side panel

| | |
|---|---|
| **K2 does** | Selecting a row shows a **screenshot** of the game as it was saved, with the character's name in a bar above it and the area's name in a bar below, then the level name (for example *Administration Level*), **Time: 0H 7M**, and up to three party portraits (the leader in the middle). A new, empty slot shows `New Slot` and `Time: 0H 0M`. |
| **We do** | We keep no picture. We do know the character, class, level, area and time saved. |
| **I propose** | Store a small picture of the play view in each bookmark (our map view, not 3D art), and fill the other fields from what we already know; party portraits from the portraits we already have. It adds a few tens of kilobytes per bookmark. |
| **Your call** | Store a picture per bookmark (my recommendation)? Or draw the panel with the area's name only? |

## 6. Where saving is refused, and the words

| | |
|---|---|
| **K2 does** | The refusals I could confirm from its own text: *"The maximum number of saves has been reached. Please delete or overwrite existing saved games."* (there is a cap), and *"You need to free N more blocks to save to a new slot. You will need to delete or overwrite an existing save game."* (disk space). K2 also blocks saving in some moments (during combat and some scripted scenes); **I could not reach one safely from the save I had, so the exact moments and wording are not captured.** |
| **We do** | Nothing is refused, because nothing is manual yet. |
| **I propose** | Refuse a manual save and a quicksave **in combat and in a conversation**, with a plain-English line in K2's message-box style ("You cannot save during combat."), because the record is mid-exchange there; allow it everywhere else. Use K2's two sentences above for the cap and for disk space (our cap: none, unless you want one). Corrupt or unreadable saves open with a plain reason, as built. |
| **Your call** | Refuse in combat and conversation (my recommendation)? Any cap on the number of saves? |

---

**Already settled and built:** the **[Modded]** tag. K2 prints it itself, in brackets to the left of the slot number, in the row's own font and colour, which is exactly where we put ours.

**What I will do the moment you answer:** build the screens element by element to K2's layout (`saveload_p.gui`, `savename_p.gui`), with the parity table in `docs/K2-PARITY-SAVELOAD-PT2729.md`, and tests for each behaviour above.
