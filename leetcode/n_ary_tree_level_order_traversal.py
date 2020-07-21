#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # BFS
    def levelOrder_BFS(self, root: 'Node') -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            curr_level = []
            curr_queue_len = len(queue)
            for _ in range(curr_queue_len):
                node = queue.popleft()
                curr_level.append(node.val)
                for child_node in node.children:
                    queue.append(child_node)
            result.append(curr_level)

        return result

    # recursion
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse(node, result, level):
            if node is None:
                return

            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse(child, result, level + 1)

        result = []
        traverse(root, result, 0)
        return result