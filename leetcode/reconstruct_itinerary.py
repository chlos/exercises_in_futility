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
            print 'self.graph[{}]: {}'.format(curr_node, sorted(self.graph[curr_node]))       # FIXME
            for next_node in sorted(self.graph[curr_node]):
                if (curr_node, next_node) not in self.visited:
                    dfs(curr_node, next_node)
            self.itinerary.append(curr_node)

        self.buildGraph(tickets)
        dfs(None, self.start)
        print 'visited: ', self.visited  # FIXME
        print 'route: ', self.itinerary[::-1]  # FIXME

        return self.itinerary[::-1]


def main():
    s = Solution()
    route = s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    assert route == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print 'test 1 OK'
    print

    s = Solution()
    route = s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    assert route == ["JFK", "NRT", "JFK", "KUL"]
    print 'test 2 OK'
    print

    s = Solution()
    route = s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
    assert route == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    print 'test 3 OK'
    print

    s = Solution()
    route = s.findItinerary([
        ["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"],
        ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"],
    ])
    assert route == ["JFK", "ANU", "EZE", "AXA", "TIA", "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"]
    print 'test 4 OK'
    print


if __name__ == "__main__":
    main()
