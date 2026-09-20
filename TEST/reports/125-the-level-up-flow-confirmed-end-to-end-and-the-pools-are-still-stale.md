# TEST 125 — the level-up flow confirmed end to end, and the pools are still stale

**Build.** App **`97ee020`** ("the level-up flow reaches play — PT-2484"),
tree clean, built from `git archive` of that sha. The committed lock resolves
Lodestar **`46f0fcea`**, and that is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules
files and 65 standard blueprints.

**Verdict.** **Item 1 confirmed on every clause**, including the cap
boundary. **Item 3 confirmed** — PT-2476 lands, and it closes the "Needed
changes after gaining XP" clause by earning the XP. **Item 2 is not
confirmed: both pools are still stale after a grant through the real flow**,
and the manual path shows it worse than Auto Level Up did.

---

## 1. The level-up screens — every clause

### It drives the real chargen screens

`Level Up` from the sheet opens `CHARACTER GENERATION` / `LEVEL 13`, with a
numbered step list, the grants named, and a `BACK` / `ACCEPT` footer:

```
1 Class        level 13 as Jedi Consular
🔒 Skills      granted   vitality — d6
🔒 Powers                attack and saves — from Jedi Consular's own table
               yours to spend   5 skill points · 1 Force power
```

Class is first and the rest are locked behind it. Each step is a real
screen — `CLASS`, `SKILLS`, `FEATS`, `POWERS`, `ABILITY SCORES` — with its
own `Cancel` / `OK` footer, and `OK` stays dim until the step's budget is
fully spent.

### The step set is the class's own

Three level-ups, three different sets:

| level-up | steps |
|---|---|
| 13 as Jedi Consular | Class · Skills · **Powers** |
| 13 as Soldier | Class · Skills · **Feats** |
| 16 as Jedi Consular | Class · **Abilities** · Skills · Powers |

Abilities appears only on the fourth levels — 12 → 13 offers none, 15 → 16
does, with *"1 ability point, to a maximum of 23"*.

### Changing class mid-flow discards and reshapes — measured

Spent under Jedi Consular first: 5 skill points, all of them (Alertness 4,
Archaeology 1), Skills ticked ✓. Then Class → Soldier → Accept:

```
                    before (Consular)        after (Soldier)
  header            level 13 as Jedi Consular  level 13 as Soldier
  vitality granted  d6                         d10
  skill points      5                          3
  third step        Powers · 1 Force power     Feats · 1 feat
  Skills tick       ✓                          gone, back to step 2
```

And re-entering Skills shows the spend is genuinely gone, not just
re-tickable:

```
points remaining 3 of 3     Alertness 0     Archaeology 0
```

⚠ Archaeology also stopped being a class skill — it reads `2/rank · cap 2`
under Soldier where it read `1/rank · cap 4` under Consular, and Athletics
became one. The class-skill set reshapes with the rest.

### Abilities ignores the creation-time cost ladder

At level 16 with exactly **1** ability point and a character already at
Wisdom 18 and Charisma 18, **every** ability shows an enabled `+`. One click
on Wisdom:

```
Wisdom   bought 18 → 19    total 19    bonus +4     points remaining 1 → 0
```

An 18 → 19 step cost exactly the one point and was not refused. Under the
creation ladder that step costs several, and the `+` would have been
disabled — which is the thing this clause exists to catch.

### Accept writes the level, the class and every choice

Not read off a screen — decoded from the save the app wrote. From the
Soldier run:

```
character.levelled    {level: 13, class: "soldier", xp: 80000}
character.skill-ranked {skill: "alertness", ranks: 3}
character.feat-taken   {id: "close_combat", source: "chosen", at_level: 13}
```

and from the level-16 run:

```
character.ability-set  {ability: "wis", score: 19}
character.skill-ranked {skill: "alertness", ranks: 4}
character.skill-ranked {skill: "archaeology", ranks: 1}
character.power-taken  {id: "battle_meditation", at_level: 16}
```

Every kind of choice is written — class, ability, skill, feat, power — and
**nothing from the discarded Consular spend appears anywhere in the log.**
Both survive a reload: the character comes back at 13 and 16 with those
values.

### The cap — genuinely absent

At level 30 the viewport carries **no buttons at all**: no `Level Up`, no
`Auto Level Up`, and no reason line under them. Not greyed, not explained —
absent, which is right when there is no level to spend.

## 2. The pools are still stale — item 2 NOT confirmed

Two runs, each measured at three moments:

| | before | immediately after Accept | after reload |
|---|---|---|---|
| **12 → 13, class changed to Soldier** | | | |
| vitality | 86 / 86 | **86 / 86** | **93 / 93** |
| force | 159 | **167** | 167 |
| **15 → 16, class unchanged** | | | |
| vitality | 107 / 107 | **107 / 107** | **114 / 114** |
| force | 198 | **206** | **211** |

**Vitality never refreshes.** It holds the previous level's maximum until
the save is reloaded, in both runs — 7 points short each time.

**And force is worse than it looks.** In the first run its immediate 167
happened to be the final value. In the second, Accept showed **206** and the
reload showed **211**: not merely stale, but a *different wrong number* that
a player has no reason to distrust.

So PT-2474's fix does not hold through the manual flow. The grant itself is
correct and persisted — the reload proves that — but a player who levels up
mid-session fights on last level's vitality and a force pool that is wrong
in a third way.

## 3. PT-2476 — confirmed, and it closes the XP clause

One fight on `m06-xp`, won by two Force Screams with no weapon held. The
fight now announces itself:

```
frail.xp.01 falls
```

and the log carries the whole outcome that was missing in TEST 123:

```
encounter.ended {subject: frail.xp.01, encounter: m06-xp, vitality: -10}
encounter.ended {subject: Whisper, vitality: 85, force: 143, force_ceiling: 157}
character.died  {subject: frail.xp.01, encounter: m06-xp, x: 1, y: 0}
character.xp-awarded {subject: Whisper, amount: 25, from: frail.xp.01,
                      cr: 1.0, level: 12}
```

**25** is exactly the floor of the level-12 row I predicted from
`xp_awards.toml` before running it, and the derivation rides the event.

And on the sheet:

```
Experience   66000 → 66025
Needed       12000 → 11975
```

`Needed` now moves because XP was **earned**, which is how this clause was
always meant to be closed rather than by the two-save workaround in TEST
123.

## Also noticed

* **The level-up Class list offers twelve standard base classes and no Force
  class.** `baseClasses` is documented as *"the 19 classes a character can
  start in"* and includes the three Jedi; the level-up list shows Soldier
  through Duelist only. So a Jedi can multiclass out through this screen and
  not back in.
  ⚠ **I checked whether that traps a player, and it does not:** continuing
  as the current class is the default (entering Class and pressing `Cancel`
  confirms it and ticks the step), and `BACK` on the step page abandons the
  whole level-up — after switching to Soldier and pressing BACK the
  character was untouched at `Jedi Consular · 12 · 86 of 86 · force 159`,
  with the level still unspent. Reporting the shape, not a defect.
* **A multiclass is invisible in the UI.** After the Soldier level the party
  card and the sheet header both still read `Jedi Consular · 13`, and
  `Character Info` shows only Species and Gender. The log has
  `class: "soldier"`; nothing on screen does.
* **The Powers list prints `null` as a cost** for the unpriced powers —
  `Crush Opposition II`, `III` and `IV` show a literal `null` in the cost
  column where the priced ones show a number.

## Fixture

`tester-mind`, and `mk123.py` gains an **`abil`** mode — level 15 with
120000 XP — because an ability point is granted only every fourth level and
the `unspent` fixture at 12 → 13 offers no Abilities step at all. The
existing `unspent`, `cap` and `owed` modes covered the rest, and `m06-xp`
did the fight unchanged.
