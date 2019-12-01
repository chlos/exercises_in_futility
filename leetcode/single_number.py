#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    def singleNumber_Count(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        for num, count in nums_count.iteritems():
            if count == 1:
                return num

    def singleNumber_Hashmap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            try:
                nums_dict.pop(num)
            except:
                nums_dict[num] = True
        return nums_dict.popitem()[0]

    def singleNumber_Math(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    # bitwise
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        return xor_sum
