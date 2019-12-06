#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1)
        len2 = len(text2)

        m = [[0] * (len2 + 1) for x in xrange(len1 + 1)]

        for i1 in xrange(1, len1 + 1):
            for i2 in xrange(1, len2 + 1):
                if text1[i1 - 1] == text2[i2 - 1]:
                    m[i1][i2] = m[i1 - 1][i2 - 1] + 1
                else:
                    m[i1][i2] = max(m[i1 - 1][i2], m[i1][i2 - 1])

        return m[len1][len2]
