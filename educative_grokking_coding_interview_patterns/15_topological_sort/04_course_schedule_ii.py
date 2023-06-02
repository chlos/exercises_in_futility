#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
    def dfs(self, vertex, visited, stack):
        if vertex in stack:
            return True
        if visited[vertex]:
            return False
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not self.dfs(i, visited, stack):
                return False

        stack.append(vertex)
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = defaultdict(list)
        for course, pre in prerequisites:
            self.graph[course].append(pre)

        visited = [False] * numCourses
        stack = []
        for i in xrange(numCourses):
            if not self.dfs(i, visited, stack):
                return []

        return stack    # FIXME

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
