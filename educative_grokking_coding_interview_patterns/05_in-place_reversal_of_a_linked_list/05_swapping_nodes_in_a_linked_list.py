from linked_list import LinkedList
from linked_list_node import LinkedListNode
from swap_two_nodes import swap

def swap_nodes(head, k):
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

    node_k.data, node_k_end.data = node_k_end.data, node_k.data

    return head