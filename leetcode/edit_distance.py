class Solution:
    # top down recursive + cheating with lru cache
    # https://leetcode.com/problems/edit-distance/solutions/1475220/python-3-solutions-top-down-dp-bottom-up-dp-o-n-in-space-clean-concise/
    def minDistance_recur(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def recur(idx1, idx2):
            # need to insert idx2 chars
            if idx1 == 0:
                return idx2
            # need to insert idx1 chars
            if idx2 == 0:
                return idx1

            if word1[idx1 - 1] == word2[idx2 - 1]:
                return recur(idx1 - 1, idx2 - 1)

            return min(
                recur(idx1 - 1, idx2),
                recur(idx1, idx2 - 1),
                recur(idx1 - 1, idx2 - 1),
            ) + 1

        return recur(len(word1), len(word2))

    # DP solution, bottom up, iterative
    # https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]