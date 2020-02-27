#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)

        invert(root)
        return root
