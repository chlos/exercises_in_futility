class Solution:
    def areSentencesSimilarTwo_DFS(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        # build a undirected graph
        adj_list = collections.defaultdict(list)
        for sim1, sim2 in similarPairs:
            adj_list[sim1].append(sim2)
            adj_list[sim2].append(sim1)

        for w1, w2 in zip(sentence1, sentence2):
            # dfs: check similarity
            stack = [w1]
            visited = {w1}
            is_simiral = False
            while stack:
                curr_word = stack.pop()
                if curr_word == w2:
                    is_simiral = True
                    break
                for adj_word in adj_list[curr_word]:
                    if adj_word in visited:
                        continue
                    stack.append(adj_word)
                    visited.add(curr_word)
                
            # the current w1-w2 pair is not simiral
            if not is_simiral:
                return False

        return True

    # DSU
    # https://cp-algorithms.com/data_structures/disjoint_set_union.html#path-compression-optimization
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        dsu = DSU()
        for sim_w1, sim_w2 in similarPairs:
            dsu.union(sim_w1, sim_w2)

        for w1, w2 in zip(sentence1, sentence2):
            w1_set, w2_set = dsu.find(w1), dsu.find(w2)
            if w1_set != w2_set:
                return False
            
        return True


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
        if set1 != set2:
            self.parent[set1] = set2