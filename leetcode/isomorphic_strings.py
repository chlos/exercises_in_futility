#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


class Solution(object):
    def isIsomorphic_hashmap_list(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = defaultdict(list)
        map_t = defaultdict(list)
        for i, ch in enumerate(s):
            map_s[ch].append(i)
        for i, ch in enumerate(t):
            map_t[ch].append(i)
        return sorted(map_s.itervalues()) == sorted(map_t.itervalues())

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = defaultdict(lambda: -1)
        map_t = defaultdict(lambda: -1)
        for i, (ch_s, ch_t) in enumerate(zip(s, t)):
            if map_s[ch_s] != map_t[ch_t]:
                return False
            map_s[ch_s] = i
            map_t[ch_t] = i

        return True


s = Solution()
res = s.isIsomorphic('ab', 'aa')
assert res == False
