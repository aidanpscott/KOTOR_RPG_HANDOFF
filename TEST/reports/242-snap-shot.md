# TEST 242: Snap Shot (Snap Shot, Reflex Fire, Interdiction), rerun

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-242/`; names in brackets below are files there. Log lines are quoted from the in-game Combat log.

The first run of TEST 242 (b39b008) stopped at step 2: there was no fight on load, and the Lurker and the Sniper were both at (10,4). MAIN accepted both, and this rerun is on the fix.

## Build

- **App**: main `a5d6662`, a fresh worktree. `gate.py --at a5d6662`: "FOR TESTER — CORE at a5d6662, 5753 tests, 0 failed"; ARCHIVE last green at a5d6662.
- **Lodestar**: `4d4e93b` compiled (package_config.json), as the order says.
- **Settings**: defaults (no settings.json) at the start. **Shelf**: `f4750f8`, check_shelf clean.
- **Beds**: all `author_tester_*` tools ran with no errors.
  - The yard's creatures are now `faction = "Sith"`, and the package is Republic.
  - The Lurker is at (11,4), the Sniper at (10,4).
  - Every run starts from a pristine copy of its save in a relaunched app.
- Every step ran on this build.

## Summary: two findings, one of them minor

| # | Check | Result |
|---|---|---|
| 1 | Gameplay row | **PASS**. "Snap Shot: Ask". |
| 2 | Snap One, Always | **PASS**. The fight begins on load; the Skirmisher leaving cover draws "Snap Shot: Snap One attacks Skirmisher" at −4; one only; reactions 3 to 2. |
| 3 | Ask | **PASS**. "Skirmisher leaves cover" asked before its walk; No: no shot; Yes: the shot. |
| 4 | Never; Blade One; Plain One | **PASS**. No shot from any of them. |
| 5 | The Sniper fires at you | **PASS**. Fires as she steps off cover; not again that walk; fires again on a later turn's walk. |
| 6 | Reflex Fire for Mate | **PASS** for an attack on the attacker's own turn. **FINDING 1**: an opportunity attack on Mate is not answered. |
| 7 | Blade One strikes the Guard | **PASS**. "Reflex Fire: Sniper attacks Blade One" follows her blow. |
| 8 | Interdict One | **PASS**. "Interdiction: …" at no penalty. |
| 9 | A Snap Shot is never answered | **PASS** for "answered". Nobody here can deflect or parry. |
| 10 | Dice; regression | **PASS**. SAME17; slot 79 to 80, mid-fight save and load, fight won. |
| — | Ask on an attack out of reach | **FINDING 2 (minor)**: "Guard attacks Mate" is asked for a blow that never lands. Nothing is spent. |

## 1: Options > Gameplay

There's a new fifth row, **"Snap Shot: Ask"** (`s1-gameplay`). Its text: "An enemy enters your line of sight or leaves cover: one shot with the gun in your hand, for one reaction, once a walk (Snap Shot -4; Reflex Fire -2, and also at an enemy attacking an ally within 4 metres of you; Interdiction, no penalty)." `−` sets it to Always (`s2-always`), and settings.json then reads `"reactions":{"snap_shot":"always"}`. For later steps I set it in settings.json before launching, or in-game where noted.

## 2: Snap One, Always

- **The fight begins on load**: the strip and "A fight begins." come at once, then "Sniper attacks Snap One : \*hit\* : (10 + 9 = 19)" (`b0-load`, `b0-log`). The order: Sniper, Skirmisher, Mate, Guard, Snap One, Lurker. All six names are on the status line, and five tokens stand on five squares.
- In round 1 the Skirmisher stays on its cover. In round 2 it walks (`b3-log`):
  > Snap Shot: Snap One attacks Skirmisher : \*hit\* : (8 + 11 = 19)
  > Snap One damages Skirmisher for 4 damage
- **−4**: her ordinary shot reads "attack 12 + Dexterity 2 + cover 1" (with point blank 4 taken off at 1 square, `b4-shot`). Her terms come to 15, and the Snap Shot is 15 − 4 = 11.
- **One only**: rounds 3 to 5 have no second Snap Shot line (`b7-log`, `b11-log`). In those rounds the Skirmisher walks again to stay beside her, and I walked her to (5,2) behind the wall.
- **The pip**: "Reactions (out of turn): three" before; "reactions 2 of 3" after the shot (`b3-hov`).

## 3: Ask, Snap One

- In round 2, before the Skirmisher moves: "**Snap Shot / Skirmisher leaves cover / one reaction · 3 left / 95% (needs 2+)**", Yes and No (`a2-q`). The Skirmisher is still on its cover at (7,6), visible behind the dialog.
- **No**: it walks to (3,5) and attacks, "(8 + 4 = 12)", with no Snap Shot line (`a3-log`, `a3-board`).
- **Yes** (a fresh load): "Snap Shot: Snap One attacks Skirmisher : \*hit\* : (8 + 11 = 19)", the same as Always (`y3-log`).

## 4: Never, Blade One, Plain One

Each ran 4 rounds from a fresh load, and in each the Skirmisher left its cover in round 2 and attacked her. No log has a "Snap Shot", "Reflex Fire" (hers) or "Interdiction" line (`n1-all`, `bl1-all`, `pl1-all`):
- Interdict One on **Never**;
- Blade One (Vibroblade) on **Always**;
- Plain One (pistol, no chain) on **Always**.

## 5: The Sniper fires at you (Snap One, Never)

Her round-1 turn (`w1` to `w7`):
- **Up to (2,3)**, off her cover: "Reflex Fire: Sniper attacks Snap One : \*hit\* : (12 + 7 = 19)". The Sniper's ordinary shot is +9, so +7 is its −2.
- **Up to (2,2), Down to (2,3), Up to (2,2)**: no second line that walk (`w3-log`, `w4-log`).
- Ended the turn at (2,2). I ended one turn too many, so her round-2 turn passed at (2,2) without a step. She stayed hidden and the Sniper shot Mate instead.
- **Her round-3 turn, Down to (2,3)**: "Reflex Fire: Sniper attacks Snap One : \*hit\* : (18 + 7 = 25)" (`w7-log`). It fires again on a later walk.

## 6: Reflex One and Mate

- **Nobody answers an attack on yourself**: the Sniper's round-1 shot at Reflex One, and its Reflex Fire when she steps off cover, draw no answer from her. She's on Always, holds tier 2 and has uses left (`r0-log`, `r1-log`).
- **Out of sight**: hidden at (2,2) with Mate at (2,4), two squares away, she doesn't answer the Sniper's round-3 shot at Mate (`r5-log`). That's right: she can't see the Sniper behind the wall, and the shot needs her sight of the attacker.
- **Answered at −2** (Mate moved to (4,5), two squares from her on cover at (2,4), `x4-log`):
  > Skirmisher attacks Mate : \*hit\* : (12 + 2 = 14)
  > Skirmisher damages Mate for 10 damage
  > Reflex Fire: Reflex One attacks Skirmisher : \*hit\* : (18 + 13 = 31)
  - Her terms on cover are 15, so 13 is the −2.
  - It's her second use. The first was "Reflex Fire: Reflex One attacks Skirmisher : (14 + 13 = 27)", on its leaving cover. The Lurker's critical hit on Mate right after got no answer.
- **Snap One doesn't answer**: on Ask, I answered No to "Skirmisher leaves cover", so she kept her one use. Then "Skirmisher attacks Mate : \*hit\* : (8 + 2 = 10)", with Mate two squares from her, brought no question and no shot (`z3-log`).

### FINDING 1: an opportunity attack on an ally draws no Reflex Fire

- **Setup**: Reflex One, Always, on cover at (2,4), Mate at (2,5), the Skirmisher at (3,5) beside both after its round-2 walk. She had answered its leaving cover, so one use and two reactions were left.
- **The attack**: I moved Mate Left to (1,5): "Opportunity attack: Skirmisher attacks Mate : \*miss\* : (1 + 2 = 3 Automatic Miss!)".
- **What happened**: no Reflex Fire followed (`m2-log`). The Skirmisher is one square from her and in her sight, and Mate is a square from her.
- **On Ask** (step 9's run): two opportunity attacks on Mate, a square from her, brought no question either (`d8-log`): "Opportunity attack: Skirmisher attacks Mate : \*miss\* : (5 + 2 = 7)" and "Opportunity attack: Lurker attacks Mate : \*hit\* : (18 + 2 = 20)".
- **The rule**: the order says Reflex Fire "also answers an enemy's attack on an ally within 2 squares of you". The Gameplay text says "an enemy attacking an ally within 4 metres of you". An opportunity attack is an attack, and nothing in either text leaves it out.
- **In the code**: `_reflexFireAfter` is called from the player's strike (`play_screen.dart:14556`) and from an enemy's own turn (`afterStrike`, `:16941`). The opportunity-attack path doesn't call it. If MAIN rules that an opportunity attack shouldn't count, this is not a defect.

## 7: Blade One strikes the Guard

- Round 1: Right ×5 to (7,4). The Sniper's Reflex Fire answered her leaving cover, "(12 + 7 = 19)".
- Round 2: Right to (8,4), then I clicked the Guard at (9,5) (`k4-strike`, `k4-log`):
  > Blade One attacks Guard : \*hit\* : (18 + 15 = 33)
  > Blade One damages Guard for 10 damage
  > Reflex Fire: Sniper attacks Blade One : \*hit\* : (18 + 7 = 25)

## 8: Interdict One, Always

"Interdiction: Interdict One attacks Skirmisher : \*hit\* : (8 + 15 = 23)" (`i1-all`). It reads "Interdiction:" and is at her full 15, so there's no penalty.

## 9: A Snap Shot is never answered

- **Setup**: Reflex One at (4,4), switched to Ask in-game (`d4-set`), with all three reactions and both uses in hand (I answered No to every question). Mate was on the half cover at (6,5).
- **Mate's round-4 turn**: Mate stepped Left off it to (5,5), a square from her. "Reflex Fire: Sniper attacks Mate : \*hit\* : (11 + 7 = 18)" (`d8-log`).
- **Result**: no question and no shot from her, though the Sniper is in her sight (it had shot her every round).
- **Deflect and parry**: nobody in the Snap Yard holds Force Deflection or Parry, so I couldn't test those here.

## FINDING 2 (minor): Ask asks about an attack that never comes

- **What happened**: in the same run, on Ask, the game asked "**Guard attacks Mate** · one reaction · 3 left · 95% (needs 2+)" in rounds 2, 3 and 5. The Guard holds its square at (9,5), and Mate was 3 and then 4 squares away.
- **The log**: right after the question, "Guard: Vibroblade · out of reach — Vibroblade reaches 1 square and Mate is 3 away" (later "4 away"). There's no attack line.
- **Answering**: No, twice. Then **Yes** in round 5: no shot followed, and she still showed "reactions 3 of 3" (`g-log`, `g-hov`).
- **Effect**: a question about a blow that never lands. It costs a click, not a reaction.

## 10: Dice and regression

- **Dice**: the right Dice One Quick Save; the first 17 lines match the TEST 206 baseline (SAME17).
- **Regression**: Icon Nine.
  - Loaded slot 79 (reg241, 16:49:37) and saved it as slot 80 ("reg242", 19:35:46).
  - A quick save mid-fight (19:35:52), then loaded slot 80.
  - Won the fight: "Icon Nine: 103 of 196", "FIGHT OVER".

## Odd, not filed

- **The Lurker behind the wall**: in the first Snap One run the Lurker reached (7,3) in round 2 and stood there through round 5, with no line of its own. That held even after I walked her to (5,2), where the package notes say it comes round the wall into her sight. In later runs, with Mate out in the open, it came round and struck Mate, and on Ask "Lurker enters your line of sight" was asked. So it seems to go for whoever it can reach.
- **The fixed seed**: one Reflex One load out of four rolled different dice from the start ("Sniper attacks Reflex One : (17 + 9 = 26)" against 10 + 9), with a different order (Sniper, Mate, Skirmisher, Guard, Lurker, Reflex One). The other three loads matched each other. The tool says "a fixed seed each". I didn't change anything between those loads that I know of.

## What I got wrong

- The OCR reads "REFLEX" as "RerFlrex", so two Reflex One loads stopped at the name check and loaded nothing.
- In step 5 I ended one turn too many (above).
- My first Reflex One setup hid her from the Sniper, so her silence there proves nothing about Reflex Fire. The later runs replaced it.
