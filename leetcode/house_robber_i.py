#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        costs = [0] * len(nums)
        costs[0] = nums[0]
        costs[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            costs[i] = max(costs[i - 2] + nums[i], costs[i - 1])
        return costs[-1]
