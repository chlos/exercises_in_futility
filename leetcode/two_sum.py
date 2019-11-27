#!/usr/bin/env python
# -*- coding: utf-8 -*-


def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if n1 + n2 == target:
                    return i1, i2
