from collections import deque, defaultdict


def find_compilation_order(dependencies):
    sorted_order = []

    # build a graph and incoming degrees counter
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    for child, parent in dependencies:
        graph[parent].append(child)
        in_degrees[child] += 1

    # add sources to the queue
    # source: any vertex with no incoming edge and only outgoing edges
    sources = deque([])
    for node in graph:
        if in_degrees[node] == 0:
            sources.append(node)

    # build sorted order list using only sources
    while sources:
        source_node = sources.popleft()
        sorted_order.append(source_node)
        for child_node in graph[source_node]:
            in_degrees[child_node] -= 1
            if in_degrees[child_node] == 0:
                sources.append(child_node)

    return sorted_order
