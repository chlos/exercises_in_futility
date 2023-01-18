# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_k(self, head, k):
        reversed_tail = head
    
        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        reversed_head = prev
        return reversed_head, reversed_tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
 
        new_head = None # result

        curr = head
        k_head = head   # head of each k-list
        reversed_tail = None
        i = 1
        while curr is not None:
            next = curr.next
            if i == k:
                prev_reversed_tail = reversed_tail
                reversed_head, reversed_tail = self.reverse_k(k_head, k)
                # connect previous nodes with k-list head
                if prev_reversed_tail is not None:
                    prev_reversed_tail.next = reversed_head
                # connect tail of reversed k-list with the remaining nodes
                curr = reversed_tail
                curr.next = next
                # new candidate for k-list head
                k_head = next

                if new_head is None:
                    new_head = reversed_head

                # reset the k counter
                i = 0

            # keep traversing list
            curr = curr.next
            i += 1

        return new_head