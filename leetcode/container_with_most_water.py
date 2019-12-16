#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_area = max(
                max_area,
                min(height[l], height[r]) * (r - l)
            )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
