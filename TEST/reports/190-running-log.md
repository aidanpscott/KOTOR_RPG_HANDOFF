# TEST 190 running log (draft, text only)

Started 2026-10-22. Tester, Xvfb :2, own data dir. All of chargen on K2 pages; four characters end to end.
Known, don't file: missing species/class/feat/form pictures, the Attacks page, level-up pages, in-game frames, Recommended on Equipment and Background.

## Build
- App c9946f8, git archive from my own clone to builds/test190. Built through the lock: 10.0 s. pubspec.lock unchanged.
- Gate: "gate.py --at c9946f8" -> "FOR TESTER — CORE at c9946f8, 4295 tests, 0 failed, 8m45s at -j 3, peak 1890 MB, run 2026-10-22T09:06:39"; "ARCHIVE last green at c9946f8".
- Lodestar 181ac71 = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 5ac3d20 (= origin). check_shelf: 32 rules files, 118 blueprints, identical.

## Items

### Character 1: Human Female Jedi Consular "Story One" (Persuade? no: bonuses Alertness+Appraise, racial Appraise; Taris Upper City Persuade; Noble; Hunter)
1a. Bar on every box: Entry Quick (overflows): short thumb, scrolls, last line "nothing to fill it in from." reachable. Custom (fits): full-track thumb. Seen on Species, Origin, Background, Equipment, Story panes too. PASS.
2. SPECIES: picture box on the left (empty, known), list right, name bar, description with bar. Human -> "Skill Bonuses" page (Back/OK).
   Skill Bonuses: behaviour PASS judged by row outlines and OK: two different skills outlined -> OK lit; a third (Athletics) not taken; touching Appraise again gives it back and OK dims. FINDING: the pane's "Skill Bonuses: N of 2" line is stale — it shows counts that don't match the outlines/OK (e.g. "2 of 2" with one skill chosen and OK dim). Cause in code: K2ListPage caches its items (`late final _all`, k2_list_page.dart:104), so descriptions built with the count never refresh.
   Racial Skill: Alertness/Appraise listed, nothing lit, OK dim until a pick. PASS.
   Note: Back from Skill Bonuses to Species then OK again keeps the two picks (fine).
CLASS: a click lights (name bar + description), OK chooses. PASS.
3. GENDER: Male/Female on the base page; one press commits (back to the hub, Portrait next); reopen shows Female lit. PASS.
4. ORIGIN: Homeworld list (help box) -> Taris -> skills under stratum bars "Upper City" (Persuade, Appraise, Pilot, Security), "Lower City" (Streetwise, Intimidate, Pilot, ...); one touch on Intimidate gives "Lower City / Aptitude: Intimidate +2 / Gangs, curfews, ...". Back returns to Homeworld. Upbringing page (Noble first). No authoring marks seen. PASS. Notes: after Back and OK again, the skills page lights Persuade, not the Intimidate picked before; Upbringing's description box is empty.
5. BACKGROUND: professions list; pane shows grant, aptitude, detail ("robe / Aptitude: Mysticism / a starting robe"; Hunter "melee weapon / Aptitude: Beast Handling / a better melee weapon"). PASS. Note: the first line is a bare lower-case word ("robe", "melee weapon").
6. EQUIPMENT: "Standard Gear" heading: Padawan Robe, Training Lightsaber (icon), Adrenal Stamina, "1 tier-1 saber upgrade" (dimmed), 2 medpacs, Dockworker's Treads, 100 Credits; then "Profession Bonus": the melee upgrade and "Aptitude: Beast Handling". OK dim until a bonus is picked; then lit. Purchase Gear opens K2's store (Credits 200 = gear value); buying a Short Sword: Credits 180, In Inventory 1; Close returns; the list becomes "Purchase Gear: Short Sword, 180 Credits" + Profession Bonus. PASS for the flow.
   FINDING: the upgrade bonus does not use plain words: it reads "Your class's own melee upgrade — Soldier → Long Sword + Short Sword or a Double-Bladed Sword; Scout → Double-Bladed Sword; Duelist → Vibrosword + Vibroblade" (the raw table, for a Consular whose class isn't listed). The row's text runs out of the list and over the frame on the right (equip-after-buy).
   Notes: only the lightsaber row has an icon; the gear pane says "Armor" (feats say "Armour"); clicking the dimmed upgrade row shows nothing. Store page: the right-hand labels are clipped on the left ("nothing selected", "n Cost", "n Inventory") and its font is not K2's (in-game frame? Note).
1c. POWERS PICK ORDER: Force Valor first (lower), then Burst of Speed (higher); reopen lit on Force Valor. PASS. Feats and Forms: a Consular has one pick each, so order can't differ (checked lit on Cautious / the form).
7. STORY: the finished character on the base page (portrait, name, class, level, scores with modifiers, Vitality 9/9, Defense 11). Try another gives a new text; CLEAR empties it. After a click in the box, typing and Left/BackSpace/Home/Delete/End all work and the "_" follows ("Born on _Taris" etc.). FINDING: before any click, the page shows the "_" caret but keys do nothing (typed "XY " at Home: not entered).
Play, F4, kill, Continue: Story One back in Tester Bolt. PASS.

### Character 2: Twi'lek Female Scout "Twi Scout" (racial Streetwise; Taris; Hunter; aptitude bonus)
2. Species pane "+2 Charisma, -2 Wisdom." (hyphen). Twi'lek -> straight to "Racial Skill" (Persuade, Streetwise), nothing lit, OK dim until a pick. PASS.
Scout hub: 11 steps, no Forms/Powers; but the hub TABS still show Forms and Powers (note).
Portrait: K2's "?" placeholder offered and taken. Attributes pane "+2 Charisma, -2 Wisdom."; Story sheet "8 (-1)", "6 (-2)". 8. Minus signs: hyphen everywhere seen. PASS.
Equipment (Hunter): the same raw upgrade text (Scout is in it: "Scout → Double-Bladed Sword" — buried in the table, not stated plainly for this character). Took the aptitude bonus instead; OK lit.
Name, Story, Play, F4, kill, Continue: Twi Scout back, "?" portrait. PASS.

### Character 3: Droid, Battle chassis, War Droid Mark II, Machinist "RX-190" (racial Scavenging, Slicer Droid, Neither)
2. Chassis page (K2): Astromech, Assassin, Battle, Remote, with Back; then Racial Skill (Scavenging/Repair), nothing lit, OK waits. PASS.
FINDING: the MODEL page (War Droid Mark I...) is still the old non-K2 page (plain font, empty right pane) — not on a K2 page.
Note: Cancel from Class back to Species forgets the species pick (Aqualish lit again) — as in TEST 184.
1b. Droid on Jedi Sentinel: "A droid chassis holds no Force class." then the class text; OK dead. PASS.
3. VOICE: Masculine, Feminine, Neither; one press commits; reopen shows Neither lit. PASS. Droid hub: 10 steps (Voice, Portrait, Background, Attributes, Skills, Feats, Attacks, Equipment, Name, Play).
Portrait: four droid faces (HK, two others, G0-T0-like). 
5. BACKGROUND (programmings): Medical, Slicer, Maintenance, Sentry, Salvage, Repair, Demolitions, Survey, Arcane...; opens lit on Demolitions Droid (not the first row?). Pane: "From: Slicer / Grant: 2 Computer Spikes / Cost: 500cr" — grant shown, no aptitude line, and "From:"/"Cost:" labels (note: is "Cost: 500cr" meant for the player?).
Attributes: fixed (no Point Cost, no Remaining, no arrows); pane "+2 Strength, +2 Constitution, -2 Intelligence, -2 Charisma." hyphens. Equipment: Standard Gear "Blaster Pistol, 1 Parts, 1 Repair Kit, 1 Frag Grenade, 2 Repair Kits, 100 Credits" (no Profession Bonus); "1 Parts" grammar (known from 184).
Designation popup, Story, Play, F4, kill, Continue: RX-190 back. PASS.

### Character 4: Aqualish (Quara) Male Sith Warrior "Quara Four" (racial Swim/Intimidate)
2. Subrace page (Aquala, Quara, Ualaq) with Back -> Species; Quara -> Racial Skill (Swim, Intimidate). PASS.
Forms: Recommended took Aggression (FORMS-01 §2.4 Sith Warrior -> Form IV). Forms tab: Determination, Aggression. PASS.
1c. Powers pick order again: Force Valor first, then Burst of Speed; reopen lit on Force Valor. PASS.
Equipment: "Dark Padawan Robe", "Training Lightsaber red" (stray lower-case colour word), "Adrenal Strength", "2 medpacs", "Dockworker's Treads", "100 Credits"; Profession Bonus "Security Tunneler, ×2" / "Aptitude: Security".
Play, F4, kill, Continue: back. NOTE for MAIN: the party card reads "force 0 of 0" for a level-1 Sith Warrior (WIS 8, CHA 8) who has two powers.
1c. Feats and Forms pick order: every class I made has one feat pick and one form pick at level 1, so first-picked vs grid order can't differ there; Feats/Forms reopen lit on the single pick.

### 9. Look at 1280x720 (Bith Consular "Bith Seven", fresh window)
Entry, Species, Class, hub, Gender, Portrait ("?"), Homeworld, stratum skills, Upbringing, Background, Attributes, Skills, Feats, Forms, Powers, Equipment, Name popup, Story: all fit, nothing clipped or overlapping, K2 fonts; minus signs hyphens ("-2 Constitution, +2 Intelligence, -2 Charisma."). The store page's text is very small at 720 and its labels clipped on the left (as at 1920). No "Defence" seen anywhere.
### 10. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 24 "reg190", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
