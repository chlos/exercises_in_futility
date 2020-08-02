#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # insert at the most bottom leaf
    def insertIntoBST_retur(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)

        if root is None:
            return new_node

        curr_node = root
        while curr_node != new_node:
            if curr_node.val < val:
                if curr_node.right is None:
                    curr_node.right = new_node
                curr_node = curr_node.right
            elif curr_node.val > val:
                if curr_node.left is None:
                    curr_node.left = new_node
                curr_node = curr_node.left

        return root