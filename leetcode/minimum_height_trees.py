#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


# FIXME
class Solution(object):
    def dfs(self, node, height):
        return
        if not self.graph[node]:
            return height + 1
        for n in self.graph[node]:
            height += self.dfs(n, height)

        return height

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.graph = defaultdict(list)
        for n1, n2 in edges:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)
        print '===== graph:', self.graph

        for node in self.graph:
            height = self.dfs(node, 0)
            print height


if __name__ == "__main__":
    s = Solution()

    res = s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    print res
    assert res == [1]
