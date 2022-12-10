"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def print_list(head):
    print('___')
    curr_node = head
    while curr_node is not None:
        if curr_node.next is not None:
            curr_node_next = curr_node.next.val
        else:
            curr_node_next = None
        if curr_node.random is not None:
            curr_node_random = curr_node.random.val
        else:
            curr_node_random = None
        print(curr_node.val, curr_node_next, curr_node_random)
        curr_node = curr_node.next
    print()

class Solution_bruteForce:
    # bruteforce / naive / my
    # time: O(N^2); space: O(N)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        new_nodes_arr = []

        # make a copy of linked list without random links
        curr_node = head
        while curr_node is not None:
            new_nodes_arr.append(Node(curr_node.val))
            if len(new_nodes_arr) > 1:
                # add link from prev_node to curr_node
                new_nodes_arr[-2].next = new_nodes_arr[-1]
            curr_node = curr_node.next

        # calculate "indexes" (distance from the tail) of original "random nodes"
        new_node_i = 0
        curr_node = head
        while curr_node is not None:
            random_node = curr_node.random
            random_node_i = 0
            if random_node is not None:
                tmp_node = random_node
                while tmp_node:
                    random_node_i += 1
                    tmp_node = tmp_node.next

                new_nodes_arr[new_node_i].random = new_nodes_arr[-random_node_i]

            curr_node = curr_node.next
            new_node_i += 1

        return new_nodes_arr[0]

class Solution_recursiveGraph:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # already visited
        if head in self.visited:
            return self.visited[head]

        node = Node(head.val)
        self.visited[head] = node
        # recursively find and copy next/random nodes in graph
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

# iterative
# time O(2N); space O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        map = {}
        
        curr_node = head
        while curr_node is not None:
            map[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next

        curr_node = head
        while curr_node is not None:
            if curr_node.next is not None:
                map[curr_node].next = map[curr_node.next]
            if curr_node.random is not None:
                map[curr_node].random = map[curr_node.random]

            curr_node = curr_node.next

        return map[head]