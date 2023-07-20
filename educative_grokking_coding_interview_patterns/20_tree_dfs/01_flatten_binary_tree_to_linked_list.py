# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# post order traversal / tricky magic!
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/36977/my-short-post-order-traversal-java-solution-for-share/
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/37154/8-lines-of-python-solution-reverse-preorder-traversal/
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None

            # save top of prev tree
            self.prev = node

        dfs(root)
