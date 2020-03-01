#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # brute force, n**2
    def getIntersectionNodeBruteForce(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_a = headA
        node_b = headB
        while node_a:
            while node_b:
                if node_a == node_b:
                    return node_a
                node_b = node_b.next
            node_a = node_a.next
            node_b = headB

        return None

    # hashmap
    def getIntersectionNodeHashMap(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = {}
        node = headA
        while node:
            visited[node] = True
            node = node.next
        node = headB
        while node:
            if node in visited:
                return node
            node = node.next
        return node

    # magic
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node_1, node_2 = headA, headB
        while node_1 != node_2:
            if node_1 is not None:
                node_1 = node_1.next
            else:
                node_1 = headB
            if node_2 is not None:
                node_2 = node_2.next
            else:
                node_2 = headA
        return node_1
