import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution_preCalcLen:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        self.len = 0
        curr_node = head
        while curr_node is not None:
            self.len += 1
            curr_node = curr_node.next

    def getRandom(self) -> int:
        random_i = random.randint(0, self.len - 1)
        node = self.head
        for i in range(random_i):
            node = node.next
        
        return node.val


# reservoir sampling
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = 0

        node = self.head
        scope = 1
        while node:
            if random.random() < (1 / scope):
                result = node.val
            node = node.next
            scope += 1

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()