#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def add_left_child(self, child_node):
        self.left = child_node

    def add_right_child(self, child_node):
        self.right = child_node


class ParseSexp(object):
    def __init__(self, sexp_str):
        self.sexp_tokenized = self._tokenize(sexp_str)
        self.root_node = None
        self._parse()

    def get_parsed(self, pretty=False):
        return self.root_node

    def pretty_print(self):
        current_level = [self.root_node]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            current_level = next_level

    def _handle_scalar_value(self, value):
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return str(value)

    def _tokenize(self, sexp_str):
        sexp_tokenized = sexp_str.replace('(', ' ( ').replace(')', ' ) ').split()
        return sexp_tokenized

    def _parse(self):
        if self.sexp_tokenized[0] == ')':
            self.sexp_tokenized.pop(0)
        current_token = self.sexp_tokenized.pop(0)

        if current_token == '(':
            operator = self.sexp_tokenized.pop(0)

            current_node = TreeNode(operator)
            if self.root_node is None:
                self.root_node = current_node

            current_node.add_left_child(self._parse())
            current_node.add_right_child(self._parse())

            return current_node
        else:
            return TreeNode(self._handle_scalar_value(current_token))


def test(parser):
    sexp = '(+ 3 (* 2 (+ 5 9)))'
    sexp_parsed = parser(sexp)
    sexp_parsed.pretty_print()
    root = sexp_parsed.root_node
    assert root.value == '+'
    assert root.left.value == 3
    assert root.right.value == '*'
    assert root.right.left.value == 2
    assert root.right.right.value == '+'
    assert root.right.right.left.value == 5
    assert root.right.right.right.value == 9
    print 'OK\n'


def test2(parser):
    '''
        +
       /  \
      -    *
     / \   /\
    10 12 2  +
            / \
           5   9
    '''
    sexp = '(+ (- 10 12) (* 2 (+ 5 9)))'
    sexp_parsed = parser(sexp)
    sexp_parsed.pretty_print()
    root = sexp_parsed.root_node
    assert root.value == '+'
    assert root.left.value == '-'
    assert root.left.left.value == 10
    assert root.left.right.value == 12
    assert root.right.value == '*'
    assert root.right.left.value == 2
    assert root.right.right.value == '+'
    assert root.right.right.left.value == 5
    assert root.right.right.right.value == 9
    print 'OK\n'


def main():
    test(ParseSexp)
    test2(ParseSexp)


if __name__ == '__main__':
    main()
