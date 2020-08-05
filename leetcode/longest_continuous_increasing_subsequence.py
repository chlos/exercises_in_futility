#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if len(nums) <= 1:
            return nums_len

        left = 0
        right = 1
        curr_subseq_len = 1
        while right < nums_len:
            if nums[right - 1] < nums[right]:
                right += 1
            else:
                curr_subseq_len = max(curr_subseq_len, right - left)
                left = right
                right += 1

        curr_subseq_len = max(curr_subseq_len, right - left)
        return curr_subseq_len