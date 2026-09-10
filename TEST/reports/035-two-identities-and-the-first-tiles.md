# 035 · Two identities in one encounter — and I finally painted tiles, which found a third thing

**From `Tester`. Unrequested number.** `PT-1512` followed: packages to `BK11/`,
saves to `SV-T034/`, before anything was opened.

**⚠⚠ BUILT AND MEASURED AGAINST:**

    §1–§2  app 919b55d · Lodestar fc32da0 · Lens 5534554     built 12:55, tree CLEAN
    §3–§5  Loom 09d9fac (pins Lodestar fc32da0)              built 13:01, tree CLEAN

**Both builds were made on clean trees with `resolved-ref` checked against
`Lodestar` HEAD.** As I write: app `919b55d` **(2 dirty)**, `Lodestar fc32da0`
**(2 dirty)**, `MAIN_WORK b57eb86`, `HANDOFF d2c2284` — **`BUILD 101` landed
while I wrote and nothing here is against it.**

**⚠ CONTAMINATION.** `probe-walker.sav` rewritten twice and **Probe Walker
killed once**. All 20 saves restored from `SV-T034/`, byte-identical. Three
deliberate package fixtures remain — `§7`.

---

# ⚠⚠ 1 · THE ANSWER: ONLY THE NAME. AND BOTH IDENTITIES PRINT IN ADJACENT LINES

**You asked whether a wrong `owner` gets the wrong creature's doctrine,
equipment or vitality, or only the name. ⚠ Only the name — and I have it on
screen with both identities visible at once.**

**I authored a deterministic fight branch into `sentinel-challenge.toml` so the
comparison would not wait on a Persuade roll**, and gave `probe-sentinel` a
distinctive `override = 33` **so that a leaked RECORD would show as a number and
not merely a label.**

    panel header      PROBE-SENTINEL.PROBE-ROOM.04     ⚠ the file's owner
    the line          "Then we do this the other way."
    the blow          probe-warden.probe-room.03: unarmed · rolled 17
                      — d20 16 + attack 1 + Strength 0 · needed 14 — hit
    status bar        probe-sentinel.probe-room.04: 3 of 33   ⚠ UNCHANGED

> **⚠⚠ THE PANEL NAMES ONE CREATURE AND THE ROUND FIGHTS ANOTHER, TWO LINES
> APART. The sentinel's 33 never moves — it is not in the encounter at all.**

## The split is exactly one line wide

    dialogue_run.dart:511   speaker: line.by ?? conversation.owner    ⚠ THE NAME
    play_screen.dart:889    final who = _talkingTo;                   ⚠ EVERYTHING ELSE
    play_screen.dart:892    if (who != null) _begin(who);

**`_talkingTo` is the placement walked into, so doctrine, equipment, vitality,
initiative and reach all follow the real creature.** ✅ **And the save agrees** —
`encounter.ended {"subject": "probe-warden.probe-room.03", "vitality": 8}`.

> **⚠ So it is two identities in one encounter and only one of them is
> mechanical. The wrong one is the only one the PLAYER reads.**

**⚠ And `PT-1562`'s Aurora comparison sharpens it:** Aurora joins a conversation
to a creature with **two closed dropdowns**. Ours is **one text box, on the file
side only** — and the blueprint's `conversation` key is the *other* half of the
join, with **nothing checking the two agree.**

**⚠ Coder is mid-flight on this.** `Lodestar`'s working tree carries
`conversationOwnerUnknown` and `conversationOwnerNotTheSpeaker` — **see `§6`,
because I nearly filed something false about them.**

---

# ⚠⚠ 2 · AND WHILE PUSHING IT I FOUND THAT A CONVERSATION WRITES NOTHING TO THE SAVE

**`dialogue.choice-made` is declared `lifetime = "campaign"` in the SHIPPED
`event_kinds.toml`. `encounter.began` is too. Neither reaches the file.**

**Measured — every event kind in `probe-walker.sav` after a session in which I
made a dialogue choice that started a fight:**

    character.created · species-set · class-added · origin-set · gender-set
    backstory-set · ability-set ×6 · skill-ranked ×4 · feat-taken
    grant-resolved · equipment-set · identity-set
    encounter.ended ×8 · character.revived ×4 · character.moved ×2

> **⚠⚠ ZERO `dialogue.choice-made`. ZERO `encounter.began` — against EIGHT
> `encounter.ended`. Every fight in this file ends and none of them begins.**

## The mechanism, and it is `PT-1448`'s defect one path over

**`onAppend` takes the events to persist. The dialogue path never calls it:**

    play_screen.dart:811   _log.addAll(b.events);              _startTalk   ⚠ no onAppend
    play_screen.dart:847   _log.addAll(next?.events ?? const []); _pick      ⚠ no onAppend
    play_screen.dart:878   _log.addAll(next.events);            _continue    ⚠ no onAppend

    play_screen.dart:1749  _log.addAll(made);  + 1544 onAppend(made)   ✅ the fight path
    play_screen.dart:1915  _log.addAll(made);  + 2022 onAppend(made)   ✅ the outcome path

**`PT-1448`'s own comment is three lines from one of the good ones:** *"`_writeOutcome`
put the event in the in-memory log and **only the fight-is-over path handed it
up**, so the outcome of every fight a player WALKED OUT of died with the
process."*

> **⚠⚠ THE SAME SENTENCE IS NOW TRUE OF EVERY CONVERSATION EVER HELD. The engine
> writes the event, the format declares it campaign, the screen puts it in
> memory, and nothing hands it up.**

**⚠ And it is not cosmetic. `dialogue.choice-made` is the ONLY record that a
conversation happened** — `§5` forbids an author naming it, so there is no
second channel. **A gate reading "have I already asked this" has nothing to read
after a reload.**

---

# ⚠⚠ 3 · I PAINTED TILES. TEN SESSIONS LATE, AND IT WORKS

**Straight answer first: ✅ it is good, and it does the thing Aurora does.**

**One click on a 4×4 area whose `[tiles]` was `default = "floor"`:**

    [tiles]
    legend = { "." = "floor", "#" = "wall" }
    map = """
    ....
    ....
    ..#.
    ....
    """

> **⚠ ONE CLICK CONVERTED A DEFAULTED AREA INTO A FULL TEXT MAP — and the legend
> holds ONLY the glyphs the map uses.** Not all five. `AREA-FORMAT-01 §2`'s
> notation, minimal, and every arrival, connection and placement preserved.

**Painting the other three grew the legend in `TileType.values` order and never
reordered it:**

    legend = { "." = "floor", "#" = "wall", "~" = "water", ":" = "difficult", "!" = "hazard" }

**✅ AND IT DRAG-PAINTS.** One press-drag-release across row 1 wrote `####`.
**That is the Aurora parity question answered: the affordance is the same one.**

---

# ⚠⚠ 4 · AND THE DRAG PAINTED OVER A CREATURE, AN ARRIVAL AND A DOORWAY. VERIFY REPORTS NONE OF THE THREE

**The drag started at `0,1`. `probe-feeble.probe-hall.02` is placed at `0,1`.**

| I painted a wall on | Loom | `Verify`, pressed fresh |
|---|---|---|
| a square holding a **creature** | ⚠ **silently allowed** | ⚠ **8 problems, not one of them** |
| the **arrival point** `from-probe-room` | ⚠ **silently allowed** | ⚠ **8 problems, not one of them** |
| the **doorway** `door.probe-hall.01` | ⚠ **silently allowed** | ⚠ **8 problems, not one of them** |

**The board draws it plainly — a grey wall band across row 1 with the creature's
token inside it — and the count never moved.** I pressed **`Verify again`** and
read all eight: six in `a01`, two in `a04`, **nothing in `a02`.**

## ⚠ And the validator has no member that could say it

**Every one of the 13 `PackageProblem` members in the build is about a NAME
resolving:**

    blueprintMissing · blueprintUnreadable · equipmentMissing · referenceMissing
    areaFileMissing · areaUnreadable · targetAreaUnknown · targetAreaUnreadable
    landingPointUndeclared · duplicateArrivalName · entryUndeclared
    entryAreaUnknown · requiredFieldMissing

> **⚠⚠ NOT ONE IS ABOUT A POSITION BEING USABLE. `landingPointUndeclared` checks
> that a door's landing is DECLARED and not that it is STANDABLE — the same
> field, one step short.**

## ⚠⚠ AND IN PLAY IT IS AN AREA YOU CAN ENTER AND CANNOT LEAVE

**Walked `a01 → a02` through `door.probe-room.05`:**

    Probe Hall — arrived at from-probe-room        ⚠ and I am standing IN the wall
    press Right, toward door.probe-hall.01:
    the wall blocks the way                        ⚠⚠ THE ONLY EXIT IS BEHIND A WALL

**The arrival placed me inside an impassable square without a word, and the
connection out is refused by the tile painted on top of it.** The only square I
could enter was the one holding a hostile creature.

> **⚠ The refusal sentence is correct and the situation is not.** *"The wall
> blocks the way"* is exactly right about the square and says nothing about the
> fact that it is a door.

**⚠ Shape it wants:** the tile map and the placements are validated
independently and **nothing checks one against the other.** Three faults fall
out of one rule — *a square that a placement, an arrival or a connection names
must be passable* — and the cheapest place is Loom's brush, which knows what is
under the cursor. **A refusal at paint time costs one comparison; a fourteenth
`PackageProblem` catches the packages already written.**

---

# ⚠ 5 · Two smaller things from the same hour

**✅ `PT-1575` IS WORKING IN VERIFY, seen in the fault list:** *"`zoo-empty.probe-room.15`
… is placed from `characters/zoo-empty`, and **that blueprint cannot be read:
The file has no [character] section**."* **That is `027 §2`'s thirteenth
problem, landed, quoting the reader's own refusal.**

**✅ And the digit rule held again** — `3` picked the third reply while the typed
box was empty, and the check said its own arithmetic on the earlier attempt:
**`⚠ Persuade failed — 5 needed 14 (d20 5)`**.

---

# ⚠⚠ 6 · AND I NEARLY FILED SOMETHING FALSE. THE INSTRUMENT WAS A DIRTY FILE

**I read `Lodestar/lib/src/package_validate.dart` and found FIFTEEN
`PackageProblem` members, two of them mine — `conversationOwnerUnknown` and
`conversationOwnerNotTheSpeaker`. Verify had just reported 8 without either.**

**⚠ I was one step from filing *"Coder landed the check and it does not fire."*
Instead I asked what the build actually contained:**

    Loom binary built                 13:01
    Lodestar/lib/src/package_validate.dart mtime   13:07   ⚠⚠ SIX MINUTES LATER
    git log -S "conversationOwnerNotTheSpeaker" --all  →  NOTHING
    ~/.pub-cache/git/Lodestar-fc32da0…/…/package_validate.dart  →  13 members

> **⚠⚠ THE MEMBERS ARE UNCOMMITTED WORK IN CODER'S TREE. `Verify`'s 8 WAS
> CORRECT. I read a file the build had never seen.**

**⚠ And the useful part is the third state.** I have been checking
`pubspec.lock`'s `resolved-ref` against **local `git HEAD`** — two things — while
the binary is compiled from **a third**, the pub-cache checkout of that ref.
**Those three agree only when the tree is clean**, which is exactly the condition
I already insist on, **and reading a source file is not covered by it at all.**

---

# 7 · Scoped negatives, and what I left behind

- **⚠ The `owner` finding is my own package.** `026`'s `endar-spire` orphan —
  the ABSENT case — **is still measured only there and I did not re-open it.**
- **⚠ I did not test a wrong owner whose creature has DIFFERENT equipment.**
  Both are unarmed, so `§1` rests on the **tag** and on the sentinel's `33` not
  moving, not on a weapon difference.
- **⚠ `§2` is a save read plus a source census.** I did not instrument `onAppend`;
  I inferred the mechanism from three call sites with no `onAppend` beside them
  and confirmed the consequence in the file.
- **⚠ Whether `encounter.began` is ALSO lost from the fight-started-by-walking-in
  path** — untested. My fight began from a conversation, so both losses share a
  cause here.
- **Painting over a placement in an area with a TILESET** — every area in
  `tester-probe` says `no tileset`. **Untested.**
- **Whether Loom refuses a wall on the ENTRY area's start square** — not tried.
- **`PT-1596`'s second sentence** — still unreachable; `034 §3` stands and I did
  not retest it.
- **The item dialog and doors/waypoints** — **not re-checked on `09d9fac`.** Last
  measured `0dd361b`, `034 §4`.

## What I left behind — three fixtures

    a02-probe-hall   ⚠ row 1 is a PAINTED wall band with probe-feeble INSIDE it
                       at 0,1. Row 0 restored to floor so the a01 round trip
                       still works — the trap is reproducible by painting 0,0
                       and 1,0 again, and the comment in the file says so.
    probe-sentinel   ⚠ vitality override 33 — a DISTINCTIVE number, so a leaked
                       record shows as a number rather than only a label.
    sentinel-challenge.toml  ⚠ a third reply, "I am not going anywhere",
                       reaching a node with effect = [{ kind = "encounter.began" }]
                       — a DETERMINISTIC fight, so §1 needs no lucky roll.

**⚠ The wall band is the fixture I most want kept.** It is one drag, it is
invisible to `Verify`, and it puts a creature in a wall in a package that
otherwise passes.

**Backups: `BK3/`–`BK11/`, `SV-T031/`–`SV-T034/`.**
