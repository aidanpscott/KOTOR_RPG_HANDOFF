# A five-member party for the Save/Load side panel (PT-2733 item 5)

Every shelf package has a party of at most three, so the party-paging arrows had nothing to show. This makes one.

**Build it (from the app repo, any data directory):**

    cd KOTOR-RPG-APP-clean
    . tool/env.sh
    XDG_DATA_HOME=<your data dir> dart run tool/author_five_party_fixture.dart [source-save-name]

It copies an existing three-member save (default `mira-mourn`: the player, Guardian and Grunt, package `0 AAA Visual Pass`) to `five-party`, adds two more companions to its log, and writes ONE bookmark, `2 : FIVE IN THE PARTY`, for it. It refuses (and writes nothing) if the source save does not have exactly two companions.

**What to look for (Main-menu Load Game > Switch Characters until the character with the "Five in the party" row; or in-game Options > Load Game):**
- Three portrait boxes with a left arrow (dim, nothing before) and a right arrow (teal). K2's own party-switch arrows; at three members or fewer they are not drawn.
- Click the right arrow: members 4 and 5 show, the third box is empty, the right arrow dims, the left arrow lights.
- Hover an arrow: it turns white. Click the left arrow: back to page one. Mouse only; the list's keys do not page.
- The leader is the MIDDLE box on page one, as in K2. Selecting another row starts that row's party at page one.

The portraits in this bookmark are stock faces chosen so the pages look different; companions carry no portrait art yet, so a real bookmark of this party shows empty boxes for them (known gap, parked with the party-panel-portraits item).

Live captures, K2-style frame: `BUILD/screens/pt2733-saveload2/five-party-pages-live.png` (page one, right arrow hovered, page two, back) and `five-party-load-screen.png`.
