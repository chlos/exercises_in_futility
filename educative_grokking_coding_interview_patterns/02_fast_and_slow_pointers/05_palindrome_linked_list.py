#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # reverse the 2nd half of linked list
    # space O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        # find the mid node; reverse the second half of list after that node
        first_half_end = self.get_mid_node(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # check palindrome
        is_palindrome = True
        left_node = head
        right_node = second_half_start
        while is_palindrome and right_node is not None:
            if left_node.val != right_node.val:
                is_palindrome = False
            left_node = left_node.next
            right_node = right_node.next

        # restore the list
        self.reverse_list(second_half_start)

        return is_palindrome

    def get_mid_node(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev