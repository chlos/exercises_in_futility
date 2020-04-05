#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    def isAnagramSort(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagramSortedDict(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for ch in s:
            d1[ch] += 1
        for ch in t:
            d2[ch] += 1
        return d1 == d2

    def isAnagramArray(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        abc_size = 26
        d1 = [0] * abc_size
        d2 = [0] * abc_size
        for ch in s:
            d1[ord(ch) - ord('a')] += 1
        for ch in t:
            d2[ord(ch) - ord('a')] += 1
        return d1 == d2

    # one dict
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1

        for v in d.itervalues():
            if v:
                return False

        return True

s = Solution()
assert s.isAnagram('a', 'a') == True
assert s.isAnagram('a', 'aa') == False
assert s.isAnagram('ab', 'ba') == True
