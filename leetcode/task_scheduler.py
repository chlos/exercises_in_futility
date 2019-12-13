#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_count = Counter(tasks)
        heap = []
        for task, count in tasks_count.iteritems():
            heapq.heappush(heap, (-count, task))

        intervals_count = 0
        while heap:
            temp_tasks = []
            cycle_i = n + 1

            while cycle_i and heap:
                task_count, task = heapq.heappop(heap)
                temp_tasks.append((-task_count - 1, task))
                intervals_count += 1
                cycle_i -= 1

            for task_count, task in temp_tasks:
                if task_count > 0:
                    heapq.heappush(heap, (-task_count, task))

            if heap:
                intervals_count += cycle_i

        return intervals_count
