#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_recurse(self, root: TreeNode) -> List[int]:
        def traverse(node, path):
            if not node:
                return
            traverse(node.left, path)
            path.append(node.val)
            traverse(node.right, path)

        result = []
        traverse(root, result)
        return result

    # iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                tmp_node = stack.pop()
                result.append(tmp_node.val)
                node = tmp_node.right

        return result