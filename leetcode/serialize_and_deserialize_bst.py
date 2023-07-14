# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # dfs, post-order
    def _dfs(self, node):
        if node is None:
            return

        left_val = self._dfs(node.left)
        if left_val is not None:
            self.stream.append(left_val)
        right_val = self._dfs(node.right)
        if right_val is not None:
            self.stream.append(right_val)
        self.stream.append(node.val)

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        self.stream = []
        self._dfs(root)
        data = ",".join(map(str, self.stream))
        print(f"serialized: {data}")
        return data

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""

        def helper(lower=float("-inf"), upper=float("inf")):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            node = TreeNode(val)
            node.right = helper(val, upper)
            node.left = helper(lower, val)
            return node

        data = [int(x) for x in data.split(",") if x]
        return helper()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
