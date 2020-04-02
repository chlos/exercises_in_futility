#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeElement_1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print 'val: ', val
        print 'before: ', nums
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        print 'after: ', nums, 'len: ', n
        return n

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in xrange(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


s = Solution()
assert s.removeElement([2], 3) == 1
print '====='
assert s.removeElement([3, 3], 3) == 0
print '====='
