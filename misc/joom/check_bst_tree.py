#     2
#    /  \
#   1    5
#    \  /
#    3 0

        
        
# Validate BST
def check_bst(node):
    def check_recur(node, parent_node, left_tree=True):
        if left_tree:
            if node.left is None and node.right is None:
                return node.value < parent_node.value
        else:
            if node.left is None and node.right is None:
                return node.value > parent_node.value
        if node.left is not None:
            return check_recur(node.left, node, left_tree=True)
        if node.right is not None:
            return check_recur(node.left, node, left_tree=False)
