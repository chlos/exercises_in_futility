START = 0
END = 1

TS = 0
TYPE = 1


class Solution:
    # sorting points
    def minMeetingRooms_sorting(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        points = []
        for start, end in intervals:
            points.append((start, START))
            points.append((end, END))

        points = sorted(points, key=lambda p: (p[TS], -p[TYPE]))

        max_overlapping = 0
        count_overlapping = 0
        for _, point_type in points:
            if point_type == START:
                count_overlapping += 1
            else:
                count_overlapping -= 1
            max_overlapping = max(max_overlapping, count_overlapping)
        
        return max_overlapping

    # priority queue / min heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda i: i[START])

        minheap = [intervals[0][END]]
        for i in range(1, len(intervals)):
            if minheap[0] <= intervals[i][START]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i][END])

        return len(minheap)


# NB: orderd map solution: https://leetcode.com/problems/meeting-rooms-ii/solutions/203658/hashmap-treemap-resolves-scheduling-problem/