#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_lcs(s1, s2):
    lcs_suf = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest = 0
    longest_i = 0

    for i in xrange(1, len(s1) + 1):
        for j in xrange(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_suf[i][j] = lcs_suf[i - 1][j - 1] + 1
                if lcs_suf[i][j] > longest:
                    longest = lcs_suf[i][j]
                    longest_i = i
            else:
                lcs_suf[i][j] = 0

    return longest, s1[longest_i - longest: longest_i]


def test(func):
    substring_len, substring = func('aa', 'aa')
    print substring_len, substring
    assert substring == 'aa'

    substring_len, substring = func('fish', 'dish')
    print substring_len, substring
    assert substring == 'ish'

    substring_len, substring = func('pfishx', 'dish')
    print substring_len, substring
    assert substring == 'ish'

    substring_len, substring = func('fooxsubstringxxxba', 'foo.substring...ba')
    print substring_len, substring
    assert substring == 'substring'

    print '\n\nOK'


def main():
    test(get_lcs)


if __name__ == "__main__":
    main()
