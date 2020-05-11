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
            print course, visited       # FIXME
            if course in visited:
                print 'VISITED!'
                return True

            visited.add(course)
            for pre in courses_graph[course]:
                return is_cycle(pre, visited)

            print 'OK, no cycle'
            return False

        courses_graph = defaultdict(list)
        for course, pre in prerequisites:
            courses_graph[course].append(pre)
        print courses_graph     # FIXME

        # for course in courses_graph.iterkeys():
        for course in list(courses_graph):
            print course    # FIXME
            if is_cycle(course, set()):
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
    print 'OK'
