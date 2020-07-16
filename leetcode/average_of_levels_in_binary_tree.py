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


# see the https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if not root:
            return result

        nodes = deque()
        nodes.append(root)
        while nodes:
            level_n = len(nodes)
            level_sum = 0
            for _ in range(level_n):
                node = nodes.popleft()
                level_sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(level_sum / level_n)

        return result