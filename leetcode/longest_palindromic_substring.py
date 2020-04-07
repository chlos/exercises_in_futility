#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        dp_table = [[False for _ in xrange(n)] for _ in xrange(n)]
        max_len = 0
        result = ''

        for i in xrange(n - 1, -1, -1):
            dp_table[i][i] = True
            curr_len = 1
            if curr_len > max_len:
                max_len = curr_len
                result = s[i:i+1]
            for j in xrange(i + 1, len(s)):
                # Check for a window of size 2
                if j == i + 1 and s[i] == s[j]:
                    dp_table[i][j] = True
                    curr_len = j+1 - i
                    if curr_len > max_len:
                        max_len = curr_len
                        result = s[i:j+1]
                # Check for a window of size 3+
                if j > i + 1 and dp_table[i + 1][j - 1] and s[i] == s[j]:
                    dp_table[i][j] = True
                    curr_len = j+1 - i
                    if curr_len > max_len:
                        max_len = curr_len
                        result = s[i:j+1]

        return result

print '====='
s = Solution()
assert s.longestPalindrome('abc') in ['a', 'b', 'c']
assert s.longestPalindrome('babad') in ['aba', 'bab']
