#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result_n = 0
        curr_i = 0
        while curr_i < len(flowerbed):
            if curr_i == 0:
                prev_place_taken = 0
            else:
                prev_place_taken = flowerbed[curr_i - 1]

            curr_place_taken = flowerbed[curr_i]

            if curr_i == len(flowerbed) - 1:
                next_place_taken = 0
            else:
                next_place_taken = flowerbed[curr_i + 1]

            if not prev_place_taken and not next_place_taken and not curr_place_taken:
                result_n += 1
                curr_i += 2
            else:
                curr_i += 1

            if result_n >= n:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert not s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print('OK')