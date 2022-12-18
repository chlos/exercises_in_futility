import collections


class Solution:
    # Multiple DFS Traversals
    def findRedundantConnection_DFS(self, edges: List[List[int]]) -> List[int]:
        def is_already_connected(u, v):
            if u == v:
                return True
            
            for node in graph[u]:
                if not visited[node]:
                    visited[node] = True
                    if is_already_connected(node, v):
                        return True
            
            return False

        # We will construct the graph by adding edges one after another.
        # After each addition , we will do a dfs traversal to check if any cycle has formed. 
        # In case of cycle, we know that the last edge addition has led to the formation of cycle 
        # so will simply return that edge.
        graph = collections.defaultdict(set)
        for u, v in edges:
            visited = collections.defaultdict(bool)
            if is_already_connected(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

        return []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            # find the first edge occurring in the graph that is already connected
            if not dsu.union(*edge):
                return edge

        return []


class DSU():
    def __init__(self):
        self.parent = {}
        
    def find(self, w):
        if w not in self.parent:
            self.parent[w] = w
        # path compression
        while w in self.parent and self.parent[w] != w:
            self.parent[w] = self.find(self.parent[w])
            w = self.parent[w]
        return w

    def union(self, k1, k2):
        set1 = self.find(k1)
        set2 = self.find(k2)
        if set1 == set2:
            return False

        if set1 != set2:
            self.parent[set1] = set2
        return True