#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def subsets_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [
                curr_result + [num] for curr_result in result
            ]

        return result

    # backtracking
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(tmp, idx):
            result.append(tmp[:])
            for i in xrange(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(tmp, i + 1)
                tmp.pop()

        backtrack([], 0)
        return result
