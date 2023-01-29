# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        node_a, node_b = head, head.next
        new_head = node_b
        next = node_b.next
        while node_a is not None and node_b is not None:
            node_b.next = node_a
            node_a.next = next
            if prev is not None:
                prev.next = node_b

            prev = node_a
            node_a = next
            if node_a is not None:
                node_b = node_a.next
            if node_b is not None:
                next = node_b.next

        return new_head