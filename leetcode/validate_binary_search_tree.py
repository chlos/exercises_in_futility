#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidRecurse(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not isValidRecurse(node.left, lower=lower, upper=node.val):
                return False
            if not isValidRecurse(node.right, lower=node.val, upper=upper):
                return False

            return True

        return isValidRecurse(root)
