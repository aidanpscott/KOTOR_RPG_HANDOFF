"""Binary DFM (Delphi/C++Builder form stream) reader.

Stream is 'TPF0' then a recursive component tree:
  prefix? | ClassName(shortstr) | Name(shortstr) | props..0 | children..0
"""
import struct

(vaNull,vaList,vaInt8,vaInt16,vaInt32,vaExtended,vaString,vaIdent,vaFalse,vaTrue,
 vaBinary,vaSet,vaLString,vaNil,vaCollection,vaSingle,vaCurrency,vaDate,vaWString,
 vaInt64,vaUTF8String,vaDouble) = range(22)

class Comp:
    def __init__(s, cls, name):
        s.cls, s.name, s.props, s.kids = cls, name, {}, []
    def walk(s):
        yield s
        for k in s.kids:
            yield from k.walk()

class R:
    def __init__(s, d):
        s.d, s.i = d, 0
    def b(s):
        v = s.d[s.i]; s.i += 1; return v
    def peek(s):
        return s.d[s.i] if s.i < len(s.d) else 0
    def raw(s, n):
        v = s.d[s.i:s.i+n]; s.i += n; return v
    def sstr(s):
        return s.raw(s.b()).decode('latin1')
    def i32(s):
        v = struct.unpack_from('<i', s.d, s.i)[0]; s.i += 4; return v

    def value(s):
        t = s.b()
        if t == vaNull:    return None
        if t == vaList:
            out = []
            while s.peek() != vaNull: out.append(s.value())
            s.b(); return out
        if t == vaInt8:    return struct.unpack('<b', s.raw(1))[0]
        if t == vaInt16:   return struct.unpack('<h', s.raw(2))[0]
        if t == vaInt32:   return s.i32()
        if t == vaExtended:s.raw(10); return '<ext>'
        if t == vaString:  return s.sstr()
        if t == vaIdent:   return s.sstr()
        if t == vaFalse:   return False
        if t == vaTrue:    return True
        if t == vaBinary:  n = s.i32(); s.raw(n); return '<bin:%d>' % n
        if t == vaSet:
            out = []
            while True:
                v = s.sstr()
                if v == '': break
                out.append(v)
            return set(out)
        if t == vaLString: n = s.i32(); return s.raw(n).decode('latin1')
        if t == vaNil:     return None
        if t == vaCollection:
            out = []
            while s.peek() != 0:
                if s.peek() in (vaInt8, vaInt16, vaInt32): s.value()
                s.b()                      # vaList marker
                item = {}
                while s.peek() != 0:
                    k = s.sstr(); item[k] = s.value()
                s.b()
                out.append(item)
            s.b(); return out
        if t == vaSingle:  v = struct.unpack_from('<f', s.d, s.i)[0]; s.i += 4; return v
        if t == vaCurrency:s.raw(8); return '<cur>'
        if t == vaDate:    s.raw(8); return '<date>'
        if t == vaWString: n = s.i32(); return s.raw(n*2).decode('utf-16-le')
        if t == vaInt64:   v = struct.unpack_from('<q', s.d, s.i)[0]; s.i += 8; return v
        if t == vaUTF8String: n = s.i32(); return s.raw(n).decode('utf-8', 'replace')
        if t == vaDouble:  v = struct.unpack_from('<d', s.d, s.i)[0]; s.i += 8; return v
        raise ValueError('bad value type %d at %d' % (t, s.i-1))

    def comp(s):
        if (s.peek() & 0xF0) == 0xF0:
            f = s.b()
            if f & 0x02: s.value()          # ffChildPos
        cls = s.sstr(); name = s.sstr()
        c = Comp(cls, name)
        while s.peek() != 0:
            k = s.sstr(); c.props[k] = s.value()
        s.b()
        while s.peek() != 0:
            c.kids.append(s.comp())
        s.b()
        return c

def parse(data):
    assert data[:4] == b'TPF0', 'not a DFM stream'
    return R(data[4:]).comp()
