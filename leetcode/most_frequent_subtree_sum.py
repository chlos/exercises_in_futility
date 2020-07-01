#!/usr/bin/env python3

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_01:
    def count_subtree_sum(self, node):
        if node is None:
            return 0
        return (
            node.val +
            self.count_subtree_sum(node.left) +
            self.count_subtree_sum(node.right)
        )

    def traverse(self, node, sums):
        if node is None:
            return
        sums[self.count_subtree_sum(node)] += 1
        self.traverse(node.left, sums)
        self.traverse(node.right, sums)

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        sums = defaultdict(int)
        self.traverse(root, sums)
        max_freq = max(sums.values())
        return [s for s, freq in sums.items() if freq == max_freq]


class Solution:
    def traverse(self, node, sums):
        if node is None:
            return 0
        curr_sum = (
            node.val +
            self.traverse(node.left, sums) +
            self.traverse(node.right, sums)
        )
        sums[curr_sum] += 1
        return curr_sum

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        sums = defaultdict(int)
        self.traverse(root, sums)
        max_freq = max(sums.values())
        return [s for s, freq in sums.items() if freq == max_freq]


s = Solution()

'''
  5
 /  \
2   -3
'''
res = s.findFrequentTreeSum(TreeNode(5, left=TreeNode(2), right=TreeNode(-3)))
print(res)
assert sorted(res) == sorted([2, -3, 4])
print('OK')

'''
  5
 /  \
2   -5
'''
res = s.findFrequentTreeSum(TreeNode(5, left=TreeNode(2), right=TreeNode(-5)))
print(res)
assert sorted(res) == sorted([2])
print('OK')