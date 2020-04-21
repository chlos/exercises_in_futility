#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            None: float('inf'),
        }

        i = 0
        result = 0
        while i < len(s):
            curr_digit = s[i]
            next_digit = s[i+1] if i < len(s)-1 else None
            # if (
            #     curr_digit == 'I' and next_digit in ['V', 'X']
            #     or curr_digit == 'X' and next_digit in ['L', 'C']
            #     or curr_digit == 'C' and next_digit in ['D', 'M']
            # ):
            if next_digit is not None and map[curr_digit] < map[next_digit]:
                result += map[next_digit] - map[curr_digit]
                i += 2
            else:
                result += map[s[i]]
                i += 1

        return result

s = Solution()
assert s.romanToInt('III') == 3
print '\nOK'
assert s.romanToInt('IV') == 4
print '\nOK'
assert s.romanToInt('IX') == 9
print '\nOK'
assert s.romanToInt('MCMXCIV') == 1994
print '\nOK'
