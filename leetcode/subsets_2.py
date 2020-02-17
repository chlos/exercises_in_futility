#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, idx):
            result.append(tmp[:])
            for i in xrange(idx, len(nums)):
                if i > idx and nums[i - 1] == nums[i]:
                    continue
                tmp.append(nums[i])
                backtrack(tmp, i + 1)
                tmp.pop()

        result = []
        if not nums:
            return result
        nums.sort()
        backtrack([], 0)
        return result
