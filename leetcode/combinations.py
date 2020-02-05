#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(curr_nums, curr_k, tmp_res):
            if curr_k == 0:
                result.append(tmp_res)

            if len(curr_nums) < curr_k:
                return

            for i in xrange(len(curr_nums)):
                dfs(curr_nums[i + 1:], curr_k - 1, tmp_res + [curr_nums[i]])

        result = []
        nums = range(1, n + 1)

        dfs(nums, k, [])
        return result
