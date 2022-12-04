class Solution:
    def merge_sort_my(self, intervals: List[List[int]]) -> List[List[int]]:
        START = 0
        END = 1

        points = []
        for start, end in intervals:
            points.append([start, START])
            points.append([end, END])
        points = sorted(points, key=lambda p: (p[0], p[1]))

        result = []
        cur_interval = [None, None]
        started_count = 0
        for point, typ in points:
            if typ == START:
                started_count += 1
                if started_count == 1:
                    cur_interval[0] = point
            elif typ == END:
                started_count -= 1
                if started_count == 0:
                    cur_interval[1] = point
                    result.append(cur_interval[:])
        
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START = 0
        END = 1

        intervals = sorted(intervals, key=lambda i: i[START])

        result = []
        for interval in intervals:
            if not result or result[-1][END] < interval[START]:
                result.append(interval)
            else:
                result[-1][END] = max(result[-1][END], interval[END])

        return result