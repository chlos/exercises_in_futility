#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_int = 2 ** 31
        max_int = 2 ** 31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rx = 0
        while x != 0:
            d = x % 10
            if sign == 1 and rx > (max_int - d) / 10:
                return 0
            if sign == -1 and rx > (min_int - d) / 10:
                return 0

            new_rx = rx * 10 + d
            if (new_rx - d) / 10 != rx:
                return 0
            rx = new_rx
            x /= 10
            print x, d, rx

        return sign * rx

s = Solution()
assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(1534236469) == 0
