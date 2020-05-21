#!/usr/bin/env python
# -*- coding: utf-8 -*-


def rev(s):
    print '===', s
    sl = list(s)
    for l in xrange(len(s)):
        r = len(s) - l - 1
        print l, r
        if l >= r:
            break
        sl[l], sl[r] = sl[r], sl[l]
    s = ''.join(sl)

    print s
    return s


s = ''
assert rev(s) == ''.join(reversed(s))
s = 'message'
assert rev(s) == ''.join(reversed(s))
s = 'm'
assert rev(s) == ''.join(reversed(s))
s = 'me'
assert rev(s) == ''.join(reversed(s))
s = 'mes'
assert rev(s) == ''.join(reversed(s))
print 'ok'
