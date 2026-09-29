# TEST 142 — first cloud pass: the environment holds; the player never keeps kill XP, and a companion's level does not survive a load

**⚠ SEVERE, sent to Main ahead of this report: the player never gains XP from a kill.** It was confirmed on
three separate characters. A companion's level-up is also lost on every load, and the Level Up button is
offered again afterwards. Both are in §4.

## Build

```
environment             cloud container (first Tester run off Aaron's PC)
flutter                 3.47.5 stable · Dart 3.13.4 · /opt/flutter
app HEAD                87fb906619ba0187d167ccf9a12a367613d3aa9e
                        "Build the class-granted-feat pipeline; revert Unarmed
                        Specialist's level-only shortcut"
snapshot                `git archive HEAD` → ~/tester-build (no working tree used;
                        the fresh clone had no local changes anyway)
linux/                  absent from the archive (gitignored), so recreated with
                        `flutter create --platforms=linux .` (same as TEST 140/141)
pubspec.lock resolves   lodestar 496d5e79088e5fbc2160ce4cb60da86a5d813594
                        lens     2bad745a53a1e741ab8d8ef94a954e6e3973b99b
pub-cache checkout      ~/.pub-cache/git/Lodestar-496d5e79…  `git rev-parse HEAD` = 496d5e7 ✓
                        ~/.pub-cache/git/Lens-2bad745…  present ✓
                        pubspec.lock byte-identical after `pub get` ✓
dependency_overrides    NOT needed: the private git deps resolved through the proxy
build                   `flutter build linux --debug`, clean
```

**Environment**

- **Data directory:** `XDG_DATA_HOME=$HOME/tester-data`, so the real content lives at
  `~/tester-data/kotor-rpg/{packages,saves,console}`. `packages/` was seeded by `git archive` from
  `Shelf` 005a2fc (16 packages). The first save landed at
  `~/tester-data/kotor-rpg/saves/cloud-soldier.sav`. The default `~/.local/share/kotor-rpg` was never
  created.
- **Display:** my own `Xvfb :2`, 1920×1080. There's no window manager, and the app window is 1280×720 at
  0,0. The app and Xvfb were both killed by their recorded PIDs at the end.
- **Input:** `xdotool mousemove --window <wid>`, then `click`/`key` without `--window`. This worked for
  every click and key in the pass.
- **One local-only fixture, not on the Shelf and committed nowhere:** `tester-xp-bed`. It holds one
  henchman (`mate`, copied from `companion-fixture`) and one level-9 `challenge = 9` enemy with 1
  vitality. It exists so a single kill pays enough XP to level someone. Its full source is in the appendix
  so anyone can rebuild it. The first version lacked `challenge`, which is what XP is priced from, so its
  kill paid nothing. That was my fixture's fault, not the app's.
- **Missing compared with the old PC:** the `0 AAA Visual Pass` package used in TEST 141 is not in
  `Shelf`, so it didn't survive the crash. There's also no K2 install and no
  `HANDOFF/STUDY/k2-reference/` captures.

## Verdict

- **The environment works.** I built from a committed snapshot, ran chargen by real clicks, entered an
  area, saved via Leave Session and reloaded via Load Game back onto the same square.
- **Two new defects came out of the work order's own reload item. Both are severe:**
  - Kill XP is written to the save for the player but never counted. The sheet reads 0 in session and
    after every load. The same kill credits the companion correctly.
  - A companion's level-up is written to the save and then ignored on load. The companion is back to
    level 1 with Level Up offered again, after every one of three loads.
- **The player's own class, level and abilities stayed unchanged across all three reloads.** That was the
  literal ask of item 4, and it held.
- **Class-granted feats (87fb906) do reach new characters.** A Soldier gets Squad Tactics and Both Hands,
  and a Brawler gets Nothing In My Hands, all `source: granted` in the save. But **no screen marks a feat
  as granted.** The Brawler's L1 1d3 + STR is confirmed on Equip and in a real fight.
- **Items 2 and 3 (dual-wield, two-handed pairing) are COULD NOT TEST.** Equipping anything in play is
  not built. Every Equip commit, for any slot and any item, returns *"equipping is not built yet — what
  it costs is unruled"*. The only chargen route to two weapons is the excluded Hunter grant.
- **The terminal (item 1) is COULD NOT TEST.** Both terminal fixtures spend spikes, the Engineer kit's
  "2 × Computer Spike" never arrives, and no spike exists anywhere else on the Shelf. The refusal itself
  is honest.

---

## 1. Environment proof — CONFIRMED

`Cloud Soldier` (Human Soldier, Taris/Upper City/Noble, Female, Doctor, 14/14/14/12/12/12, Alertness,
Athletics, Awareness and Demolitions at 4, Conditioning) was built entirely by clicks, including all 30
ability points and all 16 skill points one stepper click at a time. Entering Endar Spire wrote the save.
I moved to (2,1), then went Options → Leave Session → Leave Session. The save was rewritten (880 → 919
bytes, new mtime). Load Game listed *"Cloud Soldier · level 1 soldier · a01-command-deck · just now"*,
and loading it returned her to (2,1). Screens `test-142/01`–`05`.

Honest refusals seen along the way, reported as-is and not as defects:

- Abilities and Skills → Recommended: *"no recommended spread is in the rules yet"* / *"no recommended
  allocation…"*.
- Options → Save Game: *"not built yet — the save format and its list exist, this door into them does
  not"*. Saves happen on area entry and on Leave Session.
- Welcome → Choose a game folder: *"not built yet"*.
- *"2 rules about this character not checked"* is the validator coverage count (PT-1648), not a defect.

## 2. Terminal: a real interaction, locked-and-trapped — COULD NOT TEST, blocked by a real gap

`Cloud Slicer` (Human Engineer, INT 16, Security, Slicing, Science, Repair, Awareness, Alertness and
Appraise at 4) was built in `locked-and-trapped`. The mine was noticed on arrival: *"you notice
mine.strongroom.01 — 14 against 12"*. I walked around it to (6,2) under the console (locked 15) and
right-clicked. The menu offered **Examine (Science)** and **Slice (Slicing)**.

- **Slice** → *"Security Console — no spikes left, and slicing spends one an attempt"* (`15`). The
  terminal panel never opened, so "nothing upside down, nothing missing" is **not checked**.
- **Why there are no spikes:** chargen's Equipment step lists the Engineer kit as *"2 × Computer
  Spike"*, but her inventory holds only `clothing` and `ion-blaster` (`13`). Both terminal fixtures
  (`locked-and-trapped`, `tester-strongroom`) declare `spends = "spike"`. No area, container or store on
  the Shelf holds a spike.
- **Examine** works: *"examine Security Console — d20 5 + Science 4 = 9 ⚠ what a total tells you is
  not ruled yet"* (`16`). **Question for Main, not a claim:** she has Science 4 ranks and INT 16 (+3),
  and the total adds ranks only. Every in-play skill check in `play_screen.dart` is built as
  `Term(skill, _rank(skill), from: 'rank')`, so this is consistent across the app. I could not find a
  corpus line that says whether a key-ability modifier belongs in the total.

### 2a. Starting kit, medical, boots and the profession item are never delivered — FAILED (narrowed)

Checked on two classes. Equipment lists each item, but the Inventory never gets them:

| | Chargen "the assortment" lists | Inventory after entry (ALL filter) |
|---|---|---|
| Soldier (Doctor) | Blaster Rifle · Short Sword; Adrenal Strength · 2 Frag Grenades; 2 medpacs; Dockworker's Treads; chosen **Advanced Medpac ×2** | `blaster-rifle`, `clothing` |
| Engineer (Doctor) | Ion Blaster; **2 × Computer Spike**; 2 medpacs; Dockworker's Treads; chosen **Advanced Medpac ×2** | `ion-blaster`, `clothing` |

- The Short Sword is the known excluded item and wasn't re-tested for its own sake.
- **The save says the item was taken:** `grant-resolved {"taken":"item","item":"Advanced Medpac,
  ×2","resref":"g_i_medeqpmnt02"}`. The following `equipment-set.items` lists only the weapon.
- The chargen code has resolvers only for armour and weapon (`resolveStartingArmour/Weapon`). Nothing
  creates kit, medical or boots items. The Equipment screen doesn't say so, although it does say so for
  the upgrade path.

## 3. Dual-wield with no feat (−4) and two-handed pairing — COULD NOT TEST (equipping is not built)

`Rifle Soldier` was built in `store-bed`. She bought the Vibroblade (Item Cost 100, Credits 100 → 0). In
Equip, the empty hand beside the two-handed **blaster-rifle** offered *vibroblade* (`19`). Selecting it
and pressing OK gave:

> **equipping is not built yet — what it costs is unruled (vibroblade → weapon_l_1)** (`20`)

The slot stayed empty. **This is not a two-handed refusal.** Narrowed on the same character: body →
None → OK gives the identical *"… (nothing → body)"* (`21`). `play_screen.dart` wires Equip's `onCommit`
to that message unconditionally. So:

- **Item 3:** there's no `weaponwield` 3/5/6 refusal to record, because no pairing is ever evaluated. I
  also found no code reading `weaponwield` in the app or in Lodestar.
- **Item 2:** a no-feat character can't hold two weapons. The array's second weapon never arrives (§2a),
  equipping in play isn't built, and the Hunter two-weapon grant is excluded this pass. The −4 is
  **not checked**.

**Store-side defect found on the way — the three footer buttons have no visible labels (`18`).** Close,
Buy and Selling are drawn, but `_footButton` passes `texel: _G.footH / 2`, so the edge texture fills the
button and covers the label. I found Buy by reading the code for the button order. TEST 141 used this
store, so this may be recent.

## 4. The reload sequence — the player HOLDS; the companion does NOT; and the player's kill XP is lost

`Brawler Two` (Human Brawler, 16/14/14/10/12/10) was built in `tester-xp-bed`. Mate auto-joined as a
henchman. One punch killed the dummy.

**Save log after the kill:**
```
character.xp-awarded {"subject":"Brawler Two","amount":3000,"from":"dummy.room.02","cr":9.0,"level":1}
character.xp-awarded {"subject":"mate.room.01","amount":3000,"from":"dummy.room.02","cr":9.0,"level":1}
```

### 4a. SEVERE — the player's kill XP is never counted — FAILED

| | In session, sheet reopened | After Leave Session → Load Game |
|---|---|---|
| Player (Brawler Two) | Experience **0**, Needed 1000 | Experience **0**, Needed 1000 |
| Mate (same kill) | Experience **3000**, Needed 0, Level Up offered | same |

Reproduced on a third character (`Solo Brawler`): again 3000 in the log and 0 on the sheet (`32`). The
repro is one kill, then open the sheet.

**Probable cause (from reading the code, not confirmed as the cause):**

- `_xpFor` writes the player's award with `subject: me.handle`, which is the player's name.
- `main.dart`'s `playerLog()`, the PT-2687 contamination fix, keeps only events with `subject == null`.
  So on load the player's own XP is dropped as if it were a companion's.
- In session, `_progressFor` only counts events not already in `widget.log`. That's consistent with the
  award being folded away. I haven't traced that path fully.

Since `_xpFor` always tags the player's award this way, I expect **every** kill to be affected. I could
not run a truly solo kill; see §4c.

### 4b. SEVERE — a companion's level-up is lost on every load — FAILED

Mate was levelled 1 → 2 through the real flow (Class Soldier · Alertness +3 · Cautious · Accept). The
status line read *"Mate — level 2 — Soldier"* and the save holds:
```
character.levelled {"level":2,"class":"soldier","xp":3000,"subject":"mate.room.01"}
character.skill-ranked / feat-taken cautious (chosen, 2) / squad_tactics + both_hands (granted, 1)
```

- Immediately after the level-up, **the sidebar card still read "Soldier · 1"** (`27`).
- After each of **three** loads, Mate's sheet reads **"Soldier · level 1", Experience 3000, Needed 0,
  with Auto Level Up / Level Up offered again** (`28`, `29`).
- I didn't press it. Doing so would write a second `levelled` event over the first.
- The level-up diff did backfill Mate's L1 Soldier grants, which is a nice side effect of `87fb906`.

### 4c. What the ask literally named — CONFIRMED

Three consecutive Leave Session → Load Game cycles, each followed by opening the player's own sheet:
**Brawler · level 1 · STR 16 DEX 14 CON 14 INT 10 WIS 12 CHA 10** every time (`29`). There was no
*"class levels add to N"* refusal and no companion data on the player's sheet. The PT-2687 fix holds in
the direction it was built for. §4b is the other direction.

**Narrowing that failed, and a third defect it exposed:** I tried to make §4a solo by using Mate's
**Dismiss from party** before the fight. The status line read *"Mate leaves the party"* and the save
logged `party.left`. But the next fight still listed Mate as a MANUAL party member (*"Mate is waiting on
you"*), and he was still paid 3000 XP (`31`). **A dismissed henchman still joins the next fight as party
and still takes XP.** So no truly solo kill was run.

## 5. Class-granted feats (87fb906)

### 5a. A new Soldier shows its level-1 granted feats, marked granted — PARTLY CONFIRMED

- **In the save — CONFIRMED.** `feat-taken squad_tactics {"source":"granted","at_level":1}` and
  `both_hands` likewise, beside `conditioning {"source":"chosen"}`. These match `granted_feats.dart`'s
  Soldier L1 rows.
- **On screen, shown — CONFIRMED.** Abilities → Feats has Squad Tactics, Both Hands and Conditioning as
  the only teal (held) tiles in the grid (`06`–`09`).
- **Marked granted — FAILED / not present.** The grid distinguishes only held (teal) from unheld (red),
  and `abilities_screen.dart`'s `AbilityRow` has no granted field. Neither the chargen hub summary nor
  the Character Sheet lists feats at all. The chargen Feats step says *"188 feats are granted, not
  bought"* but names none of this class's.

### 5b. Brawler at level 1: 1d3 + Strength unarmed — CONFIRMED, on Equip and in a real fight

- **Equip:** ATKR **4–6**, **+4** (`22`). 4–6 is exactly 1d3 + 3 (STR 16), and +4 is attack 1 + STR 3.
- **Fight:** *"unarmed · rolled 24 — d20 20 + attack 1 + Strength 3 · needed 13 — hit · damage 6 — 2d3
  2+1 + Strength 3 × 2 critical"* (`23`).
- The save records the Brawler's own L1 grant, `nothing_in_my_hands`, as `source: granted`.

**Question for Main (a critical-hit rule, not about 87fb906):**

- On that natural 20, only the die was doubled (2d3 = 3). Strength 3 was added once, giving 6, not
  (1d3+3)×2.
- Lodestar `combat.dart` multiplies dice and flat weapon bonuses but adds ability `mods` after, unmultiplied.
- RULES-01-v2 says *"Critical hits multiply"* and ATTACKS-01 §12 says *"`crithitmult` 2 means damage
  doubles"*. I found no ledger ruling either way.
- The line's *"Strength 3 × 2 critical"* also reads as if Strength were doubled.

### 5c. Brawler at level 2: Unarmed Specialist I, 1d4 + Strength — COULD NOT TEST

Blocked by §4a: the player can't bank XP, so she can never level.

### 5d. A Soldier stays at 1d3 + Strength — COULD NOT TEST

- Every Soldier starts holding a Blaster Rifle.
- Nothing can be unequipped (§3).
- Companion attacks go through `fight.dart`, which Coder says 87fb906 didn't touch, so Mate isn't a
  valid stand-in.

## 6. Smaller things seen on the way (not ruled, for Main to sort)

- **Conditioning does nothing.** Chargen offers it (*"+1 to all saving throws"*) and the save stores it.
  Cloud Soldier's saves read Fort +4 / Ref +2 / Will +1, which is base + ability with no +1. Neither the
  app nor Lodestar references `conditioning` anywhere.
- **The turn-order list shows placement tags instead of names:** *"room.01"* for Mate, *"room.02"* for
  Veteran Dummy (`24`).
- **Dice look identically seeded per session.** Two fresh Brawlers in two sessions got the same
  initiative (12/7/4) and the same natural 20 on the first swing.
- **Level-up text is stale at level 2.** Skills reads *"(3 from your class + 0 for Intelligence) × 4"*,
  though the total of 3 is right (`30`). Feats reads *"A Soldier gains its first feat at 1st level."*
- **A package whose `[entry]` has no `at` drops the player at (0,0), not on its only arrival.** Endar
  Spire's "aft" is (1,3) and Store Bed's "in" is (1,1). `locked-and-trapped` names `at = "back"` and
  lands correctly.
- **The companion Character Sheet shows empty "abilities" and "ratings" sections** for Mate, whose
  blueprint has abilities.

## Not checked, named

- The terminal panel's own rendering and art.
- Any locked-and-trapped console that is itself trapped (none exists on the Shelf).
- The −4 dual-wield tier.
- A two-handed weapon refusal.
- Brawler L2.
- Soldier unarmed.
- A truly solo kill.
- Anything needing real K2 (no install and no reference captures here).
- The excluded items: the Hunter path, the Short Sword, Two-Weapon Fighting text, enemy and companion
  dual-wield, and Equip layout/Config 2/Switch Weapons.

## Appendix — `tester-xp-bed` (local only, lives in `~/tester-data/kotor-rpg/packages/`)

`package.toml`: `id = "tester-xp-bed"`, `[entry] area = "a01-room"`, `at = "start"`.

`areas/a01-room.toml`: a 6×3 floor, arrival `start` at [1,1], `mate` (role `henchman`) at [1,0], and
`dummy` at [2,1].

`blueprints/characters/dummy.toml`: `[character]` with `class = "soldier"`, `species = "human"`,
`level = 9`, `challenge = 9`; abilities 10 except dex 3; `[vitality] override = 1`.

`mate.toml` is copied unchanged from `companion-fixture`.

---

## Addendum — Main's answers (after filing), recorded so the report is complete

- **Examine adds Intelligence.** `SKILLS-01` keys Science to Int, so §2's d20 + Science 4 should have
  been d20 + 4 + 3. It's ruled at PT-2708 item 5 and is no longer an open question.
- **A critical multiplies the whole damage.** Per `ATTACKS-01 §12`, "`crithitmult` 2 means damage
  doubles", and under RCR Strength and flat bonuses are multiplied too; rider dice are not. So §5b's
  natural 20 should have been (1d3 + 3) × 2. It's ruled at PT-2708 item 6.
- **Equipping was already ruled.** PT-2046 refuses it in combat, and `ACTION-ECONOMY-01 §5` makes a
  draw, stow or loadout switch a free interaction once per turn (a second costs the Action). The *"what
  it costs is unruled"* message in §3 is stale, not an open question. Coder is building it (PT-2708
  item 3), and the dual-wield −4 and pairing refusal wait for that.

**Fixtures handed over:** `HANDOFF/TEST/fixtures/` holds `tester-xp-bed`, `tester-purse` (re-authored)
and `tester-visual` (reconstructed). Their status and gaps are in that folder's README.
