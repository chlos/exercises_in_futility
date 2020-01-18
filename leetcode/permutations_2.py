#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def recur(tmp_nums, nums):
            if not nums:
                result.append(tmp_nums[::])

            for num in set(nums):
                tmp_nums.append(num)
                curr_nums = nums[::]
                curr_nums.remove(num)
                recur(tmp_nums, curr_nums)
                # backtrack
                tmp_nums.pop()

        recur([], nums)
        return result
