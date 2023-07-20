import heapq

START = 0
END = 1


def find_sets(intervals):
    if not intervals:
        return 0

    intervals.sort()

    pq_ends = []
    for i in range(len(intervals)):
        if pq_ends and intervals[i][START] >= pq_ends[0]:
            heapq.heappop(pq_ends)
        
        heapq.heappush(pq_ends, intervals[i][END])

    return len(pq_ends)