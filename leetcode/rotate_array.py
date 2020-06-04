#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def rev(a, l, r):
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n
        rev(nums, n - k, n - 1)
        rev(nums, 0, n - k - 1)
        rev(nums, 0, n - 1)
