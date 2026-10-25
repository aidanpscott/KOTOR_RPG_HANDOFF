# TEST 201 running log (draft, text only)

Started 2026-10-25. Known, don't file: rows 2 px long; red disc at load; no K2 capture of combat bar or container.

## Build
- Settings: no settings.json (defaults); brightness default. Shelf b2de52b (unchanged); every Shelf package in my data identical to it (sync check).
- App main 5e92c46, worktree builds/test201. Gate: "FOR TESTER — CORE at 5e92c46, 5143 tests, 0 failed, 14m03s at -j 3, peak 1829 MB"; "ARCHIVE last green at 5e92c46".
- Lodestar e1b6ed9 = lock = compiled; Lens 5fe60a9.
- Fixture specs201/tab.json: Tab Eleven (Consular 1, DEX 12, party-lock-bed).
- Build through the lock 10.0 s; pubspec.lock unchanged.

## 1-3. Typed reply — all PASS (Tab Eleven, party-lock-bed)
Warden: '1. [Interrupt.] Which deck is breached?', '2. [Continue.]' (full stop — item 2 PASS), '[Type a reply.]' unnumbered (item 3).
A: Tab, '50 credits' -> the field reads '50 credits'; still the first line (nothing picked).
B: backspace x10, 'x9' -> the field reads 'x9'.
C: Escape -> field empties to '[Type a reply.]', conversation stays; '2' -> [Continue.] -> 'Warden: This one. …', '1. [Leave.]'.
D: click on the row, '1' -> the field reads '1'; BackSpace -> empty; '1' -> [Leave.] -> play.
Escape with the field unfocused (Engineer), twice: conversation stays open.
(w-0, a-typed, b-typed, c-esc, c-2, d-click1, d-empty, d-1, e-esc2)

## 4a. Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), walk, 3 Spaces, Messages > Combat: Rounds 1-3 identical to TEST 185. (dice/combat-tab, combat.txt)

## 4b. Regression (Icon Nine) — PASS
reg200 loaded; Save > New Slot '37 : reg201' (10:53:43); Escape then F4: one quick.mark (10:53:48); Load lists Auto, Quick, '37 : reg201'; loaded reg201 at the start; a fight to its end: total-defeat popup. (reg/load-list, reg/start, reg/end)
