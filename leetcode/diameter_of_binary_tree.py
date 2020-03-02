#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if node is None:
                return 0
            ld = dfs(node.left)
            rd = dfs(node.right)
            self.diameter = max(self.diameter, ld + rd)
            return max(ld, rd) + 1

        self.diameter = 0
        dfs(root)
        return self.diameter
