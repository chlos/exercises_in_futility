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

if __name__ == "__main__":
    s = Solution()

    order = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order == [0, 1, 2, 3]
    order = s.findOrder(2, [[1, 0]])
    assert order == [0, 1]
    order = s.findOrder(2, [[0, 1], [1, 0]])
    assert order == []
