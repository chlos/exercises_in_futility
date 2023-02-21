import heapq
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ORIGIN = Point(0, 0)


def get_dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def k_closest(points, k):
    top_k = []  # min heap
    # init top with any first k points
    for i in range(k):
        heapq.heappush(top_k, (
            get_dist(ORIGIN, points[i]), id(points[i]), points[i]
        ))

    # maintain top k
    for i in range(k, len(points)):
        heapq.heappushpop(top_k, (
            get_dist(ORIGIN, points[i]), id(points[i]), points[i]
        ))

    return [point for dist, pid, point in top_k]