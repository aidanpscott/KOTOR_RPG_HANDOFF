#!/bin/sh
# The guard's own test: it must catch each forbidden shape and pass each allowed one. Run by CI.
here=$(dirname "$0"); fail=0
check() { # expected(0=allowed,1=refused) path
  out=$(printf '%s\n' "$2" | sh "$here/forbidden.sh"); hit=0; [ -n "$out" ] && hit=1
  if [ "$hit" != "$1" ]; then echo "GUARD WRONG for: $2 (wanted $1, got $hit)" >&2; fail=1; fi
}
check 1 "fonts/Orbitron.ttf";        check 1 "x/Font.OTF";           check 1 "a/b.woff2"
check 1 "art/po_pmha01.tga";         check 1 "art/icon.TPC"
check 1 "KOTOR-RPG-APP/assets/extracted/portraits/k2/po_pmha01.png"
check 1 "assets/extracted/portraits/index.json"
check 1 "data/extracted/portraits/po_x.png"
check 0 "BUILD/screens/pt2721-equip-loop/pass-1/k2-1-empty-slot.png"
check 0 "STUDY/_reference/pt2722-font-candidates/equip-font-side-by-side.png"
check 0 "data/extracted/skills.json";  check 0 "data/extracted/_PROVENANCE.md"
check 0 "docs/EQUIP-COMPARISON-PT2721.md"
[ "$fail" = 0 ] && echo "forbidden.sh: all cases right"; exit $fail
