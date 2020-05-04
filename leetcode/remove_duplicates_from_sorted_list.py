#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesDict(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        freqs = defaultdict(int)
        prev_node = None
        curr_node = head
        while curr_node:
            print curr_node.val
            freqs[curr_node.val] += 1
            if freqs[curr_node.val] > 1:
                print 'duplicate!'
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                continue

            print 'no dups, get next node'
            next_node = curr_node.next
            prev_node = curr_node
            curr_node = next_node

        return head

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev_node = head
        curr_node = head.next
        while curr_node:
            print curr_node.val
            if prev_node.val == curr_node.val:
                print 'duplicate!'
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                continue

            print 'no dups, get next node'
            next_node = curr_node.next
            prev_node = curr_node
            curr_node = next_node

        return head
