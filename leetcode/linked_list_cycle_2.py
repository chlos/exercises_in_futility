#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycleHash(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return None

        node = head
        visited = set()
        visited.add(node)
        while node.next is not None:
            if node.next in visited:
                return node.next
            visited.add(node.next)
            node = node.next

        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return None

        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                head_ptr = head
                while head_ptr != slow_ptr:
                    head_ptr = head_ptr.next
                    slow_ptr = slow_ptr.next
                return slow_ptr

        return None
