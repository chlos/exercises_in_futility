# similar: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS; take the right-most node from each level
    # we start each level with a right-most node,
    # so let's just append it to the result
    def rightSideView_DFS(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if node is None:
                return

            nonlocal result
            if len(result) == depth:
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result

    # BFS
    # two queues: curr level and next level,
    # take the righ-most node from each "next" level
    def rightSideView_BFStwoQueues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        curr_level_queue = collections.deque()
        next_level_queue = collections.deque([root])
        while next_level_queue:
            curr_level_queue = next_level_queue
            next_level_queue = collections.deque()
            while curr_level_queue:
                node = curr_level_queue.popleft()
                if node.left is not None:
                    next_level_queue.append(node.left)
                if node.right is not None:
                    next_level_queue.append(node.right)

            # right-most node on the curr level
            result.append(node.val)

        return result

    # BFS
    # one queue + sentinel marker
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        queue = collections.deque([root, None])  # 1st level
        prev_node, curr_node = None, root
        while queue:
            prev_node, curr_node = curr_node, queue.popleft()

            # iterate through the current level
            while curr_node:
                # add next level's nodes
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)
                prev_node, curr_node = curr_node, queue.popleft()
            # add the last node of the current level
            result.append(prev_node.val)

            # separate the current and next levels
            if queue:
                queue.append(None)

        return result

    # BFS
    def rightSideView_tmp(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        # FIXME

        return result
