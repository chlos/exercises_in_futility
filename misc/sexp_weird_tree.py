# import requests
# import mysql.connector
# import pandas as pd

# Given an input string like "(* 2 3 (+ 4 1) 7)"
#
# Parse it into a binary tree containing each element in left leaf nodes, like
# this:
#
#
#       ()
#      /  \
#    (*)  ()
#        /  \
#      (2)  ()
#          /  \
#        (3)  ()
#            /  \
#           /   ()
#          /   /  \
#         /  (7)  (NIL)
#        ()    \
#       /  \   (NIL)
#     (+)  ()
#         /  \
#       (4)  ()
#           /  \
#         (1)  (NIL)

# "(a b c (d e f) g )"
# (a b c)


# "( a ( b c ) )"


def tokenize(s):
    exp = s.split()
    return exp


class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def __repr__(self):
        val = f'val: {self.value}'
        if self.left is None or isinstance(self.left, str):
            left = f'left: {self.left}'
        else:
            left = 'l: (...)'
        if self.right is None or isinstance(self.right, str):
            right = f'right: {self.right}'
        else:
            right = 'r: (...)'

        return f'{val} ; {left} ; {right}'


def parse_expression(expression, node=None):
    print(expression, node) # DEBUG
    if expression:
        element = expression.pop(0)
    else:
        return None
    if element == ')':
        return None

    print(f'element: {element}')
    if element == '(':
        print('create a node')
        node = Node()
        node.left = expression.pop(0)
        node.right = Node()
        parse_expression(expression, node.right)
        # return
    else:
        print(f'assignt {element} to node')
        node.left = element

    print('assing smth to right sub tree')
    node.right = Node()
    parse_expression(expression, node.right)

    return node


print('Hello')
exp_s = '( a b c )'
'''
  ()      # NODE
  / \
a    ()   # node.right
    / \
    b  ()
       / \
    c     None
'''
exp = tokenize(exp_s)
# print(exp)
root = parse_expression(exp)
print(root)
print(root.left)
print(root.right)
print('OK')
