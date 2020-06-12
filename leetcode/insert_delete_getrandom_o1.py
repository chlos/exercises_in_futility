#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from collections import deque


# O(N)
class RandomizedSet_Linear(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            self.data[val] = 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            del(self.data[val])
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data.keys())


# O(1) with list
# see the: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
class RandomizedSet_DictList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.indexes = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indexes:
            self.data.append(val)
            self.indexes[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexes:
            idx = self.indexes[val]
            last_val = self.data[-1]
            self.data[idx] = last_val
            self.indexes[last_val] = idx
            self.data.pop()
            del self.indexes[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data)


# O(1) with deque
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.indexes = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indexes:
            self.data.append(val)
            self.indexes[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexes:
            idx = self.indexes[val]
            last_val = self.data[-1]
            self.data[idx] = last_val
            self.indexes[last_val] = idx
            self.data.pop()
            del self.indexes[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
