#!/usr/bin/env python3

import heapq
import random
from typing import List


class Solution:
    # naive, sort (N logN)
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    # heap
    def findKthLargest_heap1(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        print('nums[0]:', nums[0])
        return -nums[0]

    # heap
    def findKthLargest_heap2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

    # https://en.wikipedia.org/wiki/Quickselect
    # https://www.freecodecamp.org/news/quickselect-algorithm-explained-with-examples/
    # https://stackoverflow.com/questions/10846482/quickselect-algorithm-understanding
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(li, ri):
            pivot = random.randint(li, ri)
            pivot_value = nums[pivot]
            nums[pivot], nums[ri] = nums[ri], nums[pivot]
            store_i = li
            for i in range(li, ri):
                if nums[i] >= pivot_value:
                    nums[store_i], nums[i] = nums[i], nums[store_i]
                    store_i += 1
            nums[ri], nums[store_i] = nums[store_i], nums[ri]
            return store_i

        li = 0
        ri = len(nums) - 1
        k = k - 1
        while True:
            pos = partition(li, ri)
            if pos < k:
                li = pos + 1
            elif pos > k:
                ri = pos - 1
            else:
                return nums[pos]


if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    #              v
    # [1, 2, 3, 4, 5, 6]
    assert s.findKthLargest(nums, k) == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    #                 v
    # [1, 2, 2, 3, 3, 4, 5, 5, 6]
    assert s.findKthLargest(nums, k) == 4

    print('OK')