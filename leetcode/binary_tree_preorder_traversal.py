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
    def preorderTraversal_recurse(self, root: TreeNode) -> List[int]:
        def traverse(node, path):
            if not node:
                return
            path.append(node.val)
            traverse(node.left, path)
            traverse(node.right, path)

        result = []
        traverse(root, result)
        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return result