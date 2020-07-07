#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
    def reverseBetween_1(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        l_node = dummy = ListNode()
        dummy.next = head
        for _ in range(m - 1):
            l_node = l_node.next

        local_tail = l_node.next
        for _ in range(n - m):
            tmp_node = l_node.next
            l_node.next = local_tail.next
            local_tail.next = local_tail.next.next
            l_node.next.next = tmp_node

        return head