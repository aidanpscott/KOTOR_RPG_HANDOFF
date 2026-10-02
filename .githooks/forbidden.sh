#!/bin/sh
# KOTOR_RPG_HANDOFF is PUBLIC. Reads file paths on stdin and prints every one that may not be committed here.
# One list, used by the pre-commit hook AND the CI workflow, so the two cannot drift apart.
#
#   fonts            .ttf .otf .woff .woff2 .eot  — Bank Gothic Md BT was commercial with no licence (PT-2721);
#                    Orbitron and Liberation are OFL but font files stay out of this repo regardless (owner ruling)
#   game textures    .tga .tpc                    — extracted game art is the publishers' (PT-2722, owner ruling)
#   extracted art    anything under an assets/extracted/ folder, and any image under any extracted/ folder
#
# Screenshots and side-by-sides (PNG under BUILD/screens, STUDY/_reference) are FINE and are not matched.
# data/extracted/*.json|md (rules data, not art) is fine too.
grep -iE '\.(ttf|otf|woff2?|eot|tga|tpc)$|(^|/)assets/extracted/|(^|/)extracted/.*\.(png|jpe?g|gif|bmp|webp|dds)$'
