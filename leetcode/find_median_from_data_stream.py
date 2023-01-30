class MedianFinder:

    def __init__(self):
        # elements less than median; max heap
        self.small_heap = []
        # elements greater than median; min heap
        self.large_heap = []

    def addNum(self, num: int) -> None:
        if len(self.small_heap) == 0 and len(self.large_heap) == 0:
            self.small_heap.append(-num)
            return

        if num < self.findMedian():
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)

        # re-balance if needed
        if len(self.small_heap) < len(self.large_heap):
            tmp_n = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -tmp_n)
        elif len(self.small_heap) - len(self.large_heap) > 1:
            tmp_n = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, tmp_n)

    def findMedian(self) -> float:
        # even number of elements => median is an avg of two mid values
        if (len(self.small_heap) + len(self.large_heap)) % 2 == 0:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        # otherwise it's mid values
        return -self.small_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()