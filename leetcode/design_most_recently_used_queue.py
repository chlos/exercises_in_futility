from sortedcontainers import SortedList


class ListNode():

    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'

    def print(self):
        out = f'{self.val}'
        node = self.next
        while node:
            out += f' -> {node.val}'
            node = node.next
        print(out)

# single linked list
class MRUQueue_SLL:

    def __init__(self, n: int):
        self.dummy_head = ListNode()
        self.tail = None
        node = self.dummy_head
        for v in range(1, n + 1):
            node.next = ListNode(v)
            node = node.next
            self.tail = node

    def fetch(self, k: int) -> int:
        # find kth node
        prev_node = None
        node = self.dummy_head
        for _ in range(k):
            prev_node = node
            node = node.next
            pass

        # do nothing if it's already tail
        if node == self.tail:
            return node.val

        # move kth node to the tail
        prev_node.next = node.next
        self.tail.next = node
        node.next = None
        self.tail = node

        return node.val


# sorted list
# https://leetcode.com/problems/design-most-recently-used-queue/solutions/1061040/python-3-o-log-n-fetch-and-o-n-log-n-constructor-using-sortedlist/
class MRUQueue:

    def __init__(self, n: int):
        # sorted list of (idx, value) tuples
        self.data = SortedList((x - 1, x) for x in range(1, n + 1))

    def fetch(self, k: int) -> int:
        _, value = self.data[k - 1]
        last_idx, _ = self.data[-1]
        del self.data[k - 1]
        self.data.add((last_idx + 1, value))

        return value


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)