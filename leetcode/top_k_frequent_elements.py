from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freqs = collections.Counter(nums)

        heap = [(-count, num) for num, count in freqs.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)

        return result