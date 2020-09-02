#!/usr/bin/env python3

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0
        left_person = -1
        for i in range(len(seats)):
            if seats[i]:
                if left_person < 0:
                    curr_dist = i
                else:
                    curr_dist = (i - left_person) // 2
                result = max(result, curr_dist)
                left_person = i

        return max(result, len(seats) - left_person - 1)


s = Solution()
assert s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert s.maxDistToClosest([1, 0, 0, 0]) == 3