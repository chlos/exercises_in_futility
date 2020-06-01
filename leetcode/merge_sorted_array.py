#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0
        i1_back_init = m
        while i2 < n:
            if nums1[i1] >= nums2[i2] or i1 >= i1_back_init:
                i1_back = i1_back_init
                while i1_back > i1:
                    nums1[i1_back] = nums1[i1_back - 1]
                    i1_back -= 1
                nums1[i1] = nums2[i2]
                i2 += 1
                i1_back_init += 1
            i1 += 1

    def merge_hack(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()


s = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
s.merge(nums1, 3, nums2, len(nums2))
print nums1
assert nums1 == [1, 2, 2, 3, 5, 6]
print 'ok'

nums1 = [1, 1, 1, 0, 0, 0]
nums2 = [1, 1, 1]
s.merge(nums1, 3, nums2, len(nums2))
print nums1
assert nums1 == [1, 1, 1, 1, 1, 1]
print 'ok'
