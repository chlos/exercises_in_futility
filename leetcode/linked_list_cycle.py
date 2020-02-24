#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycleHash(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next is None:
            return False

        node = head
        visited = set()
        visited.add(node)
        while node.next is not None:
            if node.next in visited:
                return True
            visited.add(node.next)
            node = node.next

        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next is None:
            return False

        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True

        return False


# s = Solution()
# node = ListNode(1)
# r = s.hasCycle(node)
# assert r == False
