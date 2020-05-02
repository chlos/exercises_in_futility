#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # flip symmetrically
        for i in xrange(n):
            for j in xrange(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # flip around vertical axis
        for i in xrange(n):
            for j in xrange(n / 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = tmp

        return matrix

    def rotate_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        matrix.reverse()

        # flip symmetrically
        for i in xrange(n):
            for j in xrange(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        return matrix


s = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
expected = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
result = s.rotate(m)
print result
assert result == expected
print 'OK'
