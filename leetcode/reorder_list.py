# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def getMidNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # reverse the second
        mid_node = self.getMidNode(head)
        reverse_head = self.reverseList(mid_node)

        # merge
        normal_node = head
        reverse_node = reverse_head
        while reverse_node.next:
            normal_next = normal_node.next
            normal_node.next = reverse_node
            normal_node = normal_next

            reverse_next = reverse_node.next
            reverse_node.next = normal_node
            reverse_node = reverse_next