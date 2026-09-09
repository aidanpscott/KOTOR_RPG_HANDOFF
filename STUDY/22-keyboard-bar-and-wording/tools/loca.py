#!/usr/bin/env python3
"""loca.py — read Larian .loca string tables (BG3). stdlib + lspk.

LOCA: "LOCA" · uint32 numEntries · uint32 textsOffset
entry (70 bytes): char[64] key · uint16 version · uint32 length
texts: NUL-terminated UTF-8, concatenated from textsOffset in entry order.
⚠ `length` INCLUDES the trailing NUL.
"""
import struct, sys, json, os
from lspk import Pak

def load(pak_path, inner='Localization/English/english.loca'):
    d = Pak(pak_path).read(inner)
    assert d[:4] == b'LOCA', d[:4]
    num, off = struct.unpack_from('<II', d, 4)
    out, pos = {}, off
    for i in range(num):
        o = 12 + i * 70
        key = d[o:o+64].split(b'\0')[0].decode('ascii', 'replace')
        _ver, ln = struct.unpack_from('<HI', d, o+64)
        out[key] = d[pos:pos+ln-1].decode('utf-8', 'replace')
        pos += ln
    return out

if __name__ == '__main__':
    D = "/mnt/ga/SteamLibrary/steamapps/common/Baldurs Gate 3/Data"
    t = load(f'{D}/Localization/English.pak')
    print(f'{len(t):,} strings', file=sys.stderr)
    if len(sys.argv) > 1 and sys.argv[1] == '--dump':
        json.dump(t, open('loca_en.json','w'))
        print('wrote loca_en.json', file=sys.stderr)
    for h in sys.argv[1:]:
        if h.startswith('--'): continue
        print(f'{h} = {t.get(h, "<<NOT FOUND>>")!r}')
