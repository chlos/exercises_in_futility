#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindromeStr(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xstr = str(x)
        return xstr == xstr[::-1]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_x = 0
        while x > reverted_x:
            reverted_x = reverted_x * 10 + x % 10
            x /= 10
        return x == reverted_x or x == reverted_x / 10
