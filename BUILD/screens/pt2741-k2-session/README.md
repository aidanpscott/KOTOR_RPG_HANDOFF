# PT-2741: one K2 session, read-only (CODER, 2026-10-10, 22:27–22:37)

Owner away; started after 5 minutes of screen idle. K2 (Aspyr 1.0.2, native Linux, through Steam) ran full screen at 3840×2160. The images here are scaled to 1920×1080; the 4K originals are on the owner's machine in `~/kotor2-backups/2026-10-10-pt2741/captures-4k/`. **Nothing was saved in K2.** K2 was left through Options > Exit Game > OK, then Quit.

## Backup rule
- Before: `~/kotor2-backups/2026-10-10-pt2741/before.sha256` (`steamassets/swkotor2.ini`, `swplayer.ini`, `devicedefaults.ini`, Steam `userdata/113192353/208580/remotecache.vdf`).
- After: all four identical to before. The eight saves (40 files) identical to the old-disk originals. The two test slots were deleted.
- **K2's live data folder on this machine is `~/snap/steam/common/.local/share/aspyr-media/kotor2`.** Steam is a snap, so K2 runs with `HOME=~/snap/steam/common`, and this launch created that folder (it did not exist before). The saves were copied there. The old `steamassets/saves` symlink, which the Linux build does not read, now points there too. The ini K2 created on its first launch was moved to the backup folder (`after/k2-created-swkotor2.ini`); K2 makes a default one on its next start.
- **K2 matches save folder names in lower case.** A slot folder with capital letters ("000009 - FP TEST FULL") is not listed. Proven with control copies: an unedited copy listed; a copy with only the Force edit listed; a copy with only the name edit listed; the two with capitals did not until renamed.

## Part A (the Force well's colours): blocked
- `top_p.gui` (the footer and Equip portrait block): `PB_FORCE1` and `PB_VIT1` fill with `uibit_bar_fp_p` / `uibit_bar_vp_p` (BORDER and PROGRESS both), `COLOR` null. Both textures (`texturepacks/swpc_tex_gui.erf`) are pure white with an alpha shape: **the engine tints them; no colour is in the files.**
- **The approved test edit does not reach the game.** "FP TEST FULL 100" (player ForcePoints = MaxForcePoints = CurrentForce = 20, in the `pc` creature and the module's player list) loads with **Force 0/0** on the Character sheet (`08-full-character.png`). K2 recomputes the player's Force on load, and on Peragus the Exile is cut off from the Force. A full or half well needs a save from after the Exile regains the Force.
- Captured anyway, all EMPTY wells: the in-play party bar (`07-full-loaded.png`, zoom `07-partybar-zoom.png`): health well orange-red frame, translucent red-brown wash; Force well teal frame, translucent teal wash. The footer on every menu screen: dark teal.

## PT-2739 item 6 (Options: two lit rows): answered
- No pointer: K2 outlines the FIRST row (Save Game) as the default (`09-options-nohover.png`, crop `09-rows.png`).
- Pointer on Gameplay: ONLY Gameplay is lit; Save Game is not (`10-options-hover-gameplay.png`). **One lit row, following the pointer.** Ours keeps Save Game lit while another row is hovered: fix to K2.

## Part B (the Inventory): captured where the saves allow
Save: a "mod test" slot (22 items in the bag, all count 1).
- `12-inventory-open.png`: the first-open help box ("The PARTY INVENTORY screen shows a list of all the items not currently equipped by other party members or the companions back at your base. This inventory is shared by all party members.") with OK.
- `inv-01-default.png`: Filter label, the tabs All · Datapads · Weapons · Armor · Useable · Quests · Misc, the item list (icon cell + name row), the description pane (feats required, damage, critical threat, flavour text), Credits 0, Use Item, Close, and the footer.
- `inv-02`…`inv-08`: each tab. `inv-06-tab-Useable.png` is the empty list (both panes blank).
- `inv-10-selected-jedi-robe.png`: another selection and its description. `inv-11-hover-row.png`: a row under the pointer. `inv-12-scrolled-bottom.png`: the list scrolled to its end (22 rows, thumb moved). `inv-13-hover-use-item.png`: Use Item under the pointer.
- **K2's Inventory offers only Use Item and Close**: no Equip, Drop, Destroy or Examine control (the description pane is the examine).

### Not capturable from these saves (owner can set up)
- **Party switching (the arrows) and a droid's inventory**: the player is alone in the party; T3-M4 is available but not in it.
- **Stacks and their counts**: every item in every save has a count of 1.
- **The in-play party bar with companions** (for the sidebar item): same reason.
