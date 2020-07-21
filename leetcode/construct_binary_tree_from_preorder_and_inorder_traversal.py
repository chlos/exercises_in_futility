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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def recur(left_idx, right_idx):
            if left_idx > right_idx:
                return

            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]
            root.left = recur(left_idx, root_idx - 1)
            root.right = recur(root_idx + 1, right_idx)
            return root

        return recur(0, len(inorder) - 1)