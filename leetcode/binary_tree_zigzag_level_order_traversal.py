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
    def zigzagLevelOrder_1(self, root: TreeNode) -> List[List[int]]:
        def traverse(node, path, level):
            if not node:
                return

            if len(path) <= level:
                path.append([])

            if level % 2:
                path[level].insert(0, node.val)
            else:
                path[level].append(node.val)
            traverse(node.left, path, level + 1)
            traverse(node.right, path, level + 1)

        path = []
        traverse(root, path, 0)
        print(path)
        return path

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result

        left_to_right = True
        nodes_deque = deque()
        nodes_deque.append(root)
        while nodes_deque:
            curr_deque_len = len(nodes_deque)
            curr_level = [None] * curr_deque_len
            for i in range(curr_deque_len):
                curr_node = nodes_deque.popleft()

                if left_to_right:
                    val_i = i
                else:
                    val_i = curr_deque_len - i - 1
                curr_level[val_i] = curr_node.val

                if curr_node.left:
                    nodes_deque.append(curr_node.left)
                if curr_node.right:
                    nodes_deque.append(curr_node.right)

            left_to_right = not left_to_right
            result.append(curr_level)

        return result