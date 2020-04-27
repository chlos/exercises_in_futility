#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # N
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return i + 1

s = Solution()
assert s.searchInsert([3, 5, 6], 1) == 0
assert s.searchInsert([1, 3, 5, 6], 2) == 1
assert s.searchInsert([1, 3, 5, 6], 5) == 2
assert s.searchInsert([1, 3, 5, 6], 6) == 3
assert s.searchInsert([1, 3, 5, 6], 7) == 4
