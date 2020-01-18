#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    digit_to_letters = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def backtrack(combination, digits):
            if not digits:
                result.append(combination)
                return

            digit = digits[0]
            for letter in self.digit_to_letters[int(digit)]:
                backtrack(combination + letter, digits[1:])

        result = []
        if not digits:
            return result
        backtrack('', digits)
        return result
