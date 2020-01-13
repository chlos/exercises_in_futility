#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple, defaultdict

Point = namedtuple("Point", ["x", "y"])


def issym(points):
    if len(points) == 0:
        return True
    d = defaultdict(int)
    xl, xr = [f(p.x for p in points) for f in (min, max)]
    print 'xl = {}; xr = {}'.format(xl, xr)
    for p in points:
        dl, dr = p.x - xl, xr - p.x
        print '({}, {}): dl = {}; dr = {}'.format(p.x, p.y, dl, dr)
        print '(dl > dr) - (dl < dr) :: ({} > {}) - ({} < {}) = {}'.format(
            dl, dr, dl, dr, (dl > dr) - (dl < dr),
        )
        d[(min(dl, dr), p.y)] += (dl > dr) - (dl < dr)
    print d
    return all(v == 0 for v in d.values())


if __name__ == "__main__":
    test_cases = [
        (True, [(-1, 0), (1, 0)]),
        # (True, [(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)]),
        # (False, [(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0)]),
        # (True, []),
        # (True, [(0, 0)]),
        # (True, [(0, 0), (100500, 0)]),
        # (False, [(0, 0), (100501, 1)]),
        # (False, [(0, 0), (1, 0), (3, 0)]),
    ]
    for result, case in test_cases:
        assert result == issym([Point(*e) for e in case])

    print 'OK'
