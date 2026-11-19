# TEST 265: Loom Verify, conversations you can't leave

Real Loom and real game, my Xvfb `:2`, no K2. Text only. Frames, the Verify readings, the conversations I wrote, the original files I edited, the load log, every gate output, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-265/`. Names in brackets below are files there.

## Build

- **Loom**: `06050c3`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **App**: main `3985c97`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Gate**: I ran `gate.py --at 3985c97` twice, one straight after the other, in the project's MAIN_WORK (`gate265-1.txt`, `gate265-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 3985c97, 6029 tests, 0 failed".
  - Both state lines were the same: "MAIN_WORK e75ee6db · HANDOFF 8cefd88 · KOTOR-RPG-APP 3985c97 dirty · Lodestar a554b93 · Loom 06050c3 · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
  - The shared app tree was dirty with Coder's edits, which MAIN told me was being put back.
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Copies only**: every Loom step ran against a scratch library (`~/kotor-tester/loom-scratch-265/kotor-rpg/packages`), a copy of the whole Shelf without `.git`. Loom and the app reached it through `XDG_DATA_HOME`. The real packages have no edits.
- **Save**: Looter, md5 `119cbbbd`, from the restore copy `notes/saves265`, which I took from `saves264`.

## Summary

All seven steps pass. One expectation in the order doesn't hold on the current Shelf; that's in Step 2 below.

| # | Check | Result |
|---|---|---|
| 1 | The Shelf as it is | **PASS**. Of the 19 packages with conversations, only tester-208 shows anything new: one Note on "join-fight". |
| 2 | The trooper, then without "Command sent me." | **PASS** where "My mistake." still loops (tester-217's copy: the Note appears). On endar-spire's copy nothing appears, because "My mistake." now ends the conversation. |
| 3 | A true trap | **PASS**. A Warning names exactly the stuck lines, both for a whole conversation and for one branch. |
| 4 | A hub that asks again or says goodbye | **PASS**. Nothing. A conversation whose only exit is gated also gives nothing. |
| 5 | A terminal that loops | **PASS**. tester-tries' console gives nothing; without `shown = "terminal"` the same file gets a Warning. |
| 6 | 0 problems with only notes and warnings | **PASS**. The Loom header, tree and status line, and the app's library tiles and count, all ignore them. |
| 7 | The app plays at 3985c97 | **PASS**. "My mistake." ends with "the conversation is over", and no fight starts. |

## 1. The Shelf as it is

- **tester-208**: Verify lists its 5 known problems (unreachable areas), then "Note · join-fight · In the conversation "join-fight", the only way out without a gate starts a fight." The count stays at 5 in the header, the dialog and the status line (`l-03-t208-verify`).
- **The other 18 packages with a `dialogue` folder**: I opened each in Loom and opened Verify. None shows a Note or a Warning (`step1-ocr.txt`, `l-1x-*`).
  - Twelve read "No problems found.": droid-shield-bed, endar-spire, locked-and-trapped, party-lock-bed, precognition-ambush, store-bed, tester-217, tester-mines, tester-pazaak, tester-purse, tester-reach, tester-talk.
  - tester-tries reads "No problems found." too; its console is the terminal in step 5.
  - The rest list only their known problems: tester-probe 17, tester-save-bed 2, tester-sight 3, tester-strongroom 2.
  - For tester-probe and tester-sight I scrolled the list to its end (`l-1x-tester-probe-end`, `l-1x-tester-sight-end`).
- **The other 60 packages** have no conversations.
- **Cross-check**: I ran Lodestar's own `conversationExits` over every conversation file in the copies (`scripts/exits265.dart`, `scripts/shelf-as-is.txt`). Only join-fight came back with `onlyFightOut`, and nothing was stuck. That matches what Loom shows.

## 2. The Command Deck trooper

- **On the copy, unchanged**: endar-spire reads "No problems found." with nothing below (`l-10-endar-spire`).
- **The Shelf now has four copies of trooper-challenge.** Shelf `8f2d845` gave "My mistake." an ending in endar-spire only. In tester-217, tester-save-bed and tester-sight it still loops back to the first line (`then = ["this-deck-is"]`).
- **"Command sent me." removed** (the reply and its line) on two copies (`conversations/edited-*`):
  - **tester-217** (My mistake loops): "No problems found.", then "Note · trooper-challenge · In the conversation "trooper-challenge", the only way out without a gate starts a fight." (`l-20-tester-217-nocmd`).
  - **endar-spire** (My mistake ends): "No problems found." and nothing else (`l-20-endar-spire-nocmd`). "My mistake." is a way out with no gate and no fight, so by the rule no Note is due.
- So the order's "the note appears" holds on the copies where the loop is still there, not on the Command Deck one. That looks right to me, but I'm reporting it because the order expected otherwise.

## 3. A true trap

I added two conversations to tester-talk's copy (`conversations/trap-all.toml`, `trap-part.toml`):

- **trap-all**: every reply loops back, and there's no ending at all.
  - "Warning · trap-all · In the conversation "trap-all", "ask-why", "guard-again", "guard-asks", "no-papers", "try-again" can never reach an ending, even with every gate passed: a player there can only close the game."
- **trap-part**: a hub with a goodbye, plus a "complain" branch whose form loops forever.
  - "Warning · trap-part · … "again", "complain", "filled", "form", "form-wrong" can never reach an ending …".
  - It names the branch and not the hub or the goodbye.
- The header still says "verify", the tree has no red, and the status line reads "opened" (`l-30-tester-talk`).

## 4. Hubs (same package, same Verify)

- **hub-ask**: two questions that come back to the hub, plus "Goodbye." to a farewell line. Nothing.
- **gated-exit**: a guard whose only exit is behind a Persuade gate; the other reply loops back. Nothing. Gates count as passable, and there's no ungated ending to make a Note about.

## 5. A terminal that loops

- tester-tries' console (`boot → log → read → log`, no ending, `shown = "terminal"`): "No problems found." (`l-1x-tester-tries`).
- **Control**: with the `shown = "terminal"` line removed on the copy, Verify read "Warning · console · … "boot", "log", "read" can never reach an ending …" (`l-40-tries-noterminal`). So the skip is what keeps it silent.
- I put the line back, then clicked Verify again in the same window: "No problems found." (`l-41-tries-restored-again`). It reread the file at once.

## 6. Counts with only notes and warnings

- **Loom**: on tester-talk (2 Warnings) and tester-217 (1 Note), the package row says "verify", not a count. The tree draws nothing red, and the status line reads "opened". On tester-208 the count stays 5 with the Note listed.
- **The app's library on the copies** (`a-02` to `a-04`): "77 packages installed · checked, 11 with problems". Tester Talk and Tester 217 show no count, and Tester 208 shows "5 problems".
- **The same app on the real Shelf** (the step 7 run): its log lists the same 11 packages with the same 47 problems as the copies' run (`devlog/app265-looter.log`, `devlog/app265-scratch.log`).

## 7. The app at 3985c97 (Looter)

- I loaded Looter by hand (`loads.txt`, frame at the Load click) on build test265.
- I walked into the Sith Trooper on the Command Deck. He opened with "This deck is sealed. Turn around." and offered all six replies (`p-03-talk`).
- I picked 6, "My mistake.". The bar read "the conversation is over", and no fight started (`p-05-after`).

## Odd window size

- Loom at 1280×1080, tester-talk's Verify: both Warnings wrap whole inside the box, and the buttons sit below them (`l-50-talk-1280x1080`).

## Odd, not filed

- **Warnings are the same red as problems.** Under "No problems found." in teal, a Warning's label and sentence are both drawn in the problems' red. Only the word "Warning" tells them apart. Notes are teal and grey.
- **Loom's folder dialog made an empty folder.** I typed a path into GTK's location bar, its autocomplete doubled my typing ("endar-spirendar-spire"), and Return created that empty folder in my scratch library. Loom then said "Not a package". It's GTK's chooser and my typing, not Loom's code. I removed the folder.

## What I got wrong

- I first ran the gate in my old clone of MAIN_WORK (`~/kotor-tester/KOTOR_RPG_MAIN_WORK`). It reads a KOTOR-RPG-APP clone left at `aa27d23` since 2026-10-12, so it showed "dirty", DO NOT SEND and NOT FOR TESTER (`gate-ledger-265a/b/c.txt`). I told MAIN that reading came from Coder's mid-edit tree, but its "aa27d23 dirty" was my stale clone. The project's MAIN_WORK gave the real reading (`gate-ledger-265d.txt`, `gate265-1/2.txt`). Its own app tree is dirty with Coder's edits too (`lib/play/*`, the new Light-and-Dark test), but it reads SENDABLE and FOR TESTER at 3985c97.
- My Load helper's OCR failed on "Looter" again; I loaded it by hand with a frame.
- My first Verify clicks on three packages hit the name and opened Properties instead. I fixed the click and reran them.
