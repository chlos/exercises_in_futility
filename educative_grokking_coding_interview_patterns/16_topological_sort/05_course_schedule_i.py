#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    # DFS, check cycles
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def is_cycle(course, visited):
            # print course, visited       # FIXME
            if visited[course]:
                # print 'VISITED!'
                return True

            visited[course] = True
            for pre in courses_graph[course]:
                # print 'pre:', pre
                if not visited[pre]:
                    if is_cycle(pre, visited):
                        return True
                else:
                    return True

            # print 'OK, no cycle'
            visited[course] = False
            return False

        courses_graph = defaultdict(list)
        for course, pre in prerequisites:
            courses_graph[course].append(pre)
        # print courses_graph     # FIXME

        visited = [False] * numCourses
        for course in xrange(numCourses):
            # print 'course: ', course    # FIXME
            if is_cycle(course, visited):
                return False

        return True


class Solution:
    # topological sort; Kahn's algorithm; BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph = {node: [] for node in range(numCourses)}
        in_degrees = {node: 0 for node in range(numCourses)}
        for child_node, parent_node in prerequisites:
            graph[parent_node].append(child_node)
            in_degrees[child_node] += 1

        # find sources
        sources = collections.deque()
        for node, in_count in in_degrees.items():
            if in_count <= 0:
                sources.append(node)

        # take courses with prereqs satisfied
        courses_taken = 0
        while sources:
            curr_node = sources.popleft()
            courses_taken += 1
            child_nodes = graph[curr_node]
            for child_node in child_nodes:
                in_degrees[child_node] -= 1
                if in_degrees[child_node] <= 0:
                    sources.append(child_node)

        if courses_taken != numCourses:
            return False

        return True
