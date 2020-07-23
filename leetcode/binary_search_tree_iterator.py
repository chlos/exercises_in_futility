#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# naive: prepare traverse path
class BSTIterator_1:

    def __init__(self, root: TreeNode):
        def traverse(node, path):
            if node is None:
                return
            traverse(node.left, path)
            path.append(node.val)
            traverse(node.right, path)

        self.inorder_nodes = []
        traverse(root, self.inorder_nodes)
        self.idx = -1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.idx += 1
        return self.inorder_nodes[self.idx]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.idx + 1 == len(self.inorder_nodes):
            return False
        return True


# iterative, stack
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left_subtree(root)

    def _push_left_subtree(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self._push_left_subtree(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()