#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.indexes = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data.append(val)
        self.indexes[val].add(len(self.data) - 1)
        return len(self.indexes[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.indexes[val]:
            return False

        idx = self.indexes[val].pop()
        last_val = self.data[-1]
        self.data[idx] = last_val
        if self.indexes[last_val]:
            self.indexes[last_val].add(idx)
            self.indexes[last_val].discard(len(self.data) - 1)
        self.data.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.data)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
