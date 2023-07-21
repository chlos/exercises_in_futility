# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def recur(lower=-float("inf"), upper=float("inf")):
            nonlocal idx
            # finished
            if idx == len(preorder):
                return None

            val = preorder[idx]

            # this val doesn't fit BST
            if val < lower or val > upper:
                return None

            root = TreeNode(val)
            # recursively try next vals from preorder arr for l/r subtrees
            idx += 1
            root.left = recur(lower, val)
            root.right = recur(val, upper)

            return root

        idx = 0
        return recur()
