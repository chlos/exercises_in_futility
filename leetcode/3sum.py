#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i, n in enumerate(nums):
            complement = target - n
            i_res = d.get(complement)
            if i_res is not None and i_res != i:
                return i, i_res
            d[n] = i

    # using twoSum()
    def threeSum_usingTwoSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3 or all((True if n > 0 else False for n in nums)):
            return result

        for n1 in set(nums):
            print 'n1:', n1
            two_sum_result = self.twoSum(nums, -n1)
            if two_sum_result is not None:
                i2, i3 = two_sum_result
                print 'n[{}], n[{}] = {}, {}'.format(i2, i3, nums[i2], nums[i3])
                curr_result = sorted([n1, nums[i2], nums[i3]])
                if curr_result not in result:
                    result.append(curr_result)

        print result
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result

        nums.sort()
        for i in xrange(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = nums[lo] + nums[i] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    result.append([nums[lo], nums[i], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1

        return result


s = Solution()
assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
