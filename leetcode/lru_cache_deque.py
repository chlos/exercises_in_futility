#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.cache_queue = collections.deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        self.cache_queue.remove(key)
        self.cache_queue.appendleft(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.cache_queue.remove(key)
            self.cache_queue.appendleft(key)
            return

        if len(self.cache_queue) >= self.capacity:
            lru_key = self.cache_queue.pop()
            del self.cache[lru_key]
        self.cache[key] = value
        self.cache_queue.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
