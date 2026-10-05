# TEST 156

Written for: Main and Coder. The Options screen, played as a player. Screenshots: `HANDOFF/BUILD/screens/test-156/` (35 images; paths below relative to it). Real game on Xvfb `:2`, K2 not launched. Compared by eye against `BUILD/screens/options-k2/` (in-game menu, main menu, feedback, graphics, exit prompt) and `docs/K2-PARITY-OPTIONS-PT2734.md`. Non-game steps: fixtures, listed at the end.

## Build

App `9c2b1c3c870f3676c24037df25e074d84285d776` (`git archive 9c2b1c3` into `/tmp/test156-build`, `flutter build linux --debug`, no `flutter create`). Lock Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = Lodestar HEAD = the pub-cache checkout it was built from (`.dart_tool/package_config.json`) = Coder's `e729d36`; no difference. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `b5c47683`, HANDOFF `dee6f0a`. `check_shelf` against my directory: 30 rules files, 105 blueprints, identical. App and Xvfb stopped by recorded PID.

## Summary (11 checks)

| # | Check | Result |
|---|---|---|
| 1 | In-game Options menu | **PARTIAL**: layout, closed-up rows, hover help and portrait footer present. Differences from your list: **no Gameplay row** (the parity table leaves it out), **Keyboard Shortcuts is extra** (kept by the owner, per the table); footer's left bracket missing, third companion tile clipped at the frame edge |
| 2 | Main-menu Options | **PASS** (Feedback, Graphics, Keyboard Shortcuts; no Save/Load/Exit, no footer, no icon row) |
| 3 | Left-out options absent | **PASS** for every screen I opened (nothing on the list appears anywhere in Options) |
| 4 | Hide Unequippable | **PASS for an organic**; **droid COULD NOT TEST** (my authored droid save was refused) |
| 5 | Floating Numbers | **PARTIAL**: ON shows a small red number over the player when hit and a small white "miss"; enemy wound number: none shown; **red edge flash NOT seen** in any captured frame. OFF shows nothing. See notes |
| 6 | Brightness | **PASS** (slider darkens/lightens the whole app; Default resets) |
| 7 | Persistence and Default | **Persistence PASS** (all three kept after an app restart). **Default FAIL: it resets every setting, not just its own screen** |
| 8 | Exit Game | **PARTIAL/FAIL**: prompt text PASS (no "progress will not be saved"). **OK does not quit the app**: it ends the session and lands on the package menu (app keeps running). Cancel returns to the Options menu, not to play. Continue afterwards resumes the same square (PASS) |
| 9 | Keys and focus | **PASS** (no leak from any Options screen; F4 and movement keys work straight after closing by Escape and by mouse). Note: arrow keys move the Graphics slider |
| 10 | The 155 leftovers | **PARTIAL**: Auto Save full area name PASS; ×2 gone PASS; package bar raw id gone PASS (bookmark rows); **Map screen still blank** FAIL |
| 11 | Text | **PASS** for the Options screens (no underscores, backticks, code names) |

## 1. The in-game menu — PARTIAL

`t1a`: rows **Save Game, Load Game, Feedback, Graphics, Keyboard Shortcuts, Exit Game**, closed up from the top, K2's 318-wide rows with the white hover outline, the icon bar, the help pane and Close. Against K2's capture (`k2-options-ingame-menu.png`): K2 has Gameplay, Auto-Pause and Sound too (ruled out), and its first row starts lower, under a taller title; ours starts at the top of the pane, which is what the parity table says K2's own main menu does. Window frame differs (listed as excused).
- **Hover help, every row** (`t1b`): Save "Save the current game", Load "Load a saved game", Feedback "Feedback Options", Graphics "Graphics Options", Keyboard Shortcuts the key list, Exit "Quit the game".
- **Your list says "Save, Load, Gameplay, Feedback, Graphics, Exit Game, Close".** There is **no Gameplay row** (the parity table's "left out" list names the Gameplay screen). I count that as listed, not a defect, but the two documents disagree.
- **Keyboard Shortcuts** is not on your list; the parity table keeps it as "ours". Its pane lists `arrows move`, `esc options — the one door out of every screen` and the other keys in plain words (`t2c`).
- **Footer** (`t1c`, `t1a`): portrait, name and class line drawn, with red-orange bar. Companion tiles in the footer show the **default art** (the same face for each, as the party has none). **Differences from K2's footer** (`k2-options-ingame-menu.png`): K2 draws curved bracket tabs on **both** sides of the portrait; ours shows only a plain line on the right and **none on the left**; with a party the **third companion tile is cut off by the window frame** (`t1c`). Not listed as excused.

## 2. Main-menu Options — PASS

From the package menu: Options opens **Feedback, Graphics, Keyboard Shortcuts**, a help pane, Close; no Save, Load or Exit row, no icon row, no footer (`t2a`). Feedback and Graphics look the same as in game.

## 3. Left out as ruled — PASS

On every screen I opened (in-game menu, main-menu Options, Feedback, Graphics, Keyboard Shortcuts) none of: Combat Difficulty, Auto Level Up, Mouse Look, Reverse Mouse Y, Mouse Settings, Mini-Game options, Mini Map, Subtitles, Tutorial Popups, Shadows, Grass, Force Speed Effects, Advanced Options, Screen Resolution, Key Mapping, Status Summary, Hide Quick Menu Buttons, any sound slider appear. Feedback has two rows (Hide Unequippable, Floating Numbers), Graphics one (Brightness) (`t2b`, `t6a`).
- **Sound:** you asked whether to add a Sound row now and build it later. The owner's PT-2734 ruling says leave it out and do not fake it; a row that opens nothing would be that. If Main wants it as a placeholder, I will test it that way.

## 4. Hide Unequippable — PASS (organic) / COULD NOT TEST (droid)

Onjo (organic; light armour only). Default is off. Ticked on (`t4a`): the Equip **body list** reads None / Light Combat Suit (Equipped) / Jedi Robe / Reinforced Fiber Armor, with **Jamoh Hogra's Battle Armor hidden** (`t4b`). Ticked off: it returns, with the **red-orange outline** (`t4c`). **Droid: COULD NOT TEST.** I authored a droid (`tee-three`) with a copy of the app's seed tool; the loader refused it (*"astromech is not a subrace or chassis that droid has. This character has no gender or voice and its species carries one"*, `dd` shot not kept); that is my fixture, not the app. Not run: a second organic or the droid-shield bed.

## 5. Floating Numbers — PARTIAL

Fixture: my `tester-save-bed`, Dressa (unarmed, 20 vitality). ON (K2's default):
- **Player hit:** a small **red "-1"** over Onjo's token (`t5c`, frame `t5a`). TEST-time rule from the parity table: "a small red number over the player's head".
- **A miss:** a small **white "miss"** over the token that was missed (over the player when Dressa missed, `t5d`; over Dressa when Onjo missed, `t5b`); it **rises a few pixels over ~5 frames**.
- **Enemy wounds:** Dressa took 6 and 8 damage from Onjo and **showed no number** (her health bar and the log carry it), matching the owner ruling.
- **Red edge flash:** **not seen.** I took 6+12 frames per enemy turn with no pause (≈0.15–0.3 s apart) on three turns; the pixels along all four viewport edges stayed pure black (0,0,0) in every frame. The parity table says the flash is "built from the K2 read" (up in ~3 frames, gone in ~8 at 30 fps, ~0.27 s). My sampling could miss one that short, but the number was caught in the same bursts, so I report it as **not observed**, not as absent.
- **Timing/colour:** the number is red `~(184,36,6)`-like, one digit tall, and gone by the later frames; I did not time it beyond the bursts.
- **OFF:** three enemy turns (Onjo went 10 → 9 → 7 of 10): the tick shows unchecked, **no figure and no "miss" in any frame**, and no edge flash either (`t5e`). So OFF also shows no flash. The brief's "does the flash stay" question: **it did not stay, because I never saw it ON either**; the parity table does not say it should stay.

## 6. Brightness — PASS

`t6a` default (thumb at the middle). Click the left end: the whole screen darkens (frame luminance 24 → 11, `t6b`); the right end: lifts to ~78 (`t6c`); Default: back to 24, thumb recentred (`t6d`). The dimming covers the main menu and the library after a restart too (`t7c`).

## 7. Settings persist; Default — persistence PASS, Default FAIL

Set Hide Unequippable ON, Floating Numbers OFF, Brightness to 0.104 (`settings.json`: `{"floatingNumbers":false,"hideUnequippable":true,"brightness":0.104…}`; `t7a`, `t7b`). Killed and relaunched the app: the library comes up dark (`t7c`) and the Feedback screen shows Hide ticked, Floating unticked (`t7d`).
- **Default FAIL, both ways, with the file as evidence.** Pressing **Default on the Feedback screen** with brightness at 0.104 made `settings.json` read `{"floatingNumbers":true,"hideUnequippable":false,"brightness":0.5}`: **the brightness went back to default and the screen brightened** (`t7e`). Pressing **Default on the Graphics screen** with Hide ticked (brightness 0.104) gave `{"floatingNumbers":true,"hideUnequippable":false,"brightness":0.5}`: **Hide Unequippable was un-ticked** (the file read `"hideUnequippable":true,"brightness":0.104…` immediately before). So **Default resets all three settings from either screen**, not "that screen only" (the work order, and K2's per-screen Default).

## 8. Exit Game — PARTIAL/FAIL

Exit Game: *"Do you really want to quit?"* with OK / Cancel, **no** "Your progress will not be saved" (`t8a`; K2's capture reads "…Your progress will not be saved.").
- **Cancel** → back to the **Options menu** (Exit Game row highlighted), not to play (`t8b`). K2's post-Cancel state is not in the captures.
- **Escape in the prompt** cancels the prompt only; the menu stays (`t8c`).
- **OK** → **the app does not quit**: the session ends and the **package menu** comes up (Continue / New Game / Load Game / Movies / Music / Options / Exit to Library), with the dim brightness applied (`t8d`, app still running by PID). The work order says OK quits. I take "quit" here to mean "leave the session", since the app has no K2-style process to exit from a package; **I may be wrong, so this is flagged for Main to rule.** Continue afterwards **resumes the same square** (3,4) with the same HP (`t8e`).

## 9. Keys and focus — PASS

Each screen opened separately, the 38-key sequence (Left×1, Right×3, a×7, d×12, Up×1, Down×3, w×7, s×12) sent, closed with Escape, and the play board compared with the board before (crop of the viewport): **0 differing pixels** for the in-game menu itself, Feedback, Graphics (after resetting brightness), Load Game, Keyboard Shortcuts and Save Game. Note: on the **Graphics screen the arrow keys move the Brightness slider** (thumb moved, whole screen dimmer; `t9a`), which is a key doing its job on the focused slider, not a leak, but it means Left/Right changed a setting. On the quit prompt the key sequence was not run to completion (the prompt opened over it).
- After **Escape** closes Options: F4 wrote `quick.mark` (16:31:53) and two Right presses moved Onjo. After **mouse CLOSE**: F4 and the same two Right presses worked again. No dead input in either path.
- Side finding: **sub-screen Close returns to the Options menu**, a second Close or Escape goes to play, which cost me wrong clicks twice.

## 10. The 155 leftovers — PARTIAL

- **Auto Save row read from the log, full area name: PASS.** A never-played Onjo shows *"TESTER SAVE BED"* over *"SAVE BED"* (`t10d`), TEST 155: "BED".
- **No "×2" on an item equipped once: PASS.** Five-party Mira Mourn: *Blaster Rifle (Equipped), Clothing (Equipped), Short Sword (Equipped), Frag Grenade ×2, Medpac ×2, Adrenal Strength* (`t10b`).
- **Package bar, no raw id: PASS.** The five-party bookmark rows now read **"0 AAA VISUAL PASS"** (`t10a`), not "tester-visual".
- **Blank Map screen: still FAIL.** Clicking the Map icon on the five-party game (and, by a wrong click, on Save Bed) opens a **black box with only the caption** *"map — ⟨Hall⟩"* (previously the raw id *"v01-hall"*; now the area's name) and nothing in it (`t10c2`, `t10c`). Escape closes it. The caption is fixed; the map is still empty.

## 11. Text — PASS

No code names, underscores or backticks on any Options screen. (Side: the **library card for "Droid Shield Bed"** shows a raw backtick fragment *"`d_…"* in its description; not an Options screen, not asked.)

## Fixtures I made (all in my own data dir, none on Shelf)

`packages/tester-save-bed` (from TEST 154/155), `onjo-bed.sav` and `vela-sorn.sav`, `five-party.sav` (Coder's tool), and `tee-three.sav` (a droid built from a copy of the app's seed tool; refused by the loader).

## What I did not check

The droid half of Hide Unequippable; the red edge flash with a faster capture than ~0.15 s (the viewer paints one frame late, so my frames are noisy); Floating figures for XP and healing (neither is built per the parity table); Escape inside the quit prompt with the key sequence; K2 side-by-sides pixel for pixel (read by eye); the main-menu Options' Hide/Floating screens against K2's.

Skills used: `verification-before-completion` (every result has a screenshot, a pixel diff, a file reading or a frame series; the Default fault is shown by `settings.json` in both directions; unrun items listed), `diagnosing-bugs` (a one-screen-at-a-time key test after my first run was invalid, reset-then-compare for Default), `research` (K2 captures, parity table and ledger first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
