#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(start_i, remains, tmp_nums):
            if remains == 0:
                # found!
                result.append(tmp_nums[::])
                return
            elif remains < 0:
                # stop checking new combinations
                return

            for i in xrange(start_i, len(candidates)):
                if i > start_i and candidates[i - 1] == candidates[i]:
                    continue

                tmp_nums.append(candidates[i])
                backtrack(i + 1, remains - candidates[i], tmp_nums)
                tmp_nums.pop()

        candidates.sort()
        result = []

        backtrack(0, target, [])
        return result
