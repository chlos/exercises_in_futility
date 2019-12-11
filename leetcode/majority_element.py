#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    # time: O(n)
    # space: O(n)
    def majorityElementDict(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums) / 2
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        for num, count in nums_count.iteritems():
            if count > majority_count:
                return num

    # time: O(n log n)
    # space: O(1) / O(n)
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) / 2]
