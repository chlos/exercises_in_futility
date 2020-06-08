#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST_recurExtraSpace(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def sum_recur(node, curr_sum, L, R):
            if node is None:
                return
            if node.val >= L and node.val <= R:
                curr_sum.append(node.val)
            sum_recur(node.left, curr_sum, L, R)
            sum_recur(node.right, curr_sum, L, R)

        result = []
        sum_recur(root, result, L, R)
        return sum(result)

    def rangeSumBST_recur(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0

        if not root:
            return result

        if root.val > L:
            result += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            result += self.rangeSumBST(root.right, L, R)

        if root.val >= L and root.val <= R:
            result += root.val

        return result

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if node.val >= L and node.val <= R:
                result += node.val

        return result
