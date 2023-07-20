from linked_list import LinkedList
from linked_list_node import LinkedListNode


def getMidNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def reorder_list(head):
    mid_node = getMidNode(head)
    reverse_head = reverseList(mid_node)

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

    return head