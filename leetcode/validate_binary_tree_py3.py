# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive; DFS; with valid range/bounds/limits
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

    # iterative; DFS; with valid range/bounds/limits
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # node, lower_limit, upper_limit
        stack = [(root, -float("inf"), float("inf"))]

        while stack:
            node, lower_limit, upper_limit = stack.pop()

            if node is None:
                continue

            if node.val <= lower_limit or node.val >= upper_limit:
                return False

            stack.append((node.left, lower_limit, node.val))
            stack.append((node.right, node.val, upper_limit))

        return True

    # recursive; inorder: left-node-right
    def isValidBST_recursiveInorder(self, root: Optional[TreeNode]) -> bool:
        def isValidRecur(node):
            if node is None:
                return True

            if not isValidRecur(node.left):
                return False

            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val

            return isValidRecur(node.right)

        self.prev_val = -float("inf")
        return isValidRecur(root)

    # iterative; Iterative Inorder Traversal
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
