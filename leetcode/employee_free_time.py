# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
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