# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # if looking for me, return myself
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left is not None and right is not None:
            return root

        # either one of the chidren returned a node,
        # meaning either p or q found on left or right branch
        return left or right
