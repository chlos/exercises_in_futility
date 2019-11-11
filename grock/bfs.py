#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


# breadth-first search
def search(graph, start_node, is_found):
    search_queue = collections.deque()
    search_queue += graph[start_node]
    visited = []

    while search_queue:
        current_node = search_queue.popleft()
        if current_node not in visited:
            if is_found(current_node):
                return current_node
            else:
                search_queue += graph[current_node]
                visited.append(current_node)

    return None


def main():
    graph = collections.defaultdict(list)
    graph['me'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_query = lambda x: x == 'anuj'
    assert search(graph, 'me', search_query) == 'anuj'
    search_query = lambda x: x == 'bob'
    assert search(graph, 'me', search_query) == 'bob'
    search_query = lambda x: x == 'bad_name'
    assert search(graph, 'me', search_query) is None

    print 'OK'

if __name__ == "__main__":
    main()
