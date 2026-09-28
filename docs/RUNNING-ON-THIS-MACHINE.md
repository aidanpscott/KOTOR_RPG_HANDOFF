# Running on this machine — separate directories, per agent

This machine runs more than one agent against this app at once — Coder and
Tester, and possibly others later. `PT-2692` opens this as a real item: the
two were sharing one save/package directory, and a save that was good
minutes earlier kept coming back unreadable ("class levels add to N and the
character is level M"). Two agents writing to the same files is the cause,
not a defect in either agent's own work.

## The mechanism

`Locations.desktop()` (`Lodestar/lib/src/locations.dart`) derives a single
shared root on Linux: `$XDG_DATA_HOME/kotor-rpg` if `XDG_DATA_HOME` is set
and non-empty, otherwise `$HOME/.local/share/kotor-rpg`. Everything —
`packages/`, `saves/`, `console/` — lives under that one root. Setting
`XDG_DATA_HOME` before launch is the whole mechanism; no code change is
needed.

⚠⚠⚠ **THE ONE THING THAT WILL TRIP YOU UP**: `XDG_DATA_HOME` is *not* the
app's own directory — it's the general data home, and the app appends its
own `kotor-rpg` folder beneath whatever you point it at. Set
`XDG_DATA_HOME=~/.local/share/coder-data` and the app's real content lands at
`~/.local/share/coder-data/kotor-rpg/`, **not**
`~/.local/share/coder-data/` itself. Pointing `XDG_DATA_HOME` straight at
what you think is the final folder (e.g. naming it
`~/.local/share/kotor-rpg-coder` and expecting packages there directly) puts
the app one level too deep, looking at a folder that was never populated —
it shows "no packages installed" with no error, because an empty directory
and a wrong directory look identical to `PackageLibrary.list()`. Found this
the hard way while setting this up; costs nothing once you know the extra
segment is coming.

## Coder's own directory

```
XDG_DATA_HOME=~/.local/share/coder-data
```

Real content at `~/.local/share/coder-data/kotor-rpg/{packages,saves,console}`.
`packages/` was seeded with a full copy of the existing shared shelf
(`~/.local/share/kotor-rpg/packages`) — a copy, not a symlink, so a write
under `packages/` (rare, but possible) can't reintroduce the exact
cross-contamination this split exists to remove. Re-sync manually if the
shelf gains new content Coder needs and hasn't picked up.

Launch:

```
XDG_DATA_HOME=~/.local/share/coder-data ./scripts/run.sh debug
```

## Tester's own directory

Tester should use its own distinct value — not Coder's, and not left unset
(unset resolves to `~/.local/share/kotor-rpg`, the original shared
location, which is exactly what this split is meant to end). Something like:

```
XDG_DATA_HOME=~/.local/share/tester-data
```

with `packages/` seeded the same way (a full copy of the shared shelf into
`~/.local/share/tester-data/kotor-rpg/packages/`), then:

```
XDG_DATA_HOME=~/.local/share/tester-data ./scripts/run.sh debug
```

## Proof this actually works

Two concurrent instances, one per directory above, each taken through a
real chargen and into a real area (which is when the app writes its first
save). Confirmed directly on-disk after both writes landed:

- Coder's save (`kaeda-lhent.sav`) existed only under
  `~/.local/share/coder-data/kotor-rpg/saves/` — absent from the shared
  directory, whose file count was unchanged by it.
- The shared directory's own save from that same run (`garon-tarkis.sav`,
  written by the instance simulating Tester's unset-`XDG_DATA_HOME`
  default) landed only there, absent from Coder's directory.

Both processes stayed alive throughout, confirmed by PID
(`ps -p <pid>` and `/proc/<pid>/environ` showing the intended
`XDG_DATA_HOME` each). Neither run touched the other's files.

## If you're setting this up fresh

1. `mkdir -p ~/.local/share/<name>-data/kotor-rpg`
2. `cp -r ~/.local/share/kotor-rpg/packages ~/.local/share/<name>-data/kotor-rpg/packages`
3. `mkdir -p ~/.local/share/<name>-data/kotor-rpg/saves ~/.local/share/<name>-data/kotor-rpg/console`
4. Launch with `XDG_DATA_HOME=~/.local/share/<name>-data` set.
5. First launch shows the "Welcome" import screen (a fresh root has never
   seen it) — click "Continue without it." This is expected once, not a
   sign anything is wrong.

## The stocked real-K2 save, for Equip 1:1 comparisons — `PT-2695`/`PT-2696`

This is about the OWNER's real Knights of the Old Republic II install, not
this app — needed for screenshot-comparing our Equip screen against K2's
real one with the same character and gear on both sides, so use it whenever
you need a K2-side reference for that work.

- **Location:** `~/.local/share/aspyr-media/kotor2/saves/000003 - stocked`.
  Loads in K2's own Load Game browser with a populated item list. The
  owner's real save (`000001 - autosave`) was backed up untouched before any
  of this; only this copy was ever written to.
- **Why it exists:** the first comparison pass used two characters with
  different gear — not a real pair — so nothing about the item list, a
  filled slot, or a weapon row was actually comparable. This save fixes
  that: same character, real varied inventory, several items per slot type.

### KSE (KOTOR Savegame Editor) — two real bugs in the tool itself

Used to stock the save above. Both bugs are in KSE's own bundled Perl, not
in anything this project owns — recorded here because anyone stocking a
save again will hit both.

- **`K2_Path` in `kse.ini`** must point at `.../Knights of the Old Republic
  II/steamassets`, not the bare game root. This Steam/Aspyr port keeps
  `chitin.key` and `data/2da.bif` under `steamassets/`; pointed at the bare
  root, KSE's `Generate_Master_Item_List` crashes (`Can't call method
  "get_resource" on an undefined value`) because its own `Bioware::BIF->new`
  never finds them.
- **KSE ignores its own ini's `K2_SavePath` entirely.** Its save-directory
  detection always re-derives `<K2_Path>/saves` (or `/Saves`, or an AppData
  fallback) on every launch, confirmed by reading KSE's own extracted Perl
  source (`unzip -o KSE_337.exe "script/*"`). A save KSE needs to see has to
  physically exist under `<K2_Path>/steamassets/saves/<slotname>/` — the ini
  value does nothing.
