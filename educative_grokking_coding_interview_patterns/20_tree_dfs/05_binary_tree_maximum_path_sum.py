# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")

        def subtree_gain(node):
            nonlocal max_sum

            # base case
            if node is None:
                return 0

            left_subtree_gain = max(subtree_gain(node.left), 0)
            right_subtree_gain = max(subtree_gain(node.right), 0)
            max_sum = max(max_sum, left_subtree_gain + node.val + right_subtree_gain)

            return max(
                left_subtree_gain + node.val,
                right_subtree_gain + node.val
            )

        subtree_gain(root)
        return max_sum