#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # This might be nice and easy to code up, but the asymptotic complexity is bad.
    # Slices take O(s) where 's' is the size of the slice.
    # Therefore this algorithm has runtime O(n lg n), space O(n),
    # wheras it could be done in O(n) runtime and O(lg n) space complexity
    # if passing indices of the start and end of string instead of the slices directly.
    def sortedArrayToBST_recur_slices(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root

    def sortedArrayToBST_recur_indexes(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def recur(left, right):
            if left > right:
                return None

            mid = (left + right + 1) / 2
            root = TreeNode(nums[mid])

            root.left = recur(left, mid - 1)
            root.right = recur(mid + 1, right)

            return root

        return recur(0, len(nums) - 1)

    # iterative:
    # https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/301769/Iterative-and-Recursive-Python-Solutions-with-Detailed-Explanations
