#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # cascading
    def subsets_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [
                curr_result + [num] for curr_result in result
            ]

        return result

    # backtracking
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(tmp, idx):
            result.append(tmp[:])
            for i in xrange(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(tmp, i + 1)
                tmp.pop()

        backtrack([], 0)
        return result


def is_bit_set(num, bit):
    x = (1 << bit) & num
    if x == 0:
        return False
    return True


class Solution:
    # bitmask
    #
    # nums = [1, 2, 3]
    # bitmasks (0...2**len(nums)-1):
    # 0 000
    # 1 001
    # 2 010
    # 3 011
    # 4 100
    # 5 101
    # 6 110
    # 7 111
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        if not nums:
            return [[]]

        for bitmask in range(2 ** len(nums)):
            curr_set = []
            for num_i in range(len(nums)):
                if is_bit_set(bitmask, bit=num_i):
                    curr_set.append(nums[num_i])
            sets.append(curr_set)

        return set