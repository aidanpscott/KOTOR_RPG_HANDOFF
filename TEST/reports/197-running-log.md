# TEST 197 running log (draft, text only)

Started 2026-10-24. Tester, Xvfb :2, own data dir. Batch 3 (Options, Save/Load, Party Selection, HUD, fight) + TEST 196 fixes.
Known, don't file: dialogue/computer/game over/pause/area transition/confirm screens on old frames (batch 4); store gold, lit rows, combat bar, white ring reasoned; list boxes short at the right edge.

## Build
- App 47fe0ea, git archive from my own clone to builds/test197.
- Gate: "FOR TESTER — CORE at 47fe0ea, 5053 tests, 0 failed, 12m28s at -j 3, peak 1787 MB"; "ARCHIVE last green at 47fe0ea"; SENDABLE with 6 warnings.
- Lodestar 240bc46 = lock = compiled (pub-cache Lodestar-240bc46…). Lens 5fe60a9. Loom: no entry. Shelf 9706207.
- Build through the lock: 10.1 s. pubspec.lock unchanged (md5 38d90beb…).
- Characters: Coder's tool wrote saber-hand.sav (18 events) and gear-note.sav (16 events), endar-spire, a01-command-deck. Mine: Lang Three (specs197/lu197-twi.json, species "twi-lek", Store Bed); Lang Two (species "twi'lek") kept from TEST 196.

## 1. Options
Main menu (Store Bed): rows Gameplay, Feedback, Graphics, Keyboard Shortcuts, closed up; lit row has a pale border. (mm-options.png)
Gameplay: three K2 spinners only (Opportunity attack, Force Deflection, Force Redirection), Close, Default; no phantom rows (K2's Difficulty/checkboxes/Mouse Settings/Key Mapping not drawn). Plus cycles Ask -> Never -> Always -> Ask; minus goes back (Ask -> Always). Hovered row pale, help pane follows. (opt-gameplay.png, opt-gameplay-set.png)
Feedback: Hide Unequippable, Tutorial Popups, Floating Numbers only. Box toggles each click (pixel mean 15 <-> 31). (opt-feedback.png, opt-feedback-set.png)
Graphics: Brightness slider only. Drag lowers/raises the whole screen (mean 33 -> 14 -> 34); left at x 500 (mean 22). (opt-graphics.png, opt-bright-*.png)
Saved at once: settings.json {"floatingNumbers":false,"hideUnequippable":true,"tutorialPopups":true,"brightness":0.4018,"reactions":{"opportunity_attack":"never","force_deflection":"always"}}.
Restart (kill PID, relaunch): Gameplay reads Never/Always/Ask; boxes on/on/off; thumb x 500. PASS. (reload-*.png)
Note: once, a fast xdotool drag chain ended on the Options menu instead of Graphics; not reproduced with stepwise drags. Not filed.

## 2. Save / Load (Lang Two, Store Bed) — PASS
Save page: no Cloud Save; nothing directly under the title (only the list's top rule, as K2). New Slot row; its preview has the empty bar. Name box = K2 popup (Save Game / bar / OK / Cancel). Saved "31 : sl197" (17:43:46). Overwrite: select row, Save -> "Are you sure you want to overwrite the save game?" OK -> saved at once (no name box), row now 17:44:07. Load: row 31 -> back in play. In-play Options rows: Save Game, Load Game, Gameplay, Feedback, Graphics, Keyboard Shortcuts, Exit Game (closed up). (save-page, save-name, save-after, overwrite-1/2, load-page, load-after)
Note: Lang Three (species "twi-lek", species.toml's id) is refused at load: "This character is a species this package does not have: "twi-lek"." The app keys species by lower-cased NAME (main.dart:244), so "twi'lek" is the id. Lang Two used.

## 4. HUD (partial, Lang Two)
Menu buttons top right; party bottom right ("?" portrait, red bar); message box top centre (red frame: "Market / Lang Two"); sidebar in a K2 pane top LEFT where K2's minimap sits (order said top-right; parity table says the minimap's place — K2 04-loaded has the minimap top-left).
Action columns: 1 attacks EMPTY (owner), 2 Force empty (Soldier). 3 Gear (g) -> arrow -> Throw a grenade (o). 4 Hide (s) -> Scan (c) -> Treat (t) -> Repair (r). 5 Dash (h) -> Disengage (d). 6 Rest (e) with "Rest" named above the bar. Each hover box shows the key. Small: column 5 shows no icon on Disengage. (hud/*.png)
Hide toggle drawn dim, no hover box, clicks do nothing here (nobody to hide from); Switch Weapons lit. Toggles to retest in the fight bed.

## 6. Twi'lek (authored) — PASS
Lang Two (species "twi'lek"): Character Info Species "Twi'lek"; Languages "Speak and read/write Ryl and Basic; Bonus language: Lekku (the head-tail language)." (lang2-info.png). Small: Gender reads lower-case "female".

## 9. Portrait meets the bar — PASS
RX-196 at 1920: portrait left x 330; bar ink right edge 325 at y 350 (5 px), 316 at y 400, 294 at y 570 (the bar's curve, 36 px at its middle), 324 at y 770 (6 px): the portrait meets the bar's ends, the curve bows away in between. At 1280x720 the same by eye: portrait at the bar's top and bottom ends. Labels Light/Dark whole. (rx-sheet-1920.png, rx-sheet-1280.png)

## 10. — PASS
Map strip: "Map — ⟨Market⟩" (map.png). Level-up hub (RX-196 6->7) portrait box shows RX-196's portrait (rx-hub.png); left without Accept. Store In Inventory: Frame One + Vibroblade "0 (replaces Blaster Rifle)" (store-vibro-frame.png); RX-196 + Vibroblade "0 (You cannot use this item.)" (store-vibro.png).

## 5 (conversation part) — PASS, with a finding
Talking to Dressa: the HUD (menu buttons, party, action bar, sidebar) hides; the red message box stays (top centre, "RX-196"). FINDING: the box overlaps the dialogue column: the speaker's name "DRESSA" shows as "ESSA" and her reply "Take your time." as "ake your time." (conversation-hud.png, conversation-clip.png)

## 6 (chargen) — PASS
Twi Seven (chargen in Tester Bolt: Twi'lek, Persuade, Female, Taris Appraise, Noble, Merchant, Soldier): chargen Origin page already lists Species Twi'lek and the Languages line; in play Character Info: Species "Twi'lek", Gender "Female", Languages "Speak and read/write Ryl and Basic. Bonus language: Lekku (the head-tail language)." (twi7-info.png). The authored Lang Two's lower-case "female" is my fixture's value.

## 8. Purchase Gear, Soldier — PASS
Twi Seven's Standard Gear: Clothing, Blaster Rifle, Short Sword, Adrenal Strength, Frag Grenade x2, Medpac x2, Dockworker's Treads, 100 Credits. Purchase Gear Armor tab: Clothing only, Item Cost 0, In Stock Infinite; no robes. (cg-equipment.png, pg-soldier-armor.png)

## 3. Party Selection (Twi Seven + Vela, Tester Bolt "Range") — PASS with one finding
K2's ring of ten portrait slots, Vela's portrait in the first, ringed WHITE while in the field; "2 Available Slots"; Vela's large portrait and "Vela / Henchman" box; Remove under the ring; Cancel, OK, Doctrine (right of OK). Help box once. (party.png)
Remove -> ring turns teal, "3 Available Slots", button reads Add; party unchanged behind. CANCEL: Vela still in the party (sidebar, bottom right). ESCAPE after Remove: Vela still in the party. OK after Remove: Vela leaves (sidebar empty). Add + OK: back, ringed white, "2 Available Slots". (party-removed*, party-after-cancel, party-after-escape, party-after-ok, party-added, party-after-add)
Doctrine (Vela selected): a chooser "Aggressive / Jedi Support / Healer". Small FINDING: Escape with the chooser open closes Party Selection but leaves the chooser floating over play (and over Options after another Escape); only a click outside it closes it. (doctrine-stuck.png)
FINDING: removing a companion with OK leaves a "V" token where she stood (non-party); adding her back puts her party token (red disc) next to the player while the "V" stays: Vela is drawn twice. Clicking either says "walk into them to act — choose an action first to aim at somebody". Reproduced twice. (party-after-add.png, party-remove2.png, party-readd2.png)
Not reached: page arrows (one companion); a refused pick's reason under Add (no refusable companion here).
Update: after the player's next steps the stale 'V' disappears and Vela (red disc, teal halo) follows; the duplicate lasts only until the party moves. Downgraded to small. Board tap on an empty square moves the player there (board-move.png).

## 4/5. Fight (Range bed, Twi Seven + Vela vs 3 gunmen)
Walking in starts the fight: sidebar becomes 'In this fight' (turn order + cards) in the top-left pane; initiative strip under the message box; bottom right shows the actor large. (fight-2.png)
Combat queue: budget '5 -> 0 move · action · gear · reaction · per encounter' and 'Defense base 10 + Dexterity 3 + cover 5 = 18'. Small: both lines run across the queue's red shapes (arrow and oval) rather than inside them.
END TURN under the queue in Cancel Combat's place, red frame, teal K2-face words; ends Vela's turn (turn passes to Twi Seven). PASS. (fight-3.png)
Message box (red): vitality of everyone + the prompt; grows for the attack line ('Short Sword · rolled 15 — d20 9 + attack 1 + Strength 3 + closed on a ranged weapon 2 · needed 10 · 1 square — hit · damage 9 — 1d6 5 + Strength 4 · 9 left'), and while grown covers the initiative strip. Small finding: after End Turn passed to Twi Seven, the box still read 'Vela is waiting on you' until the next prompt. (fight-3.png, fight-attack.png)
Switch Weapons in the fight: 'you switch weapons' in the box; the button shows no pressed/held state. Hide: dim, refused for Twi Seven ('you cannot use Stealth untrained — it needs at least one rank'); toggle has no hover box (the reason is on column 4's Hide). Held state not reached with this character.
Party bars: Vela hit for 15 (25 of 40): her red vitality bar shrank to y 989-1073 of 940-1073 = 63% (25/40 = 62.5%). PASS. Force bar full (63/63); spending not reached ('Vela knows no Force powers').
Small: column 2's hover box ('Use the Force (f)') is clipped at the screen's left edge ('se the Force', 'ela knows ...'). (vela-force-col.png)
Combat log: only in Messages > Combat, under 'Round 1/2/3' headings (attacks, misses, damage). The play view shows no log, only the message box. PASS. Small: 'A fight begins.' is listed five times at the top (once per combatant?). (messages-combat.png)

## HOLD (MAIN, 2026-10-24): stopped here. App, xsettingsd, Xvfb stopped by PID. Next on resume: Gear Note + Saber Hand (Endar Spire card in the library, 7 scroll steps right; openpkg.sh regex clicked the wrong card), Hide held state (Watch Four, Stealth 8, Tester Bolt), Purchase Gear spot-check of 2 more classes, dice, regression (Icon Nine).

## HOLD LIFTED (MAIN, 2026-10-24). Rulings since the stop (not new findings): Party Selection returns to a scrolling list with a party lock (ring findings superseded); mid-fight swap being fixed; conversation clipping to be retested on the new letterbox; scroll bar becomes 8 px. Smalls stay as written.

## 7. Gear Note — PASS
Stats: Defense "—". Character Info, under Feats, two red lines: "Defense: No Such Visor will not open: there is no item here." and "Mental Boost Package has no effect: it needs the Cybernetic Implantation, Advanced Cybernetic Implantation or Master Cybernetic Implantation feat." (gear-note-stats.png, gear-note-info.png)

## 11. Saber Hand — PASS
Lightsaber in the right hand: Abilities > Forms > Determination: header "Determination / Lightsaber Form", pane opens "Current stance" then the effects. (The order quoted "Current stance: Form I"; the name is in the header instead.) Equip: None double-clicked in Weapon R -> Lightsaber unequipped (damage 3-17 -> 2-4); Forms pane then has no "Current stance" line. (saber-forms.png, saber-equip.png, saber-unequip.png, saber-forms-off.png)

## 8 (two more classes) — PASS
Scout (Endar Spire): Standard Gear Clothing, Blaster Carbine, Short Sword, Stamina, Medpac x2, Dockworker's Treads, 100 Credits; Purchase Gear Armor = Clothing only, cost 0. Smuggler: Standard Gear Clothing, Blaster Pistol, Short Sword, Alacrity, Medpac x2, Dockworker's Treads, 100 Credits; Armor = Clothing only, cost 0. No robes. (cg-scout-standard, pg-scout-armor, cg-smuggler-standard, pg-smuggler-armor)

## Hide held state (Watch Four, Stealth 8, Tester Bolt Range) — FINDING (small)
Out of a fight walking past the gunmen started nothing; bumping one did. On her turn the Hide toggle is lit; pressed: message 'hidden — 17 beat 9', her card reads 'W... hidden'. The toggle then turns DIM instead of showing a pressed/held state (k2_hud.dart:212 has isDefault: hidden but enabled: refusal == null, and the spent action refuses, so the held look never shows). (w4-hide-0.png, w4-hide-1.png, hud/wh0-1.png)

## 12a. Dice — PASS
Instrument changed: the play view no longer shows the log (batch 3), so dicerun.sh's log crop read nothing and never saw 'Round 3' (run A went on to total defeat; md5 2519f740 is of empty crops, not a mismatch). Re-ran from Dice One's Quick Save (Oct 19 07:40:30): same walk, 3 steps, then Messages > Combat. Initiative Gunman 19, 13, 11, Dice One 10, Vela 2. Rounds 1-3 identical to TEST 185's log line for line (Round 1 14+3=17 hit, 11 dmg; 13+3=16 hit, 7 dmg; Round 2 8+3 miss, 13+3 hit 5 dmg, 5+3 miss; Round 3 8+3 miss, 1+3 Automatic Miss, 18+3=21 hit 3 dmg). (dice/B/combat-tab.png, combat.txt). Also seen: a floating line on the board 'Gunman attacks Vela : *hit* : (10 + 3 = 13)' over the gunman (after3.png).

## 12b. Regression (Icon Nine) — PASS
Loaded 30 reg196 (start); Escape > Save > New Slot 'reg197' (000032.mark, 19:57:21); Escape then F4: one quick.mark (19:57:26); Load lists Auto Save, Quick Save, '32 : reg197'; loaded reg197 back at the start; a fight to its end: 'Your entire party has been killed.' box, Go to Load Game List / Main Menu. (reg/start.png, reg/end.png)
