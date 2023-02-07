from linked_list import LinkedList

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

def reverse_even_length_groups(head):
  node_before_even_group = head
  node = head.next    # [head] is the first odd group

  curr_group_len = 0
  prev_group_len = 1

  while node is not None:
      curr_group_len += 1
      if curr_group_len > prev_group_len or node.next is None:
          # even group
          if curr_group_len % 2 == 0:
              node_next = node.next
              rev_group_head, rev_group_tail = reverse_k(
                  node_before_even_group.next, curr_group_len
              )
              node_before_even_group.next = rev_group_head
              rev_group_tail.next = node_next
              node = rev_group_tail

          curr_group_len = 0
          prev_group_len += 1
          node_before_even_group = node

      node = node.next

  return head