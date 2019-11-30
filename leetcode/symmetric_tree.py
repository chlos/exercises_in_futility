#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricRecur(tree1, tree2):
            if tree1 is None or tree2 is None:
                return tree1 == tree2
            if tree1.val != tree2.val:
                return False

            return (
                isSymmetricRecur(tree1.left, tree2.right) and
                isSymmetricRecur(tree1.right, tree2.left)
            )

        if root is None:
            return True

        return isSymmetricRecur(root.left, root.right)
