#!/bin/sh
# The guard's own test: it must catch each forbidden shape and pass each allowed one. Run by CI and by MAIN_WORK's gate.
here=$(dirname "$0"); fail=0
check() { # expected(0=allowed,1=refused) path
  out=$(printf '%s\n' "$2" | sh "$here/forbidden.sh"); hit=0; [ -n "$out" ] && hit=1
  if [ "$hit" != "$1" ]; then echo "GUARD WRONG for: $2 (wanted $1, got $hit)" >&2; fail=1; fi
}
check 1 "fonts/Orbitron.ttf";        check 1 "x/Font.OTF";           check 1 "a/b.woff2"
check 1 "art/po_pmha01.tga";         check 1 "art/icon.TPC";         check 1 "art/x.dds"
check 1 "BUILD/screens/pt2721-equip-loop/pass-1/k2-1-empty-slot.png"
check 1 "BUILD/screens/test-170/ours-only.png"; check 1 "STUDY/26-aurora-observed/a.JPG"
check 1 "BUILD/screens/test-158/analysis/hfA-60fps.mp4"; check 1 "x/clip.webm"; check 1 "x/y.gif"
check 1 "data/k2_classes.2da";       check 1 "data/feat.2DA"
check 0 "data/extracted/skills.json";  check 0 "data/extracted/_PROVENANCE.md"
check 0 "docs/EQUIP-COMPARISON-PT2721.md"; check 0 "BUILD/screens/README.md"; check 0 "x/png-notes.md"
[ "$fail" = 0 ] && echo "forbidden.sh: all cases right"; exit $fail
