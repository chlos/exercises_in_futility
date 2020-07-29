#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST_recur(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root

        # discard the whole left subtree
        if root.val < L:
            return self.trimBST(root.right, L, R)

        # if root.val > R: discard the whole right subtree
        if root.val > R:
            return self.trimBST(root.left, L, R)

        # if root.val in [L, R], proceed with both left and right subtrees
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root

    # iterative
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root

        # find a new root
        while root.val < L or R < root.val:
            if root.val < L:
                root = root.right
            if root.val > R:
                root = root.left

        # trim left subtree
        node = root
        while node:
            while node.left and node.left.val < L:
                node.left = node.left.right
            node = node.left

        # trim right subtree
        node = root
        while node:
            while node.right and node.right.val > R:
                node.right = node.right.left
            node = node.right

        return root