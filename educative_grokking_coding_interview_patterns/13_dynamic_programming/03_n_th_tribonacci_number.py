class Solution:
    # top down/dfs + memo/cache
    def tribonacci_DFS(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 0
            if n < 3:
                return 1

            return dfs(n - 3) + dfs(n - 2) + dfs(n - 1)

        return dfs(n)

    # bottom up
    def tribonacci_bottomUp(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[-1]

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        n1, n2, n3 = 0, 1, 1
        for i in range(3, n + 1):
            n1, n2, n3 = n2, n3, n1 + n2 + n3

        return n3