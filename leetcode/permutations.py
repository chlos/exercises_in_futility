#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def permute_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def recur(l, r):
            if l == r:
                result.append(nums[::])
            for i in xrange(l, r):
                nums[i], nums[l] = nums[l], nums[i]
                recur(l + 1, r)
                # backtrack
                nums[i], nums[l] = nums[l], nums[i]

        recur(0, len(nums))
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def recur(tmp_nums, nums):
            if not nums:
                result.append(tmp_nums[::])

            for num in nums:
                tmp_nums.append(num)
                curr_nums = nums[::]
                curr_nums.remove(num)
                recur(tmp_nums, curr_nums)
                # backtrack
                tmp_nums.pop()

        recur([], nums)
        return result
