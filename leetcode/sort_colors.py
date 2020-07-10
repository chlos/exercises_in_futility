#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import defaultdict


RED = 0
WHITE = 1
BLUE = 2


# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution:
    # two-pass
    def sortColors_twoPassCounter(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for color in nums:
            count[color] += 1
        pos = 0
        for color in [0, 1, 2]:
            for i in range(pos, pos + count[color]):
                nums[i] = color
                pos = i + 1

    # see the: https://leetcode.com/problems/sort-colors/discuss/26474/Sharing-C%2B%2B-solution-with-Good-Explanation
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_i, white_i, blue_i = 0, 0, len(nums) - 1
        while white_i <= blue_i:
            if nums[white_i] == WHITE:
                white_i += 1
            elif nums[white_i] == RED:
                nums[red_i], nums[white_i] = nums[white_i], nums[red_i]
                white_i += 1
                red_i += 1
            else:
                nums[white_i], nums[blue_i] = nums[blue_i], nums[white_i]
                blue_i -= 1


if __name__ == "__main__":
    s = Solution()

    actual = [2, 0, 2, 1, 1, 0]
    s.sortColors(actual)
    expected = [0, 0, 1, 1, 2, 2]
    print(actual, expected)
    assert actual == expected
    print('OK')