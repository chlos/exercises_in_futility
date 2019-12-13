#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def moveZeroes(self, nums):
        last_non_zero_i = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_i], nums[i] = nums[i], nums[last_non_zero_i]
                last_non_zero_i += 1

        return nums

    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_i = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_i] = nums[i]
                last_non_zero_i += 1
        for i in xrange(last_non_zero_i, len(nums)):
            nums[i] = 0
        return nums
