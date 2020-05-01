#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def smallerNumbersThanCurrent_BruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if i != j and nums[j] < nums[i]:
                    result[i] += 1

        print nums, result
        return result

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stats = {}
        result = nums[:]
        nums.sort()
        for i in xrange(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                pass
            else:
                stats[nums[i]] = i

        for i in xrange(len(result)):
            result[i] = stats[result[i]]

        return result
