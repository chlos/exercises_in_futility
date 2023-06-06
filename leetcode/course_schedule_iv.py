import collections
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # build graph
        graph = {node: [] for node in range(numCourses)}
        in_degrees = {node: 0 for node in range(numCourses)}
        pres = collections.defaultdict(set)
        for parent_node, child_node in prerequisites:
            graph[parent_node].append(child_node)
            in_degrees[child_node] += 1
            pres[child_node].add(parent_node)

        # find sources
        sources = collections.deque()
        for node, in_count in in_degrees.items():
            if in_count <= 0:
                sources.append(node)

        # topological sort
        while sources:
            pre_node = sources.popleft()
            for child_node in graph[pre_node]:
                pres[child_node] |= pres[pre_node]
                in_degrees[child_node] -= 1
                if in_degrees[child_node] <= 0:
                    sources.append(child_node)

        return [pre in pres[course] for pre, course in queries]
