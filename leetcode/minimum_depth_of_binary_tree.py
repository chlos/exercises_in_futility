#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def minDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        curr_level = 1
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return curr_level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            curr_level += 1

    # DFS, recursion
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1