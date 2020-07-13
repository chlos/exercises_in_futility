#!/usr/bin/env python3

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder_recur(self, root: 'Node') -> List[int]:
        def traverse(node, path):
            if node is None:
                return

            path.append(node.val)
            for child in node.children:
                traverse(child, path)

        result = []
        traverse(root, result)
        return result

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return

        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            # stack.extend(reversed(node.children))     # slower
            for child in reversed(node.children):
                stack.append(child)
        return result