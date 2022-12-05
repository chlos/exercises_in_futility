# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        def isValidRecur(node, lower_limit, upper_limit):
            if node is None:
                return True

            if node.val <= lower_limit or node.val >= upper_limit:
                return False

            return (
                isValidRecur(node.left, lower_limit, node.val) and
                isValidRecur(node.right, node.val, upper_limit)
            )

        return isValidRecur(root, -float("inf"), float("inf"))

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = []
        prev_node = None
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if prev_node and prev_node.val >= node.val:
                return False
            prev_node = node
            node = node.right

        return True