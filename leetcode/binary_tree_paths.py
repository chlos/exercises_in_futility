#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def rec(node, curr_path, paths):
            if node is None:
                return

            curr_path.append(node.val)
            if node.left is None and node.right is None:
                paths.append('->'.join(map(str, curr_path)))
                return

            rec(node.left, curr_path[:], paths)
            rec(node.right, curr_path[:], paths)

        paths = []
        rec(root, [], paths)
        return paths

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if not root:
            return paths

        nodes_stack = [(root, [])]
        while nodes_stack:
            node, curr_path = nodes_stack.pop()
            curr_path.append(node.val)
            if node.left is None and node.right is None:
                paths.append('->'.join(map(str, curr_path)))
                continue
            if node.left:
                nodes_stack.append((node.left, curr_path[:]))
            if node.right:
                nodes_stack.append((node.right, curr_path[:]))

        return paths
