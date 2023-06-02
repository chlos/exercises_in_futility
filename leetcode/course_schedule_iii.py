#!/usr/bin/env python
# -*- coding: utf-8 -*-


import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses: [[duration_1, last_day_1], ... [duration_i, last_day_i]]
        # sort by deadline
        courses.sort(key=lambda c: c[1])
        #

        # iterate through each course,
        # if we have enough days, we'll add it to our priority queue
        # if we don't have enough days, then we can pop longest course
        total_time = 0
        max_heap_durations = []
        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap_durations, -duration)

            if total_time > last_day:
                curr_max_duration = -heapq.heappop(max_heap_durations)
                total_time -= curr_max_duration

        return len(max_heap_durations)