# best explaination: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/510262/detailed-analysis-let-me-lead-you-to-the-solution-step-by-step/
# good explaination: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/1116371/python-with-detailed-explanation/

import heapq

START = 0
END = 1

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort by start days
        events = sorted(events)

        days = max(event[END] for event in events)
        minheap = []

        days_attended = 0
        curr_day = 1
        event_i = 0
        while curr_day <= days:
            # skip days without events
            if event_i < len(events) and not minheap:
                curr_day = events[event_i][START]

            # add events starting before the current day or today
            while event_i < len(events) and events[event_i][START] <= curr_day:
                heapq.heappush(minheap, events[event_i][END])
                event_i += 1

            # rm events already ended by the current day
            while minheap and minheap[0] < curr_day:
                heapq.heappop(minheap)

            # attend event ending first
            if minheap:
                heapq.heappop(minheap)
                days_attended += 1
            elif event_i >= len(events):
                break

            curr_day += 1

        return days_attended