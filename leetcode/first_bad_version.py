#!/usr/bin/env python
# -*- coding: utf-8 -*-


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < n:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid

        return l

s = Solution()
assert s.firstBadVersion(5) == 4
