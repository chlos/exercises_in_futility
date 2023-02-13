import heapq

# Tip: You may use some of the code templates provided
# in the support files

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.k = k

        self.top_k = []
        for n in nums:
            heapq.heappush(self.top_k, n)
        while len(self.top_k) > self.k:
            heapq.heappop(self.top_k)

    # adds element in the heap
    def add(self, val):
        heapq.heappush(self.top_k, val)
        if len(self.top_k) > self.k:
            heapq.heappop(self.top_k)
        return self.return_Kth_largest()

    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.top_k[0]