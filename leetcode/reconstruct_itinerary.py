#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


class Solution(object):
    start = 'JFK'

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.itinerary = []

    def buildGraph(self, tickets):
        for src, dst in tickets:
            self.graph[src].append(dst)
        print self.graph    # FIXME

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(prev_node, curr_node):
            self.visited.add((prev_node, curr_node))
            self.itinerary.append(curr_node)
            for next_node in self.graph[curr_node]:
                if (curr_node, next_node) not in self.visited:
                    dfs(curr_node, next_node)

        self.buildGraph(tickets)
        dfs(None, self.start)
        print 'visited: ', self.visited  # FIXME
        print 'route: ', self.itinerary  # FIXME

        return self.itinerary


def main():
    s = Solution()
    route = s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    assert route == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print 'test 1 OK'
    print

    s = Solution()
    route = s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    assert route == ["JFK", "NRT", "JFK", "KUL"]


if __name__ == "__main__":
    main()
