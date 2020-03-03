#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSumUglyBruteForce(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def check_sum(vals):
            for i in xrange(len(vals)):
                if sum(vals[i:]) == target_sum:
                    self.results_count += 1

        def dfs(node, curr_vals):
            if node is None:
                return

            curr_vals.append(node.val)
            check_sum(curr_vals)

            dfs(node.left, curr_vals[:])
            dfs(node.right, curr_vals[:])

        self.results_count = 0
        dfs(root, [])
        return self.results_count

    def dfs(self, node, target):
        if node is None:
            return

        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.result += 1

        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)

    # recursion, brute force
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.dfs(root, target)
        return self.result
