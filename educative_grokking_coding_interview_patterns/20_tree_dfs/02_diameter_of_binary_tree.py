from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            # we reached the end of the tree
            if node is None:
                return 0

            # longest paths of left and right sub-trees
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update diameter if this node's left + right paths is larger
            nonlocal diameter
            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter
