#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.has_path = False

        def dfs(node, curr_sum):
            if node is None:
                return

            if curr_sum - node.val == 0:
                if node.left is None and node.right is None:
                    self.has_path = True
                    print 'OK!'
                    return

            dfs(node.left, curr_sum - node.val)
            dfs(node.right, curr_sum - node.val)

        dfs(root, sum)
        return self.has_path
