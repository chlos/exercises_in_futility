# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(node, arr):
    if node is None:
        return
    inorder(node.left, arr)
    arr.append(node.val)
    inorder(node.right, arr)

class Solution:
    def kthSmallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
       bst_arr = []
       inorder(root, bst_arr)

       return bst_arr[k - 1]

    # iterative inorder traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            i += 1
            if i == k:
                return node.val

            node = node.right