START = 0
END = 1

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        merged_interval = [newInterval[START], newInterval[END]]

        for interval in intervals:
            if merged_interval is not None and merged_interval[END] < interval[START]:
                result.append(merged_interval)
                merged_interval = None

            if interval[START] < newInterval[START]:
                # no overlapping
                if interval[END] < newInterval[START]:
                    result.append(interval)
                # intersection from the left
                elif newInterval[START] <= interval[END] <= newInterval[END]:
                    merged_interval[START] = interval[START]
                # new interval is inside the current one
                elif newInterval[END] <= interval[END]:
                    result.append(interval)
                    merged_interval = None
            elif newInterval[START] <= interval[START] <= newInterval[END]:
                print("newInterval[START] <= interval[START] <= newInterval[END]")
                # current interval is inside the new one
                if interval[END] <= newInterval[END]:
                    continue
                # intersection from the right
                elif newInterval[END] < interval[END]:
                    merged_interval[END] = interval[END]
                    result.append(merged_interval)
                    merged_interval = None
                    continue
            # no overlapping
            elif newInterval[END] < interval[START]:
                result.append(interval)

        if merged_interval is not None:
            result.append(merged_interval)

        return result