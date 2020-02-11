#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fib_iter(self, N):
        """
        :type N: int
        :rtype: int
        """
        n0 = 0
        n1 = 1

        if N == 0:
            return n0
        elif N == 1:
            return n1

        for _ in xrange(2, N + 1):
            n = n0 + n1
            n0 = n1
            n1 = n

        return n

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def fib_recur(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1

            return fib_recur(n - 2) + fib_recur(n - 1)

        return fib_recur(N)

s = Solution()
s6 = s.fib(6)
print 's6 = ', s6
assert s6 == 8
