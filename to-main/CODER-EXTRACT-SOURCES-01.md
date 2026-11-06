# Extract sources, for MAIN and DOCS (CODER, 2026-11-06, PT-2752)

Read from the scripts at MAIN_WORK eb203e9f, plus the sources each file in data/extracted declares.

## The answer Docs is waiting on

No extract script reads any ATTACKS-0x document. attack_tiers reads data/attacks.json only, and its only other input is force/FORMS-01 (form names, for the "Requires the X form" gate).
No extract script reads ACTION-ECONOMY-01, ATTACKS-01 or RULES-01-v2. extract_powers and extract_item_effects name RULES-01-v2 in comments and messages only.
So the AS BUILT blocks in ATTACKS-04 and ATTACKS-05 can move as Docs moves the others. Nothing extracts them.
The line numbers are off by one or so: at 76a3778 and now, ATTACKS-04 :54, :91, :164 and ATTACKS-05 :51 are blank lines. The block opening sits on the next line. Find each by its text.

## Other scripts that read the ATTACKS documents (not extracts; keep these working)

audit_names.py (gate): every table row whose first cell is bold, in ATTACKS-04 to -07. A row moved or renamed changes its count.
audit_source.py (gate): row names in ATTACKS-07, and the rosters by document.
audit_ownership.py (advisory): needs "## Velocity — More shots" in ATTACKS-04, "## Velocity — More attacks" in ATTACKS-05, "declare one attack" and "replacement principle" in ATTACKS-01, and "a stunned character loses", "a prone character takes", "unaware of you if" in ACTION-ECONOMY-01. An as-built move that keeps the words in the same document stays clean.
audit_preflight.py (advisory): looks for "Once per encounter" in ATTACKS-04 and -05.
audit_revision.py (gate): lists these documents as play-facing.
check_citations.py (advisory): checks that a cited section exists, so a moved section can break a citation.
gen_docs.py: would overwrite ATTACKS-04 and -05, whose headers say DO NOT REGENERATE (PT-627). Do not run it.

## The extract scripts that read a document

There are 54 extract_*.py scripts, not 17. 23 read a rule or design document, listed here. The other 31 read K2's files, saves, 2DA or .gui files, or another extract.

| Script | Document | What it reads |
|---|---|---|
| extract_chassis | design/CHARGEN-DATA-01 | the section whose ### heading carries PT-1403 |
| extract_first_level_feats | design/CHARGEN-DATA-01 | the ## section carrying PT-1407 |
| extract_designations | design/CHARGEN-DATA-01; rules/DROID-MODELS-01 | a table found by heading; the §0c reserved list and §2 |
| extract_event_kinds | design/EVENT-KINDS-01 | ### headed tables |
| extract_classes | rules/CLASS-ROSTER-01, CLASSES-STANDARD-PHB, CLASSES-FORCE-PHB, CLASS-TABLES-JEDI, -AUTHORED, -BASE, -DROID, SKILLS-01, FEAT-SCHEDULE-01, PRESTIGE-DESCRIPTIONS-DRAFT-PT2752, CLASS-ATTACKS-01 | numbered ## chapters, "## Class skills", and the class tables |
| extract_skills | rules/SKILLS-01 | §1, §9.2, §9.2b, §9.2c |
| extract_droid_skills | rules/DROID-SKILLS-01 | §2.1 to §2.4 |
| extract_equipment | rules/EQUIPMENT-01 | §2, §4, §4b, §4c, §5, §5.2, §7b, §8, §9, §15 and more, by heading |
| extract_item_effects | rules/ITEMS-01 to -09; rules/EQUIPMENT-01 | item rows; §9a and §9b (poison) |
| extract_item_gates | rules/ITEMS-01 to -09 | item rows |
| extract_items | rules/ITEMS-01 to -09 | every "## Name — number" table |
| extract_feats | rules/FEATS-LIBRARY-01 | numbered headings 1 to 5, 5a to 5c, and every chain row under them |
| extract_forms | force/FORMS-01 | the form tables and "### ⚠⚠ 6.2b" |
| extract_powers | force/FORCE-POWERS-01 | every power row and its prose |
| extract_power_order | force/POWER-GRID-ORDER-01 (with powers.json, k2_spells.2da) | the document's order |
| extract_models | rules/DROID-MODELS-01 | numbered ## chassis sections |
| extract_professions | rules/PROFESSIONS-01 | §0, §1, §3b |
| extract_programmings | rules/PROGRAMMINGS-01 | §1 |
| extract_species | rules/SPECIES-CHAPTER-v2 | ### species sections |
| extract_starting_equipment | rules/STARTING-EQUIPMENT-01 | §1, §2, §2c, §4, §4a, and the headed droid arrays, A and B |
| extract_upbringings | rules/UPBRINGING-01 | "## 2 · The nine" |
| extract_upgrade_slots | rules/UPGRADE-SLOTS-01 | ## headed tables |
| extract_upgrades | rules/WEAPON-MATRIX-01 | §1, §3 |

## For Docs' lane

Every extract above fails or changes if a heading it finds moves or is reworded. Treat those headings and table shapes as fixed, or list the change for Coder.
check_extracts.py reports a stale extract after any edit to these documents, including prose. Docs editing one means an extract must be rebuilt, which is my lane: list it.

## How far this was checked

The sections are read from each script's heading patterns, not traced through every line. The "does not read" answer is firmer: grep over all extract scripts, and the sources declared in data/extracted.
