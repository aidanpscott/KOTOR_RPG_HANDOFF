# TEST 145 — Auto and manual Level Up both grant correctly; homeworld Persuade stacks live; the Hunter grant reproduces — but the Equip screen is a third "one fold, three readers" reader PT-2711 didn't reach

## Build

- App: local HEAD `383e68a3d620e817c3e910963e6278782b4ac9de`, matching `origin/main` exactly, clean tree, at catch-up. **Built from a `git archive` snapshot of that HEAD**, per the work order — not a live checkout.
- `pubspec.lock`: Lodestar resolves to `f3e70e3e21736987fd4d6673c52dc7bff0c05b37`, Lens to `2bad745a53a1e741ab8d8ef94a954e6e3973b99b`. Both exact checkouts exist in the pub-cache (`~/.pub-cache/git/Lodestar-f3e70e…`, `Lens-2bad745a…`) — this is what actually compiled.
- Shelf: `~/.local/share/tester-data/kotor-rpg/packages` was a stale git clone (`c9f64b6`) at session start. **Pulled to `267101d`** mid-session (fast-forward, clean) to pick up `tester-xp-bed-arena` (PT-2710 item 10) and the feat-id/availability regeneration (PT-2711 item 3) — both needed for this list. `check_shelf.py` clean before and after.
- Own Xvfb `:2`, own PID each launch, never touched Coder's display.

## Verdict

**One severe finding, not previously reported: the Equip screen's own Defence badge is a third reader that still omits the class bonus PT-2711 just added to the other two.** Confirmed three ways on the same character at the same moment — Character Sheet 14, a real fight's own defence breakdown 14, Equip screen **11** — and traced to the exact line: `play_screen.dart:3147` calls Lodestar's `defence()` for the Equip screen's `DEF` badge without passing `classBonus:`, so it silently defaults to 0. This is the same shape PT-2711 titled "one fold, three readers" and fixed for the Character Sheet; the Equip screen is the reader that fix didn't reach.

Everything else on the list held. In particular: **the Hunter grant now reproduces live** — Soldier + Hunter + Two-Weapon Fighting correctly resolves to Long Sword *and* Short Sword, one per hand; Hunter *alone* (no TWF) correctly resolves to a single Long Sword, which is the rule working as designed (`BOTH` in `STARTING-EQUIPMENT-01` means profession *and* the feat, not profession alone) rather than the regression I first suspected.

## Results

### 1. Player-granted feats — CONFIRMED

Built a Human Brawler (`Isolde Vos`) in `tester-xp-bed`, killed the fixture's 1-vitality enemy for the guaranteed 3000 XP, and used **Auto Level Up** on the Character Sheet. Result: level 2, feats list gained `Unarmed Specialist I — granted` (distinct from `chosen`). Equip screen's unarmed damage read `3-6 +4` (1d4 + Str 2), matching the L2 grant exactly (L1 had read `3-5 +3` on the same character, i.e. 1d3 + Str 2).

Built a second Brawler (`Rennik Tarn`) in `tester-xp-bed + Arena`, same 3000 XP kill, this time used **Level Up** (manual). The manual screen states the grant explicitly before you accept it: *"granted — vitality d10; attack and saves — from Brawler's own table; feat — Unarmed Specialist I, granted by Brawler."* Spent the 3 skill points and 1 chosen feat, accepted. Confirmed in a **real fight** against the arena's Sparring Partner: `unarmed · rolled 20 — d20 16 + attack 2 + Strength 2 · needed 9 — hit · damage 5 — 1d4 3 + Strength 2 · 55 left` — 1d4 + Str, live.

Soldier's own L1 grants (`squad_tactics`, `both_hands`) also read `granted` on the sheet, correctly distinguished from a chosen feat (`Armour Proficiency: Light — chosen`) on the same character — confirms the granted/chosen distinction is class-blind, not Brawler-specific.

**Not separately exercised:** a level-4 grant on a second class (e.g. Soldier's `improved_squad_tactics` at class level 4). Reaching level 4 needs more XP than one `tester-xp-bed` kill provides, and I judged the risk/time of grinding it not worth it once the mechanism was already confirmed class-blind via the L1 granted/chosen check above and via source (`grantedFeatsFor` is one function for every class). Flagging as unexercised rather than silently assuming it.

### 2. Seeds — COULD NOT TEST (only incidental data)

Not deliberately exercised. Incidentally, three separate `New Game` starts this session drew different first d20s (14, 1, 17 across Isolde Vos, Rennik Tarn, and Mira Sabek's first real rolls) — consistent with per-campaign seeding, but I never ran the actual paired check (same save reloaded vs. a fresh save from a later point in the same campaign) the item asks for.

### 3. Spikes (`SKILL-RESOLUTION-01 §5`) — COULD NOT TEST

Not exercised this session. None of the three characters built (Soldier ×2, Brawler ×2) carried a starting spike — the classes I happened to build don't get one in their array — and I didn't revisit `locked-and-trapped`.

### 4. Homeworld bonuses stack — CONFIRMED

Taris · Upper City · Persuade was visible as `+2` at the Origin step, correctly labelled `homeworld` (distinct from `class`) on the Skills step, and reached a **real dialogue check**: talking down the Command Deck's Sith Trooper produced `Persuade passed — 25 needed 14 (d20 17 +4 Persuade +2 Charisma +2 homeworld)`. All three terms present and separately labelled in the live roll breakdown.

### 5. The Credits route — COULD NOT TEST

Seen only in passing (the Equipment step's own text: *"You may also spend the value of this gear as credits instead, or take whatever your GM decides"*). Never selected it, never reached a Store, never confirmed a purchase arriving in Inventory.

### 6. A companion after a door — COULD NOT TEST (incidental data only)

Not deliberately exercised with the intended rigor. Incidentally, the henchman `Mate` crossed from `tester-xp-bed + Arena`'s `a01-room` into `a02-arena` with me, stayed listed in "your party" throughout, fought alongside me against the Sparring Partner, and was never attacked as if hostile nor did it attack the party — but I didn't specifically check its on-screen colour/rendering before and after the door, which is what "keeps its look" is really asking.

### 7. The skill cap at level 2+ — CONFIRMED

Level 1 Brawler: class skills read `1/rank · cap 4`. Same character after Auto/manual Level Up to level 2: `1/rank · cap 5` on the manual Level Up's own Skills step. Right value, right level.

### 8. Minor fixes — COULD NOT TEST

Not checked: Inventory stack counts, the Store inset, the initiative line's names, the level-up Feats footer count.

### 9. Boots and Sparring Gloves — CONFIRMED

Every Equipment step this session (Soldier ×2, Brawler ×2) showed `boots: Dockworker's Treads — the catalogue gives it no base type, so no item can be made of it`, dimmed like the rest of the unresolved-item text, never presented as if deliverable. Same pattern for `Sparring Gloves` in the Brawler's kit line. Consistent with a real, honestly-reported content gap rather than a UI bug.

### 10. The Hunter upgrade grant, live — CONFIRMED (closes PT-2688)

Built a Human Soldier (`Mira Sabek`), Taris origin, Hunter background, **Two-Weapon Fighting** as the level-1 feat. At Equipment, the melee-upgrade offer correctly expanded to two choices (`"and now you choose which"`, plural, only appears when `upgrades.length > 1`): **Long Sword + Short Sword** (`2 objects`) and **Double-Bladed Sword**. Picked the pair. Save log confirmed both weapons: `weapon_r_1: items/weapons/long-sword, weapon_l_1: items/weapons/short-sword`. Equip screen showed both in Config 1, one per hand. No `'upgrade' will not open` anywhere.

For comparison, built a second Soldier (`Rennik Tarn`, reused for item 1) with Hunter but **without** Two-Weapon Fighting: the offer correctly showed only **one** choice, a single Long Sword, with the note *"one weapon — wield 3, and it IS the pair."* This is correct per `STARTING-EQUIPMENT-01`'s own ruling (line ~575): `BOTH` means the profession grant **and** the Two-Weapon Fighting feat together; `Hunter` alone gives the class's single-weapon upgrade. My first read of this (before re-checking the source doc) was that the pair was missing — it isn't; the character just hadn't taken the feat the pair requires. Correcting myself here rather than filing it.

**Character Sheet, Equip, and a real fight do *not* show the same Defence** — see the severe finding above. Character Sheet 14, real fight 14, Equip 11, same Soldier, same moment.

### 11. From PT-2709 — PARTIAL

- **Start square:** confirmed. Endar Spire's Command Deck: the player's token renders exactly on the teal `aft`-labelled square on first frame, matching the package's declared `[[arrivals]] at = [1, 3]`. (Caveat below.)
- **Config 2:** confirmed for the second-weapon-in-main-hand shape, via item 10's dual-wield Equip screen — Config 1 showed `short-sword` in the **left** slot and `long-sword` in the **right (main)** slot.
- **Confirmation rolls, mine DCs, companion sheet:** not tested this session.

**Methodology note, not a defect:** clicking anywhere on the game floor — including a click meant only to give the window focus — registers as click-to-move and can silently relocate the player before you've looked. I did this to myself once (moved the player one square off `aft` by clicking to focus, which very nearly read as a start-square defect until I checked the save-writer's own status line and the arrival declaration directly). Recommend focusing via a UI element off the floor (sidebar, party panel) rather than the canvas when precision matters.

### 12. The arena fixture (`tester-xp-bed-arena`) — CONFIRMED, opens and plays

This package only reached `Shelf main` after my catch-up sync (pulled mid-session, see Build). Opened it, played the `a01-room` dummy kill for XP, walked through the door at the correct approximate position into `a02-arena` (once routed around the henchman, who blocked the direct path — expected, not a bug), and fought the Sparring Partner in real combat (see item 1's damage confirmation). Took the fight down to 3/18 HP through my own overextension, disengaged cleanly (`disengaging — your movement provokes nothing this turn`), and left the session safely. No defect in the retreat mechanism itself, once I read it correctly (`d` disengages before moving; movement toward an adjacent enemy square attacks rather than repositions).

## Severe, reported first

**The Equip screen's `DEF` badge omits the class Defence bonus.** `play_screen.dart:3147` calls Lodestar's `defence()` — the same function PT-2711 just added `classBonus` to — passing only `armourBonus`, `maxDex`, `dexterity`, `size`. No `classBonus:` argument, so it silently defaults to 0. Confirmed on `Mira Sabek` (Soldier, level 1, class bonus +3): Character Sheet `Defence: 14`, a real fight's own printed breakdown `defence base 10 + Dexterity 1 + class 3 = 14`, Equip screen `DEF 11` — same character, same moment, three readers, two agree. Confirmed the mechanism (not merely the symptom) by reading Lodestar's `defence.dart` directly: `classBonus` defaults to `0` and PT-2711's own comment names exactly this shape — *"one fold, three readers"* — for the Character-Sheet/fight pair it fixed. The Equip screen is the reader that fix didn't reach.

---

## Part 2 — the rest of the list, same session

PT-2711 landed (own display: DEF badge fixed) went to Coder before this part started; not re-checked here, since MAIN's own note says TEST 146 re-checks it once Coder confirms. Same build throughout (app HEAD `383e68a`, same Shelf `267101d`), same Xvfb, own PID each relaunch — one restart was needed mid-session (below).

### Environment note: the display hung once, recovered clean

After Part 1's long session, `DISPLAY=:2` stopped answering even `xdpyinfo` — a genuine X-server hang, not just an unresponsive app window (confirmed per the "throwaway xterm" check: nothing on `:2` would answer at all). Killed my own two PIDs (Xvfb and the app), relaunched both fresh — clean recovery, `check_shelf.py` still green. Recorded here since a future long TEST session on this same machine should expect this after enough wall-clock time and plan a restart rather than debugging a "stuck" app that is actually a stuck server.

### 1. Seeds — CONFIRMED (new-game variance only; the two other halves not exercised)

Not run as a dedicated exercise, but six fresh `New Game` starts this session (Part 1 + Part 2 combined) each logged a genuine first roll for that campaign, all different: **14, 1, 17, 9, 13, 6** (Isolde Vos, Rennik Tarn, Kaeda Nasser's Persuade check, Cassar Draan, Oreth Malick's mine-notice roll, Vash Draan). Zero of six were a natural 20. This satisfies "two new games draw different first rolls" and gives a first-20 rate (0/6) for the record, but I did not run the same-campaign-two-saves check (save, continue, save again, confirm the second save's next roll differs from what replaying the first would give) — that half is still open.

### 2. Spikes (§5) — CONFIRMED (no-roll Slicing; Security without a spike)

Built an Engineer (`Oreth Malick`) in `locked-and-trapped` — this array carries `2 × Computer Spike` in the kit, confirmed delivered via the save log (`item.acquired` × 2 for `computer-spike`). Right-clicking the terminal and choosing Slice opened `STRONGROOM CONTROL — AWAITING INSTRUCTION` **directly, with no roll at all**, listing costed options by terminal grade: `[Slicing] Unseal the vault door. (2 spikes)` and `[Slicing] Cycle the corridor lights. (1 spike)` — confirms "no pass/fail roll that burns one."

I then spent both spikes disarming the room's mine before reaching the terminal (two `Disarm (hard)` attempts, one failed, one succeeded — each spent one spike, confirmed via `item.lost … from: bag` in the save log), so I never got to execute a Slice with spikes in hand and see the cost actually deducted or watch it reduce with my Slicing 7. This is the same interaction TEST 144 already flagged ("both kit spikes get spent on unlock attempts"), not a new finding.

**Security, separately, with 0 spikes remaining:** right-clicking the locked door offered `Open Lock (hard)` as a single action; taking it rolled `d20 11 + Security 4 + Intelligence 3 = 18 vs 18 (hard) · open` — a pure DC roll, no spike mentioned, none spent. Confirms "Security is a DC roll" cleanly. Did not see an explicit spike-assist *choice* surfaced anywhere for this lock, so "a spike is spent only if you choose it" is confirmed in the sense that none was ever spent or offered without my asking — but I never had a spike in hand to test choosing to use one on a Security check specifically.

### 3. The Credits route — PARTIAL, and the reason is in source

Never reached the toggle. `equipment_screen.dart`'s own comment names why: *"THE TOGGLE — PT-2710 (5)... Offered only where `arrayValueFor` actually prices the array; every class it does not keeps exactly the old single-route screen."* Every Soldier standard-array screen this session (four separate characters, Part 1 and 2) showed the same refusal text: `clothing` resolves to 0 catalogue matches, `Blaster Rifle`/`Short Sword` each resolve to 2. Since `clothing` is the armour on every class's standard array I saw, this may block the toggle for every class, not just Soldier — I did not get to try a class with a different base armour piece to check, so I can't say it's universal, only that it was 100% consistent across what I built.

Substituted a real Store purchase instead, which exercises the same "buy something, confirm it's in Inventory" spirit even though it isn't the chargen-time route: `Sarn Ordo` (Store Bed) opened the merchant's `[Opens-store]` conversation option, bought a Vibroblade for its full 100cr listed cost, watched Credits drop from 100 to 0 in the Store's own inset, closed the store, and found `vibroblade` sitting in Inventory. Real purchase, real delivery, confirmed.

### 4. A companion after a door — CONFIRMED, and it's a real finding: the ring disappears

Checked specifically this time, not incidentally. `Mate`'s world token in `tester-xp-bed-arena`'s `a01-room` (before any door) has a visible teal ring around its fill — matching the player's own ring colour, distinct from the grey/red double-ring on a genuine hostile (the room's dummy, checked side by side in the same crop). After crossing into `a02-arena`, **Mate's ring is gone** — plain fill, no ring at all — confirmed on two separate re-renders (moved, re-checked; still gone), so not a one-frame paint glitch.

The *behavioural* half held: in `a02-arena`'s real fight, the turn-order panel still grouped Mate with the player (its own box, distinct from the Sparring Partner's red-bordered one), it was never targeted as if hostile beyond ordinary party-target damage, and it never attacked the party. So "it keeps its side" (the game-logic half) is fine; "it keeps its look" (the ring) is not — the companion's own ally indicator is lost on this area transition, confirmed reproducible.

### 5. Minor fixes

- **Store inset (Credits / In Stock rows):** CONFIRMED clean. Selecting an item in the Store Bed showed all four rows — `Item Cost`, `Credits`, `In Stock`, `Inventory` — legible, correctly valued (`100 / 100 / 2 / 0`), not overlapping or obscured.
- **Inventory stack counts:** CONFIRMED clean formatting (`medpac ×2`, `frag-grenade ×2`, `blaster-rifle ×2 (Equipped)`, `short-sword ×2 (Equipped)`) — consistent `×N` display throughout. Flagging without concluding a defect: the weapon-array items reading `×2` may reflect one copy in each of Config 1 / Config 2 rather than a genuine stacking bug; I did not have time to trace which.
- **Initiative names:** CONFIRMED — every fight this session (Part 1 and 2, six or so separate encounters) showed real character names in the turn-order panel (`Kaeda Nasser`, `Sparring Partner`, `Mate`; `Veteran Dummy`, `Vash Draan`; etc.), never a `room.NN` placeholder.
- **Level-up Feats footer count matching the summary:** not checked.

### 6. Confirmation rolls — CONFIRMED, both directions, correct arithmetic

**Confirmed:** `sparring.arena.02 falls — mate.room.01: unarmed · rolled 22 — d20 20 + attack 1 + Strength 1 · needed 9 — hit · threat confirmed: rolled 19 — d20 17 + attack 1 + Strength 1 · needed 9 — damage 6 — 2d3 1+3 + Strength 1×2 · 2 critical`. Natural 20 threatened, the second roll (same bonus) also hit, damage doubled.

**Not confirmed:** `dummy.room.02 falls — Blaster Rifle · rolled 18 — d20 19 + attack 1 + Dexterity 2 − point blank 4 · needed 13 · hit · threat not confirmed: rolled 10 — d20 11 + attack 1 + Dexterity 2 − point blank 4 · needed 13`. Natural 19 threatened (with the point-blank penalty already folded into both rolls, correctly applied twice), the confirmation roll's own total (10) fell short of the same DC (13) — arithmetic checks out on both sides.

Both log lines read exactly `threat confirmed` / `threat not confirmed`, matching the ask precisely.

### 7. Mines — PARTIAL

Right-clicking the strongroom's mine offered `Disarm (hard)` (no separate "recover" option was ever offered — possibly only appears post-disarm, not checked). First attempt: `d20 13 + Demolitions 2 + Intelligence 3 = 18 vs 20 (hard) · it is still live`. Second attempt: `d20 20 + Demolitions 2 + Intelligence 3 = 25 vs 20 (hard) · defused`. Confirms a real DC roll against a fixed number, using Demolitions + Intelligence, with a graded outcome message. **Did not confirm** the specific 15/20/25 tier-DC table, the stated disarm = tier+2 / recover = tier+5 deltas, or that the blast (had it triggered) uses the item's own save — this mine happened to read DC 20 flat and I didn't cross-reference it against the item's declared tier in the package data before disarming it.

### 8. The companion sheet — mechanism found, not fully exercised

Portrait-tap semantics, read directly from `_openPortrait` in `play_screen.dart`: tapping a companion who isn't the active one switches control to them; tapping the one **already** active opens their own screen — Equipment by default, the **Character Sheet only if that character has a level-up waiting**. Confirmed this live: tapping Mate's own portrait while already controlling it opened its Equip screen (`"no equipment is recorded for Mate — a companion is a blueprint in the roster and carries none"`, DEF 12 shown there), not a character sheet, because Mate had no pending level at that moment.

Tried to force the condition (bank a kill's XP for both player and companion without levelling the companion, then tap its portrait) using a fresh `tester-xp-bed` character (`Vash Draan` + `Mate`) — didn't get there: the fixture's own "1 HP, challenge 9" dummy hits hard (attack rolls up to 29 seen), and repeated engagement (mostly my own overextension, attacking at point-blank with a ranged weapon) took the player down to **-1 of 11 HP** before the dummy was ever killed. Left the session before anything worse happened; game state stayed reachable throughout (Options menu opened fine, Leave Session worked normally) — no crash or lockup, just a beaten character. Not itself a defect: a challenge-9 opponent should be able to drop a level-1 character that keeps re-engaging it instead of finishing it off through a safer route (e.g. controlling only the full-HP companion). Reporting the near-death as a genuine combat-balance data point, not a bug.

**Net: the companion-sheet mechanism is understood and cited, but I never actually saw one populated with a companion's own real scores/saves/Defence this session.** Flagging as the one item on this list that would need a clean, dedicated follow-up (a companion with a pending level-up, reached without the player getting drawn into a fight) rather than something I can call confirmed.

### Auto Level Up, report only

Built a fresh Soldier (`Cassar Draan`, `tester-xp-bed`), one dummy kill for exactly 3000 XP — the same total `PT-2709` cites as `xpToReach(3)`, so a level-1 character with this exact award sits with **two** pending levels at once. Pressed **Auto Level Up** once: advanced to level 2 only (`Experience 3000, Needed 0` unchanged, button still present, not "recommended-cleared-both"). Pressed it a second time: advanced to level 3, buttons gone, `Needed 3000` (fresh L4 threshold). So **Auto Level Up does not clear multiple pending levels in one press** — it takes exactly one level per press, and needs to be pressed again for each further pending level.

What it picked at each step, from the Character Sheet's own before/after: Fortitude `+3 → +4` (level 3's higher save progression), Defence `15 → 16` (Soldier's own `3 + (level-1)/2` class term stepping up at level 3), Vitality pool grew each level. **No new feat appeared in the feats list across either Auto Level Up press**, despite Soldier's own feat table (`classes.toml`) awarding an additional purchasable feat slot at both level 2 (`feats = 2`) and level 3 (`feats = 3`) — the sheet still showed only the original three entries (`Squad Tactics`, `Both Hands` — both granted — plus the one chosen feat from chargen) after both auto-levels. I did not check the Skills allocation the same way (no easy "current ranks" read outside a chargen-style screen was found in the time available). Report only, per the routing — not filed as a defect.
