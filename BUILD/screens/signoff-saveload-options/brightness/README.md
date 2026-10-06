# Brightness, K2 vs ours (PT-2736 addendum)
K2's Graphics slider is a GAMMA on the whole picture (out = in^e). Fitted from five K2 captures of one screen (`k2-min/p25/default/p75/max.png`, ini default Brightness=57): exponents 2.33, 1.74, 1.00, 0.574, 0.309; per-pixel error of the gamma model 2.3-6.9 levels vs 6-37 for a linear overlay (fit.json). Ours is a fragment shader with that curve (`lib/settings/brightness_curve.dart`, tested against K2's own pixel values).

Mean luminance of the central panel (x 200-1700, y 270-800; the two apps draw different screens, so the comparison is the SHAPE):
| level | K2 panel | ours panel | K2 / default | ours / default |
|---|---|---|---|---|
| min | 2.69 | 1.84 | 0.15 | 0.11 |
| 25% | 5.71 | 4.52 | 0.32 | 0.27 |
| default | 17.79 | 16.64 | 1 | 1 |
| 75% | 39.80 | 37.73 | 2.24 | 2.27 |
| max | 67.24 | 65.18 | 3.78 | 3.92 |
Our dark end is a little darker than K2's (min 0.11 vs 0.15 of default): the measured pixels near black quantise, so the fit there is the loosest. Not tuned further.
