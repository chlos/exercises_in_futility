#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


class LRUCache(object):
    def __init__(self, func, cache_size):
        self.func = func

        self.cache_size = cache_size
        self.cache = {}
        self.keys_queue = deque()

    def do(self, key):
        # hit
        if key in self.cache:
            # promote a key
            self.keys_queue.remove(key)
            self.keys_queue.appendleft(key)

            return self.cache[key]
        # miss
        else:
            func_result = self.func(key)

            # a new key has max prio + new cache entry
            if len(self.keys_queue) > self.cache_size - 1:
                lru_key = self.keys_queue.pop()
                del self.cache[lru_key]
            self.cache[key] = func_result
            self.keys_queue.appendleft(key)

            return func_result


def heavy_calculations(k):
    return k * 1000


def test(test_lru, test_func):
    cached = LRUCache(heavy_calculations, 3)

    # miss
    test_key = 1
    cached_result = cached.do(test_key)
    func_result = heavy_calculations(test_key)
    assert cached_result == func_result
    assert cached.cache == {1: 1000}
    assert cached.keys_queue == deque([1])

    # miss
    test_key = 2
    cached_result = cached.do(test_key)
    func_result = heavy_calculations(test_key)
    assert cached_result == func_result
    assert cached.cache == {1: 1000, 2: 2000}
    assert cached.keys_queue == deque([2, 1])

    # miss
    test_key = 3
    cached_result = cached.do(test_key)
    func_result = heavy_calculations(test_key)
    assert cached_result == func_result
    assert cached.cache == {1: 1000, 2: 2000, 3: 3000}
    assert cached.keys_queue == deque([3, 2, 1])

    # miss + cache size limit
    test_key = 4
    cached_result = cached.do(test_key)
    func_result = heavy_calculations(test_key)
    assert cached_result == func_result
    assert cached.cache == {2: 2000, 3: 3000, 4: 4000}
    assert cached.keys_queue == deque([4, 3, 2])

    # hit
    test_key = 2
    cached_result = cached.do(test_key)
    func_result = heavy_calculations(test_key)
    assert cached_result == func_result
    assert cached.cache == {2: 2000, 3: 3000, 4: 4000}
    assert cached.keys_queue == deque([2, 4, 3])

    print 'OK'


def main():
    test(LRUCache, heavy_calculations)


if __name__ == '__main__':
    main()
