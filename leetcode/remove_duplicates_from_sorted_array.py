#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        print 'before: ', nums
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        print 'after: ', nums, i, j
        return i + 1

s = Solution()
assert s.removeDuplicates([]) == 0
print '====='
assert s.removeDuplicates([1]) == 1
print '====='
assert s.removeDuplicates([1, 1]) == 1
print '====='
assert s.removeDuplicates([1, 2]) == 2
print '====='
assert s.removeDuplicates([2, 1]) == 2
print '====='
assert s.removeDuplicates([1, 1, 2, 3, 4, 4, 4]) == 4
print '====='
