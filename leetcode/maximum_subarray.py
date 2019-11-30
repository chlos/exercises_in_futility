#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if max(nums) < 0:
            return max(nums)

        global_max = local_max = nums[0]
        for i in xrange(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max
        return global_max
