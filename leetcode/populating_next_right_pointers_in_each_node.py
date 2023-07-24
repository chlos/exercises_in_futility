# similar: https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # naive: level traversal + hashmap with levels
    # space: O(2n)
    def connect_hashmap(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        levels = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])  # (node, level)
        while queue:
            node, level = queue.popleft()
            levels[level].append(node)
            if node and node.left:
                queue.append((node.left, level + 1))
            if node and node.right:
                queue.append((node.right, level + 1))

        for nodes_level in levels.values():
            for i in range(len(nodes_level) - 1):
                nodes_level[i].next = nodes_level[i + 1]

        return root

    # Level Order Traversal
    # count queue len
    # space O(n)
    def connect_traversal(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        queue = collections.deque([root])
        while queue:
            q_len = len(queue)

            # Iterate over all the nodes on the current level
            for i in range(q_len):
                node = queue.popleft()
                # This check is important. We don't want to establish any wrong connections.
                # The queue will contain nodes from 2 levels at most at any point in time.
                # This check ensures we only don't establish next pointers beyond the end of a level
                if i < q_len - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

    # Using previously established next pointers: iterative
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        # root is the level 1 only node and the first "linked list"
        # no need to establish connections on level 1
        leftmost = root

        # once we reach the final level, we are done
        while leftmost.left:
            # iterate through the "linked list" of N+1 level nodes
            list_node = leftmost
            while list_node:
                # connection 1
                list_node.left.next = list_node.right
                # connection 2
                if list_node.next:
                    list_node.right.next = list_node.next.left
                # move on in the "linked list"
                list_node = list_node.next

            # go to the next level
            leftmost = leftmost.left

        return root

    # Using previously established next pointers: recursive
    def connect_recur(self, root: "Optional[Node]") -> "Optional[Node]":
        def rec(node, next_node=None):
            if not node:
                return
            node.next = next_node
            rec(node.left, node.right)
            rec(node.right, next_node.left if next_node else None)
            return node

        return rec(root)
