# 028 · The palette lists what is on disk — six ways, and one of them is placeable

**From `Tester`. Unrequested number.** `PT-1512` followed; packages backed up to
`BK5/` before anything was touched.

**⚠ BUILT AND TESTED AGAINST — and this is the only build these findings hold
for:**

    Loom 84f49ec · Lodestar 9ef2fd2 · Lens 6b55219

**⚠⚠ THE APP WAS NOT BUILT AND NOTHING HERE IS AN APP FINDING.** At 09:48
`KOTOR-RPG-APP/lib/play/play_screen.dart` had an mtime of **09:48** — Coder was
wiring `PT-1573` as I started. **I did not build a tree being edited.**

**⚠ And the tree moved again while I worked.** `Loom` was **`84f49ec`** when I
built and is **`1f9178f`** as I write; the app is **`355f370`**. **Say what you
built against, every time** — so: everything below is `84f49ec`.

---

# ⚠⚠ 1 · PT-1575 WIDENED — the palette lists what is on disk, and six shapes prove it is a category

**You asked what else the palette lists that nothing can use. I built a zoo of
six and put them all in `blueprints/characters/`.**

| fixture | what it is | TOML | listed? |
|---|---|---|---|
| `zoo-unparseable.toml` | `str = 1 ; dex = 2` | **refused** | **⚠ listed** |
| `zoo-empty.toml` | **zero bytes** | parses to `[]` | **⚠ listed** |
| `zoo-comment-only.toml` | one comment line | parses to `[]` | **⚠ listed** |
| `zoo-no-name.toml` | `[character]`, **no `name`** | parses | **⚠ listed** |
| `zoo-wrong-kind.toml` | **`[item]` in the characters folder** | parses | **⚠ listed** |
| `zoo-directory.toml` | **a DIRECTORY** | — | ✅ **not listed** |

**The palette's `creatures` group offered TEN entries. Four work. Six do not,
and all ten are drawn identically:**

    probe-anvil · probe-doubled · probe-sentinel · probe-warden
    zoo-comment-only · zoo-deep-equip · zoo-empty · zoo-no-name
    zoo-unparseable · zoo-wrong-kind

> **⚠ It is not "unparseable" that is the case. It is `.toml` on disk.** A file
> with nothing in it, a file that is only a comment, a file missing the one
> required field, and a file of the **wrong kind entirely** are all creatures as
> far as the palette is concerned.

**✅ The one case it gets right: a DIRECTORY named `x.toml` is excluded.** So the
lister does test file-vs-directory. **It simply never asks whether the file
parses, or whether what parsed is a creature.**

**⚠ And `Verify` reports NONE of them.** Five problems before the zoo, five
after — the same five, every time, across two explicit `Verify again` presses.

## ⚠⚠ AND THEY ARE PLACEABLE. I placed a zero-byte file into an area

**One click on the board, with `zoo-empty` armed, and Loom wrote:**

    [[contents]]
    tag  = "zoo-empty.probe-room.15"
    from = "characters/zoo-empty"
    at   = [2, 4]

**`characters/zoo-empty` is a file with no bytes in it.**

**⚠⚠ AND LOOM'S OWN PALETTE SAYS WHY THAT IS WRONG, THREE INCHES TO THE RIGHT.**
Under `encounters`, `placeables`, `sounds`, `stores` and `triggers` it prints:

> *"a placement names a blueprint by path — `§3` — and this kind has no format,
> so there is nothing a placement could name. **Painting one would write a
> reference nothing can resolve.**"*

**That is exactly what it just let me do** — for a kind that *has* a format,
with a file that does not.

**⚠ Verify still said 5.** Neither gate catches it, and I read why in `027`:
`blueprintMissing` asks `existsSync()` and **the file exists**; the equipment
loop does `if (opened is! OpenedCharacterResult) continue;` and **skips what it
cannot open**. *Exists* and *cannot be opened* are both true, and neither is
reported.

**⚠ Shape it wants:** the lister and the validator disagree about what a
blueprint is. **One of them should be the other's caller.** If the palette
listed what `openCharacter` accepts, five of the six vanish; the sixth
(`zoo-wrong-kind`) needs the opener to say which table it found.

---

# ✅ 2 · NESTING AT DEPTH — the pane, the dialog AND the reader all agree

**`PT-1567` holds on all three surfaces. This is a clean pass.**

**PANE** — `blueprints/items/weapons/heavy/repeater/probe-cannon.toml`, three
folders past `items/`:

    ▼ items
      ▼ weapons
        ▼ heavy
          ▼ repeater
              deep-repeater
              probe-cannon
        blaster-rifle
        vibroblade

**⚠ Folders sort before files at every level**, which is the readable order.

**DIALOGUE** — `New item` created one at that depth. `path` is free text and
**must carry the leaf**; it does not compose with `name`. Given
`items/weapons/heavy/repeater/deep-repeater` it wrote the file, and **the
palette showed it nested and auto-selected** — the created thing is where you
are looking, the same as a placement.

**READER** — a creature equipping
`items/weapons/heavy/repeater/probe-cannon`, placed in an area: **`Verify`
reports no `equipmentMissing`.** The reader resolves the deep path.

## ⚠ But the dialog's refusal is still below forty base types — `016`, unchanged

**My first attempt used `items/weapons/heavy/repeater/` — a folder, no leaf.
`Create` did nothing: no file, no status line, no visible message.** I scrolled
the dialog body and found it at the very bottom, in red, **below all ~40 base
types and below a `description` field**:

> **"An item needs a path — where it lives IS what it is."**

**`Create` is pinned in the action row where I clicked.** The dialog refused me
and **the refusal was invisible from the button**. That is report `016`'s
finding, unchanged, on a build eleven slices later.

**⚠ It is `D8`'s rule turned around.** *Anything you can click must be laid out
where it can be seen* — and **anything that says why a click failed must be laid
out where the click was.**

---

# ⚠ 3 · DOORS AND WAYPOINTS — still both lines, confirmed on a fresh build

**You asked again. The answer is the same as `027 §4`, re-checked on `84f49ec`:**

    ▼ doors
        painted as `doorway` above — §4a and §4·0 make it a way, not a blueprint
        ⚠ cannot list — no folder is specified for this kind yet, …

    ▼ waypoints
        painted as `arrival point` above — §4a and §4·0 make it a way, not a blueprint
        ⚠ cannot list — no folder is specified for this kind yet, …

**The correct sentence was added. The wrong one was not removed.** For the five
genuinely-inert kinds *"no folder is specified **yet**"* is true; for these two
it is **false**, because `§4a` makes them a way permanently and there will never
be a folder.

---

# ⚠⚠ 4 · THE CONVERSATION WIZARD TAKES A FREE-TEXT `owner` — and this is how `endar-spire`'s orphan was written

**`PT-1559`, built from `STUDY 29`'s Store Wizard finding. I had never opened
it. It is good, and it has one fault that matters a great deal.**

## The good part first, because it is most of it

    What do they say when the conversation begins?
    <owner> speaks it — §1, and it is a placement tag.
    the first line
    [ You are not supposed to be here. ]        ⚠ PREFILLED, working content

    Does this line have replies, or does it continue?
    replies are SHOWN ALL AT ONCE and the player picks; a continuation hands
    straight on to another line they say. A line carries one or the other —
    the reader refuses both.
    [ the player answers ]   [ they keep talking ]

**It asks in the domain's language, prefills content that works, and explains
both options in a sentence that names what the reader does.** That is Aurora's
Sound Wizard shape and **better than it** — Aurora explained the options;
this explains the consequence.

## ⚠⚠ And the fault

**`owner` is a bare text box. I typed `not-a-real-tag-at-all` and it was
accepted** — and the wizard then printed, underneath:

> **"not-a-real-tag-at-all speaks it — §1, and it is a placement tag."**

> **⚠⚠ IT CITES THE RULE AND DOES NOT ENFORCE IT, IN THE SAME SENTENCE.**

**`026 §2` filed the consequence and could not explain how such a file gets
written. This is how.** `endar-spire/dialogue/trooper-challenge.toml` names
`sith-trooper.command-deck.07` against an area holding only `.39` — **a typed
owner, never checked, exactly as I just typed one.**

**⚠ And the vocabulary is not merely closed — it is enumerable in the same
window.** Every placement tag in the package is in the module tree three inches
to the left of the field. **`PT-1571` just replaced a typed skill name with a
list for the eight checks; this is the same shape, one surface over, for a
vocabulary Loom already has in memory.**

**⚠ Nothing was written.** I left the wizard before it created anything;
`dialogue/` still holds only `sentinel-challenge.toml`.

---

# ⚠ 5 · Two smaller old shapes

**⚠ "There is no conversation here." is drawn in ALERT RED on the CREATE
surface.** I pressed `+` to make a new conversation and was told in red that
there is not one. **Nothing is wrong; an error colour is doing an invitation's
job.** The palette's inert kinds say the same class of thing in calm prose.

**⚠ The entry-area chooser is still below the fold — `D8`, still open.**

> **I must correct myself here.** I first wrote that `Package properties` shows
> `entry area · where a new game begins` **with no control**. **That was wrong —
> I had not scrolled.** The control is a radio group over every area with the
> current entry marked:
>
>     ● a01-probe-room  ○ a02-probe-hall  ○ a03-probe-yard  ○ a04-probe-slit
>
> **`PT-1380` is satisfied and the control is correct.** It is **below the
> fold**, which is the `D8` I filed and `BUILD/41` listed as not fixed. **Still
> not fixed, and now with a second dialog doing it** — see `§2`.

**✅ `assistant` says "not built yet".** One line, honest, no old shape.

---

# 6 · Scoped negatives

- **The app.** Not built, not run, nothing here is an app finding. `PT-1573`'s
  find-on-approach is in `Lodestar 9ef2fd2` and was being wired into the app as
  I started; **I am waiting for it rather than chasing it**, as instructed.
- **`zoo-wrong-kind` in play.** I confirmed the palette lists an `[item]` as a
  creature; **I did not place it** and do not know what the app does with one.
- **`zoo-directory.toml`** — confirmed excluded from the palette; **I did not
  check whether `Verify` or the app trip over it.**
- **The Standard/Custom split.** `tester-probe` supplies no standard content, so
  I have still only seen one side. **A package with both is untested.**
- **The conversation wizard past step 2** — I left rather than create.
- **`New area`** (`areas +`) — never opened.
- **Painting tiles in Loom** — still not done, four sessions running.

---

# 7 · What I left behind

**`tester-probe` now carries a deliberate zoo. Every file is a fixture:**

    blueprints/characters/
      zoo-unparseable.toml     invalid TOML
      zoo-empty.toml           zero bytes
      zoo-comment-only.toml    one comment
      zoo-no-name.toml         [character], no name
      zoo-wrong-kind.toml      [item] in the characters folder
      zoo-directory.toml/      a DIRECTORY  ⚠ the control — correctly excluded
      zoo-deep-equip.toml      equips items/weapons/heavy/repeater/probe-cannon
      probe-doubled.toml       equips items//weapons/vibroblade  ⚠ 027 §1

    blueprints/items/weapons/heavy/repeater/
      probe-cannon.toml        depth fixture, hand-made
      deep-repeater.toml       depth fixture, made BY LOOM

    a01-probe-room  tag_seq 16, 11 placements, including
      zoo-empty.probe-room.15       ⚠ points at a zero-byte file
      zoo-deep-equip.probe-room.16  ⚠ the reader test

**⚠ `zoo-empty.probe-room.15` is left placed on purpose.** It is the shortest
proof of `§1` in the package: **open `tester-probe` and Loom will tell you it
has five problems.**

**Backups: `BK3/`, `BK4/`, `BK5/` in the session scratchpad.**
