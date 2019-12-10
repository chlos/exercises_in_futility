#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1
