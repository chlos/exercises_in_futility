#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # two pass
    def removeNthFromEnd_twoPass(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        node = head
        list_len = 0
        while node:
            list_len += 1
            node = node.next
        rm_i = list_len - n + 1

        dummy = ListNode(None)
        dummy.next = head
        curr_i = 0
        node = dummy
        while node.next:
            if curr_i == rm_i - 1:
                node.next = node.next.next
                return dummy.next
            node = node.next
            curr_i += 1

    # one pass: two pointers
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(None)
        dummy.next = head
        l_node = r_node = dummy
        i_diff = 0
        while r_node.next:
            r_node = r_node.next
            i_diff += 1
            if i_diff > n:
                l_node = l_node.next

        l_node.next = l_node.next.next
        return dummy.next