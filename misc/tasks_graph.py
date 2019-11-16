#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


def has_cycle_recur(graph, node, visited, recur_stack):
    visited[node] = True
    recur_stack[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if has_cycle_recur(graph, neighbour, visited, recur_stack):
                return True
        elif recur_stack[neighbour]:
            return True

    recur_stack[node] = False
    return False


def has_cycle(graph, n_verticles):
    visited = [False] * n_verticles
    recur_stack = [False] * n_verticles
    for node in xrange(n_verticles):
        if not visited[node]:
            if has_cycle_recur(graph, node, visited, recur_stack):
                return True
    return False


def has_cycle_recur_color(graph, node, colors):
    colors[node] = 'grey'
    for neighbor in graph[node]:
        if colors[neighbor] == 'grey':
            return True
        elif colors[neighbor] == 'white':
            if has_cycle_recur_color(graph, neighbor, colors):
                return True

    colors[node] = 'black'
    return False


def has_cycle_color(graph, n_verticles):
    colors = ['white'] * n_verticles
    for node in xrange(n_verticles):
        if colors[node] == 'white':
            if has_cycle_recur_color(graph, node, colors):
                return True
    return False


def test(func):
    graph_with_cycle = defaultdict(list)
    graph_with_cycle[0].append(1)
    graph_with_cycle[0].append(2)
    graph_with_cycle[1].append(2)
    graph_with_cycle[2].append(0)
    graph_with_cycle[2].append(3)
    graph_with_cycle[3].append(3)

    assert has_cycle(graph_with_cycle, 4) == True
    print func, 'Graph with cycle: OK'

    graph_wo_cycle = defaultdict(list)
    graph_wo_cycle[0].append(1)
    graph_wo_cycle[0].append(2)

    assert has_cycle(graph_wo_cycle, 3) == False
    print func, 'Graph w/o cycle: OK'


def main():
    test(has_cycle)
    test(has_cycle_color)


if __name__ == '__main__':
    main()
