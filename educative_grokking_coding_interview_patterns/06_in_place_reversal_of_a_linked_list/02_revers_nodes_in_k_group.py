import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def reverse_k(head, k):
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


def reverse_linked_list(head, k):
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
            reversed_head, reversed_tail = reverse_k(k_head, k)
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