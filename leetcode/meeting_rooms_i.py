# index in point tuple
ITS = 0
ITYPE = 1

# types of points
START = 0
END = 1


class Solution:
    # overkill with counting overlapping meetings (good for further "meeting room" tasks)
    def canAttendMeetings_count(self, intervals: List[List[int]]) -> bool:
        time_points = []
        for start, end in intervals:
            time_points.append((start, START))
            time_points.append((end, END))

        time_points = sorted(time_points, key=lambda p: (p[ITS], -p[ITYPE]))

        overlapping_count = 0
        overlapping_max = 0
        for point in time_points:
            if point[ITYPE] == START:
                overlapping_count += 1
            else:
                overlapping_count -= 1
            overlapping_max = max(overlapping_max, overlapping_count)

        return (overlapping_max <= 1)

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        for i in range(len(intervals) - 1):
            if intervals[i][END] > intervals[i + 1][START]:
                return False

        return True