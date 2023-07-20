# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # my naive solution: merge lists pairwise
    def mergeKLists_pairwise(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged_head = lists[0]
        if len(lists) == 1:
            return merged_head

        for i in range(1, len(lists)):
            # dummy list for the curent merged pair of lists
            dummy_node = ListNode()
            dummy_head = dummy_node

            node1 = merged_head
            node2 = lists[i]
            while node1 or node2:
                if not node2 or (node1 and node1.val < node2.val):
                    dummy_node.next = ListNode(val=node1.val)
                    if node1:
                        node1 = node1.next
                else:
                    dummy_node.next = ListNode(val=node2.val)
                    if node2:
                        node2 = node2.next
                dummy_node = dummy_node.next

            merged_head = dummy_head.next

        return merged_head

    # priority queue
    def mergeKLists_pq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        pq_nodes = []   # (val, node)
        for curr_head in lists:
            if curr_head:
                # we use id() to avoid:
                # https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
                heapq.heappush(pq_nodes, (curr_head.val, id(curr_head), curr_head))

        dummy_head = ListNode()
        dummy_node = dummy_head
        while pq_nodes:
            val, _, node = heapq.heappop(pq_nodes)
            if node.next is not None:
                heapq.heappush(pq_nodes, (node.next.val, id(node.next), node.next))

            dummy_node.next = ListNode(node.val)
            dummy_node = dummy_node.next

        return dummy_head.next

    # pairwise / divide and conquer
    # https://leetcode.com/problems/merge-k-sorted-lists/solutions/10919/python-easy-to-understand-divide-and-conquer-solution/
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge2Lists(l, r)

    def merge2Lists(self, l, r):
        dummy_head = ListNode()
        dummy_node = dummy_head
        while l and r:
            if l.val < r.val:
                dummy_node.next = l
                l = l.next
            else:
                dummy_node.next = r
                r = r.next
            dummy_node = dummy_node.next

        # attach the remaining tail to the merged list
        dummy_node.next = l or r

        return dummy_head.next