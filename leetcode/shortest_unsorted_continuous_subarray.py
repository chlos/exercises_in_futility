#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # n**2
    def findUnsortedSubarray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_i = -1
        right_i = len(nums)
        for i in xrange(len(nums)):
            local_min = min(nums[i:])
            if local_min == nums[i]:
                left_i = i
            else:
                break

        if left_i == len(nums) - 1:
            return 0

        for i in xrange(len(nums) - 1, -1, -1):
            local_max = max(nums[:i + 1])
            print local_max
            if local_max == nums[i]:
                right_i = i
            else:
                break

        return right_i - left_i - 1

    # sort: n log n
    def findUnsortedSubarray(self, nums):
        left_i = len(nums)
        right_i = 0
        nums_sorted = sorted(nums[:])
        for i in xrange(len(nums)):
            if nums[i] != nums_sorted[i]:
                left_i = min(left_i, i)
                right_i = max(right_i, i)

        if right_i - left_i >= 0:
            return right_i - left_i + 1
        else:
            return 0

s = Solution()
l = s.findUnsortedSubarray([2, 1])
assert l == 2
