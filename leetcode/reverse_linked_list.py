#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        def reverseListRecurse(head, prev):
            if head is None:
                return prev
            next = head.next
            head.next = prev
            return reverseListRecurse(next, head)

        return reverseListRecurse(head, None)

    def reverseListIterative(self, head):
        prev_node = None
        curr_node = next_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node

    def reverseListIterativeSlow(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes_stack = []
        current_node = head
        while current_node is not None:
            nodes_stack.append(current_node)
            current_node = current_node.next

        if not nodes_stack:
            return None

        reversed_list_head = nodes_stack.pop()
        prev_node = reversed_list_head
        current_node = None
        while nodes_stack:
            current_node = nodes_stack.pop()
            prev_node.next = current_node
            prev_node = current_node
        if current_node is None:
            reversed_list_head.next = None
        else:
            current_node.next = None

        return reversed_list_head
