#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DLLNode(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        out = '"'
        curr_node = self.head
        while curr_node is not None:
            out += str(curr_node.value)
            curr_node = curr_node.next
        out += '"'
        return out

    def push_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
            return

        node.prev = None
        node.next = self.head

        self.head.prev = node
        self.head = node

    def pop_tail(self):
        return self.pop(self.tail)

    def pop(self, node):
        if self.head is None:
            # empty list
            return

        if node.prev is None and node.next is None:
            # rm single node
            self.head = None
            self.tail = None
        elif node.prev is None:
            # rm head
            next_node = node.next
            next_node.prev = None
            self.head = next_node
        elif node.next is None:
            # rm tail
            prev_node = node.prev
            prev_node.next = None
            self.tail = prev_node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current_len = 0

        # key: (value, list_node)
        self.cache = {}
        self.keys_list = DLList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        value, node = self.cache[key]
        self.keys_list.pop(node)
        self.keys_list.push_to_head(node)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            old_value, node = self.cache[key]
            self.cache[key] = value, node
            self.keys_list.pop(node)
            self.keys_list.push_to_head(node)
            return

        if self.current_len >= self.capacity:
            tail_node = self.keys_list.pop_tail()
            self.current_len -= 1
            del self.cache[tail_node.value]
        new_node = DLLNode(key)
        self.keys_list.push_to_head(new_node)
        self.cache[key] = value, new_node
        self.current_len += 1


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(keya
    # obj.put(key,value)

    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    cache = LRUCache(2)

    cache.put(1, 1)     # (1, 1)
    print cache.keys_list

    cache.put(2, 2)     # (2, 2) (1, 1)
    print cache.keys_list

    r = cache.get(1)  # 1 : (1, 1) (2, 2)
    print r
    print cache.keys_list
    assert r == 1

    cache.put(3, 3)     # (3, 3) (1, 1)
    print cache.keys_list

    r = cache.get(2)  # -1 : (3, 3) (1, 1)
    print r
    print cache.keys_list
    assert r == -1

    cache.put(4, 4)     # (4, 4) (3, 3)
    print cache.keys_list

    r = cache.get(1)    # -1
    print r
    print cache.keys_list
    assert r == -1

    r = cache.get(3)    # 3 (3, 3) (4, 4)
    print r
    print cache.keys_list
    assert r == 3

    r = cache.get(4)    # 4 (4, 4) (3, 3)
    print r
    print cache.keys_list
    assert r == 4

    print '\nOK'
