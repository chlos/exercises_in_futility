#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # recursive, DFS
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

        # recursive, DFS

    def invertTree_recurDFS(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root

    # iter, DFS
    def invertTree_iterDFS(self, root):
        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    # iter, BFS
    def invertTree_iterBFS(self, root):
        if root is None:
            return None

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
