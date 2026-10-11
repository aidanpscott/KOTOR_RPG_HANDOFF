# PT-2739 item 5: the Loading picture covers the whole load (app 1abaea2)

The re-recorded Save/Load video counted, at 30 fps: the Loading picture for 7-9 frames, then **23-27 frames of an empty play screen** (frame and sidebar, no board), then the board.

The cause: the picture went down when the save had been read, but the new play screen then opened its area asynchronously. Now the App keeps the picture up until that play screen reports its first playable frame (the area open and the player on their square, or the area's refusal), with an 8 s backstop so it can never stick.

Live, the same build on Xvfb, 30 fps, counted frame by frame (clips not kept here: they show K2's loading art, and HANDOFF is public):
| Load | Picture | Empty play screen | Then |
|---|---|---|---|
| Continue (package menu) | 37 frames (1.23 s), the first ~3 black while the art paints | **0** | the board |
| F5 (quick save) | 14 frames (0.47 s) | **0** | the board |

Test: `the_loading_picture_covers_the_whole_load_test.dart` (real app, every frame of a Continue and an in-game load; the old rule fails it with an empty frame). Tests that acted on the "arrows to move" hint now wait for a playable board (`onTheBoard` in `test/sandbox.dart`): with the picture held, the hint shows under it.
