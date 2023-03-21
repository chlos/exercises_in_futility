#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution(object):
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


if __name__ == "__main__":
    s = Solution()

    print '\n====='
    assert s.canFinish(2, [[1, 0]])
    print '\n====='
    assert not s.canFinish(2, [[1, 0], [0, 1]])
    print '\n====='
    assert not s.canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]])
    print '\n====='
    assert s.canFinish(2, [[0, 1], [0, 2], [1, 2]])
    print 'OK'
