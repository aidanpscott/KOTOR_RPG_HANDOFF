#!/bin/sh
# KOTOR_RPG_HANDOFF is PUBLIC and keeps TEXT ONLY. Reads file paths on stdin and prints every one that may not be committed here.
# One list, used by the pre-commit hook, the CI workflow AND MAIN_WORK's gate (scripts/check_handoff_media.py), so they cannot drift apart.
#
#   images           .png .jpg .jpeg .gif .bmp .webp .svg .ico   — every image, our own app's screenshots included
#   video            .mp4 .mkv .webm .mov .avi .m4v
#   fonts            .ttf .otf .woff .woff2 .eot
#   game textures    .tga .tpc .dds
#   game data        .2da
#
# Owner ruling 2026-10-11 (all media goes private, extending PT-2744's): these live in the private repo, KOTOR_RPG_MAIN_WORK/media/.
grep -iE '\.(png|jpe?g|gif|bmp|webp|svg|ico|mp4|mkv|webm|mov|avi|m4v|ttf|otf|woff2?|eot|tga|tpc|dds|2da)$'
