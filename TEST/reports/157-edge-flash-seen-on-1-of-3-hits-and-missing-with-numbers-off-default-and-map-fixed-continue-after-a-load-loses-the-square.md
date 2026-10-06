# TEST 157

Written for: Main and Coder. Re-run of TEST 156's faults and partials. Screenshots: `HANDOFF/BUILD/screens/test-157/` (22 images). Real game on Xvfb `:2`, K2 not launched. Non-game steps: fixtures (end) and ffmpeg screen recording.

## Build

App `6a5f715c9cd79631e8d8bd0932517f8a8567d73d` (`git archive 6a5f715` into `/tmp/test157-build`, `flutter build linux --debug`, no `flutter create`). Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = the lock = the pub-cache checkout it was built from = Coder's `e729d36`; no difference. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `3f7439c3`, HANDOFF `8888146`. `check_shelf` clean (done at 156's setup, same Shelf). App and Xvfb stopped by PID.

## Summary (7 checks)

| # | Check | Result |
|---|---|---|
| 1 | The red edge flash on a real hit | **FAIL as asked**: seen on **1 of 3** hits; absent on the other two; at ~1/6 the strength the parity table gives; **OFF: the flash did not appear** (one hit). The red number shows on every ON hit that I could watch to the end |
| 2 | Default resets only its own screen | **PASS** (settings.json after each) |
| 3 | The Map screen draws the area | **PASS** (Save Bed and the five-party Hall) |
| 4 | The footer | **PARTIAL**: left bracket tab present, nothing clipped; with 5 members it shows leader + 2 (not 2 total); K2 side unknown |
| 5 | Hide Unequippable on a droid | **PASS for a weapon**; body/arm/head lists show only None either way (see note) |
| 6 | Droid Shield Bed card | **PARTIAL**: backticks gone, but `d shield 01`, `baseitems Droid Shield` and PT numbers remain |
| 7 | Quick regression | **PARTIAL**: Options open/close, Save, Load, no key leaks, Exit → Continue (without a load first) PASS; **Continue after loading a bookmark puts the party back on the arrival square FAIL** |

## 1. The red edge flash — FAIL

Method: `ffmpeg -f x11grab -framerate 60` of `:2` at 1920×1080, lossless-ish (`qp 12`, `yuv444p`), key press 1.5 s in, 5 s long; frames cut out with their real timestamps (16.7 ms apart). Fixture: `tester-save-bed`, Onjo (10 vitality) against an unarmed Dressa; each recording is one *space* press = end of my turn = one Dressa attack. 29 recordings, 5 of which contained a hit. Frame times below are from the video clock (key at ≈1.5 s).

| Hit | HP card changes | Red number over Onjo | Edge bands |
|---|---|---|---|
| V4 (ON) | 2.667 s | 3.300 → 4.133 s (0.83 s) | **none** in any frame |
| V6 (ON) | 2.700 s | 3.133 → 3.733 s (0.60 s) | **none** |
| V7 (ON) | 2.617 s | 3.550 → 4.483 s (0.93 s) | **yes**: 3.550 → 4.483 s (**0.93 s**, 57 frames), appears and disappears **in one frame** (a step, no fade), top and right edges and a band above the log; stays flat through the whole interval (`t1a`: before left, 3.7 s right) |
| V9 (ON) | 3.533 s | not visible before the clip ended | none before the end of the clip |
| V29 (**OFF**) | 2.950 s | **none** | **none** (`t1d`) |

Notes:
- **1 of 3 usable hits shows the flash.** The two without it show the number. Damage was the same (1) on V4 and V7, so I cannot tie it to the roll. The effect (number and flash) appears 0.65–0.93 s **after** the HP card changes, not with it.
- **Strength:** at its peak the band's red excess is R 9 on 0–255 at the top and 6 on the right (R−G), against the parity doc's "~+55 red along the bottom, ~0.34 alpha" and "up in ~3 frames, gone in ~8 (~0.27 s)". Ours is **a fraction of that strength and ~3× longer**, and has no ramp.
- **OFF:** one hit; HP card 4 → 3, log line shows the hit; **no number and no flash** in a recording that covers 4 s after it (`t1d` is the final frame, HP 3 of 10). You expected the flash to stay ON for now: **it did not stay.** One hit is a small sample; I could not get more (Dressa missed in 22 of 23 other turns).
- The video files were deleted after analysis; the analysis scripts are in `~/kotor-tester/run/ana*.py` (not committed).

## 2. Default resets only its own screen — PASS

Settings low brightness, Hide ON, Floating OFF. settings.json after each step:
- Set: `{"floatingNumbers":false,"hideUnequippable":true,"brightness":0.104…}`
- **Feedback → Default:** `{"floatingNumbers":true,"hideUnequippable":false,"brightness":0.104…}` — Brightness untouched (`t2a`).
- Re-tick Hide: `{"floatingNumbers":true,"hideUnequippable":true,"brightness":0.104…}`
- **Graphics → Default:** `{"floatingNumbers":true,"hideUnequippable":true,"brightness":0.5}` — Hide untouched (`t2b`).

## 3. The Map screen — PASS

Opened by the **Map icon** in the top bar and by the **M key** (play view; nothing happens if M is pressed with the Options menu already open). It now draws the area, not a black box: the 12×8 grid, the party token (white), enemies (orange-red), the door (gold square) and a caption *"map — ⟨Save Bed⟩"* (`t3a`, `t3b`). The five-party Hall draws the five party tokens in teal and the enemy (`t3c`). Escape closes it. Observations: the Map screen has **no icon bar** (you cannot reach another screen from it); the arrival square ("in") is not marked.

## 4. The footer — PARTIAL

- **Left bracket tab: present** (`t4a`): the curved tab sits left of the portrait with a line rising at its left edge. Same for the five-party game (`t4b`).
- **No clipped tile:** with the five-party game the footer shows the **leader plus two companion tiles** (right side), all inside the frame (`t4b`). TEST 156's clipped third tile is gone, but it is **three people shown of five**, not "limited to 2 members" as you wrote; the leader is not counted in Coder's 2, I read it. The two tiles are the same default face.
- **K2:** `options-k2/k2-options-ingame-menu.png` shows a **solo party** (T3-M4 alone) with both tabs empty. So K2's capture does not show two companions; I cannot say K2 shows 2.
- **Footer with a droid** (`t5…`): the portrait is a flat teal box (no art), and the Load row of the same droid shows a **human male face** (`t5a`, `t5e`).

## 5. Hide Unequippable on a droid — PASS for a weapon

Fixture: Coder's droid (`tool/author_droid_save.dart`, Tee Three, Scout, astromech) **plus seven items added by a copy of that tool** — the original has an empty bag. Hide **OFF**: the weapon-slot list offers **Blaster Pistol: Null** outlined **red-orange** (`t5c`). Hide **ON**: the same list shows only None (`t5d`). 
- The droid's **body, head, belt and arm lists show only "None" with Hide OFF too** (`t5b`): the body list does not offer Jedi Robe, Reinforced Fiber Armor or Jamoh Hogra's armour even with Hide OFF, so the wearer filter (TEST 149/151) removes organic armour before Hide matters. So "organic armour hidden / red-orange" cannot be shown on a droid; the working half is the weapon list.
- My first attempt failed because the app reads saves only at launch; I restarted it after writing the save.

## 6. The Droid Shield Bed card — PARTIAL

The raw backtick fragment is gone, but the card (`t6b`) reads *"A TEST FIXTURE, NOT A CAMPAIGN (PT-2725, TEST 149): one merchant whose stall sells a DROID-ONLY shield (Droid Deflector Mark I, **d shield 01**, baseitem…"*: the underscores were replaced by spaces, so **`d shield 01` is still an item id**, and `baseitems Droid Shield` and `PT-2725, TEST 149` follow in the cut-off part. The other cards (`t6a`, 10 viewports, all 22): several keep **PT numbers and "§10"** ("A fixture for PT-1713/PT-1715/PT-1716's three-layer droid melee gate", "ACTION-ECONOMY-01 §10", "PT-2566/PT-2568") and **"Tester Strongroom" has no description at all**. No backticks anywhere. I count the PT numbers as raw ids; Main may rule they are fixture prose.

## 7. Quick regression — PARTIAL

- Options opens and closes by Escape and by the mouse: PASS.
- **Save** (New Slot, name REGR, OK; bookmark 16) and **Load** (REGR from the Load list; the party comes back where it was, `t7b`): PASS.
- **No key leaks:** 38 keys with the in-game menu, Feedback and Keyboard Shortcuts open: the board is pixel-identical afterwards. On Graphics the arrow keys move the Brightness slider (the screen dims/brightens), as in TEST 156.
- **Exit Game → OK → package menu → Continue → resumes the same square:** PASS when I had not loaded a bookmark before leaving (`t7d`: Mira on (0,2) before and after).
- **FAIL — Continue after a bookmark load.** Steps: (1) load the five-party game; (2) Save as REGR with Mira on (2,3) (`t7a`); (3) walk elsewhere; (4) Options → Load Game → REGR → Load (Mira back on (2,3), `t7b`); (5) Options → Graphics (38 keys) → Close; (6) Options → Exit Game → OK; (7) package menu → Continue. The party comes back on the **arrival square (0,1)** with Mira on the door, not on (2,3) (`t7c`). `autosave.world.json` had `"at":[2,3]` and `"logLen":63`, so the position was written; the load ignored it. **Likely cause, not shown:** the autosave's log-length check rejects it after a load (a load appends a rewind event, so the log is longer than the autosave's). It passed in TEST 154 because no bookmark had been loaded before leaving.
- **Load list at first open, double outline:** after Options → Load Game the first row (REGR, selected) and the row under the mouse (15) both had the bright outline (`t7a`); the panel showed REGR. It resolved when the mouse moved; minor and may be hover versus selection.

## Fixtures I made (my data dir, none on Shelf)

`packages/tester-save-bed` (Dressa, trooper, door, quest reply, "Draw your blade"), `onjo-bed.sav`, `five-party.sav` (TEST 155's), `tee-three.sav` = Coder's droid tool + a copy that adds seven carried items (`jedi-robe`, `reinforced-fiber-armor`, `jamoh-hogra-s-battle-armor`, `insulated-gloves`, `blaster-pistol-null`, `cardio-regulator`, `frozian-scout-belt`).

## What I did not check

A fourth ON hit with the flash after the first 3; the flash with Floating Numbers OFF on more than one hit; the footer of a droid with a companion; K2's own footer with a party; Hide Unequippable for a second organic.

Skills used: `verification-before-completion` (each number is a timestamp, a settings.json reading or a pixel measurement; the small sample for OFF is stated), `diagnosing-bugs` (frame-by-frame 60 fps capture with real timestamps, a control hit for each state, two-step repro for the Continue fault), `research` (parity table and the ledger first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
