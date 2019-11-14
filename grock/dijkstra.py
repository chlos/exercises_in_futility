#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

inf = float('inf')


def get_min_cost_node(costs, processed):
    costs_not_processed = {k: v for k, v in costs.iteritems() if k not in processed}
    if not costs_not_processed:
        return None
    return min(costs_not_processed, key=costs.get)


def do_dijkstra(graph, parents, costs):
    print '====='
    processed = []
    node = get_min_cost_node(costs, processed)
    while node is not None:
        print 'node: ', node
        cost = costs[node]
        print 'cost: ', cost
        neighbors = graph[node]
        print 'neighbors: ', neighbors
        for neighbor in neighbors.iterkeys():
            new_cost = cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                print 'new cost {}: {}'.format(neighbor, new_cost)
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.append(node)
        node = get_min_cost_node(costs, processed)


def main():
    '''
            (A)
            ^^\
           / | 1
          6  |  \
         /   |   v
    (begin)  3  (end)
        \   |    ^
         2   |  /
          \  | 5
           v |/
           (B)
    '''

    graph = collections.defaultdict(dict)
    graph['begin']['a'] = 6
    graph['begin']['b'] = 2
    graph['a']['end'] = 1
    graph['b']['a'] = 3
    graph['b']['end'] = 5
    graph['end'] = {}
    print 'graph: ', graph

    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['end'] = inf
    print 'costs: ', costs

    parents = {}
    parents['a'] = 'begin'
    parents['b'] = 'begin'
    parents['end'] = None
    print 'parents: ', parents

    do_dijkstra(graph, parents, costs)
    print 'costs: ', costs
    print 'parents: ', parents


if __name__ == '__main__':
    main()
