#!/usr/bin/env python
# -*- coding: utf-8 -*-

# see the:
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_res_len = 0
        freqs = defaultdict(int)

        begin, end = 0, 0
        counter = 0     # count repeating chars
        while end < len(s):
            freqs[s[end]] += 1
            if freqs[s[end]] > 1:
                counter += 1
            end += 1

            while counter > 0:
                if freqs[s[begin]] > 1:
                    counter -= 1
                freqs[s[begin]] -= 1
                begin += 1

            max_res_len = max(max_res_len, end - begin)

        return max_res_len


s = Solution()

res = s.lengthOfLongestSubstring('abcabcbb')
exp = 3
print 'Result: "{}" (expected "{}")'.format(res, exp)
assert res == exp
print 'OK'

res = s.lengthOfLongestSubstring('bbbbb')
exp = 1
print 'Result: "{}" (expected "{}")'.format(res, exp)
assert res == exp
print 'OK'

res = s.lengthOfLongestSubstring('pwwkew')
exp = 3
print 'Result: "{}" (expected "{}")'.format(res, exp)
assert res == exp
print 'OK'
