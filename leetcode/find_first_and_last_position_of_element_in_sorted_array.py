#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def searchRange01(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_i, last_i = -1, -1
        if not nums:
            return first_i, last_i

        l = 0
        r = len(nums) - 1
        found_i = -1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                found_i = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if found_i < 0:
            return -1, -1

        first_i, last_i = found_i, found_i
        while True:
            if first_i == 0 or nums[first_i-1] != target:
                break
            first_i -= 1
        while True:
            if last_i == len(nums)-1 or nums[last_i+1] != target:
                break
            last_i += 1

        return first_i, last_i

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1, -1

        l = 0
        r = len(nums) - 1
        first_i = -1
        print 'target: {}; nums: {}'.format(target, nums)
        while l <= r:
            mid = (l + r) / 2
            print 'l: nums[{}]: {}'.format(mid, nums[mid])
            if nums[mid] == target and mid == 0 or nums[mid] == target and nums[mid-1] < nums[mid]:
                first_i = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        print 'first_i: {}, nums[{}]: {}'.format(first_i, first_i, nums[first_i])
        if first_i < 0:
            print 'not found'
            return -1, -1

        l = first_i + 1
        r = len(nums) - 1
        last_i = first_i
        print 'target: {}; nums: {}'.format(target, nums)
        while l <= r:
            mid = (l + r) / 2
            print 'l = {}; r = {}'.format(l, r)
            print 'r: nums[{}]: {}'.format(mid, nums[mid])
            if nums[mid] == target and mid == len(nums)-1 or nums[mid] == target and nums[mid+1] > nums[mid]:
                last_i = mid
                print 'FOUND'
                break
            elif nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        print 'last_i: {}, nums[{}]: {}'.format(last_i, last_i, nums[last_i])

        return first_i, last_i

s = Solution()
assert s.searchRange([], 1) == (-1, -1)
print 'OK\n'

assert s.searchRange([1], 9) == (-1, -1)
print 'OK\n'
assert s.searchRange([1], 1) == (0, 0)
print 'OK\n'

assert s.searchRange([1, 2], 1) == (0, 0)
print 'OK\n'
assert s.searchRange([1, 2], 2) == (1, 1)
print 'OK\n'
assert s.searchRange([1, 1], 2) == (-1, -1)
print 'OK\n'
assert s.searchRange([1, 1], 1) == (0, 1)
print 'OK\n'

assert s.searchRange([1, 2, 3], 4) == (-1, -1)
print 'OK\n'
assert s.searchRange([1, 2, 3], 1) == (0, 0)
print 'OK\n'
assert s.searchRange([1, 2, 3], 2) == (1, 1)
print 'OK\n'
assert s.searchRange([1, 2, 3], 3) == (2, 2)
print 'OK\n'
assert s.searchRange([1, 1, 3], 1) == (0, 1)
print 'OK\n'
assert s.searchRange([1, 2, 2], 2) == (1, 2)
print 'OK\n'
assert s.searchRange([3, 3, 3], 3) == (0, 2)
print 'OK\n'
