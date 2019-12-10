#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr_node = root
        while True:
            if val < curr_node.val:
                if curr_node.left is None:
                    curr_node.left = TreeNode(val)
                    return root
                curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = TreeNode(val)
                    return root
                curr_node = curr_node.right
