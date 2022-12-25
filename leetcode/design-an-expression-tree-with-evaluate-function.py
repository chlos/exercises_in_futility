# nice example: https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/solutions/959686/extensible-clean-and-concise-python-oop-implementation/

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class ExpTreeNode(Node):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        # evaluate is basically a DFS process, all digits are at leaf nodes;
        # otherwise we will calculate the result recursively
        if self.val.isdigit():
            return self.val
        else:
            # val is operator
            op = self.val
            l = self.left.evaluate()
            r = self.right.evaluate()
            return Evaluator.do(l, r, op)


class Evaluator():
    apply = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }

    @staticmethod
    def do(a, b, op):
        return Evaluator.apply[op](int(a), int(b))


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token.isdigit():
                stack.append(ExpTreeNode(token))
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(ExpTreeNode(token, left=b, right=a))

        # if you did everything right, you are always guranteed to have a stack of length 1
        # since everything should have been popped out but the root node
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""