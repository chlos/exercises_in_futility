#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.stack_min = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if x <= self.getMin():
            self.stack_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        pop_element = self.data.pop()
        if pop_element == self.getMin():
            self.stack_min.pop()
        return pop_element

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]
