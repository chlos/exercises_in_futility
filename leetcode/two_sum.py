#!/usr/bin/env python
from collections import defaultdict


class Solution(object):
    # brute force
    def twoSum_BruteForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if i1 == i2:
                    continue
                if n1 + n2 == target:
                    return i1, i2

    # hash table: two-pass
    def twoSum_HashTwoPass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        # print d
        for n, i in d.iteritems():
            i1 = i[0]
            n2 = target - n
            if d.get(n2):
                for i2 in d[n2]:
                    if i2 == i1:
                        continue
                    # print i1, i2
                    return i1, i2

    # hash table: one-pass
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i, n in enumerate(nums):
            complement = target - n
            if d.get(complement) is not None:
                return i, d.get(complement)
            d[n] = i
