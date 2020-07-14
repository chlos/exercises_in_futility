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
    def postorderTraversal_recurse(self, root: TreeNode) -> List[int]:
        def traverse(node, path):
            if not node:
                return
            traverse(node.left, path)
            traverse(node.right, path)
            path.append(node.val)

        result = []
        traverse(root, result)
        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result