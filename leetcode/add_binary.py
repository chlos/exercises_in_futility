#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        carry = 0
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2

        return result[::-1]


s = Solution()
res = s.addBinary('1010', '1011')
print res
assert res == '10101'
print 'OK'
