#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if len(nums) <= 1:
            return nums_len

        l = 0
        r = 1
        curr_subseq_len = 1
        while r < nums_len:
            if nums[r - 1] < nums[r]:
                r += 1
            else:
                curr_subseq_len = max(curr_subseq_len, r - l)
                l = r
                r += 1

        curr_subseq_len = max(curr_subseq_len, r - l)
        return curr_subseq_len