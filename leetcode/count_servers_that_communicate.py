#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        server_count_lines = [0] * len(grid)
        server_count_cols = [0] * len(grid[0])
        for line_n in xrange(len(grid)):
            for col_n in xrange(len(grid[0])):
                if grid[line_n][col_n]:
                    server_count_lines[line_n] += 1
                    server_count_cols[col_n] += 1
        for line_n in xrange(len(grid)):
            for col_n in xrange(len(grid[0])):
                if (
                    grid[line_n][col_n] and
                    (server_count_lines[line_n] > 1 or server_count_cols[col_n] > 1)
                ):
                    result += 1

        return result
