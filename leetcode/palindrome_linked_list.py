#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the half
        left_node = None
        while slow:
            right_node = slow.next
            slow.next = left_node
            left_node = slow
            slow = right_node
        # check halfs
        node_1 = left_node
        node_2 = head
        while node_1:
            if node_1.val != node_2.val:
                return False
            node_1 = node_1.next
            node_2 = node_2.next

        return True
