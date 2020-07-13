#!/usr/bin/env python3

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder_recursion(self, root: 'Node') -> List[int]:
        def traverse(node, path):
            if not node:
                return

            for child in node.children:
                traverse(child, path)
            path.append(node.val)

        result = []
        traverse(root, result)
        return result

    # iterative: postorder is reversed preorder (DIRTY HACK)
    def postorder_iter_reverse(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in node.children:
                stack.append(child)

        return result[::-1]

    # iterative: one stack
    def postorder_iter_1(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result

        stack = [root]
        prev_node = None
        while stack:
            peek_node = stack[-1]

            is_leaf = not peek_node.children
            is_done = not is_leaf and peek_node.children[-1] == prev_node

            if is_leaf or is_done:
                result.append(peek_node.val)
                prev_node = peek_node
                stack.pop()
            else:
                for child in reversed(peek_node.children):
                    stack.append(child)

        return result

    # iterative
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return result