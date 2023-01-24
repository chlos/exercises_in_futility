from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def reverseKList(head, k):
  reversed_head = None
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

def reverse_between(head, left, right):
  k = right - left + 1
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
      elif i == left - 1:
          node_before_reversed_head = node
          head_to_reverse = node_before_reversed_head.next

      if node.next is None and i == right:
          node_after_reversed_tail = None
      elif i == right + 1:
          node_after_reversed_tail = node
          break

      node = node.next
      i += 1

  reversed_head, reversed_tail = reverseKList(head_to_reverse, k)
  if node_before_reversed_head is not None:
      node_before_reversed_head.next = reversed_head
  else:
      head = reversed_head
  reversed_tail.next = node_after_reversed_tail

  return head