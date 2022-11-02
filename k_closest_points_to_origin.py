import collections
import math
import heapq


def countDist(x, y):
    return math.sqrt(x ** 2 + y ** 2)


class Solution:
    # sort
    def kClosest_sort(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dists = [(x, y, countDist(x, y)) for x, y in points]
        sorted_points_dists = sorted(points_dists, key=lambda item: item[2])

        return [(sorted_points_dists[i][0], sorted_points_dists[i][1]) for i in range(k)]

    # min heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y, in points:
            heapq.heappush(heap, (-countDist(x, y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [(heap[i][1], heap[i][2]) for i in range(k)]
