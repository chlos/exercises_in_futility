START = 0
END = 1


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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