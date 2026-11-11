# TEST 250, Finding 1: a short check for Coder on 6158aec

This is a short check, not a full test. Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, timings, the load log, the dev log and my click helpers are in `KOTOR_RPG_MAIN_WORK/media/screens/test-250c/` (525872ca); names in brackets below are files there.

## Build

- **App**: main `6158aec`, a fresh clone. `gate.py --at 6158aec`: "FOR TESTER — CORE at 6158aec, 5911 tests, 0 failed".
- **Lodestar**: `e7ece7b`. **Shelf**: `bd522ba` (origin/main; it adds Pazaak's side decks, as 6158aec does). check_shelf is clean.
- **Settings**: defaults.
- **Save**: icons-185 `.sav` and `.marks` restored from TEST 250u's copy. Before the load the md5s were: sav `d69900e8`, slot 90 `d04eb429` (`loads.txt`).
- Every step ran on `6158aec`.

## Answer: one click opens both screens, between 1 and 3 s after the click

| Click | +1.2 s | +3.2 s | +6.2 s |
|---|---|---|---|
| Save Game, once | Options, with Save Game selected ("Save the current game") | **the Save Game screen** | the Save Game screen |
| Load Game, once | Options, with Load Game selected ("Load a saved game") | **the Load Game screen** | the Load Game screen |

- The state: slot 90 ("reg250") loaded, Icon Nine on the board before the fight. I waited 9 s on the board, pressed Escape, waited 4 s, then made one click (`board`, `save-0`, `save-1s` to `save-6s`).
- For Load Game: Cancel, then Close, back to the board (`board2`). Then the same steps, with one click on Load Game (`load-0`, `load-1s` to `load-6s`).
- The frame times are measured from the click, not slept (`times.txt`).
- The dev log reads "save scan: 36 saves in 1646 ms".

## Coder's questions

1. **The click helper**: `c.sh` moves the pointer in the app's window, waits 0.15 s, then makes one click. It uses `win.sh` to find the window. `k.sh` is the key helper. All three are in the folder, with `oneclick250c.sh`, the script for this check.
2. **Just before the save step**, on 8159056 the single click was seen three times. Each frame was taken 3 s after the click, and each showed Options with Save Game only selected:
   - The script's save step (the one that silently didn't save): slot 90 had just been loaded, with 9 s on the board. No fight and no popup. Escape, 2.5 s, then the click. 3 s later the script clicked the name field (636,954), which on Options is empty space.
   - `save-screen` (250u): a fight had just been won. I clicked OK on the XP popup, then 1.5 s later pressed Escape, and 2 s after that made the click.
   - `r-save1` (250u): slot 90 had just been loaded, 9 s on the board, Escape, 2 s, then the click.
   - `o2` (250u): on the board after a Table Rules try, Escape, 4 s, then the click.
3. **o2** was taken 3.1 s after the click: `sleep 3`, then a 0.1 s wait in my screenshot helper. The second click in 250u came 13 to 16 s after the first, with no frame in between.

## What this does and doesn't settle

- On 6158aec, one click opens the screen within 3 s. By MAIN's rule, that's a slow open, not a two-click bug.
- On 8159056, my frames at 3 s still showed Options. So either the open took longer than 3 s there, or something else changed between the builds. I took no frame later than 3 s on 8159056, so I can't say which. A rerun on 8159056 with these timings would settle it, if MAIN wants that.

## Odd, not filed

- The Load list's top row is an Auto Save. Its files in icons-185.marks (`autosave.png`, `autosave.world.json`) are dated 12:38:16, the same second as my Load Game click (12:38:16.442). So opening Load Game seems to write the Auto Save and its board picture. The mtime only shows the last write, so I can't say whether the Save Game click wrote one too.
