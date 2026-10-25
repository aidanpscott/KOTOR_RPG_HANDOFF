# K2-WORDS-PENDING-PT2752 — words with no exact K2 source, for the owner's approval

**Status: 2026-10-18.** §1 APPROVED by the owner (option (a), `Point Cost N`, StrRef 218) — built. §2 APPROVED by the owner (2026-10-18) — built. Anything new below §1 is still a draft. The naming rule (`PT-2752`): a word on a chargen or level-up page comes from K2's StrRefs or the approved names; a word with no K2 source is drafted here first and is not built until the owner approves it. Nothing below is in the app yet.

## 1. The Force point cost line in the Powers pane — APPROVED (a), 2026-10-17

**The ruling (owner, 2026-10-17):** show a power's Force point cost in the Powers pane, in K2's words, with our cost from `powers.toml`, where K2's line would sit.

**The search.** K2's `dialog.tlk` (every entry) has **no line labelling a power's Force point cost**. K2's level-up Powers pane prints none (`k2-levelup/manual/L2-10`, `L2-12`, `L3-24`, `L4-14`: side, prerequisites, Restricted By Armor, description). The nearest K2 strings:

| StrRef | Exact text | Where K2 uses it |
|---|---|---|
| 218 | `Point Cost` | chargen Attributes and Skills (`abchrgen_p`, `skchrgen_p`): the cost of the next point |
| 42006 | `Force Points spent:` | combat feedback after a cast |
| 1060 | Force | the character sheet's pool label |
| 124106 / 124108 | `… + FP Cost` | inside the Force Potency / Force Mastery stance messages |

**Proposed, one to choose:**

- **(a) `Point Cost N`** (218, K2's own chargen cost label), as its own line after the side line: `Light Side Power` / `Point Cost 6` / … Reuses K2's exact words; on Attributes and Skills it means skill or attribute points, here Force points.
- **(b) `Force Points spent: N`** (42006): K2's exact words for a cast's cost, but phrased as something already spent.
- **(c) A new line `Force Point Cost: N`** — no K2 source; ours.

**Where it would sit:** in the pane, second line, under the side (`Light Side Power`), before `Prerequisites:` — K2 prints no cost line, so there is no K2 position; the second line keeps the side first, as K2 has it.

**The value:** our cost from `powers.toml`, read through the one cost function at the character's alignment (`ALIGNMENT-01 v3 §1.3`), so a dark power's cost for a light character shows the adjusted number.

When approved: the line goes into the chargen text guard's word list and is tested with a power whose cost changes (a dark power at two alignments).


## 2. The Attributes pane's six descriptions — APPROVED, 2026-10-18 · *Dexterity's "Defence" spelled "Defense", K2's spelling, owner ruling 2026-10-19 (TEST 185)*

**The rulings (owner, 2026-10-18, PLAYTEST-RULINGS-01):** use K2's six attribute descriptions (StrRefs 222–227) in the Attributes pane, Dexterity with our ranged damage; then *"if we need things to be reworded to match our rules, we absolutely should be doing that"*. All four rewordings approved as written (via MAIN), *"force of personality"* included. Built in `lib/chargen/abilities_screen.dart` (`k2AbilityDescriptions`); the chargen text guard holds each word for word.

| Attribute | K2's line | Approved | The rules that change it |
|---|---|---|---|
| Strength | 222 | **K2's 222, verbatim** | — (melee and lightsaber attack and damage use Strength: Lodestar `combat.dart:1474-1477`, `1864-1899`; `ATTACKS-01:488`; `EQUIPMENT-01:9`) |
| Dexterity | 223: *"…adds modifiers to ranged attack rolls (blasters) and increases a character's Defense, making them harder to hit."* | *"Dexterity measures agility and reflexes. A high Dexterity adds modifiers to ranged attack rolls and damage (blasters), Reflex saving throws and initiative, and increases a character's Defense, making them harder to hit."* | ranged damage `combat.dart:1846-1851` (`PT-340`, `EQUIPMENT-01:9`); Reflex `saves.dart:123`; initiative `round.dart:954` (`ACTION-ECONOMY-01:644`); Defence `defence.dart:36-80` (`EQUIPMENT-01:15`), our spelling |
| Constitution | 224: *"…adds modifiers to the vitality points gained at each level-up. Constitution also determines what types of implants…"* | *"Constitution represents health and resiliency. A high Constitution adds modifiers to the vitality points gained at each level and to Fortitude saving throws. Constitution also determines what types of implants the character can equip. This attribute is important for all classes."* | vitality `round.dart:1215-1222` (`CLASS-TABLES-BASE:142-146`); Fortitude `saves.dart:122`; implant gates CON 12/14/16 (`EQUIPMENT-01 §17.4`, `PT-2342`, `PT-2731`) |
| Intelligence | 226 | **K2's 226, verbatim** | — (skill points `levelling.dart:106-110`; `SKILLS-01:224`) |
| Wisdom | 225: *"…adds modifiers to Jedi Force Points and Force Power saving throws. The Force Powers of a Jedi with high Wisdom are also much harder to resist."* | *"Wisdom represents willpower and perception. A high Wisdom adds modifiers to a character's Force points, Will saving throws and the vitality their healing powers restore, and slows their drift in alignment. The Force powers of a character with high Wisdom are also much harder to resist."* | Force pool `pools.dart:462-513` (`FORCE-POOL-01-v3:29`); Will `saves.dart:124`; DC `5 + Force levels + WIS + CHA` (`FORCE-POWERS-01:240`, app `_castDc`); Heal adds WIS and CHA (`FORCE-POWER-DAMAGE-01:77-79`); drift `alignment.dart:112-117` (`ALIGNMENT-01-v3:232`); "Jedi Force Points" is not our term and Sith have a pool too |
| Charisma | 227: *"A high Charisma increasing the potency of a character's Force Powers. It also reduces the penalty when using Force Powers of an opposing alignment…, and a high Charisma also improves your companions' chance to hit. Finally, Charisma influences a character's Persuade skill."* | *"Charisma represents force of personality. A high Charisma adds modifiers to a character's Force points and the vitality their healing powers restore, and the Force powers of a character with high Charisma are much harder to resist. Charisma also influences a character's Persuade skill."* | Force pool and DC as Wisdom; Heal only, no damage power adds an ability (`PT-2296`); the opposing-alignment cost reads the alignment step alone (`force_cost.dart:26-45`, `ALIGNMENT-01-v3 §1.3`); no companion to-hit rule exists; Persuade is Charisma-keyed (`skills.toml:90`, `SKILLS-01:37`) |

## 3. The hub's tab and row names — APPROVED (owner, 2026-10-18, via MAIN)

**APPROVED:** **Basic Info** (owner-approved, no K2 source) · **Character** (K2 1062) — the tab for our own choices, directly right of Basic Info · **Attacks** (`ATTACKS-01`) · **Force** (K2 1060, the owner's word for Basic Info's row, 2026-10-18; *Force Points* stays approved for prose) · **Languages** · **Homeworld** · **Upbringing**. The strip, in order: Basic Info, Character, Skills, Feats, Attacks, Powers. The draft below is kept as it was proposed.

### The draft as proposed

**The rulings:** the hub is our own page from K2's parts (variant B, the tabs, approved); a new segment for our own choices; its name *"a K2 StrRef or a term in our documents; if neither fits, propose names … for owner approval first."* Searched in K2's `dialog.tlk` (every entry) and our documents.

**Already K2's (no approval needed):** `Custom Character` 240 (the sub-title bar) · `Skills` 233 · `Feats` 232 · `Powers` 1072 · `Skill Rank` 1579 · `Bonus` 32129 · `Total Rank` 41904 · `Vitality` 1061 · `Defense` 1059 · `Character` 1062.

**Not in K2 — proposed, one to choose where there are two:**

| Where | Proposed | Source | Alternative |
|---|---|---|---|
| Tab 1 (portrait, name box, stats) | **Basic Info** — MAIN's working name | none (not a K2 StrRef, not in our documents) | **Character** — K2 1062 (K2's own character-sheet word) |
| Tab 4 | **Attacks** | our documents: `ATTACKS-01`, and the hub step the owner named | — |
| Tab 6 (our own choices) | **Story** | our documents: the Story panel, *YOUR STORY* (`PT-1243`, an approved name) | **Origin** — an approved name, but it is one of the six choices the tab shows |
| Row: Force Points | **Force Points** | our documents: `FORCE-POOL-01-v3` §1 (*"Force points = …"*) | — |
| Rows in Story | **Species**, **Gender**, **Aptitude**, **Background** | approved names (the chargen word list) | — |
| Rows in Story | **Homeworld**, **Upbringing** | approved names *homeworld*, *upbringing*, capitalised as a label | — |
| Row in Story | **Languages** | our documents: `SPECIES-MASTER` §3, *Languages* | — |

When approved: the words go into the chargen text guard's list, each with its source.

## 4. The hub's going-back warning — APPROVED (owner, 2026-10-18, via MAIN), in the form of K2's 109863

**Where:** the K2 confirm box (`K2MessageBox`, OK 1580 / Cancel 1581) that shows when the player reopens a finished step on the hub, changes it and confirms, while finished steps lie after it (owner ruling, 2026-10-18, PLAYTEST-RULINGS-01 `PT-2752` going back).

**No K2 StrRef fits.** I searched K2's and K1's `dialog.tlk` for confirm lines ("Are you sure…", "…will be lost", "Proceed?", "reset"). The nearest is K2's 109863, *"All settings for this character will be lost. Proceed?"* (the hub's Cancel box). It says everything is lost, which is wrong here: only the steps after this one are.

**The draft, in 109863's form:**

> Every step after this one will be lost. Proceed?

**Status:** APPROVED as drafted (owner, 2026-10-18). It follows the form of K2's 109863 (*"All settings for this character will be lost. Proceed?"*). Built in `lib/chargen/hub.dart`; the chargen words guard checks it.

## 5. The name popup's refusal lines and the refused-Play templates — APPROVED (owner, 2026-10-19, via MAIN), as written

The chargen words guard now opens every chargen popup and confirm box (owner, 2026-10-18). The hub's Cancel box (K2 109863), the going-back warning (§4), the feats and powers prompts (K2 48730, 125861) and the granted and recommended boxes pass. **Flagged, with no K2 StrRef saying them:**

- **Organic, empty name:** "A name is required." (`lib/chargen/identity_screen.dart`).
- **Droid designations**, from Lodestar's designation rule (`lib/src/designation.dart`): "A designation for this model is "<prefix>" followed by <n> digits — never a model line, and never one a known droid …"; "A designation on this chassis is letters, digits and hyphens, with no spaces, and never one a known droid already carries."; "A designation is required."; "A designation carries no spaces — …"; "A designation is letters, digits and hyphens only."; ""<name>" belongs to somebody — pick another."; ""<name>" is a model line, not a unit in it."
- **A model with no designation rule** (a data fault): "This model has no designation rule on the shelf — <model>, so nothing can check what you type." **RULED (MAIN, 2026-10-19): developer text, off the player's screen, into the dev log.**

**The hub's refused-Play box** (`K2HelpBox`, `lib/main.dart` 838) shows a frame line and one bullet per STRUCTURAL refusal from Lodestar's validator (`record_validate.dart`, Lodestar c172e58). Rule-limit findings never refuse: the save opens, tagged Modded (owner, `PT-2728` addendum). The fixed templates (`<…>` is filled at run time):

- Frame: "This character cannot be played."
- species exists: "This character is a species this package does not have: "<species>"."
- subrace/chassis present iff required: "<species> needs a subrace or a chassis, and this save names neither." · "<species> has no subrace or chassis to choose, but this save names "<name>"." · ""<name>" is not a subrace or chassis that <species> has."
- exactly one of subrace or chassis: "This save names both a subrace and a chassis; a character has only one."
- model present iff chassis present: "This character has a droid model and is not a droid."
- model valid for that chassis: ""<model>" is not a <chassis> model."
- gender absent iff Astromech or Remote: "A <chassis> droid carries no vocabulator and this one has a voice." · "This character has no gender or voice and its species carries one."
- origin absent iff droid: "A droid has no homeworld and this one has an origin."
- classes non-empty: "This character has no class." · "This character holds a class this package does not have: "<class>"."

Nearest K2/K1 line for any of these: none. K2 has no character-refusal box; the closest is 109863's form.

The help boxes (our help text) stay exempt, as the chargen-text ruling allows; the refused-Play box no longer is: it is checked against these templates.

**Status: APPROVED (owner, 2026-10-19), as written:** "A name is required.", the seven designation lines, and the twelve refused-Play templates with their frame. The data-fault line is not among them: it went to the dev log (MAIN, 2026-10-19). The guard holds the twenty as approved, proving each is seen; any other popup line fails it.

## 6. The Forms step's words — APPROVED (owner, 2026-10-19, via MAIN, `PT-2752`)

K2 has no Forms page: it takes a form as a power on `pwrlvlup_p` (spells.2da rows 258–268), so none of these has a K2 StrRef. Drafted on the mock-ups (`media/study/pt2752/forms-step/`) and approved as written ("Forms look great"):

| Where | Word | Source | K2's nearest |
|---|---|---|---|
| Hub step row and tab | **Forms** | drafted; FORMS-01's own word | — |
| The count | **Remaining Forms** | drafted, in the form of K2's Remaining Powers (1074) | 1074 `Remaining Powers` |
| The select button | **Add Form** / **Remove Form** | drafted, in the form of K2's Add Power / Remove Power | Add Power / Remove Power |
| The list's two section headings | **Lightsaber Forms**, **Force Forms** | **owner-approved 2026-10-20** (`PT-2752`, the Forms list); no K1 or K2 StrRef: both dialog.tlk files searched whole, only the form names themselves ("Contention (Makashi Lightsaber Form)", 111613–111618) | — |

Built in `lib/chargen/forms_screen.dart`; the chargen word guard holds them as approved.

## 7. The Class page's refusal lines — APPROVED (owner, 2026-10-20, `PT-2752`, TEST 189 #2)

TEST 189 found the Class page reading "a droid chassis holds no Force class", lower-case with no full stop. Fixed at its source (`ChargenData.forceBarredReason`; the class screen's one refusal function, `classRefusal`): each line now starts with a capital and ends with a full stop, like the approved refusal texts in §5. Neither game has a line for this: both dialog.tlk files were searched whole for a class refused to a character ("cannot / may not take this class", "holds no Force"), and none matched. Every species against every class gives exactly these three, and `class_refusals_are_sentences_test` fails on any other.

| When | Line | Rule |
|---|---|---|
| A droid, any Force class | **A droid chassis holds no Force class.** | `PT-92` |
| A Rakata, any Force class | **A Rakata holds no Force class.** | `PT-92` (CLASS-ROSTER-01 §3a) |
| A droid, a class its chassis is not open to | **A droid cannot take this class.** | `PT-1464` (DROID-SKILLS-01 §3) |

They show first in the class's description pane, OK dimmed (Class, approved 2026-10-19). **Status: APPROVED by the owner, 2026-10-20, as written** (`PT-2752`); `class_refusals_are_sentences_test` holds the three as approved.

## 8. Our own steps' words — Equipment's "Profession Bonus" APPROVED (owner, 2026-10-22, `PT-2752`)

| Where | Word | Source |
|---|---|---|
| Equipment's second section bar, over the profession's two offers (an item, or an aptitude) | **Profession Bonus** | **the owner's own wording, 2026-10-22** (replacing Coder's drafted "Profession Grant"); no K2 StrRef |

Every other word on the own-steps pages is a K2 StrRef or an approved name already: Species, Subrace, Chassis, Homeworld, Upbringing, Background, Equipment, Standard Gear, Purchase Gear, Male (358), Female (359), Masculine, Feminine, Neither, Try another, CLEAR, Back (219), OK (1580), Cancel (1581).

## 9. The level-up hub's dimmed Attacks row — PENDING (CODER, 2026-10-22, `PT-2752`)

The owner's option 4 puts Attacks on the hub "dimmed, with its reason" until agenda N designs its page. Neither K2 nor our documents carry a sentence for it, so the row is dimmed WITHOUT a reason (as chargen's locked Attacks row is) until one is approved. A tap on the row would show it in K2's one-button message box.

| Where | Draft | Source |
|---|---|---|
| Level-up hub, a tap on the dimmed Attacks row | **"Attacks are not chosen here yet."** | none: ours, for approval |
| Alternative | **"The Attacks step is not built yet."** | none: ours |

> **⚠ §9 is moot (2026-10-23, `PT-2752`):** the Attacks page exists, so the row is live whenever a level brings a pick and absent when it brings none; no dimmed-row line is needed.

## 10. The Attacks page's words — PENDING (CODER, 2026-10-23, `PT-2752`)

The page is K2's Feats grid with the noun "Attack" (§9's mock-up words: "Remaining Attacks", "Add Attack" / "Remove Attack", "Attacks"). The lines below are new; each is shipping as drafted until the owner rules.

| Where | Draft | Source |
|---|---|---|
| OK with an attack pick unspent and something left to take | **"You have gained new attacks. You must use "Add Attack" to select your new attacks before continuing."** | K2's 48730 (Feats), its noun changed — MAIN's own example |
| A refused cell, a non-Force class on a lightsaber chain | **"Any Force class"** | ours, in the form of the prestige refusal's "Any Force base class 6" |
| A refused cell, a base attack gate | **"Base Attack Bonus +1"** | ours; K2's sheet says "Base Attack Bonus" |
| A refused cell, past the class's chain count | **"Chains entered: 14 of 14"** | `CLASS-ATTACKS-01`'s own column, "Chains entered" |
| A refused cell, an ability, a skill, a form, a level, a trait | "Strength 12", "Stealth 6", "Determination", "Character Level 8", "Echani Combat Training", "Cathar" | K2's Prerequisites form (the Feats and Powers panes); the names are the documents' |

## 11. The level-up Class page's new refusal lines — FROM THE DOCUMENTS (2026-10-23, `PT-2752`)

| Line | Source |
|---|---|
| "Neutral or a light band" / "Neutral or a dark band" | the owner's ruling, 2026-10-23, in its own words |
| "Closed to droids" · "Closed to Astromech and Remote" · "Open to Assassin and Battle only" | `CLASS-ROSTER-01 §3b`'s own words |

## 12. The Attacks page's words — SETTLED (owner, 2026-10-23, `PT-2752`; K2's character creation captured the same day, `media/study/pt2752/k2-chargen/`)

| Line | K2 beside it | Status |
|---|---|---|
| **"You have gained new attacks. You must use "Add Attack" to select your new attacks before continuing."** | **48730** "You have gained new feats. You must use "Add Feat" to select your new feats before continuing." — the same line K2 shows on its chargen Feats page (`k2-chargen/14`), word for word | ✓ K2's structure, "attacks" for "feats" and "Add Attack" for "Add Feat" (§10's draft stands) |
| "Any Force class" | none: K2's prerequisite lines name a thing, not a class family | ✓ owner-approved 2026-10-23 |
| "Base Attack Bonus +1" | none in dialog.tlk; the form of K2's prerequisite lines (a name and its value, as "Character Level 6") | ✓ owner-approved 2026-10-23 |
| "Chains entered: 14 of 14" | none; `CLASS-ATTACKS-01`'s own column | ✓ owner-approved 2026-10-23 |

## 13. K2's spend lines, now ours word for word (owner, 2026-10-23, `PT-2752`)

| Page | K2's line | StrRef | Capture |
|---|---|---|---|
| Skills, OK with points unspent (OK / Cancel) | "You have not spent all of your skill points. These will be saved and you may spend them the next time you gain a level. Do you wish to continue?" | 41815 | `k2-chargen/10` |
| Attributes, OK with points unspent (OK) | "You must spend all of your points. Click on the +/- arrows or use the arrow keys to assign points." | 48729 | `k2-chargen/07` |


## 14. The Attacks page's Recommended line — SETTLED (MAIN, 2026-10-23, `PT-2752`, TEST 193)

| Line | K2 beside it | Status |
|---|---|---|
| **"The following attack(s) have been recommended."** | **42256** "The following feat(s) have been recommended." | ✓ K2's line with "attack(s)" for "feat(s)", following the owner's approved pattern for the attacks popup (§12) |

## 15. The Forms tab on in-game Abilities — APPROVED (owner, 2026-10-24, `PT-2752`, the in-game frames batch 2)

| Line | K2 beside it | Status |
|---|---|---|
| **"Forms"** (the fourth tab) | the approved Forms step's word (§6) | ✓ approved with the tab |
| **"Current stance"** (the pane's first line, for the form the character is in) | none (K2 has no stance) | ✓ approved as shown |
| **"Lightsaber Form"**, **"Force Form"** (under a form's name) | the approved headings "Lightsaber Forms", "Force Forms" (§6) | ✓ approved as shown |

## 16. The conversation's own rows on K2's letterbox — APPROVED (owner via MAIN, 2026-10-24, `MAIN-TO-CODER-DIALOG-WORDS`; built at app 03415f2)

Searched in K2's and K1's `dialog.tlk` for each line and its close variants ("[Leave]", "[End conversation]", "End Dialog", "[Walk away]", "Exit", "Goodbye", "[Interrupt]", "Type a reply", "Reactions left"). K2's own tags carry a full stop inside the bracket ("[Leave.]"), as its "[Persuade]" and "[Lie]" lines open their replies.

| Our row | Found | Proposed | Status |
|---|---|---|---|
| Leave | K2 **95603** "[Leave.]" (17 lines use it); K1 29744 "[Leave]", 40075 "[End Conversation]"; K2 87230 "[End conversation, examine the deck.]" (one scene's) | **"[Leave.]"**, K2's 95603 | ✓ a K2 StrRef: ships |
| Interrupt | not in K2; **K1 44792** "[Interrupt.]" (4 lines) | **"[Interrupt.]"**, in K2's form | ✓ **approved** (replaces "[Cut in]") |
| The typed reply | none in either game ("Type" appears only as 917 and the spike-bin names) | **"[Type a reply.]"**, in K2's tag form | ✓ **approved** (replaces "say something…") |
| The reactions left | none in either game ("reaction" is our documents' word: `ATTACKS-01` §10, "The reaction pool") | **"Reactions left: one"** (the count in words) | ✓ **approved** (replaces "costs a reaction — you have …") |
| Continue | not in either game as a tag: K1 and K2 38623 "Continue" (a button, beside 38624 "Back"); K2 76098/76100/76103/76105 "Continue." (one computer scene's replies, not borrowed); "[Continue the Prologue.]" 118954/130731, "[Continue with Loop.]" 84876 | **"[Continue.]"**, ours (`PT-1578`'s control) in K2's tag form | ✓ **ruled** (MAIN, 2026-10-25, `PT-2752`; replaces "[Continue]", whose wording had no approval) |

## 17. The store's accept button — K2's words (MAIN, 2026-10-24)

| Our row | Found | Shipped |
|---|---|---|
| Accept, buying | `store_p` gives `BTN_Accept` the title's 32132 "Buying Items"; K2's running screen sets **125552 "Buy Item"** (capture run `03a`) | "Buy Item" |
| Accept, selling | the same file string; K2's **125553 "Sell Item"** | "Sell Item" |
