#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # n**2
    def findUnsortedSubarray_bruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_i = -1
        right_i = len(nums)
        for i in xrange(len(nums)):
            local_min = min(nums[i:])
            if local_min == nums[i]:
                left_i = i
            else:
                break

        if left_i == len(nums) - 1:
            return 0

        for i in xrange(len(nums) - 1, -1, -1):
            local_max = max(nums[:i + 1])
            print local_max
            if local_max == nums[i]:
                right_i = i
            else:
                break

        return right_i - left_i - 1

    # sort: n log n
    def findUnsortedSubarray_sort(self, nums):
        left_i = len(nums)
        right_i = 0
        nums_sorted = sorted(nums[:])
        for i in xrange(len(nums)):
            if nums[i] != nums_sorted[i]:
                left_i = min(left_i, i)
                right_i = max(right_i, i)

        if right_i - left_i >= 0:
            return right_i - left_i + 1
        else:
            return 0

    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solutions/549567/c-solutions-two-pass-monotonic-stack-and-sort/
    # time O(n); space: O(1)
    def findUnsortedSubarray_twoPass(self, nums: List[int]) -> int:
        n = len(nums)
        left = n
        right = -1

        max_n = -float("inf")
        for i in range(n):
            max_n = max(max_n, nums[i])
            if nums[i] < max_n:
                right = max(right, i)

        min_n = float("inf")
        for i in reversed(range(n)):
            min_n = min(min_n, nums[i])
            if nums[i] > min_n:
                left = min(left, i)

        if left < right:
            return right - left + 1
        else:
            return 0

    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solutions/2003589/python-monotonic-stack-1-pass-o-n/
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solutions/2152333/python-solution-using-monotonic-stack/
    # time O(n); space: O(n)
    def findUnsortedSubarray_montonicStack(self, nums: List[int]) -> int:
        n = len(nums)
        left = n
        right = -1

        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for i in reversed(range(n)):
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)

        if left < right:
            return right - left + 1
        else:
            return 0

s = Solution()
l = s.findUnsortedSubarray([2, 1])
assert l == 2
