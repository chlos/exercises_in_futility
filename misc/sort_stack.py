#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.stack[-1]


def test_stack():
    s = Stack()
    assert s.size == 0

    s.push(1)
    assert s.size == 1
    assert s.peek() == 1
    s.push(2)
    assert s.size == 2
    assert s.peek() == 2

    val = s.pop()
    assert val == 2
    assert s.size == 1
    val = s.pop()
    assert val == 1
    assert s.size == 0
    try:
        exception_raised = False
        val = s.pop()
    except IndexError:
        exception_raised = True
    assert exception_raised

    print 'Stack OK'


def sort_stack(stack):
    stack_size = stack.size
    tmp_stack = Stack()
    for i in xrange(stack_size):
        curr_max = float('-inf')
        for j in xrange(i, stack_size):
            val = stack.pop()
            tmp_stack.push(val)
            if val > curr_max:
                curr_max = val

        stack.push(curr_max)

        max_val_visited = False
        for j in xrange(i, stack_size):
            val = tmp_stack.pop()
            if not max_val_visited and val == curr_max:
                max_val_visited = True
                continue
            stack.push(val)


def test_sort_stack():
    s = Stack()
    sort_stack(s)
    assert s.stack == []

    s = Stack()
    s.push(1)
    sort_stack(s)
    assert s.stack == [1]

    s = Stack()
    s.push(1)
    s.push(2)
    sort_stack(s)
    assert s.stack == [2, 1]

    s = Stack()
    s.push(2)
    s.push(1)
    sort_stack(s)
    assert s.stack == [2, 1]

    s = Stack()
    s.push(1)
    s.push(1)
    sort_stack(s)
    assert s.stack == [1, 1]

    s = Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    sort_stack(s)
    assert s.stack == [3, 2, 1]

    s = Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    s.push(1)
    s.push(10)
    s.push(3)
    s.push(2)
    sort_stack(s)
    assert s.stack == [10, 3, 3, 2, 2, 1, 1]

    print 'sort_stack() OK'


def main():
    test_stack()
    test_sort_stack()


if __name__ == "__main__":
    main()
