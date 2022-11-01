from typing import List
import collections
import heapq


class Solution:
    # heap
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
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

    # sorted list of pairs
    def topKFrequent_sortedPairsList(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int)
        for n in nums:
            freqs[n] += 1

        pairs = list()
        for n, freq in freqs.items():
            pairs.append((n, freq))
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        return [pairs[i][0] for i in range(k)]

    # buckets
    # https://leetcode.com/problems/top-k-frequent-elements/solutions/81602/java-o-n-solution-bucket-sort/
    def topKFrequent_buckets(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        buckets = [[] for range in range(len(nums) + 1)]
        for n, freq in freqs.items():
            buckets[freq].append(n)

        result = []
        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            if not bucket:
                continue
            for n in bucket:
                result.append(n)
                if len(result) >= k:
                    return result