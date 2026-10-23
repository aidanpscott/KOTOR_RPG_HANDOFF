# TEST 193, SEVERE, sent ahead of the report: a droid cannot level up

Written for: Main and Coder. App 35c2893.

A Battle-chassis Machinist droid (RX-193, authored with the same species event a chargen droid writes: `{"id":"droid","chassis":"droid-battle"}`, as RX-190's real chargen save has) levelling 6 -> 7: the level-up hub's Skills step shows an empty list and the pane "a droid's skills are gated per species / A droid's skills depend on its body, and only four bodies have a list — astromech, assassin, battle and remote. This droid is on none of them. / this step cannot complete for a droid". OK on Skills is dead, Accept stays dimmed, so the level can never be accepted.

Cause in code: `play_screen.dart:2932` `_droidSkills` looks up `widget.character?.species['id']` ("droid") against `droid_skills.toml` ids ("droid-astromech", "droid-assassin", "droid-battle", "droid-remote"). The chassis field ("droid-battle") is never read, so no droid matches. Chargen's own Skills step uses `droidSkillsFor(r.variant)` and works.

The rest of the droid level-up looked right: Droid Upgrade 2 and Plating Proficiency: Medium granted at 7; facts read Species, Chassis, Model (no Subrace).
