#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(remains, tmp_nums):
            if remains == 0:
                # found!
                result.append(tmp_nums)
                return
            elif remains < 0:
                # stop checking new combinations
                return

            for num in candidates:
                if num > remains:
                    break
                if tmp_nums and num < tmp_nums[-1]:
                    continue
                tmp_nums.append(num)
                backtrack(remains - num, tmp_nums[::])
                tmp_nums.pop()

        backtrack(target, [])
        return result
