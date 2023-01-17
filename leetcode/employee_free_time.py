import heapq


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    # sweep line
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        free_intervals = []

        work_intervals = []
        for user_work_intervals in schedule:
            work_intervals += user_work_intervals
        work_intervals.sort(key=lambda i: i.start)

        curr_latest_end = None
        for work_interval in work_intervals:
            if curr_latest_end is not None and work_interval.start > curr_latest_end:
                free_intervals.append(Interval(curr_latest_end, work_interval.start))
                curr_latest_end = work_interval.end
                continue
            
            if curr_latest_end is None or work_interval.end > curr_latest_end:
                curr_latest_end = work_interval.end

        return free_intervals

    # min heap / priority queue
    def employeeFreeTime_pq(self, schedule: '[[Interval]]') -> '[Interval]':
        free_intervals = []

        pq_work_intervals = []
        for user_work_intervals in schedule:
            for user_work_interval in user_work_intervals:
                start, end = user_work_interval.start, user_work_interval.end
                heapq.heappush(pq_work_intervals, (start, end))

        start, curr_latest_end = heapq.heappop(pq_work_intervals)
        while pq_work_intervals:
            start, end = heapq.heappop(pq_work_intervals)
            if start > curr_latest_end:
                free_intervals.append(Interval(curr_latest_end, start))
            curr_latest_end = max(curr_latest_end, end)

        return free_intervals