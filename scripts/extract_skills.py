"""Pilot extraction: SKILLS-01 §1 table -> structured records.

Method, so the count is reproducible:
  - Parse ONLY the markdown table in §1 (the document's own skill list).
  - One record per table row. No row is synthesised, none is merged.
  - `attribute` comes from the table's `Key` column, expanded to a full name.
  - `description` is filled ONLY from prose the document actually writes for
    that skill. Where the document says nothing, it is null. Nothing is
    inferred from the skill's name.
  - `source` cites the file and the line(s) each value was read from.
"""
import json, re, sys

SRC = 'docs/SKILLS-01.md'
PATH = ('/tmp/claude-1001/-mnt-ga-SteamLibrary-steamapps-common/'
        'fe58f391-547f-4b93-ac84-96c2992c43d8/scratchpad/handoff/' + SRC)

ATTR = {'Str': 'Strength', 'Dex': 'Dexterity', 'Con': 'Constitution',
        'Int': 'Intelligence', 'Wis': 'Wisdom', 'Cha': 'Charisma'}

# Prose descriptions the document writes for a named skill, with the line each
# was read from. Only skills that actually have prose appear here.
DESC = {
    'Archaeology': (52,
        "the dead. Ruins, artifacts, vanished civilisations, deep history. "
        "Rakatan technology, Infinite Empire sites, reading a wall nobody has "
        "read in twenty thousand years."),
    'Xenology': (56,
        "the living. Species, biology, customs, current factions and politics. "
        "Recognising a people and knowing how not to insult them."),
    'Mysticism': (58,
        "the Force and its traditions. Recognising a power as it is used, Jedi "
        "and Sith doctrine, holocrons, what a Korriban tomb is for and what is "
        "likely inside it."),
    # These two are written inline in the table row itself.
    'Botany': (24, "plant and soil analysis."),
    'Science': (33, "laboratory analysis, chemistry, and physical theory"),
}


def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def main():
    lines = open(PATH, encoding='utf-8').read().split('\n')

    # locate the §1 table: header row, separator, then rows until a blank/non-row
    start = None
    for i, l in enumerate(lines):
        if l.startswith('| Skill | Key |'):
            start = i
            break
    if start is None:
        sys.exit('FATAL: §1 skill table not found')

    rows = []
    i = start + 2                      # skip header and separator
    while i < len(lines) and lines[i].startswith('|'):
        rows.append((i + 1, lines[i]))  # 1-indexed line number
        i += 1

    out = []
    for lineno, raw in rows:
        cells = [c.strip() for c in raw.strip().strip('|').split('|')]
        name = re.sub(r'\*\*', '', cells[0]).strip()
        key = cells[1].strip()
        if not name:
            continue
        attribute = ATTR.get(key)
        d = DESC.get(name)
        if d:
            desc, dline = d[1], d[0]
            source = '%s:%d' % (SRC, lineno) if dline == lineno \
                else '%s:%d,%d' % (SRC, lineno, dline)
        else:
            desc, source = None, '%s:%d' % (SRC, lineno)
        out.append({
            'id': slug(name),
            'name': name,
            'attribute': attribute,
            'description': desc,
            'source': source,
        })

    # ---- verification, printed before anything is written ----
    print('rows parsed from the table : %d' % len(rows))
    print('records produced           : %d' % len(out))
    print('unique ids                 : %d' % len(set(r['id'] for r in out)))
    print('unique names               : %d' % len(set(r['name'] for r in out)))
    missing_attr = [r['name'] for r in out if r['attribute'] is None]
    print('records with null attribute: %d %s' % (len(missing_attr), missing_attr))
    nulldesc = [r['name'] for r in out if r['description'] is None]
    print('records with null description: %d' % len(nulldesc))
    print('  -> %s' % ', '.join(nulldesc))
    print()
    if len(out) != 24:
        print('*** COUNT MISMATCH: expected 24, got %d — STOPPING ***' % len(out))
        sys.exit(1)
    json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'),
              indent=2, ensure_ascii=False)
    open(sys.argv[1], 'a').write('\n')
    print('WROTE %s' % sys.argv[1])


main()
