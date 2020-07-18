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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        nodes = deque()
        nodes.append(root)
        while nodes:
            curr_level = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                curr_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(curr_level)

        return result[::-1]