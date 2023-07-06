import heapq


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # dfs ; keep 2 longest paths for current node in priority queue
    def diameter_pq(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node):
            pq = []
            for child in node.children:
                child_longest_path = 1 + longest_path(child)
                heapq.heappush(pq, child_longest_path)
                # keep 2 longest paths
                if len(pq) > 2:
                    heapq.heappop(pq)
            if not pq:
                return 0

            nonlocal diameter
            diameter = max(diameter, sum(pq))

            return max(pq)

        longest_path(root)
        return diameter

    # dfs ; track 1st and 2nd longest paths w/o additional structs
    def diameter(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node):
            max_1 = 0
            max_2 = 0
            for child in node.children:
                child_longest_path = 1 + longest_path(child)
                if child_longest_path > max_1:
                    max_1, max_2 = child_longest_path, max_1
                elif child_longest_path > max_2:
                    max_2 = child_longest_path

            nonlocal diameter
            diameter = max(diameter, max_1 + max_2)

            return max(max_1, max_2)

        longest_path(root)
        return diameter
