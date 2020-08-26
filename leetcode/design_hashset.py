#!/usr/bin/env python3


# https://en.wikipedia.org/wiki/Hash_table


# Separate chaining + naive hash function
class MyHashSet_chain_naive_hash:
    # N_BUCKETS = 100
    N_BUCKETS = 1000000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [[]] * self.N_BUCKETS

    def _count_hash(self, val):
        return val % self.N_BUCKETS

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        n_bucket = self._count_hash(key)
        self.buckets[n_bucket].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        n_bucket = self._count_hash(key)
        self.buckets[n_bucket].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        n_bucket = self._count_hash(key)
        return key in self.buckets[n_bucket]


# Separate chaining + Multiplicative hashing
class MyHashSet_chain_mult_hash:
    N_BUCKETS = 1 << 15

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [[]] * self.N_BUCKETS

    def _count_hash(self, key):
        # some big odd number (sometimes good idea to use prime number)
        a = 77377
        return ((key * a) & (1 << 20) - 1) >> 5

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        n_bucket = self._count_hash(key)
        self.buckets[n_bucket].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        n_bucket = self._count_hash(key)
        self.buckets[n_bucket].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        n_bucket = self._count_hash(key)
        return key in self.buckets[n_bucket]


# Separate chaining + Multiplicative hashing + Linked List
class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class MyHashSet:
    N_BUCKETS = 1 << 15

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * self.N_BUCKETS

    def _count_hash(self, key):
        # some big odd number (sometimes good idea to use prime number)
        a = 77377
        return ((key * a) & (1 << 20) - 1) >> 5

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        n_bucket = self._count_hash(key)
        node = self.buckets[n_bucket]
        new_node = ListNode(key, next=node)
        self.buckets[n_bucket] = new_node

    def remove(self, key: int) -> None:
        n_bucket = self._count_hash(key)
        node = self.buckets[n_bucket]
        if node is None:
            return
        if node.key == key:
            self.buckets[n_bucket] = node.next
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        n_bucket = self._count_hash(key)
        node = self.buckets[n_bucket]
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False


# open addressing
# https://leetcode.com/problems/design-hashset/discuss/210494/Real-Python-Solution-no-cheating-open-addressing
# FIXME


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)