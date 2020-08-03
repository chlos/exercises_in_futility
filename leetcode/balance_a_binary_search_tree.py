#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traverse(self, root, vals):
        if root is None:
            return root
        self.inorder_traverse(root.left, vals)
        vals.append(root.val)
        self.inorder_traverse(root.right, vals)

    def construct_tree(self, vals, left, right):
        if left > right:
            return

        mid = (left + right) // 2
        val = vals[mid]
        root = TreeNode(val)
        root.left = self.construct_tree(vals, left, mid - 1)
        root.right = self.construct_tree(vals, mid + 1, right)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        self.inorder_traverse(root, vals)
        return self.construct_tree(vals, 0, len(vals) - 1)