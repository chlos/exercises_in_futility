#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # dummy head
    def removeElements_dummyHead(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head

        prev_node = dummy
        curr_node = dummy.next
        while curr_node is not None:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = prev_node.next
            curr_node = curr_node.next

        return dummy.next

    # dummy head: shorter
    def removeElements_dummyHeadShort(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head

        curr_node = dummy
        while curr_node.next is not None:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return dummy.next

    # recursion
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head