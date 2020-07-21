#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS: use null-nodes as level separators
    def levelOrder_BFSnullNodes(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        nodes = deque()
        nodes.append(root)
        nodes.append(None)
        curr_level = []
        while nodes:
            node = nodes.popleft()
            if node is not None:
                curr_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            else:
                result.append(curr_level)
                curr_level = []
                if nodes:
                    nodes.append(None)

        return result

    # BFS: count levels
    def levelOrder_BFScountLevels(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        nodes = deque()
        nodes.append(root)
        while nodes:
            level_n = len(nodes)
            curr_level = []
            for _ in range(level_n):
                node = nodes.popleft()
                curr_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(curr_level)

        return result

    # DFS, preorder traverse, recursion
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(node, level, result):
            if not node:
                return

            if len(result) <= level:
                result.append([])
            result[level].append(node.val)

            traverse(node.left, level + 1, result)
            traverse(node.right, level + 1, result)

        result = []
        traverse(root, 0, result)
        return result