#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_substrings(s1, s2):
    substrings = []
    for i1 in xrange(len(s1)):
        substring = ''
        for i2 in xrange(len(s2)):
            if i1 + i2 < len(s1) and s1[i1 + i2] == s2[i2]:
                substring += s2[i2]
            else:
                if len(substring) > 1:
                    substrings.append(substring)
                    substring = ''
        if len(substring) > 1:
            substrings.append(substring)

    return substrings


def test(func):
    s1 = 'AHAMMAD'
    s2 = 'AHAMAD'
    assert func(s1, s2) == ['AHAM', 'MAD']


def main():
    test(get_substrings)


if __name__ == '__main__':
    main()
