# FONT-CANDIDATES-PT2722 — K2's fonts by use, and what the right candidates are

**`PT-2722`, D3 and D6.** Written by CODER. Picture: `STUDY/_reference/pt2722-font-candidates/equip-font-candidates.png` (K2's own glyphs drawn from the game's **hi-res atlases**, then each candidate, at the **same capital height**, with each one's width ÷ capital height measured).

## ⚠⚠⚠ A CORRECTION TO `PT-2721`, AND IT CHANGES D6

`PT-2721` reported Bank Gothic Md BT as **about 1.8× wider than K2's face**. **That was measured against the wrong atlas.** It compared Bank Gothic with the original 256-pixel `fnt_dialog16x16`. The game on this machine does not draw that: the Steam build ships **hi-res replacements in `override/`** (`d3xfont16x16b.tga`, `d3xfnt_d16x16b.tga`, plus `d2x…`/`dialogfont16x16b` tiers) and draws those at 1920×1080. Measured against the face that is actually on screen:

| string | K2 `dialogfont16x16` (width ÷ cap) | BankGothic Md BT | wider by |
|---|---|---|---|
| Light Combat Suit (Equipped) | 29.56 | 31.36 | **6.1%** |
| LIGHT COMBAT SUIT (EQUIPPED) | 33.00 | 35.75 | 8.3% |
| ATTACK MODIFIER | 18.56 | 19.74 | 6.4% |
| the picture's two lines | 29.56 | 31.56 | **6.8%** |

**K2's real UI face is itself an extended small-caps face, and Bank Gothic Medium is within about 7% of it in width, with very close letterforms.** A condensed cut would be too NARROW, not just right. The owner's D6 ("a condensed Bank Gothic, so the letters match K2's height and width") was a reasonable answer to the number I reported; the number was wrong.

**Recommendation (D6): keep `BankGothicMediumBT.ttf` and tighten it.** Matching a word's width to K2's takes a letter-spacing of about **−0.037 em** (the 2.0 width÷cap difference, spread over ~28 characters at the picture's capital height) — no new file, no new licence. **If the owner still wants a condensed cut,** the only true Bank Gothic Condensed is GroupType's 2010 revival: **Light / Medium / Bold Condensed** (and Dist variants), **$29 per style, $119 for the family**, MyFonts (`https://www.myfonts.com/fonts/grouptype/bank-gothic/` — the style names and prices were read off the page). Its width is **not measurable without the file** and I expect it to be well under K2's; its desktop-versus-app-embedding licence was **not verified**. ParaType's Bank Gothic BT Light/Medium are not condensed. Free lookalikes (Saira Extra Condensed and others) are squared and condensed but are not Bank Gothic and were not rendered here.

## D3 — which K2 font draws which text on the Equip screen

Read from the real GFFs (`equip_p.gui`, `top_p.gui`): **exactly two faces.**

| use | control(s) | K2 font resref | what it is |
|---|---|---|---|
| title ("Equip") | `LBL_TITLE` | `dialogfont16x16` | the small-caps UI face |
| top-bar button labels / tooltips | `LBLH_*`, `BTN_*` (top_p) | `dialogfont16x16` | small-caps UI face |
| item-list rows | `LB_ITEMS`'s `PROTOITEM` | `dialogfont16x16` | small-caps UI face |
| slot subtitle, bars, buttons (Close / Cancel / OK / Switch Weapons) | `LBL_SLOTNAME`, `BTN_BACK`, `BTN_EQUIP`, `BTN_SWAPWEAPONS` | `dialogfont16x16` | small-caps UI face |
| readout numbers (DEF, ATKL, ATKR, to-hit, damage) | `LBL_DEF`, `LBL_ATKL`, `LBL_ATKR`, `LBL_TOHIT*` | `dialogfont16x16` | small-caps UI face |
| name and class / level | `LBL_CHARNAME`, `LBL_TOP_CLASS1`, `LBL_TOP_CLASS1LEVEL` (top_p) | `dialogfont16x16` | small-caps UI face |
| **description pane** | `LB_DESC`'s `PROTOITEM` | **`fnt_d16x16`** | **an Arial-Bold-class sans, drawn tracked wide** |

K2 ships ten bitmap faces in all (`dialogfont10x10(b)`, `dialogfont12x16`, `dialogfont16x16(b)`, `dialogfont32x32(b)`, `fnt_console`, `fnt_credits(a,b)`, `fnt_d10x10b`, `fnt_d16x16(b)`, `fnt_dialog16x16`, `fnt_galahad14`); the Equip screen uses only the two above. **So the only face that still needs candidates is `fnt_d16x16`, the description face.**

## D3 — three closest real fonts to `fnt_d16x16`

K2's glyphs are **Arial-Bold shapes** (double-storey a, single-storey g, straight-tailed y), drawn with **extra advance — about 12% wider than a normal Arial Bold** (width ÷ cap 50.70 against 45.41). Same shapes, wider spacing, so a metric-compatible Arial plus ~+0.057 em of letter-spacing matches it.

| # | font | where to get it | licence (verified) | width ÷ cap | |
|---|---|---|---|---|---|
| 1 | **Liberation Sans Bold** (Red Hat / Google; Arial-metric) | `https://github.com/liberationfonts/liberation-fonts/releases` (2.1.5, `LiberationSans-Bold.ttf`) | **SIL OFL 1.1** (read from the release's LICENSE) | 45.41 | **recommended:** a static file, OFL, the Arial metrics K2's face has |
| 2 | **Arimo Bold** (Google Fonts; Liberation 2's descendant) | `https://github.com/google/fonts/tree/main/ofl/arimo` (`Arimo[wght].ttf`, a variable file; weight 700) | **SIL OFL 1.1** (read from `OFL.txt` in the repo) | 45.41 (identical metrics) | the same design; a variable file |
| 3 | **Nimbus Sans Bold** (URW base-35, a Helvetica clone) | `https://github.com/ArtifexSoftware/urw-base35-fonts` (`fonts/NimbusSans-Bold.otf`) | **AGPL-3.0** (the repo's `COPYING`; a font exception is commonly attached but **was not verified here**) | 42.81 (narrower) | Helvetica-shaped rather than Arial-shaped; the licence needs the owner's read before bundling |

Not recommended: **Arial Bold itself** — it is the exact shapes, but it is Microsoft's and bundling it needs a licence.

## What was done and what was not

- K2's glyphs in the picture are drawn from the game's own `d3xfnt_d16x16b.tga` / `d3xfont16x16b.tga` with the `.txi` glyph tables taken from the original texture resources (`tpc.txi()`); the candidates are rendered from their downloaded files **for the picture only — nothing is bundled and nothing was added to either repo.**
- **The Equip screen's current size is also off, and this is a separate finding:** `kK2CapHeightOfCell` (0.5) was measured from the LOW-res atlas. The hi-res face's capitals are **0.5625** of its cell (36 px in a 64 px cell). On the 1920×1080 captures K2's list text is about 22% larger than ours (about 9.5 px per character against 7.8). It is sized with the layout slice (fix 3), from the pictures, not from this constant.
- Not measured: GroupType's condensed cuts (no file), the Dist variants, Morris Sans / Card Gothic (Linotype derivatives) — named by the research agent and not rendered.
