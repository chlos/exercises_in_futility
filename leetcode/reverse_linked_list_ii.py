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


# my solution (basically it uses "reverse K nodes" function like in "reverse nodes in k group")
class Solution:
    def reverseKList(self, head, k):
        reversed_head = None
        reversed_tail = head

        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            print('swap: ', prev, curr, next)
            curr.next = prev
            prev = curr
            curr = next
        reversed_head = prev
        print('reversed head:', reversed_head)

        return reversed_head, reversed_tail

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        k = right - left + 1
        print('k:', k)
        if k == 1:
            return head

        node_before_reversed_head = None
        head_to_reverse = None
        node_after_reversed_tail = None

        i = 1
        node = head
        while node is not None:
            if left == 1 and i == left:
                node_before_reversed_head = None
                head_to_reverse = node
                print('left-1:', node_before_reversed_head)
                print('left:', head_to_reverse.val, ' (start reverse)')
            elif i == left - 1:
                node_before_reversed_head = node
                head_to_reverse = node_before_reversed_head.next
                print('left-1:', node_before_reversed_head.val)
                print('left:', head_to_reverse.val, ' (start reverse)')

            if node.next is None and i == right:
                node_after_reversed_tail = None
                print('right+1:', node_after_reversed_tail)
            elif i == right + 1:
                node_after_reversed_tail = node
                print('right+1:', node_after_reversed_tail.val)
                break
    
            node = node.next
            i += 1

        reversed_head, reversed_tail = self.reverseKList(head_to_reverse, k)
        if node_before_reversed_head is not None:
            node_before_reversed_head.next = reversed_head
        else:
            head = reversed_head
        reversed_tail.next = node_after_reversed_tail

        return head