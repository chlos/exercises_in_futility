#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        print('')
        is_modified = False
        for i in range(1, len(nums)):
            print(i, nums[i])
            if nums[i - 1] > nums[i]:
                print('nums[i - 1] > nums[i]')
                if is_modified:
                    return False
                is_modified = True

                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    # nums[i-1] is too big
                    print('nums[i-1] is too big')
                    nums[i - 1] = nums[i]
                else:
                    # nums[i] is too small
                    print('nums[i] is too small')
                    nums[i] = nums[i - 1]

        return True


if __name__ == "__main__":
    s = Solution()

    assert s.checkPossibility([4, 2, 3])
    assert not s.checkPossibility([4, 2, 1])
    assert not s.checkPossibility([3, 4, 2, 3])
    assert s.checkPossibility([-1, 4, 2, 3])
    print('OK')