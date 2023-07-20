import collections
import heapq


# https://leetcode.com/problems/sliding-window-median/solutions/2122779/python-solution-with-two-heaps/
# https://leetcode.com/problems/sliding-window-median/solutions/394302/python-clean-solution-easy-to-understand/
class Solution:
    def calcMedian(self, small_max_heap, large_min_heap, k):
        # even window
        if k % 2 == 0:
            return (-small_max_heap[0] + large_min_heap[0]) / 2
        # odd window
        return -small_max_heap[0]

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        small_max_heap = []
        large_min_heap = []

        # prepare the first window
        for i in range(k):
            heapq.heappush(small_max_heap, -nums[i])
        for _ in range(k // 2):
            n = -heapq.heappop(small_max_heap)
            heapq.heappush(large_min_heap, n)
        median = self.calcMedian(small_max_heap, large_min_heap, k)
        result.append(median)

        out_nums_freq = collections.defaultdict(int)
        for i in range(k, len(nums)):
            # count freqs for outgoing numbers (candidates to be removed from the window)
            out_num = nums[i - k]
            out_nums_freq[out_num] += 1
            # rebalance heaps before eviction of outgoing num from large heap
            if out_num > -small_max_heap[0]:
                heapq.heappush(large_min_heap, -heapq.heappop(small_max_heap))

            # add a new num to the sliding window
            heapq.heappush(large_min_heap, nums[i])
            heapq.heappush(small_max_heap, -heapq.heappop(large_min_heap))

            # evict out num lazily from the curr window if needed
            # no matter how many elements are removed at the end of an iteration, they are invalid elements
            # so no additional re-balancing needed
            while small_max_heap and out_nums_freq[-small_max_heap[0]] > 0:
                evict_num = -heapq.heappop(small_max_heap)
                out_nums_freq[evict_num] -= 1
            while large_min_heap and out_nums_freq[large_min_heap[0]] > 0:
                evict_num = heapq.heappop(large_min_heap)
                out_nums_freq[evict_num] -= 1

            # calc median
            median = self.calcMedian(small_max_heap, large_min_heap, k)
            result.append(median)

        return result