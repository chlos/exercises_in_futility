class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # (value, value_index, list_reference)
        min_heap = []

        # placing the first element of each list in the min-hea
        for arr in matrix:
            if arr:
                heapq.heappush(min_heap, (arr[0], 0, arr))

        count = 0
        curr_smallest = 0
        while min_heap:
            # get the smallest number from top of heap and its corresponding list
            curr_smallest, curr_smallest_i, curr_smallest_arr = heapq.heappop(min_heap)
            count += 1

            if count == k:
                break

            # if there are more elements in list of the top element
            # add the next element of that list to the min-heap
            next_i = curr_smallest_i + 1
            if next_i < len(curr_smallest_arr):
                heapq.heappush(min_heap, (curr_smallest_arr[next_i], next_i, curr_smallest_arr))

        return curr_smallest