# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        node_k = None
        node = head
        while node:
            n += 1
            if n == k:
                node_k = node
            node = node.next

        k_end = n - k + 1

        node_k_end = head
        for _ in range(k_end-1):
            node_k_end = node_k_end.next

        node_k.val, node_k_end.val = node_k_end.val, node_k.val

        return head