#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def get_digits_sum(self, n):
        digits = [int(digit) for digit in str(n)]
        return sum((digit ** 2 for digit in digits))

    def isHappyHash(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        digits_sum = self.get_digits_sum(n)
        visited_sums = dict()
        while digits_sum != 1:
            digits_sum = self.get_digits_sum(digits_sum)
            if digits_sum in visited_sums:
                return False
            visited_sums[digits_sum] = True

        return True

    # floyd
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        slow = n
        fast = n
        while True:
            slow = self.get_digits_sum(slow)
            fast = self.get_digits_sum(fast)
            fast = self.get_digits_sum(fast)
            if slow == fast:
                if slow == 1:
                    return True
                else:
                    return False


s = Solution()
res = s.isHappy(20)
assert res == False
print '20 ok'
res = s.isHappy(1)
assert res == True
print '1 ok'
res = s.isHappy(2)
assert res == False
print '2 ok'
