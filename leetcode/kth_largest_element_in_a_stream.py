#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from typing import List


# sort
class KthLargest_sort:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.data = nums

    def add(self, val: int) -> int:
        self.data.append(val)
        self.data.sort(reverse=True)
        print(self.data)
        return self.data[self.k - 1]


# heap: slow and naive
class KthLargest_1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.data = nums
        heapq.heapify(self.data)

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        return heapq.nlargest(self.k, self.data)[-1]


# heap
class KthLargest:
    """
    https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100/160977
    Create a pq - keep it only having the k-largest elements by popping off small elements.
    With only k elements, the smallest item (self.pool[0]) will always be the kth largest.

    If a new value is bigger than the smallest, it should be added into your heap.
    If it's bigger than the smallest (that are already the kth largest),
    it will certainly be within the kth largest of the stream.
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.pq = nums
        heapq.heapify(self.pq)
        while len(self.pq) > k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        else:
            # Push item on the heap, then pop and return the smallest item from the heap.
            # The combined action runs more efficiently than heappush() followed by a separate call to heappop().
            heapq.heappushpop(self.pq, val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)c:w

k = 3
# 8, 5, 4, 2
arr = [4, 5, 8, 2]
kl = KthLargest(3, arr)
# 8, 5, 4, 3, 2
assert kl.add(3) == 4
# 8, 5, 5, 4, 3, 2
assert kl.add(5) == 5
# 8, 5, 5, 4, 3, 2
assert kl.add(10) == 5
assert kl.add(9) == 8
assert kl.add(4) == 8
print('OK')