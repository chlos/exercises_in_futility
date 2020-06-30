# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_equal(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.is_equal(s.left, t.left) and self.is_equal(s.right, t.right)

    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        return self.is_equal(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)


sol = Solution()

'''
    3
   / \
  4   5
 / \
1   2
'''
s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
'''
  4
 / \
1   2
'''
t = TreeNode(4, TreeNode(1), TreeNode(2))
assert sol.isSubtree(s, t)
print('OK')

'''
    3
   / \
  4   5
 / \
1   2
   /
  0
'''
s = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
'''
  4
 / \
1   2
'''
t = TreeNode(4, TreeNode(1), TreeNode(2))
assert not sol.isSubtree(s, t)
print('OK')