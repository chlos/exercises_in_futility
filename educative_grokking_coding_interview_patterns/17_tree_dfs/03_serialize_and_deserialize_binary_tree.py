# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # pre-order dfs
    def _dfs(self, node):
        # append leaf marker to the stream
        if node is None:
            self.stream.append(None)
            return

        # serialize current node
        self.stream.append(node.val)

        # continue pre-order dfs
        self._dfs(node.left)
        self._dfs(node.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.stream = []
        self._dfs(root)
        data = ",".join(map(str, self.stream))
        return data

    def _deserialize(self, stream):
        if not stream:
            return
        val = stream.pop()
        if val == "None":
            return

        node = TreeNode(val)
        node.left = self._deserialize(stream)
        node.right = self._deserialize(stream)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        stream = data.split(",")
        stream.reverse()
        root = self._deserialize(stream)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
